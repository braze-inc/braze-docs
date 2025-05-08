---
nav_title: Push-Benachrichtigungen
article_title: Push-Benachrichtigungen für das Cordova Braze SDK
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "Dieser Artikel behandelt die Implementierung von Push-Benachrichtigungen in Cordova."
channel: push
---

# Integration von Push-Benachrichtigungen

> Erfahren Sie, wie Sie Push-Benachrichtigungen für das Cordova Braze SDK integrieren.

{% multi_lang_include cordova/prerequisites.md %}

## Grundlegende Push-Funktionen

Standardmäßig sind die grundlegenden Push-Benachrichtigungsfunktionen im Braze Cordova Plugin aktiviert. Sie können diese Features durch [Anpassen der XML-Konfigurationen]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options) deaktivieren. Ausführlichere Informationen zu den Funktionen der nativen Push-Benachrichtigung finden Sie in den Anleitungen zu Push-Benachrichtigungen [für iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).

## Erweiterte Push-Funktionen

{% alert important %}
Jedes Mal, wenn Sie Cordova-Plugins hinzufügen, entfernen oder aktualisieren, überschreibt Cordova die Podfile im Xcode-Projekt. Das bedeutet, dass Sie diesen Vorgang jedes Mal wiederholen müssen, wenn Sie die Cordova-Plugins ändern.
{% endalert %}

### Umfangreiche Push-Benachrichtigungen

#### Schritt 1: Erweiterung für einen Benachrichtigungsdienst erstellen

Erstellen Sie in Ihrem Xcode-Projekt eine Benachrichtigungsdienst-Erweiterung. Eine vollständige Anleitung finden Sie unter [iOS Rich Push Notifications Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

#### Schritt 2: Neues Ziel hinzufügen

Öffnen Sie die Podfile und fügen Sie `BrazeNotificationService` zum Ziel der [soeben erstellten](#step-1-create-a-notification-service-extension) Benachrichtigungsdienst-Erweiterung hinzu. Wenn `BrazeNotificationService` bereits zu einem Ziel hinzugefügt wurde, entfernen Sie es, bevor Sie fortfahren. Um Fehler durch doppelte Symbole zu vermeiden, verwenden Sie statisches Linking.

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

#### Schritt 3: Installieren Sie Ihre CocoaPods-Abhängigkeiten neu

Wechseln Sie im Terminal in das iOS-Verzeichnis Ihres Projekts und installieren Sie die CocoaPod-Abhängigkeiten neu.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### Push-Storys

#### Schritt 1: Eine Erweiterung für Benachrichtigungsinhalte erstellen

Erstellen Sie in Ihrem Xcode-Projekt eine Erweiterung für Benachrichtigungsinhalte. Eine vollständige Anleitung finden Sie unter [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

#### Schritt 2: Konfigurieren Sie Ihre Push-App-Gruppe

Konfigurieren Sie in der Datei `config.xml` Ihres Projekts die Push-App-Gruppe [, die Sie gerade erstellt haben](#step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Ersetzen Sie `PUSH_APP_GROUP` durch den Namen Ihrer Push-App-Gruppe. Ihre `config.xml` sollte in etwa so aussehen wie die folgende:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### Schritt 3: Ein neues Ziel hinzufügen

Öffnen Sie die Podfile und fügen Sie `BrazePushStory` zum [zuvor erstellten](#step-1-create-a-notification-content-extension) Ziel der Erweiterung für Benachrichtigungsinhalte hinzu. Um Fehler durch doppelte Symbole zu vermeiden, verwenden Sie statisches Linking.

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

#### Schritt 4: Installieren Sie Ihre CocoaPods-Abhängigkeiten neu

Gehen Sie im Terminal in Ihr iOS-Verzeichnis und installieren Sie die CocoaPod-Abhängigkeiten neu.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
