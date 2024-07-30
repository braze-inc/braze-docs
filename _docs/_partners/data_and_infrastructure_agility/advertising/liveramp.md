---
nav_title: LiveRamp
article_title: LiveRamp
description: "Learn how to connect LiveRamp, Snowflake, and Braze, so you can create highly personalized and relevant marketing campaigns."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Connecting LiveRamp, Snowflake, and Braze

> Learn how to connect LiveRamp, Snowflake, and Braze, so you can create highly personalized and relevant marketing campaigns by reducing the time to insights, breaking down data silos, and optimizing customer engagement. This integration enhances data-driven marketing by providing actionable person-based insights and consolidating consumer touchpoints for better audience segmentation and timely campaigns. It also leverages benchmarks powered by Snowflake to help refine your marketing strategies against industry standards.

## Use cases

- **Actionable Person & Household Based Insights:** Consolidation of consumer touchpoints to a person-based view enables a more accurate understanding of consumer preferences for better audience segmentation, testing, and model building across LiveRamp & Braze. Providing you a holistic and actionable view across both your marketing and advertising engagements in a single cloud environment.
- **Reduce Time to Insights:** Access customer engagement and campaign data in real-time, eliminating the need for time-consuming ETL processes. This means you can base your customer experiences on the most up-to-date information, enhancing the timeliness and relevance of your campaigns.
- **Break Down Data Silos & Interoperability:** Create a comprehensive view of your customers across various channels and platforms. Data becomes more valuable when you can effectively connect it to an ecosystem, and LiveRamp Identity solutions combined with Braze can be flexibly applied to sophisticated customer use cases and are integrated as an identity layer across the ecosystem.
- **Optimize Customer Engagement:** Leverage [Braze Benchmarks](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/%23braze-benchmarks&sa=D&source=editors&ust=1719246601732592&usg=AOvVaw0zjg0fsIH0dk618YMiPrGC), powered by Snowflake, to compare your brand's engagement data to LiveRamp ROAS and benchmarks across channels, industries, and platforms. This valuable insight helps fine-tune your marketing strategies.


## Prerequisites

| Prerequisite       | Description                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake Account | You need a Snowflake account with admin-level permissions.                                                                                                                                      |
| Braze Account     | Reach out to your Braze Account or customer success manager to consult Braze data strategy services on Secure Data Sharing with Snowflake and to purchase their Snowflake Data Share Connector. |
| LiveRamp Account  | Reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com) to discuss the required LiveRamp applications within Snowflake.                              |
| A Snowflake Braze integration | To integrate Snowflake with Braze, see [Snowflake integration guide]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/).                             |
{: .reset-td-br-1 .reset-td-br-2 }

## About data sharing

Snowflake's [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro) does not transfer data between LiveRamp, Snowflake, and Braze. Data is only shared through Snowflake's services and metadata store, meaning no data is copied and no additional storage charges occur. Access to shared data is controlled and governed using the access controls of your Snowflake account.

## Setting up the integration

### Step 1: Set up your Braze secure data sharing connection
When you request a data share, Braze will provision the share from the workspace(s) that the share was purchased. After the share is provisioned, all data is immediately accessible from within your Snowflake instance in the form of an incoming data share.

### Step 2: Create a database from the Braze share

Once the share is visible in your instance create a database from the share so you can see and query the tables. Note that you’ll need to be an account admin to see the data share.

### Step 3: Install the LiveRamp Identity Resolution and Transcoding Native App 
You can view a comprehensive step-by-step process for integration and activation of the LiveRamp Snowflake Native App. Here: [LiveRamp Integration & Activation Guide](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html).

In Snowflake, go to **Snowsight** > **Marketplace**, then request [LiveRamp Identity Resolution and Translation](https://app.snowflake.com/marketplace/listing/GZT0Z11US7AT/liveramp-identity-resolution-and-translation?search=LiveRamp%20Identity%20Resolution) app. LiveRamp will reach out to begin the contracting process. Once completed, the app will be shared with your account. Select the appropriate warehouse and click **Get** to start the installation process.

### Step 4: Run the initial LiveRamp Application Setup

Run the **Application Setup SQL**. This setup will set necessary variables, create an integration to LiveRamp's auth API, and create logging and metrics tables to share back to LiveRamp.

### Step 5: Configure Logging and Metrics Tables

The native app logs activity and aggregates event data into metrics. These tables need to be shared back to LiveRamp to validate the metrics and make the output table visible. If the logging share is not shared back, the output table will not be visible in your Snowflake instance.

### Step 6: Create the Input Table for Identity Resolution
Prepare your data tables from Braze’s Snowflake Data Share Connection process to be called against the applications.  

Refer to the following categories to determine which of your identifiers are eligible for resolution, then format the input table to the [required format](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html).

| Identifier Type | Description  |
|-----------------|--------------|
| Full PII        | PII (Personally Identifiable Information) includes the user's name, postal address, email, and phone number. **Note:** Not all identifiers are required for every record. |
| Email Only      | The user's email addresses, such as `alex-lee@email.com`. |
| Device          | Includes 3rd-party cookies, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs), and RampIDs (resolved to a Household RampID). |
| CIDs            | Identifiers from a platform partner or an identity sync with LiveRamp, such as your internal Customer ID. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Before preparing any PII-based tables, consider [LiveRamp’s privacy filter](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html). At a high level, these are checks that occur within a job to ensure that the attribute columns (ie non-identifiers) within your input tables do not contain values that are too unique.  This is critical to ensure consumer privacy is maintained, and to avoid the possibility of reidentification.
{% endalert %}

