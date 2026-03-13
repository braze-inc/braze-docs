---
nav_title: Eventos recomendados para el comercio electrónico
article_title: Eventos recomendados de comercio electrónico
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artículo de referencia describe los eventos y propiedades recomendados para el comercio electrónico, su uso, segmentación, dónde ver los análisis relevantes y mucho más."
---

# Eventos recomendados para el comercio electrónico

> Esta página incluye eventos y propiedades recomendados para el comercio electrónico. Estos eventos se crean para capturar comportamientos de compra clave que los especialistas en marketing necesitan para desencadenar mensajería eficaz, como los dirigidos al abandono del carrito de compras.

{% alert important %}
Los eventos recomendados para el comercio electrónico se encuentran actualmente en fase de acceso anticipado. Si estás interesado en participar en este acceso anticipado, ponte en contacto con tu administrador del éxito del cliente de Braze. <br><br>Si utilizas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}

Braze reconoce que la planificación de datos lleva tiempo. Animamos a nuestros clientes a que familiaricen a sus equipos de desarrollo y comiencen a enviar estos eventos ahora mismo. Aunque es posible que algunas características no estén disponibles de inmediato con los eventos recomendados para el comercio electrónico, puedes esperar la introducción de nuevos productos a lo largo de 2025 que mejorarán tus capacidades de comercio electrónico.

## Tipos de eventos recomendados para el comercio electrónico

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Cualquier moneda distinta al dólar estadounidense (USD) que se informe se mostrará en Braze en USD según la tasa de cambio vigente en la fecha en que se informó. Para evitar la conversión de divisas, codifica la moneda en USD.

{% tabs %}
{% tab ecommerce.product_viewed %}

Puedes utilizar el evento «producto visto» para desencadenar una acción cuando un cliente vea la página de detalles de un producto.

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `product_id` | Sí | Cadena | Un identificador único para el producto que se ha visto. <br> Para los clientes que no utilizan Shopify, este será el valor que establezcáis para los ID de los artículos del catálogo, como los SKU. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. | 
| `variant_id` | Sí | Cadena | Identificador único de la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para obtener más detalles. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de la visualización. |
| `currency` | Sí | Cadena | La moneda en la que se indica el precio del producto (por ejemplo, «USD» o «EUR») en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sí | Cadena | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual). |
| `metadata` | No | Objeto | |
| `type` | No | Objeto | Funciona con [notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications) y [notificaciones de bajadas de precio]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications). |
| `sku` | No | Cadena | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo. |
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
        },
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

Puedes utilizar el evento «cart updated» (carrito actualizado) para realizar un seguimiento de cuándo se añaden, eliminan o actualizan productos en el carrito. El`ecommerce.cart_updated`evento verifica la siguiente información antes de desencadenarse:

- La hora del evento es posterior a la`updated_at`hora del carrito específico del usuario.
- El carrito no ha pasado al proceso de pago.
- La`products`matriz no está vacía.

#### Objeto de mapeo de carros

El`ecommerce.cart_updated`evento tiene un objeto que ha sido mapeado para los carros. Este objeto se crea para el perfil de usuario que contiene un mapeo de carritos, los cuales contienen todos los productos del carrito del comprador. Puedes acceder a los productos de tu carrito de la compra a través de la etiqueta de Liquid: 

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

Si un carrito no se ha actualizado y no ha pasado a la fase de pedido en un plazo de 10 días, eliminaremos el carrito y los productos asociados.

{% alert note %}
Los productos por carrito no están limitados en Braze. Sin embargo, el límite de Shopify es de 500.
{% endalert %}

#### Comportamiento del carrito al fusionar perfiles de usuario

Si hay dos carros, añaden ambos al usuario fusionado. Vuelve a poner el Canvas en la cola si se trata del mismo carrito o de uno diferente para enviar un mensaje con la información más reciente del carrito. El`ecommerce.cart_updated`evento contendrá el último ID del carrito y los últimos productos del carrito.

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `cart_id` | Sí | Cadena | Si no utilizas una plataforma de terceros que proporcione un `cart_id`, puedes utilizar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Sí | Flotante | Valor monetario total del carrito. | 
| `currency` | Sí | Cadena | La moneda en la que se indica el precio del producto (por ejemplo, «USD» o «EUR») en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sí | Matriz |  |
| `product_id` | Sí | Cadena | Un identificador único para el producto que se ha visto. <br> Este valor puede ser el ID del producto o el SKU. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. |
| `variant_id` | Sí | Cadena | Identificador único de la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para obtener más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de la visualización. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. <br> Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
| `sku` | No | Cadena | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual). |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. <br> Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
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

