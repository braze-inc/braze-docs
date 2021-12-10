---
nav_title: Cartes de contenu
article_title: Intégration des cartes de contenu pour Cordova
platform:
  - Cordova
  - iOS
  - Android
page_order: 3
channel: cartes de contenu
page_type: Référence
description: "Cet article explique comment démarrer avec les Cartes de Contenu pour Cordova."
---

# Cartes de contenu pour l'intégration de Cordova

Pour commencer avec les Cartes de Contenu, les SDK Braze incluent un flux de carte par défaut. Pour afficher le flux de cartes, vous pouvez utiliser la méthode `AppboyPlugin.launchContentCards()`.

Le flux de carte par défaut inclus avec le Braze SDK gère le suivi de toutes les données analytiques, les licenciements et le rendu pour les cartes de contenu d'un utilisateur.

## Personnalisation

Vous pouvez utiliser ces méthodes supplémentaires pour construire un flux de cartes de contenu personnalisé dans votre application :

| Méthode                                                                  | Libellé                                                                                                |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `AppboyPlugin.requestContentCardsRefresh()`                              | Demande les dernières Cartes de Contenu au serveur Braze SDK.                                          |
| `AppboyPlugin.getContentCardsFromServer(successCallback, errorCallback)` | Récupère les Cartes de Contenu du Braze SDK. Ceci retournera la dernière liste des cartes du serveur.  |
| `AppboyPlugin.getContentCardsFromCache(successCallback, errorCallback)`  | Récupère les Cartes de Contenu du Braze SDK. Ceci retournera la dernière liste des cartes de la cache. |
| `AppboyPlugin.logContentCardsDisplayed()`                                | Enregistre un flux de contenu affiché                                                                  |
| `AppboyPlugin.logContentCardClicked(cardId)`                             | Enregistre un clic sur l'ID de la carte de contenu donnée.                                             |
| `AppboyPlugin.logContentCardImpression(cardId)`                          | Enregistre une impression pour l'ID de la carte de contenu donnée.                                     |
| `AppboyPlugin.logContentCardDismissed(cardId)`                           | Enregistre un rejet pour l'ID de la carte de contenu donnée.                                           |
{: .reset-td-br-1 .reset-td-br-2}
