---
nav_title: Eventos recomendados de comercio electrónico
article_title: Eventos recomendados de comercio electrónico
page_type: reference
alias: /ecommerce_events/
toc_headers: h2
description: "Este artículo de referencia describe los eventos y propiedades recomendados para el comercio electrónico, su uso, segmentación, dónde ver los análisis relevantes y mucho más."
---

# Eventos recomendados en eCommerce

> Esta página cubre los eventos y propiedades recomendados para el comercio electrónico. Estos eventos se crean para captar los comportamientos de compra clave que los especialistas en marketing necesitan para desencadenar una mensajería eficaz, como la dirigida a los carritos abandonados.

Braze reconoce que la planificación de datos lleva tiempo. Animamos a nuestros clientes a que familiaricen a sus equipos de desarrolladores y empiecen ya a enviar estos eventos. Aunque algunas características pueden no estar disponibles inmediatamente con los eventos recomendados para el comercio electrónico, puedes esperar la introducción de nuevos productos a lo largo de 2025 que mejorarán tus capacidades de comercio electrónico.

{% alert important %}
Los eventos recomendados por eCommerce están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si aprovechas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}


## Tipos de eventos recomendados para el comercio electrónico

{% tabs %}
{% tab ecommerce.producto_visto %}

Puedes utilizar el evento producto visto para desencadenar el evento cuando un cliente vea la página de detalles de un producto.

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. <br> Para los clientes que no son de Shopify, será el valor que establezcas para los ID de los artículos del catálogo, como las SKU. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. | 
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de verlo. |
| `currency` | Sí | Cadena | La moneda en la que aparece el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto | |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.product_viewed",
    "properties": {
        "product_id": "12345",
        "product_name": "product",
        "variant_id": "123",
        "image_url": "www.image-url.com",
        "product_url": "mystorefront.myshopify.com/product",
        "price": 10,
        "currency": "USD",
        "source": "mystorefront.myshopify.com",
        "metadata": {
            "sku": "sku"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.carrito_actualizado %}

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

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `cart_id` | Sí | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario. |
| `total_value` | Sí | Flotante | Valor monetario total del carro. | 
| `currency` | Sí | Cadena | La moneda en la que aparece el precio del producto (como "USD" o "EUR") en [formato ISO 4217](https://www.iso.org/iso-4217-currency-codes.html). |
| `products` | Sí | Matriz |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. <br> Este valor puede ser el ID o el SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de verlo. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.cart_updated",
    "properties": {
        "cart_id": "Z2NwLXVzLWVhc3QxOjAxSjk3UFg4RlFZMjVTVkRHRlc1RlI3SlRY",
        "currency": "USD",
        "total_value": 2000000,
        "products": [
            {
                "product_id": "8266836345064",
                "product_name": "PANTS!!!",
                "variant_id": "44610569208040",
                "image_url": "https://cdn.shopify.com/s/files/1/0604/4211/6328/files/1200px-Trousers-colourisolated.jpg?v=1689256168",
                "product_url": "https://test-store.myshopify.com/products/pants?variant=44610569208040",
                "quantity": 2,
                "price": 1000000,
                "metadata": {
                    "sku": "007"
                }
            }
        ],
        "source": "https://test-store.myshopify.com",
        "metadata": {}
    }
}
```
{% endtab %}
{% tab ecommerce.checkout_started %}

Puedes utilizar el evento de pago iniciado para reorientar a los clientes que han iniciado el proceso de pago pero no han realizado el pedido.

Similar al evento `ecommerce.cart_updated`, este evento te permite aprovechar la etiqueta de Liquid del carrito de la compra para acceder a todos los productos de su carrito para los mensajes de pago abandonado:

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
| `checkout_id` | Sí | Cadena | Identificador único de la caja. |
| `cart_id` | No | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario.. | 
| `total_value` | Sí | Flotante | Valor monetario total del carro. |
| `currency` | Sí | Cadena | Moneda en la que se valora el carro. |
| `products` | Sí | Conjunto de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. Por ejemplo, este valor podría ser el ID o la SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto.  |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de verlo. |
| `metadata` | No | Objeto | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. <br> Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku` | No | Cadena | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo. |
| `source` | Sí | Cadena | Fuente de la que procede el evento. (Para Shopify, es el escaparate). |
| `metadata` | No | Objeto |  |
| `checkout_url` | No | Cadena | URL de la página de pago. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.checkout_started",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "checkout_id": "123123123",
        "metadata": {
            "checkout_url": "https://checkout.local/548380009/checkouts/123123123/recover?key=example-secret-token"
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_realizado %}

Puedes utilizar el evento pedido realizado para desencadenar el evento cuando un cliente complete correctamente el proceso de pago y realice un pedido.

#### Propiedades

| Nombre de la propiedad | Obligatoria | Tipo de datos | Descripción | 
|---|---|---|---|
| `order_id` | Sí | Cadena | Identificador único del pedido realizado. |
| `cart_id` | No | Cadena | Identificador único del carrito. Si no se pasa ningún valor, determinaremos un valor predeterminado (compartido entre los eventos de carrito, pago y pedido) para el mapeado del carrito del usuario. |
| `total_value` | Sí | Flotante | Valor monetario total del carro. | 
| `currency` | Sí | Cadena | Moneda en la que se valora el carro. |
| `total_discounts` | No | Flotante | Importe total de los descuentos aplicados al pedido. | 
| `discounts`| No | Conjunto de objetos | Lista detallada de los descuentos aplicados al pedido. |
| `products` | Sí | Conjunto de objetos |  |
| `product_id` | Sí | Cadena | Un identificador único del producto visualizado. Este valor puede ser el ID o el SKU del producto. |
| `product_name` | Sí | Cadena | El nombre del producto que se ha visto. |
| `variant_id` | Sí | Cadena | Un identificador único para la variante del producto. Un ejemplo es `shirt_medium_blue` |
| `image_url` | No | Cadena | URL de la imagen del producto. |
| `product_url` | No | Cadena | URL a la página del producto para más detalles. |
| `quantity` | Sí | Entero | Número de unidades del producto en el carrito. |
| `price` | Sí | Flotante | El precio unitario variante del producto en el momento de verlo. |
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

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.order_placed",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cart_id": "eeafa272cebfd4b22385bc4b645e762c",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ],
            "referring_site": "https://www.google.com",
            "payment_gateway_names": [
                "visa",
                "bogus"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_reembolsado %}

