---
nav_title: Intégrations des TV connectées
article_title: Intégration des TV connectées pour le Web
platform: Web
page_order: 20
description: "Cet article explique comment utiliser le SDK Braze pour le Web pour l’intégrer aux TV connectées (Samsung et LG)."

---

# Intégrations des TV connectées

> Le SDK Web de Braze vous permet de collecter des analyses et d'afficher des messages in-app enrichis et des messages de carte de contenu aux utilisateurs de TV connectée, notamment les [téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) et les [téléviseurs LG (webOS)](https://webostv.developer.lge.com/discover). Cet article explique comment utiliser le SDK Web de Braze pour l’intégrer aux TV connectées.

Pour une référence technique complète, consultez notre [documentation JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) ou nos [exemples d'applications](https://github.com/Appboy/smart-tv-sample-apps) pour voir le SDK Web fonctionner sur un téléviseur.

## Installer le SDK Braze

Pour commencer, suivez notre guide de [configuration initiale du SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) pour le SDK Web.

Deux changements sont nécessaires lors de l’intégration avec les TV connectées :

1. Lorsque vous téléchargez ou importez le SDK Web, assurez-vous d’utiliser le paquet « de base » (disponible à l'adresse https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, où x.y est la version souhaitée). Nous recommandons d’utiliser la version CDN de notre SDK Web, en effet la version NPM est rédigée en modules ES natifs alors que la version CDN est transpilée jusqu’à ES5. Si vous préférez utiliser la [version NPM](https://www.npmjs.com/package/@braze/web-sdk), assurez-vous d'utiliser un bundler tel que webpack qui supprimera le code inutilisé et que le code est transpilé jusqu'à ES5.
2. Lors de l’initialisation du SDK pour le Web, vous devez définir les options d’initialisation `disablePushTokenMaintenance` et `manageServiceWorkerExternally` sur `true`.

## Analyse

Toutes ces méthodes d’analyse du SDK pour le Web peuvent être utilisées sur les TV connectées.

Pour obtenir un guide complet sur le suivi des événements personnalisés, des attributs personnalisés, etc., consultez notre documentation [Analytics.]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/) 

## Messages in-app et cartes de contenu

Le SDK Web de Braze prend en charge à la fois [les messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/) et les [cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/) sur les téléviseurs intelligents. Notez que vous devez utiliser le [SDK Web « de base »](https://www.npmjs.com/package/@braze/web-sdk) car le rendu des messages in-app et des cartes de contenu n'est pas pris en charge par l’affichage de notre interface utilisateur standard et doit être personnalisé par votre application pour s'intégrer à l'expérience de votre application TV.

Consultez la page [Affichage manuel des messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display) pour plus d'informations sur la manière dont votre TV connectée peut recevoir et afficher des messages in-app.


