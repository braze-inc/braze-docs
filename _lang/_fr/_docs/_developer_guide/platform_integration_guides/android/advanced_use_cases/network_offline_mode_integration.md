---
nav_title: Mode réseau hors-ligne
article_title: Mode réseau hors connexion pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 3
description: "Cet article de référence couvre la façon d'intégrer le mode réseau hors ligne pour votre application Android."
---

# Mode réseau hors ligne

Network Offline Mode est une fonctionnalité optionnelle qui met en pause ou reprend les requêtes de réseau sortant du Braze SDK à tout moment pendant l'exécution. Les événements ne sont pas perdus pendant l'état hors ligne. Voir la documentation complète [ici][1].

## Exemple d'utilisation

Pour activer le mode réseau hors ligne dans le Braze SDK, voir l'exemple suivant :

{% tabs %}
{% tab JAVA %}

```java
format@@0 Braze.setOutboundNetworkRequestsOffline(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
format@@0 Braze.setOutboundNetworkRequestsOffline(true)
```

{% endtab %}
{% endtabs %}

[1]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#setOutboundNetworkRequestsOffline-boolean-
