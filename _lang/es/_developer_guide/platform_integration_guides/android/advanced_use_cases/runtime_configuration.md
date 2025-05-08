---
nav_title: Configuración en tiempo de ejecución
article_title: Configuración del tiempo de ejecución para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Este artículo de referencia explica cómo configurar el tiempo de ejecución de una aplicación Android o FireOS."

---

# Configuración de tiempo de ejecución

>[La configuración en tiempo de ejecución](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) es una forma opcional de configurar tu aplicación en tiempo de ejecución en lugar de `braze.xml`. Este artículo de referencia explica cómo establecer la configuración del tiempo de ejecución.

Sigue siendo posible utilizar tanto la configuración en tiempo de ejecución como la configuración de `braze.xml`. Los valores configurados en tiempo de ejecución siempre tendrán prioridad sobre el mismo valor en `braze.xml`. Si el SDK de Braze puede encontrar todos los valores en la configuración del tiempo de ejecución, entonces `braze.xml` ya no es necesario y se puede eliminar. 

## Ejemplo de uso

La configuración utiliza un [objeto constructor](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) que luego se construye y se pasa a [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). El siguiente ejemplo utiliza un subconjunto de las opciones de configuración de tiempo de ejecución disponibles; consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) para ver la lista completa de opciones.

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

Encontrarás otro ejemplo en nuestra [aplicación de ejemplo Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).

