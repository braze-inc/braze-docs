---
nav_title: "Consent Management"
permalink: "/consent_management/"
hidden: true
layout: dev_guide
---

# Consent management 

> This guide aggregates best practices for managing consent for email, push, SMS, WhatsApp, and data used for Targeted Advertising to stay compliant with data privacy laws and regulations and build better customer experiences.

{% alert note %}
The content presented here is meant for educational purposes only and should not be considered as legal counsel. Braze recommends that all of our customers and all e-commerce retailers seek legal advice to receive guidance on how they can effectively adhere to data protection regulations that apply to their unique situation.
{% endalert %}

## Collecting user consent

Collecting marketing consent from your users is critical to appropriately target your audiences and stay compliant. Provide clarity to your users on which channels they subscribe to and what they should expect by subscribing. You can utilize Braze’s flexible tools to collect and update consent for various channels. 

You’ll begin to review some of the specific tools Braze offers at a high level below.

#### Email capture forms

Brands can quickly generate email capture forms on their website or mobile apps through Braze’s email capture form template. 

For more information, review [Email capture form]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/email_capture_form/).

#### Email preference center

You can implement Braze's Preference Center as an easy and flexible way to manage which users receive certain groups of newsletters. Each subscription group you create is added to the preference center list. Braze will manage the subscription state updates from the preference center, which keeps the preference center in sync.

To learn more about how to add or customize a preference center, refer to [Preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/).

#### Managing consent via REST APIs, SDKs, and CSV

{% tabs %}
{% tab REST APIs %}
Brands can programmatically collect and update email, SMS, WhatsApp, push, and Ad Tracking consent through Braze’s REST APIs. Here are some use cases and how to leverage specific endpoints to collect and update consent for specific channels.

| Use Case | Details |
| -------- | ------- |
| Email global subscription state | Use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to update the `email_subscribe` attribute for a given user. This will set the global subscription state for email.<br><br>See [email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details. | 
| Email open pixel and click tracking | Use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to update `email_open_tracking_disabled` and `email_click_tracking_disabled` for a given user.<br><br>See email [open pixel and click tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/email_tracking) for more details. |
| Subscription groups for email, SMS, WhatsApp | User profiles can be programmatically set by the [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) endpoint by using Braze’s REST API.<br><br>See documentation for [email]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/), [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/opt-ins/), and [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription#subscription-groups) for channel specific details. |
| Push enablement & subscription state | Use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to update the `push_subscribe` attribute for a given user.<br><br>See [push enablement and subscription]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) for more details. |
| Ad Tracking consent custom data | Use the [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint to create and update a custom attribute that will track consent for Ad Tracking.<br><br>See [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) for more details. |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% tab SDKs %}
Brands can programmatically collect and update consent for email, SMS, WhatsApp, push, and data used for Targeted Advertising through Braze’s SDKs. Here are some use cases and how to leverage Braze’s SDKs to collect and update consent for specific channels.

| Use Case | Details |
| -------- | ------- |
| Email global subscription state | Use the Braze SDK to update a user’s global subscription state for email.<br><br>To do this, use the `setEmailNotificationSubscriptionType` method on [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-email-notification-subscription-type.html), or [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#ae8ef1e78bfafde343974a004ca81bb74).<br><br>See [email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) for more details. | 
| Subscription groups for email, SMS, WhatsApp | Users can be added to an email, SMS, or WhatsApp subscription group using the `addToSubscriptionGroup` or `removeToSubscriptionGroup` methods for [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287), or [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).<br><br>See documentation for [email]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/), [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/opt-ins/), and [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription#subscription-groups) for channel-specific details. |
| Push enablement & subscription state | Use the Braze SDK to update a user’s subscription state. For example, you can add a settings page to your app where users can turn push notifications for their profile on or off.<br><br>To do this, use the `setPushNotificationSubscriptionType` method on [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html), or [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#afb2c11d1889fd08537f90ee64c94efb3).<br><br>See [push enablement and subscription]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) for more details. |
| Ad Tracking consent custom data | Use the Braze SDK to create and update a custom attribute that will track consent for Ad Tracking or Do Not Sell or Share under CCPA.<br><br>To do this, use the `setCustomUserAttribute` method on [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setcustomuserattribute), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-custom-attribute.html), or [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#abccfa73329731620008339c76a6f4272). |
| iOS IDFA collection<br>(mobile advertiser ID) | You can use the Braze iOS SDK to collect the iOS IDFA. To collect the IDFA, you’ll need to implement the `ABKIDFADelegate`, and your application will need to request authorization from the user using Apple’s `ATTrackingManager` in the app tracking transparency framework.<br><br>See [Optional IDFA collection]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) for more details. |
| Android GAID collection<br>(mobile advertiser ID) | You have the option to use the Braze Android SDK to collect the Google Advertising ID (GAID). You’ll need to implement the `Braze.setGoogleAdvertisingId()` method to manually set the GAID.<br><br>See [Google Advertising ID (optional)]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) for more details. |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% tab CSV %}
You may need to import user data manually using the **User Import** page. Here are some use cases and how to leverage Braze’s SDKs to collect and update consent for specific channels. You can also refer to [User import] for more details on how to construct your CSVs.

| Use Case | Details |
| -------- | ------- |
| Email global subscription state | Update users’ global subscription state for email by including the `email_subscribe` column within your CSV. |
| Email open pixel and click tracking | Update opt-ins for email open and click tracking by including these two columns in your CSV: `email_open_tracking_disabled` and `email_click_tracking_disabled`. |
| Subscription groups for email, SMS, WhatsApp | Users can be added to email, SMS, or WhatsApp subscription groups via user import. When updating the subscription group status, you must have these two columns in your CSV: `subscription_group_id` and `subscription_state`. 
| Push enablement & subscription state | Update users’ global subscription state for push by including the `push_subscribe` column within your CSV. |
| Ad Tracking consent custom data | Import custom data that is relevant to Ad Tracking consent by adding new columns that do not match any of the default user data to your CSV.<br><br>See [Importing Custom Data]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#importing-custom-data) for more details. |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% endtabs %}

## How to check users’ subscription states

You can view users’ subscription statuses for email, SMS, and push, along with the subscription groups the user is associated with within the **Engagement Tab** of the **User Profile**. 

See [User Profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#engagement-tab) for more details. 

## Using consent states within campaigns and Canvases

User Targeting

Send Settings

## List hygiene 

Clean your lists
It's important to not email customers who have not opted-in to your marketing and those who do not regularly engage with your brand, to maintain good deliverability in the eyes of inbox providers. List cleaning is the process of identifying customers who aren't engaged and excluding them from your messaging. 

Refer to [List cleaning]() for more information.

## In-depth best practices by channel

Before you launch any campaigns or Canvases, please review [Know Before You Send]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/). 

Each channel has unique best practices to comply with data privacy laws and regulations. Although this guide provides a high-level overview of how brands can leverage Braze’s flexible tooling to manage consent, it is important that Braze customers review the requirements of each channel in more detail. 

- Email 
	- [Managing email subscriptions]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/)
	- [Email preference center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center)
- SMS
	- [SMS laws & regulations]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)
	- [Collecting user opt-ins]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/opt-ins/)
- WhatsApp 
	- [WhatsApp opt-in and opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)
- Push
	- [Push primer in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- Ad tracking in audience sync 
	- [Audience sync]({{site.baseurl}}/partners/canvas_steps)
