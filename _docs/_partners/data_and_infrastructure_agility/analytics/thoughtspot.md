---
nav_title: ThoughtSpot
article_title: ThoughtSpot
description: "The ThoughtSpot and Braze integration enables users to limitlessly search across their Braze interaction data and uncover actionable insights."
alias: /partners/thoughtspot/
page_type: partner
search_tag: Partner

---

# ThoughtSpot

> ThoughtSpot is the modern analytics cloud, a next-generation analytics platform that delivers live analytics to your modern data stack - empowering your colleagues, partners, and customers to turn data into actionable insights.

The Braze and ThoughtSpot integration leverages ThoughtSpot TML Blocks that allows Braze users to accelerate their user behavior analytics with prebuilt templates of worksheets and models. This integration enables users to limitlessly search across their Braze interaction data and uncover actionable insights. 

## Prerequisites

To start using ThoughtSpot on Braze, your data needs to be sent to a cloud data warehouse before ThoughtSpot can live query it.

| Requirement | Description |
| ----------- | ----------- |
| ThoughtSpot account | A ThoughtSpot account is required to take advantage of this partnership. |
| Cloud data warehouse| Braze data is stored in Cloud Data Warehouse using Braze Currents. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST Endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

## TML Blocks

Braze users can easily access and search all their digital interaction data. Our templates empower users to set up their analysis quickly with pre-built visualizations and worksheets. Analyze your website's acquisition and user behavior with search, drill-downs, and spotIQ.

## Integration

### Step 1: Connect ThoughtSpot 

Log into your ThoughtSpot instance and create an Embrace connection to each table brought in from Braze using Braze Currents.

#### Step 2: Import TML

Import the zipped file for the worksheets and liveboards in Thoughtspot and verify that they have been imported without errors. 

Once imported, you can start searching and customizing the liveboards. 

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints