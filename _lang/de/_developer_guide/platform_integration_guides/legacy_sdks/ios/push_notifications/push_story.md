---
nav_title: Push-Storys
article_title: Push Stories für iOS
platform: iOS
page_order: 27
description: "Dieser Referenzartikel beschreibt, wie Sie Push-Storys für Ihre iOS-Anwendung einrichten."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Push Story einrichten

Die Push Story-Funktion erfordert das `UNNotification` Framework und iOS 10. Das Feature ist erst ab iOS SDK Version 3.2.1 verfügbar.

## Schritt 1: Aktivieren Sie Push in Ihrer App

Folgen Sie der [Integration von Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/), um Push in Ihrer App zu aktivieren.

## Schritt 2: Hinzufügen des Ziels Benachrichtigungsinhalt-Erweiterung

Wählen Sie in Ihrem App-Projekt das Menü **Datei > Neu > Ziel...** und fügen Sie ein neues `Notification Content Extension` Ziel hinzu und aktivieren Sie es.

![]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode sollte ein neues Ziel generieren und automatisch folgende Dateien für Sie anlegen:

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab schnell %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Schritt 3: Fähigkeiten aktivieren

Die Funktion Push Story erfordert den Hintergrundmodus im Abschnitt **Fähigkeiten** des Hauptziels der App. Nachdem Sie die Hintergrundmodi aktiviert haben, wählen Sie **Hintergrundabruf** und **Fernbenachrichtigungen**.

![]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Hinzufügen einer App-Gruppe

Sie müssen auch `Capability App Groups` hinzufügen. Wenn Sie noch keine App-Gruppe in Ihrer App hatten, gehen Sie zur **Fähigkeit** des Hauptziels der App, schalten Sie die `App Groups` ein und klicken Sie auf die Schaltfläche **+**. Verwenden Sie die Bundle-ID Ihrer App, um die App-Gruppe zu erstellen. Wenn die Bundle-ID Ihrer App beispielsweise `com.company.appname` lautet, können Sie die App-Gruppe `group.com.company.appname.xyz` nennen. Sie müssen `App Groups` sowohl für die Haupt-App als auch für die Ziele der Inhaltserweiterung aktivieren.

{% alert important %}
`App Groups` bezieht sich in diesem Zusammenhang auf die [App-Gruppen-Berechtigung](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) von Apple und nicht auf Ihre Braze-Arbeitsbereichs-ID (früher App-Gruppe).
{% endalert %}

Wenn Sie Ihre App nicht zu einer App-Gruppe hinzufügen, kann es sein, dass Ihre App bestimmte Felder aus der Push-Nutzlast nicht ausfüllt und nicht vollständig wie erwartet funktioniert.

## Schritt 4: Hinzufügen des Push Story Frameworks zu Ihrer App

{% tabs local %}
{% tab Swift-Paketmanager %}

Nachdem Sie den [Leitfaden für die Integration von Swift-Paketmanager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) befolgt haben, fügen Sie `AppboyPushStory` zur `Notification Content Extension` hinzu:

![Wählen Sie in Xcode unter "Frameworks and Libraries" das Pluszeichen (+) aus, um ein Framework hinzuzufügen.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Fügen Sie die folgende Zeile in Ihr Podfile ein:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Navigieren Sie nach der Aktualisierung des Podfile in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen Sie `pod install` aus.

{% endtab %}
{% tab Manuell %}

Laden Sie die neueste Version der `AppboyPushStory.zip` von der [GitHub-Release-Seite](https://github.com/Appboy/appboy-ios-sdk/releases) herunter, extrahieren Sie sie und fügen Sie der `Notification Content Extension` Ihres Projekts die folgenden Dateien hinzu:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Stellen Sie sicher, dass unter der Spalte **Einbetten** die Option **Nicht einbetten** für **AppboyPushStory.xcframework** ausgewählt ist.
{% endalert %}

Fügen Sie unter **Build Settings > Other Linker Flags** das Flag `-ObjC` zur `Notification Content Extension` Ihres Projekts hinzu.

{% endtab %}
{% endtabs %}

## Schritt 5: View-Controller für Benachrichtigungen aktualisieren

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie der `NotificationViewController.h` die folgenden Zeilen hinzu, um neue Eigenschaften hinzuzufügen und die Header-Dateien zu importieren:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Entfernen Sie in Ihrem `NotificationViewController.m` die Standardimplementierung und fügen Sie folgenden Code hinzu:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab schnell %}

Fügen Sie in `NotificationViewController.swift` die folgende Zeile hinzu, um die Header-Dateien zu importieren:

```swift
import AppboyPushStory
```

Entfernen Sie als Nächstes die Standard-Implementierung und fügen den folgenden Code hinzu:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }
    
  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }
    
  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Schritt 6: Legen Sie das Storyboard für die Erweiterung der Benachrichtigung fest

Öffnen Sie das Storyboard `Notification Content Extension` und platzieren Sie eine neue `UIView` im View-Controller für Benachrichtigungen. Benennen Sie die Klasse in `ABKStoriesView` um. Legen Sie Breite und Höhe der Ansicht so fest, dass sie automatisch an den Rahmen der Hauptansicht des View-Controllers für Benachrichtigungen angepasst werden.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

Verknüpfen Sie als Nächstes das IBOutlet `storiesView` des View-Controllers für Benachrichtigungen mit der hinzugefügten `ABKStoriesView`.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Schritt 7: Plist-Datei der Erweiterung für Benachrichtigungsinhalte anpassen

Öffnen Sie die Datei `Info.plist` der `Notification Content Extension` und fügen Sie unter `NSExtension \ NSExtensionAttributes` die folgenden Schlüssel hinzu und ändern Sie sie:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (`String` type)
`UNNotificationExtensionDefaultContentHidden` = `YES` (`Boolean` type)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (`Number` type)

![]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Schritt 8: Aktualisieren der Braze-Integration in Ihrer Hauptanwendung

##### Option 1: Laufzeit

Fügen Sie in dem Wörterbuch `appboyOptions`, das zur Konfiguration Ihrer Braze-Instanz verwendet wird, den Eintrag `ABKPushStoryAppGroupKey` hinzu und legen Sie den Wert auf den API-Bezeichner Ihres Workspace fest.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab schnell %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Option 2: Info.plist

Um den Push Story-Arbeitsbereich von Ihrer Datei `Info.plist` aus zu konfigurieren, können Sie auch ein Wörterbuch mit dem Namen `Braze` zu Ihrer Datei `Info.plist` hinzufügen. Fügen Sie im Wörterbuch `Braze` den String-Untereintrag `PushStoryAppGroup` hinzu und legen Sie den Wert auf den Bezeichner Ihres Workspace fest. Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

## Nächste Schritte

Als Nächstes sehen Sie sich die Schritte zur Integration von [Aktionsschaltflächen]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/) an, die erforderlich sind, damit Schaltflächen in einer Push-Story-Nachricht angezeigt werden können.


