---
nav_title: Network Offline Mode
article_title: Network Offline Mode for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "This reference article covers how to integrate network offline mode for your Android or FireOS application."

---

# Network offline mode

[Network offline mode][1] is an optional feature that pauses or resumes outbound network requests from the Braze SDK at any point during runtime. Events are not lost during the offline state.

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

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/set-outbound-network-requests-offline.html
