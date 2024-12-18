---
nav_title: Stockage
article_title: Stockage pour iOS
platform: Swift
page_order: 8.9
page_type: reference
description: "Cet article de référence décrit les propriétés au niveau de l'appareil capturées par le SDK Swift iOS de Braze."
---

# Stockage

> Cet article décrit les différentes propriétés au niveau de l'appareil capturées lors de l'utilisation du SDK Swift iOS de Braze.

## Propriétés de l’appareil

Par défaut, Braze collecte les propriétés suivantes [au niveau de l'appareil](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) pour permettre la personnalisation des messages en fonction de l'appareil, de la langue et du fuseau horaire :

* Opérateur mobile (voir la note sur [l’obsolescence de`CTCarrier`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty/carrier))
* Paramètres régionaux de l’appareil
* Modèle de l’appareil
* Version du système d’exploitation de l’appareil
* Statut d’autorisation des notifications push
* Options d'affichage des notifications push
* Notifications push activées
* Résolution de l’appareil
* Fuseau horaire de l’appareil

{% alert note %}
Le SDK Braze ne recueille pas automatiquement IDFA. Les applis peuvent éventuellement transmettre l'IDFA à Braze en implémentant directement les méthodes ci-dessous. Les applis doivent obtenir l'abonnement explicite au suivi par l'utilisateur final via le framework de transparence du suivi des applis avant de transmettre l'IDFA à Braze.

1. Pour définir l'état du suivi de la publicité, utilisez [`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:)/).
2. Pour définir l'identifiant de l'annonceur (IDFA), utilisez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/).
{% endalert %}

Les champs configurables d'appareil sont définis dans l’enum [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Pour désactiver ou spécifier le champ d'appareil que vous souhaitez autoriser, ajoutez les champs à la propriété [`devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) de l'objet `configuration`.

Par exemple, pour spécifier le fuseau horaire et la collecte des paramètres régionaux à autoriser, définissez :

{% tabs %}
{% tab swift %}

```swift
configuration.devicePropertyAllowList = [.timeZone, .locale]
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
configuration.devicePropertyAllowList = @[
    BRZDeviceProperty.timeZone,
    BRZDeviceProperty.locale
];
```

{% endtab %}
{% endtabs %}

Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés de l'appareil collectées automatiquement, consultez notre [collecte de données SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

