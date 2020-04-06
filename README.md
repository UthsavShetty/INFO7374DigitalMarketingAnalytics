# Alyce Marketing Analytics Project

### WebApp link : 
https://focused-wiles-5a4b67.netlify.com/

### Dash Link : 
http://ec2-54-227-146-222.compute-1.amazonaws.com:8050/

### Report Link: 
https://codelabs-preview.appspot.com/?file_id=1HolkoVJaDIK71xLdiNATNxh7Yp1Pw_LtJCUKvieOzE8#2

### Objective

Why?
- A web app with all the details required for a marketing analyst all at one place will help him/her in viewing all the information all   at one place and easier to use.

What?
- Build a Market Mix Model for Alyce. They have a detailed data available about their marketing spent for a couple of years which         includes spending on commercials, online campaigns, and pricing and promotion strategies.

Where?
- The dashboard web app will be useful for marketing folks when they have to make decisions based on their performance for previous year   on channel wise, clients wise etc and come up with a startegy for next year or campaign.

Who?
- The web app will be used by the marketing and data analysts.

When?
- It will be mainly helpful when the company has to come up with a strategy for a campaign for next quarter or year and they want to       check how they performed previously.

How?
- Create a pipeline on AWS when there is a file upload on S3, then a lambda is triggered to store it in a table on redshift and then the   web app reads the data from there and displays in the charts

### Market Mix Modeling (MMM) 
- is a technique which helps in quantifying the impact of several marketing inputs on sales or Market Share. The purpose of using MMM is   to understand how much each marketing input contributes to sales, and how much to spend on each marketing input.MMM helps in             ascertaining the effectiveness of each marketing input in terms of Return on Investment.
- Build a Market Mix Model for Alyce. They have a detailed data available about their marketing spent for a couple of years which         includes spending on commercials, online campaigns, and pricing and promotion strategies. In order to make marketing budget for the     next year need to develop a market mix model to observe the actual impact of different marketing variables over the last year and       based on the understanding of the model will have to recommend the optimal budget allocation for different marketing levers.

### Basic Architecture

![image](https://user-images.githubusercontent.com/47194856/78532358-17c82500-77b5-11ea-9655-ba44487967d1.png)

- The manual steps of creating the infrastructure can be automated using Terraform scripts which creates all the resources on our behalf with just one command terraform apply.
- To run these you need to configure aws cli - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html and install terraform - https://learn.hashicorp.com/terraform/getting-started/install.html. Then navigate to folder where man.tf is present and run terraform init, terraform apply - this command creates all the resources and terraform destroy - this command deletes everything.
- Developed a lambda function to transfer the data into tables as soon as it is uploaded onto S3 bucket.
SageMaker reads the data for it's models from the redshift cluster.
- Deployed the application on an EC2 instance and can be accessed anywhere
- We used the data we had from our previous assignments with few modifications and tables are listed below:

a) alyce_client: This is a dimension table which contains information about the Alyce's clients.

b) alyce_giftdata: This is a dimension table which contains information about different types of gifts

c) alyce_services: This is a dimension table which contains information about different types of services offered by Alyce like one-to-one gifting, swag select etc.

d) alyce_recipient: This is a dimension table which contains information about the gifts sent by the Alyce's client to the people who they want to maintain relationship with.

e) alyce_clientexpenditure: This table holds the information about the type of gift, recipient to which the client sent the gift and also few metrics like price, quantity etc.

f) alyce_facts: This table holds the information about the total amount spent on the gifts ,total number of gifts sent by the clients and the type of service the client has enrolled for.


### Technologies

- Dash framework integrated with Python
- HTML/CSS, Javascript with Tableau for frontend
- Terraform Script to automatically spin up infrastructure
- AWS lambda to automate the data load from S3 to tables
- AWS Sagemaker
- Deploy the web app on live server ( Netlify and AWS EC2)

### Authors
- Srikanth Reddy Gubbali
- Nishanth Manjunatha
- Uthsav Shetty


