# Stockage

> Cet article décrit les différentes propriétés capturées lors de l’utilisation du SDK Braze pour Android au niveau du dispositif.

## Propriétés de l’appareil

Par défaut, Braze collecte les propriétés suivantes [au niveau de l'appareil](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html) pour permettre la personnalisation des messages en fonction de l'appareil, de la langue et du fuseau horaire :

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
Les propriétés `AD_TRACKING_ENABLED` et `TIMEZONE` ne sont pas collectées si elles sont `null` ou vides. La propriété`GOOGLE_ADVERTISING_ID` n'est pas collectée automatiquement par le SDK et doit être transmise via [`setGoogleAdvertisingId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).
{% endalert %}

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en les définissant à l'aide de [`BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html) et [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html).

L’exemple ci-dessous présente comment lister l’objet du dispositif pour y inclure uniquement la version de l’OS Android et la localisation :
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire.

Visitez notre [article sur la collecte de données SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) pour en savoir plus sur les propriétés des appareils collectées automatiquement.


