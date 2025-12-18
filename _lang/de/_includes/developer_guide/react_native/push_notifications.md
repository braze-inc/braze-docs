{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

### Schritt 1: Vervollständigen Sie die Ersteinrichtung

{% tabs local %}
{% tab Expo %}
#### Voraussetzungen

Bevor Sie Expo für Push-Benachrichtigungen verwenden können, müssen Sie [das Braze Expo Plugin]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/sdk_integration/?tab=expo) einrichten.

#### Schritt 1.1: Aktualisieren Sie Ihre `app.json` Datei

Als nächstes aktualisieren Sie Ihre `app.json` Datei für Android und iOS:

- **Android:** Fügen Sie die Option `enableFirebaseCloudMessaging` hinzu.
- **iOS:** Fügen Sie die Option `enableBrazeIosPush` hinzu.

#### Schritt 1.2: Fügen Sie Ihre Google Absender-ID hinzu

Gehen Sie zunächst zur Firebase-Konsole, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i> **Einstellungen** > **Projekteinstellungen**.

![Das Firebase-Projekt mit geöffnetem Menü "Einstellungen".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die **Absender-ID** in Ihre Zwischenablage.

![Die Seite "Cloud Messaging" des Firebase-Projekts mit hervorgehobener "Sender-ID".]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

Als nächstes öffnen Sie die Datei `app.json` Ihres Projekts und setzen die Eigenschaft `firebaseCloudMessagingSenderId` auf die Absender-ID in Ihrer Zwischenablage. Zum Beispiel:

```
"firebaseCloudMessagingSenderId": "693679403398"
```

#### Schritt 1.3: Fügen Sie den Pfad zu Ihrem Google Services JSON hinzu

Fügen Sie in der Datei `app.json` Ihres Projekts den Pfad zu Ihrer Datei `google-services.json` hinzu. Diese Datei wird benötigt, wenn Sie `enableFirebaseCloudMessaging: true` in Ihrer Konfiguration festlegen.

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

{% tab Android nativ %}
Wenn Sie das Braze Expo Plugin nicht verwenden oder diese Einstellungen stattdessen nativ konfigurieren möchten, registrieren Sie sich für Push, indem Sie auf die [Anleitung zur nativen Android Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/) referenzieren.
{% endtab %}

{% tab iOS Nativ %}
Wenn Sie das Braze Expo Plugin nicht verwenden oder diese Einstellungen stattdessen nativ konfigurieren möchten, registrieren Sie sich für Push, indem Sie die folgenden Schritte aus der [Anleitung zur nativen iOS Push Integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) referenzieren:

#### Schritt 1.1: Anfrage für Push-Berechtigungen

Wenn Sie nicht vorhaben, Push-Berechtigungen beim Start der App anzufordern, lassen Sie den Aufruf `requestAuthorizationWithOptions:completionHandler:` in Ihrem AppDelegate weg. Fahren Sie dann mit [Schritt 2](#reactnative_step-2-request-push-notifications-permission) fort. Andernfalls folgen Sie der [nativen iOS-Integrationsanleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

#### Schritt 1.2 (optional): Push-Schlüssel migrieren

Wenn Sie zuvor `expo-notifications` zur Verwaltung Ihres Push-Schlüssels verwendet haben, führen Sie `expo fetch:ios:certs` aus dem Stammordner Ihrer Anwendung aus. Dadurch wird Ihr Push-Schlüssel (eine .p8-Datei) heruntergeladen, die Sie dann auf das Braze-Dashboard hochladen können.
{% endtab %}
{% endtabs %}

### Schritt 2: Genehmigung für Push-Benachrichtigungen anfordern

Verwenden Sie die Methode `Braze.requestPushPermission()` (verfügbar ab v1.38.0), um die Berechtigung für Push-Benachrichtigungen von iOS- und Android 13+-Nutzern anzufordern. Bei Android 12 und früheren Versionen ist diese Methode nicht anwendbar.

Diese Methode nimmt einen erforderlichen Parameter auf, der angibt, welche Berechtigungen das SDK vom iOS-Nutzer anfordern soll. Diese Optionen haben keine Auswirkungen auf Android.

```javascript
const permissionOptions = {
  alert: true,
  sound: true,
  badge: true,
  provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

#### Schritt 2.1: Auf Push-Benachrichtigungen warten (optional)

Sie können zusätzlich Ereignisse abonnieren, bei denen Braze eine eingehende Push-Benachrichtigung erkannt und verarbeitet hat. Verwenden Sie den Listener-Schlüssel `Braze.Events.PUSH_NOTIFICATION_EVENT`.

{% alert important %}
Empfangene iOS-Push-Events werden nur für Benachrichtigungen im Vordergrund sowie für Benachrichtigungen im Hintergrund mit `content-available` getriggert. Für Benachrichtigungen, die während der Beendigung empfangen werden, oder für Benachrichtigungen im Hintergrund ohne das Feld `content-available` werden sie nicht getriggert.
{% endalert %}

```javascript
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
  console.log(`Push Notification event of type ${data.payload_type} seen. Title ${data.title}\n and deeplink ${data.url}`);
  console.log(JSON.stringify(data, undefined, 2));
});
```

##### Ereignisfelder für Push-Benachrichtigungen

Eine vollständige Liste der Felder für Push-Benachrichtigungen finden Sie in der unten stehenden Tabelle:

| Feldname         | Typ      | Beschreibung |
| ------------------ | --------- | ----------- |
| `payload_type`     | String    | Gibt den Nutzlasttyp der Benachrichtigung an. Die beiden Werte, die vom Braze React Native-SDK gesendet werden, sind `push_opened` und `push_received`. |
| `url`              | String    | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `use_webview`      | Boolesch   | Wenn Sie `true` wählen, wird die URL in der App in einer modalen Webansicht geöffnet. Wenn Sie `false` wählen, wird die URL im Browser des Geräts geöffnet. |
| `title`            | String    | Stellt den Titel der Benachrichtigung dar. |
| `body`             | String    | Stellt den Textkörper oder Inhalt der Benachrichtigung dar. |
| `summary_text`     | String    | Stellt den zusammenfassenden Text der Benachrichtigung dar. Dieser wird von `subtitle` unter iOS zugeordnet. |
| `badge_count`      | Zahl   | Stellt die Anzahl der Ausweise in der Benachrichtigung dar. |
| `timestamp`        | Zahl | Stellt den Zeitpunkt dar, zu dem die Nutzdaten von der Anwendung empfangen wurden. |
| `is_silent`        | Boolesch   | Wenn Sie `true` auswählen, wird die Nutzlast still empfangen. Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter Android finden Sie unter [Stille Push-Benachrichtigungen unter Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Einzelheiten zum Senden von stillen Push-Benachrichtigungen unter iOS finden Sie unter [Stille Push-Benachrichtigungen unter iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `is_braze_internal`| Boolesch   | Dies ist `true`, wenn eine Benachrichtigungsnutzlast für eine interne SDK-Funktion gesendet wurde, wie z. B. die Synchronisierung von Geofences, die Synchronisierung von Feature-Flags oder das Uninstall-Tracking. Die Nutzdaten werden für den Benutzer unbemerkt empfangen. |
| `image_url`        | String    | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `braze_properties` | Objekt    | Stellt die mit der Kampagne verbundenen Braze-Eigenschaften dar (Schlüssel-Wert-Paare). |
| `ios`              | Objekt    | Stellt iOS-spezifische Felder dar. |
| `android`          | Objekt    | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 3: Deeplinking aktivieren (optional)

Um Braze in die Lage zu versetzen, Deeplinks innerhalb von React-Komponenten zu verarbeiten, wenn auf eine Push-Benachrichtigung geklickt wird, implementieren Sie zunächst die Schritte, die in der Bibliothek [React Native Linking](https://reactnative.dev/docs/linking) beschrieben sind, oder mit der Lösung Ihrer Wahl. Folgen Sie dann den weiteren Schritten unten.

Weitere Informationen zu Deeplinks finden Sie in unserem [FAQ-Artikel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

{% tabs local %}
{% tab Android nativ %}
Wenn Sie das [Braze Expo Plugin]({{site.baseurl}}/developer_guide/platforms/react_native/sdk_integration/?tab=expo#step-2-choose-a-setup-option) verwenden, können Sie Push-Benachrichtigungen mit Deeplinks automatisch verarbeiten, indem Sie `androidHandlePushDeepLinksAutomatically` auf `true` in Ihrem `app.json` setzen.

Um Deeplinks manuell zu setzen, lesen Sie bitte die Dokumentation für Android: [Hinzufügen von Deeplinks]({{site.baseurl}}/developer_guide/push_notifications/deep_linking).

{% endtab %}
{% tab iOS Nativ %}
#### Schritt 3.1: Speichern Sie die Push-Benachrichtigung beim Start der App
{% alert note %}
Überspringen Sie Schritt 3.1, wenn Sie das Braze Expo Plugin verwenden, da diese Funktion automatisch ausgeführt wird.
{% endalert %}

Fügen Sie für iOS `populateInitialPayloadFromLaunchOptions` zur Methode `didFinishLaunchingWithOptions` des AppDelegate hinzu. Zum Beispiel:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

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

#### Schritt 3.2: Deeplinks aus einem geschlossenen Zustand heraus behandeln

Zusätzlich zu den Basisszenarien, die von [React Native Linking](https://reactnative.dev/docs/linking) behandelt werden, implementieren Sie die Methode `Braze.getInitialPushPayload` und rufen den Wert `url` ab, um Deeplinks von Push-Benachrichtigungen zu berücksichtigen, die Ihre App öffnen, wenn sie nicht läuft. Zum Beispiel:

```javascript
// Handles deep links when an iOS app is launched from a hard close via push click.
// This edge case is not handled in the React Native Linking library and is provided as a workaround by Braze.
Braze.getInitialPushPayload(pushPayload => {
  if (pushPayload) {
    console.log('Braze.getInitialPushPayload is ' + pushPayload);
    showToast('Initial URL is ' + pushPayload.url);
    handleOpenUrl({ pushPayload.url });
  }
});
```
{% alert note %}
Braze bietet diese Problemumgehung an, da die Linking-API von React Native dieses Szenario aufgrund einer Race-Condition beim Starten der App nicht unterstützt.
{% endalert %}

#### Schritt 3.3 Aktivieren Sie Universal Links (optional)

Um die Unterstützung von [Universal Linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#universal-links) zu aktivieren, erstellen Sie eine Datei `BrazeReactDelegate.h` in Ihrem Verzeichnis `iOS` und fügen Sie den folgenden Code-Snippet hinzu.

```objc
#import <Foundation/Foundation.h>
#import <BrazeKit/BrazeKit-Swift.h>

