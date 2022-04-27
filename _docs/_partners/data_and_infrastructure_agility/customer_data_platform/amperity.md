---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "This article covers the Braze and Amperity integration. Amperity provides intelligent capabilities across data management unification, analytics and insights, and activation."
page_type: partner
page_order: 2.2
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) is a comprehensive enterprise customer data platform, helping brands get to know their customers, make strategic decisions, and consistently take the right course of action to serve their consumers better. Amperity provides intelligent capabilities across data management unification, analytics, insights, and activation.

{% include video.html id="06G0lxaSjgk" align="right" %}

The Braze and Amperity integration offers a unified view of your customers across the two platforms. This integration allows you to:
- **Sync Amperity segments**: Sync segments to map Amperity user data to Braze user accounts.
- **Unify data**: Unify data across various Amperity supported platforms and Braze.
- **Send Amperity data via AWS S3 buckets to Braze**: Use a serverless Lambda function to upload Amperity user segments to your AWS S3 bucket that will post user attribute data to Braze.
- **Manually upload Amperity data to Braze**: Manually upload user CSV segments to the Braze platform through the dashboard.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Amperity account | An [Amperity account](https://amperity.com/request-a-demo) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create an Amperity user segment

To upload Amperity user data to Braze, you must first create a segment of existing Amperity users.
1. Navigate to the **Segments** tab within the Amperity dashboard.<br>![][2]<br><br>
2. Click **Create** to filter and define a segment of users to capture. Under the **Summary** tab, you can view valuable insights like historical revenue and predicted revenue for the coming year based on the given user segment. <br>![A summary of an Amperity segment showing the revenue and reachability stats.][3] <br><br>
3. Select the **Customers** tab, and choose which user fields you would like to include using the **Show Columns** selector.<br>![The Amperity segment builder showing the available customer attributes to include.][4]<br><br>
4. Next, click **Run Segment**.

### Step 2: Select upload method

Once the segment has run, you can either:
- [Set up automatic upload](#automatic-upload) - **recommended**
  - Set up a destination workflow to automatically upload Amperity user attribute data to Braze via an AWS S3 Bucket.
- [Set up manual upload](#manual-upload)
  - Manually upload user CSV segments to the Braze platform through the dashboard. 

### Automatic upload via AWS S3 bucket {#automatic-upload}

#### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| AWS account | An AWS account is required to use the S3 and Lambda services. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| CSV file | Check out the [CSV formatting specifications](#csv), and use step 1 of the Amperity integration to obtain a CSV with user external IDs and attributes to update. |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 3a: Set Braze destination

##### Activate segment

First, you must activate the segment by selecting **Activate Segment**.

In the window that opens:
- Name your destination **Braze**
- Set the Data Template to **Default**
- Enter your S3 bucket
- Enter your S3 region
- Set a file name template
- Set the workflow query frequency

![][7]{: style="max-width:60%;"}

Click **Activate**.

##### Set up destination

Next, you must set up the Braze destination workflow by selecting the **Destination** tab and clicking **Add Destination**.

In the window that opens:
- Name your destination **Braze** and add an optional description
- Select the **Amazon S3** plugin
- Set the credential type to **iam-credential**
- Name and configure the credential based on your Amazon S3 settings
- Enter your S3 bucket
- Enter your S3 region
- Set encoding to **None**
- Include header row in output files

![][8]{: style="max-width:60%;"}

Click **Save**.

Additional Amperity documentation on configuring Amazon S3 can be found [here](https://docs.amperity.com/configure/destination_amazon_s3.html).

#### Step 4a: Send data via AWS S3 bucket

##### Lambda function 

The following [Lambda function](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) is a serverless application that allows you to easily post user attribute data from an Amperity CSV file directly to Braze through the Braze users/track/ endpoint. This process launches immediately upon uploading a CSV file to a configured AWS S3 bucket. To read more, visit our [dedicated Lambda function article](https://www.braze.com/docs/user_csv_lambda/).

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
- S3 Bucket for your CSV Files that the Lambda process can read from This Lambda function will only receive notifications for `.csv` extension files.
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
To read more about different aspects of the Lambda function such as monitoring and logging, updating an existing function, fatal errors, and more, visit our [dedicated Lambda function article](https://www.braze.com/docs/user_csv_lambda/). 
{% endalert %}

### Manual upload via CSV {#manual-upload}

#### Step 3b: Create Amperity CSV

1. Once the segment has run, click **View SQL**. This will generate a SQL query that preformats the data to work well with what is required by the Braze platform. Make sure the field names match the fields in Braze that you want to load data into. If you would like to customize it, you can convert the Segment to SQL and alias the fields. Click **Run Query** to run the SQL query.<br>![Braze demo CSV shown in the AmperitySQL query editor.][5]<br><br>
2. Lastly, click **Download** to download a CSV version of this user segment. This is the file you'll upload to Braze.

#### Step 4b: Import CSV

1. From the Braze platform, go to the **User Import** page listed under **Users**.
2. Upload the CSV file downloaded from Amperity.
3. Once uploaded, confirm the default and custom attributes, assign an import name, and optionally create a group within the Braze platform from the uploaded Amperity segment. 
4. Click **Start Import**.

[2]: {% image_buster /assets/img/amperity/amperity2.png %} 
[3]: {% image_buster /assets/img/amperity/amperity3.png %} 
[4]: {% image_buster /assets/img/amperity/amperity4.png %} 
[5]: {% image_buster /assets/img/amperity/amperity5.png %} 
[7]: {% image_buster /assets/img/amperity/activate2.png %} 
[8]: {% image_buster /assets/img/amperity/destinationconfiguration.png %} 
