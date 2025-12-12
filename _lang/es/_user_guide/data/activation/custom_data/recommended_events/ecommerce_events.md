---
nav_title: Eventos recomendados en eCommerce
article_title: Eventos recomendados por eCommerce
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artículo de referencia describe los eventos y propiedades recomendados para el comercio electrónico, su uso, segmentación, dónde ver los análisis relevantes y mucho más."
---

# Eventos recomendados en eCommerce

> Esta página cubre los eventos y propiedades recomendados para el comercio electrónico. Estos eventos se crean para captar los comportamientos de compra clave que los especialistas en marketing necesitan para desencadenar una mensajería eficaz, como la dirigida a los carritos abandonados.

{% alert important %}
Los eventos recomendados por eCommerce están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si utilizas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}

Braze reconoce que la planificación de datos lleva tiempo. Animamos a nuestros clientes a que familiaricen a sus equipos de desarrolladores y empiecen ya a enviar estos eventos. Aunque algunas características pueden no estar disponibles inmediatamente con los eventos recomendados para el comercio electrónico, puedes esperar la introducción de nuevos productos a lo largo de 2025 que mejorarán tus capacidades de comercio electrónico.

## Tipos de eventos recomendados para el comercio electrónico

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Cualquier divisa que no sea USD se mostrará en Braze en USD según la tasa de cambio de la fecha en que se informó. Para evitar la conversión de divisas, codifícalas en USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Puedes utilizar el evento producto visto para desencadenar el evento cuando un cliente vea la página de detalles de un producto.

#### Propiedades

| Nombre de la propiedad | Necesario | Tipo de datos | Descripción | 
|---|---|---|---|
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. <br> Para los clientes que no son de Shopify, será el valor que establezcas para los ID de artículos de catálogo, como las SKU. |
| `product_name` | Sí | Cadena | El nombre del producto visualizado. | 
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `price` | Sí | Flotador | El precio unitario variante del producto en el momento de verlo. |
| `currency` | Sí | Cadena | La moneda en la que se indica el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto | |
| `type` | No | Objeto | Funciona con [notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) y [notificaciones de bajada de precios]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.product_viewed", {
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": {
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
BrazeProperties properties = new BrazeProperties()
    .addProperty("product_id", "4111176")
    .addProperty("product_name", "Torchie runners")
    .addProperty("variant_id", "4111176700")
    .addProperty("image_url", "https://braze-apparel.com/images/products/large/torchie-runners.jpg")
    .addProperty("product_url", "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/")
    .addProperty("price", 85)
    .addProperty("currency", "GBP")
    .addProperty("source", "https://braze-apparel.com/")
    .addProperty("metadata", new JSONObject()
        .put("sku", "")
        .put("color", "ORANGE")
        .put("size", "6")
        .put("brand", "Braze"));