@interface BrazeReactDelegate: NSObject<BrazeDelegate>

@end
```

Als nächstes erstellen Sie eine Datei `BrazeReactDelegate.m` und fügen den folgenden Code Snippet ein. Ersetzen Sie `YOUR_DOMAIN_HOST` durch Ihre tatsächliche Domain.

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

Für eine beispielhafte Integration referenzieren Sie unsere App [hier](https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm).
{% endtab %}
{% endtabs %}

### Schritt 4: Senden Sie eine Push-Benachrichtigung zum Test

Sie sollten nun in der Lage sein, Benachrichtigungen an die Geräte zu senden. Führen Sie die folgenden Schritte durch, um Ihre Push-Integration zu testen.

{% alert note %}
Ab macOS 13 können Sie auf bestimmten Geräten iOS Push-Benachrichtigungen mithilfe eines Simulators für iOS 16+ testen, der unter Xcode 14 oder höher läuft. Weitere Einzelheiten finden Sie in den [Release Notes zu Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

1. Setzen Sie einen aktiven Nutzer:innen in der React Native-Anwendung, indem Sie die Methode `Braze.changeUserId('your-user-id')` aufrufen.
2. Gehen Sie zu **Kampagnen** und erstellen Sie eine neue Push-Benachrichtigungskampagne. Wählen Sie die Plattformen, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und gehen Sie auf die Registerkarte **Test**. Fügen Sie die gleiche `user-id` wie der Testbenutzer hinzu und klicken Sie auf **Test senden**. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten.

![Eine Push-Kampagne von Braze, bei der Sie Ihre eigene Benutzer-ID als Testempfänger hinzufügen können, um Ihre Push-Benachrichtigung zu testen.]({% image_buster /assets/img/react-native/push-notification-test.png %} "Push Campaign Test")

## Verwendung des Expo-Plugins

Nachdem Sie [Push-Benachrichtigungen für Expo eingerichtet haben](#reactnative_setting-up-push-notifications), können Sie damit die folgenden Verhaltensweisen für Push-Benachrichtigungen verarbeiten - ohne dass Sie Code in den nativen Android- oder iOS-Schichten schreiben müssen.

### Weiterleitung von Android Push an zusätzliche FMS

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

Wenn Sie Expo Application Services (EAS) verwenden und `enableBrazeIosRichPush` oder `enableBrazeIosPushStories` aktiviert haben, müssen Sie die entsprechenden Bundle-Bezeichner für jede App-Erweiterung in Ihrem Projekt deklarieren. Es gibt mehrere Möglichkeiten für diesen Schritt. Diese hängen von der Konfiguration Ihres Projekt für die Verwaltung der Codesignierung mit EAS ab.

Eine Möglichkeit besteht darin, die Konfiguration `appExtensions` in der Datei `app.json` zu verwenden. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu App-Erweiterungen](https://docs.expo.dev/build-reference/app-extensions/). Alternativ können Sie die Einstellung `multitarget` in der Datei `credentials.json` einrichten. Weitere Informationen hierzu finden Sie in der [Expo-Dokumentation zu lokalen Zugangsdaten](https://docs.expo.dev/app-signing/local-credentials/#multi-target-project).

### Fehlersuche

Dies sind allgemeine Fehlerbehebungen für Push-Benachrichtigungen, die mit dem Braze React Native SDK und dem Expo-Plugin integriert sind.

#### Push-Benachrichtigungen funktionieren nicht mehr {#troubleshooting-stopped-working}

Wenn Push-Benachrichtigungen über das Expo-Plugin nicht mehr funktionieren:

1. Vergewissern Sie sich, dass das Braze SDK noch Tracking-Sitzungen durchführt.
2. Prüfen Sie, ob das SDK nicht durch einen expliziten oder impliziten Aufruf von `wipeData` deaktiviert wurde.
3. Überprüfen Sie alle kürzlich durchgeführten Upgrades für Expo oder die zugehörigen Bibliotheken, da es zu Konflikten mit Ihrer Braze-Konfiguration kommen kann.
4. Überprüfen Sie die kürzlich hinzugefügten Projektabhängigkeiten und kontrollieren Sie, ob sie Ihre bestehenden Delegatenmethoden für Push-Benachrichtigungen manuell überschreiben.

{% alert tip %}
Für iOS-Integrationen können Sie auch auf unser [Tutorial zur Einrichtung von Push-Benachrichtigungen](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications) referenzieren, um mögliche Konflikte mit Ihren Projektabhängigkeiten zu erkennen.
{% endalert %}

#### Gerätetoken lässt sich nicht bei Braze registrieren {#troubleshooting-token-registration}

Wenn sich Ihr Gerät Token nicht bei Braze registrieren lässt, lesen Sie zunächst [Push-Benachrichtigungen funktionieren nicht mehr](#troubleshooting-stopped-working).

Wenn Ihr Problem weiterhin besteht, kann es sein, dass eine andere Abhängigkeit Ihre Konfiguration der Push-Benachrichtigung von Braze beeinträchtigt. Sie können versuchen, es zu entfernen oder stattdessen `Braze.registerPushToken` manuell aufrufen.
