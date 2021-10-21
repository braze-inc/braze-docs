---
nav_title: Network Offline Mode
article_title: Network Offline Mode for Android/FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "This reference article covers how to integrate network offline mode for your Android application."

---

# Network offline mode

Network Offline Mode is an optional feature that pauses or resumes outbound network requests from the Braze SDK at any point during runtime. Events are not lost during the offline state. See the full documentation [here][1].

## Example usage

To enable network offline mode in the Braze SDK, see the following example:

{% tabs %}
{% tab JAVA %}

```java
Braze.setOutboundNetworkRequestsOffline(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.setOutboundNetworkRequestsOffline(true)
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#setOutboundNetworkRequestsOffline-boolean-
