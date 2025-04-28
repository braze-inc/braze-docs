---
nav_title: Gestion manuelle des clics
article_title: "Gestion manuelle des clics de fil d'actualité pour Android et FireOS"
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment gérer les clics de fil d'actualité manuellement dans votre application Android ou FireOS."
channel:
  - news feed
  
---

# Gestion manuelle des clics

> Cet article de référence explique comment gérer les clics de fil d'actualité manuellement dans votre application Android ou FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Vous pouvez gérer les clics de fil d'actualité manuellement en définissant un écouteur de clic de fil d'actualité personnalisé. Cela permet des cas d’usage tels que l’utilisation sélective du navigateur Web natif pour ouvrir des liens Web.

## Étape 1 : Implémenter un écouteur de clic de fil d'actualité

Créez une classe qui implémente [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java). Implémentez la méthode `onFeedCardClicked()`, qui sera appelée lorsque l’utilisateur clique sur une carte de fil d'actualité.

## Étape 2 : Demander à Braze d’utiliser votre écouteur de clic de fil d’actualité

Une fois que votre `IFeedClickActionListener` est créé, appelez `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` pour demander à `BrazeFeedManager` d’utiliser votre `IFeedClickActionListener` personnalisé.

