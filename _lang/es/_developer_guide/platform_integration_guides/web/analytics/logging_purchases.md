---
nav_title: Registrar compras
article_title: Registro de compras para la web
platform: Web
page_order: 4
page_type: reference
description: "Este artículo describe cómo registrar compras y añadir propiedades a esas compras para la Web."

---
 
# Registrar compras

> Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida. 

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

Para utilizar esta característica, añade la llamada [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) después de una compra exitosa en tu aplicación. Nota que `quantity` debe ser menor o igual que 100.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## Añadir propiedades

Puedes añadir [metadatos](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) sobre las compras pasando una [matriz de propiedades del evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) o pasando un objeto de pares clave-valor con la información de tu compra. 

#### Formateo de objetos

Las claves son objetos `string`, y los valores pueden ser objetos `string`, `numeric`, `boolean` o `Date`.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

## API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la documentación de [la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

