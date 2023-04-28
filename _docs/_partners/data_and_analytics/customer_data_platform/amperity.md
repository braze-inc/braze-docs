---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "This reference article outlines the partnership between Braze and Amperity, a comprehensive enterprise customer data platform, allowing you to sync Amperity users, unify data, send data using AWS S3 buckets to Braze, and more."
page_type: partner
search_tag: Partner
page_order: 2

---

# Amperity

> [Amperity](https://amperity.com/) is a comprehensive enterprise customer data platform, helping brands get to know their customers, make strategic decisions, and consistently take the right course of action to serve their consumers better. Amperity provides intelligent capabilities across data management unification, analytics, insights, and activation.

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

The Braze and Amperity integration offers a unified view of your customers across the two platforms. This integration allows you to:
- **Sync Amperity users**: Sync user lists to map Amperity user data to Braze user accounts.
- **Unify data**: Unify data across various Amperity-supported platforms and Braze.
- **Send Amperity data via AWS S3 buckets to Braze**: Use a serverless Lambda function to upload Amperity user lists to your AWS S3 bucket that will post user attribute data to Braze.
- **Manually upload Amperity data to Braze**: Manually upload user CSV lists to the Braze platform through the dashboard.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Amperity account | An [Amperity account](https://amperity.com/request-a-demo) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create an Amperity user list

To upload Amperity user data to Braze, you must configure a destination that enables sending query results to Braze, create a query that returns a list of users, and send the results of that query to Braze using orchestration.

1. Add a [Braze destination](https://docs.amperity.com/datagrid/destination_braze.html) for your tenant.
2. Navigate to the **Queries** tab within the Amperity dashboard. 
3. Click **Create**, and then **Select SQL Query** to define the SQL query that returns a list of users. For example:
``` sql
SELECT
 amperity_id
 ,external_id AS external_id
 ,email AS email
 ,given_name AS first_name
 ,surname AS last_name
 -- add more attributes, as desired
FROM Merged_Customers
```
4. Click **Run** to validate your query. When finished, click **Activate**. <br>![A summary of an Amperity query that has successfully created a list of users to be sent to Braze.][9] <br><br>
5. Add this query to an orchestration that is configured to [send a list of users to Braze](https://docs.amperity.com/amp360/sendto_braze.html).<br>![A summary of activating your Braze query, and then adding it to an orchestration that is configured for Braze.][10]

### Step 2: Select upload method

Once the query has run, you can either:
- [Set up automatic upload](#automatic-upload) - **recommended**
  - Set up a destination workflow to automatically upload Amperity user attribute data to Braze via an AWS S3 Bucket.
- [Set up manual upload](#manual-upload)
  - Manually upload user CSV lists to the Braze platform through the dashboard. 

### Automatic upload via AWS S3 bucket {#automatic-upload}

#### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| AWS account | An AWS account is required to use the S3 and Lambda services. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| CSV file | Check out the [CSV formatting specifications](#csv), and use step 1 of the Amperity integration to obtain a CSV with user external IDs and attributes to update. |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 4a: Send data via AWS S3 bucket

##### Lambda function 

The following [Lambda function](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) is a serverless application that allows you to easily post user attribute data from an Amperity CSV file directly to Braze through the Braze users/track/ endpoint. This process launches immediately upon uploading a CSV file to a configured AWS S3 bucket. To read more, visit our [dedicated Lambda function article]({{site.baseurl}}/user_csv_lambda/).

The Lambda function can handle large files and uploads, but the function will stop execution after 10 minutes due to Lambda's time limits. This process will then launch another Lambda instance to finish processing the remaining part of the file.

##### CSV formatting and processing {#csv}

###### CSV user attributes

User attributes to be updated must be in the following `.csv` format:

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

###### CSV processing

Any values in an array (ex. `"['Value1', 'Value2']"`) will be automatically destructured and sent to the API in an array rather than a string representation of an array.

##### Usage instructions

1. Deploy Braze's publicly available CSV processing Lambda from the AWS Serverless Application Repository.
2. Drop a CSV file with user attributes in the newly created S3 bucket.
3. The users will be automatically imported to Braze.

###### Deploy

To start processing your user attribute CSV files, we need to deploy the serverless application to handle the processing for you. This application will create the following resources automatically to deploy successfully:
- Lambda function
- S3 Bucket for your CSV files that the Lambda process can read from. This Lambda function will only receive notifications for CSV extension files.
- Role allowing for the creation of the S3 Bucket
- Policy to allow Lambda to receive S3 upload event in the new bucket

Follow the direct link to the [application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import) or open the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications) and search for **braze-user-attribute-import**. You must check the **Show apps that create custom IAM roles and resource policies** checkbox to see this application. The application creates a policy for the Lambda to read from the newly created S3 bucket.

Click **Deploy** and let AWS create all the necessary resources.

You can watch the deployment and verify that the stack (i.e., all the required resources) is being created in the [CloudFormation](https://console.aws.amazon.com/cloudformation/). Find the stack named **serverlessrepo-braze-user-attribute-import**. Once the **Status** turns to `CREATE_COMPLETE`, the function is ready to use. You can click on the stack, open **Resources**, and watch the different resources being created.

The following resources are created:

- [S3 bucket](https://s3.console.aws.amazon.com/s3/) - a bucket named `braze-user-csv-import-aaa123` where `aaa123` is a randomly generated string
- [Lambda function](https://console.aws.amazon.com/lambda/) - a Lambda function named `braze-user-attribute-import`
- [IAM role](https://console.aws.amazon.com/iam/) - policy named `braze-user-csv-import-BrazeUserCSVImportRole` to allow Lambda to read from S3 and to log function output

###### Run

To run the function, drop a user attribute CSV file in the newly created S3 bucket.

{% alert important %}
To read more about different aspects of the Lambda function, such as monitoring and logging, updating an existing function, fatal errors, and more, visit our [dedicated Lambda function article]({{site.baseurl}}/user_csv_lambda/). 
{% endalert %}

### Manual upload via CSV {#manual-upload}

#### Step 3b: Create Amperity CSV

1. Once you've run and activated your query, you can download a CSV file of your query by clicking **Download**. This is the file you will upload to Braze.<br>![A summary of an Amperity query that has successfully created a list of users to be sent to Braze.][9] 

#### Step 4b: Import CSV

1. From the Braze platform, go to the **User Import** page listed under **Users**.
2. Upload the CSV file downloaded from Amperity.
3. Once uploaded, confirm the default and custom attributes, assign an import name, and optionally create a group within the Braze platform from the uploaded Amperity query. 
4. Click **Start Import**.

[2]: {% image_buster /assets/img/amperity/amperity2.png %} 
[3]: {% image_buster /assets/img/amperity/amperity3.png %} 
[4]: {% image_buster /assets/img/amperity/amperity4.png %} 
[5]: {% image_buster /assets/img/amperity/amperity5.png %} 
[7]: {% image_buster /assets/img/amperity/activate2.png %} 
[8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
[9]: {% image_buster /assets/img/amperity/amperity6.png %} 
[10]: {% image_buster /assets/img/amperity/amperity7.png %} 
