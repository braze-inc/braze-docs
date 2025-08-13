---
nav_title: Shopify 개요
article_title: "Shopify 개요"
description: "이 참조 문서에서는 글로벌 커머스 회사인 Shopify와 Braze 간 파트너십을 간략히 설명합니다. 이를 통해 Shopify 스토어와 Braze를 원활하게 연결하여 일부 Shopify 웹훅을 Braze로 전달할 수 있습니다. Braze의 크로스채널 전략과 캔버스를 활용하여 고객이 구매를 완료하도록 넛지하거나 이전 구매를 기반으로 사용자를 리타겟팅합니다."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify 개요

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a business of any size. Shopify는 안정성을 위해 설계된 플랫폼과 서비스를 통해 전 세계 소비자에게 더 나은 쇼핑 경험을 제공하는 동시에 모든 사람에게 더 나은 상거래를 제공합니다.

The Braze integration with Shopify provides a powerful solution for ecommerce businesses looking to enhance their customer engagement and drive personalized marketing efforts. This integration seamlessly connects Shopify's robust ecommerce capabilities with our advanced customer engagement platform, enabling you to deliver targeted, relevant, and timely messages to your users based on real-time shopping behaviors and transactional data.

## 요구 사항

| 요구 사항 | 설명 |
| --- | --- |
| Shopify 스토어 | You have an active Shopify store. |
| Shopify store owner or staff member permissions | {::nomarkdown}<ul><li>Access to all General and Online Store settings.</li><li> Additional Admin Permissions:</li><ul><li>주문: 보기</li><li>Customer: ReadWrite</li><li>View Customer Events (Web Pixels)</li><li>설정 관리</li><li>View Apps Developed by Staff/Collaborators</li><li>Manage/Install Apps and Channels</li><li>Manage/Add Custom Pixels</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How to integrate 

Braze offers two integration options for Shopify merchants that are designed to meet the diverse needs of eCommerce businesses: **Standard integration** and **Custom integration**.

### Standard integration

The [standard integration]({{site.baseurl}}/shopify_standard_integration/) is tailored for Shopify online stores, providing a seamless and straightforward setup process. This option allows you to quickly connect your Shopify store to Braze, empowering you to leverage powerful customer engagement tools without extensive technical expertise. With this integration option, you can sync customer data, automate personalized messaging, and enhance your marketing efforts through comprehensive Braze features.

### Custom integration

The custom integration offers a more flexible and composable solution if you use Shopify Hydrogen or support a headless store. This option empowers you to implement Braze SDKs directly into your Shopify environment, enabling deeper integration and tailored functionalities. Whether you’re looking to create unique customer experiences or optimize specific workflows, the [custom integration]({{site.baseurl}}/shopify_custom_integration/) provides the tools necessary to fully leverage Braze’s capabilities in a headless setup.

## 통합 작동 방식

If you've already set up and turned on historical backfill in your configuration settings, the intial data sync will immediately begin. Braze will import all customers and order placed events from the last 90 days prior to your Shopify integration connection. When Braze imports your Shopify customers, we will assign the `external_id` type that you chose in your configuration settings.

Following the initial data sync, Braze will continuously track new data and updates, directly from Shopify and Braze SDKs.

