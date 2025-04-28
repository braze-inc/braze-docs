---
nav_title: Enregistrer les achats
article_title: Enregistrement des achats pour iOS
platform: Swift
page_order: 4
description: "Cet article de référence montre comment effectuer le suivi des achats et des revenus liés aux messages in-app et comment attribuer des propriétés d'achat pour le SDK Swift."

---

# Enregistrer les achats

Enregistrez les achats réalisés via l’application afin que vous puissiez suivre vos revenus au fil du temps ainsi que les sources de revenus et segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous effectuez dans une devise autre qu’USD seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été enregistrés.

Avant la mise en œuvre, assurez-vous de consulter des exemples des options de segmentation offertes par les événements personnalisés, les attributs personnalisés et les événements d'achat dans nos [meilleures pratiques]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), ainsi que nos notes sur les [conventions de nommage des événements]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Suivi des achats et des revenus

Pour utiliser cette fonction, ajoutez cet appel de méthode après un achat réussi dans votre application :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endtab %}
{% endtabs %}

- Les symboles de devise pris en charge sont les suivants : USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK, etc.
  - Tout autre symbole de devise fourni générera un avertissement enregistré et aucune autre action prise par le SDK.
- L’ID de produit peut comporter un maximum de 255 caractères
- Notez que si l’identifiant du produit est vide, l’achat ne sera pas enregistré dans Braze.

### Ajouter des propriétés {#properties-purchases}
Vous pouvez ajouter des métadonnées sur les achats en transmettant un dictionnaire contenant les valeurs `Int`, `Double`, `String`, `Bool` ou `Date`.

Pour plus de détails, reportez-vous à la [documentation sur les classes iOS ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "(documentation logpurchase)").

### Ajout d’une quantité
Vous pouvez ajouter une quantité à vos achats si les clients effectuent le même achat plusieurs fois au cours d’une même commande. Vous pouvez y parvenir en transmettant un `Int` pour la quantité.

* Une entrée de quantité doit être comprise dans la plage de [0, 100] pour que le SDK enregistre un achat.
* Les méthodes sans entrée de quantité auront une valeur de quantité égale à 1 par défaut.

Pour plus de détails, reportez-vous à la [documentation sur les classes iOS ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/logpurchase(productid:currency:price:quantity:properties:fileid:line:) "(documentation logpurchase)").

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.logPurchase(productId: "product_id", currency: "USD", price: price, quantity: quantity, properties: ["key1":"value1"])
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze logPurchase:productId
                      currency:@"USD"
                         price:price
                      quantity:quantity
                    properties:@{@"checkout_id" : self.checkoutId}];
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

