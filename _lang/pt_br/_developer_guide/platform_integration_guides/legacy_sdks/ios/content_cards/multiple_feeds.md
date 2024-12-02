---
nav_title: Vários feeds
article_title: Uso de vários cartões de conteúdo para iOS
platform: iOS
page_order: 6
description: "Este artigo de referência aborda a implementação de vários feeds de cartão de conteúdo em seu aplicativo iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Uso de vários feeds de cartão de conteúdo

Os cartões de conteúdo podem ser filtrados no app para exibir apenas cartões específicos, ativando a capacitação para ter vários feeds de cartão de conteúdo para diferentes casos de uso (como ter um feed transacional versus um feed de marketing).

A documentação a seguir demonstra um exemplo de implementação que pode ser alterado para se adequar à sua integração específica.

## Etapa 1: Definição de pares de valores-chave em cartões

Ao criar uma campanha de cartão de conteúdo, os dados do par chave-valor podem ser definidos em cada cartão. Nossa lógica de filtragem usará esses dados do par chave-valor para categorizar os cartões.

Para este exemplo, definiremos um par valor-chave com a chave `feed_type` que designará qual feed do cartão de conteúdo o cartão deve ser exibido. O valor será o valor de seus feeds personalizados, como `Transactional`, `Marketing`, etc.

## Etapa 2: Configurar um ouvinte de cartão de conteúdo

Use o seguinte trecho de código para adicionar um observador para ouvir as atualizações do cartão de conteúdo.

{% tabs %}
{% tab OBJECTIVE C %}

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

Adicione os seguintes métodos para responder às atualizações do observador e filtrar os cartões retornados por tipo.

O primeiro método, `contentCardsUpdatedNotificationReceived:`, lida com as atualizações do observador. Ele chama o segundo método, `getCardsForFeedType:`, com o tipo de feed desejado, nesse caso, `Transactional`.

{% tabs %}
{% tab OBJECTIVE C %}

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
