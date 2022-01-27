---
nav_title: Configuration de l'exécution
article_title: Configuration d'exécution pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 4
description: "Cet article de référence couvre la façon de configurer la configuration de votre application Android."
---

# Configuration de l'exécution

La configuration de l'exécution est un moyen facultatif de configurer votre application au moment de l'exécution, à la place d'un `braze.xml`. L'utilisation de la configuration d'exécution et de la configuration `braze.xml` est toujours possible. Les valeurs d'exécution configurées auront toujours la priorité sur la même valeur dans le `braze.xml`. Si le Braze SDK peut trouver toutes les valeurs dans la configuration de l'exécution, alors le `braze.xml` n'est plus nécessaire et peut être supprimé. Voir la documentation complète [ici][1].

## Exemple d'utilisation

La configuration utilise un objet [builder][2] qui est ensuite construit et passé à [Braze.configure()][1]. L'exemple suivant utilise un sous-ensemble des options de configuration disponibles pour l'exécution, voir le [KDoc][1] pour une liste complète des options de configuration disponibles.

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
        .setHandlePushDeepLinksAutomaticaly(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

Un autre exemple peut être trouvé dans notre [Bonjour Braze application][3].

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/configure.html

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/configure.html

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/configure.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html
[3]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java
