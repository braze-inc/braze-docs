---
nav_title: Badges
article_title: Demander la carte de contenu non visionnée pour les badges pour le Web
page_order: 4
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article de référence décrit comment demander le nombre de cartes de contenu non lues pour votre application Web."

---

# Badges

> Cet article de référence décrit comment demander le nombre de cartes de contenu non lues pour votre application Web.

## Demander le décompte des cartes de contenu non lues

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

``` javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Cela est souvent utilisé pour alimenter les badges indiquant combien de cartes de contenu n’ont pas été lues. Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html) pour plus d’informations.

{% comment %}
Braze n’actualisera pas les cartes de contenu sur les pages nouvellement chargées (cette fonction reviendra à 0) jusqu’à ce que vous affichiez le fil ou appeliez `braze.requestContentCardsRefresh();`.
{% endcomment %}
