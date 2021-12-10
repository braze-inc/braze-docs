---
nav_title: Flux multiples
article_title: Utilisation de plusieurs fils de cartes de contenu pour le Web
page_order: 5
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article décrit comment configurer et utiliser plusieurs flux de cartes de contenu."
---

# Utilisation de plusieurs flux de carte de contenu

Les cartes de contenu peuvent être filtrées sur l'application pour n'afficher que des cartes spécifiques, qui vous permet d'avoir plusieurs flux de carte de contenu pour différents cas d'utilisation (ayant un flux `Transactionnel` contre un flux `Marketing`).

La documentation suivante montre un exemple d'implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir les paires de valeur clé sur les cartes

Lors de la création d'une campagne de la carte de contenu, les données de la paire de valeur clé peuvent être définies sur chaque carte. Notre logique de filtrage utilisera cette paire de données de valeur clé pour catégoriser les cartes.

Pour les besoins de cet exemple, Nous allons définir une paire de valeur clé avec la clé `feed_type` qui désignera le flux de la carte de contenu dans lequel la carte doit être affichée. La valeur sera quel que soit votre flux personnalisé (`Transactional`, `Marketing`, ou autre nom de flux personnalisé).

## Étape 2 : Configurez votre flux personnalisé

L'exemple suivant affichera le flux de Cartes de Contenu pour les cartes de type `Transactionnelles`:

```javascript

/**
 * @param {String} feed_type - valeur du KVP "feed_type" pour filtrer
 */
fonction showCardsByFeedType(feed_type) {
  appboy. isplay. howContentCards(null, function(cards) {
    return cards.filter(function(card) {
      return card. xtras["feed_type"] === feed_type;
    });
  })
}
```

Ensuite, vous pouvez configurer une bascule pour votre fil personnalisé, comme l'exemple ci-dessous :

```javascript
// affiche le flux "Transactional" lorsque ce bouton est cliqué
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```
Pour plus d'informations, voir [nos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showContentCards).

Lorsque vous créez une campagne de carte de contenu, définir une paire clé-valeur comme: `feed_type` > `Transactionnel` ou basé sur la convention de nommage que vous choisissez d'implémenter.
