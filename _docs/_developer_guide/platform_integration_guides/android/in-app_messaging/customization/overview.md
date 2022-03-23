---
nav_title: Overview
article_title: In-App Message Customization Overview for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 1
description: "This reference article covers in-app messaging customization options for your Android application."
channel:
  - in-app messages

---

# Customization {#in-app-message-customization}

All of Braze’s in-app message types are highly customizable across messages, images, [Font Awesome][15] icons, click-actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

## Key-value pair extras

In-app message objects may carry key-value pairs as `extras`. They are specified on the dashboard under **Settings** when creating an in-app message campaign. These can be used to send data with an in-app message for further handling by the application.

Call the following when you get an in-app message object to retrieve its extras:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

Refer to this [KDoc][44] for more information.

## Android dialogs

Braze doesn't support displaying in-app messages in [Android dialogs][85] at this time.

[15]: http://fortawesome.github.io/Font-Awesome/
[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/get-extras.html
[85]: https://developer.android.com/guide/topics/ui/dialogs.html