Puedes utilizar el evento «checkout started» (comienzo del proceso de pago) para reorientar a los clientes que han iniciado el proceso de pago pero no han realizado el pedido.

Al igual que el`ecommerce.cart_updated`evento, este evento te permite aprovechar la etiqueta de Liquid del carrito de la compra para acceder a todos los productos que hay en tu carrito y enviar mensajes de abandono del proceso de pago:

{%raw%}
```liquid
{% shopping_cart {{context_properties.${cart_id}}} :abort_if_not_abandoned false %}
{% for item in shopping_cart.products %}
{% catalog_items <add_your_catalog> {{item.variant_id}} %}
```
{%endraw%}

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `checkout_id` | Sí | Cadena | Identificador único para el proceso de pago. |
| `cart_id` | No | Cadena | Si no utilizas una plataforma de terceros que proporcione un `cart_id`, puedes utilizar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). | 
| `total_value` | Sí | Flotante | Valor monetario total del carrito. |
| `currency` | Sí | Cadena | Moneda en la que se valora el carrito. |
| `products` | Sí | Conjunto de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único para el producto que se ha visto. Por ejemplo, este valor podría ser el ID del producto o el SKU. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto.  |
| `variant_id` | Sí | Cadena | Identificador único de la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para obtener más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de la visualización. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. <br> Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
| `sku` | No | Cadena | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual). |
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

Puedes utilizar el evento «pedido realizado» para desencadenar una acción cuando un cliente complete con éxito el proceso de pago y realice un pedido.

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `order_id` | Sí | Cadena | Identificador único del pedido realizado. |
| `cart_id` | No | Cadena | Si no utilizas una plataforma de terceros que proporcione un `cart_id`, puedes utilizar el [ID de sesión de Braze]({{site.baseurl}}/developer_guide/analytics/tracking_sessions). |
| `total_value` | Sí | Flotante | Valor monetario total del carrito. | 
| `currency` | Sí | Cadena | Moneda en la que se valora el carrito. |
| `total_discounts` | No | Flotante | Importe total de los descuentos aplicados al pedido. | 
| `discounts`| No | Conjunto de objetos | Lista detallada de los descuentos aplicados al pedido. |
| `products` | Sí | Conjunto de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único para el producto que se ha visto. Este valor puede ser el ID del producto o el SKU. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. |
| `variant_id` | Sí | Cadena | Identificador único de la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para obtener más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de la visualización. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. <br> Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
| `sku` | No | Cadena | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual). |
| `order_status_url` | No | Cadena | URL para ver el estado del pedido. |
| `order_number` | No | Cadena | (Solo Shopify) Número de pedido único para el pedido realizado. |
| `tags` | No | Matriz | (Solo Shopify) Etiquetas de pedidos
| `referring_site` | No | Cadena | (Solo Shopify) El sitio desde el que se originó el pedido (como Meta). |
| `payment_gateway_names` | No | Matriz | (Solo Shopify) Fuente del sistema de pago (como punto de venta o móvil). |
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

Puedes utilizar el evento «pedido reembolsado» para desencadenar una acción cuando un pedido se reembolsa parcial o totalmente.

#### Propiedades

| Nombre de la propiedad       | Obligatoria | Tipo de datos | Descripción   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.        |
| `total_value`         | Sí      | Flotante     | Valor monetario total del carrito.    |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carrito.    |
| `total_discounts`     | No       | Flotante     | Importe total de los descuentos aplicados al pedido.   |
| `discounts`           | No       | Conjunto de objetos     | Lista detallada de los descuentos aplicados al pedido. |
| `products`            | Sí      | Conjunto de objetos     |  |
| `product_id`       | Sí      | Cadena    | Un identificador único para el producto que se ha visto. Este valor puede ser el ID del producto, el SKU o similar. <br>Si se emite un reembolso parcial y no hay ningún`product_id`  asignado al reembolso (por ejemplo, un reembolso a nivel de pedido), proporciona un  generalizado`product_id`.             |
| `product_name`     | Sí      | Cadena    | El nombre del producto que se ha visto.                                                                      |
| `variant_id`       | Sí      | Cadena    | Un identificador único para la variante del producto (por ejemplo, `shirt_medium_blue`).                                         |
| `image_url`        | No       | Cadena    | URL de la imagen del producto.     |
| `product_url`      | No       | Cadena    | URL a la página del producto para obtener más detalles.  |
| `quantity`         | Sí      | Entero   | Número de unidades del producto en el carrito.   |
| `price`            | Sí      | Flotante     | El precio unitario variante del producto en el momento de la visualización.  |
| `metadata`         | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
| `sku`            | No       | Cadena    | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo.  |
| `source`              | Sí      | Cadena    | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual).    |
| `metadata`            | No       | Objeto    |                |
| `order_status_url`  | No       | Cadena    | URL para ver el estado del pedido.     |
| `order_note`       | No       | Cadena    | (Solo Shopify) Nota añadida al pedido por el comerciante.    |
| `order_number`     | No       | Cadena    | (Solo Shopify) Número de pedido único para el pedido realizado.   |
| `tags`             | No       | Matriz     | Etiquetas de pedidos (solo Shopify).  |
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

