---
nav_title: Registrar compras
article_title: Registro de compras para Roku
platform: Roku
page_order: 3
page_type: reference
description: "Esta página proporciona métodos para registrar eventos de compra para Roku a través del SDK de Braze."

---
 
# Registrar compras

> Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro artículo [Buenas prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Seguimiento de compras e ingresos

Para utilizar esta característica, añade esta llamada al método después de una compra con éxito en tu aplicación:

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### Añadir propiedades

Puedes añadir metadatos sobre las compras pasando un diccionario de propiedades con la información de tu compra.

Las propiedades se definen como pares clave-valor.  Las claves son objetos `String` y los valores pueden ser `String` o `Integer`.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la documentación de [la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

