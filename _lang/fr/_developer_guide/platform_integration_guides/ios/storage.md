---
nav_title: Stockage
article_title: Stockage pour iOS
platform: iOS
page_order: 8.9
page_type: reference
description: "Cet article de référence décrit les propriétés capturées par le SDK Braze pour iOS au niveau du périphérique."

---

{% multi_lang_include deprecations/objective-c.md %}

# Stockage

Cet article décrit les différentes propriétés capturées lors de l’utilisation du SDK Braze pour iOS au niveau du périphérique.

## Propriétés de l’appareil

Par défaut, Braze collecte les [propriétés suivantes au niveau du périphérique](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181) pour permettre la personnalisation des messages en fonction du périphérique, de la langue et du fuseau horaire :

* Résolution de l’appareil
* Opérateur mobile
* Emplacement de l’appareil
* Modèle de l’appareil
* Version du système d’exploitation de l’appareil
* IDFV (facultatif avec le [SDK iOS v5.7.0 et ultérieur](https://github.com/braze-inc/braze-swift-sdk))
* Notifications push activées
* Fuseau horaire de l’appareil
* Statut d’autorisation des notifications push
* Suivi des campagnes publicitaires activé

{% alert note %}
Le SDK Braze ne recueille pas automatiquement IDFA. Les applications peuvent éventuellement transmettre l’IDFA à Braze en implémentant le protocole `ABKIDFADelegate`. Les applications doivent obtenir un abonnement explicite à l’utilisateur final pour suivre l’infrastructure de transparence du suivi des applications avant de passer à l’IDFA à Braze.
{% endalert %}

Les champs configurables de périphérique sont définis dans l’enum [`ABKDeviceOptions`](https://github.com/Appboy/appboy-ios-sdk/blob/4390e9eac8401bccdb81b053fa54eb87b1f6fcaa/Appboy-tvOS-SDK/AppboyTVOSKit.framework/Headers/Appboy.h#L179). Pour désactiver ou spécifier le champ du périphérique que vous souhaitez autoriser, affectez aux champs souhaités le niveau de bit `OR` au [`ABKDeviceAllowlistKey`](https://github.com/Appboy/appboy-ios-sdk/blob/fed071000722673754da288cace15c1ff8aca432/AppboyKit/include/Appboy.h#L148) dans `appboyOptions` de `startWithApiKey:inApplication:withAppboyOptions:`.

Par exemple, pour spécifier le fuseau horaire et la collecte des paramètres régionaux à autoriser, définissez :
```
appboyOptions[ABKDeviceAllowlistKey] = @(ABKDeviceOptionTimezone | ABKDeviceOptionLocale);
```

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés du périphérique collectées automatiquement, consultez [Collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
