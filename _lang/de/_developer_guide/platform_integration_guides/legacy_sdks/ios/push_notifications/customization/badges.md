---
nav_title: Abzeichen
article_title: Push-Benachrichtigung Badge Counts für iOS
platform: iOS
page_order: 3.1
description: "Dieser Referenzartikel beschreibt, wie Sie Badge-Zählungen in Ihren iOS-Push-Benachrichtigungen implementieren."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Abzeichen

Sie können die gewünschte Anzahl der Badges angeben, wenn Sie eine Push-Benachrichtigung über das Braze-Dashboard verfassen. Sie können die Anzahl der Badges auch manuell über die Eigenschaft [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) Ihrer Anwendung oder die [remote Benachrichtigungs-Payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1) aktualisieren. Braze löscht auch die Anzahl der Badges, wenn eine Braze-Benachrichtigung empfangen wird, während die App im Vordergrund ist. 

Wenn Sie nicht vorhaben, die Badges im Rahmen des normalen Betriebs der App oder durch das Senden von Push-Nachrichten zu löschen, sollten Sie die Badges löschen, wenn die App aktiv wird, indem Sie den folgenden Code in die Delegate-Methode `applicationDidBecomeActive:` Ihrer App einfügen:

{% tabs %}
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
{% endtabs %}

Beachten Sie, dass das Setzen der Badge-Nummer auf 0 auch die Benachrichtigungen in der Benachrichtigungszentrale löscht. Auch wenn Sie die Badge-Nummer in den Push-Payloads nicht festlegen, können Sie die Badge-Nummer auf 0 setzen, um die Push-Benachrichtigung(en) im Notification Center zu entfernen, nachdem die Nutzer:innen auf den Push geklickt haben.

