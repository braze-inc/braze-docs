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

Vous pouvez gérer les clics de fil d'actualité manuellement en définissant un écouteur de clic de fil d'actualité personnalisé. Cela permet des cas d’usage tels que l’utilisation sélective du navigateur Web natif pour ouvrir des liens Web.

## Étape 1 : Implémenter un écouteur de clic de fil d'actualité

Créez une classe qui implémente [`IFeedClickActionListener`][37]. Implémentez la méthode `onFeedCardClicked()`, qui sera appelée lorsque l’utilisateur clique sur une carte de fil d'actualité.

## Étape 2 : Demander à Braze d’utiliser votre écouteur de clic de fil d’actualité

Une fois que votre `IFeedClickActionListener` est créé, appelez `AppboyFeedManager.getInstance().setFeedCardClickActionListener()` pour demander à `AppboyFeedManager` d’utiliser votre `IFeedClickActionListener` personnalisé.

[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
