---
nav_title: User Attribute CSV - Lambda Process
permalink: /lambda/
hidden: true
---

# User Attribute CSV to Braze Ingestion

> This serverless application allows you to easily deploy a Lambda process that will post user attribute data from a CSV file directly to Braze using Braze Rest API [User Track]({{site.baseurl}}/docs/api/endpoints/user_data/post_user_track/) endpoint. 

The process launches immediately when you upload a CSV file to the configured AWS S3 bucket. It can handle large files and uploads. However, it is important to keep in mind that due to Lambda's time limits, the function will stop execution after 10 minutes. The process will launch another Lambda instance to finish processing the remaining part of the file. For more details about function timing, checkout [execution times](#estimated-execution-times).

#### CSV User Attributes

User attributes to be updated are expected in the following `.csv` format:

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

where the first column must specify the external ID of the user to be updated and the following columns specify attribute names and values. The number of attributes you specify can vary. If the CSV file to be processed does not follow this format, the function will fail.  
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
- **AWS Account** in order to use the S3 and Lambda services
- **Braze API URL** to connect to Braze servers
- **Braze API Key** to be able to send requests to `/users/track` endpoint
- **CSV File** with user external IDs and attributes to update

{% tabs %}
{% tab API URL %}

You can find your API URL, or REST endpoint, in the Braze [API documentation]({{site.baseurl}}/docs/user_guide/administrative/access_braze/braze_instances/#braze-instances). Simply match your dashboard URL to the REST endpoint URL. For example, if your dashboard shows `dashboard-01.braze.com/` URL, your REST endpoint would be `https://rest.iad-01.braze.com`. You can also find your REST API URL in the dashboard. 

From the left navigation panel, scroll down and select **Manage App Group**. There, you can find your `SDK Endpoint`. Replace `sdk` with `rest` to get your REST Endpoint. For example, if you see `sdk.iad-01.braze.com`, your API URL would be `rest.iad-01.braze.com`

{% endtab %}
{% tab API Key %}

To connect with Braze servers, we also need an API key. This unique identifier allows Braze to verify your identity and upload your data. To get your API key, open the Dashboard and scroll down the left navigation section. Select **Developer Console** under _App Settings_.

You will need an API key that has permission to post to `users.track` API endpoint. If you know one of your API keys supports that endpoint, you can use that key. To create a new one, click on `Create New API Key` on the right side of your screen.

Next, name your API Key and select `users.track` under the _User Data_ endpoints group. Scroll down and click on **Save API Key**.

{% endtab %}
{% endtabs %}

## Usage Instructions

##### Overview
1. Deploy Braze's publicly available CSV processing Lambda from the AWS Serverless Application Repository
2. Drop a CSV file with user attributes in the newly created S3 bucket
3. The users will be automatically imported to Braze

#### Deploy

To start processing your User Attribute CSV files, we need to deploy the Serverless Application that will handle the processing for you. This application will create the following resources automatically in order to successfully deploy:

- Lambda function
- S3 Bucket for your CSV Files that the Lambda process can read from (_Note: this Lambda function will only receive notifications for `.csv` extension files_)
- Role allowing for creation of the above
- Policy to allow Lambda to receive S3 upload event in the new bucket

Follow the direct link to the [Application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) or open the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications) and search for _braze-user-attribute-import_. Note that you must check the `Show apps that create custom IAM roles and resource policies` checkbox in order to see this application. The application creates a policy for the lambda to read from the newly created S3 bucket.

Click **Deploy** and let AWS create all the necessary resources.

