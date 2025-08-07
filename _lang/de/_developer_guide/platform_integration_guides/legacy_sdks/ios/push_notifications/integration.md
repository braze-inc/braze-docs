---
nav_title: Integration
article_title: Push-Integration für iOS
platform: iOS
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie Push-Benachrichtigungen in Ihre iOS-Anwendung integrieren."
channel:
  - push
search_rank: 5

local_redirect:
  ios-10-rich-notifications: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/'
local_redirect:
  creating-a-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-service-extension'
local_redirect:
  setting-up-the-service-extension: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#setting-up-the-service-extension'
local_redirect:
  creating-a-rich-notification-in-your-dashboard: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/rich/#creating-a-rich-notification-in-your-dashboard'
local_redirect:
  push-action-buttons-integration: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/'
local_redirect:
  step-1-adding-braze-default-push-categories: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-1-adding-braze-default-push-categories'
local_redirect:
  step-2-enable-interactive-push-handling: '/docs/developer_guide/platform_integration_guides/ios/push_notifications/action_buttons/#step-2-enable-interactive-push-handling'
  
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push-Integration

## Schritt 1: Push-Benachrichtigungen konfigurieren

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

## Schritt 2: Aktivieren Sie Push-Funktionen

Vergewissern Sie sich in Ihren Projekteinstellungen, dass auf der Registerkarte **Fähigkeiten** die Funktion **Push-Benachrichtigungen** aktiviert ist.

![]({% image_buster /assets/img_archive/Enable_push_capabilities.png %})

Wenn Sie über getrennte Push-Zertifikate für Entwicklung und Produktion verfügen, müssen Sie auf der Registerkarte **Allgemein** das Kontrollkästchen **Signierung automatisch verwalten** deaktivieren. Auf diese Weise können Sie für jede Build-Konfiguration unterschiedliche Bereitstellungsprofile wählen, da das Feature zur automatischen Code-Signierung in Xcode nur für die Entwicklung gilt.

![Xcode Projekteinstellungen mit der Registerkarte "Allgemein". In diesem Tab ist die Option "Signierung automatisch verwalten" deaktiviert.]({% image_buster /assets/img_archive/xcode8_auto_signing.png %})

## Schritt 3: Für Push-Benachrichtigungen registrieren

Das entsprechende Code-Beispiel muss in der `application:didFinishLaunchingWithOptions:` Delegate-Methode Ihrer App enthalten sein, damit sich das Gerät Ihrer Benutzer bei APNs registrieren kann. Stellen Sie sicher, dass Sie den gesamten Code für die Push-Integration im Hauptthread Ihrer Anwendung aufrufen.

Braze bietet auch Standard-Push-Kategorien für die Unterstützung von Push-Action-Buttons, die manuell zu Ihrem Code für die Push-Registrierung hinzugefügt werden müssen. Weitere Schritte zur Integration finden Sie unter [Aktionsschaltflächen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/).

{% alert warning %}
Wenn Sie einen angepassten Push-Prompt wie in unseren [Best Practices für Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/troubleshooting/) beschrieben implementiert haben, stellen Sie sicher, dass Sie den folgenden Code **jedes Mal** aufrufen, wenn die App ausgeführt wird, nachdem die Push-Berechtigungen für Ihre App erteilt wurden. **Apps müssen sich bei APNs neu registrieren, da [sich Gerätetoken beliebig ändern können](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).**
{% endalert %}

### UserNotification-Framework verwenden (iOS 10+)

Wenn Sie das in iOS 10 eingeführte Framework `UserNotifications` verwenden (empfohlen), fügen Sie den folgenden Code zur Methode `application:didFinishLaunchingWithOptions:` Ihres App-Delegaten hinzu.

