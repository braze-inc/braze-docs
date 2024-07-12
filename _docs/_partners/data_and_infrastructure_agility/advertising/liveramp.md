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

Snowflake's [Secure Data Shares](https://www.google.com/url?q=https://docs.snowflake.com/en/user-guide/data-sharing-intro&sa=D&source=editors&ust=1719246601733507&usg=AOvVaw2oeRaDOv2PuOu_DH41hQqM) does not transfer data between LiveRamp, Snowflake, and Braze. Data is only shared through Snowflake's services and metadata store, meaning no data is copied and no additional storage charges occur. Access to shared data is controlled and governed using the access controls of your Snowflake account.

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
{: .reset-td-br-1 .reset-td-br-2 }

## Setting up your secure data sharing connection

{% alert tip %}
You can find the full guide on Braze’s Snowflake Data Share within [Braze’s docs](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/&sa=D&source=editors&ust=1719246601733880&usg=AOvVaw0uRXwEAQ36JDK6yqOPtREd).
{% endalert %}

{% alert tip %}
You can view a comprehensive step-by-step process for integration and activation of the LiveRamp Snowflake Native App [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html&sa=D&source=editors&ust=1719246601734560&usg=AOvVaw1jGdc7oaM1mUYvJxjnMbJL).
{% endalert %}

### Step 1: Create a Database from the Braze share

Once the share is visible in your instance (you need to be `ACCOUNTADMIN` role to see it), you’ll need to create a database from the share so you can see and query the tables.

### Step 2: Accept the Snowflake Consumer Terms of Service

An organizational administrator (`ORGADMIN`) or a role with greater permissions must accept the Snowflake Consumer Terms of Service. Follow Snowflake's instructions for this crucial step.

### Step 3: Install the LiveRamp Identity Resolution and Transcoding Native App

To install the app, navigate to Snowsight > Marketplace. Search for the LiveRamp Identity Resolution and Transcoding native app and click "Request." Complete the form and submit it. LiveRamp will reach out to begin the contracting process. Once completed, the app will be shared with your account. Select the appropriate warehouse and click "Get" to start the installation process.

### Step 4: Perform the Initial Application Setup

Before performing any operation, you must run the Application Setup SQL. This setup will set necessary variables, create an integration to LiveRamp's auth API, and create logging and metrics tables to share back to LiveRamp. Make sure to follow the provided setup SQL for a seamless integration.

### Step 5: Configure Logging and Metrics Tables

The native app logs activity and aggregates event data into metrics. These tables need to be shared back to LiveRamp to validate the metrics and make the output table visible. If the logging share is not shared back, the output table will not be visible in your Snowflake instance.

### Step 6: Prepare your Data and Execute the Identity Resolution Operations

With the application installed, the next step is to prepare your data tables from Braze’s Snowflake Data Share Connection process to be called against the applications. 

First, you’ll want to determine which identifiers within your tables are eligible for resolution. LiveRamp’s application categorizes identifiers into four buckets, each with a defined input format:

- **Full PII:**
  - Name
  - Postal Address
  - Email
  - Phone Number

  *Not all of the above are required for every record*

- **Email Only**

- **Device:**
  - 3rd party cookies
  - MAIDs (mobile device IDs)
  - CTV IDs (Connected TV IDs)
  - RampIDs (in this case to be resolved to a Household RampID)

- **CIDs:**
  - Custom Identifiers from a platform partner, or one with which you have directly established an identity sync with LiveRamp, such as your internal Customer ID.

Once you have determined the above, you’ll format the input table to the corresponding format detailed [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23create-the-input-table-for-identity-resolution&sa=D&source=editors&ust=1719246601736752&usg=AOvVaw38ol2WtnfAok_ZRIBUQl-u).

**Privacy Filters:** When preparing PII-based tables, it is important to consider LiveRamp’s [privacy filter](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23privacy-filter-43&sa=D&source=editors&ust=1719246601737101&usg=AOvVaw3NQ6SObT5HUCnVsysBpxRp) process. At a high level, these are checks that occur within a job to ensure that the attribute columns (ie non-identifiers) within your input tables do not contain values that are too unique. This is critical to ensure consumer privacy is maintained, and to avoid the possibility of reidentification.

