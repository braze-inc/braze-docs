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

Lorsque les cartes sont réactualisées, une fonction de rappel peut être enregistrée. 

{% alert important %}
Les cartes de contenu ne sont réactualisées au démarrage de la session que si `subscribeToContentCardsUpdates()` est appelé avant `openSession()`. Vous pouvez toujours réactualiser les cartes de contenu manuellement à l’aide de `requestContentCardsRefresh()`.
{% endalert %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates(function(updates){
  const cards = updates.cards;
  // faire quelque chose avec la dernière instance de `cards`
});

braze.openSession();
```

## Enregistrer les événements

Enregistrer les événements d’impression lorsque les cartes sont consultées par les utilisateurs :

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardImpressions([card1, card2, card3], true);
```

Enregistrer les événements de clic sur la carte lorsque les utilisateurs interagissent avec une carte :

```javascript
import * as braze from "@braze/web-sdk";

braze.logCardClick(card, true);
```

## Gestion des modifications des utilisateurs

Gestion `changeUser()` et récupération des dernières cartes de contenu pour le nouvel utilisateur.

```javascript
import * as braze from "@braze/web-sdk";


braze.initialize("YOUR_SDK_API_KEY", {
  baseUrl: "YOUR_SDK_URL",
  enableLogging: true,
  doNotLoadFontAwesome: true,
});

braze.subscribeToContentCardsUpdates(({ cards }) => {
  console.log("Braze - subscribeToContentCardsUpdates: ", cards);
  // Ceci sera invoqué à chaque fois que le fil est réactualisé avec succès après une requête de requestContentCardsRefresh
  // Ici vous pouvez rendre les cartes à l’interface utilisateur et journaliser les impressions.
});

braze.changeUser("test-user-1");

braze.openSession();


braze.requestContentCardsRefresh(
 () => {console.log("Feed Refresh Request successfully submitted");},
 () => {console.log("Feed Refresh Request Failed");}
);


//Attendez avant d’exécuter le bloc suivant après la journalisation des cartes de contenu dans la console après la réactualisation des cartes de contenu ci-dessus
braze.changeUser("test-user-2");
braze.requestContentCardsRefresh(
 () => {console.log("Feed Refresh Request successfully submitted");},
 () => {console.log("Feed Refresh Request Failed");}
);
```