#### Braze available identifiers

Braze’s Event Logs provide identifiers usable within LiveRamp’s Application. For a full list of what is available per event type, download the [Braze Event Schemas and Identifiers](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Identifier Type | Description  |
|-----------------|--------------|
| `AD_ID` | Advertising IDs, such as `ios_idfa`, `google_ad_id`, `roku_ad_id`, captured within particular event types, which can be used in conjunction with LiveRamp’s Device Resolution services. By default, Advertising IDs are not collected&#8212;however, you can enable tracking by following [Braze's documentation](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Email address which can be used in conjunction with LiveRamp’s Email Only Resolution services |
| `TO_PHONE_NUMBER` | Phone number, which can be used in conjunction with LiveRamp’s PII Resolution services. |
| `EXTERNAL_USER_ID` | The external ID associated with a user, which can be used in conjunction with LiveRamp’s Device Resolution services (CID). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Use of any client/brand-specific custom identifier within LiveRamp’s application requires an identity sync with LiveRamp.
{% endalert %}

### Step 5: Set your variables

[Set your variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) for the job in the Execution Steps worksheet provided in the app. This includes details like the target database, associated tables (input data, metrics, logging), and defining the output table name.

### Step 6: Create the Metadata Table
With the variables set, you’ll then [create the metadata table](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-input-table-for-identity-resolution), which gives details on the specific job type to be executed based on the category of identifiers involved.

### Step 7: Perform the Identity Resolution operation and verify the output

For a full walkthrough, see [Perform Identity Resolution](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html).

**Operation**
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
**Output**
```sql
call check_for_output(
$output_table_name
);
```
The output will differ slightly based on the identifiers involved. Confirm that the data from Braze has been resolved to a dedicated encoding of RampID, LiveRamp’s person-based, pseudonymous identifier.

## Action on your data via LiveRamp’s Managed Service Segmentation + Activation App in Snowflake
With your data now pseudonymized to your dedicated encoding of RampID, you have the ability to share the RampID-based tables to LiveRamp’s Managed Activation Application for streamlined fulfillment to your key advertising platform partners. With this application customers see several benefits:

- **Data Minimization:** LiveRamp’s Activation app uses Snowflake’s Secure Data Share feature to effectively read the tables directly from your instance. No data is moved from Snowflake until the point of delivery to the downstream partner.
- **Secure 1st Party Activation:** By using the above Identity Resolution application, LiveRamp’s Activation application will only utilize the RampID-based tables in your Snowflake instance, and thus PII will never have to leave your walls.
- **Expedite Time to Live:** By resolving data to RampID directly in your environment, delivery to an end destination can occur within a matter of hours, as compared to several days when using LiveRamp’s more traditional file-based approach. This greatly increases the ability to optimize campaign performance in a timely manner.
- **Operational Savings:** Similar to the above, through the use of Snowflake’s Secure Data Share feature customers save time and money when compared to coordinating egress of files to LiveRamp or directly to any end destination.

The Activation Application includes a business-user friendly interface for additional segmentation and selection/configuration of downstream destination partners. For more details on the application please reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Tips and FAQs

### Snowflake Regions

This application is currently only available for US based regions. Currently these are:
  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Privacy & Column Values

The process evaluates the combination of all the column values on a per row basis for unique values. If a particular combination of column values occurs 3 or fewer times, the rows containing those column values will not be matchable and will not be returned in the output table. Likewise, to ensure privacy, the LiveRamp service assesses the uniqueness of combinations of column values, ensuring that if over 5% of the file's rows become unmatchable due to rare combinations, the job will fail.

### Historical Data

Historical data in Snowflake goes back to April 2019, but there may be slight differences in data from before August 2019 due to product changes.

### Speed, Performance, Cost

The speed and cost of queries depend on the warehouse size used. Consider your data access needs when selecting a warehouse size.

### Braze Benchmarks

Benchmarks allow you to compare your metrics with industry standards, available directly in the Snowflake Data Exchange.

### Breaking vs. Non-Breaking Changes

Be aware of changes that can affect your integration. Breaking changes will be preceded by an announcement and a migration period.

{% alert tip %}
For more specific issues or questions, reach out to [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}
