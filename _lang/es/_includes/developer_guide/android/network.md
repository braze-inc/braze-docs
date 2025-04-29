## Modo sin conexión a la red

[El modo fuera de línea de red](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean) es una característica opcional que pausa o reanuda las solicitudes de red salientes del SDK de Braze en cualquier momento del tiempo de ejecución. Los eventos no se pierden durante el estado desconectado. Este artículo de referencia explica cómo integrar este modo.

Para habilitar el modo sin conexión a la red en el SDK de Braze, consulta el siguiente ejemplo:

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