You can watch the deployment and verify that the stack (ie. all the required resources) is being created in the [CloudFormation](https://console.aws.amazon.com/cloudformation/). Find the stack named _serverlessrepo-braze-user-attribute-import_. Once the **Status** turns to `CREATE_COMPLETE`, the function is ready to use. You can click on the stack and open **Resources** and watch the different resources being created.

The following resources were created:

- [S3 Bucket](https://s3.console.aws.amazon.com/s3/) - a bucket named `braze-user-csv-import-aaa123` where `aaa123` is a randomly generated string
- [Lambda Function](https://console.aws.amazon.com/lambda/) - a lambda function named `braze-user-attribute-import`
- [IAM Role](https://console.aws.amazon.com/iam/) - policy named `braze-user-csv-import-BrazeUserCSVImportRole` to allow lambda to read from S3 and to log function output

#### Run

To run the function, drop a user attribute CSV file in the newly created S3 bucket.

## Monitoring and Logging

To make sure the function ran successfully, you can read the function's execution logs. Open the Braze User CSV Import function (by selecting it from the list of Lambdas in the console) and navigate to **Monitor**. Here, you can see the execution history of the function. To read the output, click on **View logs in CloudWatch**. Select the lambda execution event you want to check.

## Lambda Configuration

By default, the function is created with 2048MB memory size. Lambda's CPU is proportional to the memory size. Even though, the script uses a constant, low amount of memory, the stronger CPU power allows to process the file faster and send more requests simultaneously.  
2GB was chosen as the best cost to performance ratio.  
You can review Lambda pricing [here](https://aws.amazon.com/lambda/pricing/).

You can reduce or increase the amount of available memory for the function in the Lambda **Configuration** tab. Under _General configuration_, click **Edit**, specify the amount of desired memory, and save.

Keep in mind that any more memory above 2GB has diminishing returns where it might improve processing speed by 10-20% but at the same time doubling or tripling the cost.

### Estimated Execution Times
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

In case of an unexpected error that prevents the further processing of the file, an event is logged (accessible through CloudWatch described in [Monitoring and Logging](#monitoring-and-logging)) that can be used to restart the Lambda from the point where the program stopped processing the file. It is important not to re-import the same data to save Data Points. You can find the instructions on how to do that below.

### Manual Triggers

In case you wanted to trigger the Lambda manually, for testing or due to a processing error, you can do it from the AWS Lambda Console using a test event.  
Open the Braze User Import Lambda in the AWS console by opening Lambda service and selecting `braze-user-csv-import` function. Navigate to **Test**.

#### Event

If you have an event from a returned exception, paste it in the **Test event**. Otherwise, copy the contents of [`sample-event.json`](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/blob/master/events/sample-event.json). Replace the following values:

1. `"awsRegion"` under `"Records"`, replace `"your-region"` with the proper region of the bucket with the file
2. `"name"` and `"arn"` under `"bucket"`, replace **only** `lambda-bucket-name` with the bucket name that CSV files are read from (the bucket that triggers this Lambda)
3. `"key"` under `"object"` with the CSV file key

Optional:
- `"offset"` field specifies the byte offset to start reading the file from
- `"headers"` field specifies CSV headers and it is mandatory if the file is not being read from the beginning

#### Invoke

To invoke the function, press `Invoke` and wait for the execution to finish.

### Manual Function Deploy

#### Create Role

The Lambda function requires permissions to read objects from S3, log to CloudWatch and call other Lambda functions. You can create a new role or add the policies to an existing role.
Required policies:

```
AmazonS3ReadOnlyAccess
AWSLambdaBasicExecutionROle
AWSLambdaRole
```

To create a new role with these permissions open [Roles](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles) console.

1. Click **Create role**
2. Select **Lambda** as a use case, and click on **Next: Permissions**
3. Search and mark all policies mentioned above
4. Click **Next:Tags** and **Next:Review**, name your role and finally create it by pressing **Create role**

#### Create Function

1. __Download the packaged code from [Releases](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/releases)__<br><br>
2. __Create a new [Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1#/discover) function.__
   1. Select _Author from scratch_
   2. Name your function
   3. Select **Python 3.6** runtime
   4. Under **Change default execution role**, select _Use an existing role_ and select a role with all three policies described above.
   5. Create the function<br><br>
3. __Upload the packaged code__ downloaded from the repository by clicking on **Upload from** and selecting `.zip file`<br><br>
4. __Configure Lambda__
   1. In the **Code** tab, scroll down to edit _Runtime settings_, changing Handler to `app.lambda_handler`
   2. In the **Configuration** tab, edit _General configuration_, setting the timeout to `15` min and `0` sec, and changing Memory size to `2048` MB
   3. Also in **Configuration**, under _Environment variables_ add two key-value pairs: `BRAZE_API_URL` key with your API URL as value, and `BRAZE_API_KEY` with your API Key as value
   4. Under _Asynchronous invocation_, change `Retry attempts` to `0`.<br><br>
5. __Add an S3 trigger__ where you can drop the user attribute CSV files by clicking on `+ Add trigger` under the Function overview, selecting **S3** as a trigger and the source bucket, optionally using a bucket prefix. Then Add the trigger.

## Contributing and Testing

In order to run tests, install

```
pip install pytest pytest-mock pytest-env
```

And run

```
pytest
```

Contributions are welcome!