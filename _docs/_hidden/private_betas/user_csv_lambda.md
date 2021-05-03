---
nav_title: User Attribute CSV - Lambda Process
permalink: /user_csv_lambda/
hidden: true
---

# User Attribute CSV to Braze Ingestion

> The following article references a serverless application that allows you to easily deploy a Lambda process that will post user attribute data from a CSV file directly to Braze through the Braze [User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) API endpoint. This application can be found on our Github [here](https://github.com/braze-inc/growth-shares-lambda-user-csv-import).

This process launches immediately upon uploading a CSV file to a configured AWS S3 bucket. It can handle large files and uploads, but due to Lambda's time limits, the function will stop execution after 10 minutes. This process will then launch another Lambda instance to finish processing the remaining part of the file. For more details about function timing, check out the [estimated execution times](#estimated-execution-times).

#### CSV User Attributes

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

#### CSV Processing

Any values in an array (ex. `"['Value1', 'Value2']"`) will be automatically destructured and sent to the API in an array rather than a string representation of an array.

## Requirements

To successfully run this Lambda function, you will need:
- **AWS Account** to use the S3 and Lambda services
- **Braze API URL** to connect to Braze servers
- **Braze API Key** to be able to send requests to `/users/track` endpoint
- **CSV File** with user external IDs and attributes to update

{% tabs %}
{% tab API URL %}

You can find your API URL, or REST endpoint, in the Braze API documentation and through the dashboard.

- __API Documentation__<br>Per the [API documentation]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances), simply match your Braze instance URL to the REST endpoint URL. For example, if your dashboard shows `dashboard-01.braze.com/` URL, your REST endpoint would be `https://rest.iad-01.braze.com`. <br><br>
- __Dashboard__<br>From the left navigation panel, scroll down and select **Manage App Group**. There, you can find your `SDK Endpoint`. Replace `sdk` with `rest` to get your REST Endpoint. For example, if you see `sdk.iad-01.braze.com`, your API URL would be `rest.iad-01.braze.com`

{% endtab %}
{% tab API Key %}

To connect with the Braze servers, you will need an API key. This unique identifier allows Braze to verify your identity and upload your data. 

To get your API key, open the Dashboard and scroll down the left navigation section. Select **Developer Console** under _App Settings_. You will need an API key that has permission to post to `users.track` API endpoint. If you know one of your API keys supports that endpoint, you can use that key. 

To create a new one, click on `Create New API Key` on the right side of your screen. Next, name your API Key and select `users.track` under the _User Data_ endpoints group. Scroll down and click on **Save API Key**.

{% endtab %}
{% endtabs %}

## Usage Instructions

##### Overview
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

## Monitoring and Logging

To make sure the function runs successfully, you can read the function's execution logs. Open the Braze User CSV Import function (by selecting it from the list of Lambdas in the console) and navigate to **Monitor**. Here, you can see the execution history of the function. To read the output, click on **View logs in CloudWatch**. Select the lambda execution event you want to check.

## Estimated Execution Times
_2048MB Lambda Function_

| # of rows | Exec. Time |
| --------- | ---------- |
| 10k       | 3s         |
| 100k      | 30s        |
| 1M        | 5 min      |
| 5M        | 30 min     |

## Updating an Existing Function

If you have already deployed the application and a new version is available in the repository, you can update by re-deploying the function as if you were doing it for the first time. That means you have to pass it the Braze API Key and Braze API URL again. The update will only overwrite the function code. It will not modify or delete other existing resources like the S3 bucket.

## Fatal Error

In case of an unexpected error that prevents the further processing of the file, an event is logged (accessible through CloudWatch described in [Monitoring and Logging](#monitoring-and-logging)) that can be used to restart the Lambda from the point where the program stopped processing the file. It is important not to re-import the same data to save Data Points. You can find instructions to do this in our [Github repo](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error).

{% alert important %}
Visit our Github repo to learn more about how to deal with [fatal errors](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) or [lambda configuration](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration).
{% endalert%}