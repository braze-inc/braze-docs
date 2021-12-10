---
nav_title: Stockage
article_title: Stockage pour iOS
platform: iOS
page_order: 8.9
page_type: Référence
description: "Cet article de référence décrit les propriétés de l'appareil capturées par Braze iOS SDK."
---

# Stockage

Cet article décrit les différentes propriétés au niveau de l'appareil capturées lors de l'utilisation du SDK iOS Braze.

## Propriétés de l'appareil

Par défaut, Braze recueillera les [propriétés au niveau du périphérique](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) suivantes pour permettre la personnalisation de l'appareil, de la langue et des fuseaux horaires des messages :

* Résolution de l'appareil
* Transporteur de l'appareil
* Localisation de l'appareil
* Modèle de l'appareil
* Version du système d'exploitation de l'appareil
* IDFV
* IDFA
* Push activé
* Fuseau horaire de l'appareil
* Statut d'authentification Push
* Suivi des publicités activé

Les champs périphériques configurables sont définis dans l'énumération [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179). Pour désactiver ou spécifier le champ périphérique que vous souhaitez autoriser, affecter le sens des bits `OU` des champs désirés à [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) dans `appboyOptions` de `startWithApiKey:inApplication:withAppboyOptions :`.

Par exemple, pour spécifier le fuseau horaire et la collection locale à autoriser, définir:
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionFuseau horaire | ABKDeviceOptionLocale);
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, sans le fuseau horaire, la livraison locale du fuseau horaire ne fonctionnera pas.

Pour en savoir plus sur les propriétés de l'appareil automatiquement collectées, visitez notre article [Options de collecte de données SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
