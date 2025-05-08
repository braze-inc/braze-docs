---
nav_title: Messagerie électronique des appareils Amazon
article_title: Notifications push de messagerie des appareils Amazon pour Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "Cet article de référence couvre l’intégration de notifications push Amazon Android pour la plateforme Unity."
channel: push

---

# Messagerie électronique des appareils Amazon

> Cet article de référence couvre l’intégration de notifications push Amazon Android pour la plateforme Unity.

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

ADM (Amazon Device Messaging) n’est pas pris en charge sur les appareils ne faisant pas partie d’Amazon. Pour tester la poussée Kindle, vous devez avoir un [appareil FireOS](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Consultez la [section d'aide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) pour des pratiques exemplaires supplémentaires.

Braze envoie des notifications push aux appareils Amazon en utilisant [Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Étape 1 : Activer ADM

1. Créez un compte avec le [Portail des développeurs d'applications et de jeux Amazon](https://developer.amazon.com/public) si vous ne l'avez pas encore fait.
2. Obtenez les [identifiants OAuth (ID client et secret client) et une clé API ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Activez **Enregistrement ADM automatique activé** dans la fenêtre de configuration de Braze Unity. 
  - Vous pouvez également ajouter la ligne suivante à votre `res/values/braze.xml` pour activer l’enregistrement ADM :

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Étape 2 : Mettre à jour Unity AndroidManifest.xml

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
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
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

Tout d’abord, [obtenez une clé API ADM pour votre application](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  Ensuite, enregistrez votre clé API ADM dans un fichier nommé `api_key.txt` et enregistrez-le dans le dossier [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de votre projet.

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

Le fichier Jar ADM requis peut être placé n'importe où dans votre projet, conformément à la [documentation JAR d'Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

## Étape 5 : Ajouter un identifiant secret client et un identifiant client à votre tableau de bord de Braze

Enfin, vous devez ajouter le Secret Client et l'ID Client que vous avez obtenus dans [l'Étape 1](#step-1-enable-adm) à la page **Gérer les paramètres** du tableau de bord de Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

