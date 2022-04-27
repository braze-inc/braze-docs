---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
page_order: 1
description: "This article outlines the partnership between Braze and Snowflake, a purpose-built SQL cloud data warehouse for all of your data and users."
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) is a purpose-built SQL cloud data warehouse provided as Software-as-a-Service (SaaS). Snowflake provides a data warehouse that is faster, easier to use, and far more flexible than traditional data warehouse offerings. With Snowflake's unique and patented architecture, it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Personalized and relevant marketing campaigns require in-the-moment access to data. That’s why Braze teamed up with Snowflake to launch Data Sharing. This joint offering enables marketers to unlock the potential of their customer engagement and campaign data faster than ever before.

The [Braze and Snowflake integration](https://www.braze.com/perspectives/article/snowflake-partner-announcement) leverages Snowflake's data exchange to build a presence, find new customers, and expand reach through the ever-growing Snowflake customer base.

## What is Data Sharing?

Snowflake's [Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) functionality allows Braze to give you secure access to data on our Snowflake portal without worrying about workflow friction or slowdown, failure points, and unnecessary costs that come with typical data provider relationships.

- **Reduce time to insights**<br>Say goodbye to ETL processes that take weeks to build out. Braze and Snowflake’s unique architectures make all customer engagement and campaign data immediately accessible and queryable from the instant it arrives in the data lake. No data is copied or moved, so you can deliver customer experiences based on only the most relevant, up-to-date information.
- **Break down data silos**<br>Create a holistic view of your customers across channels and platforms. Data Sharing makes joining your Braze customer engagement data with all of your other Snowflake data easier than ever—creating richer insights across a single, reliable source of truth.
- **See how your engagement stacks up**<br>Optimize your customer engagement strategies with Braze Benchmarks. This interactive tool, powered by Braze and Snowflake, allows you to compare your brand’s engagement data to benchmarks across channels, industry, and device platforms.

Check out [Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work). to read more about how Snowflake's Data Sharing works.

## Prerequisites

If you are interested in this integration, reach out to your Braze Account or Customer Success Manager and ask them to consult Braze data strategy services on Secure Data Sharing with Snowflake. This will get the cogs going inside Braze, and we'll have your views set up in no time!

| Requirement | Description |
| ----------- | ----------- |
| Snowflake account | A Snowflake account with admin-level permissions is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

With Data Sharing, no actual data is copied or transferred between accounts. All sharing is accomplished through Snowflake’s unique services layer and metadata store. This is an important concept because shared data does not take up any storage in a consumer account and, therefore, does not contribute to the consumer’s monthly data storage charges. The **only** charges to consumers are for the computing resources (i.e., virtual warehouses) used to query the shared data.

Additionally, using Snowflake's built-in roles and permissions capabilities, access to data shared from Braze can be controlled and governed using the access controls already in place for your Snowflake account and the data therein. Access can be restricted and monitored the same way as your own data.

When a client requests a data share, Braze will provision the share from the app group(s) that the share was purchased. Once the share is provisioned, all data is immediately accessible from within your Snowflake instance in the form of an incoming data share. 

![Inbound data share]({% image_buster /assets/img/inbound-data-share.png %})

Once the share is visible in your instance (you need to be `ACCOUNTADMIN` role to see it), you'll need to create a database from the share so you can see and query the tables.

In the context of Data Sharing, Braze is a [data provider](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)-any Snowflake account that creates shares and makes them available to other Snowflake accounts to consume. You, are a [data consumer](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)-any account that chooses to create a database from a share made available by a data provider.

## Usage and visualization

Once the data share is provisioned, you will need to create a database from the incoming data share, making all the tables shared appear in your Snowflake instance and be queryable just like any other data you're storing in your instance. However, keep in mind that the shared data is read-only and can only be queried but not modified or deleted in any way.

Similar to Currents, you can use your Snowflake Secure Data Sharing to:
- Create complex reports
- Perform attribution modeling
- Secure sharing within your own company
- Map raw event or user data to a CRM (like Salesforce)
- And more

[Download the raw table schemas here.][schemas]

## Important information and limitations

### Breaking vs. non-breaking changes

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
Braze currently hosts all user-level data in the Snowflake AWS US East-1 and EU-Central (Frankfurt) regions. For users outside of those regions, Braze can provide Data Sharing to joint customers who are hosting their Snowflake infrastructure across any AWS or Azure region.

### Historical data
Braze's historical event data in Snowflake only goes back to April 2019. In the first few months of Braze storing data there, product changes were made that may have resulted in some of that data looking slightly different or having some null values (as we weren't passing data into every available field from the start). It's best to assume that any results that include data before August 2019 may look slightly different from expectations.

### PII and GDPR compliance
Nearly every event record Braze stores includes a few fields representing users' personally identifiable information (PII). Some events may include email address, phone number, device ID, language, gender, and location information. If a user's request to be forgotten is submitted to Braze, we will null out those PII fields for any event belonging to those users. This way, we're not removing the historical record of the event, but now the event can never be tied back to a specific individual.

### Speed, performance, cost of queries
The speed, performance, and cost of any query run on top of the data are determined by the warehouse size you use to query the data. In some cases, depending on how much data you're accessing for analytics, you may find that you need to use a larger warehouse size for the query to be successful. Snowflake has excellent resources available about how to best determine which size to use including [Overview of warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) and [Warehouse considerations](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

### PII and NON_PII tables - deprecated
In the past, Braze separated columns that contained PII into separate tables that ended with `_PII`. Other columns were stored in tables that ended with `_NON_PII`. Those tables have since been deprecated in favor of tables that contain all columns associated with an event. This change obviates the need to perform additional computation to get a complete view of an event. If you used the old PII or NON_PII tables, update your integration to use the new, unified tables.

## Braze Benchmarks

Benchmarks, [a data tool built by Braze](https://www.braze.com/perspectives/benchmarks), allows Braze prospects and customers to see how they compare to top players in their industry by comparing their metrics against Braze's industry benchmarks.

The initial industries include: 
- Delivery services
- eCommerce
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

Our benchmarking data will also be available directly in the Snowflake Data Exchange.

> For a set of example queries to reference when setting up snowflake, check out our [sample queries][SQ] and [ETL event pipeline setup][ETL] examples.

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}