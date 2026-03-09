---
nav_title: Seguimiento de clics
article_title: Seguimiento de clic
page_order: 3
description: "Este artículo de referencia explica cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar enlaces acortados, utilizar tu dominio personalizado en enlaces rastreados y mucho más."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Seguimiento de clics

> En esta página se explica cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar enlaces acortados, utilizar tu dominio personalizado en enlaces rastreados y mucho más.

El seguimiento de clics te permite medir cuándo alguien pulsa un enlace en tu mensaje de WhatsApp, lo que te ofrece una visión clara del contenido que genera más interacción. Braze acorta tus URL, añade seguimiento en segundo plano y registra los clics a medida que se producen.

Puedes activar el seguimiento de clics tanto en los mensajes de respuesta como en los mensajes de plantilla. Funciona con enlaces en botones y texto del cuerpo, y admite URL personalizadas y dominios personalizados. Una vez activada, podrás ver los datos de clics en tus informes de rendimiento de WhatsApp y realizar la segmentación de los usuarios en función de quién ha hecho clic en qué.

{% alert note %}
El seguimiento de clics no funciona con vínculos profundos. Puedes acortar enlaces universales de proveedores como Branch o Appsflyer, pero Braze no puede solucionar los problemas que puedan surgir al hacerlo (como romper la atribución o provocar una redirección).
{% endalert %}

## Cómo funciona

### Mensajes de respuesta 

Para configurar el seguimiento de clics para los mensajes de respuesta:
1. Crea un mensaje de respuesta que incluya un botón de llamada a la acción (CTA) con la URL de un sitio web.
2. Habilita el seguimiento de clics haciendo clic en el botón correspondiente de la interfaz.

El enlace se acortará al dominio Braze, o al dominio personalizado especificado para el grupo de suscripción, y se personalizará para el usuario.

Todas las URL estáticas que empiecen por `http://` o `https://` se acortarán. Las URL acortadas que contengan personalización Liquid (como la segmentación por seguimiento a nivel de usuario) tendrán una validez de dos meses.

![Creador de mensajes de WhatsApp con cuerpo del mensaje y un botón.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Mensajes de plantilla 

En el caso de los mensajes de plantilla, la URL base debe enviarse correctamente al crear la plantilla para activar el seguimiento de clics.

#### Paso 1: Crea una plantilla compatible con el seguimiento de clics en WhatsApp.

1. En tu WhatsApp Administrador, crea una URL base que sea tu dominio personalizado o .`brz.ai`
2. Asegúrate de que los enlaces incluidos en la plantilla sean compatibles con el seguimiento de clics.
3. No modifiques las variables de la plantilla después de configurarla como campaña en Braze, ya que no se podrán incorporar los cambios posteriores.
4. Para los enlaces de los botones CTA, selecciona **Dinámico** y, a continuación, proporciona la URL base (`brz.ai`o tu dominio personalizado).<br><br>![Sección para crear una llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Para los enlaces en el cuerpo del texto, al escribir la plantilla en tu administrador de WhatsApp, elimina cualquier espacio insertado para los enlaces contenidos en el cuerpo que quieras realizar el seguimiento de ellos.<br><br>![Cuadro de texto para introducir el cuerpo del contenido de la llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Paso 2: Completa tu plantilla en Braze.

Al redactar, Braze detectará automáticamente qué plantillas tienen dominios URL compatibles, tanto en el cuerpo del texto como en los botones CTA. El estado se mostrará en la parte inferior de la plantilla. 

![Sección «Estado del enlace» que muestra un estado activo para el seguimiento de clics.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Enlaces compatibles:** Los enlaces que se envíen con la URL base correspondiente tendrán habilitado el seguimiento de clics.
- **Enlaces parcialmente compatibles:** Si algunos enlaces de una plantilla se envían como URL completas, el seguimiento de clics **no** se aplicará a esos enlaces.
- **Enlaces no compatibles:** Los enlaces sin una URL base aprobada **no** tendrán capacidad de seguimiento de clics.

Se deberá proporcionar la URL de destino para cualquier enlace con una URL base que coincida con`brz.ai`  o con tu dominio personalizado. 

![Sección «Botones» con campos para el nombre del botón, la URL del sitio web y la URL de seguimiento de clics.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Envío de mensajes de plantilla a través de la API**: El seguimiento de clics de WhatsApp (utilizando`brz.ai`  o un dominio de seguimiento personalizado y el campo **URL de seguimiento de clics** en el creador de mensajes) no es compatible cuando se envían mensajes de plantilla de WhatsApp a través del[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) [ punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

Si envías un mensaje de plantilla a través de la API, puedes rellenar las variables URL de CTA (utilizando `button_variables`), pero Braze no genera una URL de seguimiento de clics ni un enlace de redireccionamiento en el flujo de solicitudes de la API. Para utilizar el seguimiento de clics, envía la plantilla desde el panel de Braze o a través de un activador de campaña de Braze.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Personalización líquida en las URL

Puede construir dinámicamente su URL directamente dentro del compositor Braze, lo que le permite añadir parámetros UTM dinámicos a sus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que vuelve a estar en stock).
Las URL se pueden generar de forma dinámica mediante el uso de cualquier etiqueta de personalización Liquid compatible.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos la abreviación de variables Liquid personalizadas, como en estos ejemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Acortar las URL generadas por las variables de Liquid

Braze acorta las URL generadas por Liquid, incluso las incluidas en las propiedades que se desencadenan mediante API. Por ejemplo, si{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}  representa una URL válida, acortaremos y realizaremos el seguimiento de esa URL antes de enviar el mensaje de WhatsApp.

## Pruebas

Antes de lanzar tu campaña o Canvas, lo más recomendable es realizar una vista previa y probar tu mensaje primero. Para ello, ve a la pestaña **Prueba** para obtener una vista previa y enviar un WhatsApp a grupos de prueba de contenido o a un usuario individual.

Esta vista previa se actualizará con la personalización pertinente y la URL acortada. 

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando se activa el borrador de Canvas.
{% endalert %}

## Informe

Cuando el seguimiento de clics está activado o se utiliza con plantillas compatibles, la tabla de rendimiento de WhatsApp incluye la columna **«Total de clics»,** que muestra el recuento de eventos de clic por variante y la tasa de clics asociada. Para obtener más información sobre las métricas de WhatsApp, consulta [Rendimiento]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics) de [los mensajes de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![Paso en Canvas del mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Los datos de clics se reportarán automáticamente en el panel de análisis.

![Tabla de rendimiento de los mensajes de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Reorientar usuarios 

Puedes utilizar el`Clicked/Opened Step`filtro y`clicked tracked WhatsApp link`la interacción para segmentar a los usuarios en función de sus interacciones con los enlaces.

![Grupo de filtros para filtrar «enlace de WhatsApp con seguimiento al hacer clic».]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Sé qué usuarios individuales hacen clic en una URL?

Sí. Cuando el seguimiento de clics está activado (o habilitado según la configuración de la plantilla), puedes reorientar a los usuarios que han hecho clic en las URL aprovechando los filtros de retargeting de WhatsApp o los eventos de clic de WhatsApp (`users.messages.whatsapp.Click`) enviados por Currents.

### ¿Las vistas previas en el dispositivo WhatsApp cuentan como clics? 

No, no contribuyen a la tasa de clics de los mensajes de WhatsApp. 

