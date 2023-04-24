---
nav_title: Désactivation du suivi SDK iOS
article_title: Désactivation du suivi SDK pour iOS
platform: iOS
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application iOS."

---

# Désactivation de la collecte de données pour iOS

Afin de se conformer aux réglementations de confidentialité des données, l’activité de suivi des données sur le SDK iOS peut être entièrement arrêtée à l’aide de la méthode [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733). Cette méthode entraînera l’annulation de toutes les connexions réseau, et le SDK Braze ne transmettra aucune donnée aux serveurs de Braze. Si vous souhaitez reprendre le recueil des données ultérieurement, vous pouvez utiliser la méthode [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) plus tard pour reprendre la collecte des données.

En outre, vous pouvez utiliser la méthode [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) pour effacer entièrement toutes les données côté client stockées sur le périphérique.

À moins qu’un utilisateur ne désinstalle toutes les applications d’un fournisseur sur un périphérique donné, le prochain SDK Braze ainsi que l’application s’exécutant après l’utilisation de `wipeDataAndDisableForAppRun()` entraînera la réidentification de notre serveur par l’utilisateur via son identifiant de périphérique (IDFV). Afin de supprimer complètement toutes les données utilisateur, vous devez combiner un appel à `wipeDataAndDisableForAppRun` avec une demande de suppression des données sur le serveur via le Braze [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint).

## SDK iOS v5.7.0 et ultérieurs
Pour les appareils utilisant le SDK iOS v5.7.0 et les versions ultérieures, lors de la [désactivation du recueil d’IDFV](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/), l’appel [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) n’entraînera pas de nouvelle identification de l’utilisateur par notre serveur à l’aide de son identifiant d’appareil (IDFV).