---
nav_title: Registrar compras
article_title: Registro de compras para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia muestra cómo hacer un seguimiento de las compras e ingresos dentro de la aplicación y asignar propiedades de la compra en tu aplicación iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Registrar compras para iOS

Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y a través de las fuentes de ingresos, y segmenta a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar los ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), así como nuestras notas sobre [las convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Seguimiento de compras e ingresos

Para utilizar esta característica, añade esta llamada al método después de una compra con éxito en tu aplicación:

{% tabs %}
{% tab OBJETIVO-C %}

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

- Los símbolos de moneda admitidos son: USD, CAD, EUR, GBP, JPY, AUD, CHF, NOK, MXN, NZD, CNY, RUB, TRY, INR, IDR, ILS, SAR, ZAR, AED, SEK, HKD, SPD, DKK y más.
  - Cualquier otro símbolo de moneda proporcionado dará lugar a una advertencia registrada y el SDK no tomará ninguna otra medida.
- El ID del producto puede tener un máximo de 255 caracteres
- Ten en cuenta que si el identificador del producto está vacío, la compra no se registrará en Braze.

### Añadir propiedades {#properties-purchases}

Puedes añadir metadatos sobre compras pasando una [matriz de propiedades de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) o pasando un `NSDictionary` rellenado con valores de `NSNumber`, `NSString` o `NSDate`.

Consulta la [documentación de la clase iOS](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aaca4b885a8f61ac9fad3936b091448cc " logpurchase w/ properties") para obtener más detalles.

### Añadir cantidad
Puedes añadir una cantidad a tus compras si los clientes realizan la misma compra varias veces en un mismo proceso de pago. Puedes conseguirlo introduciendo una `NSUInteger` para la cantidad.

* Una cantidad introducida debe estar en el rango de [0, 100] para que el SDK registre una compra.
* Los métodos sin entrada de cantidad tendrán un valor de cantidad predeterminado de 1.
* Los métodos con una entrada de cantidad no tienen un valor predeterminado, y **deben** recibir una entrada de cantidad para que el SDK registre una compra.

Consulta la [documentación de la clase  iOS compra](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ab50403068be47c0acba9943583e259fa "con documentación de la clase cantidad") para obtener más detalles.

{% tabs %}
{% tab OBJETIVO-C %}

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
Si introduces un valor de 10 dólares y una cantidad de 3, eso se registrará en el perfil del usuario como tres compras de 10 dólares por un total de 30 dólares.
{% endalert %}

### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Claves reservadas

Las siguientes claves están reservadas y no pueden utilizarse como propiedades de la compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

### API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la [documentación de la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

