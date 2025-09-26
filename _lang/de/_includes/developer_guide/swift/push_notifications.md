## Rate-Limits

Push-Benachrichtigungen sind Rate-Limits, also haben Sie keine Angst davor, so viele zu senden, wie Ihre Anwendung benötigt. iOS und die Server des Apple Serviceleistungen; Dienste (APNs) für Push-Benachrichtigungen kontrollieren, wie oft sie zugestellt werden, und Sie werden nicht in Schwierigkeiten kommen, wenn Sie zu viele senden. Wenn Ihre Push-Benachrichtigungen gedrosselt werden, werden sie möglicherweise verzögert, bis das Gerät das nächste Mal ein Keep-Alive-Paket sendet oder eine andere Benachrichtigung erhält.

## Push-Benachrichtigungen einrichten

### Schritt 1: Laden Sie Ihr APN-Token hoch

{% multi_lang_include developer_guide/swift/apns_token.md %}

### Schritt 2: Aktivieren Sie Push-Funktionen

Gehen Sie in Xcode zum Abschnitt **Signing & Capabilities** des Hauptziel der App und fügen Sie die Fähigkeit für Push-Benachrichtigungen hinzu.

![Der Abschnitt "Signing & Capabilities" in einem Xcode-Projekt.]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

### Schritt 3: Einrichten der Push-Bearbeitung

Sie können das Swift SDK verwenden, um die Verarbeitung der von Braze empfangenen Fernbenachrichtigungen zu automatisieren. Dies ist die einfachste Art, Push-Benachrichtigungen zu handhaben und die empfohlene Bearbeitungsmethode.

{% tabs local %}
{% tab Automatisch %}
#### Schritt 3.1: Enablement der Automatisierung in der Push-Eigenschaft

Um die automatische Push Integration zu aktivieren, setzen Sie die Eigenschaft `automation` in der Konfiguration von `push` auf `true`:

{% subtabs %}
{% subtab Swift %}
```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-API-ENDPOINT}")
configuration.push.automation = true
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{YOUR-BRAZE-API-KEY}" endpoint:@"{YOUR-BRAZE-API-ENDPOINT}"];
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
```

{% endsubtab %}
{% endsubtabs %}

Dies weist das SDK an, Folgendes auszuführen:
- Registrieren Sie Ihre Anwendung für Push-Benachrichtigungen auf dem System.
- Anfrage an die Push-Benachrichtigung Autorisierung/Erlaubnis bei der Initialisierung.
- Stellen Sie dynamisch Implementierungen für die Push-Benachrichtigung betreffende Delegatmethoden des Systems bereit.

{% alert note %}
Die vom SDK durchgeführten Automatisierungsschritte sind mit bereits bestehenden Integrationen zur Handhabung von Push-Benachrichtigungen in Ihrer Codebasis kompatibel. Das SDK automatisiert nur die Verarbeitung der von Braze empfangenen Remote-Benachrichtigung. Jeder System-Handler, der für die Verarbeitung eigener oder fremder SDK-Remote-Benachrichtigungen implementiert wurde, funktioniert auch dann noch, wenn `automation` aktiviert ist.
{% endalert %}

{% alert warning %}
Das SDK muss im Hauptthread initialisiert werden, um die Automatisierung der Push-Benachrichtigung zu ermöglichen. Die SDK-Initialisierung muss erfolgen, bevor die Anwendung gestartet wurde, oder in der AppDelegate-Implementierung von [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application).
Wenn Ihre Anwendung vor der Initialisierung des SDK zusätzliche Einstellungen erfordert, lesen Sie bitte die Dokumentationsseite über die [verzögerte Initialisierung]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift).
{% endalert %}

#### Schritt 3.2: Individuelle Konfigurationen außer Kraft setzen (optional)

Für eine genauere Kontrolle kann jeder Schritt der Automatisierung einzeln aktiviert oder deaktiviert werden:

{% subtabs %}
{% subtab Swift %}

```swift
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = true
configuration.push.automation.requestAuthorizationAtLaunch = false
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Enable all automations and disable the automatic notification authorization request at launch.
configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initEnablingAllAutomations:YES];
configuration.push.automation.requestAuthorizationAtLaunch = NO;
```

{% endsubtab %}
{% endsubtabs %}