Puedes utilizar el evento «pedido cancelado» para desencadenar una acción cuando un cliente cancele un pedido.

#### Propiedades

| Nombre de la propiedad      | Obligatoria | Tipo de datos | Descripción       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.              |
| `cancel_reason`       | Sí      | Cadena    | Motivo por el que se canceló el pedido.           |
| `total_value`         | Sí      | Flotante     | Valor monetario total del carrito.         |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carrito.           |
| `total_discounts`     | No       | Flotante     | Importe total de los descuentos aplicados al pedido.     |
| `discounts`           | No       | Conjunto de objetos     | Lista detallada de los descuentos aplicados al pedido.             |
| `products`            | Sí      | Conjunto de objetos     |         |
| `product_id`          | Sí      | Cadena    | Un identificador único para el producto que se ha visto. Este valor puede ser el ID del producto, el SKU o similar.             |
| `product_name`        | Sí      | Cadena    | El nombre del producto que se ha visto.          |
| `variant_id`          | Sí      | Cadena    | Un identificador único para la variante del producto (por ejemplo, `shirt_medium_blue`).        |
| `image_url`           | No       | Cadena    | URL de la imagen del producto.           |
| `product_url`         | No       | Cadena    | URL a la página del producto para obtener más detalles.                                                                     |
| `quantity`            | Sí      | Entero   | Número de unidades del producto en el carrito.        |
| `price`               | Sí      | Flotante     | El precio unitario variante del producto en el momento de la visualización.     |
| `metadata`            | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente desea añadir para sus casos de uso. Para Shopify, añadiremos el SKU. Esto tendrá un límite basado en el límite general de propiedades del evento de 50 kb. |
| `sku`                 | No       | Cadena    | (Solo Shopify) SKU de Shopify. Esto se puede configurar como el campo ID del catálogo.        |
| `source`              | Sí      | Cadena    | Fuente de la que se deriva el evento. (En Shopify, esto es la tienda virtual).    |
| `metadata`            | No       | Objeto    |       |
| `order_status_url`    | No       | Cadena    | URL para ver el estado del pedido.                                                                          |
| `order_number`        | No       | Cadena    | (Solo Shopify) Número de pedido único para el pedido realizado.  |
| `tags`                | No       | Matriz     | Etiquetas de pedidos (solo Shopify).            |
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

## Plantillas de Canvas para comercio electrónico

Braze ha creado plantillas Canvas prediseñadas que se basan en eventos recomendados para el comercio electrónico, como dirigirse a los clientes que han iniciado el proceso de pago pero lo han abandonado antes de realizar el pedido. Puedes utilizar estos eventos para tomar decisiones informadas que mejoren la experiencia de los usuarios, mediante la personalización de la mensajería y la dirección a audiencias objetivo.

Echa un vistazo a nuestros [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) específicos para [comercio electrónico]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) y descubre más formas de utilizar estos eventos con las plantillas de Canvas.

## Campos calculados por el usuario

Utilizamos cálculos de campos de usuario estandarizados para los siguientes campos: 

- **Ingresos totales** = suma del valor total de los pedidos realizados - suma del valor total de los pedidos reembolsados
- **Recuento total de pedidos** = recuento de eventos de pedidos realizados distintos - recuento de cancelaciones de pedidos distintos
- **Valor total del reembolso** = suma del valor total reembolsado del pedido 

Estos cálculos de campos de usuario también se incluyen en la pestaña **Transacciones** de los perfiles de usuario.

