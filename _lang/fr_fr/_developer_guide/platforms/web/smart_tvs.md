---
nav_title: Prise en charge de la TV connectée
article_title: Prise en charge de la TV connectée pour le SDK Web Braze
platform: Web
page_order: 30
description: "Cet article explique comment utiliser le SDK Braze pour le Web pour l’intégrer aux TV connectées (Samsung et LG)."

---

# Prise en charge de la TV connectée

> Le SDK Web de Braze vous permet de collecter des analyses et d'afficher des messages in-app enrichis et des messages de carte de contenu aux utilisateurs de TV connectée, notamment les [téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) et les [téléviseurs LG (webOS)](https://webostv.developer.lge.com/discover). Cet article explique comment utiliser le SDK Web de Braze pour l’intégrer aux TV connectées.

{% alert tip %}
Pour une référence technique complète, consultez notre [documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) ou nos [exemples d'applications](https://github.com/Appboy/smart-tv-sample-apps) pour voir le SDK Web fonctionner sur un téléviseur.
{% endalert %}

 %} developer_guide/prerequisites/web.md

## Configuration du SDK de Braze Web

Deux changements sont nécessaires lors de l’intégration avec les TV connectées :

1. Lorsque vous téléchargez ou importez le SDK Web, assurez-vous d’utiliser le paquet « de base » (disponible à l'adresse `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, où `x.y` est la version souhaitée). Nous recommandons d’utiliser la version CDN de notre SDK Web, en effet la version NPM est rédigée en modules ES natifs alors que la version CDN est transpilée jusqu’à ES5. Si vous préférez utiliser la [version NPM](https://www.npmjs.com/package/@braze/web-sdk), assurez-vous d'utiliser un bundler tel que webpack qui supprimera le code inutilisé et que le code est transpilé jusqu'à ES5.
2. Lors de l’initialisation du SDK pour le Web, vous devez définir les options d’initialisation `disablePushTokenMaintenance` et `manageServiceWorkerExternally` sur `true`.

## Analyse

Toutes ces méthodes d’analyse du SDK pour le Web peuvent être utilisées sur les TV connectées. Pour une présentation complète du suivi des événements personnalisés, des attributs personnalisés, etc., consultez la section [Analyses.]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)

## Messages in-app et cartes de contenu

Le SDK Web de Braze prend en charge à la fois [les messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web) et les [cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) sur les téléviseurs intelligents. Notez que vous devez utiliser le [SDK Web « de base »](https://www.npmjs.com/package/@braze/web-sdk) car le rendu des messages in-app et des cartes de contenu n'est pas pris en charge par l’affichage de notre interface utilisateur standard et doit être personnalisé par votre application pour s'intégrer à l'expérience de votre application TV.

Pour plus d'informations sur la façon dont votre TV connectée peut recevoir et afficher des messages in-app, voir [Déclencher des messages.]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
