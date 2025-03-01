---
nav_title: Ignorieren von internen Push-Benachrichtigungen
article_title: Braze-interne Push-Benachrichtigungen für iOS ignorieren
platform: iOS
page_order: 4
description: "Dieser Referenzartikel beschreibt, wie interne Push-Benachrichtigungen von Braze ignoriert werden können."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Interne Push-Benachrichtigungen von Braze ignorieren

Braze verwendet stille Push-Benachrichtigungen für die interne Implementierung bestimmter erweiterter Funktionen. Bei den meisten Integrationen erfordert dies keine Änderungen an Ihrer App. Wenn Sie jedoch eine Braze-Funktion integrieren, die auf interne Push-Benachrichtigungen angewiesen ist (z. B. Deinstallations-Tracking oder Geofences), sollten Sie Ihre App so aktualisieren, dass sie unsere internen Push-Benachrichtigungen ignoriert.

Wenn Ihre App beim Starten von Anwendungen oder bei Push-Nachrichten im Hintergrund automatisch Aktionen ausführt, sollten Sie in Erwägung ziehen, diese Aktivitäten so zu steuern, dass sie nicht durch interne Push-Benachrichtigungen ausgelöst werden. Wenn Sie beispielsweise eine Logik haben, die Ihre Server bei jedem Hintergrund-Push oder Anwendungsstart nach neuen Inhalten fragt, möchten Sie wahrscheinlich nicht, dass unsere internen Pushs dies auslösen, da dies unnötigen Netzwerkverkehr verursachen würde. Da Braze außerdem bestimmte Arten von internen Push-Nachrichten an alle Benutzer ungefähr zur gleichen Zeit sendet, könnten Netzwerkaufrufe beim Start von internen Push-Nachrichten zu einer erheblichen Serverbelastung führen, wenn sie nicht unterbrochen werden.

## Überprüfen Sie Ihre App auf automatische Aktionen

Sie sollten Ihre Anwendung an den folgenden Stellen auf automatische Aktionen überprüfen und Ihren Code aktualisieren, um unsere internen Pushes zu ignorieren:

1. **Push-Empfänger.** Push-Benachrichtigungen im Hintergrund rufen `application:didReceiveRemoteNotification:fetchCompletionHandler:` auf der `UIApplicationDelegate` auf.
2. **App-Delegat.** Pushes im Hintergrund können [angehaltene](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/TheAppLifeCycle/TheAppLifeCycle.html#//apple_ref/doc/uid/TP40007072-CH2-SW3) Apps im Hintergrund starten und dabei die Methoden `application:willFinishLaunchingWithOptions:` und `application:didFinishLaunchingWithOptions:` beim `UIApplicationDelegate` triggern. Sie können die `launchOptions` dieser Methoden überprüfen, um festzustellen, ob die Anwendung durch einen Push im Hintergrund gestartet wurde.

## Verwendung der internen Push-Utility-Methoden von Braze

Sie können die Utility-Methoden in `ABKPushUtils` verwenden, um zu überprüfen, ob Ihre App eine interne Push-Benachrichtigung von Braze erhalten hat oder durch eine solche gestartet wurde. `isAppboyInternalRemoteNotification:` gibt `YES` für alle internen Push-Benachrichtigungen von Braze zurück, während `isUninstallTrackingRemoteNotification:` und `isGeofencesSyncRemoteNotification:` `YES` für Tracking-Benachrichtigungen zur Deinstallation bzw. für Synchronisierungsbenachrichtigungen von Geofences zurückgeben. Siehe [`ABKPushUtils.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKPushUtils.h) für Methodendeklarationen.

## Implementierungsbeispiel {#internal-push-implementation-example}

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  NSDictionary *pushDictionary = launchOptions[UIApplicationLaunchOptionsRemoteNotificationKey];
  BOOL launchedFromAppboyInternalPush = pushDictionary && [ABKPushUtils isAppboyInternalRemoteNotification:pushDictionary];
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
  if (![ABKPushUtils isAppboyInternalRemoteNotification:userInfo]) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% tab schnell %}

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {
  let pushDictionary = launchOptions?[UIApplicationLaunchOptionsKey.remoteNotification] as? NSDictionary as? [AnyHashable : Any] ?? [:]
  let launchedFromAppboyInternalPush = ABKPushUtils.isAppboyInternalRemoteNotification(pushDictionary)
  if (!launchedFromAppboyInternalPush) {
    // ... Gated logic here (such as pinging your server to download content) ...
  }
}
```

```swift
func application(_ application: UIApplication,
                 didReceiveRemoteNotification userInfo: [AnyHashable : Any],
                 fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
  if (!ABKPushUtils.isAppboyInternalRemoteNotification(userInfo)) {
    // ... Gated logic here (such as pinging server for content) ...
  }
}
```

{% endtab %}
{% endtabs %}

