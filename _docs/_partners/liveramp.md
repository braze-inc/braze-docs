---
nav_title: LiveRamp
article_title: LiveRamp
description: "SHORT_DESCRIPTION."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Connecting LiveRamp, Snowflake, and Braze

> Unlocking the full potential of your customer engagement and campaign data has never been easier with the seamless integration of Braze, Snowflake, and LiveRamp. This integration empowers you to create highly personalized and relevant marketing campaigns by reducing the time to insights, breaking down data silos, and optimizing customer engagement.

## Why This Integration Matters:

This integration is a game-changer for data-driven marketing. Here's why it matters:

- **Actionable Person & Household Based Insights:** Consolidation of consumer touchpoints to a person-based view enables a more accurate understanding of consumer preferences for better audience segmentation, testing, and model building across LiveRamp & Braze. Providing you a holistic and actionable view across both your marketing and advertising engagements in a single cloud environment.
- **Reduce Time to Insights:** Access customer engagement and campaign data in real-time, eliminating the need for time-consuming ETL processes. This means you can base your customer experiences on the most up-to-date information, enhancing the timeliness and relevance of your campaigns.
- **Break Down Data Silos & Interoperability:** Create a comprehensive view of your customers across various channels and platforms. Data becomes more valuable when you can effectively connect it to an ecosystem, and LiveRamp Identity solutions combined with Braze can be flexibly applied to sophisticated customer use cases and are integrated as an identity layer across the ecosystem.
- **Optimize Customer Engagement:** Leverage [Braze Benchmarks](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/%23braze-benchmarks&sa=D&source=editors&ust=1719246601732592&usg=AOvVaw0zjg0fsIH0dk618YMiPrGC), powered by Snowflake, to compare your brand's engagement data to LiveRamp ROAS and benchmarks across channels, industries, and platforms. This valuable insight helps fine-tune your marketing strategies.

Let's dive into the technical details of how to complete the integration from Braze to LiveRamp and set up the app in LiveRamp.

## Prerequisites:

- **Snowflake Account:** You need a Snowflake account with admin-level permissions.
- **Braze Account:** Reach out to your Braze Account or customer success manager to consult Braze data strategy services on Secure Data Sharing with Snowflake and to purchase their Snowflake Data Share Connector.
- **LiveRamp Account:** Reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com) to discuss the required LiveRamp applications within Snowflake.

## About Snowflake Secure Data Shares:

