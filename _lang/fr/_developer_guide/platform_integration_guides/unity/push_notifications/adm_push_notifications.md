---
nav_title: Messagerie électronique des périphériques Amazon
article_title: Notifications push de messagerie des périphériques Amazon pour Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "Cet article de référence couvre l’intégration de notifications push Amazon Android pour la plateforme Unity."
channel: push

---

# Intégration

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

ADM (Amazon Device Messaging) n’est pas pris en charge sur les appareils ne faisant pas partie d’Amazon. Pour tester la notification push Kindle, vous devez avoir un [appareil FireOS][32]. Découvrez la [section d’aide][8] pour des meilleures pratiques supplémentaires.

Braze envoie des notifications push aux appareils Amazon en utilisant [Amazon Device Messaging (ADM)][14].

## Étape 1 : Activer ADM

1. Créer un compte auprès du [Portail des développeurs des applications et des jeux Amazon][10] si vous ne l’avez pas déjà fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM][11].
3. Activez **Enregistrement ADM automatique activé** dans la fenêtre de configuration de Braze Unity. 
  - Vous pouvez également ajouter la ligne suivante à votre `res/values/braze.xml` pour activer l’enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Étape 2 : Mettre à jour AndroidManifest.xml pour Unity

Si votre application n’a pas de `AndroidManifest.xml`, vous pouvez utiliser ce qui suit comme modèle. Sinon, si vous avez déjà un `AndroidManifest.xml`, assurez-vous que l’une des sections manquantes suivantes est ajoutée à votre `AndroidManifest.xml` existant.

```xml
<?xml version="1.0" encoding="utf-8"?>
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

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
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
    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

## Étape 3 : Stocker votre clé API ADM

Tout d’abord, [obtenez une clé API ADM pour votre application][11].  Ensuite, enregistrez votre clé API ADM dans un fichier nommé `api_key.txt` et enregistrez-le dans votre dossier de projet [`Assets/`][54].

Amazon ne reconnaîtra pas votre clé si `api_key.txt` contient des caractères blancs, comme un saut de ligne.

Ajoutez à votre fichier `mainTemplate.gradle` :

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## Étape 4 : Ajouter un Jar ADM

Le fichier de récipient ADM requis peut être placé n’importe où dans votre projet conformément au [Documentation UNITY JAR][53].

## Étape 5 : Ajouter un identifiant secret client et un identifiant client à votre tableau de bord de Braze

Enfin, vous devez ajouter le secret client et l’ID client que vous avez obtenu au cours de l’[étape 1][2] à la page **Manage Settings** du tableau de bord de Braze.

![][34]

[2]: #step-1-enable-adm
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/
[10]: https://developer.amazon.com/public
[11]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials
[12]: https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm
[14]: https://developer.amazon.com/public/apis/engage/device-messaging
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[32]: https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm
[34]: {% image_buster /assets/img_archive/fire_os_dashboard.png %}
[53]: https://docs.unity3d.com/Manual/AndroidJARPlugins.html
[54]: https://docs.unity3d.com/Manual/AndroidAARPlugins.html
