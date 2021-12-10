---
nav_title: Badges
article_title: Demande de carte de contenu non consultée pour les badges pour le Web
page_order: 4
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article de référence décrit comment demander le nombre de cartes de contenu non lues."
---

# Requête du nombre de cartes de contenu non consultées

Vous pouvez demander le nombre de cartes non lues à tout moment en appelant :

``` javascript
appboy.getCachedContentCard().getUnviewedCardCount();
```

Ceci est souvent utilisé pour alimenter les badges indiquant combien de cartes de contenu non lues existent. Voir les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/ab.ContentCards.html#toc4) pour plus d'informations.

{% comment %}
Braze n'actualisera pas les Cartes de Contenu lors du chargement de nouvelles pages (et donc cette fonction retournera 0) jusqu'à ce que vous montiez le flux ou appelez `appboy. equestContentCardsRafraîchissement ();`.
{% endcomment %}
