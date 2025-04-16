# Modo off-line de rede

> [O modo offline de rede](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/outbound-network-requests-offline.html?query=var%20outboundNetworkRequestsOffline:%20Boolean) é um recurso opcional que pausa ou retoma as solicitações de rede de saída do SDK da Braze em qualquer ponto durante o tempo de execução. Os eventos não são perdidos durante o estado off-line. Este artigo de referência aborda como integrar esse modo.

## Exemplo de uso

Para ativar o modo offline de rede no SDK da Braze, consulte o exemplo a seguir:

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

