---
nav_title: Recurly
article_title: Recurly
description: "Recurly is the leading subscription management and billing platform for direct-to-consumer brands seeking to grow their subscriptions and recurring revenue."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) is a subscription management and billing platform. The Recurly integrated platform simplifies the automation of the subscription lifecycle at scale by enabling teams to manage and optimize the subscriber experience—from testing new plans, offers, and promotions to managing payment methods, integrations, and insights.

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
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. Recurly는 `users.track` 엔드포인트만 사용하므로 이 권한으로만 Recurly 특정 키를 프로비저닝하는 것이 좋습니다. |
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
3\. After you enter your credentials, click **Connect**.

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

특정 구독 수명 주기 이벤트를 반복적으로 일괄 처리하여 Braze에 대한 단일 API 호출로 처리하여 요청 횟수를 줄입니다.

- 단일 요청으로 동시에 생성된 여러 구독을 반복적으로 일괄 처리하여 전송합니다.
- 계정에 대한 여러 개의 동시 갱신을 하나의 요청으로 반복적으로 일괄 처리합니다.
- 동일한 모델 구독 수명 주기 이벤트를 한 번의 요청으로 반복적으로 전송합니다. 예를 들어, 결제와 함께 새로 생성된 인보이스는 `Recurly Invoice Created` 및 `Recurly Successful Payment` 커스텀 이벤트가 모두 포함된 하나의 API 요청을 생성합니다.

Batches are sent to Braze in groups of up to 75 events at a time. For example, if 100 subscriptions were created at once, Recurly would make two API requests to Braze. See [batching User Track requests]({{site.baseurl}}/api/api_limits/#batch-user-track) for details.


