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

