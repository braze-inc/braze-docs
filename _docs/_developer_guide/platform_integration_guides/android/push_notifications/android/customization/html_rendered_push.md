---
nav_title: HTML Push Notifications
article_title: HTML Push Notifications for Android
platform: Android
page_order: 6
description: "This article covers hwo to implement HTML push notifications in your Android application."
channel:
  - push

---

# HTML push notifications

In Braze SDK version 3.1.1, HTML can be sent to a device to render multicolor text in push notifications.

![An Android push message "Multicolor Push test message" where the letters are different colors, italisized and given a background color.][1]{: style="max-width:40%;"}

This example is rendered with the following HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

> Android OS limits what HTML elements/tags are valid in push notifications. For example, `marquee` is not allowed.

## Implementation

To render multicolor text in push notification either:

Add the following in your `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**OR** 

Add the following in your [`BrazeConfig`][2]:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/multicolor_android_push.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
