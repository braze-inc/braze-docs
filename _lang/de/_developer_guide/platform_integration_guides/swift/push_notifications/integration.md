---
nav_title: Integration
article_title: Push-Integration für iOS
platform: Swift
page_order: 0
description: "Dieser Referenzartikel  beschreibt, wie Sie iOS Push-Benachrichtigungen für das Braze Swift SDK einrichten."
channel:
  - push
  
---

# Integration von Push-Benachrichtigungen

> Dieser Referenzartikel  beschreibt, wie Sie iOS Push-Benachrichtigungen für das Braze Swift SDK einrichten.

[Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) ermöglichen es Ihnen, von Ihrer App aus Benachrichtigungen über wichtige Ereignisse zu versenden. Sie können eine Push-Benachrichtigung senden, wenn Sie neue Nachrichten zugestellt haben, aktuelle Nachrichten senden oder die neueste Folge der Lieblingssendung Ihres Nutzers:innen zum Herunterladen für die Offline-Nutzung bereitstellen. Push-Benachrichtigungen können auch [stumm]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) sein und nur zum Update der Schnittstelle Ihrer App oder zum Triggern von Hintergrundarbeiten verwendet werden. 

Push-Benachrichtigungen eignen sich hervorragend für sporadische, aber unmittelbar wichtige Inhalte, bei denen die Verzögerung zwischen den Abrufen im Hintergrund möglicherweise nicht akzeptabel ist. Push-Benachrichtigungen können auch viel effizienter sein als Hintergrundabrufe, da Ihre Anwendung nur bei Bedarf gestartet wird. 

Push-Benachrichtigungen sind Rate-Limits, also haben Sie keine Angst davor, so viele zu senden, wie Ihre Anwendung benötigt. iOS und die Server des Apple Serviceleistungen; Dienste (APNs) für Push-Benachrichtigungen kontrollieren, wie oft sie zugestellt werden, und Sie werden nicht in Schwierigkeiten kommen, wenn Sie zu viele senden. Wenn Ihre Push-Benachrichtigungen gedrosselt werden, werden sie möglicherweise verzögert, bis das Gerät das nächste Mal ein Keep-Alive-Paket sendet oder eine andere Benachrichtigung erhält.

## Ersteinrichtung

### Schritt 1: Laden Sie das Zertifikat Ihres APNs hoch

