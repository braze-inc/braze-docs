---
nav_title: iOS
article_title: Configuration initiale du SDK iOS pour Cordova
platform:
  - Cordova
  - iOS
page_order: 2
page_type: Référence
description: "Cet article décrit les étapes initiales de configuration du SDK pour les applications iOS fonctionnant sur Cordova."
---

# Configuration initiale du SDK

Téléchargez le SDK depuis [Github][1] et exécutez ce qui suit à la racine de votre projet :

```
plugin cordova ajouter path_to_repo/appboy-cordova-sdk/
```

Alternativement, si vous exécutez Cordova 6 ou plus, vous pouvez installer directement à partir de Github :

```
plugin cordova ajoutez https://github.com/appboy/appboy-cordova-sdk#master
```

## Configurer le plugin

Dans votre configuration. ml, ajoute un élément `préférence` sous l'élément de plateforme `iOS` qui contient votre clé d'API Braze avec le nom `com. ppboy.api_key`:

```xml
<platform name="ios">
    <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
</platform>
```

Configurez vos applications pour avoir les certificats appropriés pour push, via la [documentation push iOS][2].

### Suppression de la configuration automatique du push

Si vous voulez désactiver l'enregistrement automatique des push d'iOS, définissez les préférences de configuration suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.ios_disable_automatic_push_registration" value="YES" />
    ...
</platform>
```

### Collection facultative IDFA

Pour activer la collection automatique de l'iOS IDFA, définissez les préférences de configuration suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.ios_enable_idfa_automatic_collection" value="YES" />
</platform>
```

> Veuillez consulter la documentation de [iOS IDFA][3] pour plus d'informations.

### Collection de lieux et géorepérages

Pour activer la collecte d'emplacement et Braze Geofences, utilisez la branche [`de la branche de géorepérage`][3] au lieu de la branche par défaut `master` par défaut. Par défaut, Braze SDK désactive la collection d'emplacement et Braze Geofences. De plus, utilisez la configuration de préférences suivantes :

```xml
<platform name="ios">
    <preference name="com.appboy.enable_location_collection" value="true" />
    <preference name="com.appboy.geofences_enabled" value="true" />
</platform>
```

La branche geofence-branch peut être ajoutée à votre projet Cordova avec les éléments suivants :

```
plugin cordova ajouter https://github.com/appboy/appboy-cordova-sdk#geofence-branch
```

> Veuillez également visiter la documentation de [iOS Geofences][4] pour plus d'informations.

### Installation initiale terminée

Une fois la configuration initiale terminée, vous pouvez accéder à l'interface JavaScript `AppboyPlugin` dans votre application.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/
