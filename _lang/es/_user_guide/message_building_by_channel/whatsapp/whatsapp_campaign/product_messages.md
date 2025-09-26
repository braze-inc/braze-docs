---
nav_title: Mensajes de producto
article_title: Mensajes de producto
page_order: 1
description: "En esta página se explica cómo utilizar los mensajes de producto de WhatsApp para enviar mensajes de WhatsApp interactivos que muestren productos de tu catálogo de Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Mensajes de producto

> Los mensajes de producto te permiten enviar mensajes de WhatsApp interactivos que muestran productos directamente desde tu catálogo Meta.

{% alert important %}
Los mensajes de producto de WhatsApp se encuentran actualmente en acceso anticipado y está previsto que tengan actualizaciones continuas durante la duración del acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

Cuando envías un mensaje de WhatsApp sobre un producto a un usuario, éste realiza el siguiente recorrido del cliente:

1. El usuario recibe tu mensaje de producto o catálogo en WhatsApp.
2. El usuario añade productos a su cesta directamente desde WhatsApp.
3. El usuario pulsa **Realizar pedido** en WhatsApp.
4. Tu sitio web o aplicación recibe los datos del carrito de Braze y genera un enlace de pago.
5. El usuario es dirigido a tu sitio web o aplicación para completar su pago.

Cuando los usuarios añaden artículos a su cesta a través de mensajes de catálogo, Braze recibe datos de webhook para acciones de seguimiento.

## Requisitos

