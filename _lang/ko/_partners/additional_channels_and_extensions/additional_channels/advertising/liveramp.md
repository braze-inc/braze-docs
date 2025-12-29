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

{% alert important %}
Snowflake's [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro) does not transfer data between LiveRamp, Snowflake, and Braze. Data is only shared through Snowflake's services and metadata store, meaning no data is copied and no additional storage charges occur. Access to shared data is controlled and governed using the access controls of your Snowflake account.
{% endalert %}

## Use cases

- **Data Minimization:** LiveRamp’s Activation app uses Snowflake’s Secure Data Share feature to effectively read the tables directly from your instance. No data is moved from Snowflake until the point of delivery to the downstream partner.
- **Secure 1st Party Activation:** By using the above Identity Resolution application, LiveRamp’s Activation application will only utilize the RampID-based tables in your Snowflake instance, and thus PII will never have to leave your walls.
- **Expedite Time to Live:** By resolving data to RampID directly in your environment, delivery to an end destination can occur within a matter of hours, as compared to several days when using LiveRamp’s more traditional file-based approach. This greatly increases the ability to optimize campaign performance in a timely manner.
- **Operational Savings:** Similar to the above, through the use of Snowflake’s Secure Data Share feature customers save time and money when compared to coordinating egress of files to LiveRamp or directly to any end destination.

## Prerequisites

| Prerequisite       | Description                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake Account | You need a Snowflake account with admin-level permissions.                                                                                                                                      |
| LiveRamp Account  | Reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com) to discuss the required LiveRamp applications within Snowflake.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Setting up the integration

### Step 1: Request a data share from Braze

First, reach out to your Braze account manager or customer success manager to purchase a Snowflake Data Share Connector for your Braze account. When you request a data share, Braze will provision the share from the workspace(s) that the share was purchased. After the share is provisioned, all data is immediately accessible from within your Snowflake instance in the form of an incoming data share. Once the share is visible in your instance create a database from the share so you can see and query the tables.

For a full walkthrough, see [Snowflake integration guide with Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Step 2: Set up the LiveRamp app in Snowflake 

Translation and identity resolution capabilities are available within Snowflake through the LiveRamp Identity Resolution and Translation native app, which creates a share to your account, opening up a view to query the reference dataset from within your own Snowflake environment.

To set up the native app, follow these steps on the LiveRamp docs: [Set Up the LiveRamp Native App in Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). When you're finished, continue to the next step.

### Step 3: Create a data table

{% alert warning %}
Before preparing any PII-based tables, be sure you understand [LiveRamp’s privacy filter](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) which is run during jobs to ensure that the attribute columns (non-identifiers) in your input tables do not contain values that are too unique. This is critical for maintaining consumer privacy and avoiding reidentification.
{% endalert %}

Next, create a data table with the [required format](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) that will be called against the LiveRamp native app. Refer to the following categories to determine which of your identifiers are eligible for resolution:

| Identifier Type | Description  |
|-----------------|--------------|
| Full PII        | Personally identifiable information (PII) includes the user's name, postal address, email, and phone number. **Note:** Not all identifiers are required for every record. |
| Email Only      | The user's email addresses, such as `alex-lee@email.com`. |
| Device          | This includes 3rd-party cookies, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs), and RampIDs (resolved to a Household RampID). |
| CIDs            | These are identifiers from a platform partner or an identity sync with LiveRamp, such as your internal Customer ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Braze identifiers

Braze’s event logs contain identifiers you can use within the LiveRamp native app. For a full list of available identifiers for each event type, download the [Braze Event Schemas and Identifiers]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

| Identifier Type | Description  |
|-----------------|--------------|
| `AD_ID` | Advertising IDs, such as `ios_idfa`, `google_ad_id`, `roku_ad_id`, captured within particular event types, which can be used in conjunction with LiveRamp’s Device Resolution services. By default, Advertising IDs are not collected—however, you can enable tracking by following [Braze documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Email address which can be used in conjunction with LiveRamp’s Email Only Resolution services |
| `TO_PHONE_NUMBER` | Phone number, which can be used in conjunction with LiveRamp’s PII Resolution services. |
| `EXTERNAL_USER_ID` | The external ID associated with a user, which can be used in conjunction with LiveRamp’s Device Resolution services (CID). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
The use of any client or brand-specific custom identifiers within LiveRamp’s application requires an [identity sync with LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Step 4: Set your variables

Next, set your variables for the job in the Execution Steps worksheet provided in the app. This includes details like the target database, associated tables (input data, metrics, logging), and defining the output table name. For a full walkthrough, see [LiveRamp: Specify the Variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Step 5: Create the metadata table for PII resolution

Now that your variables are set, create the metadata table for PII resolution. This will give details on the specific job type to be executed based on the category of identifiers involved. For a full walkthrough, see [LiveRamp: Create the Metadata Table](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Step 6: Perform the identity resolution operation

Finally, perform the identity resolution operation. For a full walkthrough, see [LiveRamp: Perform the Identity Resolution Operation](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab example input %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Next steps

With your data now pseudonymized to your dedicated encoding of RampID, you have the ability to share the RampID-based tables to LiveRamp’s Managed Activation Application for streamlined fulfillment to your key advertising platform partners. The Activation Application includes a business-user friendly interface for additional segmentation and selection/configuration of downstream destination partners. For more details on the application please reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Troubleshooting

{% alert note %}
If you have more specific issues or questions, reach out to [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Snowflake Regions

Currently, this application is only available for the following US-based regions:

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
