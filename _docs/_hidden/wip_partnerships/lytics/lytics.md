---
nav_title: Lytics
article_title: Lytics
description: "This reference article covers the Braze and Lytics integration. Lytics is a enterprise Customer Data platform for marketers, analysts, and technologists. This integration allows brands to sync and map their Lytics data directly to Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
page_order: 1
hidden: true
---

# Lytics

> [Lytics][1] is the customer data platform (CDP) of choice for the next generation of customer-centric businesses. Lytics Decision Engine, Condcutor and Cloud Connect solutions provide marketers and data teams opportunities to perform identity resolution, orchestration and campaign optimization in realtime and in a privacy compliant manner.


The Braze and Lytics integration provides a unified view of your customers to enable powerful personalization and to drive optimized campaigns using next best action orchestration and decisioning. The integration allows brands to:

- Sync Lytics audiences: Export audiences to Braze directly from Lytics
- Send events from Braze Campaigns or Canvas to Lytics in realtime for personalized campaigns and to build rich user profiles

## Use Cases
Connect Braze to Lytics to import email, SMS, and push activity to enrich Lytics user profiles. Using Braze and Lytics together, you can also export Lytics' cross-channel, behavioral-driven audiences to build highly personalized Braze Customer Journeys using 1st Party Data.


## Integration - Exporting Lytics data into Braze
Optimizing Braze Customer Journeys using Lytics 1st Party Audiences

### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lytics account | A Lytics account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with `users.track` permission. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| App Id or Group | When creating a Braze REST API key, you must grant permission for each App Group or App Id which you would like to use with Lytics. |
| Braze Instance | Your Braze instance. Contact your Braze onboarding manager for this information, if you don't have it. |
{: .reset-td-br-1 .reset-td-br-2}

### Step 1: Create an Authorization 
In Lytics, navigate to the **Authorization** dashboard within the **Data** console in the navigation bar. Select **Create New Authorization** and search for and select **Braze**.

In the **Configure Authorization** prompt that appears, provide a label and a description and input your REST API Key and Braze Instance. Select **Complete** when finished.

![][2]{: style="max-width:80%;"}

### Step 2: Create Job and Select Job Type
In Lytics, navigate to the **Jobs** dashboard within the **Data** console in the navigation bar. Select **Create New Job** and search for and select **Braze**.  In the **Select Job Type** prompt that appears, select the Export Audience option.

![][3]{: style="max-width:80%;"}


Next, choose an authorization within the **Select Authorization** options.

![][4]{: style="max-width:80%;"}

### Step 3: Configure Job
Within the **Configure Job** prompt, provide a label and an optional description. Next, From the **Braze External User ID Field** input, select the field in Lytics that contains the Braze External User ID (`braze_id`).  The next step is the most important - select the audiences to export to Braze.

![][5]{: style="max-width:80%;"}

Finally, choose the preferable option for the **Existing Users** checkbox. Leaving this box checked will add users who already exist in the selected Lytics audience. If unchecked, users will only be exported to Braze when entering or exiting the audience after the workflow begins. Select **Complete** when finished to initiate the export and save.


![][6]{: style="max-width:80%;"}


## Integration - Importing data from Braze via Webhook
Enriching Lytics Customer Profiles using Braze Customer Journey Events

### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lytics account | A Lytics account is required to take advantage of this integration. |
| Lytics Account Number | A Lytics account number is necessary for configuring the webhooks endpoint URL. |
| Lytics API Token | A Braze REST API key with `users.track` and `user.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

### Step 1: Create a Lytics API Token
Navigate to the Lytics Account Menu in the bottom left corner by selecting your account name, and select **Access Tokens** from the dropdown menu.  Next select **Create API Token**

![][7]{: style="max-width:80%;"}

Input a name, optional description and a token expiration period. Next, toggle the **Data Manager** scope for API Permissions and click on **Generate Token**. Copy the token and store this token in a secure place.

![][8]{: style="max-width:80%;"}

### Step 2: Configure the Lytics Webhook URL
The Lytics webhook URL is used by Braze to send a message to the Lytics API from Braze. This message can be used to personalize your campaigns in Lytics or can be used to enrich your Lytics Customer Profile.  The following two parameters are required to be added within the Lytics webhook url:

1. Lytics Account Number.
2. Lytics API token.

Configure your webhook URL as indicated below by inserting each of these parameters in the URL template below where indicated by the `<Parameter>` placeholders:

 `https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>`

### Step 3: Create a Webhook on Braze 
Navigate to Campaigns in the Braze dashboard and click **+Create Campaign**. Select **Webhook** or, for campaigns targeting multiple channles select **Multichannel Campaign** and select Webhook as an option for one of the channels.  Compose your webhook, placing the Lytics Wwbhook URL in the **Webhook URL** field.

After defining the request type (http `POST` method), and configuring the rest of the webhook details, your webhook is ready for testing and deployment.


## Importing data from Braze from a CSV File
Braze provides a CSV User Data Export Option. This option supports an export of up to 500,000 users. Follow the below instructions to import Braze CSV User Data into Lytics:

### Step 1: Create an Authorization 
In Lytics, navigate to the **Authorization** dashboard within the **Data** console in the navigation bar. Select **Create New Authorization** and search for and select **Custome Integrations**. 

Select the preferrred type of SFTP authorization based on your business and security requirements. Note that only Client SFTP Server Authorization, Client SFTP Server Authorization with PGP Private Key, and Lytics Managed SFTP Server Authorization are the only types of authorization supported for importing files via SFTP into Lytics. Public key SFTP authorizations are for SFTP export only.

![][9]{: style="max-width:80%;"}

In the **Configure Authorization** prompt that appears, provide a label and a description and compplete the rest of the configuration requirements. Select **Complete** when finished.


### Step 2: Export a CSV from Braze
To export audiences using a CSV file on Braze, there are two options. If you're editing a segment, select the CSV Export User Data option from the User Data dropdown menu in the upper right corner of the Segment editing console. Alternatively, you may export a CSV file from within the Segments dashboard. To the right side of the segment you would like to export, click on the Settings icon and select CSV Export User Data from the dropdown options.

### Step 3: Configure a CSV Import Job
In Lytics, navigate to the **Jobs** dashboard within the **Data** console in the navigation bar. Select **Create New Job** and search for and select **Custom Integrations**.

Next, select the job type. To import Braze CSV files into Lytics, select **Import CSV** as the job type.

![][10]{: style="max-width:80%;"}

Finally, input a label and optional description for the job and configure any other required details. Click **Complete** to intiate and save the job.


[1]: https://www.lytics.com/
[2]: {% image_buster /assets/img/lytics/braze_authorization.png %}
[3]: {% image_buster /assets/img/lytics/braze_jobtype.png %}
[4]: {% image_buster /assets/img/lytics/braze_jobauth.png %}
[5]: {% image_buster /assets/img/lytics/braze_job.png %}
[6]: {% image_buster /assets/img/lytics/braze_backfill.png %}
[7]: {% image_buster /assets/img/lytics/create_token.png %}
[8]: {% image_buster /assets/img/lytics/data_manager.png %}
[9]: {% image_buster /assets/img/lytics/authorization_method.png %}
[10]: {% image_buster /assets/img/lytics/configure_job.png %}





