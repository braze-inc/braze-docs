---
nav_title: Connecting Multiple Stores
article_title: Shopify Multiple Store Support
alias: /shopify_connecting_multiple_stores/
page_order: 6
description: "This reference article covers how to connect and configure multiple Shopify stores to a single workspace."
---

# 여러 Shopify 스토어 연결

> Connect multiple Shopify store domains to a single workspace to have a holistic view of your customers across all markets. Build and launch automation programs and journeys in a single workspace without duplicating efforts across regional stores.  

{% alert important %}
This feature doesn't support Shopify Markets or Markets Pro. If you would like to request support for these, submit a [product request]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## 요구 사항

| Requirement | Description |
| ----------- | ----------- |
| Enable multiple stores | Contact your customer success manager to enable Shopify multiple store support. |
| Set up a Shopify store | Be sure that you've already [set up at least one Shopify store with Braze]({{site.baseurl}}/shopify_overview/). |
| Unique Shopify storefront domains for each region | Multiple store support is intended for use with unique Shopify store domains for different regional storefronts. <br><br>If you want to connect multiple sub-brands to Braze, we recommend creating separate workspaces for each sub-brand. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Connecting an additional store
After you install the Braze app to your Shopify store and install your first store, select **\+ Connect New Store**.

![Shopify 통합 페이지의 "+ 새 스토어 연결" 버튼을 클릭합니다.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

For your additional Shopify regional store, select **Begin setup**.

!["설정 시작" 버튼이 있는 "통합 설정" 섹션입니다.]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Like your first Shopify store integration, you can choose either between a standard or custom setup.

![표준 또는 커스텀 설정으로 Braze 웹 SDK를 구현할 수 있는 옵션이 있는 "Braze SDK 활성화" 섹션을 클릭합니다.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Choose the option that best fits your needs:

{% multi_lang_include shopify.md section='Integration Tabs' %}

To view each store integration and configure advanced settings, select a store in the dropdown menu.

![드롭다운 메뉴가 있는 "통합 설정"에서 Shopify 스토어를 선택합니다.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Syncing users across stores

### Shopify alias

When you connect multiple stores, synced Shopify users who have logged in or placed an order will receive a new alias in the format: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Braze external ID

You can choose from the following options for your Braze external ID:

|Option|Description|
|------|-----------|
|Shopify Customer ID|If you use Shopify's customer ID as your Braze external ID, each store will generate a unique customer ID for each user. This means that if a user interacts with multiple stores, they will have separate profiles in Braze.|
|Email, Hashed Email, or Custom External ID|If you use the email, hashed email, or custom external ID types, users who engage with multiple stores will have their profiles merged into a single consolidated profile when they log in or place an order.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Merged fields

When a user profile is synced, the following fields will be merged. For full details on merging behavior, refer to [Merge behavior]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Device information
- Total session count (combined from both profiles)
- Custom event and purchase data
- Custom event properties for segmentation (for example, “X times in Y days” where X ≤ 50 and Y ≤ 30)
- Event count (combined from both profiles)
- 첫 번째 및 마지막 이벤트 날짜(Braze는 가장 빠른 날짜와 가장 최근 날짜를 선택)
- Campaign interaction data (most recent date fields)
- Workflow summaries (most recent date fields)
- Message and engagement history
- Subscription groups

### Collecting subscribers (optional)

You can choose to collect subscribers directly through Braze (in your Shopify connector settings) or through API and SDK alternatives that sync data from Shopify.

{% tabs local %}
{% tab Shopify connector %}
In the **Manage users** step of your Shopify connector settings, you can use Braze to collect email and SMS subscriber opt-ins and organize them into a dedicated subscription group:

1. Create a unique subscription group for each store you connect. This helps you maintain accurate data about where subscribers are coming from.
2. Enable email and SMS subscriber collection.
{% endtab %}

{% tab Braze API or SDKs %}
Alternatively, you can sync email and SMS marketing opt-in information directly from Shopify using the Braze API or SDKs.

|Option|Resources|
|------|---------|
|API |- [Subscription group endpoints]({{site.baseurl}}/api/endpoints/subscription_groups/) to directly replace what is supported by the integration<br>- [`Users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) to set subscription group data or the [global email subscription state]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Braze preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) for more customized marketing opt-in collection options|
|SDKs |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Shopify data 

### Synced attributes

When you connect more than one store, the following attributes will be synced with the most recent state of the Shopify profile:
- First Name
- Last Name
- Email
- Gender
- Date of Birth
- Country
- City
- Last Used App
- Language
- Time Zone
- Shopify Tags
- Shopify Order Count
- Shopify Total Spent

### Supported events

#### eCommerce recommended events 

When you connect multiple stores, incoming eCommerce recommended events will include a source event property. This property identifies which storefront URL the event originated from, allowing you to use this information for segmentation or triggering specific use cases.

![`ecommerce.order_placed` 커스텀 이벤트를 수행하는 사용자를 입력하는 트리거가 있는 액션 기반 캔버스입니다.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

The supported eCommerce recommended events within the Shopify integration are:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify custom events 

Incoming Shopify custom events include an event property called `shopify_storefront`. This property indicates which storefront URL the event came from, allowing you to leverage it for segmentation or triggering use cases.

![`shopify_paid_order` 커스텀 이벤트를 수행하는 사용자를 입력하는 트리거가 있는 액션 기반 캔버스입니다.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Supported Shopify custom events include:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

For a complete overview of all event payloads, refer to [Shopify data features]({{site.baseurl}}/shopify_data_features/).

### Shopify product sync 

When you connect and configure each Shopify store in Braze, you can optionally enable the Shopify product sync as part of the integration.

각 스토어에 대해 제품 동기화를 활성화하는 경우 Braze는 카탈로그 이름에 Shopify 스토어 이름을 포함합니다. 이렇게 하면 다른 스토어와 제품을 구분할 수 있습니다.

![Shopify 스토어 이름으로 카탈로그를 생성합니다.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

