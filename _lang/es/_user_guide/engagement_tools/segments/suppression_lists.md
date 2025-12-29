---
nav_title: Listas de supresión
article_title: Listas de supresión
page_order: 3
page_type: reference
tool: Segments
description: "En esta página se explica cómo utilizar las listas de supresión para especificar qué usuarios no deben recibir nunca tus mensajes."

---

# Listas de supresión

> Las listas de supresión son grupos de usuarios que no reciben automáticamente ninguna campaña o Lienzo. Las listas de supresión se definen mediante filtros de segmento, y los usuarios entrarán y saldrán de las listas de supresión a medida que cumplan los criterios de filtrado. También puedes establecer etiquetas de excepción para que la lista de supresión no se aplique a campañas o Lienzos con esas etiquetas. Los mensajes de campañas o Lienzos con etiquetas de excepción seguirán llegando a los usuarios de listas de supresión que estén en los segmentos objetivo.

## ¿Por qué utilizar listas de supresión?

Las listas de supresión son dinámicas y se aplican automáticamente a todas las formas de mensajería, pero puedes establecer excepciones para las etiquetas seleccionadas. Si las etiquetas de excepción seleccionadas se utilizan en una campaña o Canvas, la lista de supresión no se aplicará a esa campaña o Canvas. Los mensajes de campañas o Lienzos con etiquetas de excepción seguirán llegando a cualquier usuario de la lista de supresión que forme parte de tus segmentos objetivo.

### Tipos de mensajes y canales afectados por las listas de supresión

