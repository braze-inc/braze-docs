---
nav_title: Définir une catégorie de fil d’actualité
article_title: Définir une catégorie de fil d’actualité pour le Web
platform: Web
page_order: 3
page_type: reference
description: "Cet article explique comment définir une catégorie de fil d’actualité pour votre application Web."
channel: news feed

---

# Définir une catégorie de fil d’actualité

> Cet article explique comment définir une catégorie de fil d’actualité pour le SDK Web de Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Les instances du fil d’actualité Braze peuvent être configurées pour ne recevoir que des cartes d’une certaine « catégorie ». Cela permet l’intégration efficace de plusieurs flux de fils d’actualité au sein d’une seule application.

Les catégories de fils d’actualité peuvent être définies en fournissant le troisième paramètre `allowedCategories` à `toggleFeed` :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Vous pouvez également remplir un fil avec une combinaison de catégories comme dans l’exemple suivant :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
