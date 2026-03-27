El acortamiento de enlaces te permite acortar automáticamente las URL contenidas en mensajes SMS o RCS y recopilar análisis de tasa de click-through, proporcionando métricas de interacción adicionales para ayudar a comprender cómo los usuarios interactúan con tus campañas.

El acortamiento de enlaces se puede activar a [nivel de variante del mensaje]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) tanto en campañas como en Canvas. Cuando el acortamiento de enlaces está activado, los clics generan un [evento de clic de SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) enviado a través de Currents.

Los enlaces se acortan usando nuestro dominio corto compartido (`brz.ai`) o tu dominio personalizado de acortamiento de enlaces, y son válidos durante 9 semanas a partir de la fecha en que fueron creados. Un ejemplo de URL podría verse como `https://brz.ai/8jshX2dj`. 

## Uso del acortamiento de enlaces

Para usar el acortamiento de enlaces, asegúrate de que la casilla de acortamiento de enlaces en el creador de mensajes esté seleccionada.

{% tabs %}
{% tab SMS composer %}

![Creador de mensajes SMS con una casilla seleccionada para el acortamiento de enlaces.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![Creador de mensajes RCS con una casilla seleccionada para el acortamiento de enlaces.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze reconoce solo las URL que comienzan con `http://` o `https://`. Cuando se reconoce una URL, la sección de **vista previa** se actualiza con un marcador de posición de URL. Braze estima la longitud del mensaje después del acortamiento, pero una advertencia te solicita seleccionar un usuario de prueba y guardar el mensaje como borrador para obtener una estimación más precisa.

![Creador de mensajes con una URL larga en el cuadro "Mensaje" y un enlace acortado generado en la vista previa.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Agregar parámetros UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalización con Liquid en URLs

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

El acortamiento de enlaces también está activado para mensajes exclusivos de API a través del [punto de conexión `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Para obtener una lista completa de parámetros de solicitud, ve a [parámetros de solicitud]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Sí | Booleano | Establece `link_shortening_enabled` en `true` para activar el acortamiento de enlaces. Para usar el seguimiento, deben estar presentes un `campaign_id` y un `message_variation_id`.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Pruebas

Antes de lanzar tu campaña o Canvas, es una buena práctica previsualizar y probar tu mensaje primero. Para hacerlo, ve a la pestaña **Test** para previsualizar y enviar un mensaje SMS o RCS a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) o a un usuario individual. 

Esta vista previa se actualiza con la personalización relevante y la URL acortada. El número de caracteres y los [segmentos facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) también se actualizan para reflejar la personalización renderizada y la URL acortada.

Asegúrate de guardar la campaña o Canvas antes de enviar un mensaje de prueba para recibir una representación de la URL acortada que se envía en tu mensaje. Si la campaña o Canvas no se guarda antes de un envío de prueba, el envío de prueba incluirá un marcador de posición de URL.

{% alert important %}
Si se crea un borrador dentro de un Canvas activo, no se generará una URL acortada. La URL acortada real se genera cuando el borrador del Canvas se activa.
{% endalert %}

![Pestaña "Test" del mensaje con campos para seleccionar destinatarios de prueba.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
La personalización con Liquid y las URL acortadas se procesan en la pestaña **Test** después de que se haya seleccionado un usuario. Asegúrate de seleccionar un usuario para recibir un conteo de caracteres preciso.
{% endalert %}

## Seguimiento de clics

Cuando el acortamiento de enlaces está activado, la tabla de **rendimiento de SMS/MMS/RCS** incluye una columna titulada **Total Clicks** que muestra un conteo de eventos de clic por variante y una tasa de clics asociada. Para más detalles sobre métricas, consulta [Rendimiento de mensajes]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabla de métricas de rendimiento de SMS y MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Las tablas de **rendimiento histórico** y **rendimiento de SMS/MMS/RCS** también incluyen una opción para **Total Clicks** y muestran una serie temporal diaria de eventos de clic. Los clics se incrementan en la redirección (como cuando un usuario visita un enlace) y pueden incrementarse más de una vez por usuario.

## Reorientar usuarios

Para obtener orientación sobre la reorientación, visita [Reorientación]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### ¿Puedo saber qué usuarios individuales están haciendo clic en una URL?

Sí. Puedes reorientar a los usuarios que han hecho clic en URL usando los [filtros de reorientación de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) o los eventos de clic de SMS (`users.messages.sms.ShortLinkClick`) enviados por Currents.

### ¿Funciona el acortamiento de enlaces con vínculos profundos o enlaces universales?

El acortamiento de enlaces no funciona con vínculos profundos. Como alternativa, puedes acortar enlaces universales de proveedores externos como Branch o Appsflyer, pero los usuarios pueden experimentar una breve redirección o efecto de "parpadeo". Esto ocurre porque el enlace acortado se enruta primero a través de la web antes de resolverse al enlace universal que admite la apertura de la aplicación. Además, Braze no puede solucionar problemas que puedan surgir al acortar enlaces universales, como la interrupción de la atribución o causar redirecciones inesperadas.

{% alert note %}
Prueba la experiencia del usuario antes de implementar el acortamiento de enlaces con enlaces universales para confirmar que cumple con tus expectativas.
{% endalert %}

### ¿Los `send_ids` están asociados con los eventos de clic de SMS?

No. Sin embargo, generalmente puedes atribuir `send_ids` con eventos de clic usando [Query Builder]({{site.baseurl}}/query_builder/) para consultar datos de Currents con esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```