Bevor Sie mit Braze eine iOS-Push-Benachrichtigung senden können, müssen Sie Ihre von Apple bereitgestellte `.p8` Push-Benachrichtigungsdatei bereitstellen. Wie in der [Apple-Entwicklerdokumentation](https://developer.apple.com/documentation/usernotifications) beschrieben:

1. Gehen Sie in Ihrem Apple-Entwicklerkonto zu [**Zertifikate, Kennungen & Profile**](https://developer.apple.com/account/ios/certificate).
2. Wählen Sie unter **Schlüssel** die Option **Alle** und klicken Sie auf die Schaltfläche Hinzufügen (+) in der oberen rechten Ecke.
3. Geben Sie unter **Schlüsselbeschreibung** einen eindeutigen Namen für den Signierschlüssel ein.
4. Aktivieren Sie unter **Wichtige Dienste** das Kontrollkästchen **Apple Push Notification Service (APNs)** und klicken Sie dann auf **Weiter**. Klicken Sie auf **Bestätigen**.
5. Notieren Sie sich die ID des Schlüssels. Klicken Sie auf **Download**, um den Schlüssel zu generieren und herunterzuladen. Stellen Sie sicher, dass Sie die heruntergeladene Datei an einem sicheren Ort speichern, da Sie sie nur einmal herunterladen können.
6. Gehen Sie in Braze zu **Einstellungen** > **App-Einstellungen** und laden Sie die Datei `.p8` unter **Apple Push Certificate** hoch. Sie können entweder Ihr Entwicklungs- oder Ihr Produktions-Push-Zertifikat hochladen. Um Push-Benachrichtigungen zu testen, nachdem Ihre App live im App Store ist, empfiehlt es sich, einen separaten Arbeitsbereich für die Entwicklungsversion Ihrer App einzurichten.
7. Wenn Sie dazu aufgefordert werden, geben Sie die [Bundle-ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), die [Schlüssel-ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) und die [Team-ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) Ihrer App ein und klicken dann auf **Speichern**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie Ihre `.p8` Datei über **Einstellungen verwalten** > **Einstellungen** hochladen.
{% endalert %}

### Schritt 2: Aktivieren Sie Push-Funktionen

Gehen Sie in Xcode zum Abschnitt **Signing & Capabilities** des Hauptziel der App und fügen Sie die Fähigkeit für Push-Benachrichtigungen hinzu.

![Der Abschnitt "Signing & Capabilities" in einem Xcode-Projekt.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

## Automatische Push-Integration

Das Swift SDK bietet einen rein konfigurationsbasierten Ansatz zur Automatisierung der Verarbeitung von Remote-Benachrichtigungen, die von Braze empfangen werden. Dieser Ansatz ist die einfachste Art der Integration von Push-Benachrichtigungen und wird für die meisten Kund:innen empfohlen.

Um die automatische Push Integration zu aktivieren, setzen Sie die Eigenschaft `automation` in der Konfiguration von `push` auf `true`:

{% tabs %}
{% tab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endtab %}
{% endtabs %}

Dies weist das SDK an, Folgendes auszuführen:
- Registrieren Sie Ihre Anwendung für Push-Benachrichtigungen auf dem System.
- Anfrage an die Push-Benachrichtigung Autorisierung/Erlaubnis bei der Initialisierung.
- Stellen Sie dynamisch Implementierungen für die Push-Benachrichtigung betreffende Delegatmethoden des Systems bereit.

{% alert note %}
Die vom SDK durchgeführten Automatisierungsschritte sind mit bereits bestehenden Integrationen zur Handhabung von Push-Benachrichtigungen in Ihrer Codebasis kompatibel. Das SDK automatisiert nur die Verarbeitung der von Braze empfangenen Remote-Benachrichtigung. Jeder System-Handler, der für die Verarbeitung eigener oder fremder SDK-Remote-Benachrichtigungen implementiert wurde, funktioniert auch dann noch, wenn `automation` aktiviert ist.
{% endalert %}

{% alert warning %}
Das SDK muss im Hauptthread initialisiert werden, um die Automatisierung der Push-Benachrichtigung zu ermöglichen. Die SDK-Initialisierung muss erfolgen, bevor die Anwendung gestartet wurde, oder in der AppDelegate-Implementierung von [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Wenn Ihre Anwendung vor der Initialisierung des SDK zusätzliche Einstellungen erfordert, lesen Sie bitte die Dokumentationsseite über die [verzögerte Initialisierung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/).
{% endalert %}

### Einzelne Konfigurationen außer Kraft setzen

Für eine genauere Kontrolle kann jeder Schritt der Automatisierung einzeln aktiviert oder deaktiviert werden:

{% tabs %}
{% tab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endtab %}
{% endtabs %}

Siehe [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) für alle verfügbaren Optionen und [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) für weitere Informationen zum Verhalten bei der Automatisierung.

Sie können den nächsten Abschnitt überspringen und mit dem [Deeplinking](#deep-linking) fortfahren, wenn Sie die automatische Push-Integration verwenden.

## Manuelle Push-Integration

Push-Benachrichtigungen können auch manuell integriert werden. In diesem Abschnitt werden die für diese Integration erforderlichen Schritte beschrieben. 

{% alert note %}
Wenn Sie sich auf Push-Benachrichtigungen für zusätzliches Verhalten verlassen, das für Ihre App spezifisch ist, können Sie die automatische Integration von Push-Benachrichtigungen anstelle der manuellen Integration von Push-Benachrichtigungen verwenden. Die Methode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) bietet eine Möglichkeit, über von Braze verarbeitete Remote-Benachrichtigungen informiert zu werden.
{% endalert %}

### Schritt 1: Registrieren Sie sich für Push-Benachrichtigungen mit APNs

Fügen Sie das entsprechende Code-Beispiel in die [`application:didFinishLaunchingWithOptions:` Delegate-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) Ihrer App ein, damit sich die Geräte Ihrer Nutzer:innen bei APNs registrieren können. Stellen Sie sicher, dass Sie den gesamten Code für die Push Integration im Hauptthread Ihrer Anwendung aufrufen.

Braze bietet auch Standard-Push-Kategorien für die Unterstützung von Push-Action-Buttons, die manuell zu Ihrem Code für die Push-Registrierung hinzugefügt werden müssen. Weitere Schritte zur Integration finden Sie unter [Aktionsschaltflächen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/action_buttons/).

Fügen Sie den folgenden Code in die Methode `application:didFinishLaunchingWithOptions:` Ihres App-Delegaten ein. 

{% alert note %}
Das folgende Code-Beispiel enthält die Integration für die vorläufige Push-Authentifizierung (Zeilen 5 und 6). Wenn Sie nicht vorhaben, eine vorläufige Autorisierung in Ihrer App zu verwenden, können Sie die Zeilen des Codes entfernen, die `UNAuthorizationOptionProvisional` zu den `requestAuthorization`-Optionen hinzufügen.<br>In den [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) erfahren Sie mehr über die vorläufige Push-Authentifizierung.
{% endalert %}

{% tabs %}
{% tab Swift %}

```swift
application.registerForRemoteNotifications()
let center = UNUserNotificationCenter.current()
center.setNotificationCategories(Braze.Notifications.categories)
center.delegate = self
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
center.requestAuthorization(options: options) { granted, error in
  print("Notification authorization, granted: \(granted), error: \(String(describing: error))")
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[application registerForRemoteNotifications];
UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
[center setNotificationCategories:BRZNotifications.categories];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
}
[center requestAuthorizationWithOptions:options
                      completionHandler:^(BOOL granted, NSError *_Nullable error) {
                        NSLog(@"Notification authorization, granted: %d, "
                              @"error: %@)",
                              granted, error);
}];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Startvorgang beendet, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Wenn Sie dies nicht tun, kann Ihre App eingehende Push-Benachrichtigungen verpassen. Mehr dazu erfahren Sie in der Dokumentation zu [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) von Apple.
{% endalert %}

### Schritt 2: Registrieren Sie Push-Token bei Braze

Sobald die Registrierung der APNs abgeschlossen ist, übergeben Sie die resultierende `deviceToken` an Braze, um Push-Benachrichtigungen für die Nutzer zu aktivieren.  

{% tabs %}
{% tab Swift %}

Fügen Sie den folgenden Code in die Methode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` Ihrer App ein:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endtab %}
{% tab OBJECTIVE-C %}

Fügen Sie den folgenden Code in die Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` Ihrer App ein:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endtab %}
{% endtabs %}

{% alert important %}
Die Delegatenmethode `application:didRegisterForRemoteNotificationsWithDeviceToken:` wird jedes Mal aufgerufen, nachdem `application.registerForRemoteNotifications()` aufgerufen wurde. <br><br>Wenn Sie von einem anderen Push-Dienst zu Braze migrieren und das Gerät Ihres Benutzers sich bereits bei APNs registriert hat, sammelt diese Methode beim nächsten Aufruf Token von bestehenden Registrierungen und die Benutzer müssen sich nicht erneut für Push anmelden.
{% endalert %}

### Schritt 3: Push-Bearbeitung aktivieren

Als nächstes leiten Sie die empfangenen Push-Benachrichtigungen an Braze weiter. Dieser Schritt ist für die Protokollierung von Push Analytics und die Behandlung von Links erforderlich. Stellen Sie sicher, dass Sie den gesamten Code für die Push Integration im Hauptthread Ihrer Anwendung aufrufen.

#### Standard Push Handling

{% tabs %}
{% tab Swift %}
Um das Standard Push Handling von Braze zu aktivieren, fügen Sie den folgenden Code in die `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`-Methode Ihrer App ein:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleBackgroundNotification(
  userInfo: userInfo,
  fetchCompletionHandler: completionHandler
) {
  return
}
completionHandler(.noData)
```

Als nächstes fügen Sie der Methode `userNotificationCenter(_:didReceive:withCompletionHandler:)` Ihrer App Folgendes hinzu:

```swift
if let braze = AppDelegate.braze, braze.notifications.handleUserNotification(
  response: response,
  withCompletionHandler: completionHandler
) {
  return
}
completionHandler()
```
{% endtab %}

{% tab OBJECTIVE-C %}
Um das Standard Push Handling von Braze zu aktivieren, fügen Sie den folgenden Code in die `application:didReceiveRemoteNotification:fetchCompletionHandler:`-Methode Ihrer App  ein:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleBackgroundNotificationWithUserInfo:userInfo
                                                                                                       fetchCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler(UIBackgroundFetchResultNoData);
```

Als nächstes fügen Sie den folgenden Code in die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` Ihrer App ein:

```objc
BOOL processedByBraze = AppDelegate.braze != nil && [AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                                                                                  withCompletionHandler:completionHandler];
if (processedByBraze) {
  return;
}

completionHandler();
```
{% endtab %}
{% endtabs %}

#### Foreground Push Handling

{% tabs %}
{% tab Swift %}
Um das Foreground Push Handling zu aktivieren und die Nachrichten von Braze erkennen zu lassen, wenn sie empfangen werden, implementieren Sie `UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)`. Wenn die Benachrichtigung im Vordergrund angetippt wird, wird der Push-Delegat `userNotificationCenter(_:didReceive:withCompletionHandler:)` aufgerufen und Braze protokolliert das Push-Klick-Event.

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  willPresent notification: UNNotification,
  withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions
) -> Void) {
  if let braze = AppDelegate.braze {
    // Forward notification payload to Braze for processing.
    braze.notifications.handleForegroundNotification(notification: notification)
  }

  // Configure application's foreground notification display options.
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner])
  } else {
    completionHandler([.alert])
  }
}
```
{% endtab %}

{% tab OBJECTIVE-C %}
Um das Foreground Push Handling zu aktivieren und die Nachrichten von Braze erkennen zu lassen, wenn sie empfangen werden, implementieren Sie `userNotificationCenter:willPresentNotification:withCompletionHandler:`. Wenn die Benachrichtigung im Vordergrund angetippt wird, wird der Push-Delegat `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` aufgerufen und Braze protokolliert das Push-Klick-Event.

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (AppDelegate.braze != nil) {
    // Forward notification payload to Braze for processing.
    [AppDelegate.braze.notifications handleForegroundNotificationWithNotification:notification];
  }

  // Configure application's foreground notification display options.
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```
{% endtab %}
{% endtabs %}

