---
nav_title: Listas de supresión
article_title: Listas de supresión
page_order: 2.5
page_type: reference
tool: Segments
description: "En esta página se explica cómo utilizar las listas de supresión para especificar qué usuarios no deben recibir nunca tus mensajes."

---

# Listas de supresión

> Las listas de supresión especifican grupos de usuarios que nunca recibirán mensajes. Los administradores pueden crear listas de supresión dinámicas con filtros de segmento para acotar un grupo de usuarios del mismo modo que lo harías para la segmentación.

{% alert important %}
Las listas de supresión están actualmente en fase beta. Si te interesa formar parte de esta versión beta, ponte en contacto con tu administrador del éxito del cliente. Durante la versión beta, la funcionalidad puede cambiar, y puedes tener hasta cinco listas de supresión activas a la vez, pero informa a tu administrador del éxito del cliente si necesitas más.
{% endalert %}

## Cómo funciona

Las listas de supresión son dinámicas y se aplican automáticamente a determinadas formas de mensajería, pero puedes establecer excepciones para las etiquetas seleccionadas. Si las etiquetas de excepción seleccionadas se utilizan en una campaña o Canvas, la lista de supresión no se aplicará a esa campaña o Canvas. Los mensajes de campañas o Lienzos con etiquetas de excepción seguirán llegando a cualquier usuario de la lista de supresión que forme parte de tus segmentos objetivo.

### Mensajes no afectados por las listas de supresión

Como parte de la versión beta, las listas de supresión no se aplicarán a los siguientes tipos de mensajes (en otras palabras, los usuarios de las listas de supresión **seguirán** recibiendo mensajes que pertenezcan a los siguientes):
- Conmutador de características
- Casos de uso transaccional
- Campañas API
- Campañas activadas por API
- Lienzos desencadenados por API
- Campañas desencadenadas por la API Braze (`/messages` y `/send`)

No necesitas añadir una etiqueta de excepción para ninguno de estos casos de uso, ya que las listas de supresión no se les aplicarán automáticamente. Para excluir a un grupo de usuarios de un mensaje dentro de estos casos de uso, tienes que crear un segmento objetivo que excluya a estos usuarios.

{% alert important %}
Durante la versión beta, recogemos las opiniones de los clientes para ayudar a mejorar nuestro producto. Informa a tu administrador del éxito del cliente si piensas aplicar listas de supresión a casos de uso transaccional.
{% endalert %}

### Canales afectados por las listas de supresión

Las listas de supresión son dinámicas y se aplicarán automáticamente a todos los canales siguientes (a menos que la campaña o el Canvas contengan una etiqueta de excepción): 
- SMS
- Correo electrónico
- Push
- Mensajes dentro de la aplicación
- Tarjeta de contenido
- Banner
- SMS/MMS
- Webhook
- WhatsApp
- LINE

## Configuración de las listas de supresión

Dado que las listas de supresión pueden afectar significativamente a los mensajes que envías, sólo los administradores pueden editar, guardar, activar y desactivar las listas de supresión (todos los usuarios pueden ver las listas de supresión).

1. Ve a **Audiencia** > **Listas de supresión**.<br><br>![La página "Listas de supresión" con una lista de tres listas de supresión.][1]<br><br>
2. Selecciona **Crear lista de supresión** y añade un nombre.<br><br>![Una ventana llamada "Crear una lista de supresión" con un campo para introducir un nombre.][2]{: style="max-width:80%;"}<br><br>
3. Utiliza filtros de segmento para identificar a los usuarios de tus listas de supresión. Debes seleccionar al menos uno.

{% alert important %}
Aunque el proceso de configuración parece similar a la [creación de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), una lista de supresión es un grupo de usuarios a los que **no** quieres enviar mensajes, independientemente de su pertenencia a un segmento.
{% endalert %}

![Un creador de listas de supresión con un filtro para usuarios que abrieron un correo electrónico por última vez hace más de 90 días.][3]

