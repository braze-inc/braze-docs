---
nav_title: Intégration
article_title: "Intégration de fil d'actualité pour le Web"
platform: Web
page_order: 0
page_type: reference
description: "Cet article couvre le type de carte de fil d'actualité et comment intégrer le fil d'actualité dans votre application Web via le SDK Braze."
channel: news feed

---

# Intégration du fil d’actualité

> Cet article explique comment paramétrer un fil d’actualité pour le SDK Web de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Le fil d’actualités est un fil de contenu in-app entièrement personnalisable pour vos utilisateurs. Notre ciblage et notre segmentation vous permettent de créer un fil de contenu individuel, adapté aux intérêts de chaque utilisateur. Selon leur position dans le cycle de vie de l’utilisateur et la nature de votre application, il peut s’agir d’un serveur de contenu d’onboarding, d’un centre de publicité, de réalisation ou d’actualités génériques.

## Exemple de fil d'actualité

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="Un exemple de fil d&apos;actualité affichant plusieurs notifications telles que des demandes de suivi, des avis de mise à jour, des publicités, etc." height="600" />

## Intégration

Pour basculer l’affichage du fil d'actualité via le SDK Braze pour le Web, il suffit d’appeler :

``` javascript
braze.toggleFeed();
```

Ceci affichera les cartes de fil d'actualité mises en cache les plus récentes (en lançant un rafraîchissement si ces cartes ont plus d’une minute ou si le fil d'actualité n’a jamais été actualisé) et mettra automatiquement à jour l’affichage lorsque de nouvelles cartes sont reçues depuis les serveurs Braze tant qu’elles sont à l’écran.

Par défaut, le fil s’affichera dans une barre latérale à position fixe sur le côté droit du site Internet (ou en superposition en plein écran sur les appareils mobiles à l’aide d’un CSS réactif). Si vous souhaitez écraser ce comportement et afficher un fil d'actualité positionné de manière statique à l’intérieur de votre propre élément parent, fournissez l’élément suivant comme premier argument pour `showFeed` :

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

Si vous souhaitez afficher un jeu statique spécifique de cartes de fil d'actualité, filtrer les cartes du serveur ou fournir vos propres sémantiques de rafraîchissement, vous pouvez désactiver la mise à jour automatique et fournir vos propres cartes :

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

Voir les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed) pour une documentation complète sur `showFeed`, `destroyFeed` et `toggleFeed`.

## Types de cartes

Le Braze Web SDK prend en charge 3 types uniques de cartes de fil d'actualité, [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), qui partagent un modèle de base, [Card.](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)

### Demande de décompte de cartes non lues

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Cela est souvent utilisé pour alimenter les badges indiquant combien de cartes de fil d’actualité n’ont pas été lues. Consultez la [documentation de référence JS](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) pour plus d'informations. Notez que Braze n’actualisera pas les cartes de fil d’actualité sur les pages nouvellement chargées (cette fonction reviendra à 0) jusqu’à ce que vous affichiez le fil ou appelez `braze.requestFeedRefresh();`

### Paires clé-valeur

Les objets `Card` peuvent éventuellement porter des paires clé-valeur comme `extras`. Ces données peuvent être utilisées pour envoyer des données avec une carte pour une manipulation ultérieure par l’application. Appelez simplement `card.extras` pour accéder à ces valeurs.

## Personnalisation

Les éléments de l’IU de Braze sont dotés d’un aspect et une convivialité par défaut qui correspondent aux composeurs du tableau de bord de Braze et visent à assurer la cohérence avec d’autres plateformes mobiles Braze. Les styles par défaut de Braze sont définis en CSS dans le SDK Braze. En écrasant des styles sélectionnés dans votre application, il est possible de personnaliser notre fil standard avec vos propres images de fond, des familles de polices, des styles, des tailles, des animations, et bien plus encore.

Par exemple, voici un exemple d'override qui fera apparaître le fil d'actualité en 800 px de large :

``` css
body .ab-feed {
  width: 800px;
}
```

## Catégories

Les instances du fil d’actualité Braze peuvent être configurées pour ne recevoir que des cartes d’une certaine « catégorie ». Cela permet l’intégration efficace de plusieurs flux de fils d’actualité au sein d’une seule application.

Les catégories de fils d’actualité peuvent être définies en fournissant le troisième paramètre `allowedCategories` à `toggleFeed` :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Vous pouvez également remplir un fil avec une combinaison de catégories comme dans l’exemple suivant :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## Indicateurs de messages non lus et lus

Braze fournit un indicateur de messages lus et non lus sur les cartes de fil d'actualité comme illustré ci-dessous :

![Une carte de fil d’actualité affichant l’image d’une montre accompagnée d’un texte. Dans le coin supérieur droit du texte, un triangle bleu ou gris indique si une carte a été lue ou non. Un triangle bleu indique qu'une carte a été lue.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

### Désactiver les indicateurs

Pour désactiver cette fonctionnalité, ajoutez le style suivant à votre CSS :

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

