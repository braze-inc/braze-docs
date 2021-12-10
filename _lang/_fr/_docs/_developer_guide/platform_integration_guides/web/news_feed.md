---
nav_title: Flux d'actualité
article_itle: Intégration de flux d'actualités pour le Web
platform: Web
page_order: 3
page_type: Référence
description: "Cet article explique comment interagir avec les fils de nouvelles via le Braze SDK."
channel: fil d'actualité
---

# Flux d'actualité

Le fil d'actualité est un flux de contenu entièrement personnalisable dans l'application pour vos utilisateurs. Notre ciblage et segmentation vous permettent de créer un flux de contenu qui est individuellement adapté aux intérêts de chaque utilisateur. Selon leur position dans le cycle de vie de l'utilisateur et la nature de votre application, Il peut s'agir d'un serveur de contenu embarqué, d'un centre de publicité, d'un centre d'accomplissement ou d'un centre d'information générique.

## Exemple de flux d'actualités

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="Exemple de flux d'actualités" height="600" />

## Intégration des fils d'actualité

Pour activer/désactiver l'affichage du flux d'actualités via le Braze Web SDK, appelez simplement

``` javascript
appboy.display.toggleFeed();
```

Ceci affichera les cartes de mise en cache des actualités les plus récentes (démarrage d'une mise à jour si ces cartes sont obsolètes de plus d'une minute, ou si le fil d'actualité n'a jamais été actualisé) et mettra à jour automatiquement l'affichage lorsque de nouvelles cartes sont reçues des serveurs de Braze tant qu'il est à l'écran.

Par défaut, le flux sera affiché dans une barre latérale à position fixe sur le côté droit du site (ou comme une superposition en plein écran sur les appareils mobiles, par css réactif). Si vous souhaitez remplacer ce comportement et afficher un flux d'actualités statiquement positionné dans votre propre élément parent, fournir simplement cet élément comme premier argument à afficherFeed, par exemple :

``` javascript
appboy.display.toggleFeed(document.getElementById('mon-news-feed-parent'));
```

Si vous souhaitez afficher un ensemble statique spécifique de cartes de News Feed, filtrez les cartes depuis le serveur, ou fournir votre propre sémantique, vous pouvez désactiver la mise à jour automatique et fournir vos propres cartes. Par exemple :

``` javascript
appboy.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  appboy.display.showFeed(undefined, cards);
});
appboy.requestFeedRefresh();
```

Voir les [JSDocs][2] pour une documentation complète pour `showFeed`, `destroyFeed`, et `toggleFeed`.

## Personnalisation du fil d'actualité

Les éléments de Braze UI sont fournis avec une apparence par défaut qui correspond aux compositeurs dans le tableau de bord Braze et vise à la cohérence avec d'autres plates-formes mobiles de Braze. Les styles par défaut de Braze sont définis en CSS dans le Braze SDK. En écrasant les styles sélectionnés dans votre application, il est possible de personnaliser notre flux standard avec vos propres images de fond, familles de polices, styles, tailles, animations, et plus encore. Par exemple, ce qui suit est un exemple de substitution qui fera apparaître le fil d'actualité en 800px dans toute la partie :

``` css
body .ab-feed {
  width: 800px;
}
```

## Catégories

Les instances de Braze News Feed peuvent être configurées pour recevoir uniquement des cartes d'une certaine « catégorie ». Cela permet l'intégration effective de plusieurs flux de nouvelles dans une seule application. Pour plus d'informations sur cette fonctionnalité, visitez notre [documentation][14].

Les catégories de flux d'actualité peuvent être définies en fournissant le troisième paramètre "allowedCategories" à `toggleFeed`:

``` javascript
appboy.display.toggleFeed(indéfini, indéfini, [appboy.Card.Category.NEWS]);
```

Vous pouvez également remplir un flux avec une combinaison de catégories comme dans l'exemple suivant :

``` javascript
appboy.display.toggleFeed(indéfini, indéfini, [appboy.Card.Category.ANNOUNCEMENTS, appboy.Card.Category.NEWS]);
```

## Indicateurs lus et non lus

Braze fournit un indicateur non lu/lu sur les cartes de News Feed comme illustré ci-dessous :

!\[UnreadvsRead\]\[25\]

### Désactivation des indicateurs

Afin de désactiver cette fonctionnalité, ajoutez le style suivant à votre CSS :

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

## Types de carte

Le Braze Web SDK prend en charge 3 types de cartes de flux d'actualités uniques, [ab.ClassicCard][3], [ab. anner][4], [ab.CaptionedImage][5] qui partagent un modèle de base, [ab.Card][1].

### Demander le nombre de cartes non lues

Vous pouvez demander le nombre de cartes non lues à tout moment en appelant :

``` javascript
appboy.getCachedFeed().getUnreadCardCount();
```

Ceci est souvent utilisé pour alimenter les badges indiquant combien de cartes de flux de nouvelles non lues existent. Voir les [JSDocs][17] pour plus d'informations. Notez que Braze n'actualisera pas les cartes des fils d'actualité lors du chargement de nouvelles pages (et donc cette fonction retournera 0) jusqu'à ce que vous montiez le flux ou appelez `appboy. equestFeedReRafraîchit();`

### Paires clé-valeur

Les objets `ab.Card` peuvent éventuellement transporter des paires clé-valeur sous la forme `d'extras`. Celles-ci peuvent être utilisées pour envoyer des données avec une carte pour un traitement ultérieur par l'application.  Appelez simplement `card.extras` pour accéder à ces valeurs.

Voir les JSDocs pour [ab.ClassicCard][3], [ab.Banner][4], ou [ab.CaptionedImage][5] pour plus d'informations.
[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}

[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html
[2]: https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showFeed
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ClassicCard.html
[4]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html
[4]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Banner.html
[5]: https://js.appboycdn.com/web-sdk/latest/doc/ab.CaptionedImage.html
[14]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[17]: https://js.appboycdn.com/web-sdk/latest/doc/ab.Feed.html
