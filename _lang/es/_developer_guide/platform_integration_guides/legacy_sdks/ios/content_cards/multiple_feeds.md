---
nav_title: Múltiples fuentes
article_title: Uso de múltiples fuentes de tarjetas de contenido para iOS
platform: iOS
page_order: 6
description: "En este artículo de referencia se cubre la implementación de múltiples fuentes de tarjetas de contenido en tu aplicación iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Utilizar varias fuentes de tarjetas de contenido

Las tarjetas de contenido pueden filtrarse en la aplicación para mostrar sólo tarjetas específicas, lo que te habilita para tener varias fuentes de tarjetas de contenido para diferentes casos de uso (como tener una fuente transaccional frente a una fuente de marketing).

La siguiente documentación muestra un ejemplo de implementación que puede modificarse para adaptarlo a tu integración específica.

## Paso 1: Configuración de los pares clave-valor en las tarjetas

Al crear una campaña de tarjeta de contenido, se pueden establecer datos de par clave-valor en cada tarjeta. Nuestra lógica de filtrado utilizará estos datos par clave-valor para categorizar las tarjetas.

En este ejemplo, estableceremos un par clave-valor con la clave `feed_type` que designará la fuente de la tarjeta de contenido que debe mostrarse. El valor será el que tengan tus fuentes personalizadas, como `Transactional`, `Marketing`, etc.

## Paso 2: Configurar una escucha de tarjeta de contenido

Utiliza el siguiente fragmento de código para añadir un observador que escuche las actualizaciones de la tarjeta de contenido.

{% tabs %}
{% tab OBJETIVO-C %}

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

Añade los siguientes métodos para responder a las actualizaciones del observador y filtrar las tarjetas devueltas por tipo.

El primer método, `contentCardsUpdatedNotificationReceived:`, se encarga de las actualizaciones del observador. Llama al segundo método, `getCardsForFeedType:`, con el tipo de fuente deseado, en este caso, `Transactional`.

{% tabs %}
{% tab OBJETIVO-C %}

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