Braze.getInstance(context).logCustomEvent("ecommerce.product_viewed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let properties: [String: Any] = [
    "product_id": "4111176",
    "product_name": "Torchie runners",
    "variant_id": "4111176700",
    "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
    "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
    "price": 85,
    "currency": "GBP",
    "source": "https://braze-apparel.com/",
    "metadata": [
        "sku": "",
        "color": "ORANGE",
        "size": "6",
        "brand": "Braze"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.product_viewed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.product_viewed",
      "time": "2024-01-15T09:03:45Z",
      "properties": {
        "product_id": "4111176",
        "product_name": "Torchie runners",
        "variant_id": "4111176700",
        "image_url": "https://braze-apparel.com/images/products/large/torchie-runners.jpg",
        "product_url": "https://braze-apparel.com/footwear-categories/sneakers/braze-orange-torchie-runners/",
        "price": 85,
        "currency": "GBP",
        "source": "https://braze-apparel.com/",
        "metadata": {
          "sku": "",
          "color": "ORANGE",
          "size": "6",
          "brand": "Braze"
        }
        "type": [
          "price_drop",
          "back_in_stock"
        ]
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.cart_updated %}

Puedes utilizar el evento de actualización del carrito para hacer un seguimiento de cuándo se añaden, eliminan o actualizan productos en el carrito. El evento `ecommerce.cart_updated` verifica la siguiente información antes de desencadenarse:

- La hora del evento es mayor que la hora de `updated_at` para el carro específico del usuario.
- El carrito no ha pasado al proceso de pago.
- La matriz `products` no está vacía.

#### Objeto mapeado de carros

El evento `ecommerce.cart_updated` tiene un objeto mapeado de carros. Este objeto se crea para el perfil de usuario que contiene un mapeado de carritos, que contiene todos los productos del carrito del comprador. Puedes acceder a los productos de su cesta de la compra a través de la etiqueta de Liquid: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Si un carrito no se ha actualizado y pasado a un evento de pedido realizado en 10 días, eliminaremos el carrito y los productos asociados.

{% alert note %}
Los productos por carrito no están limitados en Braze. Sin embargo, el límite de Shopify es de 500.
{% endalert %}

#### Comportamiento del carro al fusionar perfiles de usuario

Si hay dos carros, añade ambos al usuario fusionado. Vuelve a poner en cola el Canvas si se trata del mismo carrito o de un carrito diferente para enviar un mensaje con la información más reciente del carrito. El evento `ecommerce.cart_updated` contendrá el ID del carrito durado y los productos durados del carrito.

#### Propiedades

| Nombre de la propiedad | Necesario | Tipo de datos | Descripción | 
|---|---|---|---|
| `cart_id` | Sí | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario. |
| `total_value` | Sí | Flotador | Valor monetario total del carro. | 
| `currency` | Sí | Cadena | La moneda en la que se indica el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sí | Matriz |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. <br> Este valor puede ser el ID o el SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto visualizado. |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotador | El precio unitario variante del producto en el momento de verlo. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.cart_updated", {
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": [
        {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
                "sku": "TSH-BLU-M",
                "color": "BLUE",
                "size": "Medium",
                "brand": "Braze"
            }
        }
    ],
    "source": "https://braze-apparel.com",
    "metadata": {}
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "8266836345064")
    .put("product_name", "Classic T-Shirt")
    .put("variant_id", "44610569208040")
    .put("image_url", "https://braze-apparel.com/images/tshirt-blue-medium.jpg")
    .put("product_url", "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040")
    .put("quantity", 2)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "TSH-BLU-M")
        .put("color", "BLUE")
        .put("size", "Medium")
        .put("brand", "Braze"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("cart_id", "cart_12345")
    .addProperty("currency", "USD")
    .addProperty("total_value", 199.98)
    .addProperty("products", products)
    .addProperty("source", "https://braze-apparel.com")
    .addProperty("metadata", new JSONObject());

Braze.getInstance(context).logCustomEvent("ecommerce.cart_updated", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "8266836345064",
        "product_name": "Classic T-Shirt",
        "variant_id": "44610569208040",
        "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
        "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
        "quantity": 2,
        "price": 99.99,
        "metadata": [
            "sku": "TSH-BLU-M",
            "color": "BLUE",
            "size": "Medium",
            "brand": "Braze"
        ]
    ]
]

let properties: [String: Any] = [
    "cart_id": "cart_12345",
    "currency": "USD",
    "total_value": 199.98,
    "products": products,
    "source": "https://braze-apparel.com",
    "metadata": [:]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.cart_updated", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.cart_updated",
      "time": "2024-01-15T09:15:30Z",
      "properties": {
        "cart_id": "cart_12345",
        "currency": "USD",
        "total_value": 199.98,
        "products": [
          {
            "product_id": "8266836345064",
            "product_name": "Classic T-Shirt",
            "variant_id": "44610569208040",
            "image_url": "https://braze-apparel.com/images/tshirt-blue-medium.jpg",
            "product_url": "https://braze-apparel.com/products/classic-tshirt?variant=44610569208040",
            "quantity": 2,
            "price": 99.99,
            "metadata": {
              "sku": "TSH-BLU-M",
              "color": "BLUE",
              "size": "Medium",
              "brand": "Braze"
            }
          }
        ],
        "source": "https://braze-apparel.com",
        "metadata": {}
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.checkout_started %}

Puedes utilizar el evento de pago iniciado para reorientar a los clientes que han iniciado el proceso de pago pero no han realizado un pedido.

Similar al evento `ecommerce.cart_updated`, este evento te permite aprovechar la etiqueta de Liquid del carrito de la compra para acceder a todos los productos de su carrito para los mensajes de pago abandonado:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propiedades

| Nombre de la propiedad | Necesario | Tipo de datos | Descripción | 
|---|---|---|---|
| `checkout_id` | Sí | Cadena | Identificador único de la caja. |
| `cart_id` | No | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario.. | 
| `total_value` | Sí | Flotador | Valor monetario total del carro. |
| `currency` | Sí | Cadena | Moneda en la que se valora el carro. |
| `products` | Sí | Matriz de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. Por ejemplo, este valor podría ser el ID o la SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto visualizado.  |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotador | El precio unitario variante del producto en el momento de verlo. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto |  |
| `checkout_url` | No | Cadena | URL de la página de pago. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.checkout_started", {
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("checkout_id", "checkout_abc123")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 199.98)
    .addProperty("currency", "USD")
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("checkout_url", "https://checkout.braze-audio.com/abc123"));

