---
nav_title: SDK-Ersteinrichtung
article_title: Erste SDK-Einrichtung für React Native
platform: React Native
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie das React Native SDK unter Android und iOS integrieren."
search_rank: 1
---

# SDK-Ersteinrichtung

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK für React Native installieren. Die Installation des Braze React Native SDK stellt grundlegende Analytics-Funktionen bereit und ermöglicht Ihnen die Integration von In-App-Nachrichten und Content-Cards für iOS und Android mit nur einer Codebasis.

## Voraussetzungen und Kompatibilität

Für die Einrichtung dieses SDK ist React Native v0.71 oder höher erforderlich. Die vollständige Liste der unterstützten Versionen finden Sie in unserem [React Native SDK GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Unterstützung für die neue Architektur von React Native

{% sdk_min_versions reactnative:2.0.1 %}

## Verwendung von Braze mit der neuen Architektur

Das Braze React Native SDK ist mit allen Apps kompatibel, die die [React Native New Architecture](https://reactnative.dev/docs/the-new-architecture/landing-page) ab SDK Version 2.0.1+ verwenden.

Ab SDK Version 6.0.0 wurde Braze intern auf ein React Native Turbo-Modul upgegradet, das weiterhin entweder mit der New Architecture oder der Legacy Bridge Architektur verwendet werden kann. Da das Turbo-Modul abwärtskompatibel ist, sind außer den im [Changelog](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) erwähnten Änderungen und der Verwendung von React Native v0.70+ keine weiteren Migrationsschritte erforderlich.

{% alert warning %}
Wenn Ihre iOS-App mit `RCTAppDelegate` konform ist und unserem früheren `AppDelegate` Setup in dieser Dokumentation oder im Braze-Beispielprojekt gefolgt ist, stellen Sie sicher, dass Sie auf die Beispiele im [vollständigen nativen Setup](#step-2-complete-native-setup) verweisen, um Abstürze beim Abonnieren von Ereignissen im Turbo-Modul zu vermeiden.
{% endalert %}

## Schritt 1: Braze-Bibliothek integrieren

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

## Schritt 2: Native Einrichtung abschließen

{% tabs %}
{% tab Expo %}

#### Schritt 2.1: Installieren Sie das Braze Expo Plugin

Stellen Sie sicher, dass Sie mindestens Version 1.37.0 des Braze React Native SDK verwenden. Dann installieren Sie das Braze Expo Plugin.

```bash
expo install @braze/expo-plugin
```

#### Schritt 2.2: Plugin zu app.json hinzufügen

Fügen Sie in Ihrem `app.json` das Braze Expo Plugin hinzu. Sie können die folgenden Konfigurationsoptionen angeben:

| Methode                                        | Typ    | Beschreibung                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | String  | Erforderlich. Der [API-Schlüssel]({{site.baseurl}}/api/identifier_types/) für Ihre Android-Anwendung, den Sie in Ihrem Braze Dashboard unter **Einstellungen verwalten** finden. |
| `iosApiKey`                                   | String  | Erforderlich. Der [API-Schlüssel]({{site.baseurl}}/api/identifier_types/) für Ihre iOS-Anwendung, den Sie in Ihrem Braze Dashboard unter **Einstellungen verwalten** finden.     |
| `baseUrl`                                     | String  | Erforderlich. Der [SDK-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) für Ihre Anwendung. Er befindet sich im Braze-Dashboard unter **Einstellungen verwalten**.    |
| `enableBrazeIosPush`                          | boolean | Nur iOS. Ob Sie Braze zur Verwaltung von Push-Benachrichtigungen unter iOS verwenden möchten. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Nur für Android. Ob Sie Firebase Cloud Messaging für Push-Benachrichtigungen verwenden möchten. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | String  | Nur für Android. Ihre Sender-ID für Firebase Cloud Messaging. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | Ganzzahl | Der Braze-Session-Timeout für Ihre Anwendung in Sekunden.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Ob die [SDK-Authentifizierungsfunktion](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication) aktiviert werden soll.      |
| `logLevel`                                    | Ganzzahl | Die Protokollstufe für Ihre Anwendung. Die Standard-Protokollstufe ist 8\. Sie protokolliert nur minimale Informationen. Um die ausführliche Verbose-Protokollierung zum Debuggen zu aktivieren, verwenden Sie die Protokollstufe 0.    |
| `minimumTriggerIntervalInSeconds`             | Ganzzahl | Das minimale Zeitintervall in Sekunden zwischen den Triggern. Die Standardeinstellung ist 30 Sekunden.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Ob die automatische Standorterfassung aktiviert ist (wenn der Benutzer dies erlaubt).                                                                                  |
| `enableGeofence`                              | boolean | Ob Geofences aktiviert sind.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Ob Geofence-Anfragen automatisch gestellt werden sollen.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Nur iOS. Ob eine modale In-App-Nachricht ausgeblendet wird, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht klickt.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Nur für Android. Ob Push-Deeplinks automatisch vom Braze SDK verarbeitet werden sollen.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Nur für Android. Legt fest, ob der Textinhalt in einer Push-Benachrichtigung mit `android.text.Html.fromHtml` als HTML interpretiert und gerendert werden soll.        |
| `androidNotificationAccentColor`              | String  | Nur für Android. Legt die Akzentfarbe für Android-Benachrichtigungen fest.                                                                                                |
| `androidNotificationLargeIcon`                | String  | Nur für Android. Legt das große Android-Benachrichtigungssymbol fest.                                                                                                  |
| `androidNotificationSmallIcon`                | String  | Nur für Android. Legt das kleine Android-Benachrichtigungssymbol fest.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Nur iOS. Ob der Benutzer beim Start der App automatisch nach Push-Berechtigungen gefragt werden soll.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Nur iOS. Ob Sie Rich-Push-Funktionen für iOS aktivieren möchten.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Nur iOS. Ob Sie Braze Push Stories für iOS aktivieren möchten.                                                                                                  |
| `iosPushStoryAppGroup`                        | String  | Nur iOS. Die App-Gruppe, die für iOS Push Stories verwendet wird.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Beispielkonfiguration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
        }
      ],
    ]
  }
}
```

#### Schritt 2.3: Erstellen und Ausführen Ihrer Anwendung

Durch das Pre-Building Ihrer Anwendung werden die erforderlichen nativen Dateien generiert, damit das Braze SDK funktioniert.

```bash
expo prebuild
```

Führen Sie Ihre Anwendung wie in den [Expo-Dokumenten](https://docs.expo.dev/workflow/customizing/) beschrieben aus. Hinweis: Wenn Sie Änderungen an den Konfigurationsoptionen vornehmen, müssen Sie ein neues Pre-Build erstellen und Ihre Anwendung erneut ausführen.

{% endtab %}
{% tab Android %}

#### Schritt 2.1: Unser Repository hinzufügen

In Ihrem Top-Level-Projekt `build.gradle` fügen Sie unter `buildscript` > `dependencies` Folgendes hinzu:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Dadurch wird Kotlin zu Ihrem Projekt hinzugefügt.

#### Schritt 2.2: Konfigurieren Sie das Braze SDK

Um eine Verbindung zu Braze-Servern herzustellen, erstellen Sie die Datei `braze.xml` im Ordner `res/values` Ihres Projekts. Fügen Sie den folgenden Code ein und ersetzen Sie den [API-Schlüssel]({{site.baseurl}}/api/identifier_types/) und den [Endpunkt]({{site.baseurl}}/api/basics/#endpoints) durch Ihre Werte:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Fügen Sie die erforderlichen Berechtigungen zu Ihrer Datei `AndroidManifest.xml` hinzu:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Ab Braze SDK Version 12.2.0 können Sie die Bibliothek "android-sdk-location" automatisch einbinden, indem Sie `importBrazeLocationLibrary=true` in der Datei `gradle.properties` festlegen.
{% endalert %}

#### Schritt 2.3: Sitzungs-Tracking implementieren

Die Aufrufe von `openSession()` und `closeSession()` werden automatisch verarbeitet.
Fügen Sie den folgenden Code in die Methode `onCreate()` Ihrer Klasse `MainApplication` ein:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Schritt 2.4: Intent-Updates verarbeiten

Wenn für Hauptaktivität `android:launchMode` auf `singleTask` festgelegt ist, fügen Sie den folgenden Code zur Klasse `MainActivity` hinzu:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Schritt 2.1: (Optional) Konfigurieren Sie Podfile für dynamische XCFrameworks

Um bestimmte Braze-Bibliotheken, wie z. B. BrazeUI, in eine Objective-C++ Datei zu importieren, müssen Sie die Syntax `#import` verwenden. Ab Version 7.4.0 des Braze Swift SDK verfügen die Binärdateien über einen [optionalen Verteilungskanal als dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), die mit dieser Syntax kompatibel sind.

