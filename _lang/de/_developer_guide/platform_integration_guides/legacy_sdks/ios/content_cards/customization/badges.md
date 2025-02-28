---
nav_title: Abzeichen
article_title: Content Card Badges für iOS
platform: iOS
page_order: 5
description: "Dieser Artikel behandelt das Hinzufügen von Badges zu Ihren Content Cards in Ihrer iOS-Anwendung."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Abzeichen

## Abfrage der Anzahl ungelesener Inhaltskarten

Wenn Sie die Anzahl der ungelesenen Inhaltskarten Ihres Benutzers anzeigen möchten, empfehlen wir Ihnen, die Anzahl der Karten abzufragen und diese mit einem Badge darzustellen. Badges sind eine großartige Möglichkeit, um Ihre Nutzer auf neue Inhalte in den Content-Cards aufmerksam zu machen. Wenn Sie Ihren Content-Cards ein Badge hinzufügen möchten, bietet das Braze SDK Methoden zur Abfrage der folgenden Informationen:

- Ungelesene Inhaltskarten für den aktuellen Benutzer
- Gesamtzahl der sichtbaren Inhaltskarten für den aktuellen Benutzer

Die folgenden Methodendeklarationen in [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) beschreiben dies im Detail:

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## Anzeige der Anzahl der ungesehenen Inhaltskarten auf der App-Badge-Anzeige

Badges dienen nicht nur als Push-Benachrichtigung für eine App, sondern können auch verwendet werden, um ungesehene Elemente im Content Cards Feed des Benutzers zu kennzeichnen. Das Aktualisieren des Badge-Zählers auf der Basis von nicht aufgerufenen Content-Card-Updates kann dazu beitragen, Nutzer wieder auf Ihre App aufmerksam zu machen und die Anzahl der Sitzungen zu erhöhen.

Diese Methode erfasst den Badge-Zähler, nach dem die App geschlossen und die Sitzung beendet wurde:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn der Nutzer in einer bestimmten Sitzung Karten ansieht:

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab schnell %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn der Nutzer in einer bestimmten Sitzung Karten ansieht:

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in der [Header-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
