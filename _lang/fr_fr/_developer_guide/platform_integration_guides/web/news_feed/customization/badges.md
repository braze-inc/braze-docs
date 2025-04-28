---
nav_title: Badges
article_title: Badges de fil d’actualité pour le Web
platform: Web
page_order: 3
page_type: reference
description: "Cet article traite de la manière de demander le nombre de cartes de fil d’actualité non lues et d’utiliser ces informations pour alimenter des badges pour votre application Web."
channel: news feed

---

# Badges

> Cet article traite de la manière de demander le nombre de cartes de fil d’actualité non lues et d’utiliser ces informations pour alimenter des badges pour votre application Web.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Demande de décompte de cartes de fil d’actualité non lues

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Cela est souvent utilisé pour alimenter les badges indiquant combien de cartes de fil d’actualité n’ont pas été lues. Consultez les [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) pour plus d'informations. Notez que Braze n’actualisera pas les cartes de fil d’actualité sur les pages nouvellement chargées (cette fonction reviendra à 0) jusqu’à ce que vous affichiez le fil ou appelez `braze.requestFeedRefresh();`

