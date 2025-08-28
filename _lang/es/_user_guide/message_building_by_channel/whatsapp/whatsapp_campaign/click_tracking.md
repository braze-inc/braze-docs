---
nav_title: Seguimiento de clic
article_title: Seguimiento de clic
page_order: 2
description: "Este artículo de referencia explica cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar los enlaces acortados, utilizar tu dominio personalizado en los enlaces rastreados y mucho más."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Seguimiento de clics

> Esta página explica cómo activar el seguimiento de clics en tus mensajes de WhatsApp, probar los enlaces acortados, utilizar tu dominio personalizado en los enlaces rastreados y mucho más.

El seguimiento de clics te permite medir cuándo alguien pulsa un enlace en tu mensaje de WhatsApp, dándote una visión clara de qué contenido está generando interacción. Braze acorta tus URL, añade seguimiento entre bastidores y registra los clics en el momento en que se producen.

Puedes activar el seguimiento de clics tanto en los mensajes de respuesta como en los de plantilla. Funciona con enlaces en botones y cuerpo de texto, y admite URL personalizadas y dominios personalizados. Una vez activada, verás los datos de clics en tus informes de rendimiento de WhatsApp y podrás segmentar a los usuarios en función de quién hizo clic en qué.

## Cómo funciona

### Mensajes de respuesta 

Para configurar el seguimiento de clics para los mensajes de respuesta:
1. Crea un mensaje de respuesta que incluya un botón de llamada a la acción (CTA) con la URL de un sitio web.
2. Habilita el seguimiento de los clics haciendo clic en el botón designado de la interfaz.

El enlace se acortará al dominio Braze, o al dominio personalizado especificado para el grupo de suscripción, y se personalizará para el usuario.

Todas las URL estáticas que empiecen por `http://` o `https://` se acortarán. Las URL acortadas que contengan personalización Liquid (como la orientación de seguimiento a nivel de usuario) serán válidas durante dos meses.

![Creador de mensajes de WhatsApp con cuerpo de contenido y un botón.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Mensajes de plantilla 

Para los mensajes de plantilla, la URL base debe enviarse correctamente al crear la plantilla para activar el seguimiento de clics.

#### Paso 1: Crea una plantilla compatible con el seguimiento de clics en WhatsApp

1. En tu administrador de WhatsApp, crea una URL base que sea tu dominio personalizado o `brz.ai`.
2. Asegúrate de que los enlaces incluidos en la plantilla son compatibles con el seguimiento de clics.
3. No cambies las variables de la plantilla después de haberla configurado como campaña en Braze; los cambios posteriores no podrán incorporarse.
4. Para los enlaces de botón CTA, selecciona **Dinámico** y, a continuación, proporciona la URL base (`brz.ai` o tu dominio personalizado).<br><br>![Sección para crear una llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Para los enlaces en el cuerpo del texto, cuando escribas la plantilla en tu administrador de WhatsApp, elimina los espacios insertados para los enlaces contenidos en el cuerpo que quieras seguir.<br><br>![Cuadro de texto para introducir el cuerpo del contenido de la llamada a la acción.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Paso 2: Completa tu plantilla en Braze

Al componer, Braze detectará automáticamente qué plantillas tienen dominios URL compatibles, tanto en el cuerpo del texto como en los botones CTA. El estado se mostrará en la parte inferior de la plantilla. 

![Sección "Estado del enlace" que muestra un estado activo para el seguimiento de los clics.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Enlaces compatibles:** Los enlaces que se envíen con la URL base coincidente tendrán habilitado el seguimiento de clics.
- **Enlaces con soporte parcial:** Si algunos enlaces de una plantilla se envían como URL completas, el seguimiento de clics **no** se aplicará a esos enlaces.
- **Enlaces no compatibles:** Los enlaces sin una URL base aprobada **no** tendrán capacidad de seguimiento de clics.

Tendrás que indicar la URL de destino para cualquier enlace con una URL base que coincida con `brz.ai` o con tu dominio personalizado. 

![Sección "Botones" con campos para el nombre de un botón, la URL del sitio web y la URL de seguimiento de los clics.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include click_tracking.md section='Dominios personalizados' %}

## Personalización líquida en las URL

Puede construir dinámicamente su URL directamente dentro del compositor Braze, lo que le permite añadir parámetros UTM dinámicos a sus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que vuelve a estar en stock).
Las URL pueden generarse dinámicamente mediante el uso de cualquiera de las etiquetas de personalización de Liquid admitidas.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos el acortamiento de variables Liquid definidas de forma personalizada, como en estos ejemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Acortar las URL generadas por las variables de Liquid

Braze acorta las URL renderizadas por Liquid, incluso las incluidas en propiedades desencadenadas por la API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortaremos y haremos un seguimiento de esa URL antes de enviar el mensaje de WhatsApp.

## Pruebas

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar primero tu mensaje. Para ello, ve a la pestaña **Prueba** para obtener una vista previa y enviar un WhatsApp a grupos de prueba de contenido o a un usuario individual.

Esta vista previa se actualizará con la personalización pertinente y la URL acortada. 

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando se activa el borrador de Canvas.
{% endalert %}

## Informe

Cuando el seguimiento de clics está activado o se utiliza con plantillas compatibles, la tabla de rendimiento de WhatsApp incluye la columna **Clics totales**, que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas de WhatsApp, consulta [Rendimiento de los mensajes de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![Paso en Canvas de mensajes de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Los datos de los clics aparecerán automáticamente en el panel de análisis.

![Tabla de rendimiento de los mensajes de WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Reorientar usuarios 

Puedes utilizar el filtro `Clicked/Opened Step` y la interacción `clicked tracked WhatsApp link` para segmentar a los usuarios en función de sus interacciones con los enlaces.

![Filtrar grupo con un filtro para "enlace de WhatsApp de seguimiento pulsado".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include click_tracking.md section='Preguntas frecuentes' %}

### ¿Sé qué usuarios individuales hacen clic en una URL?

Sí. Cuando el seguimiento de clics está activado (o habilitado según la configuración de la plantilla), puedes reorientar a los usuarios que han hecho clic en URL aprovechando los filtros de reorientación de WhatsApp o los eventos de clic de WhatsApp (`users.messages.whatsapp.Click`) enviados por Currents.

### ¿Funciona el seguimiento de clics con vínculos profundos o universales?

El seguimiento de los clics no funciona con los vínculos en profundidad. Puedes acortar enlaces universales de proveedores como Branch o Appsflyer, pero Braze no puede solucionar los problemas que puedan surgir al hacerlo (como romper la atribución o provocar una redirección).

### ¿Las vistas previas en el dispositivo de WhatsApp cuentan como clics? 

No, no contribuyen a la tasa de clics de los mensajes de WhatsApp. 

