---
nav_title: How Braze Uses Currents
article_title: How Braze Uses Currents
page_order: 6
page_type: tutorial
description: "This Currents how-to article will walk you through the basic process for setting up proper intakes for event data, as well as moving it into a database and BI tool."
tool: Currents

---

# How braze uses currents

> Braze uses Currents! That’s right, we like our own product enough to use it in conjunction with a few of [our partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

We filter our data from our email and push campaigns into a business insights tool, Looker, but it takes an interesting route to get there. We use a slightly inverted version of the ETL (Extract, Transform, Load) methodology - we just switched up the order to ELT (Extract, Load, Transform)!

## Step 1: intake and aggregate event data

After launching campaigns using any of our Engagement Tools (like campaigns or Canvas), we track event data using our own system as well as some from our email partners. Some of this data is aggregated and shown in the dashboard, but we were interested in diving deeper!

## Step 2: send event data to a data storage partner

We set up Currents to send Braze event data to Amazon S3 for storage and extraction. Now, we know that you can use [Athena][2] to sit on top of S3 and run queries. It's a great short-term solution. But we wanted (and recommend to you) a long-term solution using a Relational Database and a Business Intelligence/Analytics tool.

We think of S3 as our keys to the castle! It opens up the door to so many possibilities for moving, pivoting, and analyzing our data by transferring it where we need it to go. However, we are careful not to transform our data in S3, as we have a very specific structure for it.

## Step 3: transform event data with a relational database

From S3, we choose a warehouse ([Snowflake](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE), in our case). We transform it there, then move it to Looker, where we have blocks set up that will structure and organize our data.

Snowflake isn't your only warehouse option. You can also choose [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), and more!

## Step 4: use a bi tool to manipulate your data

Finally, we use a BI tool to analyze our data, turn it into charts and other visual tools, and more using [Looker and Looker Blocks](https://looker.com/platform/blocks/directory?utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct#braze) so we don't have to ETL/ELT data every time it moves from Currents.

Check out the docs below to get more information on these and how you can use them to build your database!

- [User Behavior Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Message Engagement Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)




[2]: https://aws.amazon.com/athena/
