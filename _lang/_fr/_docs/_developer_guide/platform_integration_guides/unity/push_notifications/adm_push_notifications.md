---
nav_title: Messagerie de l'appareil Amazon
article_title: Notifications push de messagerie Amazon pour l'unité
platform:
  - Unité
  - Android
page_order: 2
description: "Cet article de référence couvre l’intégration de notification push Amazon Android pour la plate-forme Unity."
channel: Pousser
---

# Intégration

Une notification push est une alerte hors application qui apparaît à l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push sont un moyen précieux de fournir à vos utilisateurs un contenu sensible au temps et pertinent ou de les réengager avec votre application.

> ADM (Amazon Device Messaging) n'est pas pris en charge sur les appareils non-Amazon. Pour tester Kindle Push vous devez avoir un appareil FireOS ([voir la liste Amazon des périphériques pris en charge][32]).

Consultez [la section Aide][8] pour les meilleures pratiques additionnelles.

Braze envoie des notifications push aux appareils Amazon en utilisant [Amazon Device Messaging (ADM)][14].

> La messagerie de l'appareil Amazon (ADM) est prise en charge __seulement__ sur les téléphones Feu et tablettes (à l'exception de la génération Kindle Fire 1er). Vous ne pouvez pas tester la messagerie ADM sur un appareil Android normal.

## Étape 1 : Activer l'ADM

- Créez un compte avec le [Amazon Apps & Games Developer Portal][10] si vous ne l'avez pas déjà fait.
- Obtenez les identifiants OAuth (Client ID et Client Secret) et une clé API ADM en suivant les instructions dans [Obtention des identifiants de messagerie Amazon][11].
- Activez "Enregistrement automatique ADM activé" dans la fenêtre de configuration de Braze d'unité.
- Alternativement, vous pouvez ajouter la ligne suivante à votre fichier `res/values/braze.xml` pour activer l'enregistrement ADM :

  ```xml
  <bool name="com_appboy_push_adm_messaging_registration_enabled">vrai</bool>
  ```

## Étape 2 : Mettre à jour Unity AndroidManifest.xml

Si votre application n'a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que toutes les sections manquantes ci-dessous sont ajoutées à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1. " encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <! - Applique les méthodes nécessaires à Braze pour s'assurer que les analyses sont collectées et que les notifications push sont transmises correctement à l'application Unity. -->
    <activity android:name="com.appboy.unity.AppboyUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- BroadcastReceiver used to forward certain Braze push notification events to Unity -->
    <receiver android:name="com.appboy.unity.AppboyUnityPushBroadcastReceiver" android:exported="false" >
      <intent-filter>
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_RECEIVED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_NOTIFICATION_OPENED" />
        <action android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.intent.APPBOY_PUSH_DELETED" />
      </intent-filter>
    </receiver>
    <receiver android:name="com.appboy.AppboyAdmReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

## Étape 3 : Stockez votre clé API ADM

- Enregistrez votre clé API ADM dans un fichier nommé `api_key.txt` et sauvegardez-la dans le dossier [`Assets/Plugins/Android/assets`][54].
- Pour savoir comment obtenir une clé API ADM pour votre application, consultez la documentation d'Amazon sur [l'obtention d'une clé API ADM][11].
- Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères d'espace blanc, comme un saut de ligne suivant.

## Étape 4 : Ajouter un Jar ADM

Le fichier ADM Jar requis peut être placé n'importe où dans votre projet selon la [documentation JAR Unity][53].

## Étape 5 : Ajouter le Client Secret et l'ID Client au tableau de bord Braze

Enfin, vous devez ajouter le Client Secret et l'ID Client que vous avez obtenu dans [Étape 1][2] à la page du tableau de bord de Braze __Gérer les paramètres__ comme illustré ci-dessous :

!\[Tableau de bord FireOS\]\[34\]
[34]: {% image_buster /assets/img_archive/fire_os_dashboard.png %}

[2]: #step-1-enable-adm
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/
[10]: https://developer.amazon.com/public
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[14]: https://developer.amazon.com/public/apis/engage/device-messaging
[32]: https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm
[53]: https://docs.unity3d.com/Manual/AndroidJARPlugins.html
[54]: https://docs.unity3d.com/Manual/AndroidAARPlugins.html
