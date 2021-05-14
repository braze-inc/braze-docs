---
nav_title: Amperity
alias: /partners/amperity/
description: "This article covers the Braze and Amperity integration."
page_type: partner
hidden: true
---

# Amperity

> [Amperity](https://amperity.com/) is a comprehensive enterprise customer data platform, helping you turn customer data into great experiances for your customers and great results for your business. Amperity helps brands get to know their customers, make strategic decisions, and consistently take the right course of action to better serve their consumers and continue growing their businesses by providing intelligent capabilities across data management unification, analytics and insights, and activation. Amperity's product offerings include [AmpID](https://amperity.com/what-we-do/amp-id), [Amp360](https://amperity.com/what-we-do/amp-360), [AmpIQ](https://amperity.com/what-we-do/amp-iq), and [DataGrid](https://amperity.com/what-we-do/datagrid).

{% include video.html id="06G0lxaSjgk" align="right" %}

The Braze and Amperity integration allows you to: 
- Sync 'segments' to Braze from users from a variety of offline/online sources
- deal with historical data backfill in a smart way
- Send Braze data via currents to Amperity

## Pre-Requisites

| Requirement | Origin | Access | Description |
| ----------- | ------ | ------ | ----------- |
| Amperity Account | Amperity | [Amperity](https://amperity.com/request-a-demo) | An Amperity account is required to set up the Amperity-Braze integration |
| AWS account | AWS | AWS | An AWS account is required to use the S3 and lambda services |
| Braze API URL | Braze | Braze | description |
| Braze API Key | Braze | Braze | description |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Step 1: Export Data

## Step 2: Upload Data

## Step 3: Send Data via Currents (Optional)

### Lambda Function 

This [Lambda function](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) is a serverless application that allows you to easily deploy a lambda process that will post user attribute data from an Amperity CSV file directly to Braze through the Braze User Track endpoint. 

This process launches immediately upon uploading a CSV file to a configured AWS S3 bucket. It can handle large files and uploads, but due to Lambda's time limits, the function will stop execution after 10 minutes. This process will then launch another Lambda instance to finish processing the remaining part of the file.

#### CSV Formatting and Processing

##### CSV User Attributes

User attributes to be updated are expected in the following `.csv` format:

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

The first column must specify the external ID of the user to be updated and the following columns must specify attribute names and values. The number of attributes you specify can vary. If the CSV file to be processed does not follow this format, the function will fail.  

CSV file example:

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

##### CSV Processing

Any values in an array (ex. `"['Value1', 'Value2']"`) will be automatically destructured and sent to the API in an array rather than a string representation of an array.

### Usage Instructions

1. Deploy Braze's publicly available CSV processing Lambda from the AWS Serverless Application Repository
2. Drop a CSV file with user attributes in the newly created S3 bucket
3. The users will be automatically imported to Braze

#### Deploy

To start processing your User Attribute CSV files, we need to deploy the Serverless Application that will handle the processing for you. This application will create the following resources automatically to successfully deploy:

- Lambda function
- S3 Bucket for your CSV Files that the Lambda process can read from (_Note: this Lambda function will only receive notifications for `.csv` extension files_)
- Role allowing for the creation of the above
- Policy to allow Lambda to receive S3 upload event in the new bucket

Follow the direct link to the [Application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) or open the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications) and search for _braze-user-attribute-import_. Note that you must check the `Show apps that create custom IAM roles and resource policies` checkbox to see this application. The application creates a policy for the lambda to read from the newly created S3 bucket.

Click **Deploy** and let AWS create all the necessary resources.

You can watch the deployment and verify that the stack (ie. all the required resources) is being created in the [CloudFormation](https://console.aws.amazon.com/cloudformation/). Find the stack named _serverlessrepo-braze-user-attribute-import_. Once the **Status** turns to `CREATE_COMPLETE`, the function is ready to use. You can click on the stack and open **Resources** and watch the different resources being created.

The following resources were created:

- [S3 Bucket](https://s3.console.aws.amazon.com/s3/) - a bucket named `braze-user-csv-import-aaa123` where `aaa123` is a randomly generated string
- [Lambda Function](https://console.aws.amazon.com/lambda/) - a lambda function named `braze-user-attribute-import`
- [IAM Role](https://console.aws.amazon.com/iam/) - policy named `braze-user-csv-import-BrazeUserCSVImportRole` to allow lambda to read from S3 and to log function output

#### Run

To run the function, drop a user attribute CSV file in the newly created S3 bucket.

{% alert important %}
To read more about different aspects of the Lambda function such as monitoring and logging, updating an existing function. fatal errors, and more. Visit our [dedicated Lambda function article](https://www.braze.com/docs/user_csv_lambda/). 
{% endalert %}







