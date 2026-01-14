{% multi_lang_include developer_guide/prerequisites/cordova.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Push-Storys einrichten

### Schritt 1: Eine Erweiterung für Benachrichtigungsinhalte erstellen

Erstellen Sie in Ihrem Xcode-Projekt eine Erweiterung für Benachrichtigungsinhalte. Eine vollständige Anleitung finden Sie unter [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Schritt 2: Konfigurieren Sie Ihre Push-App-Gruppe

Konfigurieren Sie in der Datei `config.xml` Ihres Projekts die Push-App-Gruppe [, die Sie gerade erstellt haben](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Ersetzen Sie `PUSH_APP_GROUP` durch den Namen Ihrer Push-App-Gruppe. Ihre `config.xml` sollte in etwa so aussehen wie die folgende:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Schritt 3: Ein neues Ziel hinzufügen

Öffnen Sie die Podfile und fügen Sie `BrazePushStory` zum [zuvor erstellten](#cordova_step-1-create-a-notification-content-extension) Ziel der Erweiterung für Benachrichtigungsinhalte hinzu. Um Fehler durch doppelte Symbole zu vermeiden, verwenden Sie statisches Linking.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Ersetzen Sie `NOTIFICATION_CONTENT_EXTENSION` durch den Namen der Erweiterung Ihres Benachrichtigungsinhalts. Ihr Podfile sollte in etwa so aussehen wie das folgende:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

### Schritt 4: Installieren Sie Ihre CocoaPods-Abhängigkeiten neu

Gehen Sie im Terminal in Ihr iOS-Verzeichnis und installieren Sie die CocoaPod-Abhängigkeiten neu.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
