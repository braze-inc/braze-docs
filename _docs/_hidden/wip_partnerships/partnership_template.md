---
nav_title: Your Partner Page
page_order: 1

description: "RevenueCat can automatically send subscription revenue events to Braze. This can be helpful in understanding what stage a customer is in to react accordingly. With accurate and up-to-date subscription data in Braze, you'll be set to turbocharge your campaigns."
alias: /partners/revenuecat/

page_type: partner
hidden: true
---

# RevenueCat

> RevenueCat is a powerful, reliable, and free to use in-app purchase server with cross-platform support that allows you to keep track of all of your app transactions in one place.

RevenueCat can automatically send subscription events to Braze via a server-to-server integration. This can be helpful in understanding what stage a customer is in to react accordingly. For example, you might want to:

- Send an onboarding campaign to a user in a free trial
- Allow customer support grant a promotional subscription to a loyal user that experienced issues
- Send campaigns to users that cancelled free trials

## Requirements

At a minimum, you will need to set up the server-to-server integration in RevenueCat in order to connect RevenueCat to Braze. If you're using the Braze SDK, you can use the RevenueCat and Braze SDKs together to enhance the integration.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| RevenueCat Account and Configured App | RevenueCat | [https://app.revenuecat.com/login][9] | You must have an active account and a configured app with RevenueCat to use their service. |
| RevenueCat SDK Integration | RevenueCat | [https://docs.revenuecat.com/docs/configuring-sdk][8] | RevenueCat must be successfully installed in your app. |
| Braze SDK Integration | Braze | For more details regarding Braze’s SDKs, please refer to our [iOS][5], [Android][6] and [Web][7] documentation. | It's strongly recommended to install the Braze SDK to provide user aliases to RevenueCat. |
| Braze API Key | Braze | Your API key can be found in the Developer Console -> Settings -> REST API Keys. | RevenueCat requires the API key to send server-side to Braze. |
| Braze Instance | Braze | Your Braze Instance can be obtained from your Braze onboarding manager. | RevenueCat requires the Braze Instance to send server-side to the correct Braze REST endpoint. |
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

For events that have revenue, such as trial conversions and renewals, RevenueCat will automatically record this amount along with the event in Braze.

### Step 3: Set Braze User Identity

In the Braze SDK, you can set the User ID to match the RevenueCat App User ID. This way, events sent from the Braze SDK and events sent from RevenueCat can be synced to the same user.

Configure the Braze SDK with the same App User ID as RevenueCat or use the `.changeUser()` method on the Braze SDK.

Optionally, you can also [set RevenueCat Subscriber Attributes][10] for the name and label of the user which will allow RevenueCat to send a User Alias Object to Braze.

{% tabs %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// [Optional] Set User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
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
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
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
Purchases.sharedInstance.setAttributes(mapOf("$brazeAliasName" to "name",
                                             "$brazeAliasLabel" to "label"));
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
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

## Customization

### Send User Alias Object to Braze

If you are looking to send an alternative unique user identifier that is different than the RevenueCat app user ID, update users with the below data as RevenueCat subscriber attributes.

| Key | Description |
|---|---|
| `$brazeAliasName	` | The Braze `alias_name` in the [User Alias Object][2] |
| `$brazeAliasLabel		` | The Braze `alias_label` in the [User Alias Object][2] |
{: .reset-td-br-1 .reset-td-br-2}

Both attributes are required for the [User Alias Object][2] to be sent alongside your event data. These properties can be set manually, like any other [RevenueCat Subscriber Attribute][4].

### Add a Sandbox API Key

If you only provide one Braze REST API Key to RevenueCat, then only production purchase events will be sent. If you also want to send sandbox events, [create another Braze REST API Key][11] and add it to your Braze settings in RevenueCat.

## Using This Integration

After configuring Braze Settings in RevenueCat, events will automatically begin flowing from RevenueCat to Braze without any other action on your part.

## Use Cases

This can be a critical part of your documentation. Though this is optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly a way to visualize the capabilities of the integration.

**TBD**

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: #customization
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[10]: http://127.0.0.1:5006/docs/hidden/wip_partnerships/partnership_template/#customization
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
