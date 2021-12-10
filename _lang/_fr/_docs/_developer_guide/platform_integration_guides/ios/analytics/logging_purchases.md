---
nav_title: Achats de journalisation
article_title: Achats de journalisation pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les revenus dans l'application et attribuer des propriétés d'achat dans votre application iOS."
---

# Enregistrement des achats pour iOS

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés vs. achetez des événements dans notre section [Meilleures pratiques][5], ainsi que nos notes sur [les conventions de nommage d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi des achats et des revenus

Pour utiliser cette fonctionnalité, ajoutez cette méthode d'appel après un achat réussi dans votre application :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"votre ID de produit"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("votre ID de produit", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Les symboles monétaires pris en charge comprennent : USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, et plus.
  - Tout autre symbole de devise fourni donnera lieu à un avertissement et aucune autre action du SDK.
- L'ID du produit peut avoir un maximum de 255 caractères
- Veuillez noter que si l'identifiant du produit est vide, l'achat ne sera pas enregistré en Brésil.

### Ajout de propriétés {#properties-purchases}
Vous pouvez ajouter des métadonnées sur les achats en passant un `NSDictionary` rempli avec `NSNumber`, `NSString`, ou `valeurs NSDate`.

Veuillez consulter la documentation de la classe [iOS pour plus de détails][8].

### Ajout de la quantité
Vous pouvez ajouter une quantité à vos achats si les clients font le même achat plusieurs fois en un seul paiement. Vous pouvez accomplir cela en passant un `NSUInteger` pour la quantité.

* Une entrée de quantité doit être dans la plage de [0, 100] pour que le SDK enregistre un achat.
* Les méthodes sans entrée de quantité auront une valeur de quantité par défaut de 1.
* Les méthodes avec une quantité n'ont pas de valeur par défaut et **doivent** recevoir une entrée de quantité pour le SDK pour enregistrer un achat.

Veuillez consulter la documentation de la classe [iOS pour plus de détails][7].

> Si vous passez une valeur de 10 USD, et une quantité de 3 puis qui se connectera au profil de l'utilisateur comme 3 achats de 10 dollars pour un total de 30 dollars.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"votre ID de produit"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("votre ID de produit", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

Consultez la [Documentation Technique][6] pour plus d'informations.

### Clés réservées

Les clés suivantes sont __RÉSERVÉES__ et __NE PEUT PAS__ être utilisées comme propriétés d'achat:

- `Heure`
- `identifiant_produit`
- `Quantité`
- `nom_événement`
- `prix`
- `Devise`

**Informations supplémentaires

- Voir la déclaration de méthode dans le fichier [`Appboy.h`][2]. - De plus, vous pouvez vous référer à la documentation [logPurchase]() pour plus d'informations.

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer vos achats. Reportez-vous à la documentation [de l'API utilisateur][4] pour plus de détails.

[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[6]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ad35bb238aaa4fe9d1ede0439a4c401db "logcustomevent:withproperties documentation"
[7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa "logpurchase w/ quantity class documentation"
[8]: http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc "logpurchase w/ properties class documentation"
