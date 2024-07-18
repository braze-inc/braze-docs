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

## About data sharing

Snowflake's [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro) does not transfer data between LiveRamp, Snowflake, and Braze. Data is only shared through Snowflake's services and metadata store, meaning no data is copied and no additional storage charges occur. Access to shared data is controlled and governed using the access controls of your Snowflake account.

## Use cases

With your data now pseudonymized to your dedicated encoding of RampID, you have the ability to share the RampID-based tables to LiveRamp’s Managed Activation Application for streamlined fulfillment to your key advertising platform partners. With this application customers see several benefits:

- **Data Minimization:** LiveRamp’s Activation app uses Snowflake’s Secure Data Share feature to effectively read the tables directly from your instance. No data is moved from Snowflake until the point of delivery to the downstream partner.
- **Secure 1st Party Activation:** By using the above Identity Resolution application, LiveRamp’s Activation application will only utilize the RampID-based tables in your Snowflake instance, and thus PII will never have to leave your walls.
- **Expedite Time to Live:** By resolving data to RampID directly in your environment, delivery to an end destination can occur within a matter of hours, as compared to several days when using LiveRamp’s more traditional file-based approach. This greatly increases the ability to optimize campaign performance in a timely manner.
- **Operational Savings:** Similar to the above, through the use of Snowflake’s Secure Data Share feature customers save time and money when compared to coordinating egress of files to LiveRamp or directly to any end destination.

The Activation Application includes a business-user friendly interface for additional segmentation and selection/configuration of downstream destination partners. For more details on the application please reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Prerequisites

| Prerequisite       | Description                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake Account | You need a Snowflake account with admin-level permissions.                                                                                                                                      |
| Braze Account     | Reach out to your Braze Account or customer success manager to consult Braze data strategy services on Secure Data Sharing with Snowflake and to purchase their Snowflake Data Share Connector. |
| LiveRamp Account  | Reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com) to discuss the required LiveRamp applications within Snowflake.                              |
| A Snowflake Braze integration | To integrate Snowflake with Braze, see [Snowflake integration guide]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/).                             |
{: .reset-td-br-1 .reset-td-br-2 }

## Setting up your secure data sharing connection

### Step 1: Create a database using the Braze share

To view the Braze share, you'll need `ACCOUNTADMIN` permissions in LiveRamp. After you create your database using the Braze share, you'll be able to access and query the data table.

### Step 2: Install the LiveRamp app on Snowflake

In Snowflake, go to **Snowsight** > **Marketplace**, then request [LiveRamp Identity Resolution and Translation](https://app.snowflake.com/marketplace/listing/GZT0Z11US7AT/liveramp-identity-resolution-and-translation?search=LiveRamp%20Identity%20Resolution) app. After your request is approved, choose the relevant warehouse, then select **Get** to install them to your account.

### Step 3: Set up the LiveRamp app

To set necessary variables, run **Application Setup SQL**. When you're finished,  create an integration to LiveRamp's auth API, then create create logging and metrics tables to share back to LiveRamp.

### Step 4: Format your table's identifiers

Refer to the following categories to determine which of your identifiers are eligible for resolution, then format the input table to the corresponding format detailed [here](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html).

| Identifier Type | Description  |
|-----------------|--------------|
| Full PII        | - Name<br>- Postal Address<br>- Email<br>- Phone Number <br>*Not all are required for every record* |
| Email Only      | Emails             |
| Device          | - 3rd party cookies<br>- MAIDs (mobile device IDs)<br>- CTV IDs (Connected TV IDs)<br>- RampIDs (resolved to a Household RampID) |
| CIDs            | Custom Identifiers from a platform partner or an identity sync with LiveRamp, such as your internal Customer ID. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Before preparing any PII-based tables, consider using [LiveRamp’s privacy filter](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html). This will ensure that the attribute columns in your input tables do not contain values that are too unique, so you can maintain consumer privacy and avoid re-identification.
{% endalert %}

#### Braze identifiers

Braze’s Event Logs provide identifiers usable within LiveRamp’s Application. You can download the full list [Braze Event Schemas](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Identifier Type | Description  |
|-----------------|--------------|
| `AD_ID`           | The advertising IDs used for LiveRamp’s Device Resolution services, such as `ios_idfa`, `google_ad_id`, `roku_ad_id`. By default, Advertising IDs are not collected&#8212;however, you can enable tracking using [`Braze.setGoogleAdvertisingId()`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection). |
| `EMAIL_ADDRESS`   | The emails used for LiveRamp’s Email Only Resolution services. |
| `TO_PHONE_NUMBER` | The phone number that will be exposed via SMS campaigns for LiveRamp’s PII Resolution services. |
| `EXTERNAL_USER_ID` | The external ID associated with a user for LiveRamp’s Device Resolution services (CID). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Use of any client/brand-specific custom identifier within LiveRamp’s application requires an identity sync with LiveRamp.
{% endalert %}

### Step 5: Set your variables

[Set your variables](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) for the job in the Execution Steps worksheet provided in the app. This includes details like the target database, associated tables (input data, metrics, logging), and defining the output table name.

### Step 6: Verify the output

To verify your output, run the following code and confirm that your previous identifiers were replaced with your LiveRamp Identifier. For a full walkthrough, see [Perform Identity Resolution](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html).

```sql
call check_for_output(
$output_table_name
);
```

## Troubleshooting

{% alert tip %}
If you're still having trouble after trying these troubleshooting steps, please reach out to [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

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