## Deeplinks setzen

Deeplinks von einem Push in die App werden automatisch über unsere standardmäßige Dokumentation zur Push-Integration gesetzt. Wenn Sie mehr darüber erfahren möchten, wie Sie Deeplinks zu bestimmten Standorten in Ihrer App setzen können, sehen Sie sich unsere [fortgeschrittenen Anwendungsfälle]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-implementation) an.

## Push-Benachrichtigungen für Updates abonnieren

Um auf die Push-Benachrichtigungen zuzugreifen, die von Braze verarbeitet werden, verwenden Sie die Methode [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)/).

Mit dem Parameter `payloadTypes` können Sie angeben, ob Sie Benachrichtigungen über geöffnete Push-Events, empfangene Push-Events oder beides abonnieren möchten.

{% tabs %}
{% tab Swift %}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.notifications.subscribeToUpdates(payloadTypes: [.open, .received]) { payload in
  print("Braze processed notification with title '\(payload.title)' and body '\(payload.body)'")
}
```

{% alert important %}
Denken Sie daran, dass empfangene Push-Events nur für Push-Benachrichtigungen im Vordergrund und `content-available` im Hintergrund ausgelöst werden. Für Benachrichtigungen, die während der Beendigung empfangen werden, oder für Benachrichtigungen im Hintergrund ohne das Feld `content-available` werden sie nicht getriggert.
{% endalert %}

{% endtab %}

{% tab OBJECTIVE-C %}

```objc
NSInteger filtersValue = BRZNotificationsPayloadTypeFilter.opened.rawValue | BRZNotificationsPayloadTypeFilter.received.rawValue;
BRZNotificationsPayloadTypeFilter *filters = [[BRZNotificationsPayloadTypeFilter alloc] initWithRawValue: filtersValue];
BRZCancellable *cancellable = [notifications subscribeToUpdatesWithPayloadTypes:filters update:^(BRZNotificationsPayload * _Nonnull payload) {
  NSLog(@"Braze processed notification with title '%@' and body '%@'", payload.title, payload.body);
}];
```

{% alert important %}
Denken Sie daran, dass empfangene Push-Events nur für Push-Benachrichtigungen im Vordergrund und `content-available` im Hintergrund ausgelöst werden. Für Benachrichtigungen, die während der Beendigung empfangen werden, oder für Benachrichtigungen im Hintergrund ohne das Feld `content-available` werden sie nicht getriggert.
{% endalert %}

{% endtab %}

{% endtabs %}
{% alert note %}
Wenn Sie die automatische Push-Integration verwenden, ist `subscribeToUpdates(_:)` die einzige Möglichkeit, über von Braze verarbeitete Remote-Benachrichtigungen informiert zu werden. Die Systemmethoden `UIAppDelegate` und `UNUserNotificationCenterDelegate` werden nicht aufgerufen, wenn die Benachrichtigung automatisch von Braze verarbeitet wird.
{% endalert %}

{% alert tip %}
Erstellen Sie Ihr Abo für Push-Benachrichtigungen in `application(_:didFinishLaunchingWithOptions:)`, um sicherzustellen, dass Ihr Abo ausgelöst wird, wenn ein Endnutzer:in auf eine Benachrichtigung tippt, während sich Ihre App in einem beendeten Zustand befindet.
{% endalert %}

## Testen {#push-testing}

Wenn Sie In-App- und Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie über CURL und die [Messaging API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) eine einzelne Nachricht über das Terminal senden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` - verfügbar unter **Einstellungen** > **API-Schlüssel**.
- `YOUR_EXTERNAL_USER_ID` - verfügbar auf der Seite **Benutzer suchen**. Weitere Informationen finden Sie unter [Zuweisung von Nutzer:innen IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befinden sich diese Seiten an einer anderen Stelle: <br>- **API-Schlüssel** finden Sie unter **Entwicklerkonsole** > **API-Einstellungen** <br>- **Benutzer suchen** finden Sie unter **Benutzer** > **Benutzersuche**
{% endalert %}

In dem folgenden Beispiel wird die Instanz `US-01` verwendet. Wenn Sie sich nicht in dieser Instanz befinden, sehen Sie in unserer [API Dokumentation]({{site.baseurl}}/api/basics/) nach, an welchen Endpunkt Sie Anfragen stellen müssen.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## Push-Primer {#push-primers}

Push-Benachrichtigungskampagnen ermutigen Ihre Nutzer:innen, Push-Benachrichtigungen auf ihrem Gerät für Ihre App zu aktivieren. Dies kann ohne SDK-Anpassung mit unserem [No Code Push Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) geschehen.