Braze.getInstance(context).logCustomEvent("ecommerce.checkout_started", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "checkout_id": "checkout_abc123",
    "cart_id": "cart_12345",
    "total_value": 199.98,
    "currency": "USD",
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "checkout_url": "https://checkout.braze-audio.com/abc123"
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.checkout_started", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.checkout_started",
      "time": "2024-01-15T09:25:45Z",
      "properties": {
        "checkout_id": "checkout_abc123",
        "cart_id": "cart_12345",
        "total_value": 199.98,
        "currency": "USD",
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "checkout_url": "https://checkout.braze-audio.com/abc123"
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_placed %}

Puedes utilizar el evento pedido realizado para desencadenar el evento cuando un cliente complete correctamente el proceso de pago y realice un pedido.

#### Propiedades

| Nombre de la propiedad | Necesario | Tipo de datos | Descripción | 
|---|---|---|---|
| `order_id` | Sí | Cadena | Identificador único del pedido realizado. |
| `cart_id` | No | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario. |
| `total_value` | Sí | Flotador | Valor monetario total del carro. | 
| `currency` | Sí | Cadena | Moneda en la que se valora el carro. |
| `total_discounts` | No | Flotador | Importe total de los descuentos aplicados al pedido. | 
| `discounts`| No | Matriz de objetos | Lista detallada de los descuentos aplicados al pedido. |
| `products` | Sí | Matriz de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. Este valor puede ser el ID o el SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto visualizado. |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotador | El precio unitario variante del producto en el momento de verlo. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto |  |
| `order_status_url` | No | Cadena | URL para ver el estado del pedido. |
| `order_number` | No | Cadena | (Sólo Shopify) Número de pedido único para el pedido realizado. |
| `tags` | No | Matriz | (Sólo Shopify) Etiquetas de pedido
| `referring_site` | No | Cadena | (Sólo Shopify) El sitio desde el que se originó el pedido (como Meta). |
| `payment_gateway_names` | No | Matriz | (Sólo Shopify) Fuente del sistema de pago (como punto de venta o móvil). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_placed", {
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cart_id", "cart_12345")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("electronics").put("audio"))
        .put("referring_site", "https://www.e-referrals.com")
        .put("payment_gateway_names", new JSONArray().put("tap2pay").put("dotcash")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_placed", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cart_id": "cart_12345",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["electronics", "audio"],
        "referring_site": "https://www.e-referrals.com",
        "payment_gateway_names": ["tap2pay", "dotcash"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_placed", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_placed",
      "time": "2024-01-15T09:35:20Z",
      "properties": {
        "order_id": "order_67890",
        "cart_id": "cart_12345",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["electronics", "audio"],
          "referring_site": "https://www.e-referrals.com",
          "payment_gateway_names": ["tap2pay", "dotcash"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_refunded %}

Puedes utilizar el evento pedido reembolsado para desencadenar el reembolso parcial o total de un pedido.

#### Propiedades

| Nombre de la propiedad       | Necesario | Tipo de datos | Descripción   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.        |
| `total_value`         | Sí      | Flotador     | Valor monetario total del carro.    |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carro.    |
| `total_discounts`     | No       | Flotador     | Importe total de los descuentos aplicados al pedido.   |
| `discounts`           | No       | Matriz de objetos     | Lista detallada de los descuentos aplicados al pedido. |
| `products`            | Sí      | Matriz de objetos     |  |
| `product_id`       | Sí      | Cadena    | Un identificador único del producto visualizado. Este valor puede ser el ID del producto, SKU o similar. <br>Si se emite una devolución parcial y no hay ningún `product_id` asignado a la devolución (por ejemplo, una devolución a nivel de pedido), proporciona un `product_id` generalizado.             |
| `product_name`     | Sí      | Cadena    | El nombre del producto visualizado.                                                                      |
| `variant_id`       | Sí      | Cadena    | Un identificador único de la variante del producto (como `shirt_medium_blue`).                                         |
| `image_url`        | No       | Cadena    | URL de la imagen del producto.     |
| `product_url`      | No       | Cadena    | URL a la página del producto para más detalles.  |
| `quantity`         | Sí      | Entero   | Número de unidades del producto en el carrito.   |
| `price`            | Sí      | Flotador     | El precio unitario variante del producto en el momento de verlo.  |
| `metadata`         | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku`            | No       | Cadena    | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo.  |
| `source`              | Sí      | Cadena    | Fuente de la que procede el evento. (Para Shopify, es el escaparate).    |
| `metadata`            | No       | Objeto    |                |
| `order_status_url`  | No       | Cadena    | URL para ver el estado del pedido.     |
| `order_note`       | No       | Cadena    | (Sólo Shopify) Nota añadida al pedido por el comerciante.    |
| `order_number`     | No       | Cadena    | (Sólo Shopify) Número de pedido único para el pedido realizado.   |
| `tags`             | No       | Matriz     | (Sólo Shopify) Etiquetas de pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_refunded", {
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": [
        {
            "code": "SAVE5",
            "amount": 5.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE5")
    .put("amount", 5.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 99.99)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("total_value", 99.99)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 5.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_note", "Customer requested refund due to defective item")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("refund").put("defective")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_refunded", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE5",
        "amount": 5.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 99.99,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "total_value": 99.99,
    "currency": "USD",
    "total_discounts": 5.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_note": "Customer requested refund due to defective item",
        "order_number": "ORD-2024-001234",
        "tags": ["refund", "defective"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_refunded", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_refunded",
      "time": "2024-01-15T10:15:30Z",
      "properties": {
        "order_id": "order_67890",
        "total_value": 99.99,
        "currency": "USD",
        "total_discounts": 5.00,
        "discounts": [
          {
            "code": "SAVE5",
            "amount": 5.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 99.99,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_note": "Customer requested refund due to defective item",
          "order_number": "ORD-2024-001234",
          "tags": ["refund", "defective"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab ecommerce.order_cancelled %}

Puedes utilizar el evento pedido cancelado para desencadenar cuando un cliente cancele un pedido.

#### Propiedades

| Nombre de la propiedad      | Necesario | Tipo de datos | Descripción       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.              |
| `cancel_reason`       | Sí      | Cadena    | Motivo por el que se canceló el pedido.           |
| `total_value`         | Sí      | Flotador     | Valor monetario total del carro.         |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carro.           |
| `total_discounts`     | No       | Flotador     | Importe total de los descuentos aplicados al pedido.     |
| `discounts`           | No       | Matriz de objetos     | Lista detallada de los descuentos aplicados al pedido.             |
| `products`            | Sí      | Matriz de objetos     |         |
| `product_id`          | Sí      | Cadena    | Un identificador único del producto visualizado. Este valor puede ser el ID del producto, SKU o similar.             |
| `product_name`        | Sí      | Cadena    | El nombre del producto visualizado.          |
| `variant_id`          | Sí      | Cadena    | Un identificador único de la variante del producto (como `shirt_medium_blue`).        |
| `image_url`           | No       | Cadena    | URL de la imagen del producto.           |
| `product_url`         | No       | Cadena    | URL a la página del producto para más detalles.                                                                     |
| `quantity`            | Sí      | Entero   | Número de unidades del producto en el carrito.        |
| `price`               | Sí      | Flotador     | El precio unitario variante del producto en el momento de verlo.     |
| `metadata`            | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku`                 | No       | Cadena    | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo.        |
| `source`              | Sí      | Cadena    | Fuente de la que procede el evento. (Para Shopify, es el escaparate).    |
| `metadata`            | No       | Objeto    |       |
| `order_status_url`    | No       | Cadena    | URL para ver el estado del pedido.                                                                          |
| `order_number`        | No       | Cadena    | (Sólo Shopify) Número de pedido único para el pedido realizado.  |
| `tags`                | No       | Matriz     | (Sólo Shopify) Etiquetas de pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplos de objetos

{% subtabs %}
{% subtab Web SDK %}

```javascript
braze.logCustomEvent("ecommerce.order_cancelled", {
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": [
        {
            "code": "SAVE10",
            "amount": 10.00
        }
    ],
    "products": [
        {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
                "sku": "WH-BLK-PRO",
                "color": "Black",
                "brand": "BrazeAudio"
            }
        }
    ],
    "source": "https://braze-audio.com",
    "metadata": {
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    }
});
```

{% endsubtab %}
{% subtab Android SDK %}

```java
JSONArray discounts = new JSONArray();
discounts.put(new JSONObject()
    .put("code", "SAVE10")
    .put("amount", 10.00));

JSONArray products = new JSONArray();
JSONObject product = new JSONObject()
    .put("product_id", "632910392")
    .put("product_name", "Wireless Headphones")
    .put("variant_id", "808950810")
    .put("quantity", 1)
    .put("price", 199.98)
    .put("metadata", new JSONObject()
        .put("sku", "WH-BLK-PRO")
        .put("color", "Black")
        .put("brand", "AudioTech"));
products.put(product);

BrazeProperties properties = new BrazeProperties()
    .addProperty("order_id", "order_67890")
    .addProperty("cancel_reason", "customer changed mind")
    .addProperty("total_value", 189.98)
    .addProperty("currency", "USD")
    .addProperty("total_discounts", 10.00)
    .addProperty("discounts", discounts)
    .addProperty("products", products)
    .addProperty("source", "https://braze-audio.com")
    .addProperty("metadata", new JSONObject()
        .put("order_status_url", "https://braze-audio.com/orders/67890/status")
        .put("order_number", "ORD-2024-001234")
        .put("tags", new JSONArray().put("cancelled").put("customer_request")));

Braze.getInstance(context).logCustomEvent("ecommerce.order_cancelled", properties);
```

{% endsubtab %}
{% subtab Swift SDK %}

```swift
let discounts: [[String: Any]] = [
    [
        "code": "SAVE10",
        "amount": 10.00
    ]
]

let products: [[String: Any]] = [
    [
        "product_id": "632910392",
        "product_name": "Wireless Headphones",
        "variant_id": "808950810",
        "quantity": 1,
        "price": 199.98,
        "metadata": [
            "sku": "WH-BLK-PRO",
            "color": "Black",
            "brand": "BrazeAudio"
        ]
    ]
]

let properties: [String: Any] = [
    "order_id": "order_67890",
    "cancel_reason": "customer changed mind",
    "total_value": 189.98,
    "currency": "USD",
    "total_discounts": 10.00,
    "discounts": discounts,
    "products": products,
    "source": "https://braze-audio.com",
    "metadata": [
        "order_status_url": "https://braze-audio.com/orders/67890/status",
        "order_number": "ORD-2024-001234",
        "tags": ["cancelled", "customer_request"]
    ]
]

AppDelegate.braze?.logCustomEvent(name: "ecommerce.order_cancelled", properties: properties)
```

{% endsubtab %}
{% subtab API Payload %}

```json
{
  "events": [
    {
      "external_id": "user_id",
      "app_id": "your_app_identifier",
      "name": "ecommerce.order_cancelled",
      "time": "2024-01-15T10:45:15Z",
      "properties": {
        "order_id": "order_67890",
        "cancel_reason": "customer changed mind",
        "total_value": 189.98,
        "currency": "USD",
        "total_discounts": 10.00,
        "discounts": [
          {
            "code": "SAVE10",
            "amount": 10.00
          }
        ],
        "products": [
          {
            "product_id": "632910392",
            "product_name": "Wireless Headphones",
            "variant_id": "808950810",
            "quantity": 1,
            "price": 199.98,
            "metadata": {
              "sku": "WH-BLK-PRO",
              "color": "Black",
              "brand": "BrazeAudio"
            }
          }
        ],
        "source": "https://braze-audio.com",
        "metadata": {
          "order_status_url": "https://braze-audio.com/orders/67890/status",
          "order_number": "ORD-2024-001234",
          "tags": ["cancelled", "customer_request"]
        }
      }
    }
  ]
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Plantillas Canvas para comercio electrónico

Braze ha creado plantillas Canvas prediseñadas que se basan en eventos recomendados para el comercio electrónico, como los clientes que iniciaron el proceso de pago pero lo abandonaron antes de realizar el pedido. Puedes utilizar estos eventos para tomar decisiones informadas que mejoren tu viaje de usuario personalizando la mensajería y dirigiéndote a audiencias específicas.

Consulta nuestros [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) dedicados [al comercio electrónico]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) para saber más sobre cómo puedes utilizar estos eventos con las plantillas de Canvas.

## Campos calculados por el usuario

Utilizamos cálculos estandarizados de campos de usuario para los siguientes campos: 

- **Ingresos totales** = suma del valor total del pedido realizado - suma del valor total del pedido reembolsado
- **Recuento total de pedidos** = recuento de eventos distintos de pedidos realizados - recuento de cancelaciones distintas de pedidos
- **Valor total** del reembolso = suma del valor total reembolsado del pedido 

Estos cálculos de campo de usuario también se incluyen en la pestaña **Transacciones** de los perfiles de usuario.

Pestaña "Transacciones" con campos calculados por el usuario.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}
