---
nav_title: Registrar compras
article_title: Registro de compras para Windows Universal
platform: Windows Universal
page_order: 4
description: "En este artículo de referencia se explica cómo registrar compras en la plataforma Universal de Windows."
hidden: true
---
 
# Registrar compras
{% multi_lang_include archive/windows_deprecation.md %}

Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestro artículo [Buenas prácticas][3]. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

Para utilizar esta característica, añade esta llamada al método después de una compra con éxito en tu aplicación:

Las compras se registran utilizando `EventLogger`, que es una propiedad expuesta en IAppboy. Para obtener una referencia a `EventLogger`, llama a `Appboy.SharedInstance.EventLogger`.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

## API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la documentación de [la API de usuario][2] para más detalles.

[2]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
