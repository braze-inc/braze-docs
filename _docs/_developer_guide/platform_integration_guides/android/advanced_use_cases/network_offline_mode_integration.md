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

> [Network offline mode](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean) is an optional feature that pauses or resumes outbound network requests from the Braze SDK at any point during runtime. Events are not lost during the offline state. This reference article covers how to integrate this mode.

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

