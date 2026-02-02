---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "This reference article outlines the partnership between Braze and Yotpo, a leading eCommerce marketing platform that helps thousands of forward-thinking brands accelerate direct-to-consumer growth."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), the leading eCommerce marketing platform, helps thousands of forward-thinking brands accelerate direct-to-consumer growth. Yotpo's single-platform approach integrates data-driven solutions for reviews, loyalty, SMS marketing, and more, empowering brands to create smarter, higher-converting customer experiences.

_This integration is maintained by Yotpo._

## About the integration

With the Braze and Yotpo integration, you can dynamically pull and display star ratings, top reviews, and visual user-generated content (UGC) on products within emails and other communication channels within Braze. You can also include customer-level loyalty data in emails and other communication methods to create a more personalized interaction, boosting sales and loyalty.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Yotpo account | A Yotpo account is required to take advantage of this partnership. |
| Yotpo reviews API key | This API will be implemented within the Connected Content code snippet.<br><br>For more information, refer to [finding your Yotpo app key and secret key](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Yotpo loyalty API key | 이 API 키와 글로벌 고유 식별자(GUID)는 연결된 콘텐츠 코드 스니펫 내에서 구현됩니다.<br><br>자세한 내용은 [로열티 찾기 & 추천 API 키 및 GUID를](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid) 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Before continuing, confirm that the Yotpo product ID is the same as the `product_id` that will be pulled dynamically from Braze. This is mandatory for the integration to work. 

To find your Yotpo product ID, perform the following steps:

1. Go to your store website.
2. Open the product page.
3. Right-click and select **Inspect**.
4. Press <kbd>Control</kbd> + <kbd>F</kbd> and search for `yotpo-main` in the code. `data-product ID` 변수와 해당 값은 Yotpo div에 표시됩니다.

![yotpo-main을 검사하고 검색하여 데이터 제품 ID 변수 찾기]({% image_buster /assets/img/yotpo/image1.png %})

## 통합

To integrate Yotpo and Braze, perform the following steps:

1. Go to your Braze dashboard.
2. On the **Campaigns** page, click **Create Campaign** and select **Email**.
3. Select your preferred template.
4. Click **Edit email body** and add the respective [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) snippet for your use case:
    - [Display a product's star rating and review count](#star-review-count)
    - [Display a recent 5-star review for a product](#five-star-review)
    - [Display visual UGC by product](#visual-ugc)
    - [Display a customer's loyalty balance in an email](#loyalty-balance)

### Display a product's star rating and review count {#star-review-count}

Use this snippet to provide the public average score and number of total reviews for a product that is included in the email:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

Replace `<YOTPO-API-KEY>` with your Yotpo reviews API key. The `product_id` will be pulled dynamically from Braze. For the integration to work, the `product_id` in Braze must match the product ID in Yotpo (typically the eCommerce parent product ID).

![YOTPO-API-KEY를 Yotpo 리뷰 API 키로 교체합니다.]({% image_buster /assets/img/yotpo/image2.png %})

### 제품의 최근 5점 별점 리뷰 표시 {#five-star-review}

Use this snippet to provide a top (published) review for a specific product that is included in the email:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Replace `<YOTPO-API-KEY>` with your Yotpo reviews API key. The `product_id` will be pulled dynamically from Braze. For the integration to work, the `product_id` in Braze must match the product ID in Yotpo (typically the eCommerce parent product ID).

Here's what the snippet in your email editor will look like:

![최근 별 5개 리뷰에 대한 스니펫을 표시하는 이메일 편집기 예시]({% image_buster /assets/img/yotpo/image3.png %})

### 제품별 시각적 UGC 표시 {#visual-ugc}

Use this snippet to retrieve tagged and published Yotpo images and add them to your emails instead of the stock image or as an additional gallery:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Replace `<YOTPO-API-KEY>` with your Yotpo reviews API key. The `product_id` will be pulled dynamically from Braze. For the integration to work, the `product_id` in Braze must match the product ID in Yotpo (typically the eCommerce parent product ID).

The snippet will look something like this:

![Yotpo에 게시된 이미지 스니펫을 보여주는 이메일 편집기 예제]({% image_buster /assets/img/yotpo/image4.png %})

### 이메일에 고객 로열티 잔액 표시하기 {#loyalty-balance}

Use this snippet to retrieve a customer's loyalty point balance and use it in your email messaging:

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Replace `<YOTPO-LOYALTY-GUID>` and `<YOTPO-LOYALTY-API-KEY>` with your Yotpo loyalty credentials. The `email_address` is pulled dynamically from Braze. For the integration to work, the email must be the email address of the customer receiving the email.

스니펫은 다음과 비슷합니다.

![고객 로열티 잔액 스니펫을 보여주는 이메일 편집기 예제]({% image_buster /assets/img/yotpo/image5.png %})

## 자주 묻는 질문 {#faq}

### What if I don't have a 5-star review?

If you don't have any 5-star reviews (such as if the endpoint response returns NULL for the 5-star review), then no content will be displayed.

### What if I don't have an image published for a product?

If you don't have any images for a product (such as if the endpoint response returns NULL for the product image), then no content will be displayed.

### Can I customize the look and feel, or pull other data fields from Yotpo?

Yes! To discover other data points and customization options available, refer to [Making an API call]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). You may need some assistance from a front-end developer to do so.

{% alert note %}
Yotpo does not support custom requirements beyond what is described in this guide.
{% endalert %}


