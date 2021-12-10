---
nav_title: Intégrations Smart TV en utilisant le SDK Web
article_title: Intégration de Smart TV pour le Web
platform: Web
page_order: 20
description: "Cet article couvre la façon d'utiliser le SDK Braze Web pour s'intégrer avec les Smart TVs (Samsung et LG)"
---

# Intégration de Smart TV

Le SDK Web Braze vous permet de collecter des données analytiques et d'afficher des messages riches dans l'application de messages et de cartes de contenu aux utilisateurs de la TV intelligente y compris [Samsung Tizen TVs][1] et [LG TVs (webOS)][2].

Pour une référence technique complète, veuillez consulter notre [Documentation Javascript][3] ou consultez nos [exemples d'applications][9] pour voir le Web SDK fonctionnant sur un téléviseur.

## Installer le Braze SDK

Pour commencer, veuillez suivre notre guide [Initial SDK][4] pour le SDK Web.

Deux modifications sont requises lors de l'intégration avec les Smart TVs :

1. Lors du téléchargement ou de l'importation du SDK Web, assurez-vous d'utiliser le bundle "core" qui peut être trouvé ici : [https://www.npmjs.com/package/@braze/web-sdk-core][6].

2. Lors de l'initialisation du SDK Web, vous devez définir les options d'initialisation `disablePushTokenMaintenance` et `manageServiceWorkerExternally` à `true`.

## Analyses

Toutes les mêmes méthodes d'analyse Web SDK peuvent être utilisées sur les Smart TVs.

Pour un guide complet sur le suivi des événements personnalisés, des attributs personnalisés et plus encore, veuillez lire notre [Documentation Analytiques]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/).

## Messages dans l'application et cartes de contenu

Le Web SDK de Braze prend en charge à la fois les [Messages In-App][7] et les [Cartes de Contenu][8] sur des téléviseurs intelligents. Veuillez noter : Vous devez utiliser le [« Core» Web SDK][6] comme le rendu des messages et des cartes de contenu intégrés n'est pas pris en charge en utilisant notre affichage standard de l'interface utilisateur, et devrait à la place être personnalisé par votre application pour s'adapter à l'expérience de votre application TV.

Pour en savoir plus sur la façon dont votre application Smart TV peut recevoir et afficher des messages dans l'application, voir notre guide pour [afficher manuellement les messages dans l'application][5].


[1]: https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html
[2]: http://webostv.developer.lge.com/discover/discover-webos-tv/
[3]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#manual-in-app-message-display
[6]: https://www.npmjs.com/package/@braze/web-sdk-core
[6]: https://www.npmjs.com/package/@braze/web-sdk-core
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/overview/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/overview/
[9]: https://github.com/Appboy/smart-tv-sample-apps
