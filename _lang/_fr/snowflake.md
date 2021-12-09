---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
page_order: 1
description: "This article outlines the partnership between Braze and Snowflake, a purpose-built SQL cloud data warehouse for all of your data and all of your users."
page_type: partner
search_tag: Partner
---

# Snowflake secure data sharing

Personalized and relevant marketing campaigns require in-the-moment access to data. That’s why Braze teamed up with Snowflake to launch Data Sharing. This joint offering enables marketers to unlock the potential of their customer engagement and campaign data faster than ever before.

Braze leverages Snowflake’s Data Exchange to build a presence, find new customers, and expand reach through the ever-growing Snowflake customer base.

Learn more about this partnership [here](https://www.braze.com/perspectives/article/snowflake-partner-announcement)!

## What is Snowflake?

[Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) is an analytic data warehouse provided as Software-as-a-Service (SaaS). Snowflake provides a data warehouse that is faster, easier to use, and far more flexible than traditional data warehouse offerings.

Snowflake’s cloud data platform shatters the barriers that prevent organizations of all sizes from unleashing their data’s true value. Snowflake equips brands with a single, integrated platform that offers the only data warehouse built for the cloud; instant, secure, and governed access to their entire network of data.

> Snowflake is a purpose-built SQL cloud data warehouse for all of your data and all of your users. With Snowflake's unique and patented architecture it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

## What is data sharing?

Snowflake's [Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html) functionality allows Braze to give you secure access to data on our Snowflake portal without worrying about workflow friction or slowdown, failure points, and unnecessary costs that come with typical data provider relationships.

#### Reduce time to insights
Say goodbye to ETL processes that take weeks to build out. With Braze and Snowflake’s unique architectures, all customer engagement and campaign data is immediately accessible AND queryable from the instant it arrives in our data lake. No data is copied or moved, so you can deliver customer experiences based on only the most relevant, up-to-date information.

#### Break down data silos
Create a holistic view of your customers across channels and platforms. Data Sharing makes joining your Braze customer engagement data with all of your other Snowflake data easier than ever—creating richer insights across a single, reliable source of truth.

#### See how your engagement stacks up
Optimize your customer engagement strategies with Braze Benchmarks. This interactive tool, powered by Braze and Snowflake, allows you to compare your brand’s engagement data to benchmarks across channel, industry, and device platform.

Read more about how Snowflake's Data Sharing works here: [Introduction to Secure Data Sharing — Snowflake Documentation](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)

## Integration

> If you're interested in this integration, reach out to your Braze Account or Customer Success Manager and ask them to consult Braze Data Strategy Services on Secure Data Sharing with Snowflake. This will get the cogs going inside Braze and we'll have your views set up in no time!

{% alert important %}
In order to use the Braze Data Sharing feature, you must also be a Snowflake customer. This is because the data is shared within the Snowflake platform.
{% endalert %}

With Data Sharing, no actual data is copied or transferred between accounts. All sharing is accomplished through Snowflake’s unique services layer and metadata store. This is an important concept because it means that shared data does not take up any storage in a consumer account and, therefore, does not contribute to the consumer’s monthly data storage charges. The **only** charges to consumers are for the computing resources (i.e. virtual warehouses) used to query the shared data.

Additionally, using Snowflake's built-in roles and permissions capabilities, access to data that is shared from Braze can be controlled and governed using the access controls already in place for your Snowflake account and the data therein. Access can be restricted and monitored the same exact way as your own data.

When a Data Share is requested by a client, Braze will provision the share from the App Group(s) for which the share was purchased. Once the share is provisioned, all data is immediately accessible from within your Snowflake instance in the form of an Incoming Data Share.

![inbound-share]({% image_buster /assets/img/inbound-data-share.png %})

Once the share is visible in your instance (you need to be `ACCOUNTADMIN` role to see it), you'll need to create a database from the share so you can see and query the tables.

In the context of Data Sharing, Braze is a [Data Provider](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) - any Snowflake account that creates shares and makes them available to other Snowflake accounts to consume. You, our client, are a [Data Consumer](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) - any account that chooses to create a database from a share made available by a data provider.

## Usage and visualization

Once the data share is provisioned, you'll need to create a database from the Incoming Data Share, which will then make all the tables shared appear in your Snowflake instance and be queryable just like any other data you're storing in your instance. Keep in mind, however, that the shared data is ready only, and can only be queried, but not modified or deleted in any way.

Similar to Currents, you can use your Secure Snowflake Data Sharing to...

-   Create complex reports,
-   Perform attribution modeling,
-   Secure sharing within your own company,
-   Map raw event or user data to a CRM (like Salesforce)...

And so much more!

\[Download the raw table schemas here.\]\[schemas\]

## Important information and limitations

### Breaking vs non-breaking changes
#### Non-Breaking Changes
Non-breaking changes can happen at any time and generally provide additional functionality.<br> Examples of non-breaking changes:
- Adding a new table or view
- Adding a column to an existing table or view

{% alert important %}
Because new columns are considered non-breaking, Braze strongly recommends explicitly listing the columns of interest in each query instead of using `SELECT *` queries. Alternately, customers might want to create views that explicitly name columns, and then query those views instead of the tables directly.
{% endalert %}

#### Breaking changes
Breaking changes will be preceded by an announcement and a migration period when possible. Examples of breaking changes include:
- Removing a table or view
- Removing a column from an existing table or view
- Changing the type or nullability of an existing column

### Snowflake regions
Braze currently hosts all user-level data in the Snowflake AWS US East-1 and EU-Central (Frankfurt) regions. However, we are able to provide Data Sharing to joint customers who are hosting their Snowflake infrastructure across any AWS or Azure region.

### Historical data
Braze's historical event data in Snowflake only goes back to April of 2019. In the first few months of us storing data there, we made some product changes that may result in some of that data looking slightly different or having some null values (as we weren't passing data into every available field from the start.) It's best to assume that any results that include data prior to August 2019 may look slightly different from expectations.