The integration with [Secure Data Shares](https://www.google.com/url?q=https://docs.snowflake.com/en/user-guide/data-sharing-intro&sa=D&source=editors&ust=1719246601733507&usg=AOvVaw2oeRaDOv2PuOu_DH41hQqM) does not involve the actual transfer of data between accounts. Data sharing is facilitated through Snowflake's services layer and metadata store, which means no data is copied, and there are no additional storage charges for consumers. Access to shared data is controlled and governed using the access controls of your Snowflake account.

## Setting up a Braze Secure Data Sharing Connection

You can find the full guide on Braze’s Snowflake Data Share within [Braze’s docs](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/&sa=D&source=editors&ust=1719246601733880&usg=AOvVaw0uRXwEAQ36JDK6yqOPtREd).

## Step 1: Create a Database from the Braze share

Once the share is visible in your instance (you need to be `ACCOUNTADMIN` role to see it), you’ll need to create a database from the share so you can see and query the tables.

## Step 2: Set up Native Identity Resolution Application in Snowflake

You can view a comprehensive step-by-step process for integration and activation of the LiveRamp Snowflake Native App [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html&sa=D&source=editors&ust=1719246601734560&usg=AOvVaw1jGdc7oaM1mUYvJxjnMbJL).

#### Step 2.1: Accept the Snowflake Consumer Terms of Service

An organizational administrator (ORGADMIN) or a role with greater permissions must accept the Snowflake Consumer Terms of Service. Follow Snowflake's instructions for this crucial step.

#### Step 2.2: Install the LiveRamp Identity Resolution and Transcoding Native App

To install the app, navigate to Snowsight > Marketplace. Search for the LiveRamp Identity Resolution and Transcoding native app and click "Request." Complete the form and submit it. LiveRamp will reach out to begin the contracting process. Once completed, the app will be shared with your account. Select the appropriate warehouse and click "Get" to start the installation process.

#### Step 2.3: Perform the Initial Application Setup

Before performing any operation, you must run the Application Setup SQL. This setup will set necessary variables, create an integration to LiveRamp's auth API, and create logging and metrics tables to share back to LiveRamp. Make sure to follow the provided setup SQL for a seamless integration.

#### Step 2.4: Configure Logging and Metrics Tables

The native app logs activity and aggregates event data into metrics. These tables need to be shared back to LiveRamp to validate the metrics and make the output table visible. If the logging share is not shared back, the output table will not be visible in your Snowflake instance.

#### Step 2.5: Prepare your Data and Execute the Identity Resolution Operations

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

  *Ad IDs are not collected by default, follow the [Braze developer documentation](https://www.google.com/url?q=https://www.braze.com/docs/developer_guide/home&sa=D&source=editors&ust=1719246601737523&usg=AOvVaw0qO5YCQXnx1R3JNGfJAzTh) to turn on AD ID tracking.*

- **EMAIL_ADDRESS** - email address which can be used in conjunction with LiveRamp’s Email Only Resolution services
- **TO_PHONE_NUMBER** - Phone number of user was exposed via an SMS campaign, which can be used in conjunction with LiveRamp’s PII Resolution services.
- **EXTERNAL_USER_ID** - external ID tied to user, which can be used in conjunction with LiveRamp’s Device Resolution services (CID).

  *Use of any client/brand-specific custom identifier within LiveRamp’s application will require an identity sync to be established with LiveRamp.*

NOTE: A list of all of Braze’s available event schemas can be found [here](https://www.google.com/url?q=https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt?3e7258ef1caf19c2417b5616f6bbea54&sa=D&source=editors&ust=1719246601738023&usg=AOvVaw0vbXqrELRHekKKeEOG7iA6).

### Step 2.6: Specify your variables

The next step will be to [specify the variables](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23specify-the-variables-43-150727&sa=D&source=editors&ust=1719246601738460&usg=AOvVaw0xhZyJVnj0CcJnvIUF2D2f) for the job within the Execution Steps worksheet provided in the app, which includes details such as the target database where the job will run, the associated tables (input data, metrics, logging), as well as defining what the output table should be named.

With the variables set, you’ll then create the [metadata table](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23create-the-metadata-table-43&sa=D&source=editors&ust=1719246601738881&usg=AOvVaw1T0JZt_ROBE-MNMeFBytpe), which gives details on the specific job type to be executed based on the category of identifiers involved.

### Step 2.7: Check the output

With the above set, first run the operation.

```

markdown
Copy code
# Connecting LiveRamp, Snowflake, and Braze

> Unlocking the full potential of your customer engagement and campaign data has never been easier with the seamless integration of Braze, Snowflake, and LiveRamp. This integration empowers you to create highly personalized and relevant marketing campaigns by reducing the time to insights, breaking down data silos, and optimizing customer engagement.

## Why This Integration Matters:

This integration is a game-changer for data-driven marketing. Here's why it matters:

- **Actionable Person & Household Based Insights:** Consolidation of consumer touchpoints to a person-based view enables a more accurate understanding of consumer preferences for better audience segmentation, testing, and model building across LiveRamp & Braze. Providing you a holistic and actionable view across both your marketing and advertising engagements in a single cloud environment.
- **Reduce Time to Insights:** Access customer engagement and campaign data in real-time, eliminating the need for time-consuming ETL processes. This means you can base your customer experiences on the most up-to-date information, enhancing the timeliness and relevance of your campaigns.
- **Break Down Data Silos & Interoperability:** Create a comprehensive view of your customers across various channels and platforms. Data becomes more valuable when you can effectively connect it to an ecosystem, and LiveRamp Identity solutions combined with Braze can be flexibly applied to sophisticated customer use cases and are integrated as an identity layer across the ecosystem.
- **Optimize Customer Engagement:** Leverage [Braze Benchmarks](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/%23braze-benchmarks&sa=D&source=editors&ust=1719246601732592&usg=AOvVaw0zjg0fsIH0dk618YMiPrGC), powered by Snowflake, to compare your brand's engagement data to LiveRamp ROAS and benchmarks across channels, industries, and platforms. This valuable insight helps fine-tune your marketing strategies.

Let's dive into the technical details of how to complete the integration from Braze to LiveRamp and set up the app in LiveRamp.

## Prerequisites:

- **Snowflake Account:** You need a Snowflake account with admin-level permissions.
- **Braze Account:** Reach out to your Braze Account or customer success manager to consult Braze data strategy services on Secure Data Sharing with Snowflake and to purchase their Snowflake Data Share Connector.
- **LiveRamp Account:** Reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com) to discuss the required LiveRamp applications within Snowflake.

## About Snowflake Secure Data Shares:

The integration with [Secure Data Shares](https://www.google.com/url?q=https://docs.snowflake.com/en/user-guide/data-sharing-intro&sa=D&source=editors&ust=1719246601733507&usg=AOvVaw2oeRaDOv2PuOu_DH41hQqM) does not involve the actual transfer of data between accounts. Data sharing is facilitated through Snowflake's services layer and metadata store, which means no data is copied, and there are no additional storage charges for consumers. Access to shared data is controlled and governed using the access controls of your Snowflake account.

## Setting up a Braze Secure Data Sharing Connection

You can find the full guide on Braze’s Snowflake Data Share within [Braze’s docs](https://www.google.com/url?q=https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/&sa=D&source=editors&ust=1719246601733880&usg=AOvVaw0uRXwEAQ36JDK6yqOPtREd).

## Step 1: Create a Database from the Braze share

Once the share is visible in your instance (you need to be `ACCOUNTADMIN` role to see it), you’ll need to create a database from the share so you can see and query the tables.

## Step 2: Set up Native Identity Resolution Application in Snowflake

You can view a comprehensive step-by-step process for integration and activation of the LiveRamp Snowflake Native App [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html&sa=D&source=editors&ust=1719246601734560&usg=AOvVaw1jGdc7oaM1mUYvJxjnMbJL).

#### Step 2.1: Accept the Snowflake Consumer Terms of Service

An organizational administrator (ORGADMIN) or a role with greater permissions must accept the Snowflake Consumer Terms of Service. Follow Snowflake's instructions for this crucial step.

#### Step 2.2: Install the LiveRamp Identity Resolution and Transcoding Native App

To install the app, navigate to Snowsight > Marketplace. Search for the LiveRamp Identity Resolution and Transcoding native app and click "Request." Complete the form and submit it. LiveRamp will reach out to begin the contracting process. Once completed, the app will be shared with your account. Select the appropriate warehouse and click "Get" to start the installation process.

#### Step 2.3: Perform the Initial Application Setup

Before performing any operation, you must run the Application Setup SQL. This setup will set necessary variables, create an integration to LiveRamp's auth API, and create logging and metrics tables to share back to LiveRamp. Make sure to follow the provided setup SQL for a seamless integration.

#### Step 2.4: Configure Logging and Metrics Tables

The native app logs activity and aggregates event data into metrics. These tables need to be shared back to LiveRamp to validate the metrics and make the output table visible. If the logging share is not shared back, the output table will not be visible in your Snowflake instance.

#### Step 2.5: Prepare your Data and Execute the Identity Resolution Operations

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

  *Ad IDs are not collected by default, follow the [Braze developer documentation](https://www.google.com/url?q=https://www.braze.com/docs/developer_guide/home&sa=D&source=editors&ust=1719246601737523&usg=AOvVaw0qO5YCQXnx1R3JNGfJAzTh) to turn on AD ID tracking.*

- **EMAIL_ADDRESS** - email address which can be used in conjunction with LiveRamp’s Email Only Resolution services
- **TO_PHONE_NUMBER** - Phone number of user was exposed via an SMS campaign, which can be used in conjunction with LiveRamp’s PII Resolution services.
- **EXTERNAL_USER_ID** - external ID tied to user, which can be used in conjunction with LiveRamp’s Device Resolution services (CID).

  *Use of any client/brand-specific custom identifier within LiveRamp’s application will require an identity sync to be established with LiveRamp.*

NOTE: A list of all of Braze’s available event schemas can be found [here](https://www.google.com/url?q=https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt?3e7258ef1caf19c2417b5616f6bbea54&sa=D&source=editors&ust=1719246601738023&usg=AOvVaw0vbXqrELRHekKKeEOG7iA6).

### Step 2.6: Specify your variables

The next step will be to [specify the variables](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23specify-the-variables-43-150727&sa=D&source=editors&ust=1719246601738460&usg=AOvVaw0xhZyJVnj0CcJnvIUF2D2f) for the job within the Execution Steps worksheet provided in the app, which includes details such as the target database where the job will run, the associated tables (input data, metrics, logging), as well as defining what the output table should be named.

With the variables set, you’ll then create the [metadata table](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html%23create-the-metadata-table-43&sa=D&source=editors&ust=1719246601738881&usg=AOvVaw1T0JZt_ROBE-MNMeFBytpe), which gives details on the specific job type to be executed based on the category of identifiers involved.

### Step 2.7: Check the output

With the above set, first run the operation.

call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```


Then check your output. The output will look slightly different based on the identifiers involved. The primary modification from input to output involves the removal of any identifiers originally used to generate the LiveRamp identifier in the input table, with these being substituted by the LiveRamp Identifier itself.

```
call check_for_output(
$output_table_name
);
```


NOTE: The full process is outlined [here](https://www.google.com/url?q=https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html&sa=D&source=editors&ust=1719246601740211&usg=AOvVaw2yTdhM5puVwdAGS0R0g56s) within LiveRamp’s documentation.

## Use cases

With your data now pseudonymized to your dedicated encoding of RampID, you have the ability to share the RampID-based tables to LiveRamp’s Managed Activation Application for streamlined fulfillment to your key advertising platform partners. With this application customers see several benefits:

- **Data Minimization:** LiveRamp’s Activation app uses Snowflake’s Secure Data Share feature to effectively read the tables directly from your instance. No data is moved from Snowflake until the point of delivery to the downstream partner.
- **Secure 1st Party Activation:** By using the above Identity Resolution application, LiveRamp’s Activation application will only utilize the RampID-based tables in your Snowflake instance, and thus PII will never have to leave your walls.
- **Expedite Time to Live:** By resolving data to RampID directly in your environment, delivery to an end destination can occur within a matter of hours, as compared to several days when using LiveRamp’s more traditional file-based approach. This greatly increases the ability to optimize campaign performance in a timely manner.
- **Operational Savings:** Similar to the above, through the use of Snowflake’s Secure Data Share feature customers save time and money when compared to coordinating egress of files to LiveRamp or directly to any end destination.

The Activation Application includes a business-user friendly interface for additional segmentation and selection/configuration of downstream destination partners. For more details on the application please reach out to your LiveRamp account team or [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Transcoding and Collaboration

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
