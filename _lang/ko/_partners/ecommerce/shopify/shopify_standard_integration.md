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

## Step 1: Connect your Shopify store

1. In Braze, go to **Partner Integrations** > **Technology Partners** and then search for “Shopify”.

{% alert note %}
If you’re using the older navigation, you can find **Technology Partners** under **Integrations**.
{% endalert %}

{: start="2"}
2\. On the Shopify partner page, select **Begin setup** to start the integration process.<br><br>![Shopify integration page with button to begin setup.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. In the Shopify app store, install the Braze application.<br><br>![The Braze app store page with a button to install the application.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
If your Shopify account is associated with more than one store, you can change the store you’re logged into by selecting the store icon at the top-right of the page and selecting **Switch stores**.
{% endalert %}

{: start="4"}
4\. After installing the Braze app, you’ll be redirected to Braze to confirm the workspace you want to connect to Shopify. A Shopify store can connect to only one workspace. If you need to switch, select the correct workspace.<br><br>![A window asking you to confirm that you’re in the right workspace.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Select **Begin setup**.<br><br>!["Integration settings" with field to enter domain and a button to begin setup.]({% image_buster /assets/img/Shopify/choose_account.png %})

## 2단계: Enable Braze Web SDKs

For Shopify online stores, you can select the standard setup to automatically implement the Braze Web SDK and JavaScript SDK.

![“Enable Web SDK” step with options to implement through a standard setup or custom setup.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

After you select the standard setup onboarding path, you’ll need to choose when Braze should initialize and load the SDKs from one of the following options: 
- Upon site visit, such as session start
    - Tracks both identified and anonymous users
- Upon account signup, such as account login
    - Track only identified users
    - Starts tracking data when site visitors sign up or log into their accounts

## Step 3: Configure your Shopify data

### Standard data setup

Now you’ll select the Shopify data you want to track.

![“Tracking Shopify data” section with a checkbox to track behavioral events and user attributes.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

The following events will be enabled by default in the standard integration.

| Braze recommended events | Shopify custom events | Shopify custom attributes |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Product viewed</li><li>Cart updated</li><li>Checkout started</li><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

For more information on the data tracked through the integration, refer to [Shopify Data Features]({{site.baseurl}}/shopify_data_features/).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### Historical backfill setup

Through the standard setup, you have the option to perform an initial load of your Shopify customers and orders from the last 90 days prior to your Shopify integration connection. To do so, select the checkbox to include the initial data load as part of your integration. 

![Historical data backfill toggle.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

This table contains the data that will be initially loaded through the backfill.

| Braze recommended events | Shopify custom events | Braze standard attributes | Braze subscription statuses |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Order placed</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>Email</li><li>First Name</li><li>Last Name</li><li>Phone</li><li>City</li><li>Country</li></ul>{:/} | {::nomarkdown}<ul><li>Email marketing subscriptions associated with this Shopify store</li><li>SMS marketing subscriptions associated with this Shopify store</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

As your Shopify customer records are loaded into Braze, the Shopify customer ID will be used as the Braze external ID. 

{% alert note %}
If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify data features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) for more details.
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
      <th style="width: 50%;">Custom events</th>
      <th style="width: 50%;">Custom attributes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Using a custom discount code</li>
          <li>Interacting with a personalized product recommendation</li>
          <li>Adding a gift message to their order</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Favorite brands or products</li>
          <li>Preferred shopping categories</li>
          <li>Membership or loyalty status</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

커스텀 데이터를 추적하면 사용자 행동에 대한 심층적인 인사이트를 확보하고 추가적인 개인화를 지원할 수 있습니다. To implement custom events, you need to edit your [storefront's theme code](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) in the `theme.liquid` file. You may need help from your developers.

For example, the following JavaScript snippet tracks if the current user subscribes to a newsletter, and logs that as a custom event on their profile in Braze:

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

## 4단계: 사용자 관리 방법 구성하기 {#step-4}

Select your `external_id` type from the dropdown. 

![“Collect subscribers” section.]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있습니다. However, it's important to consider the potential risks to user privacy and data security.<br><br>

- **Guessable Information:** Email addresses are easily guessable, making them vulnerable to attacks.
- **Risk of Exploitation:** If a malicious user alters their web browser to send someone else's email address as their external ID, they could potentially access sensitive messages or account information.
{% endalert %}

기본값으로 Braze는 Shopify의 이메일을 외부 ID로 사용하기 전에 소문자로 자동 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우 이메일 주소를 외부 ID로 할당하기 전이나 다른 데이터 소스에서 해시하기 전에 이메일 주소도 소문자로 변환되었는지 확인하세요. 이렇게 하면 외부 ID의 불일치를 방지하고 Braze에서 중복된 고객 프로필이 생성되는 것을 방지할 수 있습니다.

{% alert note %}
다음 단계는 외부 ID 선택에 따라 달라집니다:<br><br>
- **커스텀 외부 ID 유형을 선택한 경우:** 4.1~4.3단계를 완료하여 커스텀 외부 ID 구성을 설정합니다.
- **Shopify 고객 ID, 이메일 또는 해시된 이메일을 선택한 경우:** 4.1~4.3단계를 건너뛰고 바로 4.4단계로 계속 진행합니다.
{% endalert %}

### Step 4.1: `braze.external_id` 메타필드 만들기

1. Shopify 관리자 패널에서 **설정** > **메타필드 및 메타객체로** 이동합니다.
2. **고객** > **정의 추가를** 선택합니다.
3. **이름에** `braze.external_id` 을 입력합니다. 
4. 자동 생성된 네임스페이스를 선택하고 키(`custom.braze_external_id`)를 눌러 편집하여 `braze.external_id` 으로 변경합니다.
5. **유형에서** **ID 유형을** 선택합니다.

메타필드가 생성되면 고객을 위해 메타필드를 채웁니다. 다음과 같은 방법을 권장합니다:

- **고객 제작 웹훅을 들어보세요:** [`customer/create` 이벤트를](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) 수신하도록 웹훅을 설정합니다. 이를 통해 새 고객이 생성될 때 메타필드를 작성할 수 있습니다.
- **기존 고객을 다시 채우세요:** [관리자 API](https://shopify.dev/docs/api/admin-graphql) 또는 [고객 API를](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) 사용하여 이전에 생성한 고객의 메타필드를 다시 채우세요.

### Step 4.2: 외부 ID를 검색할 엔드포인트 만들기

외부 ID를 검색하기 위해 Braze가 호출할 수 있는 공용 엔드포인트를 만들어야 합니다. 이렇게 하면 Shopify에서 `braze.external_id` 메타필드를 직접 제공할 수 없는 시나리오에서 Braze가 ID를 가져올 수 있습니다.

#### 엔드포인트 사양

**Method:** GET

Braze는 다음 매개변수를 엔드포인트로 전송합니다:

| 매개변수            | 필수 | 데이터 유형 | 설명                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | 예      | 문자열    | Shopify 고객 ID입니다.                                         |
| shopify_storefront   | 예      | 문자열    | 요청에 대한 상점 이름입니다. Ex: `<storefront_name>.myshopify.com` |
| email_address        | 아니요       | 문자열    | 로그인한 사용자의 이메일 주소입니다. <br><br>특정 웹훅 시나리오에서는 이 필드가 누락될 수 있습니다. 엔드포인트 로직은 여기서 null 값을 고려해야 합니다(예: 내부 로직에 필요한 경우 shopify_customer_id 을 사용하여 이메일을 가져옵니다). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### 엔드포인트 예시

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### 예상 응답
Braze는 외부 ID JSON을 반환하는 `200` 상태 코드를 기대합니다:
```json
{
  "external_id": "my_external_id"
}
```

#### 검증
`shopify_customer_id` 및 `email_address` (있는 경우)이 Shopify의 고객 값과 일치하는지 확인하는 것이 중요합니다. [Shopify 관리자 API](https://shopify.dev/docs/api/admin-graphql) 또는 [고객 API를](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) 사용하여 이러한 매개 변수의 유효성을 검사하고 올바른 `braze.external_id` 메타필드를 검색할 수 있습니다.

#### 실패 동작 및 병합
`200` 이외의 상태 코드는 모두 실패로 간주됩니다.

- **의미 병합:** 엔드포인트가 실패하면(`200` 가 아닌 반환되거나 시간 초과), Braze는 외부 ID를 검색할 수 없습니다. 따라서 Shopify 사용자와 Braze 사용자 프로필 간의 병합은 해당 시점에 이루어지지 않습니다.
- **로직을 다시 시도합니다:** Braze는 표준 즉시 네트워크 재시도를 시도할 수 있지만, 실패가 지속되면 다음 적격 이벤트(예: 사용자가 프로필을 업데이트하거나 결제를 완료할 때)까지 병합이 연기됩니다.
- **지원 가능성:** 적시에 사용자 병합을 지원하려면 엔드포인트의 가용성이 높고 `email_address` 필드를 원활하게 처리하는지 확인하세요.

### Step 4.3: 외부 ID를 입력하세요.

[4단계를](#step-4) 반복하고 Braze 외부 ID 유형으로 커스텀 외부 ID를 선택한 후 엔드포인트 URL을 입력합니다.

#### 고려 사항

- Braze가 엔드포인트에 요청을 보낼 때 외부 ID가 생성되지 않은 경우 통합은 `changeUser` 함수가 호출될 때 기본값으로 Shopify 고객 ID를 사용합니다. 이 단계는 익명 사용자 프로필을 식별된 사용자 프로필과 병합하는 데 매우 중요합니다. 따라서 일시적으로 워크스페이스 내에 여러 유형의 외부 ID가 존재할 수 있습니다.
- `braze.external_id` 메타필드에서 외부 ID를 사용할 수 있으면 통합에서 이 외부 ID에 우선순위를 지정하여 할당합니다. 
    - 이전에 Shopify 고객 ID가 Braze 외부 ID로 설정된 경우 `braze.external_id` 메타필드 값으로 대체됩니다. 

### 4.4단계: Collect your email or SMS opt-ins from Shopify (optional)

You have the option to collect your email or SMS marketing opt-ins from Shopify. 

If you use the email or SMS channels, you can sync your email and SMS marketing opt-in states into Braze. If you sync email marketing opt-ins from Shopify, Braze will automatically create an email subscription group for all users associated with that specific store. You need to create a unique name for this subscription group.

![“Collect subscribers” section with option to collect email or SMS marketing opt-ins.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
As mentioned in [Shopify overview]({{site.baseurl}}/shopify_overview/), if you want to use a third-party capture form, your developers need to integrate Braze SDK code. This will let you capture the email address and global email subscription status from form submissions. Specifically, you need to implement and test these methods to your `theme.liquid` file:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Sets the email address on the user profile
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Updates the global email subscription status
{% endalert %}

## Step 5: Sync products (optional)

You can sync all products from your Shopify store to a Braze catalog for deeper messaging personalization. 자동 업데이트가 거의 실시간으로 이루어지므로 카탈로그에 최신 제품 세부 정보가 반영됩니다. To learn more, check out [Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Step 4 of the set up process with "Shopify Variant ID" as the "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## 6단계: Activate Channels (optional)

You can enable in-app messages without using a developer by configuring them in your setup.

![Setup step to activate channels, with the available option being in-browser messaging.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. 이 정보는 Shopify로 전송됩니다. 판매자는 이 데이터를 통해 매장 방문자를 인식하고 보다 개인화된 쇼핑 경험을 제공할 수 있습니다. For more details, refer to [Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Supporting additional SDK channels

The Braze SDKs enable various messaging channels, including Content Cards.

#### Content Cards and Feature Flags

To add content cards or feature flags, you will need to collaborate with your developers to insert the necessary SDK code directly into your `theme.liquid` file. For detailed instructions, refer to [Integrating the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Web push notifications

현재 웹 푸시는 Shopify 통합에서 지원되지 않습니다. 지원을 요청하려면 [Braze 제품 포털을]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) 통해 제품 요청을 제출하세요.

## 7단계: Finish setup

1. After you configure your setup, select **Finish Setup**.
2. Enable the Braze app embed within your Shopify theme settings. Select **Open Shopify** to be redirected to your Shopify account to enable the app embed within your store’s theme settings. 

![Banner that says you need to active the Braze app embed in Shopify and contains a button to open Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. After you enable the app embed, your setup is complete!
Confirm you can view your integration settings, the status of initial data sync, and your active Shopify events. <br><br>![Shopify partner page displaying the integration settings.]({% image_buster /assets/img/Shopify/install_complete.png %})