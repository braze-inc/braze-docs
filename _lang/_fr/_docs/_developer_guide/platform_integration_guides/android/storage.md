---
nav_title: Stockage
article_title: Stockage pour Android/FireOS
platform:
  - Android
  - Pare-feu
page_order: 9
page_type: Référence
description: "Cet article de référence décrit les propriétés au niveau de l'appareil capturées par le Braze Android SDK."
---

# Stockage

Cet article décrit les différentes propriétés au niveau de l'appareil capturées lors de l'utilisation du SDK Android Braze.

## Propriétés de l'appareil

Par défaut, Braze recueillera les [propriétés au niveau du périphérique](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/enums/DeviceKey.html) suivantes pour permettre la personnalisation de l'appareil, de la langue et des fuseaux horaires des messages :

* AD_TRACKING_ACTIVÉ
* ANDROID version
* CARRIÈRE
* ID de la mise en valeur du GOOGLE
* Recommandé
* LOCALE
* MODEL
* NOTIFICIATION ACTIVÉE
* RÉSOLUTION
* TIMEZONE

Vous pouvez désactiver ou spécifier les propriétés que vous souhaitez collecter en les définissant en utilisant [`BrazeConfig.Builder. etDeviceObjectAllowlistEnabled()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDeviceObjectAllowlistEnabled-boolean-) et [`BrazeConfig.Builder.setDeviceObjectAllowlist()`](https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html#setDeviceObjectAllowlist-java.util.EnumSet-).

L'exemple suivant permet à l'objet périphérique de n'inclure que la version d'Android OS et la locale de l'appareil dans l'objet périphérique :
```
  new BrazeConfig.Builder()
      .setDeviceObjectAllowlistEnabled(true)
      .setDeviceObjectAllowlist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
```
Par défaut, tous les champs sont activés. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, sans le fuseau horaire, la livraison locale du fuseau horaire ne fonctionnera pas.

Pour en savoir plus sur les propriétés de l'appareil automatiquement collectées, visitez notre article [Options de collecte de données SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 
