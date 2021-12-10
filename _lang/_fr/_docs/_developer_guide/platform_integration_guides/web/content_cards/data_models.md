---
nav_title: Intégration
article_title: Intégration de la carte de contenu pour le Web
page_order: 0.2
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article couvre l'intégration de la carte de contenu pour le Web, y compris les types de cartes contenues et la façon de demander le nombre de cartes de contenu non lues."
---

# Intégration de la carte de contenu

Le SDK Web Braze comprend une interface utilisateur de flux de cartes de contenu pour accélérer vos efforts d'intégration. Si vous préférez construire votre propre interface utilisateur à la place, consultez notre [Guide de personnalisation](/docs/developer_guide/platform_integration_guides/web/content_cards/customization/).

## Interface de flux standard

Pour utiliser l'interface des Cartes de Contenu incluse, vous devrez spécifier où sur votre site Web pour afficher le flux.

Dans cet exemple, nous avons un `<div id="feed"></div>` dans lequel nous voulons placer le flux de cartes de contenu.

Nous utiliserons trois boutons pour masquer, afficher ou basculer (masquer ou afficher en fonction de son état actuel) le flux.

```html

<button id="toggle" type="button">Activer/désactiver le flux des cartes</button>
<button id="hide" type="button">Masquer le flux des cartes</button>
<button id="show" type="button">Afficher le flux des cartes</button>

<nav>
    <h1>Votre flux personnalisé</h1>
    <div id="feed"></div>
</nav>

<script>
   // nous supposons que nous avons une fenêtre. ppboy
   // vous pouvez également utiliser notre intégration npm à la place:
   // importer braze de "@braze/web-sdk";

   const toggle = document. etElementById("activer");
   const hide = document. etElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle. nclick = function(){
      appboy.display.toggleContentCards(feed);    
   }

   cacher. nclick = function(){
      appboy.display.hideContentCards();
   }

   afficher. nclick = function(){
      appboy.display.showContentCards(feed);    
   }
</script>
```

Lors de l'utilisation des `toggleContentCards(parentNode, filterFunction)` et `showContentCard(parentNode, methodes)` , si aucun argument n'est fourni, toutes les Cartes de Contenu seront affichées dans une barre latérale à position fixe sur le côté droit de la page. Sinon, le flux sera placé dans l'option `parentNode` spécifiée.

| Paramètres             | Libellé                                                                                                                                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Noeud parent`         | Le noeud HTML dans lequel afficher les cartes de contenu. Si le noeud parent a déjà une vue de Cartes de Contenu Braze comme descendant direct, les Cartes de Contenu existantes seront remplacées. Par exemple, vous devez passer dans `document.querySelector(".my-container")`. |
| `fonction de filtrage` | Une fonction de filtre/tri pour les cartes affichées dans cette vue. Invoqué avec le tableau d'objets ab.Card, trié par {pinned, date} Il est attendu de retourner un tableau d'objets ab.Card triés à afficher pour cet utilisateur. Si omis, toutes les cartes seront affichées. |
{: .reset-td-br-1 .reset-td-br-2}

[Voir les docs JS](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards) pour plus d'informations sur la désactivation des cartes de contenu.

### Requête du nombre de cartes de contenu non consultées

Vous pouvez demander le nombre de cartes non lues à tout moment en appelant :

```javascript
appboy.getCachedContentCard().getUnviewedCardCount();
```

Ceci est souvent utilisé pour alimenter les badges indiquant combien de cartes de contenu non lues existent. Voir les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) pour plus d'informations.

{% comment %}
Braze n'actualisera pas les Cartes de Contenu lors du chargement de nouvelles pages (et donc cette fonction retournera 0) jusqu'à ce que vous montiez le flux ou appelez `appboy. equestContentCardsRafraîchissement ();`.
{% endcomment %}

### Groupe de contrôle

Si vous utilisez le flux de Cartes de Contenu par défaut de Braze, les impressions et les clics seront automatiquement suivies.

Si vous utilisez une intégration personnalisée pour les cartes de contenu, votre intégration doit enregistrer les impressions quand une carte de contrôle _aurait été vue_.

Voici un exemple de la façon de déterminer si une carte de contenu est une carte "Contrôle" :

```javascript
function isControlCard(card) {
    return card instanceof appboy.ControlCard;
}
```

### Paires clé-valeur

Les objets `ab.Card` peuvent éventuellement transporter des paires clé-valeur sous la forme `d'extras`. Celles-ci peuvent être utilisées pour envoyer des données avec une carte pour un traitement ultérieur par l'application. Appelez [`card.extras`](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html) pour accéder à ces valeurs.

### Méthodes de carte supplémentaires

| Méthode                                                     | Libellé                                                                                                                                                                                         | Lier                                                                                                                                                                    |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Impressions de la carte de log`                            | Enregistre un événement d’impression pour la liste de cartes donnée. Ceci est requis lorsque vous utilisez une interface utilisateur personnalisée et non pas l'interface utilisateur de Braze. | [Docs JS pour logCardImpressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcardimpressions)                                                   |
| `format@@0 logCardClick`                                    | Enregistre un événement en cliquant pour une carte donnée. Ceci est requis lorsque vous utilisez une interface utilisateur personnalisée et non pas l'interface utilisateur de Braze.           | [Docs JS pour logCardClick](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcardclick)                                                               |
| `Montrer les cartes de contenu`                             | Afficher les fiches de contenu de l'utilisateur.                                                                                                                                                | [Docs JS pour showContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards)                                                      |
| `masquer les cartes de contenu`                             | Masquer toutes les cartes de contenu Braze actuellement affichées.                                                                                                                              | [Documents JS pour les cartes cachées](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.hideContentCards)                                               |
| `activer/désactiver les cartes de contenu`                  | Afficher les fiches de contenu de l'utilisateur.                                                                                                                                                | [Documents JS pour toggleContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.toggleContentCards)                                             |
| `getCachedContentCards()`                                   | Obtenez toutes les cartes actuellement disponibles à partir de la dernière mise à jour des cartes de contenu.                                                                                   | [Docs JS pour getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)                                             |
| `s'abonner aux mises à jour des cartes de contenu (abonné)` | S'abonner aux mises à jour des Cartes de Contenu. <br> La fonction de rappel de l'abonné sera appelée chaque fois que les cartes de contenu sont mises à jour.                            | [Documents JS pour vous abonner aux mises à jour des cartes de contenu](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.subscribeToContentCardsUpdates) |
| `dismissCard()`                                             | Rejeter la carte par programmation (disponible dans la v2.4.1).                                                                                                                                 | [Docs JS pour la carte de rejet](https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html#dismissCard)                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
