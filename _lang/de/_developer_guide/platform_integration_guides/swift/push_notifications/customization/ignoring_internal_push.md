---
nav_title: Internen Push ignorieren
article_title: Braze-interne Push-Benachrichtigungen für iOS ignorieren
platform: Swift
page_order: 6
description: "Dieser Artikel beschreibt, wie Sie interne Push-Benachrichtigungen von Braze für das Swift SDK ignorieren können."
channel:
  - push

---

# Interne Push-Benachrichtigungen ignorieren

> Braze verwendet [stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) für die interne Implementierung bestimmter fortschrittlicher Features. Bei den meisten Integrationen erfordert dies keine Änderungen an Ihrer App. Wenn Sie jedoch eine Braze-Funktion integrieren, die auf interne Push-Benachrichtigungen angewiesen ist (z. B. Deinstallations-Tracking oder Geofences), sollten Sie Ihre App so aktualisieren, dass sie unsere internen Push-Benachrichtigungen ignoriert.

Wenn Ihre App beim Starten von Anwendungen oder bei Push-Nachrichten im Hintergrund automatisch Aktionen ausführt, sollten Sie diese Aktivitäten so einschränken, dass sie nicht durch unsere internen Push-Benachrichtigungen ausgelöst werden. Wenn Sie beispielsweise eine Logik haben, die Ihre Server bei jedem Push im Hintergrund oder beim Start einer Anwendung nach neuen Inhalten fragt, möchten Sie wahrscheinlich nicht, dass die internen Pushs von Braze dies triggern, da dies zu unnötigem Netzwerkverkehr führen würde. Da Braze außerdem bestimmte Arten von internen Push-Nachrichten an alle Benutzer ungefähr zur gleichen Zeit sendet, könnten Netzwerkaufrufe beim Start von internen Push-Nachrichten zu einer erheblichen Serverbelastung führen, wenn sie nicht unterbrochen werden.

## Überprüfen Sie Ihre App auf automatische Aktionen

Überprüfen Sie Ihre Anwendung an den folgenden Stellen auf automatische Aktionen und aktualisieren Sie Ihren Code, um die internen Pushes von Braze zu ignorieren:

1. **Push-Empfänger.** Push-Benachrichtigungen im Hintergrund rufen `application:didReceiveRemoteNotification:fetchCompletionHandler:` auf der `UIApplicationDelegate` auf.
2. **App-Delegat.** Pushes im Hintergrund können [angehaltene](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle) Apps im Hintergrund starten und dabei die Methoden `application:willFinishLaunchingWithOptions:` und `application:didFinishLaunchingWithOptions:` beim `UIApplicationDelegate` triggern. Überprüfen Sie die `launchOptions` dieser Methoden, um festzustellen, ob die Anwendung durch einen Push im Hintergrund gestartet wurde.

## Verwendung der internen Push-Utility-Methode

Sie können die statische Utility-Methode in `Braze.Notifications` verwenden, um zu überprüfen, ob Ihre App einen internen Push von Braze erhalten hat oder von diesem gestartet wurde. [`Braze.Notifications.isInternalNotification(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/isinternalnotification(_:)) liefert `true` für alle internen Push-Benachrichtigungen von Braze, einschließlich der Synchronisierung von Uninstall-Tracking, Feature-Flags und Geofences.

## Implementierungsbeispiel {#internal-push-implementation-example}

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

