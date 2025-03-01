---
nav_title: Amazon Gerät Messaging
article_title: Amazon Device Messaging Push-Benachrichtigungen für Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "Dieser Artikel referenziert die Integration von Amazon Android Push-Benachrichtigungen in die Unity-Plattform."
channel: push

---

# Amazon Gerät Messaging

> Dieser Artikel referenziert die Integration von Amazon Android Push-Benachrichtigungen in die Unity-Plattform.

Eine Push-Benachrichtigung ist eine Benachrichtigung außerhalb der App, die auf dem Bildschirm des Nutzers erscheint, wenn ein wichtiges Update erfolgt. Push-Benachrichtigungen sind eine wertvolle Möglichkeit, Ihre Nutzer:innen mit zeitkritischen und relevanten Inhalten zu versorgen oder sie mit Ihrer App zu erneuern.

ADM (Amazon Device Messaging) wird auf Nicht-Amazon-Geräten nicht unterstützt. Um Kindle Push zu testen, müssen Sie ein [FireOS Gerät](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm) besitzen. In der [Hilfe]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) finden Sie weitere bewährte Verfahren.

Braze sendet Push-Benachrichtigungen an Amazon Geräte über [Amazon Device Messaging (ADM](https://developer.amazon.com/public/apis/engage/device-messaging)).

## Schritt 1: Enablement von ADM

1. Erstellen Sie ein Konto im [Amazon Apps & Games Entwickler:in Portal](https://developer.amazon.com/public), falls Sie dies noch nicht getan haben.
2. Holen Sie sich die [OAuth-Zugangsdaten (Client-ID und Client-Geheimnis) und einen ADM-API-Schlüssel](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Aktivieren Sie **Automatische ADM-Registrierung aktiviert** im Unity Braze-Konfigurationsfenster. 
  - Alternativ können Sie auch die folgende Zeile in Ihre `res/values/braze.xml` Datei einfügen, um die ADM Registrierung zu aktivieren:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Schritt 2: AndroidManifest.xml aus Unity aktualisieren

Wenn Ihre App nicht über ein `AndroidManifest.xml` verfügt, können Sie das folgende Template als Vorlage verwenden. Wenn Sie bereits eine `AndroidManifest.xml` haben, stellen Sie sicher, dass die folgenden fehlenden Abschnitte zu Ihrer bestehenden `AndroidManifest.xml` hinzugefügt werden.

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

## Schritt 3: Speichern Sie Ihren ADM API-Schlüssel

Besorgen Sie sich zunächst [einen ADM API-Schlüssel für Ihre App](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  Als Nächstes speichern Sie Ihren ADM-API-Schlüssel in einer Datei mit dem Namen `api_key.txt` und speichern diese im [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) Ihres Projekts.

Amazon wird Ihren Schlüssel nicht erkennen, wenn `api_key.txt` Leerzeichen enthält, wie z.B. einen Zeilenumbruch am Ende.

Fügen Sie in Ihrer Datei `mainTemplate.gradle` Folgendes hinzu:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## Schritt 4: ADM-Jar hinzufügen

Die erforderliche ADM Jar-Datei kann gemäß der [Unity JAR-Dokumentation](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) an beliebiger Stelle in Ihrem Projekt platziert werden.

## Schritt 5: Fügen Sie das Client-Geheimnis und die Client-ID zu Ihrem Braze-Dashboard hinzu

Schließlich müssen Sie das Client-Geheimnis und die Client-ID, die Sie in [Schritt 1](#step-1-enable-adm) erhalten haben, auf der Seite Einstellungen verwalten des Braze-Dashboards hinzufügen.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

