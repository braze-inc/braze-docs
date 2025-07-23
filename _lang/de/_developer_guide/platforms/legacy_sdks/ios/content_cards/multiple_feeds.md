---
nav_title: Mehrere Feeds
article_title: Mehrere Content Card Feeds für iOS verwenden
platform: iOS
page_order: 6
description: "Dieser Referenzartikel behandelt die Implementierung mehrerer Content Card Feeds in Ihrer iOS-Anwendung."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Verwendung mehrere Content-Card-Feeds

Content Cards können in der App gefiltert werden, so dass nur bestimmte Karten angezeigt werden. So können Sie mehrere Content Card Feeds für verschiedene Anwendungsfälle haben (z.B. einen Transaktions-Feed und einen Marketing-Feed).

Die folgende Dokumentation zeigt eine Beispielimplementierung, die an Ihre spezifische Integration angepasst werden kann.

## Schritt 1: Schlüssel-Wert-Paare auf Karten setzen

Bei der Erstellung einer Content-Card-Kampagne können für jede Karte Schlüssel-Wert-Paare festgelegt werden. Unsere Filterlogik wird diese Schlüssel-Wert-Paar-Daten verwenden, um die Karten zu kategorisieren.

In diesem Beispiel legen wir ein Schlüssel-Wert-Paar mit dem Schlüssel `feed_type` fest, um anzugeben, welcher Content-Card-Feed angezeigt werden soll. Der Wert entspricht dem Ihrer benutzerdefinierten Feeds, z. B. `Transactional`, `Marketing`, usw.

## Schritt 2: Einrichten eines Inhaltskarten-Hörers

Verwenden Sie das folgende Code-Snippet, um einen Beobachter hinzuzufügen, der auf Content-Card-Updates wartet.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                           selector:@selector(contentCardsUpdatedNotificationReceived:)
                                               name:ABKContentCardsProcessedNotification
                                             object:nil];
```

{% endtab %}
{% tab SWIFT %}

```swift
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

{% endtab %}
{% endtabs %}

Fügen Sie die folgenden Methoden hinzu, um auf Updates vom Beobachter zu reagieren und die zurückgegebenen Karten nach Typ zu filtern.

Die erste Methode, `contentCardsUpdatedNotificationReceived:`, verarbeitet Updates vom Beobachter. Sie ruft die zweite Methode, `getCardsForFeedType:`, mit dem gewünschten Feed-Typ – in diesem Fall `Transactional` – auf.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)contentCardsUpdatedNotificationReceived:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // Get an array containing only cards that have the "Transactional" feed type set in their extras.
    NSArray<ABKContentCard *> *filteredArray = [self getCardsForFeedType:@"Transactional"];
    NSLog(@"Got filtered array of length: %lu", [filteredArray count]);

    // Pass filteredArray to your UI layer for display.
  }
}

- (NSArray<ABKContentCard *> *)getCardsForFeedType:(NSString *)type {
  NSArray<ABKContentCard *> *cards = [Appboy.sharedInstance.contentCardsController getContentCards];

  NSArray<ABKContentCard *> *filteredArray = [cards filteredArrayUsingPredicate:[NSPredicate predicateWithBlock:^BOOL(ABKContentCard * card, NSDictionary *bindings) {
    NSDictionary *extras = [card extras];
    if (extras != nil && [extras objectForKey:@"feed_type"] != nil && [[extras objectForKey:@"feed_type"] isEqualToString:type]) {
      NSLog(@"Got card: %@ ", card.idString);
      return YES;
    }
    return NO;
  }]];

  return filteredArray;
}
```

{% endtab %}
{% tab SWIFT %}

```swift
@objc private func contentCardsUpdatedNotificationReceived(notification: NSNotification) {
    guard let updateSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool else { return }
    if updateSuccessful {
        // Get an array containing only cards that have the "Transactional" feed type set in their extras.
        let filteredArray = getCards(forFeedType: "Transactional")
        NSLog("Got filtered array of length: %@",filteredArray?.count ?? 0)

        // Pass filteredArray to your UI layer for display.
    }
}

func getCards(forFeedType type: String) -> [ABKContentCard]? {
    guard let allCards = Appboy.sharedInstance()?.contentCardsController.contentCards as? [ABKContentCard] else { return nil }
    // return filtered cards
    return allCards.filter {
        if $0.extras?["feed_type"] as? String == type {
            NSLog("%@","Got card: \($0.idString)")
            return true
        } else {
            return false
        }
    }
}
```

{% endtab %}
{% endtabs %}
