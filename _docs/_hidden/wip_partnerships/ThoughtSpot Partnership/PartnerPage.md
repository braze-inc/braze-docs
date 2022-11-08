---
nav_title: ThoughtSpot
article_title: ThoughtSpot & Braze Partnership
page_order: 1

description: "Together, ThoughtSpot and Braze make it easy to get started on user behaviour analytics.
alias: /partners/your_partner_name/

page_type: partner
search_tag: Partner
hidden: true
---

# [Partner Name]

>ThoughtSpot is the Modern Analytics Cloud, a next-generation analytics platform that delivers Live Analytics to your modern data stack - empowering your colleagues, partners and customers to turn data into actionable insights.

Leveraging TML Blocks, Braze users can acclerate their user behaviour analytics with prebuilt templates of worksheets and models. Enable all users to limitlessly search across their Braze interaction data and uncover actionable insights. 


## Prerequisites

To get started with using ThoughtSpot on Braze, your data needs to be sent to a cloud data warehouse before it is able to be live queried by ThoughtSpot.

<div class='alert alert-important' role='alert'><div class='alert-msg'> <b>important: </b><br />
<p>The following requirements are typical requirements you might need from Braze. We recommend using the attributed titling and phrasing listed in the following chart. Be sure to adjust the descriptions and tailor them to your partnership integration.</p>
</div></div>


| Requirement | Description |
| ----------- | ----------- |
| ThoughtSpot Account | A ThoughtSpot Account is required to take advantage of this partnership. |
| Cloud Data Warehouse| Braze data is stored in Cloud Data Warehouse using Braze Currents. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST Endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |

## TML Blocks

Braze users can easily access and search on all their digital interaction data. Our templates empower users to set up their analysis quickly with pre-built visualizations and worksheets. Analyze user acquisition and user behavior of your website with search, drill-downs, and spotIQ.


## Integration

### Connect ThoughtSpot 
Log into your ThoughtSpot instance and create an Embrace connection to each of the tables that have been brought in from Blaze using Blaze Currents 

#### Import TML
Import the zipped file for the worksheets and verify that it has all been imported without any errors. Import the zipped for the liveboards and verify that it has all been imported without any errors.

Once imported you can start searching and customizing the liveboards. 
