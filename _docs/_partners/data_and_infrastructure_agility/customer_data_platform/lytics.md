---
nav_title: Lytics
article_title: Lytics
description: "This reference article covers the Braze and Lytics integration, a customer data platform, that allows brands to sync and map their Lytics data directly to Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner

---

# Lytics

> [Lytics][1] is a customer data platform for the next generation of customer-centric businesses. Lytics Decision Engine, Conductor, and Cloud Connect solutions provide marketers and data teams opportunities to perform identity resolution, orchestration, and campaign optimization in realtime and in a privacy-compliant manner.

The Braze and Lytics integration provides a unified view of your customers to enable powerful personalization and to drive optimized campaigns using the next-best action orchestration and decisions. The integration allows brands to:
- Sync Lytics audiences to Braze directly from Lytics
- Send events from Braze Campaigns or Canvas to Lytics in realtime for personalized campaigns and to build rich user profiles

## Integration

### Exporting Lytics data to Braze

#### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lytics account | A Lytics account is required to take advantage of this integration. |
| Braze REST API key | A Braze REST API key with `users.track` permission. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| App ID or group | When creating a Braze REST API key, you must grant permission for each app group or app ID you want to use with Lytics. |
| Braze Instance | Your Braze instance. Contact your Braze onboarding manager for this information if you don't have it. |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 1: Create an authorization 
1. In Lytics, navigate to the **Authorization** dashboard within the **Data** console in the navigation bar. 
2. Select **Create New Authorization** and search for and select **Braze**.
3. In the **Configure Authorization** prompt that appears, provide a label and a description and input your REST API Key and Braze Instance. 
4. Select **Complete** when finished.

![][2]{: style="max-width:80%;"}

#### Step 2: Create a job and select the job type
1. In Lytics, navigate to the **Jobs** dashboard within the **Data** console in the navigation bar. 
2. Select **Create New Job** and search for and select **Braze**. 
3. Select the **Export Audience** option in the **Select Job Type** prompt.<br>![][3]{: style="max-width:80%;"}<br><br>
4. Next, choose an authorization within the **Select Authorization** options.<br>![][4]{: style="max-width:80%;"}

#### Step 3: Configure the job
1. Provide a label and an optional description within the **Configure Job** prompt. 
2. Next, From the **Braze External User ID Field** input, select the Lytics field containing the Braze External User ID (`braze_id`).<br>![][5]{: style="max-width:80%;"}<br><br>
3. Finally, choose the preferable option for the **Existing Users** checkbox. 
    - Leaving this box checked will add users already existing in the selected Lytics audience. 
    - If unchecked, users will only be exported to Braze when entering or exiting the audience after the workflow begins. Select **Complete** when finished to initiate the export and save.<br>![][6]{: style="max-width:80%;"}

### Importing data from Braze via Webhook

Enriching Lytics customer profiles using Braze customer journey events.

#### Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Lytics account | A Lytics account is required to take advantage of this integration. |
| Lytics account number | A Lytics account number is necessary for configuring the webhook endpoint URL. |
| Lytics API Token | A Lytics REST API Token with Data Manager permissions. <br><br> This can be created within the **Lytics Dashboard > Account Settings Console > Access Tokens > Create New Token**. |
{: .reset-td-br-1 .reset-td-br-2}

#### Step 1: Create a Lytics API token
1. Navigate to the Lytics account menu by selecting your account name and selecting **Access Tokens** from the dropdown menu. 
2. Select **Create API Token**
3. Input a name, an optional description, and a token expiration period. 
4. Next, toggle the **Data Manager** scope for API Permissions and click on **Generate Token**.
5. Copy the token and store this token in a secure place.<br>![][8]{: style="max-width:80%;"}

#### Step 2: Configure the Lytics webhook URL
Braze uses the Lytics webhook URL to send a message to the Lytics API from Braze. This message can be used to personalize your campaigns in Lytics or to enrich your Lytics customer profile. The following two parameters are required to be added within the Lytics webhook URL:

1. Lytics Account Number
2. Lytics API token

Configure your webhook URL as indicated below by inserting each of these parameters in the URL template below where indicated by the `<Parameter>` placeholders:

`https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>`

#### Step 3: Create a Webhook on Braze 
1. Navigate to **Campaigns** in the Braze dashboard and click **+Create Campaign**. 
2. Select **Webhook** or, for campaigns targeting multiple channels, select **Multichannel Campaign** and select Webhook as an option for one of the channels. 
3. Compose your webhook, placing the Lytics Wwbhook URL in the **Webhook URL** field.
4. After defining the request type (HTTP `POST` method) and configuring the rest of the webhook details, your webhook is ready for testing and deployment.

### Importing data from Braze from a CSV File
Braze provides a CSV user data export option. This option supports the export of up to 500,000 users.

#### Step 1: Create an authorization 
1. In Lytics, navigate to the **Authorization** dashboard within the **Data** console in the navigation bar.
2. Select **Create New Authorization** and search for and select **Custome Integrations**.
3. Select the preferred type of SFTP authorization based on your business and security requirements.
- Note that only Client SFTP Server Authorization, Client SFTP Server Authorization with PGP Private Key, and Lytics Managed SFTP Server Authorization are the only types of authorization supported for importing files via SFTP into Lytics. Public key SFTP authorizations are for SFTP export only.<br>![][9]{: style="max-width:80%;"}<br><br>
4. In the **Configure Authorization** prompt, provide a label and a description and complete the rest of the configuration requirements. Select **Complete** when finished.

#### Step 2: Export a CSV from Braze
There are two options to export audiences using a CSV file on Braze:
1. If you're editing a segment, select the **CSV Export User Data** option from the **User Data** dropdown menu. 
2. Alternatively, export a CSV file from within the Segments dashboard. Besides the segment you want to export, click the **Settings** icon and select **CSV Export User Data** from the dropdown options.

#### Step 3: Configure a CSV import job
1. In Lytics, navigate to the **Jobs** dashboard within the **Data** console in the navigation bar. 
2. Select **Create New Job** and search for and select **Custom Integrations**.
3. Next, select the job type. To import Braze CSV files into Lytics, select **Import CSV** as the job type.<br>![][10]{: style="max-width:80%;"}<br><br>
4. Finally, input a label and optional description for the job and configure any other required details. Click **Complete** to initiate and save the job.

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