{% alert important %}
Das folgende Code-Beispiel enthält die Integration für die vorläufige Push-Authentifizierung (Zeilen 5 und 6). Wenn Sie nicht vorhaben, eine vorläufige Autorisierung in Ihrer App zu verwenden, können Sie die Codezeilen entfernen, die `UNAuthorizationOptionProvisional` zu den Optionen von `requestAuthorization` hinzufügen.<br>Weitere Informationen zur vorläufigen Push-Authentifizierung finden Sie unter [Optionen für iOS-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).
{% endalert %}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
  UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
  center.delegate = self;
  UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
  if (@available(iOS 12.0, *)) {
  options = options | UNAuthorizationOptionProvisional;
  }
  [center requestAuthorizationWithOptions:options
                        completionHandler:^(BOOL granted, NSError * _Nullable error) {
                          [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
} else {
  UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
  [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
}
```

{% endtab %}
{% tab schnell %}

```swift
if #available(iOS 10, *) {
  let center = UNUserNotificationCenter.current()
  center.delegate = self as? UNUserNotificationCenterDelegate
  var options: UNAuthorizationOptions = [.alert, .sound, .badge]
  if #available(iOS 12.0, *) {
    options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
  }
  center.requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()
} else {
  let types : UIUserNotificationType = [.alert, .badge, .sound]
  let setting : UIUserNotificationSettings = UIUserNotificationSettings(types:types, categories:nil)
  UIApplication.shared.registerUserNotificationSettings(setting)
  UIApplication.shared.registerForRemoteNotifications()
}
```

{% endtab %}
{% endtabs %}


{% alert warning %}
Sie müssen Ihr Delegate-Objekt mit `center.delegate = self` synchron zuweisen, bevor Ihre App den Startvorgang beendet, vorzugsweise in `application:didFinishLaunchingWithOptions:`. Wenn Sie dies nicht tun, kann Ihre App eingehende Push-Benachrichtigungen verpassen. Weitere Informationen finden Sie in der Apple-Dokumentation [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate).
{% endalert %}

### Ohne UserNotifications-Framework

Wenn Sie das Framework `UserNotifications` nicht verwenden, fügen Sie den folgenden Code zur Methode `application:didFinishLaunchingWithOptions:` Ihres App-Delegaten hinzu:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
[[UIApplication sharedApplication] registerForRemoteNotifications];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab schnell %}

```swift
let types : UIUserNotificationType = UIUserNotificationType.Badge | UIUserNotificationType.Sound | UIUserNotificationType.Alert
var setting : UIUserNotificationSettings = UIUserNotificationSettings(forTypes: types, categories: nil)
UIApplication.shared.registerUserNotificationSettings(setting)
UIApplication.shared.registerForRemoteNotifications()
```

{% endtab %}
{% endtabs %}


## Schritt 4: Registrieren Sie Push-Token bei Braze

Sobald die Registrierung der APNs abgeschlossen ist, muss die folgende Methode geändert werden, um die resultierende `deviceToken` an Braze zu übergeben, damit der Benutzer für Push-Benachrichtigungen aktiviert wird:

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie den folgenden Code zu Ihrer Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` hinzu:

```objc
[[Appboy sharedInstance] registerDeviceToken:deviceToken];
```

{% endtab %}
{% tab schnell %}

Fügen Sie den folgenden Code in die Methode `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` Ihrer App ein:

```swift
Appboy.sharedInstance()?.registerDeviceToken(deviceToken)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Die Delegate-Methode `application:didRegisterForRemoteNotificationsWithDeviceToken:` wird jedes Mal nach dem Aufruf von `[[UIApplication sharedApplication] registerForRemoteNotifications]` aufgerufen. Wenn Sie von einem anderen Push-Dienst zu Braze migrieren und das Gerät Ihres Benutzers sich bereits bei APNs registriert hat, sammelt diese Methode beim nächsten Aufruf Token von bestehenden Registrierungen und die Benutzer müssen sich nicht erneut für Push anmelden.
{% endalert %}

## Schritt 5: Push-Bearbeitung aktivieren

Der folgende Code leitet empfangene Push-Benachrichtigungen an Braze weiter und ist für die Protokollierung von Push-Analysen und die Behandlung von Links erforderlich. Stellen Sie sicher, dass Sie den gesamten Code für die Push Integration im Hauptthread Ihrer Anwendung aufrufen.

### iOS 10+

Für iOS 10+ empfehlen wir die Integration des Frameworks `UserNotifications` und die folgenden Schritte:

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie den folgenden Code in die Methode `application:didReceiveRemoteNotification:fetchCompletionHandler:` Ihrer Anwendung ein:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Als nächstes fügen Sie den folgenden Code in die Methode `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` Ihrer App ein:

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                 didReceiveNotificationResponse:response
                          withCompletionHandler:completionHandler];
```

**Push im Vordergrund**

Um eine Push-Benachrichtigung anzuzeigen, während sich die App im Vordergrund befindet, implementieren Sie `userNotificationCenter:willPresentNotification:withCompletionHandler:`:

```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
       willPresentNotification:(UNNotification *)notification
         withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {
  if (@available(iOS 14.0, *)) {
    completionHandler(UNNotificationPresentationOptionList | UNNotificationPresentationOptionBanner);
  } else {
    completionHandler(UNNotificationPresentationOptionAlert);
  }
}
```

Wenn auf die Benachrichtigung im Vordergrund geklickt wird, wird der iOS 10 Push-Delegat `userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` aufgerufen und Braze protokolliert ein Push-Klick-Event.

{% endtab %}
{% tab schnell %}

Fügen Sie den folgenden Code in die Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App ein:

```swift
Appboy.sharedInstance()?.register(application,
                                            didReceiveRemoteNotification: userInfo,
                                            fetchCompletionHandler: completionHandler)
```

Als nächstes fügen Sie den folgenden Code in die Methode `userNotificationCenter(_:didReceive:withCompletionHandler:)` Ihrer App ein:

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                               didReceive: response,
                                               withCompletionHandler: completionHandler)
