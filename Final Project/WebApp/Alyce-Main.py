import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import boto3

dynamodb = boto3.resource('dynamodb',
                          # ,aws_session_token = aws_session_token,
                          aws_access_key_id = '',
                          aws_secret_access_key = '',
                          region_name = 'us-east-1'
                          )

# Read Alyce Fact data
df_fact = dynamodb.Table('FinalAlyce_facts')
response = df_fact.scan()
df_fact = response['Items']

while 'LastEvaluatedKey' in response:
    response = df_fact.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    df_fact.extend(response['Items'])

df_fact = pd.DataFrame(df_fact)

# Read Alyce Client data
df_client = dynamodb.Table('FinalAlyce_client')
response = df_client.scan()
df_client = response['Items']

while 'LastEvaluatedKey' in response:
    response = df_client.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    df_client.extend(response['Items'])

df_client = pd.DataFrame(df_client)

# Read Alyce Gift data
df_gift = dynamodb.Table('FinalAlyce_giftdata')
response = df_gift.scan()
df_gift = response['Items']

while 'LastEvaluatedKey' in response:
    response = df_gift.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    df_gift.extend(response['Items'])

df_gift = pd.DataFrame(df_gift)


df = pd.merge(df_fact, df_client, how='inner', left_on = 'client_id', right_on = 'client_id')

df = pd.merge(df, df_gift, how='inner', left_on = 'gift_id', right_on = 'gift_id')
df['date'] = pd.to_datetime(df['date'])
df['year'], df['month'] = df['date'].dt.year, df['date'].dt.month

client_name = df['client_name'].unique()
channel = df['client_acquisition_source'].unique()

# Boostrap CSS.
#app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Alyce',
                        className='nine columns'),
                html.Img(
                    className='three columns',
                    style={
                        'height': '9%',
                        'width': '9%',
                        'float': 'right',
                        'position': 'relative',
                        'padding-top': 0,
                        'padding-right': 0
                    },
                ),
                html.Div(children='''
                        A web application for Analytical purpose.
                        ''',
                         className='nine columns'
                         )
            ], className="row"
        ),
        dcc.Graph(id='graph-with-slider'),
        dcc.Slider(
            id='year-slider',
            min=df['year'].min(),
            max=df['year'].max(),
            value=df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            step=None
        ),
        html.Div([
            html.Div([dcc.Dropdown(id='channel-selected1',
                                   options=[{
                                       'label': i,
                                       'value': i
                                   } for i in channel],
                                   value='email')], className="six columns",
                     style={"width": "40%", "float": "right"}),
            html.Div([dcc.Dropdown(id='Clients1',
                                   options=[{
                                       'label': i,
                                       'value': i
                                   } for i in client_name],
                                   value='All')], className="six columns", style={"width": "40%", "float": "left"}),
        ], className="row", style={"padding": 50, "width": "60%", "margin-left": "auto", "margin-right": "auto"}),
        dcc.Graph(id='my-graph'),
    ], className='ten columns offset-by-one')
)

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.gift_name.unique():
        df_by_gift_name = filtered_df[filtered_df['gift_name'] == i]
        traces.append(go.Scatter(
            x=df_by_gift_name['total_revenue'],
            y=df_by_gift_name['total_gifts'],
            #text=df_by_gift_name['client_subscription'],
            mode='markers',
            opacity=0.7,
            # marker={
            #     'size': 15,
            #     'line': {'width': 0.5, 'color': 'white'}
            # },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Gift Cost'},
            yaxis={'title': 'Total Gifts', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('Clients1', 'value'),
     dash.dependencies.Input('channel-selected1','value')])
def update_graph(selected_client, selected_channel):
    if selected_client == "All":
        df_plot = df.copy()
    else:
        df_plot = df[(df['client_name'] == selected_client) & (df['client_acquisition_source'] == selected_channel)]

    #dff = df[selected_client]
    #dff = df[df[selected_sub]]
    trace1 = go.Bar(x=df_plot['client_statecode'], y=df_plot['total_amount'], name="Total Amount" )
    trace2 = go.Bar(x=df_plot['client_statecode'], y=df_plot['total_revenue'], name="Total Revenue" )

    return {
        'data': [trace1,trace2],
        'layout': go.Layout(title='Total Revenue by client',
                            colorway=["#EF963B", "#EF533B"], hovermode="closest",
                            xaxis={'title': "State", 'titlefont': {'color': 'black', 'size': 14},
                                   'tickfont': {'size': 9, 'color': 'black'}}
                            # yaxis={'title': "Export price (million USD)", 'titlefont': {'color': 'black', 'size': 14, },
                            #        'tickfont': {'color': 'black'}}
                            )}

if __name__ == '__main__':
    app.run_server(host = "0.0.0.0", port = 8050)