Siehe [`Braze.Configuration.Push.Automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) für alle verfügbaren Optionen und [`automation`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property) für weitere Informationen zum Verhalten bei der Automatisierung.
{% endtab %}

{% tab Manual %}
{% alert note %}
Wenn Sie sich auf Push-Benachrichtigungen für zusätzliches Verhalten verlassen, das für Ihre App spezifisch ist, können Sie die automatische Integration von Push-Benachrichtigungen anstelle der manuellen Integration von Push-Benachrichtigungen verwenden. Die Methode [`subscribeToUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)) bietet eine Möglichkeit, über von Braze verarbeitete Remote-Benachrichtigungen informiert zu werden.
{% endalert %}

#### Schritt 3.1: Registrieren Sie sich für Push-Benachrichtigungen mit APNs

Fügen Sie das entsprechende Code-Beispiel in die [`application:didFinishLaunchingWithOptions:` Delegate-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) Ihrer App ein, damit sich die Geräte Ihrer Nutzer:innen bei APNs registrieren können. Stellen Sie sicher, dass Sie den gesamten Code für die Push Integration im Hauptthread Ihrer Anwendung aufrufen.

Braze bietet auch Standard-Push-Kategorien für die Unterstützung von Push-Action-Buttons, die manuell zu Ihrem Code für die Push-Registrierung hinzugefügt werden müssen. Weitere Schritte zur Integration finden Sie unter [Aktionsschaltflächen]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories).

Fügen Sie den folgenden Code in die Methode `application:didFinishLaunchingWithOptions:` Ihres App-Delegaten ein. 

{% alert note %}
Das folgende Code-Beispiel enthält die Integration für die vorläufige Push-Authentifizierung (Zeilen 5 und 6). Wenn Sie nicht vorhaben, eine vorläufige Autorisierung in Ihrer App zu verwenden, können Sie die Zeilen des Codes entfernen, die `UNAuthorizationOptionProvisional` zu den `requestAuthorization`-Optionen hinzufügen.<br>In den [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) erfahren Sie mehr über die vorläufige Push-Authentifizierung.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

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

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert warning %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Startvorgang beendet, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Wenn Sie dies nicht tun, kann Ihre App eingehende Push-Benachrichtigungen verpassen. Mehr dazu erfahren Sie in der Dokumentation zu [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) von Apple.
{% endalert %}

#### Schritt 3.2: Registrieren Sie Push-Token bei Braze

Sobald die Registrierung der APNs abgeschlossen ist, übergeben Sie die resultierende `deviceToken` an Braze, um Push-Benachrichtigungen für die Nutzer zu aktivieren.  

{% subtabs %}
{% subtab Swift %}

Fügen Sie den folgenden Code in die Methode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` Ihrer App ein:

```swift
AppDelegate.braze?.notifications.register(deviceToken: deviceToken)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Fügen Sie den folgenden Code in die Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` Ihrer App ein:

```objc
[AppDelegate.braze.notifications registerDeviceToken:deviceToken];
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Die Delegatenmethode `application:didRegisterForRemoteNotificationsWithDeviceToken:` wird jedes Mal aufgerufen, nachdem `application.registerForRemoteNotifications()` aufgerufen wurde. <br><br>Wenn Sie von einem anderen Push-Dienst zu Braze migrieren und das Gerät Ihres Benutzers sich bereits bei APNs registriert hat, sammelt diese Methode beim nächsten Aufruf Token von bestehenden Registrierungen und die Benutzer müssen sich nicht erneut für Push anmelden.
{% endalert %}

#### Schritt 3.3: Push-Bearbeitung aktivieren

Als nächstes leiten Sie die empfangenen Push-Benachrichtigungen an Braze weiter. Dieser Schritt ist für die Protokollierung von Push Analytics und die Behandlung von Links erforderlich. Stellen Sie sicher, dass Sie den gesamten Code für die Push Integration im Hauptthread Ihrer Anwendung aufrufen.

##### Standard Push Handling

{% subtabs %}
{% subtab Swift %}
Um die Standard-Push-Behandlung von Braze zu aktivieren, fügen Sie den folgenden Code in die Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App ein:

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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
Um die Standard Push-Behandlung von Braze zu aktivieren, fügen Sie den folgenden Code in die `application:didReceiveRemoteNotification:fetchCompletionHandler:` Methode Ihrer Anwendung ein:

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
{% endsubtab %}
{% endsubtabs %}

##### Foreground Push Handling

