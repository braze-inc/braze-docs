---
nav_title: Sincronización de productos de Shopify
article_title: Sincronización de productos de Shopify
alias: /shopify_catalogs/
page_order: 4
description: "Este artículo de referencia explica cómo importar tus productos de Shopify a los catálogos de Braze."
---

# Sincronización de productos en Shopify 

> Puedes sincronizar todos los productos de tu tienda Shopify con un [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) Braze para una mayor personalización de la mensajería. 

Los catálogos de Shopify se actualizarán casi en tiempo real a medida que realices ediciones y cambios en los productos de tu tienda Shopify. Puedes enriquecer tu carrito abandonado, la confirmación del pedido y mucho más con los detalles y la información más actualizados sobre los productos.

## Configuración de la sincronización de productos de Shopify {#setting-up}

Si ya has instalado tu tienda Shopify, puedes sincronizar tus productos siguiendo las instrucciones que se indican a continuación. 

### Paso 1: Activa la sincronización

Puedes sincronizar tus productos con un catálogo Braze a través del flujo de instalación de Shopify o en la página del socio de Shopify. 

![Paso 3 del proceso de configuración con "Shopify Variant ID" como "Identificador del producto del catálogo".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Los productos sincronizados con un catálogo Braze contribuirán a tu [límite de Catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits).

### Paso 2: Selecciona el identificador de tu producto

Selecciona qué identificador de producto utilizar como ID del catálogo:
- ID de variante en Shopify
- SKU

Los valores de ID y cabecera del identificador de producto que elijas sólo pueden incluir letras, números, guiones y guiones bajos. Si el identificador del producto no sigue este formato, Braze lo filtrará de la sincronización de tu catálogo.

Este será el identificador principal que utilizarás para hacer referencia a la información del catálogo de Braze. 

{% alert note %}
Si seleccionas SKU como ID del catálogo, asegúrate de que todos los productos y variantes de tu tienda tienen un SKU establecido y son únicos. 
- Si a un artículo le falta un SKU, Braze no puede sincronizar ese producto en el catálogo. 
- Si tienes más de un producto con el mismo SKU, esto puede provocar un comportamiento inesperado o que la información del producto sea anulada involuntariamente por el SKU duplicado.
{% endalert %}

### Paso 3: Sincronización en curso

Recibirás una notificación en el panel y tu estado se mostrará como "En curso" para indicar que se está iniciando la sincronización inicial. Ten en cuenta que el tiempo que tarde en finalizar la sincronización dependerá de cuántos productos y variantes tenga que sincronizar Braze desde Shopify. Durante este tiempo, puedes salir de esta página y esperar a recibir una notificación en el panel o un correo electrónico que te avise cuando se haya completado.

Ten en cuenta que si la sincronización inicial supera el [límite de tu catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits), Braze dejará de sincronizar más productos. Si superas el límite después de que la sincronización se haya realizado correctamente debido a que se han añadido nuevos productos con el tiempo, la sincronización dejará de estar activa. En ambos casos, las actualizaciones de productos de Shopify ya no se reflejarán en Braze. Ponte en contacto con tu administrador de cuentas para considerar la posibilidad de subir de nivel. 

### Paso 4: Sincronización completada

Recibirás una notificación en el panel y un correo electrónico cuando la sincronización se haya realizado correctamente. La página del socio de Shopify también actualizará el estado en los catálogos de Shopify a "Sincronizando". Puedes ver tus productos haciendo clic en el nombre del catálogo en la página del socio de Shopify.

Consulta los [casos de uso adicionales de Catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases) para saber más sobre cómo aprovechar los datos de los catálogos para personalizar tu mensaje.

#### Datos de catálogo de Shopify compatibles

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Modificar el catálogo de Shopify de cualquier forma puede interferir involuntariamente con la sincronización de productos en tiempo real. No hagas ninguna modificación en el catálogo de Shopify, ya que podría ser anulada por Shopify. En su lugar, realiza las actualizaciones de producto necesarias en tu instancia de Shopify.<br><br>Para eliminar tu catálogo de Shopify, ve a la página de Shopify y desactiva la sincronización. No elimines el catálogo de Shopify directamente en la página de catálogos.
{% endalert %}

##### Utilizando `product_handle` o `product_url`

Para acceder y utilizar `product_handle` y `product_url`, desconecta y vuelve a conectar tu catálogo de Shopify haciendo lo siguiente.

1. Ve a la página de integración de Shopify y selecciona **Editar configuración**.

![Página de integración de Shopify.]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\. En el paso **Sincronizar catálogo**, alterna entre desactivar el catálogo y actualizar la configuración.
3\. Alterna el catálogo y actualiza la configuración.

![Paso "Sincronizar catálogo" de Shopify con alternar catálogo.]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## Casos de uso de existencias remanentes y bajada de precios

Para configurar las notificaciones de falta de existencias, sigue los pasos que se [indican aquí]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications).

