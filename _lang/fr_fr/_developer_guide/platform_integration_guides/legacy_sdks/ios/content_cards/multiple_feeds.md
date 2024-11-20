---
nav_title: Flux multiples
article_title: Utilisation de plusieurs flux de carte de contenu pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence explique l’implémentation de plusieurs flux de carte de contenu dans votre application iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Utilisation de plusieurs flux de carte de contenu

Les cartes de contenu peuvent être filtrées sur l’application pour afficher uniquement des cartes spécifiques, ce qui vous permet d’avoir plusieurs flux de carte de contenu pour différents cas d’usage (comme avoir un flux transactionnel ou un flux marketing).

La documentation suivante montre un exemple d’implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir des paires clé-valeur sur les cartes

Lors de la création d’une campagne de carte de contenu, les données de paires clé-valeur peuvent être définies pour chaque carte. Notre logique de filtrage utilisera les données de cette paire clé-valeur pour catégoriser les cartes.

Pour cet exemple, nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera dans quel flux la carte de contenu doit s’afficher. La valeur sera ce qu’est votre flux personnalisé, comme dans `Transactional`, `Marketing` etc.

## Étape 2 : Configurer un auditeur de carte de contenu

Utilisez l’extrait de code suivant pour ajouter un observateur à l’écoute des mises à jour de la carte de contenu.

{% tabs %}
{% tab OBJECTIF-C %}

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

Ajoutez les méthodes suivantes pour répondre aux mises à jour de l’observateur et filtrer les cartes retournées par type.

La première méthode, `contentCardsUpdatedNotificationReceived:`, gère les mises à jour de l’observateur. Il appelle la deuxième méthode, `getCardsForFeedType:`, avec le type de flux souhaité, dans ce cas, `Transactional`.

{% tabs %}
{% tab OBJECTIF-C %}

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