Puedes utilizar el evento pedido reembolsado para desencadenar el reembolso parcial o total de un pedido.

#### Propiedades

| Nombre de la propiedad       | Obligatoria | Tipo de datos | Descripción   |
|---------------|---------|-----------|-------------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.        |
| `total_value`         | Sí      | Flotante     | Valor monetario total del carro.    |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carro.    |
| `total_discounts`     | No       | Flotante     | Importe total de los descuentos aplicados al pedido.   |
| `discounts`           | No       | Conjunto de objetos     | Lista detallada de los descuentos aplicados al pedido. |
| `products`            | Sí      | Conjunto de objetos     |  |
| `product_id`       | Sí      | Cadena    | Un identificador único del producto visualizado. Este valor puede ser el ID del producto, SKU o similar. <br>Si se emite una devolución parcial y no hay ningún `product_id` asignado a la devolución (por ejemplo, una devolución a nivel de pedido), proporciona un `product_id` generalizado.             |
| `product_name`     | Sí      | Cadena    | El nombre del producto que se ha visto.                                                                      |
| `variant_id`       | Sí      | Cadena    | Un identificador único de la variante del producto (como `shirt_medium_blue`).                                         |
| `image_url`        | No       | Cadena    | URL de la imagen del producto.     |
| `product_url`      | No       | Cadena    | URL a la página del producto para más detalles.  |
| `quantity`         | Sí      | Entero   | Número de unidades del producto en el carrito.   |
| `price`            | Sí      | Flotante     | El precio unitario variante del producto en el momento de verlo.  |
| `metadata`         | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku`            | No       | Cadena    | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo.  |
| `source`              | Sí      | Cadena    | Fuente de la que procede el evento. (Para Shopify, es el escaparate).    |
| `metadata`            | No       | Objeto    |                |
| `order_status_url`  | No       | Cadena    | URL para ver el estado del pedido.     |
| `order_note`       | No       | Cadena    | (Sólo Shopify) Nota añadida al pedido por el comerciante.    |
| `order_number`     | No       | Cadena    | (Sólo Shopify) Número de pedido único para el pedido realizado.   |
| `tags`             | No       | Matriz     | (Sólo Shopify) Etiquetas de pedido.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.order_refunded",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
			"order_note": "item was broken",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```
{% endtab %}
{% tab ecommerce.pedido_cancelado %}

Puedes utilizar el evento pedido cancelado para desencadenar cuando un cliente cancele un pedido.

#### Propiedades

