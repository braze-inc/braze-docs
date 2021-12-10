---
nav_title: Flux multiples
article_title: Utilisation de plusieurs flux de cartes de contenu pour iOS
platform: iOS
page_order: 6
description: "Cet article de référence couvre comment implémenter plusieurs flux de cartes de contenu dans votre application iOS."
channel:
  - cartes de contenu
---

# Utilisation de plusieurs flux de carte de contenu

Les cartes de contenu peuvent être filtrées sur l'application pour n'afficher que des cartes spécifiques, qui vous permet d'avoir plusieurs flux de cartes de contenu pour différents cas d'utilisation (comme pour avoir un flux "transactionnel" par rapport à un flux "Marketing").

La documentation suivante montre un exemple d'implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir les paires de valeur clé sur les cartes

Lors de la création d'une campagne de la carte de contenu, les données de la paire de valeur clé peuvent être définies sur chaque carte. Notre logique de filtrage utilisera cette paire de données de valeur clé pour catégoriser les cartes.

Pour les besoins de cet exemple, Nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera le flux de la carte de contenu dans lequel la carte doit être affichée. La valeur sera quel que soit votre flux personnalisé, comme dans `Transactionnel`, `Marketing`, et plus.

## Étape 2 : Configurez un écouteur de carte de contenu

Utilisez le code snippet suivant pour ajouter un observateur pour écouter les mises à jour de la carte de contenu.

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

Ajouter les méthodes suivantes pour répondre aux mises à jour de l'observateur et filtrer les cartes retournées par type.

La première méthode, `contentCardsUpdatedNotificationReceiv:`, gère les mises à jour de l'observateur. Il appelle la deuxième méthode, `getCardsForFeedType:`, avec le type de flux désiré, dans ce cas `Transactionnel`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)contentCardsUpdatedNotificationReceived:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification. serInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue] ;
  if (updateIsSuccessful) {
    // Récupère un tableau contenant uniquement les cartes qui ont le type de flux "Transactional" défini dans leurs extras.
    NSArray<ABKContentCard *> *filteredArray = [self getCardsForFeedType:@"Transactional"];
    NSLog(@"On a filtré la table de longueur : %lu", [filteredArray count]);

    // Passez filteredArray à votre couche d'interface utilisateur pour l'affichage.
  }
}

- (NSArray<ABKContentCard *> *)getCardsForFeedType:(NSString *)type {
  NSArray<ABKContentCard *> *cards = [Appboy.sharedInstance. ontentCardsController getContentCards] ;

  NSArray<ABKContentCard *> *filteredArray = [cartes filteredArrayUsingPredicate:[NSPredicate predicateWithBlock:^BOOL(ABKContentCard * card, NSDictionary *bindings) {
    NSDictionary *extras = [card extras];
    si (extras ! nil && [extras objectForKey:@"feed_type"] ! nil && [[extras objectForKey:@"feed_type"] isEqualToString:type]) {
      NSLog(@"Got card: %@ ", carte. dString);
      retourner OUI;
    }
    retour NON;
  }]];

  retour de tableau filtré ;
}
```

{% endtab %}
{% tab SWIFT %}

```swift
@objc privé func contentCardsUpdatedNotificationReceived(notification: NSNotification) {
    garde let updateSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] comme? Bool else { return }
    if updateSuccessful {
        // Récupère un tableau contenant uniquement les cartes qui ont le type de flux "Transactional" défini dans leurs extras.
        let filteredArray = getCards(forFeedType: "Transactional")
        NSLog("Vous avez filtré le tableau de longueur : %@",filteredArray?.count ?? 0)

        // Passez filteredArray à votre couche d'interface utilisateur pour l'affichage.
    }
} }

func getCards(forFeedType type: String) -> [ABKContentCard]? {
    garde laisse allCards = Appboy.sharedInstance()?.contentCardsController.contentCards comme? [ABKContentCard] else { return nil }
    // return les cartes filtrées
    return allCards.filter {
        if $0.extras?["feed_type"] as ? String == type {
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