Las listas de supresión se aplicarán a todos los tipos de mensajes y canales, excepto a [las banderas de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). Esto significa que las listas de supresión se aplican por predeterminado a todos los canales, campañas y Canvases, incluidos:
- [Campañas API]({{site.baseurl}}/api/api_campaigns/)
- Campañas desencadenadas por API y Lienzos
- [Correos electrónicos transaccionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

El único tipo de mensaje al que no se aplican las listas de supresión son las banderas de características. Los usuarios de una lista de supresión no serán suprimidos de los indicadores de características, pero sí de todos los demás canales. 

Puedes utilizar etiquetas de excepción para que los usuarios de la lista de supresión sigan siendo el objetivo de determinadas campañas y Canvases. Para más detalles, consulta el paso 4 de [Configurar listas de supresión](#setup). Si no añades etiquetas de excepción a una lista de supresión, los usuarios de esa lista de supresión no recibirán ningún mensaje aparte de los indicadores de características. 

{% alert note %}
Las listas de supresión se aplican a las campañas API que se crean en el panel Braze con un `campaign_id`. Las listas de supresión no se aplican a los mensajes enviados a través de [puntos finales de mensajería Braze]({{site.baseurl}}/api/endpoints/messaging/) sin un `campaign_id` asociado.
{% endalert %}

La sección "Configuración de excepciones" con una casilla de verificación para no aplicar la lista de supresión a las campañas desencadenadas por la API y a los Lienzos.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configuración de las listas de supresión {#setup}

{% alert note %}
Todos los usuarios pueden ver las listas de supresión, pero sólo los usuarios con [permisos de administrador]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) pueden crear y gestionar listas de supresión.
{% endalert %}

1. Ve a **Audiencia** > **Listas de supresión**.<br><br>\![La página "Listas de supresión" con una lista de tres listas de supresión.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Selecciona **Crear lista de supresión** y añade un nombre.<br><br>Aparece una ventana llamada "Crear una lista de supresión" con un campo para introducir un nombre.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Utiliza filtros de segmento para identificar a los usuarios de tus listas de supresión. Debes seleccionar al menos uno.

{% alert important %}
Aunque el proceso de configuración parece similar a la [creación de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), una lista de supresión es un grupo de usuarios a los que **no** quieres enviar mensajes, independientemente de su pertenencia a un segmento.
{% endalert %}

Un creador de listas de supresión con un filtro para usuarios que abrieron un correo electrónico por última vez hace más de 90 días.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Determina si quieres tener excepciones basadas en etiquetas marcando la casilla situada bajo el nombre de tu segmento (para más información, consulta [¿Por qué utilizar listas de supresión?](#why-use-suppression-lists) ), y luego añade las etiquetas de campañas o Lienzos que los usuarios de esta lista de supresión deberían seguir recibiendo. <br><br>En otras palabras, si añades la etiqueta de excepción "Confirmación de envío", los usuarios de tu lista de supresión quedarán excluidos de toda mensajería excepto de aquellos que utilicen la etiqueta "Confirmación de envío".<br><br>\![La sección "Detalles de la lista de envío" con una etiqueta de excepción aplicada llamada "Confirmación de envío".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5\. Guarda o activa tu lista de supresión.
- Cuando guardes, tu lista de supresión se guardará pero no se activará, lo que significa que no entrará en vigor. Tu lista de supresión permanecerá inactiva hasta que la actives, y las listas de supresión inactivas no afectarán a la mensajería (los usuarios no quedarán excluidos de los mensajes).
- Cuando la actives, tu lista de supresión se guardará y entrará en vigor inmediatamente, lo que significa que los usuarios de tu lista de supresión quedarán excluidos inmediatamente de las campañas o Lienzos (excepto los que contengan una etiqueta de excepción).

{% alert note %}
Sólo los administradores pueden guardar o activar listas de supresión. Puedes tener hasta cinco listas de supresión activas a la vez en la versión beta.
{% endalert %}

Puedes desactivar o archivar las listas de supresión cuando ya no las necesites. 
- Para desactivarla, selecciona una lista de supresión activa y elige **Desactivar**. Las listas de supresión desactivadas pueden reactivarse más tarde.
- Para archivar, hazlo desde la página **Listas de supresión**.

## Uso de la lista de supresión

Para comprobar si tu lista de supresión impidió que un usuario recibiera un mensaje, utiliza **la Búsqueda de usuarios** en el paso **Audiencia objetivo** dentro de tu campaña o Canvas. Aquí podrás ver de qué lista de supresión forman parte.

\!["Ventana de búsqueda de usuarios" que muestra que un usuario está en una lista de supresión.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
También puedes encontrar listas de supresión aplicadas en el paso **Resumen**.
{% endalert %}

Al crear una campaña o Canvas, utiliza **la Búsqueda de usuarios** dentro del paso en **Audiencia objetivo** para buscar a un usuario y, si no está en la audiencia objetivo, podrás ver la lista de supresión de la que forma parte. 

\!["Ventana de búsqueda de usuarios" que muestra que un usuario está en una lista de supresión.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campaña 

Si un usuario está en una lista de supresión, no recibirá una campaña para la que se aplique esa lista de supresión. Consulta [Tipos de mensajes y canales afectados por las listas](#message-types-and-channels-affected-by-suppression-lists) de supresión para ver los casos en los que no se aplicará una lista de supresión.

La sección "Listas de supresión" con una lista de supresión activa, llamada "Puntuación baja en marketing".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas 

Desde el momento en que un usuario es añadido a una lista de supresión, no entrará en Lienzos. Si ya han entrado en un Canvas, no recibirán pasos en Mensajería. Esto significa que si un usuario ya está dentro de un Canvas cuando se le añade a una lista de supresión, avanzará por el Canvas hasta el siguiente paso en Mensajería, momento en el que saldrá sin recibir el paso en Mensajería. 

Por ejemplo, supongamos que un Canvas tiene un paso de Actualización de usuario seguido de un paso de Mensaje. Si un usuario entra en el Canvas y luego es añadido a una lista de supresión, ese usuario seguirá pasando por el paso de Actualización de usuario (donde puede ser actualizado), y luego saldrá en el paso de Mensajes, momento en el que será incluido en la métrica de salida.
