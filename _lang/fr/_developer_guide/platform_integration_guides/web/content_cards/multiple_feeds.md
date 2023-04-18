---
nav_title: Flux multiples
article_title: Utilisation de plusieurs flux de carte de contenu pour le Web
page_order: 3
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article décrit comment configurer et utiliser plusieurs flux de carte de contenu dans votre application Web."

---

# Fils multiples

> Les cartes de contenu peuvent être filtrées sur l’application pour afficher uniquement des cartes spécifiques, ce qui vous permet d’avoir plusieurs flux de carte de contenu pour différents cas d’usage (par exemple, avoir un flux `Transactional` et un flux `Marketing`).<br><br>La documentation suivante montre un exemple d’implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir des paires clé-valeur sur les cartes

Lors de la création d’une campagne de carte de contenu, les données de paires clé-valeur peuvent être définies pour chaque carte. Notre logique de filtrage utilisera les données de cette paire clé-valeur pour catégoriser les cartes.

Pour cet exemple, nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera dans quel flux la carte de contenu doit s’afficher. La valeur sera ce qu’est votre flux personnalisé (`Transactional`, `Marketing` ou d’autres noms de flux personnalisés).

## Étape 2 : Configurer votre flux personnalisé

L’exemple suivant montre le flux des cartes de contenu pour les types de cartes `Transactional` :

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter(function(card) {
      return card.extras["feed_type"] === feed_type;
    });
  })
}
```

Ensuite, vous pouvez configurer un basculement pour votre flux personnalisé :

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

Consultez [nos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) pour plus d’informations.

## Étape 3 : Définir les paires clé-valeur dans votre campagne

Lors de la création d’une campagne de carte de contenu, définissez votre paire clé-valeur dans laquelle la clé est `feed_type` et la valeur est `Transactional`.
