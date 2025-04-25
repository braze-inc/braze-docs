# Netzwerk-Offline-Modus

> Der [Netzwerk-Offline-Modus](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean) ist ein optionales Feature, mit dem ausgehende Netzwerkanfragen des Braze SDK während der Laufzeit angehalten oder fortgesetzt werden können. Im Offline-Status gehen keine Events verloren. Dieser Referenzartikel beschreibt, wie Sie diesen Modus integrieren können.

## Verwendungsbeispiel

Um den Netzwerk-Offline-Modus im Braze SDK zu aktivieren, sehen Sie sich das folgende Beispiel an:

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

