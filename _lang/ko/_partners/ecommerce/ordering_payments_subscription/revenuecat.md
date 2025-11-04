---
nav_title: RevenueCat
article_title: RevenueCat
description: "The RevenueCat and Braze integration allows you to automatically sync your customer's purchase and subscription lifecycle events across platforms. This allows you to build campaigns that react to the subscription lifecycle stage of your customers, such as engaging with customers that opted out during their free trial or sending reminders to customers with billing issues."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) is the single source of truth for your subscription status across iOS, Android, and web. Whether you are building a new app or already have millions of subscribers, you can use RevenueCat to build cross-platform in-app purchases, manage your products and subscribers, and analyze your data - no server code required.

_This integration is maintained by RevenueCat._

## About the integration

The RevenueCat and Braze integration allows you to automatically sync your customer's purchase and subscription lifecycle events across platforms. This allows you to build campaigns that react to the subscription lifecycle stage of your customers, such as engaging with customers that opted out during their free trial or sending reminders to customers with billing issues.

## Prerequisites

At a minimum, you will need to enable the integration from the RevenueCat dashboard to connect RevenueCat to Braze. If you're using the Braze SDK, you can use the RevenueCat and Braze SDKs together to enhance the integration by ensuring the same customer identifier is being used in both systems.

| Requirement | Description |
|---|---|
| RevenueCat account and app | A [RevenueCat account](https://app.revenuecat.com/login) is required to take advantage of this partnership. You must also have a configured RevenueCat app. |
| RevenueCat SDK | In addition to the required Braze SDK, we recommend installing the [RevenueCat SDK](https://docs.revenuecat.com/docs/configuring-sdk) to provide user aliases to RevenueCat. |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat requires the Braze instance to send server-side to the correct Braze REST endpoint. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze test REST API key (optional) | A test API key can be used for test and production purchases if you'd like these requests sent to separate Braze instances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use Cases 

- Trigger an onboarding campaign highlighting your premium features when a customer starts a free trial.
- Send a reminder to update billing information when a "Billing Issue" event is received.
- Send a feedback survey after a customer cancels a free trial. 

## Integration

### Step 1: Set Braze user identity

In the Braze SDK, you can set the Braze user ID to match the RevenueCat app user ID, ensuring events sent from the Braze and RevenueCat can be synced to the same user.

Configure the Braze SDK with the same app user ID as RevenueCat or use the Braze SDK `.changeUser()` method.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
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

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Send user alias object to Braze (optional) 

If you want to send an alternative unique user identifier different from the RevenueCat app user ID, update users with the following data as RevenueCat subscriber attributes.

| Key | Description |
|---|---|
| `$brazeAliasName` | The Braze `alias_name` in the [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | The Braze `alias_label` in the [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Both attributes are required for the [user alias object]({{site.baseurl}}/api/objects_filters/user_alias_object/) to be sent alongside your event data. These properties can be set manually, like any other [RevenueCat subscriber attribute](https://docs.revenuecat.com/docs/subscriber-attributes). Example code snippets are shown in step one.

### Step 2: Send RevenueCat events to Braze

After you've set up the RevenueCat purchases SDK and Braze SDK to have the same user identity, you can turn on the integration and configure the event names from the RevenueCat dashboard.

1. Navigate to your project in the RevenueCat dashboard and find the **Integrations** card in the left menu. Select **\+ New**.
2. Next, select **Braze** from the available integration and add your Braze instance and Braze REST API key. 
3. Enter the event names that RevenueCat will send or choose the default event names. More details on available events can be found in [step 3](#configure-event-names).
4. Select whether you want RevenueCat to report proceeds (after app store cut) or revenue (gross sales).

![Braze settings in RevenueCat with fields for Braze instance, API key identifier, and sandbox identifier.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Step 3: Configure event names {#configure-event-names}

Enter the event names that RevenueCat will send or select from the default event names by selecting **Use Default Event Names**. The events that RevenueCat supports sending are described in the following chart.

| Event | Description |
|---|---|
| Initial Purchase | The first purchase of an auto-renewing subscription product that does not contain a free trial. |
| Trial Started | The start of an auto-renewing subscription product free trial. |
| Trial Converted | When an auto-renewing subscription product converts from a free trial to a normal paid period. |
| Trial Canceled | When a user turns off renewals for an auto-renewing subscription product during a free trial period. |
| Renewal | When an auto-renewing subscription product renews, or a user repurchases the auto-renewing subscription product after a lapse in their subscription. |
| Cancellation | When a user turns off renewals for an auto-renewing subscription product during the normal paid period. |
| Non Subscription Purchase | The purchase of any product that's not an auto-renewing subscription. |
| Expiration | When a subscription expires. |
| Billing Issue | When there has been a problem trying to charge the user. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For events that include revenue, RevenueCat will automatically record this amount along with the event in Braze, such as trial conversions and renewals.

## Using this integration

After configuring Braze settings in RevenueCat, events will automatically begin flowing from RevenueCat to Braze without any other action on your part.

## Customization

### Add a sandbox API key for Testing

If you only provide one Braze REST API key to RevenueCat, only production events will be sent. If you also want to send sandbox testing events, [create another Braze REST API key]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) and add it to your Braze settings in RevenueCat.


