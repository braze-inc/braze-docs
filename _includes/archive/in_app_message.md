### Slideup In-App Messages

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen.  They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![Slideup Example][in_app_message_9]

### Modal In-App Messages

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

![Modal Example][in_app_message_10]

### Full In-App Messages

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} in-app messages are useful for maximizing the content and impact of your user communication.  The upper half of a `full` in-app message contains an image and the lower half displays text as well as up to two click action and analytics enabled buttons.

![Full Example][in_app_message_11]

### HTML Full In-App Messages

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality.

 {% if include.platform == "iOS" %}
The following example shows a paginated HTML Full in-app message:

![HTML5 Example][in_app_message_23]

 {% elsif include.platform == "Android" %}The following example shows a survey HTML Full in-app message created by Soundcloud.

![HTML5 Example][in_app_message_12]
{% endif %}

Full in-app message content is displayed in a WKWebView and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. **Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.**

## In-App Message Delivery

### In-App Messages (Triggered)

The following documentation refers to Braze's `In-App Messaging` product, aka "triggered in-app messages," which are branded as highlighted below in the "Create Campaign" drop-down:

![In-App Messaging Composer][in_app_message_13]

You may also refer to the documentation for our deprecated [`Original In-App Messaging`][in_app_message_14] product.

#### Trigger Types

Our in-app message product allows you to trigger in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

-**Note:** Triggered in-app messages only work with custom events logged through the SDK and not through the REST APIs.  If you're working with Android, please check out how to log custom events [here][in_app_message_24]. If you're working with iOS, check out how to log custom events [here][in_app_message_25].

#### Delivery Semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. For more information about the SDK's session start semantics, see our [session lifecycle documentation]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Upon delivery, the SDK will pre-fetch assets so that they are available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

For in-app messages that display immediately on deliver (*i.e.*, session start, push click) there can be some latency due to assets not being prefetched.

#### Minimum Time Interval Between Triggers

By default, we rate limit in-app messages to once every 30 seconds to ensure a quality user experience.

{% if include.platform == "iOS" %}You can override this value via the `ABKMinimumTriggerTimeIntervalKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set the `ABKMinimumTriggerTimeIntervalKey` to the integer value you want as your minimum time in seconds between in-app messages:

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

An example of overriding the default trigger interval can be found in our sample application's [`AppDelegate.m`][in_app_message_16] file.

{% elsif include.platform == "Android" %}
To override this value, set `com_appboy_trigger_action_minimum_time_interval_seconds` in your `appboy.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageSlideup.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageModal.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageFull.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/InAppMessageHtmlFull.html
[in_app_message_9]: {% image_buster /assets/img_archive/In-App_Slideup.png %}
[in_app_message_10]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[in_app_message_11]: {% image_buster /assets/img_archive/In-App_Full.png %}
[in_app_message_12]: {% image_buster /assets/img_archive/HTML5.gif %}
[in_app_message_13]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[in_app_message_14]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
[in_app_message_16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/AppDelegate.m
[in_app_message_19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/{{ include.platform }}/in-app_messaging/#in-app-messages-triggered
[in_app_message_23]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[in_app_message_24]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[in_app_message_25]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events

