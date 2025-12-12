---
nav_title: "Objeto de compra"
article_title: Objeto de compra API
page_order: 8
page_type: reference
description: "Este artículo de referencia explica los distintos componentes de un objeto de compra, cómo utilizarlo correctamente y ejemplos en los que inspirarse."

---

# Objeto de compra

> Este artículo explica los distintos componentes de un objeto de compra, cómo utilizarlo correctamente, las mejores prácticas y ejemplos en los que inspirarse.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

## ¿Qué es un objeto de compra?

Un objeto de compra es un objeto que se pasa a través de la API cuando se ha realizado una compra. Cada objeto de compra está ubicado dentro de una matriz de objetos de compra, siendo cada objeto una única compra realizada por un usuario concreto en un momento determinado. El objeto de compra tiene muchos campos diferentes que permiten al backend Braze almacenar y utilizar esta información para la personalización, la recopilación de datos y la personalización.

### Cuerpo del objeto

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required.
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  // See the following product_id naming conventions for clarification.
  "product_id" : (required, string) identifier for the purchase, for example, Product Name or Product Category,
  "currency" : (required, string) ISO 4217 Alphabetic Currency Code,
  //Revenue from a purchase object is calculated as the product of quantity and price.
  "price" : (required, float) value in the base currency unit (for example, Dollars for USD, Yen for JPY),
  "quantity" : (optional, integer) the quantity purchased (defaults to 1, must be <= 100 -- currently, Braze treats a quantity _X_ as _X_ separate purchases with quantity 1),
  "time" : (required, datetime as string in ISO 8601) Time of purchase,
  // See the following purchase object explanation for clarification.
  "properties" : (optional, Properties Object) properties of the event,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
}
```

- [ID usuario externo]({{site.baseurl}}/api/basics/#user-ids)
- [Identificador de la aplicación]({{site.baseurl}}/api/identifier_types/)
- [Wiki de código de divisa ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)
- [Wiki de código de hora ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)

## ID del producto de compra

Dentro del objeto de compra, el `product_id` es un identificador de la compra (como `Product Name` o `Product Category`):

- Braze te permite almacenar hasta 5000 `product_id` en el panel.
- La dirección `product_id` puede tener hasta 255 caracteres.

### Convenciones de denominación

En Braze, ofrecemos algunas convenciones generales de nomenclatura para el objeto de compra `product_id`. Al elegir `product_id`, Braze sugiere utilizar nombres simplistas como el nombre del producto o la categoría del producto (en lugar de SKU) con la intención de agrupar todos los artículos registrados por este `product_id`.

Esto ayuda a que los productos sean fáciles de identificar para su segmentación y desencadenamiento.

### Registrar las compras a nivel de pedido

Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id` (como `Online Order` o `Completed Order`).

Por ejemplo, para registrar compras a nivel de pedido en el SDK Web:

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
      }
    }
  ]
}
```

## Objeto propiedades de compra

Los eventos personalizados y las compras pueden tener propiedades del evento. Los valores de las "propiedades" deben ser un objeto en el que las claves son los nombres de las propiedades y los valores son los valores de las propiedades. Los nombres de propiedad deben ser cadenas no vacías de menos o igual a 255 caracteres, sin signos de dólar al principio. 

Los valores de propiedad pueden ser cualquiera de los siguientes tipos de datos:

| Tipo de datos | Descripción |
| --- | --- |
| Números | Como [números enteros](https://en.wikipedia.org/wiki/Integer) o [flotantes](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos |  |
| Fechas y horas | Formateados como cadenas en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) o `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. No se admite dentro de matrices. |
| Cadenas | 255 caracteres o menos. |
| Matrices | Las matrices no pueden incluir fechas. |
| Objetos | Los objetos se ingestarán como cadenas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Los objetos de propiedades del evento que contienen valores de matrices u objetos pueden tener una carga útil de propiedades del evento de hasta 50 KB.

### Propiedades de la compra

[Las propiedades de la compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) pueden utilizarse para desencadenar mensajes y para la personalización mediante Liquid, permitiéndote también segmentar en función de estas propiedades.

#### Convenciones de denominación

Es importante tener en cuenta que esta característica se activa **por producto**, no por compra. Por ejemplo, si tienes un gran volumen de productos distintos, pero cada uno tiene las mismas propiedades, segmentar puede ser más innecesario.

En esta instancia, recomendamos utilizar nombres de productos a "nivel de grupo" en lugar de algo granular al configurar las estructuras de datos. Por ejemplo, una empresa de billetes de tren debería tener productos para "viaje de ida", "viaje de vuelta", "multiciudad", y no transacciones específicas como "transacción 123" o "transacción 046". Como otro ejemplo, con el evento de compra "comida", lo mejor sería establecer las propiedades "tarta" y "bocadillo".

{% alert important %}
Ten en cuenta que los productos se pueden añadir a través de la API REST de Braze. Por ejemplo, si envías una llamada al punto final `/users/track` e incluyes un nuevo ID de compra, se creará automáticamente un producto en la sección **Configuración de datos** > **Productos** del panel.
{% endalert %}

### Ejemplo de objeto de compra

```html
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "purchases" : [
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "backpack",
      "currency" : "USD",
      "price" : 40.00,
      "time" : "2013-07-16T19:20:30+01:00",
      "properties" : {
        "color" : "red",
        "monogram" : "ABC",
        "checkout_duration" : 180,
        "size" : "Large",
        "brand" : "Backpack Locker"
      }
    },
    {
      "external_id" : "user1",
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pencil",
      "currency" : "USD",
      "price" : 2.00,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "number" : 2,
        "sharpened" : true
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "pen",
      "currency" : "USD",
      "price" : 2.50,
      "time" : "2013-07-17T19:20:20+01:00",
      "properties" : {
        "color" : "blue",
      }
    }
  ]
}
```

### Objetos de compra, objetos de evento y webhooks

Utilizando el ejemplo proporcionado, podemos ver que alguien compró una mochila con las propiedades: color, monograma, duración de la compra, tamaño y marca. A continuación, podemos crear segmentos con estas propiedades utilizando [las propiedades del evento de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#purchase-properties) o enviar mensajes personalizados a través de un canal utilizando Liquid. Por ejemplo: "Hola, **Ann F.**, gracias por comprar esa **mochila roja mediana** por ** 40,00 dólares**. Gracias por comprar en **Backpack Locker**".

Si quieres guardar, almacenar y hacer un seguimiento de las propiedades para segmentar, tienes que configurarlas como atributos personalizados. Esto puede hacerse utilizando [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), que te permiten dirigirte a los usuarios basándote en un evento personalizado o en el comportamiento de compra almacenado durante toda la vida de ese perfil de usuario.


