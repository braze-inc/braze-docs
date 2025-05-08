---
nav_title: Configuração do tempo de execução
article_title: Configuração do tempo de execução para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Este artigo de referência aborda como configurar o tempo de execução para seu app Android ou FireOS."

---

# Configuração do tempo de execução

>[A configuração em tempo de execução](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) é uma maneira opcional de configurar seu app em tempo de execução no lugar de um `braze.xml`. Este artigo de referência aborda como configurar o tempo de execução.

Ainda é possível usar tanto a configuração do tempo de execução quanto a configuração do `braze.xml`. Os valores configurados do tempo de execução sempre terão precedência sobre o mesmo valor no `braze.xml`. Se o SDK da Braze conseguir encontrar todos os valores na configuração de tempo de execução, então o `braze.xml` não será mais necessário e poderá ser removido. 

## Exemplo de uso

A configuração usa um [objeto builder](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) que é criado e passado para o [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). O exemplo a seguir usa um subconjunto das opções de configuração de tempo de execução disponíveis; consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) para obter uma lista completa de opções.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Outro exemplo pode ser encontrado em nosso [app de amostra Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).

