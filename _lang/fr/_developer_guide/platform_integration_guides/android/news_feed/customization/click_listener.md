---
nav_title: Gestion manuelle des clics
article_title: Gestion manuelle des clics de fil d'actualité pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment gérer les clics de fil d'actualité manuellement dans votre application Android ou FireOS."
channel:
  - fil d’actualité
  
---

# Gestion manuelle des clics

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Vous pouvez gérer les clics de fil d'actualité manuellement en définissant un écouteur de clic de fil d'actualité personnalisé. Cela permet des cas d’usage tels que l’utilisation sélective du navigateur Web natif pour ouvrir des liens Web.

## Étape 1 : Implémenter un écouteur de clic de fil d'actualité

Créez une classe qui implémente [`IFeedClickActionListener`][37]. Implémentez la méthode `onFeedCardClicked()`, qui sera appelée lorsque l’utilisateur clique sur une carte de fil d'actualité.

## Étape 2 : Demander à Braze d’utiliser votre écouteur de clic de fil d’actualité

Une fois que votre `IFeedClickActionListener` est créé, appelez `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` pour demander à `BrazeFeedManager` d’utiliser votre `IFeedClickActionListener` personnalisé.

[37]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java
