{% multi_lang_include developer_guide/prerequisites/swift.md %} Bitte [richten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) Sie auch [Push-Benachrichtigungen ein]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Einrichten von Rich-Push-Benachrichtigungen

### Schritt 1: Erstellen einer Serviceerweiterung

Um eine [Benachrichtigungsdienst-Erweiterung](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension) zu erstellen, navigieren Sie in Xcode zu **„Datei“ > „Neu“ > „Ziel“** und wählen Sie **„Benachrichtigungsdienst-Erweiterung**“.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Vergewissern Sie sich, dass **In Anwendung einbetten** so eingestellt ist, dass die Erweiterung in Ihre Anwendung eingebettet wird.

### Schritt 2: Einrichtung des Benachrichtigungsdienstes

Eine Erweiterung für einen Benachrichtigungsdienst ist eine eigene Binärdatei, die mit Ihrer App gebündelt wird. Sie muss im [Apple Developer Portal](https://developer.apple.com) mit einer eigenen App-ID und einem eigenen Bereitstellungsprofil eingerichtet werden.

Die Bundle-ID der Erweiterung des Benachrichtigungsdienstes muss sich von der Bundle-ID Ihres App-Hauptziels für die App unterscheiden. Wenn die Bundle-ID Ihrer App zum Beispiel `com.company.appname` lautet, können Sie `com.company.appname.AppNameServiceExtension` für Ihre Diensterweiterung verwenden.

### Schritt 3: Hinzufügen einer App-Gruppe

Fügen Sie in Xcode die Funktion „App-Gruppen“ aus dem Bereich **„Signing&Capabilities“** zu Ihrem Haupt-App-Ziel sowie zum Ziel „Notification Service Extension“ hinzu. Klicken Sie dann auf die Schaltfläche **+**. Verwenden Sie die Bundle-ID Ihrer App, um die App-Gruppe zu erstellen. Wenn die Bundle-ID Ihrer App beispielsweise `com.company.appname` lautet, können Sie die App-Gruppe `group.com.company.appname.xyz` nennen.

{% alert important %}
App-Gruppen beziehen sich in diesem Zusammenhang auf die [App-Gruppen-Berechtigung](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) von Apple und nicht auf die ID Ihres Braze-Arbeitsbereichs (früher App-Gruppe).
{% endalert %}

Sie benötigen eine gemeinsame App-Gruppe, damit Ihre Haupt-App und die Benachrichtigungsdienst-Erweiterung auf gemeinsame Daten zugreifen können. Wenn Sie Ihre App nicht zu einer App-Gruppe hinzufügen, kann es vorkommen, dass Ihre App bestimmte Felder aus der Push-Nutzlast nicht ausfüllt und nicht vollständig wie erwartet funktioniert.

### Schritt 4: Integration von Rich-Push-Benachrichtigungen

Eine Schritt-für-Schritt-Anleitung zur Integration von Rich-Push-Benachrichtigungen finden`BrazeNotificationService` Sie in unserem [Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Ein Beispiel wird in der Verwendung in[`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift)unserer Beispiel-App referenziert.

#### Rich-Push-Benachrichtigung zu Ihrer App hinzufügen

{% tabs local %}
{% tab Swift Package Manager %}

Nachdem Sie die [Anleitung zur Integration des Swift-Paketmanagers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/) befolgt haben, fügen Sie `BrazeNotificationService` zu Ihrem `Notification Service Extension` hinzu, indem Sie wie folgt vorgehen:

1. Wählen Sie in Xcode unter Frameworks und Bibliotheken das Symbol <i class="fas fa-plus"></i> "Hinzufügen" aus, um ein Framework hinzuzufügen. <br><br>![Der Standort des Plus-Symbols in Xcode lautet „Frameworks und Bibliotheken“.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Bitte wählen Sie das Framework „BrazeNotificationService“ aus. <br><br>![Das „BrazeNotificationService“-Framework kann in dem während der Öffnung des Modals erscheinenden Modal ausgewählt werden.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Fügen Sie Folgendes zu Ihrer Podfile hinzu:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Anweisungen zur Implementierung von Push-Storys finden Sie in der [Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Nachdem Sie das Podfile aktualisiert haben, wechseln Sie in Ihrem Terminal in das Verzeichnis Ihres Xcode App-Projekts und führen Sie `pod install` aus.

{% endtab %}

{% tab Manual %}

Um `BrazeNotificationService.xcframework` zu Ihrer `Notification Service Extension` hinzuzufügen, siehe [Manuelle Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Verwendung Ihrer eigenen UNNotificationServiceExtension

Wenn Sie Ihre eigene UNNotificationServiceExtension verwenden müssen, können Sie stattdessen [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) in Ihrer `didReceive`-Methode aufrufen.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Schritt 5: Konfiguration der App-Gruppe in Braze

Weisen Sie vor der Initialisierung von Braze der Eigenschaft [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) der Braze-Konfiguration den Namen Ihrer App-Gruppe zu.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Schritt 6: Erstellen einer umfangreichen Benachrichtigung in Ihrem Dashboard

Ihr Marketing-Team kann auch Rich-Benachrichtigungen über das Dashboard erstellen. Erstellen Sie eine Push-Benachrichtigung über den Push-Composer und fügen Sie ein Bild oder GIF hinzu oder geben Sie eine URL an, unter der ein Bild, GIF oder Video gehostet wird. Beachten Sie, dass Assets beim Empfang von Push-Benachrichtigungen heruntergeladen werden. Planen Sie also große, synchrone Spitzen bei Anfragen ein, wenn Sie Ihre Inhalte hosten.
