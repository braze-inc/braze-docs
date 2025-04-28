---
nav_title: Enregistrer les achats
article_title: Enregistrement des achats pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment suivre les achats et les revenus dans l’application et attribuer des propriétés d’achat dans votre application iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Enregistrement des achats pour iOS

Enregistrez les achats réalisés via l’application afin que vous puissiez suivre vos revenus au fil du temps ainsi que les sources de revenus et segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi des achats et des revenus

Pour utiliser cette fonction, ajoutez cet appel de méthode après un achat réussi dans votre application :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"))
```

{% endtab %}
{% endtabs %}

- Les symboles de devise pris en charge sont les suivants : USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, etc.
  - Tout autre symbole de devise fourni générera un avertissement enregistré et aucune autre action prise par le SDK.
- L’ID de produit peut comporter un maximum de 255 caractères
- Notez que si l’identifiant du produit est vide, l’achat ne sera pas enregistré dans Braze.

### Ajouter des propriétés {#properties-purchases}

Vous pouvez ajouter des métadonnées sur les achats en passant soit un [tableau de propriétés d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects), soit en passant un `NSDictionary` rempli avec des valeurs de `NSNumber`, `NSString` ou `NSDate`.

Pour plus de détails, consultez la [documentation de la classe iOS ](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc "(documentation sur la classe logpurchase avec propriétés)").

### Ajout d’une quantité
Vous pouvez ajouter une quantité à vos achats si les clients effectuent le même achat plusieurs fois au cours d’une même commande. Vous pouvez y parvenir en transmettant un `NSUInteger` pour la quantité.

* Une entrée de quantité doit être comprise dans la plage de [0, 100] pour que le SDK enregistre un achat.
* Les méthodes sans entrée de quantité auront une valeur de quantité égale à 1 par défaut.
* Les méthodes avec une entrée de quantité n'ont pas de valeur par défaut et **doivent** recevoir une entrée de quantité pour que le SDK puisse enregistrer un achat.

Pour plus de détails, reportez-vous à la [documentation de la classe iOS ](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa "(documentation de la classe logpurchase avec quantité)").

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[[Appboy sharedInstance] logPurchase:@"your product ID"
inCurrency:@"USD"
atPrice:[[[NSDecimalNumber alloc] initWithString:@"0.99"] autorelease]
withProperties:@{@"key1":"value1"}];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logPurchase("your product ID", inCurrency: "USD", atPrice: NSDecimalNumber(string: "0.99"), withProperties: ["key1":"value1"])
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Si vous transmettez une valeur de 10 USD et une quantité de 3, cela s’enregistrera dans le profil de l’utilisateur comme trois achats de 10 dollars pour un total de 30 dollars.
{% endalert %}

### Journaliser les achats au niveau de la commande
Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Reportez-vous à la [Documentation de l'API utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) pour plus de détails.