{% alert note %}
If you’re an existing Braze customer with active campaigns or Canvases, review [Shopify historical backfill]({{site.baseurl}}/shopify_features#historical-backfill) for important information. To see what specific customer data is being backfilled, refer to [Shopify features]({{site.baseurl}}/shopify_features/#shopify-data).
{% endalert %}

### User and data syncing

After the integration is live, Braze will gather user data from two key sources through the Shopify integration:
- **Shopify Web Pixel API and app embeds:** This powers the Braze Web SDK and Javascript SDK to support on-site tracking, identity management, eCommerce behavioral data, and power messaging channels like in-app messages.
- **Shopify webhooks:** eCommerce behavioral data, product syncing, and subscriber collection

During integration onboarding, you will need to select when the Braze SDKs initialize and load your Shopify site: 
- Upon site visit (such as session start)
    - **What it does:** Tracks anonymous users—such as guest shoppers—to access more data for deeper personalization 
- Upon account signup (such as account login) 
    - **What it does:** Prevents anonymous user tracking for a more conservative, privacy-oriented approach, so user activity is tracked *after* the user signs into their account

{% alert note %}
- Website visits (sessions) count towards your Monthly Active User (MAU) allotments.
- The Braze Web SDK and JavaScript SDK versions will automatically set to v5.4.0.
{% endalert %}

Braze uses the Shopify integration to support multiple identifiers that track your users from their guest shopping experience until they become an identified users:

| Braze identifier | 설명 |
| --- | --- |
| Braze `device_id` | A randomly generated ID stored in the browser that tracks anonymous user activity through Braze SDKs. |
| Cart token user alias | An alias that Braze creates to track cart update events. This token is created by using Shopify cart token. |
| Checkout token user alias | An alias that Braze creates when the user starts the checkout process. This token is created by using the Shopify checkout token. |
| Shopify customer ID alias | The Shopify customer ID is assigned as an alias when the external ID is assigned during account login or when an order is placed. |
| Braze `external_id` | A unique identifier that helps track customers across devices and platforms. This maintains a consistent user experience and improves analytics by preventing multiple profiles when users switch devices or reinstall the app.<br><br>The Shopify integration supports the following `external_id` types: <br><br>{::nomarkdown}<ul><li>Shopify customer ID (default)</li><li>Hashed email (SHA-256)</li><li>Hashed email (SHA-1)</li><li>Hashed email (MD5)</li><li>이메일</li></ul>{:/}Braze assigns an `external_id` to your users by calling the changeUser method within the SDKs when: <br><br>{::nomarkdown}<ul><li>A user logs in or creates an account</li><li>An order is placed</li></ul>{:/}<br> For more information on what happens when you assign an `external_id` to an anonymous profile, refer to [User profile lifecycle]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze will also leverage the `external_id` to attribute downstream eCommerce behavioral data from Shopify webhooks.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The integration requires Braze SDKs and Shopify services to work together to appropriately track and attribute Shopify data to the right users in near-real time. To find more details on the data tracked through the integration, see [Shopify data]({{site.baseurl}}/shopify_features#shopify-data).

{% alert note %}
- If you're testing the integration, we advise you to use incognito mode or clear your cookies to reset the Braze `device_id` and mimic the behavior of an anonymous user.
- Even though a Shopify customer ID is generated when an email is entered into the Shopify newsletter footer or during the checkout process before an order is placed, that customer ID isn't accessible through Shopify Web Pixels. Because of this, Braze can't use the `changeUser` method in these two situations.
{% endalert %}

### Syncing Shopify email and SMS marketing opt-ins

If you enable subscriber collection in your configuration settings, you need to assign a subscription group for each store you connect to Braze. This means your customers will be categorized as either “subscribed” or “unsubscribed” to your store’s subscription group.

The Shopify marketing opt-in status for email and SMS marketing can be updated in the following ways:
- **Manual update:** You can manually change a user’s email or SMS marketing opt-in status in your Shopify admin.
- **Shopify newsletter footer:** If a user enters their email in the Shopify default newsletter footer, their opt-in status will be updated.
- **Checkout process:** If a user updates their opt-in status during checkout.

{% alert note %}
The email marketing opt-in status from Shopify will not change a user’s [global email subscription state]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) in Braze. The default subscription state when a user profile is created is “subscribed.” Remember to use the subscription group as part of your campaign or Canvas entry criteria.
{% endalert %}

This table shows which Shopify marketing opt-in states correlate with the statuses within your Braze subscription group. 

| Shopify marketing opt-in state | Braze subscription group state |
| --- | --- |
| Email is subscribed | 가입됨 |
| Email is unsubcribed | 탈퇴됨 |
| Email is pending confirmation | 탈퇴됨 |
| Email is invalid | 탈퇴됨 |
| SMS subscribed | 가입됨 |
| SMS unsubscribed | 탈퇴됨 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Sign-up forms

#### Shopify newsletter footer

Users who enter their email address into the Shopify newsletter footer will experience one of these workflows:

##### Users who haven't logged into their account

1. Braze receives an inbound Shopify webhook whenever a customer is created or updated.
2. Braze creates a user profile containing the email address and Shopify customer ID alias that are associated with that user.
3. The Braze SDK updates the anonymous profile with the email address.

{% alert note %}
This might result in a duplicate profile until the user identifies themselves by creating their account, logging into their account, or placing an order. Braze offers bulk merging tools to help you automate the reconciliation of duplicate profiles. Refer to [Duplicate users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/) for more details.
{% endalert %}

##### Users who have already logged into their account

Braze will create a user profile containing the email address and Shopify customer ID alias that are associated with that user. Braze won't update the logged-in user’s email address, because we assume that Shopify has already provided this information.

#### Braze sign-up forms

Braze provides two types of sign-up form templates:
- **[Email sign-up forms]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Create these using the drag-and-drop editor.
- **[Traditional editor email capture form]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** A more straightforward form for capturing email addresses.

When you use these sign-up form templates, Braze automatically updates the global email subscription status on the user profile. For more details on how the global email subscription state is handled, including information on on email validation, refer to documentation for each form template type.

{% alert note %}
Make sure to include entry criteria in your campaign or Canvas that includes both the global email subscription status and the subscription group that are connected to your Shopify store. This will help ensure that you are targeting the right audience.
{% endalert %}

#### Third-party sign-up forms 

If you're using a third-party platform or Shopify plugin for your sign-up forms, you need to work with your developers to integrate Braze SDK code to capture the email address and global email subscription status from form submissions. To learn more, review [Shopify standard integration setup]({{site.baseurl}}/shopify_standard_integration/) and [Shopify custom integration setup]({{site.baseurl}}/shopify_custom_integration/).

### Product syncing 

Braze supports the ability to sync your Shopify store’s products into a Braze catalog. For more details refer to [Shopify product syncs]({{site.baseurl}}/shopify_catalogs/).

## Data subject requests

As part of the Braze platform’s Shopify integration, Braze automatically receives [Shopify’s compliance webhooks](https://shopify.dev/docs/apps/build/privacy-law-compliance/). However, because customers are the data controllers of their End Users’ data, customers must carry out any actions required to address Data Subject Requests received with respect to End User data in Braze (including End User data received via the Shopify integration). Please see our [Data Protection Technical Assistance]({{site.baseurl}}/dp-technical-assistance) documentation for more details.