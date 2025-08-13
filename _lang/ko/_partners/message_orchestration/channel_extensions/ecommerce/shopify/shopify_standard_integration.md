---
nav_title: Shopify Standard Integration Setup
article_title: "Shopify Standard Integration Setup"
description: "This reference article outlines how to set up the standard Shopify integration."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify standard integration setup

> This page walks you through how to integrate Braze with Shopify using our standard integration for users with a Shopify online store. If you use a Shopify headless site or are looking to implement more tailored solutions, refer to [Shopify custom integration setup]({{site.baseurl}}/shopify_custom_integration/).

## 1단계: Shopify 스토어 연결

1. Braze에서 **파트너 통합** > **기술 파트너로** 이동한 다음 "Shopify"를 검색합니다.

{% alert note %}
If you’re using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

{: start="2"}
2\. On the Shopify partner page, select **Begin setup** to start the integration process.<br><br>![Shopify integration page with button to begin setup.][1]<br><br> 
3\. In the Shopify app store, install the Braze application.<br><br>![The Braze app store page with a button to install the application.][5]{: style="max-width:70%;"}

{% alert note %}
If your Shopify account is associated with more than one store, you can change the store you’re logged into by selecting the store icon at the top-right of the page and selecting **Switch stores**.
{% endalert %}

{: start="4"}
4\. After installing the Braze app, you’ll be redirected to Braze to confirm the workspace you want to connect to Shopify. A Shopify store can connect to only one workspace. If you need to switch, select the correct workspace.<br><br>![A window asking you to confirm that you’re in the right workspace.][2]{: style="max-width:70%;"}

{: start="5"}
5\. Select **Begin setup**.<br><br>!["Integration settings" with field to enter domain and a button to begin setup.][9]

## 2단계: Enable Braze Web SDKs

For Shopify online stores, you can select the standard setup to automatically implement the Braze Web SDK and JavaScript SDK.

![“Enable Web SDK” step with options to implement through a standard setup or custom setup.][3]

After you select the standard setup onboarding path, you’ll need to choose when Braze should initialize and load the SDKs from one of the following options: 
- Upon site visit, such as session start
    - Tracks both identified and anonymous users
- Upon account signup, such as account login
    - 식별된 사용자만 추적
    - Starts tracking data when site visitors sign up or log into their accounts

## 3단계: Configure your Shopify data

### Standard data setup

Now you’ll select the Shopify data you want to track.

![“Tracking Shopify data” section with a checkbox to track behavioral events and user attributes.][6]

The following events will be enabled by default in the standard integration.

| Braze recommended events | Shopify 커스텀 이벤트 | Shopify 커스텀 속성 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>조회한 제품</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

For more information on the data tracked through the integration, refer to [Shopify Data Features]({{site.baseurl}}/shopify_data_features/).

### Historical backfill setup

Through the standard setup, you have the option to perform an initial load of your Shopify customers and orders from the last 90 days prior to your Shopify integration connection. To do so, select the checkbox to include the initial data load as part of your integration. 

![Historical data backfill toggle.][4]

This table contains the data that will be initially loaded through the backfill.

| Braze recommended events | Shopify 커스텀 이벤트 | 브레이즈 표준 속성 | Braze subscription statuses |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>이메일</li><li>이름</li><li>성</li><li>전화</li><li>도시</li><li>국가</li></ul>{:/} | {::nomarkdown}<ul><li>Email marketing subscriptions associated with this Shopify store</li><li>SMS marketing subscriptions associated with this Shopify store</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

As your Shopify customer records are loaded into Braze, the Shopify customer ID will be used as the Braze external ID. 

{% alert note %}
If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify data features]({{site.baseurl}}/shopify_data_features/#historical-backfill) for more details.
{% endalert %}

### (Advanced) Custom data tracking setup

With the Braze SDKs, you can track custom events or custom attributes that go beyond standard events for this integration. Custom events capture unique interactions in your store, such as:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">사용자 지정 이벤트</th>
      <th style="width: 50%;">사용자 지정 속성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>커스텀 할인 코드 사용</li>
          <li>개인화된 제품 추천과 상호 작용</li>
          <li>선물 메시지를 주문에 추가</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>브랜드 또는 제품 즐겨찾기</li>
          <li>선호하는 구매 카테고리</li>
          <li>멤버십 또는 로열티 상태</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Tracking custom data helps you gain deeper insights into user behavior and personalize their experience even further. To implement custom events, you need to edit your [storefront's theme code](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in the `theme.liquid` file. You may need help from your developers.

예를 들어 다음 JavaScript 스니펫은 현재 사용자의 뉴스레터 구독 여부를 추적하고 Braze의 고객 프로필에서 이를 커스텀 이벤트로 기록합니다.

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

The SDK must be initialized (listening for activity) on a user's device to log events or custom attributes. To learn more about logging custom data, refer to [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) and [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## 4단계: Configure how you manage users

First, select your `external_id` from the dropdown. 

![“Collect subscribers” section.][10]

{% alert important %}
Using an email address or a hashed email address as your Braze external ID can help simplify identity management across your data sources. However, it's important to consider the potential risks to user privacy and data security.<br><br>

- **Guessable Information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of Exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.
{% endalert %}

Second, you have the option to collect your email or SMS marketing opt-ins from Shopify. 

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

![“Collect subscribers” section with option to collect email or SMS marketing opt-ins.][13]

{% alert note %}
As mentioned in [Shopify overview]({{site.baseurl}}/shopify_overview/), if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your `theme.liquid` file:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Sets the email address on the user profile
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Updates the global email subscription status
{% endalert %}

## 5단계: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. Automatic updates occur in near real-time so your catalog always reflects the latest product details. To learn more, check out [Shopify product sync]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/).

![Step 4 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".][11]{: style="max-width:80%;"}

## 6단계: Activate Channels (optional)

You can enable in-app messages without using a developer by configuring them in your setup.

![Setup step to activate channels, with the available option being in-browser messaging.][13]

### Supporting additional SDK channels

The Braze SDKs enable various messaging channels, including in-app messages and Content Cards.

#### Content Cards and Feature Flags

To add content cards or feature flags, you will need to collaborate with your developers to insert the necessary SDK code directly into your `theme.liquid` file. For detailed instructions, refer to [Integrating the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### 웹 푸시 알림

Web push currently isn't supported for the Shopify integration. If you want to see this supported in the future, submit a product request through the [Braze product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

If you wish to see this supported in the future, submit a product request through the Braze [product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## 7단계: 설정 완료

1. 설정을 구성한 후 **설정 완료**를 선택합니다.
2. Enable the Braze app embed within your Shopify theme settings. Select **Open Shopify** to be redirected to your Shopify account to enable the app embed within your store’s theme settings. 

![Banner that says you need to active the Braze app embed in Shopify and contains a button to open Shopify.][7]

{: start="3"}
3\. After you enable the app embed, your setup is complete!
Confirm you can view your integration settings, the status of initial data sync, and your active Shopify events. <br><br>![Shopify partner page displaying the integration settings.][8]

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}
[13]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}