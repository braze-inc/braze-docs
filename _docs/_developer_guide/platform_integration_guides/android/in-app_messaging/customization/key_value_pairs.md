---
nav_title: Key-Value Pairs
article_title: In-App Message Key-Value Pairs for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "This reference article covers in-app messaging key-value pairs for your Android or FireOS application."
channel:
  - in-app messages

---

# Key-value pair extras

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

[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/get-extras.html
