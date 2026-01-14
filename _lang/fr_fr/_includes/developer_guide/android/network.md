## Réseau en mode hors connexion

Le [réseau en mode hors connexion](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean) est une fonctionnalité facultative qui suspend ou reprend les demandes de réseau sortant du SDK Braze, à tout moment pendant l’exécution. Les événements ne sont pas perdus pendant l’état hors connexion. Cet article de référence explique l’intégration de ce mode.

Pour activer le réseau en mode hors connexion dans le SDK Braze, voir l’exemple suivant :

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

