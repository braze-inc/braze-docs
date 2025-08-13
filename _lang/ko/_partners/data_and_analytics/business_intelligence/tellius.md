---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "This reference article outlines the partnership between Braze and Tellius, a decision intelligence and augmented analytics platform, allowing you to leverage data, without relying on BI engineers, to build dashboards and generate insights to make better marketing decisions."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), a decision intelligence and augmented analytics platform, enables you to answer questions of your data using natural language search and go deeper to understand 'why' with AI-driven guided insights.

The Braze and Tellius integration empowers users to leverage data, without relying on BI engineers, to build dashboards and generate insights to make better marketing decisions. This integration requires Braze data be stored in Snowflake, where Tellius can connect directly and push down queries with live-mode integration.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Tellius account | A Tellius account is required to take advantage of this partnership. You can start your Tellius journey with a [free trial](https://www.tellius.com/free-trial/)|
| Snowflake Data Sharing program | For current Snowflake customers, contact your Braze representative about the Snowflake Data Sharing program to pipe your Braze data into your Snowflake instance.|
| Snowflake Reader account | For non-Snowflake customers, contact your Braze representative about a Snowflake Reader account that can be provisioned for you to access your Braze data.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Obtain access to Braze through Snowflake

Braze stores granular customer data in Snowflake. You can leverage your Braze data to generate insights through the Braze Snowflake Data Sharing program or by obtaining a Snowflake reader account. 

Follow the [Snowflake integration]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) to get set up. 

### Step 2: Connect Tellius to Braze data in Snowflake

Connect Tellius to Braze data in Snowflake through one of the following methods:

- Direct access: To load data into Tellius, following the steps to [Load datasets](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- OAuth access: For OAuth access to Snowflake, follow the steps for [OAuth authentication](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Step 3: Create Business View in Tellius from loaded data

To start using natural-language search and automated insights, create a [Business View](https://help.tellius.com/article/hy9yvh5tom-create-business-view) and select datasets from your Snowflake connection.

### Step 4: Get the most value out of your data using Tellius

In Tellius, there is a guided interface to walk you through the platform's features. For additional questions and walkthroughs, refer to their complete [knowledge base](https://help.tellius.com/).