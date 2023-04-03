---
nav_title: Intégrations des TV connectées
article_title: Intégration des TV connectées pour le Web
platform: Web
page_order: 20
description: "Cet article explique comment utiliser le SDK Braze pour le Web pour l’intégrer aux TV connectées (Samsung et LG)."

---

# Intégrations des TV connectées

Le SDK Braze pour le Web vous permet de collecter des analytiques et d’afficher des messages in-app et de carte de contenu détaillés aux utilisateurs de TV connectées, notamment les [téléviseurs Samsung Tizen][1] et les [téléviseurs LG (webOS)][2].

Pour obtenir une référence technique complète, consultez notre [documentation JavaScript][3] ou nos [exemples d’applications][9] pour voir le SDK pour le Web exécuté sur un téléviseur.

## Installer le SDK Braze

Pour commencer, suivez notre guide de [configuration initiale du SDK][4] du SDK pour le Web.

Deux changements sont nécessaires lors de l’intégration avec les TV connectées :

1. Lors du téléchargement ou de l’importation de SDK Web, assurez-vous d’utiliser le groupe « noyau » (disponible sur https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js, où x.y est la version souhaitée). Nous recommandons d’utiliser la version CDN de notre SDK Web, en effet la version npm est rédigée en modules ES natifs alors que la version CDN est transpilée en ES5. Si vous préférez utiliser la [version npm][6], vérifiez que vous utilisez un bundler comme webpack qui va supprimer le code inutilisé et que le code est transpilé en ES5.
2. Lors de l’initialisation du SDK pour le Web, vous devez définir les options d’initialisation `disablePushTokenMaintenance` et `manageServiceWorkerExternally` sur `true`.

## Analytique

Toutes ces méthodes d’analytique du SDK pour le Web peuvent être utilisées sur les TV connectées.

Pour un guide complet sur le suivi des événements personnalisés, des attributs personnalisés et bien plus encore, consultez notre documentation sur l’[analytique]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/).

## Messages in-app et cartes de contenu

Le SDK Braze pour le Web prend en charge à la fois les [messages in-app][7] et les [cartes de contenu][8] sur les TV connectées. Notez que vous devez utiliser le [SDK pour le Web « central »][6] étant donné que le rendu de messages in-app et de cartes de contenu n’est pas pris en charge par l’affichage de notre interface utilisateur standard et doit plutôt être personnalisé par votre application pour s’intégrer à l’expérience sur l’application de votre téléviseur.

Consultez l’[affichage manuel de message in-app][5] pour plus d’informations sur la manière dont votre application de TV connectée peut recevoir et afficher ces messages.


[1]: https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html
[2]: https://webostv.developer.lge.com/discover
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display
[6]: https://www.npmjs.com/package/@braze/web-sdk
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/integration/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/
[9]: https://github.com/Appboy/smart-tv-sample-apps
