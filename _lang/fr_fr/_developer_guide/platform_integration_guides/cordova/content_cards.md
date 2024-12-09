---
nav_title: Cartes de contenu
article_title: Intégration des cartes de contenu
page_order: 2
---

# Intégration des cartes de contenu

> Découvrez comment intégrer les cartes de contenu au SDK Braze Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Flux de cartes

Le SDK Braze comprend un flux de cartes par défaut. Pour afficher le flux de cartes par défaut, vous pouvez utiliser la méthode `launchContentCards()`. Cette méthode gère l'ensemble des activités de suivi des analyses, de rejets et de rendu des cartes de contenu d'un utilisateur.

## Cartes de contenu

Vous pouvez utiliser ces méthodes supplémentaires pour créer un flux de cartes de contenu personnalisé dans votre application :

|Méthode | Description |
|---|---|
|`requestContentCardsRefresh()`|Envoie une requête en arrière-plan pour demander les dernières cartes de contenu au serveur SDK de Braze.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Récupère les cartes de contenu du SDK Braze Cette fonction demande les dernières cartes de contenu au serveur et renvoie la liste des cartes terminées.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Récupère les cartes de contenu du SDK Braze Cette fonction renvoie la dernière liste de cartes du cache local, qui a été actualisée lors de la dernière actualisation.|
|`logContentCardClicked(cardId)`|Enregistre un clic pour l’ID de carte de contenu donné.|
|`logContentCardImpression(cardId)`|Enregistre une impression pour l’ID de carte de contenu donné.|
|`logContentCardDismissed(cardId)`|Enregistre un rejet pour l’ID de carte de contenu donné.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Support GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}
