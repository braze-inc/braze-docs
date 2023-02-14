---
nav_title: Android et FireOS
article_title: Configuration initiale du SDK Android pour Cordova
platform: 
  - Cordova
  - iOS
page_order: 0
page_type: reference
description: "Cet article couvre les étapes initiales de configuration du SDK pour les applications Android et FireOS fonctionnant sur Cordova."
search_rank: 2
---

# Configuration initiale du SDK

Télécharger le SDK depuis [GitHub][1]  et exécutez ce qui suit depuis la racine de votre projet :

```
cordova plugin add path_to_repo/appboy-cordova-sdk
```

Sinon, si vous exécutez Cordova 6 ou ultérieure, vous pouvez installer directement depuis GitHub :

```
cordova plugin add https://github.com/appboy/appboy-cordova-sdk#master
```

## Configurer le plug-in

Dans votre `config.xml`, ajouter un élément `preference` sous l’élément Android `platform` contenant votre clé API Braze avec le nom `com.appboy.api_key` :

```xml
<platform name="android">
    <preference name="com.appboy.api_key" value="YOUR_API_KEY" />
</platform>
```

## Définir une configuration supplémentaire

Le SDK Android pour Cordova permet également de configurer divers autres paramètres via le fichier `config.xml` :

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

Consultez le [plug-in Android pour Cordova][2] pour plus de détails.

### Exemple de préférence numérique

En raison de la manière dont le cadre de la structure Cordova 8.0.0 et ultérieures gère les préférences, celles étant entièrement numériques comme les ID d’expéditeur doivent être préfixées avec `str_` afin d’être correctement lues par le SDK, comme dans l’exemple suivant :

```xml
<platform name="android">
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="true" />
    <preference name="com.appboy.android_fcm_sender_id" value="str_64422926741" />
</platform>
```

## Configuration personnalisée

Ce plug-in peut être forké et modifié pour des implémentations personnalisées. Trouvez le code source natif spécifique à la plateforme dans le répertoire `/plugin/src`, l’interface JavaScript dans le répertoire `/plugin/www` et le fichier de configuration principal en `/plugin`.

Les utilisateurs qui vérifient leur répertoire de plateforme dans le contrôle de version (leur permettant de modifier les codes de manière permanente) seront en mesure de tirer davantage profit des éléments IU de Braze en les appelant directement à partir de leur projet spécifique à la plateforme.

### Enlever la configuration de notifications push automatiques (Android)

Pour supprimer un enregistrement de notification push automatique sur Android, définissez les préférences de configuration suivantes :

```xml
<platform name="android">
    <preference name="com.appboy.firebase_cloud_messaging_registration_enabled" value="false" />
</platform>
```

### Collecte des positions et des geofences

Pour activer la collecte des positions et les geofences Braze, utilisez [`geofence-branch`][3] au lieu de la valeur par défaut de la branche `master`. Par défaut, le SDK Braze désactive la collecte de position et les geofences Braze. En outre, utilisez la configuration des préférences suivantes :

```xml
<platform name="android">
    <preference name="com.appboy.enable_location_collection" value="true" />
    <preference name="com.appboy.geofences_enabled" value="true" />
</platform>
```

La branche de geofence peut être ajoutée à votre projet Cordova avec les éléments suivants :

```
cordova plugin add https://github.com/appboy/appboy-cordova-sdk#geofence-branch
```

### Retarder le suivi automatique des sessions

Définir `<preference name="com.appboy.android_disable_auto_session_tracking" value="true" />` dans votre `config.xml` pour désactiver le suivi automatique des sessions du plug-in Android pour Cordova. Pour commencer à suivre les sessions, appelez `AppboyPlugin.startSessionTracking()`. Notez que cela ne fera pas de suivi rétroactif et que le suivi de session commencera seulement à la `Activity.onStart()` suivante.

## Configuration initiale terminée

Une fois la configuration initiale terminée, vous pouvez accéder à l’interface JavaScript `AppboyPlugin` de votre application.

[1]: https://github.com/Appboy/appboy-cordova-sdk
[2]: https://github.com/Appboy/appboy-cordova-sdk/blob/master/src/android/AppboyPlugin.java
[3]: https://github.com/Appboy/appboy-cordova-sdk/tree/geofence-branch
