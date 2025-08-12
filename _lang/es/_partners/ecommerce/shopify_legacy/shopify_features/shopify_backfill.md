---
nav_title: "Relleno histórico de Shopify"
article_title: "Relleno histórico de Shopify"
alias: "/shopify_historical_backfill_legacy/"
description: "Este artículo de referencia describe cómo configurar la reposisición de datos históricos de Shopify, incluidos los riesgos y los datos admitidos."
page_type: partner
search_tag: Partner
page_order: 1
---

# Relleno histórico de Shopify 

> La función de Backfill Histórico de Shopify permite a las marcas sincronizar los datos de clientes y compras de forma automatizada y sin problemas, para que puedas empezar inmediatamente a relacionarte con uno de tus segmentos más valiosos: los compradores. 

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

Como parte de este backfill, Braze importará todos los clientes, pedidos y eventos de compra de los últimos 90 días anteriores a su conexión de integración con Shopify. Tenga en cuenta que esta función es ideal para los nuevos clientes que no tienen ningún mensaje activo en ejecución, dadas las implicaciones que se explican en la siguiente sección. Esta función también contará para tu uso de puntos de datos.

## Riesgos

Esta función importará datos y eventos históricos que podrían tener consecuencias no deseadas, como que los usuarios reciban mensajes irrelevantes e inoportunos para cualquier campaña o lienzo afectado. Las campañas y los lienzos que utilizan los siguientes eventos de activación podrían verse afectados si utilizan alguno de los datos de Shopify que esta función sincroniza:
- Cambiar el valor del atributo personalizado
- Llevar a cabo evento de conversión
- Realizar un evento de excepción para la campaña
- Actualizar el estado de suscripción
- Actualizar el estado del grupo de suscripción
- Agregar una dirección de correo electrónico
- Realizar compra*
- Realizar un evento personalizado\*.

{% alert important %}
Le recomendamos que audite sus campañas activas actuales y Lienzos en busca de mensajes que puedan desencadenar los eventos anteriores utilizando los datos de nuestro Shopify Historical Backfill. 

- Para "Realizar compra" y "Realizar evento personalizado", puede actualizar la [duración de la hora de inicio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) a cualquier fecha y hora después de que su tienda Shopify se haya conectado en Braze. Cualquier evento anterior a esta nueva hora de inicio no activará ningún mensaje. 
- Para todos los demás eventos anteriores, puede [detenerlos temporalmente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) antes de activar el relleno para garantizar que no se envíe ningún mensaje.
{% endalert %}

## Configuración del relleno histórico de Shopify

### Requisitos previos

Los siguientes eventos deben habilitarse antes de activar el relleno o sus datos no se importarán:

- `shopify_created_order`
- Evento de compra de Braze 

Los eventos anteriores se pueden activar durante la configuración de Shopify durante la [selección de eventos]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection).

{% alert important %}
Puedes activar la característica de Reposición Relleno sólo una vez en tu integración.
{% endalert %}

### Paso 1: Inicia el proceso de reposición de Shopify

En la página del socio de Shopify, selecciona **Iniciar reposición de datos**. En el caso de los clientes existentes de Shopify, deberá volver a autorizar el acceso para que Braze recopile todos los eventos de pedidos anteriores antes de poder iniciar el relleno de datos.

![]({% image_buster /assets/img/Shopify/backfill3.png %}){: style="max-width:75%;"}

### Paso 2: Alternar la reposición de datos de Shopify

A continuación, aparecerá el creador de configuración, y podrás habilitar opcionalmente la reposición de datos históricos de Shopify. Como parte de este backfill, Braze sincronizará por defecto sólo los siguientes datos de Shopify de los últimos 90 días anteriores a su integración con Shopify:
- Evento de pedido creado
- Evento de compra de Braze
- Datos del cliente

Para ver qué datos de clientes concretos se están rellenando, puedes visitar la sección [Datos de clientes de Shopify respaldados](#supported-shopify-customer-data).

{% alert note %}
Esta función sólo sincronizará los estados de suscripción de correo electrónico y SMS de los nuevos usuarios creados durante el relleno. Esto no sincronizará los estados de suscripción de los usuarios existentes en Braze para evitar anular los estados actuales de sus usuarios.<br><br>Si tiene algún comentario sobre el comportamiento actual, envíelo a través del portal del producto, que aparece en el **Panel de control** en **Recursos** como **Hoja de ruta del producto** (si utiliza nuestra [navegación actualizada]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), seleccione **Comunidad** > **Hoja de ruta del producto**).
{% endalert %}

Una vez que pulses **Siguiente**, el backfill se activará y empezará a sincronizar los datos anteriores. Tenga en cuenta que el Relleno Histórico sólo puede completarse **una vez**, por lo que no podrá volver a ejecutar esta importación una vez que los datos hayan terminado de sincronizarse.

![]({% image_buster /assets/img/Shopify/backfill1.jpg %}){: style="max-width:75%;"}

### Paso 3: Reposición en curso

Recibirá una notificación en el panel de control y su estado se mostrará como "En curso" para indicar que el relleno ha comenzado. Ten en cuenta que el tiempo que tarde en completarse la reposició n dependerá de cuántos clientes y pedidos tenga que sincronizar Braze desde Shopify. Durante este tiempo, puede salir de esta página y esperar a recibir una notificación en el tablero de mandos o un correo electrónico que le avise de cuándo se ha completado el relleno.

![]({% image_buster /assets/img/Shopify/backfill2.png %}){: style="max-width:75%;"}

### Paso 4: Reposición completada
Recibirás una notificación en el panel y un correo electrónico cuando se haya completado la reposición de Shopify. La página del socio de Shopify también actualizará el estado en Reposición histórica "Completo".

## Datos de clientes de Shopify compatibles

### Atributos personalizados de Shopify

| Nombre del atributo | Descripción |
| --- | --- |
| `shopify_order_count` | Este atributo personalizado corresponde al total de pedidos que este cliente ha completado en Shopify. Esto sólo está disponible para los usuarios que se rellenaron como parte de este proceso. |
| `shopify_total_spent` | Este atributo personalizado corresponde al importe total gastado por este cliente en Shopify. Esto sólo está disponible para los usuarios que se rellenaron como parte de este proceso. |
| `shopify_tags` | Este atributo corresponde a las [etiquetas de cliente](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) establecidas por los administradores de Shopify. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Atributos estándar de Shopify
- Correo electrónico
- Nombre
- Apellido
- Teléfono
- Localidad
- País

