---
nav_title: Android et FireOS
article_title: Configuration initiale du SDK Android pour Cordova
platform:
  - Cordova
  - iOS
page_order: 0
page_type: Référence
description: "Cet article couvre les étapes initiales de configuration du SDK pour les applications Android et FireOS exécutées sur Cordova."
---

# Configuration initiale du SDK

Téléchargez le SDK depuis [Github][1] et exécutez ce qui suit à la racine de votre projet :

```
plugin cordova ajouter path_to_repo/appboy-cordova-sdk
```

Alternativement, si vous exécutez Cordova 6 ou plus, vous pouvez installer directement à partir de Github :

```
plugin cordova ajoutez https://github.com/appboy/appboy-cordova-sdk#master
```

## Configurer le plugin

Dans votre configuration. ml, ajoute un élément `préférence` sous l'élément plate-forme `android` qui contient votre clé API Braze avec le nom `com. ppboy.api_key`:

```xml
<platform name="android">
    <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
</platform>
```

## Paramétrage de la configuration supplémentaire

Le SDK Android Cordova permet également à divers autres paramètres d'être configurés via le fichier config.xml :

```xml
<platform name="android">
    <preference name="com.appboy.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.appboy.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.appboy.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.appboy.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.appboy.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.appboy.android_log_level" value=LOG_LEVEL_INTEGER />
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.appboy.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.appboy.enable_location_collection" value="true"/"false" />
    <preference name="com.appboy.geofences_enabled" value="true"/"false" />
    <preference name="com.appboy.android_disable_auto_session_tracking" value="true"/"false" />
</platform>
```

Voir le [Plugin Android Cordova][2] pour plus de détails.


> En raison de la façon dont la Cordova 8.0. + framework gère les préférences, les préférences entièrement numériques comme les identifiants de l'expéditeur doivent être préfixées par `str_` afin d'être correctement lues par le SDK. Un exemple est inclus ci-dessous:

```xml
<platform name="android">
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="true" />
    <preference name="com.appboy.android_fcm_sender_id" value="str_64422926741" />
</platform>
```

## Configuration personnalisée

Notez que ce plugin peut être forked et modifié pour des implémentations personnalisées. Trouve le code source natif spécifique à la plate-forme dans le répertoire `/plugin/src` , l'interface JavaScript dans le répertoire `/plugin/www` et le fichier de configuration principal à `/plugin`.

Les utilisateurs qui vérifient le répertoire de leur plate-forme en contrôle de version (ce qui leur permet de faire des modifications permanentes de code là-bas) seront en mesure de tirer profit des éléments de l'interface utilisateur de Braze en les appelant directement depuis leur projet spécifique à leur plateforme.

### Suppression de la configuration automatique de push (Android)

Pour supprimer l'enregistrement automatique de push sur Android, définissez les préférences de configuration suivantes :

```xml
<platform name="android">
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="false" />
</platform>
```

### Collection de lieux et géorepérages

Pour activer la collecte d'emplacement et Braze Geofences, utilisez la branche [`de la branche de géorepérage`][3] au lieu de la branche par défaut `master` par défaut. Par défaut, Braze SDK désactive la collection d'emplacement et Braze Geofences. De plus, utilisez la configuration de préférences suivantes :

```xml
<platform name="android">
    <preference name="com.appboy.enable_location_collection" value="true" />
    <preference name="com.appboy.geofences_enabled" value="true" />
</platform>
```

La branche geofence-branch peut être ajoutée à votre projet Cordova avec les éléments suivants :

```
plugin cordova ajouter https://github.com/appboy/appboy-cordova-sdk#geofence-branch
```

### Retarder le suivi automatique de la session

Définissez `<preference name="com.appboy.android_disable_auto_session_tracking" value="true" />` dans votre `config.xml` pour désactiver le plugin Android Cordova des sessions de suivi automatique. To start tracking sessions, call `AppboyPlugin.startSessionTracking()`. Notez que cela ne suivra pas rétroactivement les sessions et ne commencera que les sessions de suivi à partir de la prochaine `Activity.onStart()`.

## Installation initiale terminée

Une fois la configuration initiale terminée, vous pouvez accéder à l'interface JavaScript `AppboyPlugin` dans votre application.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: https://github.com/Appboy/appboy-cordova-sdk/blob/master/src/android/AppboyPlugin.java
[3]: https://github.com/Appboy/appboy-cordova-sdk/tree/geofence-branch
