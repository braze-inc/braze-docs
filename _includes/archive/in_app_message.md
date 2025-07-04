### Slideup in-app messages

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} in-app messages are so-named because they "slide up" or "slide down" from the top or bottom of the screen.  They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![Slideup Example]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### Modal in-app messages

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

![Modal Example]({% image_buster /assets/img_archive/In-App_Modal.png %})

### Full in-app messages

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} in-app messages are useful for maximizing the content and impact of your user communication.  The upper half of a `full` in-app message contains an image and the lower half displays text as well as up to two click action and analytics enabled buttons.

![Full Example]({% image_buster /assets/img_archive/In-App_Full.png %})

### HTML full in-app messages

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} in-app messages are useful for creating fully customized user content. User-defined HTML Full in-app message content is displayed in a {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality.

 {% if include.platform == "iOS" %}
The following example shows a paginated HTML Full in-app message:

![HTML5 Example]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}The following example shows a survey HTML Full in-app message created by SoundCloud.

![HTML5 Example]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

Full in-app message content is displayed in a WKWebView and may optionally contain other rich content, such as images and fonts, allowing for full control over message appearance and functionality. **Please note that we currently do not support display of custom HTML in-app messages in an iFrame on the iOS and Android platforms.**

## In-app message delivery

### In-app messages (triggered)

The following documentation refers to the Braze `In-App Messaging` product, also known as "triggered in-app messages," which are branded as highlighted below in the "Create Campaign" dropdown:

![In-App Messaging Composer]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

You may also refer to the documentation for our deprecated [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages) product.

#### Trigger types

Our in-app message product allows you to trigger in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

{% alert note %}
Triggered in-app messages only work with custom events logged through the Braze SDK. In-app messages can't be triggered through the API or by API events (such as purchase events). If you're working with Android, check out how to [log custom events on Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). If you're working with iOS, check out how to [log custom events on iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

#### Delivery semantics

All in-app messages that a user is eligible for are delivered to the user's device on session start. For more information about the SDK's session start semantics, see our [session lifecycle documentation]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Upon delivery, the SDK will pre-fetch assets so that they are available immediately at trigger time, minimizing display latency.

When a trigger event has more than one eligible in-app message associated with it, only the in-app message with the highest priority will be delivered.

For in-app messages that display immediately on deliver (such as session start, push click) there can be some latency due to assets not being prefetched.

#### Minimum time interval between triggers

By default, we rate limit in-app messages to once every 30 seconds for a quality user experience.

{% if include.platform == "iOS" %}You can override this value via the `ABKMinimumTriggerTimeIntervalKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set the `ABKMinimumTriggerTimeIntervalKey` to the integer value you want as your minimum time in seconds between in-app messages:

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
To override this value, set `com_appboy_trigger_action_minimum_time_interval_seconds` in your `braze.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

