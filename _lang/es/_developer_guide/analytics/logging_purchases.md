---
nav_title: Registrar compras
article_title: Registro de compras a través del SDK de Braze
page_order: 3.2
description: "Aprende a registrar compras a través del SDK de Braze."

---

# Registrar compras

> Aprende a registrar las compras dentro de la aplicación a través del SDK de Braze, para que puedas determinar tus ingresos a lo largo del tiempo y a través de distintas fuentes. Esto te permitirá segmentar a los usuarios en función [de su valor de duración]({{site.baseurl}}/developer_guide/analytics/#purchase-events--revenue-tracking) utilizando eventos personalizados, atributos personalizados y eventos de compra.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente.
{% endalert %}

## Compras e ingresos por tala de árboles

Para registrar las compras y los ingresos, llama a `logPurchase()` después de una compra exitosa en tu aplicación. Si el identificador del producto está vacío, la compra no se registrará en Braze.

{% tabs %}
{% tab Android %}
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

{% tab Web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

Si quieres utilizar Google Tag Manager en su lugar, puedes utilizar el tipo de etiqueta **Compra** para llamar al [método`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase). Utiliza esta etiqueta para hacer un seguimiento de las compras a Braze, incluyendo opcionalmente las propiedades de la compra. Para ello:

1. Los campos **ID de producto** y **Precio** son obligatorios.
2. Utiliza el botón **Añadir fila** para añadir propiedades de la compra.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta", "ID externo", "precio", "código de moneda", "cantidad" y "propiedades de la compra".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})
{% endtab %}

{% tab Cordova %}

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

{% tab nativo de react %}

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

{% tab motor unreal engine %}

```cpp
UBraze->LogPurchase(TEXT("product_id"), TEXT("USD"), price, quantity);
```

{% endtab %}
{% endtabs %}

{% alert warning %}
`productID` sólo puede tener un máximo de 255 caracteres. Además, si el identificador del producto está vacío, la compra no se registrará en Braze.
{% endalert %}

### Añadir propiedades

Puedes añadir metadatos sobre las compras pasando un Diccionario rellenado con los valores `Int`, `Double`, `String`, `Bool`, o `Date`.

{% tabs %}
{% tab Android %}
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

{% tab Web %}
Para una implementación estándar del SDK Web, puedes utilizar el siguiente método:

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

Si tu sitio registra las compras utilizando el elemento estándar de la capa de datos de [eventos de comercio electrónico](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) de Google Tag Manager, entonces puedes utilizar el tipo de etiqueta **Compra de comercio electrónico**. Este tipo de acción registrará una "compra" separada en Braze para cada artículo enviado en la lista de `items`.

También puedes especificar nombres de propiedades adicionales que quieras incluir como propiedades de la compra especificando sus claves en la lista Propiedades de la compra. Ten en cuenta que Braze buscará en el `item` individual que se está registrando cualquier propiedad de la compra que añadas a la lista.

Por ejemplo, dada la siguiente carga útil de comercio electrónico:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si sólo quieres que `item_brand` y `item_name` se pasen como propiedades de la compra, sólo tienes que añadir esos dos campos a la tabla de propiedades de la compra. Si no proporcionas ninguna propiedad, no se enviará ninguna propiedad de la compra en la [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) llamada a Braze.
{% endtab %}

{% tab Cordova %}

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

{% tab nativo de react %}

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

{% tab motor unreal engine %}

```cpp
TMap<FString, FString> PurchaseProperties;
PurchaseProperties.Add(TEXT("key"), TEXT("value"));

UBraze->LogPurchaseWithProperties(TEXT("product_id"), TEXT("USD"), price, quantity, PurchaseProperties);
```

{% endtab %}
{% endtabs %}

### Añadir cantidad

Por predeterminado, `quantity` está configurado como `1`. Sin embargo, puedes añadir una cantidad a tus compras si los clientes realizan la misma compra varias veces en un mismo proceso de pago. Para añadir una cantidad, pasa un valor `Int` a `quantity`.

### Utilizar la API REST

También puedes utilizar nuestra API REST para registrar las compras. Para más información, consulta [Puntos finales de datos de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Registro de pedidos

Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

## Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Divisas admitidas

Estos son los símbolos de moneda admitidos. Cualquier otro símbolo de moneda que proporciones registrará una advertencia y la compra no se registrará en Braze.

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
