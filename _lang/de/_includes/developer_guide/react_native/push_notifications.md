{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

### 1. Schritt: Ersteinrichtung abschließen

{% tabs local %}
{% tab Expo %}
#### Voraussetzungen

Bevor Sie Expo für Push-Benachrichtigungen verwenden können, müssen Sie [das Braze Expo Plugin einrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo).

#### Schritt 1.1: Ihre `app.json`-Datei aktualisieren

Aktualisieren Sie als Nächstes Ihre `app.json`-Datei für Android und iOS:

- **Android:** Fügen Sie die Option `enableFirebaseCloudMessaging` hinzu.
- **iOS:** Fügen Sie die Option `enableBrazeIosPush` hinzu.

#### Schritt 1.2: Ihre Google-Absender-ID hinzufügen

Gehen Sie zunächst zur Firebase-Konsole, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i>&nbsp;**Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü „Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die **Absender-ID** in Ihre Zwischenablage.

![Die Seite „Cloud Messaging" des Firebase-Projekts mit hervorgehobener „Sender-ID".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Öffnen Sie als Nächstes die Datei `app.json` Ihres Projekts und setzen Sie die Eigenschaft `firebaseCloudMessagingSenderId` auf die Absender-ID in Ihrer Zwischenablage. Zum Beispiel:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Schritt 1.3: Den Pfad zu Ihrer Google Services JSON hinzufügen

Fügen Sie in der Datei `app.json` Ihres Projekts den Pfad zu Ihrer `google-services.json`-Datei hinzu. Diese Datei wird benötigt, wenn Sie `enableFirebaseCloudMessaging: true` in Ihrer Konfiguration festlegen.

```json
{
  "expo": {
    "android": {
      "googleServicesFile": "PATH_TO_GOOGLE_SERVICES"
    },
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true
        }
      ],
    ]
  }
}
```

Beachten Sie, dass Sie diese Einstellungen anstelle der nativen Einrichtungsanweisungen verwenden müssen, wenn Sie auf zusätzliche Push-Benachrichtigungsbibliotheken wie [Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/) angewiesen sind.
{% endtab %}

{% tab Android Native %}
Wenn Sie das Braze Expo Plugin nicht verwenden oder diese Einstellungen stattdessen nativ konfigurieren möchten, registrieren Sie sich für Push anhand der [Anleitung zur nativen Android-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/).
{% endtab %}

{% tab iOS Native %}
Wenn Sie das Braze Expo Plugin nicht verwenden oder diese Einstellungen stattdessen nativ konfigurieren möchten, registrieren Sie sich für Push, indem Sie die folgenden Schritte aus der [Anleitung zur nativen iOS-Push-Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) befolgen:

#### Schritt 1.1: Push-Berechtigungen anfordern

Wenn Sie nicht vorhaben, Push-Berechtigungen beim Start der App anzufordern, lassen Sie den Aufruf `requestAuthorizationWithOptions:completionHandler:` in Ihrem AppDelegate weg. Fahren Sie dann mit [Schritt 2](#reactnative_step-2-request-push-notifications-permission) fort. Andernfalls folgen Sie der [nativen iOS-Integrationsanleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Schritt 1.2 (optional): Push-Schlüssel migrieren

Wenn Sie zuvor `expo-notifications` zur Verwaltung Ihres Push-Schlüssels verwendet haben, führen Sie `expo fetch:ios:certs` aus dem Stammordner Ihrer Anwendung aus. Dadurch wird Ihr Push-Schlüssel (eine .p8-Datei) heruntergeladen, der dann in das Braze-Dashboard hochgeladen werden kann.
{% endtab %}
{% endtabs %}

### 2. Schritt: Berechtigung für Push-Benachrichtigungen anfordern

Verwenden Sie die Methode `Braze.requestPushPermission()` (verfügbar ab v1.38.0), um die Berechtigung für Push-Benachrichtigungen von Nutzer:innen unter iOS und Android 13+ anzufordern. Bei Android 12 und älter hat diese Methode keine Auswirkung.

Diese Methode erwartet einen erforderlichen Parameter, der angibt, welche Berechtigungen das SDK unter iOS von den Nutzer:innen anfordern soll. Diese Optionen haben keine Auswirkungen auf Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Schritt 2.1: Auf Push-Benachrichtigungen lauschen (optional)

Sie können zusätzlich Ereignisse abonnieren, bei denen Braze eine eingehende Push-Benachrichtigung erkannt und verarbeitet hat. Verwenden Sie den Listener-Schlüssel `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Empfangene iOS-Push-Events werden nur für Benachrichtigungen im Vordergrund sowie für Hintergrundbenachrichtigungen mit `content-available` getriggert. Für Benachrichtigungen, die im beendeten Zustand empfangen werden, oder für Hintergrundbenachrichtigungen ohne das Feld `content-available` werden sie nicht getriggert.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Ereignisfelder für Push-Benachrichtigungen

Eine vollständige Liste der Felder für Push-Benachrichtigungen finden Sie in der folgenden Tabelle:

| Feldname         | Typ      | Beschreibung |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Gibt den Nutzlasttyp der Benachrichtigung an. Die beiden Werte, die vom Braze React Native SDK gesendet werden, sind `push_opened` und `push_received`. |
| `url`              | String    | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `use_webview`      | Boolescher Wert   | Wenn `true`, wird die URL in der App in einer modalen Webansicht geöffnet. Wenn `false`, wird die URL im Browser des Geräts geöffnet. |
| `title`            | String    | Stellt den Titel der Benachrichtigung dar. |
| `body`             | String    | Stellt den Textkörper oder Inhalt der Benachrichtigung dar. |
| `summary_text`     | String    | Stellt den zusammenfassenden Text der Benachrichtigung dar. Dieser wird unter iOS aus `subtitle` zugeordnet. |
| `badge_count`      | Zahl   | Stellt die Badge-Anzahl der Benachrichtigung dar. |
| `timestamp`        | Zahl | Stellt den Zeitpunkt dar, zu dem die Nutzlast von der Anwendung empfangen wurde. |
| `is_silent`        | Boolescher Wert   | Wenn `true`, wird die Nutzlast still empfangen. Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter Android finden Sie unter [Stille Push-Benachrichtigungen unter Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter iOS finden Sie unter [Stille Push-Benachrichtigungen unter iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Boolescher Wert   | Dies ist `true`, wenn eine Benachrichtigungsnutzlast für eine interne SDK-Funktion gesendet wurde, wie z. B. die Synchronisierung von Geofences, die Synchronisierung von Feature-Flags oder das Uninstall-Tracking. Die Nutzlast wird für die Nutzer:innen unbemerkt empfangen. |
| `image_url`        | String    | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `braze_properties` | Objekt    | Stellt die mit der Kampagne verbundenen Braze-Eigenschaften dar (Schlüssel-Wert-Paare). |
| `ios`              | Objekt    | Stellt iOS-spezifische Felder dar. |
| `android`          | Objekt    | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 3. Schritt: Deeplinking aktivieren (optional)

Um Braze in die Lage zu versetzen, Deeplinks innerhalb von React-Komponenten zu verarbeiten, wenn auf eine Push-Benachrichtigung geklickt wird, implementieren Sie zunächst die Schritte, die in der Bibliothek [React Native Linking](https://reactnative.dev/docs/linking) beschrieben sind, oder verwenden Sie die Lösung Ihrer Wahl. Folgen Sie dann den weiteren Schritten unten.

Weitere Informationen zu Deeplinks finden Sie in unserem [FAQ-Artikel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android Native %}
Wenn Sie das [Braze Expo Plugin]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option) verwenden, können Sie Push-Benachrichtigungs-Deeplinks automatisch verarbeiten, indem Sie `androidHandlePushDeepLinksAutomatically` in Ihrer `app.json` auf `true` setzen.

Um Deeplinks stattdessen manuell zu verarbeiten, lesen Sie die native Android-Dokumentation: [Deeplinks hinzufügen]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

#### Schritt 3.1: Push-Benachrichtigungs-Nutzlast beim App-Start speichern

{% alert note %}
Dies wird ab React Native SDK 19.1.0 unterstützt.
{% endalert %}

Fügen Sie `populateInitialPushPayloadFromIntent` zur Methode `onCreate()` Ihrer Hauptaktivität hinzu. Dies muss vor der Initialisierung von React Native aufgerufen werden, um die ursprünglichen Intent-Daten zu erfassen. Zum Beispiel:

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
  BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
  super.onCreate(savedInstanceState)
}
```

#### Schritt 3.2: Deeplinks aus einem geschlossenen Zustand heraus behandeln

Zusätzlich zu den Basisszenarien, die von [React Native Linking](https://reactnative.dev/docs/linking) behandelt werden, implementieren Sie die Methode `Braze.getInitialPushPayload` und rufen den Wert `url` ab, um Deeplinks von Push-Benachrichtigungen zu berücksichtigen, die Ihre App öffnen, wenn sie nicht läuft. Zum Beispiel:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Für diese Methode ist die native Einrichtung in Schritt 3.1 für Ihre Plattform erforderlich. Wenn Sie das Braze Expo Plugin verwenden, wird dies möglicherweise automatisch abgewickelt.
{% endalert %}

{% endtab %}
{% tab iOS Native %}

{% alert important %}
Um Deeplinks aus Push-Benachrichtigungen unter iOS zu verarbeiten, müssen Sie auch die Link-Verarbeitung in Ihrer nativen iOS-Schicht konfigurieren.
{% endalert %}

Dazu gehört die Registrierung eines benutzerdefinierten URL-Schemas und die Implementierung eines URL-Handlers in Ihrem `AppDelegate`. Eine vollständige Einrichtungsanleitung finden Sie unter [Deeplinks verarbeiten]({{site.baseurl}}/developer_guide/platforms/swift/in_app_messages/deep_linking/?tab=objective-c) in der nativen iOS-Dokumentation.
#### Schritt 3.1: Push-Benachrichtigungs-Nutzlast beim App-Start speichern
{% alert note %}
Überspringen Sie Schritt 3.1, wenn Sie das Braze Expo Plugin verwenden, da diese Funktionalität automatisch abgewickelt wird.
{% endalert %}

Fügen Sie für iOS `populateInitialPayloadFromLaunchOptions` zur Methode `didFinishLaunchingWithOptions` des AppDelegate hinzu. Zum Beispiel:

{% subtabs local %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // ... Perform regular React Native setup

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```
{% endsubtab %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
) -> Bool {
  // ... Perform regular React Native setup

  let configuration = Braze.Configuration(apiKey: apiKey, endpoint: endpoint)
  configuration.triggerMinimumTimeInterval = 1
  configuration.logger.level = .info
  let braze = BrazeReactBridge.initBraze(configuration)
  AppDelegate.braze = braze
  registerForPushNotifications()
  BrazeReactUtils.shared().populateInitialPayload(fromLaunchOptions: launchOptions)

  return super.application(application, didFinishLaunchingWithOptions: launchOptions)
}
```
{% endsubtab %}
{% endsubtabs %}

#### Schritt 3.2: Deeplinks aus einem geschlossenen Zustand heraus behandeln

Zusätzlich zu den Basisszenarien, die von [React Native Linking](https://reactnative.dev/docs/linking) behandelt werden, implementieren Sie die Methode `Braze.getInitialPushPayload` und rufen den Wert `url` ab, um Deeplinks von Push-Benachrichtigungen zu berücksichtigen, die Ihre App öffnen, wenn sie nicht läuft. Zum Beispiel:

```javascript
// Handles deep links when an app is launched from a hard close via push click.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Für diese Methode ist die native Einrichtung in Schritt 3.1 für Ihre Plattform erforderlich. Wenn Sie das Braze Expo Plugin verwenden, wird dies möglicherweise automatisch abgewickelt.
{% endalert %}

#### Schritt 3.3: Universal Links aktivieren (optional)

Um die Unterstützung für [Universal Links]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links) zu aktivieren, implementieren Sie einen Braze-Delegaten, der festlegt, ob eine bestimmte URL geöffnet werden soll, und registrieren Sie diesen anschließend bei Ihrer Braze-Instanz.

{% subtabs local %}
{% subtab Swift %}
Erstellen Sie eine `BrazeReactDelegate.swift`-Datei in Ihrem `iOS`-Verzeichnis und fügen Sie Folgendes hinzu. Ersetzen Sie `YOUR_DOMAIN_HOST` durch Ihre tatsächliche Domain.

```swift
import Foundation
import BrazeKit
import UIKit

class BrazeReactDelegate: NSObject, BrazeDelegate {

  /// This delegate method determines whether to open a given URL.
  /// Reference the context to get additional details about the URL payload.
  func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
    if let host = context.url.host,
       host.caseInsensitiveCompare("YOUR_DOMAIN_HOST") == .orderedSame {
      // Sample custom handling of universal links
      let application = UIApplication.shared
      let userActivity = NSUserActivity(activityType: NSUserActivityTypeBrowsingWeb)
      userActivity.webpageURL = context.url
      // Routes to the `continueUserActivity` method, which should be handled in your AppDelegate.
      application.delegate?.application?(
        application,
        continue: userActivity,
        restorationHandler: { _ in }
      )
      return false
    }
    // Let Braze handle links otherwise
    return true
  }
}
```

Erstellen und registrieren Sie dann Ihr `BrazeReactDelegate` in `didFinishLaunchingWithOptions` der Datei `AppDelegate.swift` Ihres Projekts.

```swift
import BrazeKit

class AppDelegate: UIResponder, UIApplicationDelegate {
  
  static var braze: Braze?
  
  // Keep a strong reference to the BrazeDelegate so it is not deallocated.
  private var brazeDelegate: BrazeReactDelegate?
  
  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Other setup code (e.g., Braze initialization)
    
    brazeDelegate = BrazeReactDelegate()
    AppDelegate.braze?.delegate = brazeDelegate
    return true
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
Erstellen Sie eine `BrazeReactDelegate.h`-Datei in Ihrem `iOS`-Verzeichnis und fügen Sie anschließend das folgende Snippet hinzu.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Erstellen Sie als Nächstes eine Datei `BrazeReactDelegate.m` und fügen Sie das folgende Code-Snippet ein. Ersetzen Sie `YOUR_DOMAIN_HOST` durch Ihre tatsächliche Domain.

```objc
#import "BrazeReactDelegate.h"
#import <UIKit/UIKit.h>

@implementation BrazeReactDelegate

/// This delegate method determines whether to open a given URL.
///
/// Reference the `BRZURLContext` object to get additional details about the URL payload.
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"YOUR_DOMAIN_HOST"]) {
    // Sample custom handling of universal links
    UIApplication *application = UIApplication.sharedApplication;
    NSUserActivity* userActivity = [[NSUserActivity alloc] initWithActivityType:NSUserActivityTypeBrowsingWeb];
    userActivity.webpageURL = context.url;
    // Routes to the `continueUserActivity` method, which should be handled in your `AppDelegate`.
    [application.delegate application:application
                 continueUserActivity:userActivity restorationHandler:^(NSArray<id<UIUserActivityRestoring>> * _Nullable restorableObjects) {}];
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}

@end
```

Erstellen und registrieren Sie dann Ihr `BrazeReactDelegate` in `didFinishLaunchingWithOptions` der Datei `AppDelegate.m` Ihres Projekts.

```objc
#import "BrazeReactUtils.h"
#import "BrazeReactDelegate.h"

@interface AppDelegate ()

// Keep a strong reference to the BrazeDelegate to ensure it is not deallocated.
@property (nonatomic, strong) BrazeReactDelegate *brazeDelegate;

@end

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  // Other setup code

  self.brazeDelegate = [[BrazeReactDelegate alloc] init];
  braze.delegate = self.brazeDelegate;
}
```
{% endsubtab %}
{% endsubtabs %}

Eine beispielhafte Integration finden Sie in unserer Beispiel-App [hier](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### 4. Schritt: Vordergrundbenachrichtigungen behandeln

Die Behandlung von Benachrichtigungen im Vordergrund funktioniert je nach Plattform und Konfiguration unterschiedlich. Wählen Sie den Ansatz, der zu Ihrer Integration passt:

{% tabs local %}
{% tab iOS %}
Für iOS entspricht die Verarbeitung von Vordergrundbenachrichtigungen der nativen Swift-Integration. Rufen Sie `handleForegroundNotification(notification:)` innerhalb Ihrer `UNUserNotificationCenterDelegate.userNotificationCenter(_:willPresent:withCompletionHandler:)`-Implementierung auf.

Ausführliche Informationen und Code-Beispiele finden Sie unter [Vordergrundbenachrichtigungen behandeln]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#handling-foreground-notifications) in der Dokumentation zu Swift-Push-Benachrichtigungen.
{% endtab %}

{% tab Android %}
Bei Android entspricht die Verarbeitung von Vordergrundbenachrichtigungen der nativen Android-Integration. Rufen Sie `BrazeFirebaseMessagingService.handleBrazeRemoteMessage` innerhalb Ihrer `FirebaseMessagingService.onMessageReceived`-Methode auf.

Ausführliche Informationen und Code-Beispiele finden Sie unter [Vordergrundbenachrichtigungen behandeln]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) in der Dokumentation zu Android-Push-Benachrichtigungen.
{% endtab %}

{% tab Expo %}
Im von Expo verwalteten Workflow rufen Sie native Benachrichtigungs-Handler nicht direkt auf. Verwenden Sie stattdessen die Expo Notifications API, um die Vordergrunddarstellung zu steuern, während das Braze Expo Plugin die native Verarbeitung automatisch übernimmt.

```javascript
import * as Notifications from 'expo-notifications';
import Braze from '@braze/react-native-sdk';

// Control foreground presentation in Expo
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,    // Show alert while in foreground
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// React to Braze push events
const subscription = Braze.addListener('pushNotificationEvent', (event) => {
  console.log('Braze push event', {
    type: event.payload_type,   // "push_received" | "push_opened"
    title: event.title,
    url: event.url,
    is_silent: event.is_silent,
  });
  // Handle deep links, custom behavior, etc.
});

// Handle initial payload when app launches via push
Braze.getInitialPushPayload((payload) => {
  if (payload) {
    console.log('Initial push payload', payload);
  }
});
```

{% alert note %}
Im Expo-verwalteten Workflow übernimmt das Braze Expo Plugin automatisch die native Push-Verarbeitung. Sie steuern die UI im Vordergrund über die oben gezeigten Präsentationsoptionen für Expo-Benachrichtigungen.
{% endalert %}

Für Bare-Workflow-Integrationen verwenden Sie stattdessen die nativen Ansätze für iOS und Android.
{% endtab %}
{% endtabs %}

### 5. Schritt: Test-Push-Benachrichtigung senden

Sie sollten nun in der Lage sein, Benachrichtigungen an die Geräte zu senden. Führen Sie die folgenden Schritte durch, um Ihre Push-Integration zu testen.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten iOS-Push-Benachrichtigungen mithilfe eines Simulators für iOS 16+ testen, der unter Xcode 14 oder höher läuft. Weitere Einzelheiten finden Sie in den [Release Notes zu Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Setzen Sie eine:n aktive:n Nutzer:in in der React Native-Anwendung, indem Sie die Methode `Braze.changeUserId('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und erstellen Sie eine neue Push-Benachrichtigungskampagne. Wählen Sie die Plattformen aus, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und wechseln Sie zum Tab **Test**. Fügen Sie dieselbe `user-id` als Testnutzer:in hinzu und klicken Sie auf **Test senden**. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten.

![Eine Braze-Push-Kampagne, die zeigt, wie Sie Ihre eigene Nutzer-ID als Testempfänger:in hinzufügen können, um Ihre Push-Benachrichtigung zu testen.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Verwendung des Expo-Plugins

Nachdem Sie [Push-Benachrichtigungen für Expo eingerichtet haben](#reactnative_setting-up-push-notifications), können Sie damit die folgenden Verhaltensweisen für Push-Benachrichtigungen verarbeiten&#8212;ohne Code in den nativen Android- oder iOS-Schichten schreiben zu müssen.

### Weiterleitung von Android-Push an zusätzliche FMS

Wenn Sie einen zusätzlichen Firebase Messaging Service (FMS) verwenden möchten, können Sie einen Fallback-FMS angeben, der aufgerufen wird, wenn Ihre Anwendung einen Push erhält, der nicht von Braze stammt. Zum Beispiel:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "androidFirebaseMessagingFallbackServiceEnabled": true,
          "androidFirebaseMessagingFallbackServiceClasspath": "com.company.OurFirebaseMessagingService"
        }
      ]
    ]
  }
}
```

### Verwendung von App-Erweiterungen mit Expo Application Services {#app-extensions}

Wenn Sie Expo Application Services (EAS) verwenden und `enableBrazeIosRichPush` oder `enableBrazeIosPushStories` aktiviert haben, müssen Sie die entsprechenden Bundle-Bezeichner für jede App-Erweiterung in Ihrem Projekt deklarieren. Es gibt mehrere Möglichkeiten für diesen Schritt, abhängig davon, wie Ihr Projekt für die Verwaltung der Codesignierung mit EAS konfiguriert ist.

Eine Möglichkeit besteht darin, die Konfiguration `appExtensions` in der Datei `app.json` zu verwenden. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu App-Erweiterungen](https://docs.expo.dev/build-reference/app-extensions/). Alternativ können Sie die Einstellung `multitarget` in der Datei `credentials.json` einrichten. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu lokalen Zugangsdaten](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project).

### Fehlerbehebung

Dies sind allgemeine Schritte zur Fehlerbehebung für die Integration von Push-Benachrichtigungen mit dem Braze React Native SDK und dem Expo-Plugin.

#### Push-Benachrichtigungen funktionieren nicht mehr {#troubleshooting-stopped-working}

Sollten Push-Benachrichtigungen über das Expo-Plugin nicht mehr funktionieren:

1. Überprüfen Sie, ob das Braze SDK weiterhin Sitzungen trackt.
2. Überprüfen Sie, ob das SDK nicht durch einen expliziten oder impliziten Aufruf von `wipeData` deaktiviert wurde.
3. Überprüfen Sie alle kürzlich durchgeführten Upgrades von Expo oder den zugehörigen Bibliotheken, da es zu Konflikten mit Ihrer Braze-Konfiguration kommen könnte.
4. Überprüfen Sie kürzlich hinzugefügte Projektabhängigkeiten und stellen Sie sicher, dass diese Ihre bestehenden Delegate-Methoden für Push-Benachrichtigungen nicht manuell überschreiben.

{% alert tip %}
Für iOS-Integrationen können Sie auch unser [Tutorial zur Einrichtung von Push-Benachrichtigungen](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) heranziehen, um mögliche Konflikte mit Ihren Projektabhängigkeiten zu identifizieren.
{% endalert %}

#### Das Geräte-Token wird nicht bei Braze registriert {#troubleshooting-token-registration}

Sollte Ihr Geräte-Token nicht bei Braze registriert werden, überprüfen Sie zunächst, ob [Push-Benachrichtigungen nicht mehr funktionieren](#troubleshooting-stopped-working).

Sollte das Problem weiterhin bestehen, besteht die Möglichkeit, dass eine separate Abhängigkeit die Konfiguration Ihrer Braze-Push-Benachrichtigungen beeinträchtigt. Sie können versuchen, diese zu entfernen oder stattdessen manuell `Braze.registerPushToken` aufzurufen.