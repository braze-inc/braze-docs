---
nav_title: Acortamiento de enlaces
article_title: Acortamiento de enlaces
page_order: 3
description: "Este artículo de referencia explica cómo activar el acortamiento de enlaces en tus mensajes SMS y algunas preguntas frecuentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Acortamiento de enlaces

> Esta página explica cómo activar el acortamiento de enlaces en tus mensajes SMS y RCS, probar los enlaces acortados, utilizar tu dominio personalizado en los enlaces acortados y mucho más.

El acortamiento de enlaces y el seguimiento de clics te permiten acortar automáticamente las URL contenidas en los mensajes SMS o RCS y recopilar análisis de la tasa de click-through, proporcionando métricas de interacción adicionales para ayudar a comprender cómo interactúan tus usuarios con tus campañas.

El acortamiento de enlaces y el seguimiento de clics pueden activarse [a nivel de variante de mensaje]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign), tanto en campañas como en Lienzos. 

La longitud de la URL viene determinada por el tipo de seguimiento activado:
- **El seguimiento básico** permite realizar un seguimiento de los clics a nivel de campaña. Las URL estáticas tendrán una longitud de 20 caracteres, y las URL personalizadas tendrán una longitud de 25 caracteres.
- **El seguimiento avanzado** habilita el seguimiento de los clics a nivel de campaña y a nivel de usuario, y permite utilizar las funciones de segmentación y reorientación que se basan en los clics. Los clics también generarán un [evento de clic SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado a través de Currents. Las URL estáticas con seguimiento avanzado tendrán una longitud de 27-28 caracteres, lo que te permitirá crear segmentos de usuarios que hayan hecho clic en las URL. Las URL personalizadas tendrán una longitud de 32-33 caracteres.

Los enlaces se acortan utilizando nuestro dominio corto compartido (`brz.ai`). Un ejemplo de URL puede ser algo así: `https://brz.ai/8jshX` (básico, estático) o `https://brz.ai/p/8jshX/2dj8d` (avanzado, personalizado). Consulte la sección [Pruebas](#testing) para obtener más información.

Cualquier URL estática que empiece por `http://` o `https://` se acorta. Las URL acortadas estáticas son válidas durante un año a partir de la fecha en que se crearon. Las URL acortadas que contienen personalización Liquid son válidas durante dos meses.

{% alert note %}
Si piensas utilizar el [filtro de canales inteligentes]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) <sup>BrazeAITM</sup> y quieres que los canales SMS y RCS sean seleccionables, activa el acortamiento de enlaces con seguimiento avanzado.
{% endalert %}

## Utilizar el acortamiento de enlaces

Para utilizar el acortamiento de enlaces, asegúrate de que está activado el alternador de acortamiento de enlaces en el creador de mensajes. A continuación, elige utilizar el seguimiento básico o el avanzado.

![Creador de mensajes con un botón alternativo para acortar enlaces.]({% image_buster /assets/img/link_shortening/shortening1.png %})

Braze sólo reconoce las URL que empiezan por `http://` o `https://`. Cuando se reconoce una URL, la sección **Vista previa** se actualiza con una URL de marcador de posición. Braze estima la longitud de la URL después de acortarla, pero una advertencia te pide que selecciones un usuario de prueba y guardes el mensaje como borrador para obtener una estimación más precisa.

![Creador de mensajes con una URL larga en la casilla "Mensaje" y un enlace acortado generado en la vista previa.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Añadir parámetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalización líquida en las URL

Puede construir dinámicamente su URL directamente dentro del compositor Braze, lo que le permite añadir parámetros UTM dinámicos a sus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que vuelve a estar en stock).

### Crear una URL con etiquetas de personalización de Liquid compatibles

Las URL pueden generarse dinámicamente mediante el uso de cualquiera de las [etiquetas de personalización de Liquid admitidas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos el acortamiento de variables Liquid definidas a medida. A continuación se muestran varios ejemplos:

### Crear una URL utilizando variables Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Acortar las URL generadas por las variables de Liquid

Acortamos las URL generadas por Liquid, incluso las incluidas en las propiedades de activación de API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortamos y hacemos un seguimiento de esa URL antes de enviar el mensaje. 

### Acortar URLs en `/messages/send` endpoint

El acortamiento de enlaces también está activado para los mensajes exclusivos de la API a través del [punto final`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para activar también el seguimiento básico o avanzado, utiliza los parámetros de solicitud `link_shortening_enabled` o `user_click_tracking_enabled`.

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | Booleano | Establezca `link_shortening_enabled` en `true` para activar el acortamiento de enlaces y el seguimiento de clics a nivel de campaña. Para utilizar el seguimiento, deben estar presentes `campaign_id` y `message_variation_id`.|
|`user_click_tracking_enabled`| Opcional | Booleano | Establezca `user_click_tracking_enabled` en `true` para activar el acortamiento de enlaces y el seguimiento de clics a nivel de campaña y a nivel de usuario. Puede utilizar los datos rastreados para crear segmentos de usuarios que hicieron clic en las URL.<br><br> Para utilizar este parámetro, `link_shortening_enabled` debe ser `true`, y deben estar presentes `campaign_id` y `message_variation_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para obtener una lista completa de los parámetros de solicitud, ve a [Parámetros de solicitud]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Pruebas

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar primero tu mensaje. Para ello, ve a la pestaña **Prueba** para obtener una vista previa y enviar un mensaje SMS o RCS a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) o a un usuario individual. 

Esta vista previa se actualiza con la personalización pertinente y la URL acortada. El número de caracteres y los [segmentos facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) también se actualizan para reflejar la personalización renderizada y la URL acortada.

Asegúrate de guardar la campaña o Canvas antes de enviar un mensaje de prueba para recibir una representación de la URL acortada que se envía en tu mensaje. Si la campaña o el Canvas no se guardan antes de un envío de prueba, el envío de prueba incluye una URL de marcador de posición.

Para que los Canvas aparezcan en el filtro "Enlace SMS acortado en el que se ha hecho clic", el paso en Canvas que contiene el enlace corto también debe estar habilitado con el seguimiento avanzado, que permite el seguimiento de los clics a nivel de usuario. Si el enlace corto está configurado con un seguimiento básico, la opción de filtrar los eventos de clic del enlace corto SMS no está disponible.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando se activa el borrador de Canvas.
{% endalert %}

![Pestaña "Prueba" de mensajes con campos para seleccionar destinatarios de prueba.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
La personalización líquida y las URL acortadas se planifican en la pestaña **Prueba** después de seleccionar un usuario. Asegúrese de que se selecciona un usuario para recibir un recuento preciso de caracteres.
{% endalert %}

## Seguimiento de clics

Cuando el acortamiento de enlaces está activado, la tabla **Rendimiento de SMS/MMS/RCS** incluye una columna titulada **Clics totales** que muestra un recuento de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas, consulta [Rendimiento de los mensajes]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabla de métricas de rendimiento de SMS y MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Las tablas de **Rendimiento histórico** y **Rendimiento de SMS/MMS/RCS** también incluyen una opción para **Clics totales** y muestran una serie temporal diaria de eventos de clic. Los clics se incrementan en la redirección (como cuando un usuario visita un enlace), y pueden incrementarse más de una vez por usuario.

## Reorientar usuarios

Para obtener orientación sobre reorientación, visita [Reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Sé qué usuarios individuales hacen clic en una URL?

Sí. Cuando **el seguimiento avanzado** está activado, puedes reorientar a los usuarios que han hecho clic en las URL aprovechando los [filtros de reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) por SMS o los eventos de clic por SMS (`users.messages.sms.ShortLinkClick`) enviados por Currents.

{% alert note %}
En este momento, los eventos de clic de RCS no están disponibles a través de Currents.
{% endalert %}

### ¿Funciona el acortamiento de enlaces con enlaces profundos o universales?

El acortamiento de enlaces no funciona con los vínculos profundos. Como alternativa, puedes acortar enlaces universales de proveedores externos como Branch o Appsflyer, pero los usuarios pueden experimentar una breve redirección o un efecto de "parpadeo". Esto ocurre porque el enlace acortado pasa primero por la Web antes de resolverse en el enlace universal que admite la apertura de la aplicación. Además, Braze no puede solucionar los problemas que pueden surgir al acortar enlaces universales, como romper la atribución o provocar redireccionamientos inesperados.

{% alert note %}
Prueba la experiencia del usuario antes de implantar el acortamiento de enlaces con enlaces universales para confirmar que cumple tus expectativas.
{% endalert %}

### ¿Están `send_ids` asociados a eventos de clic de SMS?

No. Sin embargo, si tienes habilitado el seguimiento avanzado, en general puedes atribuir `send_ids` con eventos de clic utilizando [el Generador de consultas]({{site.baseurl}}/query_builder/) para consultar los datos de Currents con esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
