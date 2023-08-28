---
nav_title: Stockage
article_title: Stockage pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 9
page_type: reference
description: "Cet article de référence décrit les propriétés capturées par le SDK Braze pour Android au niveau du dispositif."

---

# Stockage

> Cet article décrit les différentes propriétés capturées lors de l’utilisation du SDK Braze pour Android au niveau du dispositif.

## Propriétés de l’appareil

Par défaut, Braze collecte les [propriétés suivantes au niveau du périphérique][1] pour permettre la personnalisation des messages en fonction du périphérique, de la langue et du fuseau horaire :

* `AD_TRACKING_ENABLED`
* `ANDROID_VERSION`
* `CARRIER`
* `IS_BACKGROUND_RESTRICTED`
* `LOCALE`
* `MODEL`
* `NOTIFICIATION_ENABLED`
* `RESOLUTION`
* `TIMEZONE`

{% alert note %}
`AD_TRACKING_ENABLED` et `TIMEZONE` ne sont pas collectées si elles sont `null` ou vides. `GOOGLE_ADVERTISING_ID` n’est pas collecté automatiquement par le SDK et doit être transmis via `com.braze.IBraze.setGoogleAdvertisingId`.
{% endalert %}

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en les paramétrant à l’aide de [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`][2] et de [`BrazeConfig.Builder.setDeviceObjectAllowlist()`][3].

L’exemple ci-dessous présente comment lister l’objet du dispositif pour y inclure uniquement la version de l’OS Android et la localisation :
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Pour en savoir plus sur les propriétés du dispositif collectées automatiquement, consultez notre [collecte de données du SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html
[3]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html
