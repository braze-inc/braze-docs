---
nav_title: Recurly
article_title: Recurly
page_order: 1

description: "Recurly is the leading subscription management and billing platform for direct-to-consumer brands seeking to grow their subscriptions and recurring revenue."
alias: /partners/recurly/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# Recurly

> [Recurly](https://recurly.com/) is a subscription management and billing platform trusted by leading direct-to-consumer brands to grow their recurring revenue.
>
> Recurly’s integrated platform simplifies the automation of the subscription lifecycle at scale by enabling teams to manage and optimize the subscriber experience with ease— from testing new plans, offers and promotions to payment methods, integrations and insights.
>
> Category-defining companies including Sling, Twitch, BarkBox, FabFitFun, and Paramount+ have chosen Recurly to manage billions of dollars in recurring revenues, future-proof their recurring billing and revenue management, and recover billions of dollars in lost revenue due to churn.


The integration between Recurly and Braze allows businesses to seamlessly facilitate meaningful, context-aware communications with subscribers to increase engagement, retention and lifetime value.

- Leverage Recurly subscription lifecycle events (e.g. subscription renewals, pauses, cancels) in Braze to trigger personalized campaigns and communications.
- Leverage Recurly subscription data (e.g. subscription plans, add-ons, status) to create and manage Braze users, segments, and canvases to execute cohort-specific campaigns and communications.
- Enables merchants to send Recurly data directly to Braze, enabling additional messaging use cases, while reducing developmental overhead costs.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Recurly account | A [Recurly](https://recurly.com/) account with the Braze feature flag enabled is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. Since Recurly only uses the `users.track` endpoint, we recommend provisioning a Recurly specific key with only this permission. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance. |

## Integration

### Connect Recurly to Braze

In Recurly, go to **Integrations** > **Braze**. When first navigating to the Braze integration configuration page in Recurly, the interface will prompt you to connect the two systems.

Provide the following credentials:

- **Instance URL:** The Braze REST endpoint of the instance you are provisioned to.
- **API Key (Identifier):** The Braze REST API key that Recurly should use when sending requests to Braze.

After you enter your credentials, click **Connect**.

## Using this integration

### Supported Identifiers

Recurly uses an account's `account_code` as the `external_id` in Braze. Because of this, the `account_code` of your Recurly accounts should correspond with your Braze user's `external_id`.

### Supported Events

When you integrate Braze and Recurly, the following custom events will be available in Braze.

| Braze Custom Event| Recurly Event |
| ----------- | ----------- |
| Recurly New Subscription              | A subscription is created                            |
| Recurly Renewed Subscription          | A subscription renews                                |
| Recurly Updated Subscription          | A subscriptions attributes change (Plan change, price change, or quantity change) |
| Recurly Canceled Subscription         | A subscription is canceled                           |
| Recurly Reactivated Subscription      | A canceled subscription is reactivated               |
| Recurly Paused Subscription           | A subscription is set to be paused                   |
| Recurly Resumed Subscription          | A subscription unpauses                              |
| Recurly Subscription Expired          | A subscription expires                               |
| Recurly Invoice Created               | An invoice is created                                |
| Recurly Successful Payment            | An invoice is successfully collected                 |
| Recurly Refund Issued                 | A refund is issued                                   |
| Recurly Failed Recurring Payment      | An invoice fails for a subscription renewal          |

### Batching and Rate Limiting

Because Recurly uses your API key configured with Braze, the integration is subject to standard Braze rate limits of 20000 requests per minute.

Recurly batches certain subscription lifecycle events as single API calls to Braze to reduce the number of calls made.

- Creation of multiple subscriptions at the same time are batched and sent to Braze as a single request.
- When multiple subscriptions are renewed at the same time for an account, each of those renewals is batched into a single request.
- Same model subscription lifecycle events are sent as a single request. An example being a newly created invoice with a payment would send a single API request with both the 'Recurly Invoice Created' and 'Recurly Successful Payment' custom events.

Batches are sent to braze in groups of up to 75 events at a time. If 100 subscriptions were created at once, we would make 2 API requests to handle this.

Additional details around using Recurly with Braze can be found [HERE](https://docs.recurly.com/docs/braze-integration).

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
