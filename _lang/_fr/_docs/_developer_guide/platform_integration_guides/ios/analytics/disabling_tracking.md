---
nav_title: Désactivation du suivi des SDK iOS
article_title: Désactivation du suivi SDK pour iOS
platform: iOS
page_order: 8
description: "Cet article montre comment désactiver la collecte de données pour votre application iOS."
---

# Désactivation de la collecte de données pour iOS

Afin de se conformer à la réglementation en matière de confidentialité des données, l'activité de suivi des données sur le SDK iOS peut être entièrement arrêtée en utilisant la méthode [`désactive SDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733). Cette méthode entraînera l'annulation de toutes les connexions réseau, et le Braze SDK ne transmettra aucune donnée aux serveurs de Brase. Si vous souhaitez reprendre la collecte de données à un moment ultérieur, vous pouvez utiliser la méthode [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) pour reprendre la collecte de données.

De plus, vous pouvez utiliser la méthode [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) pour effacer complètement toutes les données côté client stockées sur l'appareil.

À moins qu'un utilisateur ne désinstalle *toutes les* applications d'un vendeur sur un appareil donné, le prochain Braze SDK/app s'exécute après avoir appelé `wipeDataAndDisableForAppRun()` fera que notre serveur ré-identifie cet utilisateur via son identifiant de périphérique (IDFV). Afin de supprimer complètement toutes les données de l'utilisateur, vous devriez combiner un appel à `wipeDataAndDisableForAppRun` avec une demande de suppression de données sur le serveur via la [Braze REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-delete-endpoint).
