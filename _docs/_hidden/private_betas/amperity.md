---
nav_title: Amperity
alias: /partners/amperity/
description: "This article covers the Braze and Amperity integration. Amperity provides intelligent capabilities across data management unification, analytics and insights, and activation."
page_type: partner
hidden: true
---

# Amperity

> [Amperity](https://amperity.com/) is a comprehensive enterprise customer data platform, helping brands get to know their customers, make strategic decisions, and consistently take the right course of action to serve their consumers better. Amperity provides intelligent capabilities across data management unification, analytics, insights, and activation.

{% include video.html id="06G0lxaSjgk" align="right" %}

Amperity supports the Braze platform by providing a unified view of your customers across its customer data platform and Braze. This integration allows you to: 
- __Sync Amperity Segments:__ Sync segments to map Amperity user data to Braze user accounts.
- __Unify data:__ Unify data across various Amperity supported platforms and Braze.
- __Send Amperity data via AWS S3 Buckets to Braze:__ Use a serverless Lambda function to upload Amperity user segments to your AWS S3 bucket that will post user attribute data to Braze.
- __Manually Upload Amperity data to Braze:__ Manually upload user CSV segments to the Braze platform through the dashboard.

## Pre-Requisites

| Requirement | Origin | Access | Description |
| ----------- | ------ | ------ | ----------- |
| Amperity Account | Amperity | [Amperity](https://amperity.com/request-a-demo) | An Amperity account is required to set up the Amperity-Braze integration |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze and Amperity Integration

### Create Amperity User Segment

To upload Amperity user data to Braze, you must first create a segment of existing Amperity users.
1. Navigate to the __Segments__ tab within the Amperity dashboard.<br>![Amperity Segments Overview][2]<br><br>
2. Select __Create__ to filter and define a segment of users to capture. Under the __Summary__ tab you can view valuable insights like historical revenue and predicted revenue for the coming year based on the given user segment. <br>![Amperity Segment Builder][3] <br><br>
3. Select the __Customers__ tab, and choose which user fields you would like to include using the __Show Columns__ selector on the right.<br>![Amperity Segment Builder][4]<br><br>
4. Next, click __Run Segment__.

### Select Upload Method

__Once the segment has run, you can either:__
- [Set up Automatic Upload](#automatic-upload) - __Recommended__
  - Set up a destination workflow to automatically upload Amperity user attribute data to Braze via an AWS S3 Bucket.
- [Set up Manual Upload](#manual-upload)
  - Manually upload user CSV segments to the Braze platform through the dashboard. 

### Automatic Upload - Upload via AWS S3 Bucket

#### Set Braze Destination

First, you must activate the segment and set up the Braze destination workflow.<br>
Amperity documentation on this topic can be found [here](https://docs.amperity.com/configure/destination_amazon_s3.html).

![Segment 1][6]{: style="max-width:30%;"} ![Segment 2][7]{: style="max-width:30%;"} ![Destination Configuration][8]{: style="max-width:37%;"}

#### Send Data via AWS S3 Bucket

##### Lambda Function 

The following [Lambda function](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) is a serverless application that allows you to easily post user attribute data from an Amperity CSV file directly to Braze through the Braze User Track endpoint. This process launches immediately upon uploading a CSV file to a configured AWS S3 bucket. To read more, visit our [dedicated Lambda function article](https://www.braze.com/docs/user_csv_lambda/).

##### Requirements and Limitations

- __AWS Account:__ An AWS Account is required to use the S3 and Lambda services.
- __Braze API URL:__ Braze [API REST Endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) is required to connect to Braze servers.
- __Braze API Key:__ A [Braze API key]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) with `user/track` permission is required to send requests to [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint.
- __CSV File:__ Use step 1 of the Amperity integration steps to obtain a CSV with user external IDs and attributes to update.

It can handle large files and uploads, but the function will stop execution after 10 minutes due to Lambda's time limits. This process will then launch another Lambda instance to finish processing the remaining part of the file.

##### CSV Formatting and Processing

###### CSV User Attributes

User attributes to be updated are expected in the following `.csv` format:

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

The first column must specify the external ID of the user to be updated, and the following columns must specify attribute names and values. The number of attributes you specify can vary. If the CSV file to be processed does not follow this format, the function will fail.  

CSV file example:

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

###### CSV Processing

Any values in an array (ex. `"['Value1', 'Value2']"`) will be automatically destructured and sent to the API in an array rather than a string representation of an array.

##### Usage Instructions

1. Deploy Braze's publicly available CSV processing Lambda from the AWS Serverless Application Repository
2. Drop a CSV file with user attributes in the newly created S3 bucket
3. The users will be automatically imported to Braze

###### Deploy

To start processing your User Attribute CSV files, we need to deploy the Serverless Application to handle the processing for you. This application will create the following resources automatically to deploy successfully:

- Lambda function
- S3 Bucket for your CSV Files that the Lambda process can read from (_Note: this Lambda function will only receive notifications for `.csv` extension files_)
- Role allowing for the creation of the above
- Policy to allow Lambda to receive S3 upload event in the new bucket

Follow the direct link to the [application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) or open the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications) and search for _braze-user-attribute-import_. Note that you must check the `Show apps that create custom IAM roles and resource policies` checkbox to see this application. The application creates a policy for the Lambda to read from the newly created S3 bucket.

Click **Deploy** and let AWS create all the necessary resources.

You can watch the deployment and verify that the stack (i.e., all the required resources) is being created in the [CloudFormation](https://console.aws.amazon.com/cloudformation/). Find the stack named _serverlessrepo-braze-user-attribute-import_. Once the **Status** turns to `CREATE_COMPLETE`, the function is ready to use. You can click on the stack and open **Resources** and watch the different resources being created.

The following resources are created:

- [S3 Bucket](https://s3.console.aws.amazon.com/s3/) - a bucket named `braze-user-csv-import-aaa123` where `aaa123` is a randomly generated string
- [Lambda Function](https://console.aws.amazon.com/lambda/) - a lambda function named `braze-user-attribute-import`
- [IAM Role](https://console.aws.amazon.com/iam/) - policy named `braze-user-csv-import-BrazeUserCSVImportRole` to allow lambda to read from S3 and to log function output

###### Run

To run the function, drop a user attribute CSV file in the newly created S3 bucket.

{% alert important %}
To read more about different aspects of the Lambda function such as monitoring and logging, updating an existing function, fatal errors, and more. Visit our [dedicated Lambda function article](https://www.braze.com/docs/user_csv_lambda/). 
{% endalert %}

### Manual Upload - Upload via CSV

#### Amperity Platform

1. Once the segment has run, select __View SQL__. This will generate a SQL query that preformats the data to work well with what is required by the Braze platform. Make sure the field names match the fields in Braze that you want to load data into. If you would like to customize it, you can convert the Segment to SQL and alias the fields. Select __Run Query__ to run the SQL query.<br>![Amperity Segment Builder][5]<br><br>
2. Lastly, select __Download__ to download a CSV version of this user segment. 

#### Braze Platform

1. From the Braze platform, select __User Import__ listed under __Users__.
2. Upload the CSV file downloaded from Amperity.
3. Once uploaded, confirm the default and custom attributes, assign an import name, and optionally create a group within the Braze platform from the uploaded Amperity segment. 
4. Select __Start Import__.


[2]: {% image_buster /assets/img/amperity/amperity2.png %} 
[3]: {% image_buster /assets/img/amperity/amperity3.png %} 
[4]: {% image_buster /assets/img/amperity/amperity4.png %} 
[5]: {% image_buster /assets/img/amperity/amperity5.png %} 
[6]: {% image_buster /assets/img/amperity/activate1.png %} 
[7]: {% image_buster /assets/img/amperity/activate2.png %} 
[8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
