---
nav_title: Key-value pairs
article_title: Key-Value Pairs
page_order: 4
description: "This reference article covers key-value pairs and how to use them to send extra data payloads to user devices."
channel:
  - push
  - in-app messages
  - content cards

---

# Key-value pairs

> This page covers how to use key-value pairs to send extra data payloads to user devices. This feature is available across push, in-app, email, and Content Card messaging channels.

Use key-value pairs to add structured metadata to messages. These extra data payloads can enrich messages with additional contextual information that can influence how a message is rendered or processed.

Because key-value pairs are metadata, this data isn't necessarily visible to the recipient, but can be used by your connected systems or processes to customize message handling. 

Each pair consists of:

- **Key:** The identifier (Example: `utm_source`)
- **Value:** The associated data (Example: `newsletter`)

## Use cases

Here are some example use cases for adding metadata with key-value pairs:

1. **Tracking parameters:** Attaching UTM parameters for analytics purposes
   - Key: `utm_campaign`
   - Value: `spring_sale`
2. **Custom tags:** Adding tags for internal routing or categorization
   - Key: `priority`
   - Value: `high`
3. **Behavior triggers:** Metadata used to trigger or customize in-app behaviors
   - Key: `deep_link`
   - Value: `app://promo-page`

## Push notifications

Key-value pairs can be added to Android, iOS, and web push notifications. You might use key-value pairs to update internal metrics and app content or customize push notification properties, such as alert prioritization, localization, and sounds.

In the message composer, select the **Settings** tab, select **Add New Pair**, and specify your key-value pairs.

### iOS

Apple Push Notification service (APNs) supports setting alert preferences and sending custom data using key-value pairs. APNs makes use of the Apple-reserved ```aps``` library, which includes predetermined keys and values that govern alert properties.

##### APS library

| Key  | Value Type  | Value Description |
|-------------------|-----------------------------|----------------------------------|
| alert             | string or dictionary object | For string inputs, displays an alert with the string as the message with Close and View buttons; for non-string inputs, displays an alert or banner depending on the input's child properties |
| badge             | number                      | Governs the number that is displayed as the badge on the app icon                                                                                                                              |
| sound             | string                      | The name of the sound file to play as an alert; must be in the app's bundle or ```Library/Sounds``` folder                                                                                    |
| content-available | number                      | Input values of 1 signal to the app the availability of new information upon launch or session resumption |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Alert properties library

| Key            | Value Type               | Value Description                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | string                   | A short string that Apple Watch displays briefly as part of a notification                                                                    |
| body         | string                   | The push notification's content                                                                                                                  |
| title-loc-key  | string or null           | A key that sets the title string for the current localization from the ```Localizable.strings``` file                                          |
| title-loc-args | array of strings or null | String values that can appear in place of the title localization format specifiers in title-loc-key                                           |
| action-loc-key | array of string or null  | If present, the specified string sets the localization for the Close and View buttons                                                         |
| loc-key        | string or null           | A key that sets the notification message for the current localization from the ```Localizable.strings``` file                                  |
| loc-args       | array of strings         | String values that can appear in place of the localization format specifiers in loc-key                                                       |
| launch-image   | strings                  | The name of an image file in the app bundle you wish to be used as the launch image when users tap the action button or move the action slide |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

The Braze message composer automatically handles the creation of the following keys: **alert** and **its properties**, **content-available**, **sound**, and **category**. 

These values can be input in the **Settings** tab when building a push message. Select **Alert Options** and select an alert dictionary key for the key to be automatically populated in a new key-value entry.

![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
When Braze sends a push notification to APNs, the payload will be formatted as a JSON.

**Simple Payload**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Complex Payload**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Custom key-value pairs

In addition to the ```aps``` library payload values, you may send custom key-value pairs to a user's device. The values in these pairs are restricted to primitive types: dictionary (object), array, string, number, and boolean.

![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Use cases for custom key-value pairs include but are not limited to internal metrics keeping and setting the context for the user interface. Braze allows you to send additional key-value pairs along with a push notification to be used through your application within the [extras key]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). If you prefer to use another key, confirm that your app can handle this custom key.

{% alert warning %}
You should avoid handling a top-level key or dictionary called ab in your application.
{% endalert %}

Apple advises clients to avoid including customer information or any sensitive data as custom payload data. Furthermore, Apple recommends that any action associated with an alert message should not delete data on a device.

{% alert warning %}
If you're using the HTTP/2 provider API, any individual payload you send to APNs cannot exceed a size of 4096 bytes. The legacy binary interface, which will soon be depreciated, only supports a payload size of 2048 bytes.
{% endalert %}

###### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a developer console output of `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze allows you to send send additional data payloads in push notifications using key-value pairs.

##### Data payload

Similar to iOS push, you may send custom key-value pairs to a user's device.

Some use cases for custom key-value pairs include internal metrics keeping and setting the context for the user interface, but they may be used for whatever purpose you choose.

{% alert important %}
Your app's backend must be able to process custom key-value pairs for the data payload to function properly.
{% endalert %}

###### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a developer console output of `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### FCM messaging options

Android push notifications can be further customized with FCM message options. These include [notification priority]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [sound]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), delay, lifespan, and collapsibility. These values can be specified in the **Settings** tab when creating a push message. Refer to [Advanced push notification settings]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) for further instructions on how to set these options in the Braze message composer.

![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Silent push notifications

A silent push notification is a push notification containing no alert message or sound, used to update your app's interface or content in the background. These notifications make use of key-value pairs to trigger these background app actions. Silent push notifications also power our [uninstall tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Marketers should test that silent push notifications trigger expected behavior before sending them to their app's users. After you compose your [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) or [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) silent push notification, ensure that you only target a test user by filtering on [external user ID]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) or [email address]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Upon campaign launch, you should check that you have not received any visible push notification on your test device.

{% alert note %}
The iOS operating system may [gate notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) for some features (uninstall tracking, geofences, and Push Stories). Note that if you are experiencing difficulties with these features, the iOS's silent notifications gate might be the cause.
{% endalert %}

## In-app messages

To add a key-value pair to an in-app message, select the **Settings** tab in the message composer, select **Add New Pair**, and specify your key-value pairs.

![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a developer console output of `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Emails

Both SparkPost and SendGrid support key-value pairs in emails. If you use SendGrid, key-value pairs will be sent as [unique arguments](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid allows you to attach an unlimited number of key-value pairs up to 10,000 bytes of data. These key-value pairs can be seen in posts from the SendGrid [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/).

{% alert note %}
Bounced emails will not deliver key-value pairs to SparkPost or SendGrid.
{% endalert %}

![Sending Info tab of the email message composer in Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

To add a key-value pair to a Content Card, go to the **Settings** tab in the Braze message composer and select **Add New Pair**.

![Add key-value pair to Content Card]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


