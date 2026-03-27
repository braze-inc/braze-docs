El acortamiento de enlaces y el seguimiento de clics te permiten acortar automáticamente las URL contenidas en mensajes SMS o RCS y recopilar análisis de tasa de click-through, proporcionando métricas de interacción adicionales para ayudarte a comprender cómo los usuarios interactúan con tus campañas.

El acortamiento de enlaces y el seguimiento de clics se pueden activar a [nivel de variante del mensaje]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) tanto en campañas como en Canvas. 

La longitud de la URL está determinada por el tipo de seguimiento que se active:
- **Seguimiento básico** habilita el seguimiento de clics a nivel de campaña. Las URL estáticas tendrán una longitud de 20 caracteres, y las URL personalizadas tendrán una longitud de 25 caracteres.
- **Seguimiento avanzado** habilita el seguimiento de clics a nivel de campaña y a nivel de usuario, y permite el uso de capacidades de segmentación y reorientación que dependen de los clics. Los clics también generarán un [evento de clic de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado a través de Currents. Las URL estáticas con seguimiento avanzado tendrán una longitud de 27-28 caracteres, lo que te permite crear segmentos de usuarios que han hecho clic en las URL. Las URL personalizadas tendrán una longitud de 32-33 caracteres.

Los enlaces se acortan usando nuestro dominio corto compartido (`brz.ai`) o tu dominio personalizado de acortamiento de enlaces. Un ejemplo de URL podría verse así: `https://brz.ai/8jshX` (básico, estático) o `https://brz.ai/p/8jshX/2dj8d` (avanzado, personalizado). Consulta [Pruebas](#testing) para más información.

Cualquier URL estática que comience con `http://` o `https://` se acorta. Las URL estáticas acortadas son válidas durante un año a partir de la fecha en que fueron creadas. Las URL acortadas que contienen personalización con Liquid son válidas durante dos meses.

{% alert note %}
Si planeas usar el [filtro de canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) de BrazeAI<sup>TM</sup> y quieres que los canales SMS y RCS sean seleccionables, activa el acortamiento de enlaces con seguimiento avanzado.
{% endalert %}

## Uso del acortamiento de enlaces

Para usar el acortamiento de enlaces, asegúrate de que el interruptor de acortamiento de enlaces en el creador de mensajes esté activado. Luego, elige usar seguimiento básico o avanzado.

![Creador de mensajes con un interruptor para el acortamiento de enlaces.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Braze solo reconoce URL que comiencen con `http://` o `https://`. Cuando se reconoce una URL, la sección de **vista previa** se actualiza con un marcador de posición de URL. Braze estima la longitud de la URL después del acortamiento, pero una advertencia te solicita seleccionar un usuario de prueba y guardar el mensaje como borrador para obtener una estimación más precisa.

![Creador de mensajes con una URL larga en el cuadro "Mensaje" y un enlace acortado generado en la vista previa.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

### Agregar parámetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalización con Liquid en las URL

Puedes construir dinámicamente tu URL directamente dentro del compositor de Braze, lo que te permite agregar parámetros UTM dinámicos a tus URL o enviar a los usuarios enlaces únicos (como dirigir a los usuarios a su carrito abandonado o a un producto específico que volvió a estar disponible).

### Crear una URL con etiquetas de personalización de Liquid compatibles

Las URL se pueden generar dinámicamente mediante el uso de cualquier [etiqueta de personalización de Liquid compatible]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

También admitimos el acortamiento de variables Liquid definidas de forma personalizada. A continuación se muestran varios ejemplos:

### Crear una URL usando variables Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Acortar URL renderizadas por variables Liquid

Acortamos las URL que son renderizadas por Liquid, incluso aquellas incluidas en propiedades de activación por API. Por ejemplo, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa una URL válida, acortamos y hacemos seguimiento de esa URL antes de enviar el mensaje. 

### Acortar URL en el punto de conexión `/messages/send`

El acortamiento de enlaces también está activado para mensajes exclusivos de API a través del [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para activar también el seguimiento básico o avanzado, usa los parámetros de solicitud `link_shortening_enabled` o `user_click_tracking_enabled`.

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Opcional | Booleano | Establece `link_shortening_enabled` en `true` para activar el acortamiento de enlaces y el seguimiento de clics a nivel de campaña. Para usar el seguimiento, deben estar presentes un `campaign_id` y un `message_variation_id`.|
|`user_click_tracking_enabled`| Opcional | Booleano | Establece `user_click_tracking_enabled` en `true` para activar el acortamiento de enlaces, y el seguimiento de clics a nivel de campaña y a nivel de usuario. Puedes usar los datos rastreados para crear segmentos de usuarios que hicieron clic en las URL.<br><br> Para usar este parámetro, `link_shortening_enabled` debe ser `true`, y deben estar presentes un `campaign_id` y un `message_variation_id`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para obtener una lista completa de los parámetros de solicitud, ve a [parámetros de solicitud]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Pruebas

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Prueba** para previsualizar y enviar un mensaje SMS o RCS a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) o a un usuario individual. 

Esta vista previa se actualiza con la personalización relevante y la URL acortada. El número de caracteres y los [segmentos facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) también se actualizan para reflejar la personalización renderizada y la URL acortada.

Asegúrate de guardar la campaña o Canvas antes de enviar un mensaje de prueba para recibir una representación de la URL acortada que se envía en tu mensaje. Si la campaña o Canvas no se guarda antes de un envío de prueba, el envío de prueba incluirá un marcador de posición de URL.

Para que los Canvas aparezcan en el filtro "Hizo clic en enlace SMS acortado", el paso en Canvas que contiene el enlace corto también debe estar habilitado con seguimiento avanzado, lo que permite el seguimiento de clics a nivel de usuario. Si el enlace corto está configurado con seguimiento básico, la opción de filtrar eventos de clic en enlaces SMS cortos no está disponible.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

![Pestaña "Prueba" del mensaje con campos para seleccionar destinatarios de prueba.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
La personalización con Liquid y las URL acortadas se procesan en la pestaña **Prueba** después de que se haya seleccionado un usuario. Asegúrate de seleccionar un usuario para recibir un conteo de caracteres preciso.
{% endalert %}

## Seguimiento de clics

Cuando el acortamiento de enlaces está activado, la tabla de **rendimiento de SMS/MMS/RCS** incluye una columna titulada **Clics totales** que muestra un conteo de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre las métricas, consulta [Rendimiento de mensajes]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabla de métricas de rendimiento de SMS y MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Las tablas de **rendimiento histórico** y **rendimiento de SMS/MMS/RCS** también incluyen una opción para **Clics totales** y muestran una serie temporal diaria de eventos de clic. Los clics se incrementan en la redirección (como cuando un usuario visita un enlace), y pueden incrementarse más de una vez por usuario.

## Reorientación de usuarios

Para obtener orientación sobre la reorientación, visita [Reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Puedo saber qué usuarios individuales están haciendo clic en una URL?

Sí. Cuando el **seguimiento avanzado** está activado, puedes reorientar a los usuarios que han hecho clic en las URL aprovechando los [filtros de reorientación de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) o los eventos de clic de SMS (`users.messages.sms.ShortLinkClick`) enviados por Currents.

### ¿Funciona el acortamiento de enlaces con vínculos profundos o enlaces universales?

El acortamiento de enlaces no funciona con vínculos profundos. Como alternativa, puedes acortar enlaces universales de proveedores externos como Branch o Appsflyer, pero los usuarios pueden experimentar una breve redirección o efecto de "parpadeo". Esto ocurre porque el enlace acortado se enruta primero a través de la web antes de resolverse al enlace universal que admite la apertura de la aplicación. Además, Braze no puede solucionar problemas que puedan surgir al acortar enlaces universales, como romper la atribución o causar redirecciones inesperadas.

{% alert note %}
Prueba la experiencia del usuario antes de implementar el acortamiento de enlaces con enlaces universales para confirmar que cumple con tus expectativas.
{% endalert %}

### ¿Los `send_ids` están asociados con los eventos de clic de SMS?

No. Sin embargo, si tienes el seguimiento avanzado habilitado, generalmente puedes atribuir `send_ids` con eventos de clic usando el [Generador de consultas]({{site.baseurl}}/query_builder/) para consultar datos de Currents con esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```