### PII and GDPR compliance
Nearly every event record we store includes a few fields that represent users' PII (Personally Identifiable Information). Some events may include data such as email address, phone number, device ID, language, gender, and location information. In the event of a user's request to be forgotten being submitted to Braze, we will null out those PII fields for any event belonging to those users. This way we're not removing the historical record of the event, but now the event can never be tied back to a specific individual.

#### PII / NON_PII tables - deprecated
In the past, Braze separated out columns that contained PII into separate tables that ended with _PII. Other columns were stored in tables that ended with _NON_PII. Those tables have since been deprecated, in favor of tables that contain all columns associated with an event. This change obviates the need to perform additional computation to get a complete view of an event. If you were using the old PII / NON_PII tables, please update your integration to use the new, unified tables.

### Speed, Performance, Cost of Queries
Speed, performance, and cost of any query run on top of the data is entirely determined by the size of the warehouse you use to query the data. In some cases, depending on how much data you're accessing for analytics, you may find that you need to use a larger warehouse size for the query to be performant or even to finish before timing out. Snowflake has excellent resources available about how to best determine which size to use: [Overview of Warehouses — Snowflake Documentation](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) and [Warehouse Considerations — Snowflake Documentation](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)

## Braze benchmarks

Braze Benchmarks will allow Braze prospects and customers alike to see how they compare to top players in their industry by comparing their metrics against Braze's industry benchmarks.

We created a [Data Tool for Braze Benchmarks](https://www.braze.com/perspectives/benchmarks) so you can view a selection of the data, outside the Snowflake interface.

The initial industries are Delivery Services, Ecommerce, Education, Entertainment, Finance, Gaming, Health, Lifestyle, Restaurants, Retail, Technology, Transportation, and Travel.

Our benchmarking data will also be available directly in the Snowflake Data Exchange.

> For a set of example queries to reference when setting up snowflake, check out our [Sample Queries][SQ] and [ETL Event Pipeline Setup][ETL] examples.
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
