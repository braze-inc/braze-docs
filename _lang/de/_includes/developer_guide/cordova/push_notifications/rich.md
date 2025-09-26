{% multi_lang_include developer_guide/prerequisites/cordova.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Einrichten von Rich-Push-Benachrichtigungen

### Schritt 1: Erweiterung für einen Benachrichtigungsdienst erstellen

Erstellen Sie in Ihrem Xcode-Projekt eine Benachrichtigungsdienst-Erweiterung. Eine vollständige Anleitung finden Sie unter [iOS Rich Push Notifications Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Schritt 2: Neues Ziel hinzufügen

Öffnen Sie die Podfile und fügen Sie `BrazeNotificationService` zum Ziel der [soeben erstellten](#cordova_step-1-create-a-notification-service-extension) Benachrichtigungsdienst-Erweiterung hinzu. Wenn `BrazeNotificationService` bereits zu einem Ziel hinzugefügt wurde, entfernen Sie es, bevor Sie fortfahren. Um Fehler durch doppelte Symbole zu vermeiden, verwenden Sie statisches Linking.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Ersetzen Sie `NOTIFICATION_SERVICE_EXTENSION` durch den Namen der Erweiterung Ihres Benachrichtigungsdienstes. Ihr Podfile sollte in etwa so aussehen wie das folgende:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

### Schritt 3: Installieren Sie Ihre CocoaPods-Abhängigkeiten neu

Wechseln Sie im Terminal in das iOS-Verzeichnis Ihres Projekts und installieren Sie die CocoaPod-Abhängigkeiten neu.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
