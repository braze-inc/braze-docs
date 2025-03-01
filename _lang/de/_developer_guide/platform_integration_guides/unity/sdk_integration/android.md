---
nav_title: Android
article_title: SDK-Android-Integration für Unity
platform: 
  - Unity
  - Android
page_order: 0
description: "Dieser Referenzartikel behandelt die Android SDK-Integration für die Unity-Plattform."
search_rank: .9
---

# SDK Android-Integration

> Dieser Referenzartikel behandelt die Android SDK-Integration für die Unity-Plattform. Folgen Sie diesen Anweisungen, um Braze in Ihrer Unity-Anwendung zum Laufen zu bringen.

## Schritt 1: Wählen Sie Ihr Braze Unity-Paket

Das Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) bündelt native Bindings für die Plattformen Android und iOS sowie eine C#-Schnittstelle.

Auf der [Braze Unity-Seite Releases](https://github.com/Appboy/appboy-unity-sdk/releases) stehen mehrere Braze Unity-Pakete zum Download zur Verfügung:
 
- `Appboy.unitypackage`
    - Dieses Paket bündelt die Android- und iOS-SDKs von Braze sowie die [SDWebImage-Abhängigkeit](https://github.com/SDWebImage/SDWebImage) für das iOS-SDK, die für die ordnungsgemäße Funktionalität des In-App-Messagings und der Content-Cards-Features von Braze auf iOS erforderlich ist. Das SDWebImage-Framework wird zum Herunterladen und Anzeigen von Bildern, einschließlich GIFs, verwendet. Wenn Sie die volle Funktionalität von Braze nutzen möchten, laden Sie dieses Paket herunter und importieren Sie es.
- `Appboy-nodeps.unitypackage`
    - Dieses Paket ähnelt dem `Appboy.unitypackage` mit der Ausnahme, dass das [SDWebImage](https://github.com/SDWebImage/SDWebImage) Framework nicht vorhanden ist. Dieses Paket ist nützlich, wenn Sie das SDWebImage-Framework nicht in Ihrer iOS App verwenden möchten.

**iOS**: Um zu sehen, ob Sie die [SDWebImage-Abhängigkeit](https://github.com/SDWebImage/SDWebImage) für Ihr iOS-Projekt benötigen, besuchen Sie die [Dokumentation zu iOS In-App-Nachrichten ]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).<br>
**Android**: Ab Unity 2.6.0 benötigt das gebündelte Braze Android SDK-Artefakt [AndroidX](https://developer.android.com/jetpack/androidx)-Abhängigkeiten. Wenn Sie zuvor ein `jetified unitypackage` verwendet haben, können Sie bedenkenlos auf das entsprechende `unitypackage` umsteigen.

## Schritt 2: Paket importieren

Importieren Sie das Paket im Unity-Editor in Ihr Unity-Projekt, indem Sie zu **Assets > Paket importieren > Angepasstes Paket** navigieren. Klicken Sie anschließend auf **Importieren**.

Alternativ folgen Sie den Anweisungen zum [Importieren von Unity-Assetpaketen](https://docs.unity3d.com/Manual/AssetPackages.html), um eine detailliertere Anleitung zum Importieren von benutzerdefinierten Unity-Paketen zu erhalten. 

{% alert note %}
Wenn Sie nur das iOS- oder Android-Plugin importieren möchten, heben Sie die Auswahl des Unterverzeichnisses `Plugins/Android` oder `Plugins/iOS` auf, wenn Sie das Braze `.unitypackage` importieren.
{% endalert %}

## Schritt 3: AndroidManifest.xml aktualisieren

Android Unity-Projekte erfordern eine [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)-Datei, um die Anwendung auszuführen. Außerdem benötigt Braze einige Ergänzungen zu Ihrem [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) um zu funktionieren.

### AndroidManifest.xml konfigurieren

Wenn Ihre App nicht über ein `AndroidManifest.xml` verfügt, können Sie das folgende Template als Vorlage verwenden. Wenn Sie bereits eine `AndroidManifest.xml` haben, stellen Sie sicher, dass die folgenden fehlenden Abschnitte zu Ihrer bestehenden `AndroidManifest.xml` hinzugefügt werden.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> Ihr `AndroidManifest.xml` sollte unter `Assets/Plugins/Android/AndroidManifest.xml` existieren. Weitere Informationen finden Sie in der [Unity AndroidManifest Dokumentation](https://docs.unity3d.com/Manual/android-manifest.html).

> Alle in Ihrer `AndroidManifest.xml`-Datei registrierten Activity-Klassen müssen vollständig mit dem Braze Android SDK integriert sein. Wenn Sie Ihre eigene Activity-Klasse hinzufügen, müssen Sie unsere [Anweisungen zur Integration von Unity Activity](#extending-braze-unity-player) befolgen, um sicherzustellen, dass Analytics gesammelt werden.

{% alert note %}
Ihre endgültige `AndroidManifest.xml` sollte nur eine einzige Aktivität mit `"android.intent.category.LAUNCHER"` enthalten.
{% endalert %}

### Aktualisieren Sie die AndroidManifest.xml mit Ihrem Paketnamen

Um Ihren Paketnamen zu finden, klicken Sie auf **Datei > Build-Einstellungen > Player-Einstellungen > Android Tab.**
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

In Ihrem `AndroidManifest.xml` sollten alle Instanzen von `REPLACE_WITH_YOUR_PACKAGE_NAME` durch Ihre `Package Name` aus dem vorherigen Schritt ersetzt werden.

## Schritt 4: Gradle-Abhängigkeiten hinzufügen {#unity-android-gradle-configuration}

Um Gradle-Abhängigkeiten zu Ihrem Unity-Projekt hinzuzufügen, müssen Sie zunächst ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) in Ihren Veröffentlichungseinstellungen anpassen. Dadurch wird eine Template gradle Datei erstellt, die Ihr Projekt verwenden wird. Eine Gradle-Datei ist für das Setzen von Abhängigkeiten und andere Projekteinstellungen zur Build-Zeit zuständig. Weitere Informationen finden Sie in der Braze Unity Beispiel App unter [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

Die folgenden Abhängigkeiten sind erforderlich:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Sie können diese Abhängigkeiten auch mit dem [External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver):in einstellen.

## Schritt 5: SDK konfigurieren {#unity-static-configuration}

Braze bietet eine native Unity Lösung für die Automatisierung der Unity-Android-Integration. 

1. Öffnen Sie im Unity-Editor die Braze-Konfigurationseinstellungen, indem Sie zu **Braze > Braze-Konfiguration** navigieren.
2. Aktivieren Sie das Kontrollkästchen **Unity Android Integration automatisieren**.
3. Geben Sie in das Feld **Braze API-Schlüssel** den API-Schlüssel Ihrer Anwendung ein, den Sie auf dem Braze-Dashboard unter **Einstellungen verwalten** finden.

{% alert note %}
Diese automatische Integration sollte nicht mit einer manuell erstellten `braze.xml`-Datei verwendet werden, da die Konfigurationswerte bei der Projekterstellung in Konflikt geraten können. Wenn Sie eine manuelle `braze.xml`-Datei benötigen, deaktivieren Sie die automatische Integration.
{% endalert %}

## Grundlegende SDK-Integration abgeschlossen

Braze sollte nun Daten von Ihrer Anwendung erfassen und die grundlegende Integration sollte abgeschlossen sein. Weitere Informationen über Integration Push finden Sie in den folgenden Artikeln: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) und [Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Wenn Sie mehr über die erweiterten Optionen der SDK-Integration erfahren möchten, lesen Sie bitte unter [Erweiterte Implementierung]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced) nach.

