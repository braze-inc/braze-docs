---
nav_title: Personnalisation
article_title: Personnalisation de la carte de contenu pour le Web
page_order: 1
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article couvre la façon de personnaliser le style des Cartes de Contenu par défaut dans le Braze SDK."
---

# Personnalisation de la carte de contenu

## Modèles de données de carte de contenu {#data-models}

Le Braze Web SDK prend en charge plusieurs types de cartes de contenu uniques, [ab.ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/ab.ClassicCard.html), [ab. anner](https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html), [ab.CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/ab.CaptionedImage.html) qui partagent un modèle de base, [ab.Card](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html).

## Personnalisation de l'interface par défaut

Les éléments de Braze UI sont fournis avec une apparence par défaut qui correspond aux compositeurs dans le tableau de bord Braze et vise à la cohérence avec d'autres plates-formes mobiles de Braze. Les styles par défaut de Braze sont définis en CSS dans le Braze SDK.

En écrasant les styles sélectionnés dans votre application, il est possible de personnaliser notre flux standard avec vos propres images de fond, familles de polices, styles, tailles, animations, et plus encore. Par exemple, ce qui suit est un exemple de substitution qui fera apparaître des cartes de contenu de 800px de largeur :

``` css
body .ab-feed {
  width: 800px;
}
```

## Créer une interface utilisateur personnalisée

### Rafraîchissement du flux

Pour actualiser et synchroniser le flux d'un utilisateur avec les serveurs Braze, utilisez la méthode [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#requestcontentcardsrefresh).

```javascript
importer le braze de "@braze/web-sdk"

function refresh(){
  braze.requestContentCardsRefresh();    
}
```

### Écoute des mises à jour de la carte

Lorsque les cartes sont actualisées, une fonction de rappel peut être abonnée à :

```javascript
importez le braze de "@braze/web-sdk"

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // faites quelque chose avec la dernière instance de `cartes`
});
```

### Événements d'analyse de la journalisation

Journaliser les événements d’impression lorsque les cartes sont vues par les utilisateurs.

```javascript
importer le braze de "@braze/web-sdk"

braze.logCardImpressions(cards, vrai);
```

Log card cliquez sur les événements lorsque les utilisateurs interagissent avec une carte.

```javascript
importer le braze de "@braze/web-sdk"

braze.logCardClick(card, vrai);
```