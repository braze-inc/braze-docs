{% multi_lang_include developer_guide/prerequisites/android.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Settings

There are many advanced settings available for FireOS push notifications sent through the Braze dashboard. This article will describe these features and how to use them successfully.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### Time to live (TTL) {#ttl}

The **Time to Live** (TTL) field allows you to set a custom length of time to store messages with the push messaging service. The default values for time to live are four weeks for FCM and 31 days for ADM.

### Summary text {#summary-text}

The summary text allows you to set additional text in the expanded notification view. It also serves as a caption for notifications with images.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

The summary text will display under the body of the message in the expanded view. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. 

### Custom URIs {#custom-uri}

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep link inside your app and direct users to resources that exist outside of your app. This can be specified via the [Messaging API]({{site.baseurl}}/api/endpoints/messaging) or our dashboard under **Advanced Settings** in the push composer as pictured:

![The deep linking advanced setting in the Braze push composer.]({% image_buster /assets/img_archive/deep_link.png %})

### Notification display priority

{% alert important %}
The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life whereas high priority messages are always sent immediately.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for FireOS notifications is possible via the Braze dashboard and messaging API. 

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) *and* send the individual priority from the dashboard (to target &#60;O devices).

The priority levels that you can set on Fire OS push notifications are:

| Priority | Description/Intended Use | `priority` value (for API messages) |
|----------|--------------------------|-------------------------------------|
| Max      | Urgent or time-critical messages | `2` |
| High     | Important communication, such as a new message from a friend | `1` |
| Default  | Most notifications - use if your message doesn't explicitly fall under any of the other priority types | `0` |
| Low      | Information that you want users to know about but does not require immediate action | `-1` |
| Min      | Contextual or background information. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's [Android notification](http://developer.android.com/design/patterns/notifications.html) documentation.

### Sounds {#sounds}

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (for example, `android.resource://com.mycompany.myapp/raw/mysound`). Specifying "default" in this field will play the default notification sound on the device. This can be specified via the [Messaging API]({{site.baseurl}}/api/endpoints/messaging) or the dashboard under **Settings** in the push composer.

![The sound advanced setting in the Braze push composer.]({% image_buster /assets/img_archive/sound_android.png %})

Enter the full sound resource URI (for example, `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) *and* send the individual sound from the dashboard (to target &#60;O devices).
