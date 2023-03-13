---
nav_title: Configuration du temps d’exécution
article_title: Configuration du temps d’exécution pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Cet article de référence explique comment configurer le temps d’exécution pour votre application Android ou FireOS."

---

# Configuration du temps d’exécution

La [configuration du temps d’exécution][1] est un moyen facultatif de configurer votre application à la place d’un `braze.xml`. L’utilisation de la configuration du temps d’exécution et de la configuration `braze.xml` en même temps est toujours possible. Les valeurs configurées du temps d’exécution ont toujours préséance sur la même valeur dans le `braze.xml`. Si le SDK Braze peut trouver toutes les valeurs dans la configuration du temps d’exécution, alors `braze.xml` n’est plus nécessaire et peut être retiré. 

## Exemple d’utilisation

La configuration utilise un [objet de segmentation][2] qui est ensuite construit et transmis à [`Braze.configure()`][1]. L’exemple suivant utilise un sous-ensemble des options de configuration du temps d’exécution disponibles. Consultez notre [KDoc][1] pour une liste complète des options.

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

Un autre exemple est disponible dans notre [exemple d’application Hello Braze][3].

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html
[3]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java