Braze’s Event Logs provide a variety of identifiers that can be used within LiveRamp’s Application, specifically:
- **AD_ID** - Advertising IDs (ios_idfa, google_ad_id, roku_ad_id), captured within particular event types, which can be used in conjunction with LiveRamp’s Device Resolution services.

{% alert important %}
Ad IDs are not collected by default, follow the [Braze developer documentation](https://www.google.com/url?q=https://www.braze.com/docs/developer_guide/home&sa=D&source=editors&ust=1719246601737523&usg=AOvVaw0qO5YCQXnx1R3JNGfJAzTh) to turn on AD ID tracking.
{% endalert %}

- **EMAIL_ADDRESS** - email address which can be used in conjunction with LiveRamp’s Email Only Resolution services
- **TO_PHONE_NUMBER** - Phone number of user was exposed via an SMS campaign, which can be used in conjunction with LiveRamp’s PII Resolution services.
- **EXTERNAL_USER_ID** - external ID tied to user, which can be used in conjunction with LiveRamp’s Device Resolution services (CID).

{% alert important %}
Use of any client/brand-specific custom identifier within LiveRamp’s application will require an identity sync to be established with LiveRamp.
{% endalert %}

{% alert note %}
A list of all of Braze’s available event schemas can be found [here](https://www.google.com/url?q=https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt?3e7258ef1caf19c2417b5616f6bbea54&sa=D&source=editors&ust=1719246601738023&usg=AOvVaw0vbXqrELRHekKKeEOG7iA6).
{% endalert %}

### Step 7: Specify your variables

The next step will be to [specify the variables](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23specify-the-variables-43-150727&sa=D&source=editors&ust=1719246601738460&usg=AOvVaw0xhZyJVnj0CcJnvIUF2D2f) for the job within the Execution Steps worksheet provided in the app, which includes details such as the target database where the job will run, the associated tables (input data, metrics, logging), as well as defining what the output table should be named.

With the variables set, you’ll then create the [metadata table](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23create-the-metadata-table-43&sa=D&source=editors&ust=1719246601738881&usg=AOvVaw1T0JZt_ROBE-MNMeFBytpe), which gives details on the specific job type to be executed based on the category of identifiers involved.

### Step 8: Check the output

Run the operation, then check your output. The output will look slightly different based on the identifiers involved. The primary modification from input to output involves the removal of any identifiers originally used to generate the LiveRamp identifier in the input table, with these being substituted by the LiveRamp Identifier itself.

```
call check_for_output(
$output_table_name
);
```

{% alert note %}
The full process is outlined [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html&sa=D&source=editors&ust=1719246601740211&usg=AOvVaw2yTdhM5puVwdAGS0R0g56s) within LiveRamp’s documentation.
{% endalert %}

## Transcoding and collaboration

LiveRamp also offers a native application to transcode data from one partner’s RampID encoding to your own encoding, or vice-versa. This allows for secure collaboration with your key partners directly in Snowflake, while alleviating the need to deliver directly identifiable customer data. [See here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-rampid-transcoding-in-snowflake.html%23perform-rampid-transcoding-in-snowflake&sa=D&source=editors&ust=1719246601741396&usg=AOvVaw1BBj3bm81yIeAb_CRLZ9jd) for more details or reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Troubleshooting

- **Snowflake Regions:** This application is currently only available for US based regions. Currently these are:
  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425
- **Privacy & Column Values:** The process evaluates the combination of all the column values on a per row basis for unique values. If a particular combination of column values occurs 3 or fewer times, the rows containing those column values will not be matchable and will not be returned in the output table. Likewise, to ensure privacy, the LiveRamp service assesses the uniqueness of combinations of column values, ensuring that if over 5% of the file's rows become unmatchable due to rare combinations, the job will fail.
- **Historical Data:** Historical data in Snowflake goes back to April 2019, but there may be slight differences in data from before August 2019 due to product changes.
- **Speed, Performance, Cost:** The speed and cost of queries depend on the warehouse size used. Consider your data access needs when selecting a warehouse size.
- **Braze Benchmarks:** Benchmarks allow you to compare your metrics with industry standards, available directly in the Snowflake Data Exchange.
- **Breaking vs. Non-Breaking Changes:** Be aware of changes that can affect your integration. Breaking changes will be preceded by an announcement and a migration period.

For more specific issues or questions, please reach out to [martech@liveramp.com](mailto:martech@liveramp.com).
