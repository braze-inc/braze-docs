{% multi_lang_include developer_guide/prerequisites/swift.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## iOS Einschränkungen

Das iOS-Betriebssystem kann Benachrichtigungen für einige Funktionen ausblenden. Sollten Sie Schwierigkeiten mit diesen Features haben, könnte das iOS-Gate für stille Benachrichtigungen die Ursache sein. Weitere Einzelheiten finden Sie in der Dokumentation zu Apples [Instanz-Methode](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) und [nicht empfangenen Benachrichtigungen](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23).

## Stille Push-Benachrichtigungen einrichten

Wenn Sie stille Push-Benachrichtigungen verwenden möchten, um Aufgaben im Hintergrund zu triggern, müssen Sie Ihre App so konfigurieren, dass sie auch dann Benachrichtigungen erhält, wenn sie sich im Hintergrund befindet. Dazu fügen Sie die Funktion "Background Modes" über das Fenster **Signing & Capabilities** zum Ziel der Haupt-App in Xcode hinzu. Aktivieren Sie das Kontrollkästchen **Fernbenachrichtigungen**.

![Xcode mit dem Kontrollkästchen für den Modus "remote notifications" unter "capabilities".]({% image_buster /assets/img_archive/background_mode.png %} "Hintergrundmodus aktiviert")

Auch wenn der Hintergrundmodus für Remote-Benachrichtigungen aktiviert ist, startet das System Ihre App nicht im Hintergrund, wenn der Nutzer das Beenden der Anwendung erzwungen hat. Der Benutzer muss die Anwendung explizit starten oder das Gerät neu starten, bevor die Anwendung vom System automatisch im Hintergrund gestartet werden kann.

Weitere Informationen finden Sie unter [Pushing Background Updates](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) und in der [Dokumentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Stille Push-Benachrichtigungen senden

Um eine stille Push-Benachrichtigung zu senden, setzen Sie das Flag `content-available` in der Nutzlast einer Push-Benachrichtigung auf `1`. 

{% alert note %}
Was Apple als Remote-Benachrichtigung bezeichnet, ist eine normale Push-Benachrichtigung, bei der das Kennzeichen `content-available` gesetzt ist.
{% endalert %}

Das `content-available` Flag kann sowohl im Braze Dashboard als auch in unserem [Apple Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) in der [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) gesetzt werden.

{% alert warning %}
Es wird davon abgeraten, einen Titel und einen Textkörper mit `content-available=1` anzuhängen, da dies zu undefiniertem Verhalten führen kann. Um sicherzustellen, dass eine Benachrichtigung wirklich stumm ist, schließen Sie sowohl den Titel als auch den Text aus, wenn Sie das `content-available` Flag auf `1.` setzen. Weitere Einzelheiten finden Sie in der offiziellen [Apple-Dokumentation über Hintergrundaktualisierungen](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![Braze-Dashboard mit dem Kontrollkästchen "content-available" auf dem Tab "Einstellungen" des Push-Composers.]({% image_buster /assets/img_archive/remote_notification.png %} "Inhalt verfügbar")

Wenn Sie eine stille Push-Benachrichtigung senden, möchten Sie vielleicht auch einige Daten in die Nutzlast der Benachrichtigung aufnehmen, damit Ihre Anwendung das Event referenzieren kann. Dies könnte Ihnen einige Netzwerkanfragen ersparen und die Reaktionsfähigkeit Ihrer App verbessern.

## Interne Push-Benachrichtigungen ignorieren

Braze verwendet stille Push-Benachrichtigungen, um bestimmte fortschrittliche Features wie Uninstall-Tracking oder Geoofences intern zu verwalten. Wenn Ihre App beim Starten von Anwendungen oder bei Push-Nachrichten im Hintergrund automatische Aktionen ausführt, sollten Sie diese Aktivitäten so steuern, dass sie nicht durch interne Push-Benachrichtigungen ausgelöst werden.

Wenn Sie beispielsweise eine Logik haben, die Ihre Server bei jedem Hintergrund-Push oder Anwendungsstart nach neuen Inhalten fragt, möchten Sie vielleicht verhindern, dass die internen Pushs von Braze getriggert werden, um unnötigen Netzwerkverkehr zu vermeiden. Da Braze bestimmte Arten von internen Pushs an alle Nutzer:innen ungefähr zur gleichen Zeit sendet, kann es zu einer erheblichen Belastung des Servers kommen, wenn die Netzwerkaufrufe beim Start von internen Pushs nicht eingeschränkt werden.

### Schritt 1: Überprüfen Sie Ihre App auf automatische Aktionen

Überprüfen Sie Ihre Anwendung an den folgenden Stellen auf automatische Aktionen und aktualisieren Sie Ihren Code, um die internen Pushes von Braze zu ignorieren:

1. **Push-Empfänger.** Push-Benachrichtigungen im Hintergrund rufen `application:didReceiveRemoteNotification:fetchCompletionHandler:` auf der `UIApplicationDelegate` auf.
2. **App-Delegat.** Pushes im Hintergrund können [angehaltene](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) Apps im Hintergrund starten und dabei die Methoden `application:willFinishLaunchingWithOptions:` und `application:didFinishLaunchingWithOptions:` beim `UIApplicationDelegate` triggern. Überprüfen Sie die `launchOptions` dieser Methoden, um festzustellen, ob die Anwendung durch einen Push im Hintergrund gestartet wurde.

### Schritt 2: Verwenden Sie die interne Push-Utility-Methode

Sie können die statische Utility-Methode in `Braze.Notifications` verwenden, um zu überprüfen, ob Ihre App einen internen Push von Braze erhalten hat oder von diesem gestartet wurde. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) liefert `true` für alle internen Push-Benachrichtigungen von Braze, einschließlich der Synchronisierung von Uninstall-Tracking, Feature-Flags und Geofences.

Zum Beispiel:

{% tabs %}
{% tab schnell %}


```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!Braze.Notifications.isInternalNotification(userInfo)) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}


```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![BRZNotifications isInternalNotification:userInfo]) {
    // Gated logic here (for example pinging server for content)
  }
}
```

{% endtab %}
{% endtabs %}
