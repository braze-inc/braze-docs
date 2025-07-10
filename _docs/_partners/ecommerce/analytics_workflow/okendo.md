---
nav_title: Okendo
article_title: "Okendo"
description: "Learn how to integrate Okendo with Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> Turn customers into Superfans with [Okendo](https://okendo.io/). Okendo’s unified platform for reviews, referrals, loyalty, quizzes and surveys makes it easy to cultivate advocacy, scale word-of-mouth and maximize lifetime value. 17,000+ Shopify brands use Okendo to mobilize their customers for faster and more efficient growth, including SKIMS, True Classic and Oh Polly.

*This integration is maintained by Okendo.*

## About the integration

The Braze integration with Okendo works across multiple products in Okendo's platform, including Reviews, Loyalty, Referrals, Surveys and Quizzes. Okendo sends custom events and user attributes to Braze, which can be used to personalize and trigger messages.  

## Prerequisites

| Requirement            | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Okendo account         | An Okendo account is required to take advantage of this partnership.        |
| Braze REST API key     | A Braze REST API key with `users.track` permissions. This can be created in the Braze dashboard from Settings > API Keys. |
| Braze REST endpoint    | [Your REST endpoint URL](https://www.braze.com/docs/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |

## Integration

### Step 1: Braze Connector setup in Okendo

1. Open Okendo and navigate to Settings > Integrations > Email & SMS > Braze  
2. Add the API Endpoint and API Key to the Integration settings.

### Step 2: Configure your identifier

The `external_id` field is used to identify the user associated with each event. Toggle on **Use Shopify Customer ID for Braze user identification** to associate the field with Shopify Customer IDs. Otherwise, toggle it off to associate it with each user's email address.

## Syncing Okendo Events and Attributes to Braze

### Custom Events:

#### Review Events:
- Okendo Review Created  
- Okendo Review Request  

#### Referral Events

- Sent Okendo Referral  
- Opted In to Okendo Referrals  
- Okendo Referral Invitation  
- Received Okendo Referral Coupon  
- Redeemed Okendo Referral Coupon  
- Okendo Referral Rejected  

#### Loyalty Events

- Enrolled in Okendo Loyalty  
- Okendo Loyalty Points Awarded  
- Okendo Loyalty Points Redeemed  
- Okendo Loyalty Tier Changed  
- Okendo Loyalty Points Adjusted  

#### Survey Event
- Submitted Okendo Survey  

#### Quiz Event
- Submitted Okendo Quiz  


{% alert note %} Sample event data can be found in [Okendo’s documentation](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c) {% endalert %}


### Custom attributes

Okendo sends user profile data as custom attributes in Braze which can be used to create audience segments. Examples include:

- Profile questions asked in surveys and during a review submission such as: Age, Birthday, Skin Type and Hair Color  
- Review metrics such as Average Review Rating and Average Review Sentiment  
- Loyalty metrics such as Points Balance and VIP Tier  
- Referrals metrics such as No. of Successful Referrals and Total Referral Revenue  
- NPS Score collected from a survey  

## Using Braze with Okendo products

Depending on the Okendo product, you must complete additional steps to use Braze and Okendo together.

#### Reviews

[Integrating Reviews with Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)

#### Loyalty

[Integrating Loyalty with Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)

#### Referrals

[Integrating Referrals with Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)

#### Surveys

[Integrating Surveys with Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)

#### Quizzes

[Integrating Quizzes with Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

## Support

For assistance with configuring the integration, contact the Okendo support team.
