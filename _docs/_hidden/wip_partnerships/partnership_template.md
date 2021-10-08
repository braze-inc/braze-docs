---
nav_title: RevenueCat
page_order: 1

description: "RevenueCat automatically sends your customers purchase and subscription lifecycle events into Braze. This allows you to build campaigns that react to the subscription lifecycle stage of your customers. Want to engage with customers that opted out during their free trial? Send reminders to customers with billing issues? With accurate and up-to-date subscription data in Braze, you'll be set to turbocharge your campaigns."
alias: /partners/revenuecat/

page_type: partner
hidden: true
---

# RevenueCat

> RevenueCat is the single source-of-truth for your subscription status across iOS, Android, and web. Whether you are building a new app or already have millions of subscribers, you can use RevenueCat to build cross-platform in-app purchases, manage your products and subscribers, and analyze your IAP data - no server code required.

RevenueCat automatically sends your customers purchase and subscription lifecycle events into Braze. This allows you to build campaigns that react to the subscription lifecycle stage of your customers.

Want to engage with customers that opted out during their free trial? Send reminders to customers with billing issues? With accurate and up-to-date subscription data in Braze, you'll be set to turbocharge your campaigns.

## Requirements

At a minimum, you will need to enable the integration from the RevenueCat dashboard in order to connect RevenueCat to Braze. If you're using the Braze SDK, you can use the RevenueCat and Braze SDKs together to enhance the integration by ensuring the same customer identifier is being used in both systems.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| RevenueCat Account and Configured App | RevenueCat | [https://app.revenuecat.com/login][9] | You must have an active account and a configured app with RevenueCat to use their service. |
| RevenueCat SDK Integration | RevenueCat | [https://docs.revenuecat.com/docs/configuring-sdk][8] | RevenueCat must be successfully installed in your app. |
| Braze SDK Integration | Braze | For more details regarding Braze’s SDKs, please refer to our [iOS][5], [Android][6] and [Web][7] documentation. | It's strongly recommended to install the Braze SDK to provide user aliases to RevenueCat. |
| Braze Instance | Braze | Your Braze Instance can be obtained from your Braze onboarding manager. | RevenueCat requires the Braze Instance to send server-side to the correct Braze REST endpoint. |
| Braze API Key | Braze | Your API keys can be found in the Developer Console -> Settings -> REST API Keys. | RevenueCat requires the API key to send server-side to Braze. |
| Braze Test API Key | Braze | Your API keys can be found in the Developer Console -> Settings -> REST API Keys. | (optional) You can use a separate API key for test and production purchases if you'd like them sent to seperate Braze instances. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Server-to-Server Integration


### Step 1: Configure Braze Settings in RevenueCat

Navigate to your app in the RevenueCat dashboard and choose 'Braze' from the integrations menu and add your Braze instance and API key.

![braze_settings_in_revenuecat][3]

### Step 2: Configure Event Names in RevenueCat

Enter the event names that RevenueCat will send or choose the default event names by clicking **Use default event names**. The events that RevenueCat supports sending are described in the chart below.

| Event | Description |
|---|---|
| Initial Purchase | The first purchase of an auto-renewing subscription product that does not contain a free trial. |
| Trial Started | The start of an auto-renewing subscription product free trial. |
| Trial Converted | When an auto-renewing subscription product converts from a free trial to normal paid period. |
| Trial Cancelled | When a user turns off renewals for an auto-renewing subscription product during a free trial period. |
| Renewal | When an auto-renewing subscription product renews OR a user repurchases the auto-renewing subscription product after a lapse in their subscription. |
| Cancellation | When a user turns off renewals for an auto-renewing subscription product during the normal paid period. |
| Non Subscription Purchase | The purchase of any product that's not an auto-renewing subscription. |
| Expiration | When a subscription expires. |
| Billing Issue | When there has been a problem trying to charge the user. |

For events that have revenue, such as trial conversions and renewals, RevenueCat will automatically record this amount along with the event in Braze.

### Step 3: Set Braze User Identity

In the Braze SDK, you can set the User ID to match the RevenueCat App User ID. This way, events sent from the Braze SDK and events sent from RevenueCat can be synced to the same user.

Configure the Braze SDK with the same App User ID as RevenueCat or use the `.changeUser()` method on the Braze SDK.

#### (Optional) Send User Alias Object to Braze

If you are looking to send an alternative unique user identifier that is different than the RevenueCat app user ID, update users with the below data as RevenueCat subscriber attributes.

| Key | Description |
|---|---|
| `$brazeAliasName	` | The Braze `alias_name` in the [User Alias Object][2] |
| `$brazeAliasLabel		` | The Braze `alias_label` in the [User Alias Object][2] |
{: .reset-td-br-1 .reset-td-br-2}

Both attributes are required for the [User Alias Object][2] to be sent alongside your event data. These properties can be set manually, like any other [RevenueCat Subscriber Attribute][4].

{% tabs %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// [Optional] Set User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "alias_name", 
                             "$brazeAliasLabel" : "alias_label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// [Optional] Set User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"alias_name",
    @"$brazeAliasLabel": @"alias_label"
}];
```
{% endtab %}
{% tab kotlin %}
```kotlin
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(this).changeUser("my_app_user_id");

// [Optional] Set User Alias Object attributes
Purchases.sharedInstance.setAttributes(mapOf("$brazeAliasName" to "alias_name",
                                             "$brazeAliasLabel" to "alias_label"));
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(this).changeUser("my_app_user_id");

// [Optional] Set User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "alias_name");
attributes.put("$brazeAliasLabel", "alias_label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

## Customization

### Add a Sandbox API Key

If you only provide one Braze REST API Key to RevenueCat, then only production purchase events will be sent. If you also want to send sandbox events, [create another Braze REST API Key][11] and add it to your Braze settings in RevenueCat.

## Using This Integration

After configuring Braze Settings in RevenueCat, events will automatically begin flowing from RevenueCat to Braze without any other action on your part.

## Use Cases

- Trigger an onboarding campaign highlighting your premium features when a customer starts a free trial.
- Send a reminder to update billing information when a BILLING ISSUE event is recieved.
- Send a feedback survey after a customer cancels a free trial. 

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[10]: http://127.0.0.1:5006/docs/hidden/wip_partnerships/partnership_template/#customization
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
