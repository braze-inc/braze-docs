---
nav_title: iOS
article_title: Configuration initiale du SDK iOS pour Cordova
platform: 
  - Cordova
  - iOS
page_order: 2
page_type: reference
description: "Cet article décrit les étapes initiales de configuration SDK pour les applications iOS fonctionnant sur Cordova."
search_rank: 1
---

# Configuration initiale du SDK

Télécharger le SDK depuis [GitHub][1] et exécutez ce qui suit depuis la racine de votre projet :

```
cordova plugin add path_to_repo/appboy-cordova-sdk/
```

Sinon, si vous exécutez Cordova 6 ou ultérieure, vous pouvez installer directement depuis GitHub :

```
cordova plugin add https://github.com/appboy/appboy-cordova-sdk#master
```

## Configurer le plug-in

Dans votre `config.xml`, ajouter un élément `preference` sous l’élément iOS `platform` contenant votre clé API Braze avec le nom `com.appboy.api_key` :

```xml
<platform name="ios">
    <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
</platform>
```

Configurez vos applications pour que les certificats appropriés soient utilisés pour les notifications push, via la [Documentation de notification push iOS][2].

### Enlever la configuration de notifications push automatiques

Si vous souhaitez désactiver l’enregistrement de notification push automatique iOS, définissez les préférences de configuration suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.ios_disable_automatic_push_registration" value="YES" />
    ...
</platform>
```

### Collecte IDFA facultative

Pour activer la collection automatique de l’[IDFA iOS][3], définissez les préférences de configuration suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.ios_enable_idfa_automatic_collection" value="YES" />
</platform>
```

### Collecte des positions et des geofences

Pour activer la collecte des positions et les geofences Braze, utilisez [`geofence-branch`][3] au lieu de la valeur par défaut de la branche `master`. Par défaut, le SDK Braze désactive la collecte de position et les geofences Braze. En outre, utilisez la configuration des préférences suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.enable_location_collection" value="true" />
    <preference name="com.appboy.geofences_enabled" value="true" />
</platform>
```

Le `geofence-branch` peut être ajouté à votre projet Cordova avec les éléments suivants :

```
cordova plugin add https://github.com/appboy/appboy-cordova-sdk#geofence-branch
```

Consultez les [Geofences iOS][4] pour plus de détails.

### Configuration initiale terminée

Une fois la configuration initiale terminée, vous pouvez accéder à l’interface JavaScript `AppboyPlugin` dans votre application.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/
