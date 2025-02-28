---
nav_title: Abzeichen
article_title: Newsfeed Badges für iOS
platform: iOS
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie Badges für den Newsfeed in Ihrer iOS-Anwendung implementieren."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Abzeichen

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Abfrage der Anzahl ungelesener News Feed Karten

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Badges sind eine großartige Möglichkeit, Ihre Nutzer auf neue Inhalte im Newsfeed aufmerksam zu machen. Wenn Sie Ihrem Newsfeed ein Badge hinzufügen möchten, bietet das Braze SDK Methoden zur Abfrage der folgenden Informationen:

- Ungelesene Newsfeed-Karten für den aktuellen Nutzer:in
- Insgesamt sichtbare Newsfeed-Karten für den aktuellen Nutzer:innen

Die folgenden Methodendeklarationen in [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller") beschreiben dies im Detail:

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## Anzeige der Anzahl der ungelesenen Artikel im Newsfeed auf dem Badge der App

Badges dienen nicht nur als Push-Benachrichtigung für eine App, sondern können auch ungesehene Artikel im Nutzer:innen Newsfeed kennzeichnen. Das Update der Anzahl der Badges auf der Grundlage ungelesener Newsfeed-Updates kann ein wertvolles Instrument sein, um Nutzer:innen wieder auf Ihre App zu locken und die Zahl der Sitzungen zu erhöhen.

Rufen Sie diese Methode auf, die die Anzahl der Badges aufzeichnet, nachdem die App geschlossen und die Sitzung des Nutzers beendet wurde:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab schnell %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Implementieren Sie innerhalb dieser Methode den folgenden Code, der den Badge-Zähler aktiv aktualisiert, wenn der Nutzer in einer bestimmten Sitzung Karten ansieht:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab schnell %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

Verwenden Sie an einem beliebigen Punkt, z. B. in der Methode `applicationDidBecomeActive`, den folgenden Code, um die Anzahl der Badges zu löschen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab schnell %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in der `Appboy.h` [Header-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Header File").

