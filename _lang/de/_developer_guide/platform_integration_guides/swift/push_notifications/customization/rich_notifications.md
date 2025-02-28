---
nav_title: Reichhaltige Benachrichtigungen
article_title: Reichhaltige Push-Benachrichtigungen für iOS
platform: Swift
page_order: 5
description: "Dieser Artikel behandelt die Implementierung von Rich-Push-Benachrichtigungen für iOS für das Swift SDK."
channel:
  - push

---

# Rich-Benachrichtigungen

> Rich-Benachrichtigungen sind Push-Benachrichtigungen mit Bildern, GIFs und Videos. Um diese Funktion zu aktivieren, müssen Sie eine Erweiterung für einen Benachrichtigungsdienst erstellen - eine Art von Erweiterung, die die Änderung einer Push-Nutzlast ermöglicht, bevor sie angezeigt wird. Eine Liste der unterstützten Dateitypen und -größen finden Sie in Apples [`UNNotificationAttachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) finden Sie eine Liste der unterstützten Dateitypen und -größen.

## Schritt 1: Erstellen einer Serviceerweiterung

Um eine [Erweiterung für einen Benachrichtigungsdienst](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension) zu erstellen, navigieren Sie in Xcode zu **Datei > Neu > Targeting** und wählen **Benachrichtigungsdienst-Erweiterung**.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Vergewissern Sie sich, dass **In Anwendung einbetten** so eingestellt ist, dass die Erweiterung in Ihre Anwendung eingebettet wird.

## Schritt 2: Einrichten der Erweiterung des Benachrichtigungsdienstes

Eine Erweiterung für einen Benachrichtigungsdienst ist eine eigene Binärdatei, die mit Ihrer App gebündelt wird. Sie muss im [Apple Developer Portal](https://developer.apple.com) mit einer eigenen App-ID und einem eigenen Bereitstellungsprofil eingerichtet werden.

Die Bundle-ID der Erweiterung des Benachrichtigungsdienstes muss sich von der Bundle-ID Ihres App-Hauptziels für die App unterscheiden. Wenn die Bundle-ID Ihrer App zum Beispiel `com.company.appname` lautet, können Sie `com.company.appname.AppNameServiceExtension` für Ihre Diensterweiterung verwenden.

## Schritt 3: Integration von Rich-Push-Benachrichtigungen

Eine schrittweise Anleitung zur Integration von Rich-Push-Benachrichtigungen mit `BrazeNotificationService` finden Sie in unserem [Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Um ein Beispiel zu sehen, sehen Sie sich die Verwendung in [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) unserer App Beispiele.

### Rich-Push-Benachrichtigung zu Ihrer App hinzufügen

{% tabs local %}
{% tab Swift Package Manager %}

Nachdem Sie die [Anleitung zur Integration des Swift-Paketmanagers]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) befolgt haben, fügen Sie `BrazeNotificationService` zu Ihrem `Notification Service Extension` hinzu, indem Sie wie folgt vorgehen:

1. Wählen Sie in Xcode unter Frameworks und Bibliotheken das Symbol <i class="fas fa-plus"></i> "Hinzufügen" aus, um ein Framework hinzuzufügen. <br><br>![Das Plus-Symbol befindet sich unter Frameworks und Bibliotheken in Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Wählen Sie das Framework "BrazeNotificationService" aus. <br><br>![Das Framework "BrazeNotificationService" kann in dem sich öffnenden Modal ausgewählt werden.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Fügen Sie Folgendes zu Ihrem Podfile hinzu:

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
Eine Anleitung zur Implementierung von Push-Stories finden Sie in der [Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Nachdem Sie das Podfile aktualisiert haben, wechseln Sie in Ihrem Terminal in das Verzeichnis Ihres Xcode App-Projekts und führen Sie `pod install` aus.

{% endtab %}

{% tab Manual %}

Um `BrazeNotificationService.xcframework` zu Ihrer `Notification Service Extension` hinzuzufügen, siehe [Manuelle Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/).

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

## Schritt 4: Erstellen einer umfangreichen Benachrichtigung in Ihrem Dashboard

Ihr Marketing Team kann auch Rich-Benachrichtigungen über das Dashboard erstellen. Erstellen Sie eine Push-Benachrichtigung über den Push Composer und hängen Sie einfach ein Bild oder GIF an oder geben Sie eine URL an, die ein Bild, GIF oder Video enthält. Beachten Sie, dass Assets beim Empfang von Push-Benachrichtigungen heruntergeladen werden. Planen Sie also große, synchrone Spitzen bei Anfragen ein, wenn Sie Ihre Inhalte hosten.