| Nombre de la propiedad      | Obligatoria | Tipo de datos | Descripción       |
|---------------------|----------|-----------|-------------------|
| `order_id`            | Sí      | Cadena    | Identificador único del pedido realizado.              |
| `cancel_reason`       | Sí      | Cadena    | Motivo por el que se canceló el pedido.           |
| `total_value`         | Sí      | Flotante     | Valor monetario total del carro.         |
| `currency`            | Sí      | Cadena    | Moneda en la que se valora el carro.           |
| `total_discounts`     | No       | Flotante     | Importe total de los descuentos aplicados al pedido.     |
| `discounts`           | No       | Conjunto de objetos     | Lista detallada de los descuentos aplicados al pedido.             |
| `products`            | Sí      | Conjunto de objetos     |         |
| `product_id`          | Sí      | Cadena    | Un identificador único del producto visualizado. Este valor puede ser el ID del producto, SKU o similar.             |
| `product_name`        | Sí      | Cadena    | El nombre del producto que se ha visto.          |
| `variant_id`          | Sí      | Cadena    | Un identificador único de la variante del producto (como `shirt_medium_blue`).        |
| `image_url`           | No       | Cadena    | URL de la imagen del producto.           |
| `product_url`         | No       | Cadena    | URL a la página del producto para más detalles.                                                                     |
| `quantity`            | Sí      | Entero   | Número de unidades del producto en el carrito.        |
| `price`               | Sí      | Flotante     | El precio unitario variante del producto en el momento de verlo.     |
| `metadata`            | No       | Objeto    | Campo de metadatos adicional sobre el producto que el cliente quiere añadir para sus casos de uso. Para Shopify, añadiremos SKU. Esto tendrá un límite basado en nuestro límite general de propiedades del evento de 50kb. |
| `sku`                 | No       | Cadena    | (sólo Shopify) SKU de Shopify. Puede configurarse como campo ID del catálogo.        |
| `source`              | Sí      | Cadena    | Fuente de la que procede el evento. (Para Shopify, es el escaparate).    |
| `metadata`            | No       | Objeto    |       |
| `order_status_url`    | No       | Cadena    | URL para ver el estado del pedido.                                                                          |
| `order_number`        | No       | Cadena    | (Sólo Shopify) Número de pedido único para el pedido realizado.  |
| `tags`                | No       | Matriz     | (Sólo Shopify) Etiquetas de pedido.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Ejemplo de objeto

```json
{
    "name": "ecommerce.order_cancelled",
    "time": "2022-05-23T13:52:38-04:00",
    "properties": {
        "order_id": "820982911946154508",
        "cancel_reason": "no longer necessary",
        "total_value": 421.88,
        "currency": "USD",
        "total_discounts": 5,
        "discounts": [],
        "products": [
            {
                "product_id": "632910392",
                "product_name": "IPod Nano - 8GB",
                "variant_id": "808950810",
                "quantity": 1,
                "price": 199,
                "metadata": {
                    "sku": "IPOD2008PINK"
                }
            }
        ],
        "source": "braze-mock-storefront.myshopify.com",
        "metadata": {
            "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
            "order_number": 1234,
            "tags": [
                "heavy",
                "heavy2"
            ]
        }
    }
}
```

{% endtab %}
{% endtabs %}

## Plantillas eCommerce Canvas

Braze ha creado plantillas Canvas prediseñadas que se basan en eventos recomendados para el comercio electrónico, como los clientes que iniciaron el proceso de pago pero lo abandonaron antes de realizar el pedido. Puedes utilizar estos eventos para tomar decisiones informadas que mejoren tu viaje de usuario personalizando la mensajería y dirigiéndote a audiencias específicas.

Consulta nuestros [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) dedicados [al comercio electrónico]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases) para saber más sobre cómo puedes utilizar estos eventos con las plantillas de Canvas.

## Campos calculados por el usuario

Utilizamos cálculos estandarizados de campos de usuario para los siguientes campos: 

- **Ingresos totales** = suma del valor total del pedido realizado - suma del valor total del pedido reembolsado
- **Recuento total de pedidos** = recuento de eventos distintos de pedidos realizados - recuento de cancelaciones distintas de pedidos
- **Valor total** del reembolso = suma del valor total reembolsado del pedido 

Estos cálculos de campo de usuario también se incluyen en la pestaña **Transacciones** de los perfiles de usuario.

![La pestaña "Transacciones" con campos calculados por el usuario.]({% image_buster /assets/img/Shopify/transactions_tab.png %}){: style="max-width:60%;"}

{% alert important %}
Los planes para eliminar gradualmente el acto de compra se anunciarán a finales de 2025. A largo plazo, el evento de compra será sustituido por nuevos [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/), que vendrán con características mejoradas de segmentación, informes, análisis y mucho más. Sin embargo, los nuevos eventos de comercio electrónico no serán compatibles con las características existentes relacionadas con el evento de compra, como el valor de duración (LTV) o los informes de ingresos en Lienzos o campañas. Para obtener una lista completa de las características relacionadas con los [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events), consulta la sección sobre [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}
