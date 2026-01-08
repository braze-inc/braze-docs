---
nav_title: Recurly
article_title: Recurly
description: "Recurly is the leading subscription management and billing platform for direct-to-consumer brands seeking to grow their subscriptions and recurring revenue."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) is a subscription management and billing platform. The Recurly integrated platform simplifies the automation of the subscription lifecycle at scale by enabling teams to manage and optimize the subscriber experience&#8212;from testing new plans, offers, and promotions to managing payment methods, integrations, and insights.

_This integration is maintained by Recurly._

## About the integration

The integration between Recurly and Braze simplifies the process of sharing subscription data with Braze, enabling targeted communication with customers.

- Leverage Recurly subscription lifecycle events (for example, subscription renewals, pauses, or cancels) in Braze to trigger personalized campaigns and communications.
- Leverage Recurly subscription data (for example, subscription plans, add-ons, or status) to create and manage Braze users, segments, and Canvases to execute cohort-specific campaigns and communications.
- Send Recurly data directly to Braze, enabling additional messaging use cases and reducing developmental overhead costs.

Additional details around using Recurly with Braze can be found in the [Recurly Docs](https://docs.recurly.com/docs/braze-integration).

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Recurly account | An Elite [Recurly](https://recurly.com/) subscription plan with the Braze feature flag enabled is required to take advantage of this partnership. The activation of credit invoices in your Recurly platform is also required.|
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. Because Recurly only uses the `users.track` endpoint, we recommend provisioning a Recurly specific key with only this permission. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |

## Integration

Before you begin, make sure you have active accounts on both Braze and Recurly.

### Connect Recurly to Braze

1. In Recurly, go to **Integrations** > **Braze**. When first navigating to the Braze integration configuration page in Recurly, the interface will prompt you to connect the two systems.

2. Provide the following credentials:

- **Instance URL:** The Braze REST endpoint of the instance you are provisioned to.
- **API Key (Identifier):** The Braze REST API key that Recurly should use when sending requests to Braze.

Remember to copy the URL of your Braze instance. For example, your URL might look like: 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3. After you enter your credentials, click **Connect**.

## Using this integration

### Supported identifiers

Recurly uses an account's `account_code` as the `external_id` in Braze. Because of this, the `account_code` of your Recurly accounts should correspond with your Braze user's `external_id`.

### Custom events

For effective customer engagement, you must [configure custom events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) in Braze to receive events triggered by Recurly. Ensure to include each event from Recurly for thorough data integration. These events can also be tracked within [Braze analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Once configured, these custom events can be used to segment users or personalize messaging. 

| Braze Custom Event| Recurly Event |
| ----------- | ----------- |
| Recurly New Subscription              | Triggered when a subscription is created                            |
| Recurly Renewed Subscription          | Triggered when a subscription is renewed                                |
| Recurly Updated Subscription          | Triggered when a subscription's attributes change (plan change, price change, or quantity change) |
| Recurly Canceled Subscription         | Triggered when a subscription is canceled                           |
| Recurly Reactivated Subscription      | Triggered when a canceled subscription is reactivated               |
| Recurly Paused Subscription           | Triggered when a subscription is set to be paused                   |
| Recurly Resumed Subscription          | Triggered when a subscription unpauses                              |
| Recurly Subscription Expired          | Triggered when a subscription expires                               |
| Recurly Invoice Created               | Triggered when an invoice is created                                |
| Recurly Successful Payment            | Triggered when an invoice is successfully collected                 |
| Recurly Refund Issued                 | Triggered when a refund is issued                                   |
| Recurly Failed Recurring Payment      | Triggered when an invoice fails for a subscription renewal          |

### Batching and rate limiting

Because Recurly uses the Braze `/users/track` endpoint, the integration is subject to standard Braze rate limits of 50,000 requests per minute.

Recurly batches certain subscription lifecycle events as single API calls to Braze to reduce the number of calls made.

- Creation of multiple subscriptions at the same time are batched and sent to Braze as a single request.
- When multiple subscriptions are renewed at the same time for an account, each of those renewals is batched into a single request.
- Same model subscription lifecycle events are sent as a single request. An example being a newly created invoice with a payment would send a single API request with both the `Recurly Invoice Created` and `Recurly Successful Payment` custom events.

Batches are sent to Braze in groups of up to 75 events at a time. For example, if 100 subscriptions were created at once, Recurly would make two API requests to Braze. See [batching User Track requests]({{site.baseurl}}/api/api_limits/#batch-user-track) for details.


