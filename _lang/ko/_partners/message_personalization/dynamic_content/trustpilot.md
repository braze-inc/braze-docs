---
nav_title: Trustpilot
article_title: Trustpilot
description: "This page covers how to integrate Trustpilot with Braze, send review invitations, and personalize messages with product review insights."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/) is an online review platform that enables customers to share feedback and allows you to manage and respond to reviews.

This page provides a step-by-step guide for:

* Creating review invitations using Trustpilot's Create Invitation API  
* Personalizing messages with product reviews through Trustpilot's Product Reviews API

## Prerequisites

시작하기 전에 다음이 필요합니다:

| 전제 조건 | 설명 |
| --- | --- |
| A Trustpilot account | You need a Trustpilot account with access to Trustpilot's API. |
| A Trustpilot authentication key | You will need to set up an API key and request an access token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 통합

### 1단계: Get your Trustpilot API credentials

1. [Log into Trustpilot](https://app.contentful.com/login) with your credentials.  
2. Create or retrieve the API key and secret in the Trustpilot dashboard by going to **Integrations** > **Developers** > **APIs**. 아직 API 키가 없는 경우 새로 생성하세요:  
   1. Go to **Application Name** > **Create Application**  
   2. Copy your API key and secret, which will be used to authenticate your Connected Content requests.

## Sending Trustpilot review invitations

### 1단계: Set up a Braze webhook campaign 

Set up an action-based Braze webhook campaign to trigger the Trustpilot APIs to send email review invitations to users. For example, you could send a review invitation after a user places an order with the following webhook details:
   * [웹훅 URL](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * Method: POST  
   * Add the relevant customer information as key-value pairs

### 2단계: 액세스 토큰 검색

1. Use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) to make a request to [Trustpilot’s Authentication endpoint](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) to retrieve the Access Token.
2. Use the **client_credentials** grant type, and enter your API key and secret into a Connected Content tag to retrieve a token. The Connected Content request can be entered into the request header. The Connected Content may look like this:
  
{% raw %}

```liquid
{% connected_content 
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3\. Add the access token to the request header of your webhook campaign.

{% alert tip %}
Refer to [Trustpilot’s documentation](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites) for more detailed instructions.
{% endalert %}

## Personalizing messages with product review insights

In your Braze campaign, make a Connected Content call to request data from Trustpilot’s [Get product reviews summary endpoint](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}). This method retrieves product reviews for specific SKUs from the business unit. The following example specifies the specific product SKU and filters for five-star reviews.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Connected Content in email using Liquid to pull in information.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

The Connected Content request will return the product reviews.

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2\. Use Liquid syntax to pull the relevant content into your message. For example, to pull in the product review's content, use the Liquid tag {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![Personalized email with a review of a toy truck that the user left in their cart.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}