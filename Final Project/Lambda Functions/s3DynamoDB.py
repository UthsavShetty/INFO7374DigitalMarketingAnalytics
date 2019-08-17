import json
import boto3

s3 = boto3.client('s3')
dynamodb =boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    obj = s3.get_object(Bucket=bucket, Key=key)
    
    rows = obj['Body'].read().decode("utf-8").split ('\n')
    
    table = dynamodb.Table('FinalAlyce_facts')
    
    with table.batch_writer() as batch:
        for row in rows:
            
            batch.put_item(Item= {
                'order_id':row.split(',')[0],
                'client_id':row.split(',')[1],
                'service_id':row.split(',')[2],
                'gift_id':row.split(',')[3],
                'gift_cost':row.split(',')[4],
                'total_gifts':row.split(',')[5],
                'total_amount':row.split(',')[6],
                'fee':row.split(',')[7],
                'variable_cost':row.split(',')[8],
                'total_revenue':row.split(',')[9],
                'date':row.split(',')[10]
                }
            )