{% subtabs %}
{% subtab Swift %}
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
{% endsubtab %}

{% subtab OBJECTIVE-C %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Benachrichtigungen testen {#push-testing}

Wenn Sie In-App- und Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie über CURL und die [Messaging API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) eine einzelne Nachricht über das Terminal senden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

- `YOUR_API_KEY` - verfügbar unter **Einstellungen** > **API-Schlüssel**.
- `YOUR_EXTERNAL_USER_ID` - verfügbar auf der Seite **Benutzer suchen**. Weitere Informationen finden Sie unter [Zuweisung von Nutzer:innen IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id).
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

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

## Push-Primer {#push-primers}

Push-Benachrichtigungskampagnen ermutigen Ihre Nutzer:innen, Push-Benachrichtigungen auf ihrem Gerät für Ihre App zu aktivieren. Dies kann ohne SDK-Anpassung mit unserem [No Code Push Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) geschehen.

## Dynamische APNs Gateway-Verwaltung

Die dynamische Verwaltung des Apple Push Notification Service (APNs) Gateways verbessert die Zuverlässigkeit und Effizienz von iOS Push-Benachrichtigungen durch die automatische Erkennung der richtigen APN-Umgebung. Früher mussten Sie die APN-Umgebungen (Entwicklung oder Produktion) für Ihre Push-Benachrichtigungen manuell auswählen, was manchmal zu falschen Gateway-Konfigurationen, Zustellungsfehlern und `BadDeviceToken` Fehlern führte.

Mit der dynamischen APNs-Gateway-Verwaltung haben Sie:

- **Verbesserte Zuverlässigkeit:** Benachrichtigungen werden immer an die richtige APN-Umgebung zugestellt, wodurch die Zahl der fehlgeschlagenen Zustellungen reduziert wird.
- **Vereinfachte Konfiguration:** Sie müssen die APN-Gateway-Einstellungen nicht mehr manuell verwalten.
- **Fehlerresistenz:** Ungültige oder fehlende Gateway-Werte werden zuverlässig behandelt, so dass der Dienst nicht unterbrochen wird.

### Voraussetzungen

Braze unterstützt die dynamische APNs-Gateway-Verwaltung für Push-Benachrichtigungen unter iOS mit der folgenden SDK-Versionsanforderung:

{% sdk_min_versions swift:10.0.0 %}

### Funktionsweise

Wenn eine iOS App mit dem Braze Swift SDK integriert ist, sendet sie gerätebezogene Daten, einschließlich [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) an die Braze SDK API, falls verfügbar. Der Wert `apns_gateway` zeigt an, ob die App die Entwicklungs- (`dev`) oder die Produktionsumgebung (`prod`) APNs verwendet.

Braze speichert auch den gemeldeten Gateway-Wert für jedes Gerät. Wenn ein neuer, gültiger Gateway-Wert empfangen wird, aktualisiert Braze den gespeicherten Wert automatisch.

Wenn Braze eine Push-Benachrichtigung sendet:

- Wenn für das Gerät ein gültiger Gateway-Wert (dev oder prod) gespeichert ist, verwendet Braze diesen, um die richtige APN-Umgebung zu ermitteln.
- Wenn kein Gateway-Wert gespeichert ist, verwendet Braze standardmäßig die APN-Umgebung, die auf der Seite **App-Einstellungen** konfiguriert wurde.

### Häufig gestellte Fragen

#### Warum wurde dieses Feature eingeführt?

Bei der dynamischen APNs-Gateway-Verwaltung wird die richtige Umgebung automatisch ausgewählt. Zuvor mussten Sie das APN-Gateway manuell konfigurieren, was zu `BadDeviceToken` Fehlern, ungültigen Token und potenziellen Problemen bei der Rate-Limitierung von APNs führen konnte.

#### Wie wirkt sich dies auf die Performance der Push-Zustellung aus?

Dieses Feature verbessert die Zustellungsraten, indem Push-Tokens immer an die richtige APN-Umgebung weitergeleitet werden. So werden Fehler durch falsch konfigurierte Gateways vermieden.

#### Kann ich dieses Feature deaktivieren?

Die dynamische APNs Gateway-Verwaltung ist standardmäßig aktiviert und bietet Verbesserungen der Zuverlässigkeit. Wenn Sie spezielle Anwendungsfälle haben, die eine manuelle Auswahl des Gateways erfordern, wenden Sie sich an den [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/).