![La pestaña «Transacciones» con campos calculados por el usuario.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:70%;"}

## Preguntas más frecuentes

### ¿Dónde puedes consultar los datos de compra a nivel de producto?

La pestaña **Transacciones** del perfil de usuario muestra campos calculados de alto nivel (como los ingresos totales y el total de pedidos). Para ver los detalles a nivel de producto de un usuario específico, utiliza el [generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) para consultar los datos de eventos de comercio electrónico o exporta los datos de eventos a través de [Currents]({{site.baseurl}}/user_guide/data/braze_currents/).

A diferencia de los eventos de compra heredados, los eventos recomendados de comercio electrónico almacenan los detalles del producto como propiedades de eventos anidados dentro de la`products`matriz. Estas propiedades están disponibles en la mensajería a través de Liquid y en la segmentación a través de [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/).

### ¿Cómo puedo segmentar a los usuarios por un producto específico?

El segmentador te permite filtrar por el número de veces que un usuario ha realizado un evento de comercio electrónico. Para filtrar por propiedades específicas del producto (como`product_id`  o `product_name`), utiliza [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), que admiten el filtrado de propiedades del evento anidado. Por ejemplo, puedes encontrar todos los usuarios que compraron el producto «SKU-123» en los últimos 90 días.

### ¿Cuál es la diferencia entre los eventos de compra heredados y los eventos recomendados para el comercio electrónico?

Los eventos de compra heredados utilizan el [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze y registran las compras de productos individuales con un`product_id`  y `price`. Los eventos recomendados para comercio electrónico (como `ecommerce.order_placed`) utilizan propiedades del evento personalizadas y capturan el contexto completo del pedido, incluidos varios productos, descuentos y metadatos en un solo evento.

Con el lanzamiento de los eventos recomendados para el comercio electrónico, Braze eliminará gradualmente el evento de compra heredado en el futuro. Si actualmente utilizas eventos de compra, recibirás un aviso previo. Mientras tanto, puedes seguir utilizando los eventos de compra hasta la fecha oficial de descatalogación. Consulta el [resumen]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/) de [eventos recomendados]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/) para obtener más detalles.

### ¿Puedes añadir propiedades personalizadas a los eventos recomendados para el comercio electrónico?

Los eventos recomendados para el comercio electrónico tienen un esquema definido con campos obligatorios y opcionales. Puedes incluir datos personalizados adicionales dentro del`metadata`objeto para cada evento. Sin embargo, las etiquetas personalizadas a nivel de pedido o los campos propios (como el canal de compra o la información del comercio minorista) no se admiten como propiedades de nivel superior. Si necesitas estos campos para la segmentación, continúa enviándolos como eventos personalizados independientes junto con tus eventos de comercio electrónico.

### ¿Es necesario incluirexternal_id  al enviar eventos de comercio electrónico?

Depende de cómo envíes los eventos:

- **A través del SDK**: No. Cuando utilizas un SDK de Braze, los eventos se asocian automáticamente con el contexto de usuario actual del SDK (anónimo o con identificador). No es necesario pasar un identificador de usuario con cada llamada de evento; en su lugar, puedes identificar al usuario para ese contexto utilizando métodos como `changeUser`.
- **A través de la API REST** (`/users/track`): Sí. Cada solicitud de API debe incluir un identificador de usuario, como `external_id`, `braze_id`, `user_alias`,`email` o `phone`, ya que la API no tiene contexto de «usuario actual».

### ¿Por qué no aparecen las propiedades de los productos anidados en el menú desplegable de configuración de Recomendaciones de IA?

Al configurar [las recomendaciones de artículos de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/), el menú desplegable **Nombre de la propiedad** solo muestra las propiedades del evento de nivel superior (como `order_id`,`total_value` y `currency`). Es posible que las propiedades anidadas dentro de`products`la matriz (por ejemplo,`products.product_id`o `products.variant_id`) no aparezcan en esta lista, pero puedes escribirlas manualmente utilizando la notación de puntos en el campo. Para la mayoría de las implementaciones de comercio electrónico, Braze recomienda utilizar`products.product_id`  como identificador de artículo y emparejarlo con un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) cuyos ID de artículo coincidan con tus `product_id`valores  `variant_id`o .

### ¿Por qué algunos de mis eventos de comercio electrónico no aparecen en Braze?

Si los eventos no aparecen en los perfiles de usuario o en los registros, comprueba lo siguiente:

- **Momento de vaciado de datos del SDK**: El SDK de Braze almacena los datos en caché localmente y los carga periódicamente (normalmente en un intervalo de 10 a 60 segundos). Llama a`requestImmediateDataFlush()`  después de`logCustomEvent()`  para forzar una carga inmediata.
- **Propiedades requeridas**: los eventos de comercio electrónico tienen propiedades requeridas. Si falta una propiedad obligatoria o tiene un tipo de datos no válido, es posible que se rechace el evento. Comprueba que la carga útil de tu evento coincida con el [esquema requerido](#types-of-ecommerce-recommended-events).
- **Precisión del nombre del evento**: los nombres de los eventos de comercio electrónico distinguen entre mayúsculas y minúsculas y deben coincidir exactamente (por ejemplo, `ecommerce.checkout_started`, no `ecommerce.checkoutStarted`).