```

**Push im Vordergrund**

Um eine Push-Benachrichtigung anzuzeigen, während sich die App im Vordergrund befindet, implementieren Sie `userNotificationCenter(_:willPresent:withCompletionHandler:)`:

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
                              willPresent notification: UNNotification,
                              withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
  if #available(iOS 14.0, *) {
    completionHandler([.list, .banner]);
  } else {
    completionHandler([.alert]);
  }
}
```

Wenn auf die Benachrichtigung im Vordergrund geklickt wird, wird der iOS 10 Push-Delegat `userNotificationCenter(_:didReceive:withCompletionHandler:)` aufgerufen und Braze protokolliert ein Push-Klick-Event.

{% endtab %}
{% endtabs %}

### Vor-iOS 10

iOS 10 hat das Verhalten aktualisiert, sodass beim Klicken auf einen Push `application:didReceiveRemoteNotification:fetchCompletionHandler:` nicht mehr aufgerufen wird. Aus diesem Grund müssen Sie, wenn Sie nicht auf die Erstellung für iOS 10+ updaten und das Framework `UserNotifications` verwenden, Braze von beiden alten Delegaten aufrufen, was einen Bruch mit unserer früheren Integration darstellt.

Für Apps, die mit SDKs < iOS 10 erstellt werden, verwenden Sie die folgenden Anweisungen:

{% tabs %}
{% tab OBJECTIVE-C %}

Um die Nachverfolgung von geöffneten Push-Benachrichtigungen zu aktivieren, fügen Sie den folgenden Code in die Methode `application:didReceiveRemoteNotification:fetchCompletionHandler:` Ihrer App ein:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo
                      fetchCompletionHandler:completionHandler];
```

Um Push-Analytics unter iOS 10 zu unterstützen, müssen Sie außerdem den folgenden Code zur Delegate-Methode `application:didReceiveRemoteNotification:` Ihrer App hinzufügen:

```objc
[[Appboy sharedInstance] registerApplication:application
                didReceiveRemoteNotification:userInfo];
```

{% endtab %}
{% tab schnell %}

Um die Nachverfolgung von geöffneten Push-Benachrichtigungen zu aktivieren, fügen Sie den folgenden Code in die Methode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` Ihrer App ein:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo,
  fetchCompletionHandler: completionHandler)
```

Um Push-Analytics unter iOS 10 zu unterstützen, müssen Sie außerdem den folgenden Code zur Delegate-Methode `application(_:didReceiveRemoteNotification:)` Ihrer App hinzufügen:

```swift
Appboy.sharedInstance()?.register(application,
  didReceiveRemoteNotification: userInfo)
```

{% endtab %}
{% endtabs %}

## Schritt 6: Deeplinking

Deeplinking von einem Push in die App wird automatisch über unsere standardmäßige Push-Integration verarbeitet. Wenn Sie mehr darüber erfahren möchten, wie Sie Deeplinks zu bestimmten Stellen in Ihrer App hinzufügen, sehen Sie sich unsere [fortgeschrittenen Anwendungsfälle]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#linking-implementation) an.

## Schritt 7: Unit-Tests (optional)

Um die Testabdeckung für die soeben durchgeführten Integrationsschritte zu erhöhen, implementieren Sie [Push-Unit-Tests]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests/).

