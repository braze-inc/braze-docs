---
nav_title: How Braze Uses Currents
article_title: How Braze Uses Currents
page_order: 6
page_type: tutorial
description: "This Currents how-to article will walk you through the basic process for setting up proper intakes for event data, as well as moving it into a database and Business Intelligence (BI) tool."
tool: Currents
 
---

# How Braze uses Currents

> Braze uses Currents! That's right, we like our own product enough to use it in conjunction with a few of [our partners]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/).

We filter our data from our email and push campaigns into a business insights tool, Looker, but it takes an interesting route to get there. We use a slightly inverted version of the Extract, Transform, Load (ETL) methodology—we just switch up the order to Extract, Load, Transform (ELT)!

## Step 1: Intake and aggregate event data

After launching campaigns using any of our engagement tools (like campaigns or Canvas), we track event data using our own system as well as some from our email partners. Some of this data is aggregated and shown in the dashboard, but we're interested in diving deeper!

## Step 2: Send event data to a data storage partner

We set up Currents to send Braze event data to Amazon S3 for storage and extraction. Now, we do know that you can use [Athena](https://aws.amazon.com/athena/) to sit on top of S3 and run queries. It's a great short-term solution. But we wanted a long-term solution using a Relational Database and a Business Intelligence/Analytics tool. (We recommend that same for you.)

We think of S3 as our keys to the castle! It opens up the door to so many possibilities for moving, pivoting, and analyzing our data by transferring it where we need it to go. However, we are careful not to transform our data in S3, as we have a very specific structure for it.

## Step 3: Transform event data with a relational database

From S3, we choose a warehouse ([Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) or Snowflake Reader Accounts, in our case). We transform it there, then move it to Looker, where we have blocks set up that will structure and organize our data.

Snowflake isn't the only warehouse option. Other options include [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), and more!

### Snowflake Reader Accounts

Snowflake Reader Accounts offer users access to the same data and functionality as [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), all without requiring a Snowflake account or customer relationship with Snowflake. With Reader Accounts, Braze will create and share your data into an account and provide you credentials to log in and access your data. This will result in all data sharing and usage billing being handled entirely by Braze. 

To learn more, reach out to your customer success manager.

#### Additional resources
For helpful usage monitoring resources, check out Snowflake's [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) and [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) articles.

## Step 4: Use a Business Intelligence (BI) tool to manipulate your data

Finally, we use a BI tool to analyze our data, turn it into charts and other visual tools, and more using [Looker and Looker Blocks](https://www.marketplace.looker.com/) so we don't have to ETL or ELT data every time it moves from Currents.

Feeling inspired to do the same? Check out the following docs to get more information on these and how you can use them to build your database!

- [User Behavior Block](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

