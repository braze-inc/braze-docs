---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_type: reference
description: "Este artículo de referencia describe los eventos recomendados, que son recomendaciones proporcionadas por Braze para los eventos de comercio electrónico."
---

# Eventos recomendados

> Los eventos recomendados se corresponden con los casos de uso más comunes del comercio electrónico. Al utilizar eventos recomendados, puedes desbloquear plantillas Canvas prediseñadas, paneles de informes mapeados según el ciclo de vida del cliente y mucho más.

Por ejemplo, puedes tener un evento personalizado llamado “cart_updated” o “update_to_cart” para capturar cuando un usuario ha añadido, eliminado o actualizado los productos de su cesta. Para los eventos recomendados, Braze proporcionará la plantilla del evento, que incluye un nombre definido y las propiedades relevantes para este evento.

{% alert important %}
Los eventos recomendados están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si aprovechas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Cómo funciona

Braze aplica una validación especial a todos los eventos recomendados, y algunos eventos recomendados tienen acciones especiales de post-procesamiento. Para determinados eventos recomendados por el sector, Braze puede admitir un tratamiento especial, como nuevos desencadenantes basados en acciones para campañas y Lienzos.

Los eventos recomendados funcionan de forma similar a [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events). Puedes exportar eventos recomendados desde Currents, incluirlos en listas de bloqueo y utilizarlos en informes. También puedes enviar datos a Braze para el seguimiento de estos eventos utilizando el [SDK de Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) o el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

### Eventos recomendados en eCommerce

Los [eventos]({{site.baseurl}}/ecommerce_events/) recomendados [de eCommerce]({{site.baseurl}}/ecommerce_events/) se basan en eventos recomendados. Estos eventos recomendados de comercio electrónico hacen un seguimiento de las acciones realizadas por tus clientes, como ver un producto, actualizar su cesta o iniciar el proceso de pago. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Plantillas Canvas para comercio electrónico

Consulta nuestros [casos de uso]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados [al comercio electrónico]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) para obtener más ideas sobre cómo utilizar las plantillas prediseñadas de Braze Canvas para poner en práctica estrategias esenciales.

## Preguntas más frecuentes

### ¿Los eventos recomendados son lo mismo que los eventos personalizados?

No. Braze definirá esquemas de datos opinables para los eventos recomendados. Incluirá propiedades del evento obligatorias y opcionales que se someterán a un proceso de validación en Braze. [Los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) son acciones específicas realizadas por, o actualizaciones sobre, tus usuarios en tu aplicación o sitio web que quieres seguir. Puedes personalizar el nombre del evento y lo que sigue.

### ¿Puedo personalizar el nombre de los eventos recomendados?

No. Los eventos recomendados tienen nombres y propiedades del evento normalizados. Estas normalizaciones ayudan a crear coherencia entre tus datos.

### ¿Puedo seguir utilizando los eventos de compra para registrar las compras?

Con el lanzamiento de los eventos recomendados de comercio electrónico, Braze eliminará gradualmente el evento de compra heredado en el futuro. Si actualmente utilizas el evento de compra, recibirás un aviso previo sobre los planes de amortización. Mientras tanto, puedes seguir utilizando los eventos de compra hasta la fecha oficial de caducidad.