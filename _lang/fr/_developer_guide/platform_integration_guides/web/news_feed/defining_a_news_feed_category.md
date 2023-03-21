---
nav_title: Définir une catégorie de fil d’actualité
article_title: Définir une catégorie de fil d’actualité pour le Web
platform: Web
page_order: 3
page_type: reference
description: "Cet article explique comment définir une catégorie de fil d’actualité pour votre application Web."
channel: fil d’actualité

---

# Définir une catégorie de fil d’actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Les instances du fil d’actualité Braze peuvent être configurées pour ne recevoir que des cartes d’une certaine « catégorie ». Cela permet l’intégration efficace de plusieurs flux de fils d’actualité au sein d’une seule application.

Les catégories de fils d’actualité peuvent être définies en fournissant le troisième paramètre `allowedCategories` à `toggleFeed` :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Vous pouvez également remplir un fil avec une combinaison de catégories comme dans l’exemple suivant :

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