| Requisito | Descripción |
| --- | --- |
| Cuenta de WhatsApp Business | Para utilizar los mensajes de producto de WhatsApp, debes tener una cuenta de WhatsApp Business conectada con Braze. |
| Metacatálogo | Tienes que configurar un Metacatálogo en tu administrador de comercio. |
| Cumplimiento del plazo | Cumplir las [Condiciones y Políticas de Meta Commerce](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Plantillas de mensajes de productos

{% tabs %}
{% tab Mensajes del catálogo %}

Los mensajes de catálogo muestran todo tu catálogo de productos en un formato interactivo.

{% alert note %}
No necesitas hacer selecciones adicionales de productos en Braze, ya que la conexión del catálogo la gestiona Meta y, por tanto, se hereda en tu catálogo de productos.
{% endalert %}


{% endtab %}
{% tab Mensajes multiproducto %}

Los mensajes multiproducto destacan productos específicos de tu catálogo, con hasta 30 elementos destacados por mensaje. Actualmente, no hay un selector de productos integrado, por lo que debes consultar manualmente tu Metacatálogo para obtener las SKU de los productos.

{% alert important %}
Hay un problema conocido de visualización de cabeceras con plantillas de mensajes multiproducto en Meta. Meta es consciente del problema y está trabajando en una solución.
{% endalert %}


{% endtab %}
{% endtabs %}

## Configuración de los mensajes de producto

1. En el [administrador de comercio de Meta](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), sigue [las instrucciones de Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) para crear tu catálogo Meta. Asegúrate de que estás en la misma Meta Cartera de Negocios donde reside tu cuenta de WhatsApp Business conectada a Braze.
2. Sigue las instrucciones de Meta para [conectar tu catálogo Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) a tu cuenta WhatsApp Business conectada a Braze, asignando el permiso "Gestionar catálogo" en Meta Business Manager. 

![Meta "Catálogos" página con una flecha apuntando al botón "Asignar socio" para el catálogo llamado "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:80%;"}

Asegúrate de utilizar el ID del administrador de empresas de Braze, `332231937299182`, como ID de la empresa asociada.

![Ventana para compartir un catálogo con un socio que contiene campos para introducir un ID de empresa del socio y asignar el permiso "Gestionar catálogo".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Selecciona la configuración de tu Metacatálogo. Debes seleccionar **Mostrar icono de catálogo en la cabecera del chat** para enviar mensajes de catálogo.

![Página de configuración del administrador de WhatsApp para el catálogo "Catálogo_productos".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:80%;"}

{: start="4"}
4\. En Braze, sigue el proceso de [registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) para proporcionar permisos. Esto desbloqueará el selector de productos integrado Braze.

{% alert tip %}
Para conocer las mejores prácticas a seguir al crear metacatálogos, consulta [Consejos para crear un catálogo de alta calidad en el Administrador de comercio](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Crear un mensaje de producto

1. En tu administrador de Meta Business, ve a **Plantillas de mensajes**.
2. Selecciona **Catálogo** como formato y, a continuación, elige entre **Mensaje de catálogo** (muestra el catálogo completo) y **Mensaje de catálogo multiproducto** (destaca artículos concretos).
3. En Braze, crea una campaña de WhatsApp o un paso en Canvas de mensajes.
4. Selecciona el grupo de suscripción que coincida con el lugar donde enviaste la plantilla.
5. Selecciona **la plantilla de mensaje de WhatsApp**. (Los mensajes sobre productos y catálogos aún no están disponibles en los mensajes de respuesta).
6. Selecciona la plantilla que quieras utilizar.
    - Si seleccionas una plantilla multiproducto, proporciona el título de la sección y los ID de contenido de los productos a destacar.

![Lista de elementos con campos para introducir los títulos de tus secciones y el ID del contenido.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

{: start="7"}
7\. Sigue construyendo tu mensaje.

## Administrador de productos

### Acceder al Administrador de Comercio

En tu Meta Administrador de Empresas, ve a **Administrador de Comercio** y selecciona tu organización. Aquí puedes gestionar los activos de tu catálogo, por ejemplo
- Crear nuevos catálogos
- Añadir productos a catálogos existentes
- Actualizar la información del producto
- Eliminar artículos descatalogados

{% alert important %}
Si eliminas los productos referenciados de tu catálogo, los mensajes asociados no se enviarán.
{% endalert %}

## Pasar por caja: Procesamiento de carritos y webhooks

Cuando los usuarios interactúan con tus mensajes de WhatsApp sobre productos, pueden examinar los productos y añadir artículos a su cesta. Sin embargo, actualmente no hay ninguna función de pago integrada para la información de envío o el procesamiento de pagos. En su lugar, te animamos a que crees un carrito dentro de tu propia aplicación o sitio web y dirijas a los usuarios a ese carrito mediante un enlace personalizado.

### Consideraciones

- **No hay pago desde la aplicación:** Los usuarios no pueden realizar compras directamente en WhatsApp. Todas las transacciones deben redirigirse a tu sitio web o aplicación.
- **Se requiere enlace personalizado:** Necesitas crear un enlace personalizado que dirija a los usuarios a su carrito en tu plataforma.
- **Configuración manual:** El proceso de instalación requiere la configuración manual de tu carrito y de los flujos de trabajo de mensajería.

{% alert note %}
Actualmente no admitimos pagos que se produzcan directamente en WhatsApp, y la compatibilidad futura será específica de cada país (actualmente, Meta sólo lo ofrece a empresas con sede en India, Brasil y Singapur y que trabajen directamente con usuarios de estos países).
{% endalert %}

### Configuración de los desencadenadores de eventos del carrito

Cuando un cliente hace un pedido en WhatsApp, Braze automáticamente:
1. Recibe el contenido del carrito de WhatsApp (ID de producto, cantidades y otros datos del pedido).
2. Crea un evento de comercio electrónico `ecommerce.cart_update` con todos los datos relevantes, incluido `source = whats_app`.
3. Desencadena una respuesta, permitiéndote configurar campañas automatizadas para responder al pedido.

El evento `ecommerce.cart_update` eCommerce sólo aparece listado en Braze después de que se haya enviado un evento, lo que puede hacerse generando un mensaje de producto de prueba desde Braze y enviando un evento de carrito.
El evento del carro incluye:

- **ID del carrito:** Identificador único para el carrito
- **Productos:** Lista de productos con ID de producto, cantidades y precios
- **Valor total:** Suma de todas las partidas
- **Moneda:** La moneda del carro
- **Fuente:** Marcado como "whats_app"
- **Metadatos:** Datos adicionales como ID del catálogo y texto del mensaje

Puedes encontrar información adicional sobre los eventos del carrito de Braze en [Tipos de eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events).

### Configurar una respuesta desencadenada

1. Crea un desencadenador de eventos personalizado para `ecommerce.cart_updated`.
2. Añade un filtro de propiedad para `source = "whats_app"`.

![Paso en Canvas para desencadenar un evento personalizado `ecommerce.cart_updated` con la propiedad básica "fuente" igual a `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\. Configura acciones de seguimiento basadas en los datos del carrito.

### Implementaciones de pago recomendadas 

{% tabs %}
{% tab Enlaces sencillos para carritos basados en Liquid %}

Utiliza Liquid para crear URL de carrito directamente en tu mensaje de respuesta. Esto es mejor si tienes ID de producto consistentes entre WhatsApp y tu plataforma de comercio electrónico.

#### Ejemplo Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configurar

1. Crea una campaña de mensajería de respuesta de WhatsApp con el desencadenante de un evento de comercio electrónico de `ecommerce.cart_update`.
2. Crea un mensaje posterior con la URL del carrito.
3. Construye la URL de tu carrito con Liquid. Si utilizas Shopify, puedes [crear un carrito permalink](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) con el ejemplo anterior Liquid.

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para un carro generado por Liquid: Meta envía un mensaje de pedido recibido a Braze, que desencadena una acción basada en el desencadenante y luego crea un mensaje con un enlace al carrito, que a su vez envía un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Contenido conectado %}

Haz una llamada API a tu sistema de comercio electrónico para generar una URL de pago personalizada. Es lo mejor si necesitas una generación dinámica de URL de carrito o un mapeado complejo de productos.

#### Configurar

1. Crea una campaña webhook o un paso en Canvas desencadenado por el evento de [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) que enviará los datos del carrito a tu sistema de comercio electrónico.
2. Crea una campaña de WhatsApp o un paso en Canvas de Mensajes desencadenado por el mismo evento de eCommerce para enviar un mensaje de respuesta de WhatsApp con la URL del carrito al usuario. Sigue las instrucciones del mensaje de respuesta posterior para utilizar [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content).

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para una llamada de Contenido conectado: Meta envía un mensaje de pedido recibido a Braze, que tiene llamadas de ida y vuelta con una plataforma de comercio electrónico, y luego envía un mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook y eventos personalizados %}

Utiliza webhooks para enviar los datos del carrito a tu sistema y, a continuación, desencadenar mensajes de seguimiento a través de eventos personalizados. Es la mejor opción para integraciones complejas que requieran un amplio procesamiento de carritos o flujos de trabajo de varios pasos.

#### Configurar

Crea una campaña webhook o un paso en Canvas desencadenado por el evento de comercio electrónico `ecommerce.cart_update`, que enviará los datos del carrito a tu sistema de comercio electrónico. Tu API lo hará entonces:
1. Recibir datos del carrito
2. Crea un carrito en tu sistema
3. Generar la URL de pago
4. Envía un evento `checkout_started` a Braze, desencadenando el envío de tu mensaje de WhatsApp con el enlace de pago

![Diagrama que muestra el flujo de trabajo de la experiencia de pago para webhooks y eventos personalizados: Meta envía un mensaje de pedido recibido a Braze, que tiene llamadas de ida y vuelta con una plataforma de comercio electrónico, y luego envía un mensaje de WhatsApp con la URL del carrito.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Pruebas y validación

### Requisitos de los mensajes de prueba

La funcionalidad del carro se traslada entre los mensajes de prueba, pero el procesamiento del resultado entrante no se traslada.

### Vista previa del mensaje

- Las imágenes y detalles de los productos se extraen de tu Metacatálogo.
- La vista previa interactiva muestra marcadores de posición hasta que se complete la integración.

### Códigos de error 

- Si el ID de un producto no existe en el catálogo, recibirás el error `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Si un catálogo se desconecta del WABA, recibirás el error `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
