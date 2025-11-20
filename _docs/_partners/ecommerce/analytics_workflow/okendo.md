---
nav_title: Okendo
article_title: "Okendo"
description: "Learn how to integrate Okendo with Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) is a unified customer marketing platform that provides tools to cultivate advocacy, scale word-of-mouth, and maximize lifetime value to mobilize your customers for faster, more efficient growth.

*This integration is maintained by Okendo.*

## About the integration

The Braze integration with Okendo works across multiple products in Okendo's platform, including Reviews, Loyalty, Referrals, Surveys, and Quizzes. Okendo sends custom events and user attributes to Braze, which can be used to personalize and trigger messages.  

## Prerequisites

| Requirement            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Okendo account         | An Okendo account is required to take advantage of this partnership.        |
| Braze REST API key     | A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint    | [Your REST endpoint URL]({{site.baseurl}}/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Set up Braze Connector in Okendo

1. In Okendo, go to **Settings** > **Integrations** > **Email & SMS** > **Braze**
2. Add the API endpoint and API key to the **Integration** settings.

### Step 2: Configure your identifier

The `external_id` field is used to identify the user associated with each event. Toggle on **Use Shopify Customer ID for Braze user identification** to associate the field with Shopify Customer IDs. Otherwise, toggle it off to associate it with each user's email address.

## Syncing Okendo events and attributes to Braze

### Custom events

{% alert note %} 
For sample event data, refer to [Okendo's documentation](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c). 
{% endalert %}

#### Review events

- Okendo Review Created
- Okendo Review Request

#### Referral events

- Sent Okendo Referral
- Opted In to Okendo Referrals
- Okendo Referral Invitation
- Received Okendo Referral Coupon
- Redeemed Okendo Referral Coupon
- Okendo Referral Rejected

#### Loyalty events

- Enrolled in Okendo Loyalty
- Okendo Loyalty Points Awarded
- Okendo Loyalty Points Redeemed
- Okendo Loyalty Tier Changed
- Okendo Loyalty Points Adjusted

#### Survey event

- Submitted Okendo Survey

#### Quiz event

- Submitted Okendo Quiz

### Custom attributes

Okendo sends user profile data as custom attributes in Braze, which can be used to create audience segments. Examples include:

- Profile questions asked in surveys and during a review submission, such as age, birthday, skin type, and hair color
- Review metrics such as _Average Review Rating_ and _Average Review Sentiment_
- Loyalty metrics such as _Points Balance_ and _VIP Tier_
- Referrals metrics such as the _Number of Successful Referrals_ and _Total Referral Revenue_  
- NPS score collected from a survey

## Using Braze with Okendo products

Depending on the Okendo product, you must complete additional steps to use Braze and Okendo together. Refer to the following articles for more details:

- [Integrating Reviews with Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integrating Loyalty with Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integrating Referrals with Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integrating Surveys with Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integrating Quizzes with Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
For assistance with configuring the integration, contact the Okendo support team.
{% endalert %}