Para configurar las notificaciones de bajada de precios, sigue los pasos que se [indican aquí]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/).

Ten en cuenta que con la integración de Shopify, tendrás que crear un evento personalizado que capture el estado de suscripción de un usuario en tu catálogo para cada caso de uso. El evento personalizado requerirá una propiedad del evento que mapee el [SKU o el ID de variante de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) que hayas seleccionado como parte de la sincronización de tu producto de Shopify. 

## Cambiar el ID del catálogo

Para cambiar el identificador de producto de tu catálogo de Shopify, tendrás que desactivar la sincronización. Confirma primero que has dejado de enviar mensajes utilizando los datos de este catálogo de Shopify. Vuelve a ejecutar la sincronización inicial del catálogo de Shopify y selecciona el identificador de producto que desees siguiendo los pasos de [sincronización de productos](#setting-up).

## Desactivar la sincronización de tu producto {#deactivate}

Desactivar la característica de sincronización de productos de Shopify eliminará todo tu catálogo y productos. Esto también puede afectar a cualquier mensaje que pueda estar utilizando activamente los datos de producto de este catálogo. Confirma que has actualizado o pausado estas campañas o Lienzos antes de la desactivación, ya que esto podría dar lugar al envío de mensajes sin detalles del producto. No elimines el catálogo de Shopify directamente en la página de catálogos.

## Solución de problemas
Si la sincronización de tu producto de Shopify se encuentra con un error, podría ser el resultado de los siguientes errores. Sigue las instrucciones para corregir el problema y resolver la sincronización:

| Error | Causa | Solución |
| --- | --- | --- |
| Error del servidor | Esto ocurre si hay un error de servidor por parte de Shopify cuando intentamos sincronizar tus productos. | [Desactiva la sincronización](#deactivate) y vuelve a sincronizar todo tu inventario de productos. |
| Duplicar SKU | Esto ocurre si utilizas una SKU como ID de artículo del catálogo y tienes productos con la misma SKU. Como el ID de artículo del catálogo tiene que ser único, todos tus productos deben tener SKU únicos. | Audita tu lista completa de productos y variantes en Shopify para asegurarte de que no hay SKU duplicados. Si hay SKU duplicados, actualízalos para que sean SKU únicos sólo en la cuenta de tu tienda Shopify. Una vez corregido esto, [desactiva la sincronización](#deactivate) y vuelve a sincronizar todo tu inventario de productos. |
| Límite de catálogo superado | Esto ocurre si superas el límite de tu catálogo. Braze no podrá finalizar la sincronización o mantenerla activa debido a que no hay más almacenamiento disponible. | Hay dos soluciones a este problema:<br><br>1\. Ponte en contacto con tu administrador de cuentas para subir de nivel y aumentar el límite de tu catálogo. <br><br>2\. Libera espacio de almacenamiento borrando cualquiera de los siguientes elementos:<br>\- Artículos de otros catálogos<br>\- Otros catálogos<br>\- Selecciones creadas<br><br> Después de utilizar cualquiera de las dos soluciones, hay que desactivar la sincronización y volver a sincronizarla. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

