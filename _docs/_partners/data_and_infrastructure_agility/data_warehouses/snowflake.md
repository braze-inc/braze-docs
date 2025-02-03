---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "This reference article outlines the partnership between Braze and Snowflake, a purpose-built SQL cloud data warehouse for all of your data and users."
page_type: partner
search_tag: Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) is a purpose-built SQL cloud data warehouse provided as Software-as-a-Service (SaaS). Snowflake provides a data warehouse that is faster, easier to use, and far more flexible than traditional data warehouse offerings. With Snowflake's unique and patented architecture, it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Personalized and relevant marketing campaigns require in-the-moment access to data. That's why Braze teamed up with Snowflake to launch data sharing. This joint offering enables marketers to unlock the potential of their customer engagement and campaign data faster than ever before.

The [Braze and Snowflake integration](https://www.braze.com/perspectives/article/snowflake-partner-announcement) leverages Snowflake's data exchange to build a presence, find new customers, and expand reach through the ever-growing Snowflake customer base.

{% alert tip %}
**Interested in having access to Snowflake-level data without the need for a Snowflake account?**<br>Check out [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts). With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze.
{% endalert %}

## What is Data Sharing?

Snowflake's [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) functionality allows Braze to give you secure access to data on our Snowflake portal without worrying about workflow friction or slowdown, failure points, and unnecessary costs that come with typical data provider relationships. Data sharing can be set up through the following integration or through [Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts).

- **Reduce time to insights**<br>Say goodbye to ETL processes that take weeks to build out. Braze and Snowflake's unique architectures make all customer engagement and campaign data immediately accessible and queryable from the instant it arrives in the data lake. No data is copied or moved, so you can deliver customer experiences based on only the most relevant, up-to-date information.
- **Break down data silos**<br>Create a holistic view of your customers across channels and platforms. Data sharing makes joining your Braze customer engagement data with all of your other Snowflake data easier than ever—creating richer insights across a single, reliable source of truth.
- **See how your engagement stacks up**<br>Optimize your customer engagement strategies with Braze Benchmarks. This interactive tool, powered by Braze and Snowflake, allows you to compare your brand's engagement data to benchmarks across channels, industry, and device platforms.

With data sharing, no actual data is copied or transferred between accounts. All sharing is accomplished through Snowflake's unique services layer and metadata store. This is an important concept because shared data does not take up any storage in a consumer account and, therefore, does not contribute to the consumer's monthly data storage charges. The **only** charges to consumers are for the computing resources (such as virtual warehouses) used to query the shared data.

Additionally, using Snowflake's built-in roles and permissions capabilities, access to data shared from Braze can be controlled and governed using the access controls already in place for your Snowflake account and the data therein. Access can be restricted and monitored the same way as your own data.

Check out [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work) to read more about how Snowflake's data sharing works.

## Prerequisites

If you are interested in this integration, reach out to your Braze Account or customer success manager and ask them to consult Braze data strategy services on Secure Data Sharing with Snowflake. This will get the cogs going inside Braze, and we'll have your views set up in no time!

| Requirement | Description |
| ----------- | ----------- |
| Snowflake account | A Snowflake account with admin-level permissions is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To set Secure Data Sharing with your Braze account, follow these steps.

1. Navigate to **Partner Integrations** > **Data Sharing** in the Braze dashboard.
2. Enter your Snowflake account details. To find your Snowflake `account_locator`, run `SELECT CURRENT_ACCOUNT()` in the destination account.
3. If you're using a CRR share, specify the cloud provider and region.
4. Select **Create Datashare**.

Within a few moments, your data share should be visible in your Snowflake instance. Create a database from the share so you can see and query the tables. Note that you'll need to be an account admin to see the data share.

![Inbound data share]({% image_buster /assets/img/inbound-data-share.png %})

In the context of data sharing, Braze is a [data provider](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)&#8212;any Snowflake account that creates shares and makes them available to other Snowflake accounts to consume. You are a [data consumer](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)&#8212;any account that chooses to create a database from a share made available by a data provider.

## Usage and visualization

After the data share is provisioned, you will need to create a database from the incoming data share, making all the tables shared appear in your Snowflake instance and be queryable just like any other data you're storing in your instance. However, keep in mind that the shared data is read-only and can only be queried but not modified or deleted in any way.

Similar to Currents, you can use your Snowflake Secure Data Sharing to:
- Create complex reports
- Perform attribution modeling
- Secure sharing within your own company
- Map raw event or user data to a CRM (like Salesforce)
- And more

[Download the raw table schemas here.][schemas]

### User ID schema

Note the following differences between Braze and Snowflake naming conventions for user IDs.

| Braze schema | Snowflake schema | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | The unique identifier that is automatically assigned by Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | The unique identifier of a user's profile that is set by the customer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Important information and limitations

### Breaking versus non-breaking changes

#### Non-breaking changes
Non-breaking changes can happen at any time and generally provide additional functionality. Examples of non-breaking changes:
- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using `SELECT *` queries. Alternately, you might want to create views that explicitly name columns and then query those views instead of the tables directly.
{% endalert %}

#### Breaking changes
When possible, breaking changes will be preceded by an announcement and a migration period. Examples of breaking changes include:
- Removing a table or view
- Removing a column from an existing table or view
- Changing the type or nullability of an existing column

### Snowflake regions
Braze currently hosts all user-level data in the Snowflake AWS US East-1 and EU-Central (Frankfurt) regions. For users outside of those regions, Braze can provide data sharing to joint customers who are hosting their Snowflake infrastructure across any AWS, Azure, or GCP region.

### Data Retention

#### Retention Policy
Any data older than two years will be archived and moved to long term storage. As part of the archival process, all events are anonymized and any personal identifiable information (PII) sensitive fields are stripped out (this includes optionally PII fields like `properties`). Archived data still contains the `user_id` field, which allows for per-user analytics across all events data.

You will be able to query against the most recent two years of data for each event in the corresponding `USERS_*_SHARED` view. Additionally, each event will have a `USERS_*_SHARED_ALL` view which can be queried against to return both anonymized and non-anonymized data.

#### Historical data
The archive of historical event data in Snowflake goes back to April 2019. In the first few months of Braze storing data in Snowflake, product changes were made that may have resulted in some of that data looking slightly different or having some null values (as we weren't passing data into every available field at this time). It's best to assume that any results that include data before August 2019 may look slightly different from expectations.

### General Data Protection Regulation (GDPR) compliance
Nearly every event record Braze stores includes a few fields representing users' personally identifiable information (PII). Some events may include email address, phone number, device ID, language, gender, and location information. If a user's request to be forgotten is submitted to Braze, we will null out those PII fields for any event belonging to those users. This way, we're not removing the historical record of the event, but now the event can never be tied back to a specific individual.

### Speed, performance, cost of queries
The speed, performance, and cost of any query run on top of the data are determined by the warehouse size you use to query the data. In some cases, depending on how much data you're accessing for analytics, you may find that you need to use a larger warehouse size for the query to be successful. Snowflake has excellent resources available about how to best determine which size to use including [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) and [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

## Braze Benchmarks

Benchmarks, [a data tool built by Braze](https://www.braze.com/perspectives/benchmarks), allows Braze prospects and customers to see how they compare to top players in their industry by comparing their metrics against Braze's industry benchmarks.

The initial industries include:
- Delivery services
- Ecommerce
- Education
- Entertainment
- Finance
- Gaming
- Health
- Lifestyle
- Restaurants
- Retail
- Technology
- Transportation
- Travel

Our benchmarking data is also available directly in the [Snowflake Data Exchange](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR).

> For a set of example queries to reference when setting up snowflake, check out our [sample queries][SQ] and [ETL event pipeline setup][ETL] examples.

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
