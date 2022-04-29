---
nav_title: Peak Partner Page article_title: Peak Partner Page page_order: 1

description: "Integrating Decision Intelligence from Peak’s platform to Braze platform"
alias: /partners/Peak/

page_type: partner search_tag: Partner, Peak, Braze, Integration, Connect, Email, Reccomender, Decision Intelligence
hidden: true

---

# Peak

> Peak, a Decision Intelligence platform, is an end to outcome system, where Decision Intelligence is the commercial application of AI to enhance business decision-making, to grow revenues and profits

The commercial partnership between Peak and Braze, enables Peak customers who are additionally engaged with Braze to
supercharge their Braze Solutions with AI driven outputs, such as enriching understanding of customers.

## Prerequisites

As a starting point a Peak tenant is required to host the integration between Peak and Braze. This is traditionally
created during the onboarding of Peak Customers. Additionally a Decisions Intelligence solution is initially required as
this generates the AI driven outputs that will subsequently be integrated into Braze.

| Requirement | Description |
| ----------- | ----------- |
| Peak Tenant | An instance of the Peak platform, known as a Tenant, is required to host and orchestrate the integration |
| Decision Intelligence Solution | Integration between Peak and Braze is based on AI driven outputs and thus requires a Peak or Customer deployed solution, within the above Tenant |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the ** Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |

## Use cases

Peak offers a range of different use cases for integrating between Peak Decision Intelligence solutions and Braze. We're
also looking to add more use cases as they arise, so if not currently listed can be added. Currenetly we have the
following use cases:

- Customer Churn probability
- Predictive Customer attributes

## Integration

The Peak solution Customer Intelligence utilises a model to predict a range of forward looking attributes, based on
customers behaviours and interactions. These attributes are stored within Peak and can be used to generate predictive
segmentation, including a customer’s probability of churning. The updating of these predictive attributes will be based
on a configurable cadence and are often daily or weekly. The following integration enables the sharing and updating of
these attributes with Braze Customers.

#### Step One - Model Run

The integration is triggered off the back of the AI model run and recalculation of the predictive customer attributes.
These AI outputs are stored within Peak, including when the attribute has been updated with a new status or value.

#### Step Two - Extraction of Customers

Based on when attributes have been updated a selection is carried out to collect all customer with updated predictive
attributes since the last sync between Peak and Braze

#### Step Three - Update Braze

With the updated Customers and associated attributes Peak will POST these to Braze using the [/user/track][1] endpoint,
utilising the ["Bulk"](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/#making-bulk-updates) header.

#### Step Four - Confirm and Log

On receipt of successful status code from the API, Peak will make a record of the successful sync between Peak and
Braze.


[1]: https://www.braze.com/docs/api/endpoints/user_data/post_user_track/
