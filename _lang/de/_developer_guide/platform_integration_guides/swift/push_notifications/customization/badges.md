---
nav_title: Abzeichen
article_title: Push-Benachrichtigung Badge Counts für iOS
platform: Swift
page_order: 2
description: "Dieser Artikel beschreibt, wie Sie iOS Badge-Zählungen für das Swift SDK implementieren."
channel:
  - push

---

# Abzeichen

> Badges sind kleine Symbole, die dazu dienen, die Aufmerksamkeit eines Benutzers zu gewinnen. Sie können die Anzahl der Badges in den [**Einstellungen**]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/) Tab festlegen, wenn Sie eine Push-Benachrichtigung über das Dashboard von Braze erstellen. Sie können die Anzahl der Badges auch manuell über die Eigenschaft [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) Ihrer Anwendung oder die [remote Benachrichtigungs-Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1) aktualisieren. 

Braze löscht automatisch die Anzahl der Badges, wenn eine Braze-Benachrichtigung empfangen wird, während die App im Vordergrund ist. Wenn Sie die Badge-Nummer manuell auf 0 setzen, werden auch die Benachrichtigungen in der Benachrichtigungszentrale gelöscht. 

Wenn Sie nicht vorhaben, die Badges im Rahmen des normalen Betriebs der App oder durch das Senden von Push-Nachrichten zu löschen, sollten Sie die Badges löschen, wenn die App aktiv wird, indem Sie den folgenden Code in die Delegate-Methode `applicationDidBecomeActive:` Ihrer App einfügen:

{% tabs %}
{% tab schnell %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

