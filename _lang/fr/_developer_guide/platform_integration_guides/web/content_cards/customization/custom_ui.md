---
nav_title: IU personnalisée
article_title: IU de carte de contenu personnalisée pour le Web
page_order: 0
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article couvre les composants de création d’une IU personnalisée pour votre application Web."

---

# Créer une IU personnalisée

## Rafraîchir le flux

Pour actualiser et synchroniser le flux d’un utilisateur avec les serveurs Braze, utilisez la méthode [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) :

```javascript
import * as braze from "@braze/web-sdk";

function refresh(){
  braze.requestContentCardsRefresh();    
}
```
## Écouter les mises à jour de la carte

Lorsque les cartes sont rafraîchies, une fonction de rappel peut être enregistrée pour :

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // do something with the latest instance of `cards`
});
```

## Enregistrer les événements

Enregistrer les événements d’impression lorsque les cartes sont consultées par les utilisateurs :

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardImpressions(cards, true);
```

Enregistrer les événements de clic sur la carte lorsque les utilisateurs interagissent avec une carte :

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardClick(card, true);
```