Wenn Sie diesen Verteilungskanal verwenden möchten, müssen Sie die CocoaPods-Quellen in Ihrem Podfile manuell überschreiben. Beziehen Sie sich auf das unten stehende Beispiel und ersetzen Sie `{your-version}` durch die entsprechende Version, die Sie importieren möchten:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### Schritt 2.2: Pods installieren

Da React Native die Bibliotheken automatisch mit der nativen Plattform verknüpft, können Sie das SDK mithilfe von CocoaPods installieren.

Aus dem Stammordner des Projekts:

```bash
# To install using the React Native New Architecture
cd ios && RCT_NEW_ARCH_ENABLED=1 pod install

# To install using the React Native legacy architecture
cd ios && pod install
```

#### Schritt 2.3: Konfigurieren Sie das Braze SDK

{% subtabs local %}
{% subtab SWIFT %}

Importieren Sie das Braze SDK am Anfang der Datei `AppDelegate.swift`:
```swift
import BrazeKit
```

Ersetzen Sie in der Methode `application(_:didFinishLaunchingWithOptions:)` den [API-Schlüssel]({{site.baseurl}}/api/identifier_types/) und den [Endpunkt]({{site.baseurl}}/api/basics/#endpoints) durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mithilfe der Konfiguration und legen Sie eine statische Eigenschaft in `AppDelegate` an, um den Zugriff zu erleichtern:

{% alert note %}
Unser Beispiel geht von einer [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)-Implementierung aus, die eine Reihe von Abstraktionen im React Native-Setup bereitstellt. Wenn Sie ein anderes Setup für Ihre App verwenden, müssen Sie Ihre Implementierung entsprechend anpassen.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Importieren Sie das Braze SDK am Anfang der Datei `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

Ersetzen Sie in der Methode `application:didFinishLaunchingWithOptions:` den [API-Schlüssel]({{site.baseurl}}/api/identifier_types/) und den [Endpunkt]({{site.baseurl}}/api/basics/#endpoints) durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mithilfe der Konfiguration und legen Sie eine statische Eigenschaft in `AppDelegate` an, um den Zugriff zu erleichtern:

{% alert note %}
Unser Beispiel geht von einer [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h)-Implementierung aus, die eine Reihe von Abstraktionen im React Native-Setup bereitstellt. Wenn Sie ein anderes Setup für Ihre App verwenden, müssen Sie Ihre Implementierung entsprechend anpassen.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Schritt 3: Nutzung

Nach der Installation können Sie die Bibliothek mittels `import` in Ihren React Native-Code einbinden:

```javascript
import Braze from "@braze/react-native-sdk";
```

In unserem [Beispielprojekt](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) finden Sie weitere Einzelheiten.

## Testen Sie Ihre grundlegende Integration

An dieser Stelle können Sie die SDK-Integration verifizieren, indem Sie die Sitzungsstatistiken im Dashboard überprüfen. Wenn Sie Ihre Anwendung auf einer der beiden Plattformen ausführen, sollten Sie im Dashboard (im Bereich **Übersicht** ) eine neue Sitzung sehen.

Sie können eine Sitzung für einen bestimmten Nutzer starten, indem Sie den folgenden Code in Ihrer App aufrufen.

```javascript
Braze.changeUser("userId");
```

Sie können zum Beispiel die Nutzer-ID beim Start der App zuweisen:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Sie können dann im Dashboard unter [Benutzersuche]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) mit `some-user-id` nach dem Benutzer suchen. Dort können Sie dann überprüfen, ob Sitzungs- und Gerätedaten protokolliert wurden.