{: start="4"}
4\. Determina si quieres tener excepciones basadas en etiquetas marcando la casilla situada bajo el nombre de tu segmento (consulta [Cómo funciona](#how-it-works) para obtener más información), y luego añade las etiquetas de campañas o Lienzos que los usuarios de esta lista de supresión deben seguir recibiendo. <br><br>En otras palabras, si añades la etiqueta de excepción "Confirmación de envío", los usuarios de tu lista de supresión quedarán excluidos de toda mensajería excepto de aquellos que utilicen la etiqueta "Confirmación de envío".<br><br>![La sección "Detalles de la lista de envío" con una etiqueta de excepción aplicada llamada "Confirmación de envío".][4]<br><br>
5\. Guarda o activa tu lista de supresión.
- Cuando guardes, tu lista de supresión se guardará pero no se activará, lo que significa que no entrará en vigor. Tu lista de supresión permanecerá inactiva hasta que la actives, y las listas de supresión inactivas no afectarán a la mensajería (los usuarios no quedarán excluidos de los mensajes).
- Cuando la actives, tu lista de supresión se guardará y entrará en vigor inmediatamente, lo que significa que los usuarios de tu lista de supresión quedarán excluidos inmediatamente de las campañas o Lienzos (excepto los que contengan una etiqueta de excepción).

{% alert note %}
Sólo los administradores pueden guardar o activar listas de supresión. Puedes tener hasta cinco listas de supresión activas a la vez en la versión beta.
{% endalert %}

Puedes desactivar o archivar las listas de supresión cuando ya no las necesites. 
- Para desactivarla, selecciona una lista de supresión activa y elige **Desactivar**. Las listas de supresión desactivadas pueden reactivarse más tarde.
- Para archivar, hazlo desde la página **Listas de Supresión**.

## Uso de la lista de supresión

### Para las campañas

![La sección "Listas de supresión" con una lista de supresión activa, llamada "Puntuación baja en marketing".][5]

Si un usuario está en una lista de supresión, no recibirá una campaña para la que se aplique esa lista de supresión. Consulta [Mensajes no afectados por listas](#messages-not-affected-by-suppression-lists) de supresión para ver los casos en los que no se aplicará una lista de supresión.

#### Comprobar qué listas de supresión se aplican

Para comprobar el uso de listas de supresión en una campaña, ve a la sección **Lista de supresión** de la página **Audiencia objetivo** para ver qué listas de supresión se están aplicando a esa campaña.

### Para lienzos

Si un usuario está en una lista de supresión, seguirá entrando en el Canvas pero no podrá recibir pasos en Canvas. Cuando avancen a un paso en Mensaje, saldrán del Canvas. Sin embargo, un usuario de una lista de supresión puede seguir recibiendo pasos que no sean de Mensaje antes de un paso de Mensajería. 

#### Evitar que los segmentos entren en un Canvas

Para que un segmento no se introduzca en **absoluto** en un Canvas, puedes configurar los ajustes de Objetivo de ese Canvas para excluir ese segmento siguiendo estos pasos:

1. Construye un segmento utilizando los mismos filtros y criterios que tu lista de supresión.
2. En el paso **Destino**, utiliza el filtro **Pertenencia al segmento** para dirigirte a los usuarios que no están incluidos en tu segmento.

Por ejemplo, supongamos que tienes un Canvas con una lista de supresión aplicada. El Canvas tiene un paso de Actualización de Usuario seguido de un paso de Mensaje. En este escenario, los usuarios de la lista de supresión entrarán en el Canvas, pasarán por el paso de Actualización de usuario (donde el usuario puede ser actualizado, en función de cómo esté configurado ese paso), y luego saldrán en el paso de Mensaje (momento en el que el usuario se incluirá en la métrica "Salido"). 

#### Comprobar qué listas de supresión se aplican

Para comprobar el uso de listas de supresión en un Canvas, ve a la sección **Lista de supresión** de la página **Audiencia objetivo** para ver qué listas de supresión se están aplicando a ese Canvas. También puedes ver las listas de supresión aplicadas en el paso **Resumen**.

[1]: {% image_buster /assets/img/suppression_lists_home.png %}
[2]: {% image_buster /assets/img/create_suppression_list.png %}
[3]: {% image_buster /assets/img/suppression_list_filters.png %}
[4]: {% image_buster /assets/img/exception_tags.png %}
[5]: {% image_buster /assets/img/active_suppression_list.png %}
