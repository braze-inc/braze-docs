---
nav_title: Key-Value Pairs
article_title: Key-Value Pairs
page_order: 4
description: "This reference article covers key-value pairs and how to use them to send extra data payloads to user devices."
channel:
  - push
  - in-app messages
  - content cards

---

# Key-value pairs

Braze enables you to send extra data payloads to user devices via key-value pairs. This feature is available across push, in-app, and Content Card messaging channels. Extra data payloads can help you update internal metrics and app content as well as customize push notification properties, such as alert prioritization, localization, and sounds.

## Push notifications

Key-value pairs can also be added to Android, iOS, and web push notifications. In the message composer, select the **Settings** tab, click **Add New Pair**, and specify your key-value pairs.

### iOS

Apple Push Notification service (APNs) supports setting alert preferences and sending custom data using key-value pairs. APNs makes use of the Apple-reserved ```aps``` library, which includes predetermined keys and values that govern alert properties.

##### APS library

| Key  | Value Type  | Value Description |
|-------------------|-----------------------------|----------------------------------|
| alert             | string or dictionary object | For string inputs, displays an alert with the string as the message with Close and View buttons; for non-string inputs, displays an alert or banner depending on the input's child properties |
| badge             | number                      | Governs the number that is displayed as the badge on the app icon                                                                                                                              |
| sound             | string                      | The name of the sound file to play as an alert; must be in the app's bundle or ```Library/Sounds``` folder                                                                                    |
| content-available | number                      | Input values of 1 signal to the app the availability of new information upon launch or session resumption |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze's message composer automatically handles the creation of the following keys: **alert** and **its properties**, **content-available**, **sound**, and **category**. 

These values can be input in the **Settings** tab when building a push message. Select **Alert Options** and select an alert dictionary key for the key to be automatically populated in a new key-value entry.

![][16]
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

In addition to the ```aps``` library payload values, you may send custom key-value pairs to a user's device. The values in these pairs are restricted to primitive types: dictionary (object), array, string, number, and Boolean.

![][17]

Use-cases for custom key-value pairs include but are not limited to internal metrics keeping and setting the context for the user interface. Braze allows you to send additional key-value pairs along with a push notification to be used however you so via your application within the [extras key][1]. If you prefer to use another key, ensure that your app can handle this custom key.

{% alert warning %}
You should avoid handling a top-level key or dictionary called ab in your application.
{% endalert %}

Apple advises clients to avoid including customer information or any sensitive data as custom payload data. Furthermore, Apple recommends that any action associated with an alert message should not delete data on a device.

{% alert warning %}
If you are using the HTTP/2 provider API, any individual payload you send to APNs cannot exceed a size of 4096 bytes. The legacy binary interface, which will soon be depreciated, only supports a payload size of 2048 bytes.
{% endalert %}

###### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a dev console output of `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze allows you to send send additional data payloads in push notifications using key-value pairs.

##### Data payload

Similar to iOS push, you may send custom key-value pairs to a user's device.

Some use cases for custom key-value pairs include internal metrics keeping and setting the context for the user interface, but they may be used for whatever purpose you choose.

{% alert important %}
Your app's backend must be able to process custom key-value pairs for the data payload to function properly.
{% endalert %}

###### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a dev console output of `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### FCM messaging options

Android push notifications can be further customized with FCM message options. These include [notification priority][8], [sound][10], delay, lifespan, and collapsibility. These values can be specified in the **Settings** tab when creating a push message. Refer to [Advanced push notification settings][7] for further instructions on how to set these options in the Braze message composer.

![][18]

### Silent push notifications

A silent push notification is a push notification containing no alert message or sound, used to update your app's interface or content in the background. These notifications make use of key-value pairs to trigger these background app actions. Silent push notifications also power Braze's [uninstall tracking][4].

Marketers should test that silent push notifications trigger expected behavior before sending them to their app's users. Once you compose your [iOS][2] or [Android][13] silent push notification, ensure that you only target a test user by filtering on [external user ID][14] or [email address][15].

Upon campaign launch, you should check that you have not received any visible push notification on your test device.

{% alert note %}
The iOS operating system may [gate notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) for some features (uninstall tracking, geofences, and Push Stories). Note that if you are experiencing difficulties with these features, the iOS's silent notifications gate might be the cause.
{% endalert %}

## In-app messages

To add a key-value pair to an in-app message, select the **Settings** tab in the message composer, click **Add New Pair**, and specify your key-value pairs.

![][21]

#### API-triggered campaigns

Braze allows you to send custom-defined string key-value pairs, known as `extras`. To access your extras in API-triggered and scheduled API-triggered campaigns, in the dashboard set a key as "example_key", and a value as {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. This will result in a dev console output of `"extras": { "test": { "foo": 1, "bar": 1 }`.

## Emails

For Braze customers that use SendGrid, key-value pairs will be sent as [unique arguments][11]. SendGrid allows you to attach an unlimited number of key-value pairs up to 10,000 bytes of data. These key-value pairs can be seen in posts from the SendGrid [Event Webhook][12]. 

{% alert note %}
Note that bounced emails will not deliver key-value pairs to SendGrid.
{% endalert %}

![Sending Info tab of the email message composer in Braze.][22]

## Content Cards

To add a key-value pair to a Content Card, go to the **Settings** tab in the Braze message composer and click **Add New Pair**.

![Add key-value pair to Content Card][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/advanced_settings/#sounds
[11]: https://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}
