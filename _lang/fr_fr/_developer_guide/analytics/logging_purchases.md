---
nav_title: Enregistrer les achats
article_title: Enregistrement des achats via le SDK de Braze
page_order: 3.2
description: "Découvrez comment enregistrer des achats via le SDK de Braze."

---

# Enregistrer les achats

> Apprenez à enregistrer les achats in-app via le SDK de Braze, afin de pouvoir déterminer vos chiffres d'affaires au fil du temps et selon les différentes sources. Vous pourrez ainsi segmenter les utilisateurs [en fonction de leur valeur vie en]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) utilisant des événements personnalisés, des attributs personnalisés et des événements d'achat.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## Enregistrement des achats et des chiffres d'affaires

Pour enregistrer les achats et les chiffres d'affaires, appelez `logPurchase()` après un achat réussi dans votre application. Si l’identifiant du produit est vide, l’achat ne sera pas enregistré sur Braze.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(context).logPurchase(
   String productId,
   String currencyCode,
   BigDecimal price,
   int quantity
);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(context).logPurchase(
  productId: String,
  currencyCode: String,
  price: BigDecimal,
  quantity: Int
)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
[AppDelegate.braze logPurchase:"product_id"
                      currency:@"USD"
                         price:price];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Si vous souhaitez utiliser Google Tag Manager à la place, vous pouvez utiliser le type d'étiquette **Purchase** pour appeler la [méthode`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Utilisez cette balise pour suivre les achats avec Braze, y compris, en option, les propriétés d’achat. Pour ce faire :

1. Les champs **ID produit** et **Prix** sont obligatoires.
2. Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'achat.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette", l'"ID externe", le "prix", le "code devise", la "quantité" et les "propriétés d'achat".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab Flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

{% endtab %}

{% tab React native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

{% endtab %}

{% tab Unity %}

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

{% endtab %}

{% tab moteur irréel %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` ne peut contenir plus de 255 caractères. En outre, si l'identifiant du produit est vide, l'achat ne sera pas enregistré dans Braze.
{% endalert %}

### Ajouter des propriétés

Vous pouvez ajouter des métadonnées sur les achats en transmettant un dictionnaire contenant les valeurs `Int`, `Double`, `String`, `Bool` ou `Date`.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}

```java
BrazeProperties purchaseProperties = new BrazeProperties();
purchaseProperties.addProperty("key", "value");
Braze.getInstance(context).logPurchase(..., purchaseProperties);
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
val purchaseProperties = BrazeProperties()
purchaseProperties.addProperty("key", "value")
Braze.getInstance(context).logPurchase(..., purchaseProperties)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}

```swift
let purchaseProperties = ["key": "value"]
AppDelegate.braze?.logPurchase(productID: "product_id", currency: "USD", price: price, properties: purchaseProperties)
```

{% endsubtab %}
{% subtab objective-c %}

```objc
NSDictionary *purchaseProperties = @{@"key": @"value"};
[AppDelegate.braze logPurchase:@"product_id"
                      currency:@"USD"
                         price:price
                   properties:purchaseProperties];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Si votre site enregistre les achats à l'aide de l'élément de couche de données d'[événement e-commerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) standard dans Google Tag Manager, vous pouvez utiliser le type d'étiquette **E-commerce Purchase.**  Ce type d’action enregistre un « achat » séparé dans Braze pour chaque article envoyé dans la liste de `items`.

Vous pouvez également préciser les noms supplémentaires des propriétés que vous souhaitez inclure comme propriétés d’achat en spécifiant leurs clés dans la liste des Propriétés d’achat. Veuillez remarquer que Braze observe la personne `item` qui est enregistrée pour toute propriété d’achat que vous ajoutez à la liste.

Par exemple, si l'on considère la charge utile suivante pour le commerce électronique :

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si vous souhaitez transmettre uniquement`item_brand` et `item_name` comme propriétés d’achat, il vous suffit d’ajouter ces deux champs au tableau des propriétés d’achat. Si vous ne fournissez pas de propriétés, aucune propriété d'achat ne sera envoyée dans l'appel à Braze. [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) à Braze.
{% endtab %}

{% tab cordova %}

```javascript
var properties = {};
properties["key"] = "value";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% endtab %}

{% tab Flutter %}

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: {"key": "value"});
```

{% endtab %}

{% tab React native %}

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, { key: "value" });
```

{% endtab %}

{% tab roku %}

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

{% endtab %}

{% tab Unity %}

```csharp
Dictionary<string, object> purchaseProperties = new Dictionary<string, object>
{
    { "key", "value" }
};
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), purchaseProperties);
```

{% endtab %}

{% tab moteur irréel %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### Ajout d’une quantité

Par défaut, `quantity` est défini comme `1`. Toutefois, vous pouvez ajouter une quantité à vos achats si les clients effectuent le même achat plusieurs fois lors d'un même passage en caisse. Pour ajouter une quantité, transmettez à `quantity` une valeur `Int` comprise dans l'intervalle de `[0, 100]`.

### Utiliser l'API REST

Vous pouvez également utiliser notre API REST pour enregistrer les achats. Pour plus d'informations, reportez-vous aux [Endpoints de données utilisateur]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Enregistrement des commandes

Si vous souhaitez enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, vous pouvez utiliser le nom de la commande ou la catégorie de commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## Clés réservées

Les clés suivantes sont réservées et ne peuvent pas être utilisées comme propriétés d’achat :

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Devises prises en charge

Il s'agit des symboles monétaires pris en charge. Tout autre symbole monétaire que vous fournirez fera l'objet d'un avertissement et l'achat ne sera pas enregistré dans Braze.

- `USD`
- `CAD`
- `EUR`
- `GBP`
- `JPY`
- `AUD`
- `CHF`
- `NOK`
- `MXN`
- `NZD`
- `CNY`
- `RUB`
- `TRY`
- `INR`
- `IDR`
- `ILS`
- `SAR`
- `ZAR`
- `AED`
- `SEK`
- `HKD`
- `SPD`
- `DKK`
