---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artículo de referencia describe los grupos internos, una forma excelente de obtener información sobre los registros del SDK o la API de tu dispositivo de prueba cuando se prueba la integración de SDK."

---

# Grupos internos

> Los grupos internos son una forma estupenda de crear y organizar grupos de prueba internos o externos. Proporcionan información sobre los registros de tu SDK o API y resultan útiles a la hora de probar la integración de SDK. Puedes crear un número ilimitado de grupos internos personalizados con hasta 1000 usuarios.

{% alert tip %}
También recomendamos consultar nuestro curso de Braze Learning sobre [pruebas y solución de problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que explica cómo utilizar los grupos internos para realizar tus propias tareas de solución de problemas y depuración.
{% endalert %}

## Requisitos previos

Para crear y administrar grupos internos, necesitas el [permiso heredado de Access Dev Console]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) o estos [permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions):

- Ver las claves de API
- Editar claves de API
- Ver grupos internos
- Editar grupos internos
- Ver registro de actividad de mensajes
- Ver registro de usuarios del evento
- Ver identificadores API
- Ver panel de uso de la API
- Ver límites de la API
- Ver alertas de uso de la API
- Editar alertas de uso de la API
- Editar depurador de SDK
- Ver depurador de SDK

{% multi_lang_include deprecations/user_permissions.md %}

## Creación de un grupo interno

Para crear un grupo interno: 

1. Vaya a **Configuración** > **Grupos internos**.
2. Selecciona **Crear grupo interno**.
3. Ponle un nombre a tu grupo, por ejemplo, «Grupo de prueba de correo electrónico».
4. Elige uno o varios tipos de grupo, tal y como se enumeran en la siguiente tabla.

| Tipo de grupo         | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuarios**   | Utiliza esto para verificar los eventos o registros de tu dispositivo de prueba.                                    |
| **Grupo de pruebas de contenido** | Utiliza esto en mensajes push, correos electrónicos y mensajes dentro de la aplicación para enviar una copia renderizada del mensaje. |
| **Grupo semilla**         | Envía automáticamente una copia del correo electrónico a todos los miembros del grupo semilla al enviarlo.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Un grupo interno llamado «Grupo de prueba de correo electrónico».]({% image_buster /assets/img_archive/internal_group.png %})

### Añadir usuarios de prueba

Después de crear tu grupo interno, agrega usuarios de prueba como miembros de ese grupo. 

1. En la página de administración de tu grupo interno, selecciona **Añadir usuarios de prueba**.
2. Elige entre los siguientes métodos para buscar y seleccionar a tus usuarios de prueba.

| Método                  | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Añadir usuario identificado** | Busca al usuario por su ID de usuario externo, dirección de correo electrónico, número de teléfono o token de notificaciones push.                                                                                                                                                           |
| **Añadir usuario anónimo**  | Busca por dirección IP. A continuación, asigna un nombre a cada usuario de prueba que añadas. Este es el nombre con el que se asocian todos los registros de eventos en la página [Registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Añadir usuarios en bloque**      | Copia y pega una lista de direcciones de correo electrónico o ID externos. Solo puedes añadir usuarios que ya estén registrados en el panel. Para obtener más información, consulta [Importación]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/) de [usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configuración interna del grupo al crear un nuevo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de pruebas de contenido

De forma similar al envío de una vista previa de un mensaje, el grupo de pruebas de contenido te permite ahorrar tiempo y lanzar pruebas simultáneamente a una lista predefinida de usuarios de Braze. Está disponible para notificaciones push, mensajes dentro de la aplicación, SMS, correo electrónico y tarjetas de contenido en Braze. Solo los grupos etiquetados como «Grupos de prueba de contenido» están disponibles en la sección de vista previa de un mensaje.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

Selecciona usuarios individuales de Braze o cualquier número de grupos internos a los que enviar el mensaje. Si tu mensaje incluye cualquier personalización dinámica o Liquid, Braze utiliza los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tienen atributos, Braze utiliza el valor predeterminado establecido.

Además, si realizas una vista previa del mensaje como un usuario aleatorio, un usuario personalizado o un usuario existente, puedes enviar esa versión de vista previa en su lugar. Al desmarcar la casilla, podrás enviar el correo basándote en los atributos de cada usuario en lugar de en la vista previa.

Si utilizas un grupo de direcciones IP para enviar un correo electrónico, selecciona desde qué grupo de direcciones IP deseas enviar el correo electrónico seleccionando el grupo en el menú desplegable disponible.

![La sección Prueba del editor de mensajes dentro de la aplicación para seleccionar el Grupo de prueba de contenido.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos semilla

Los grupos semillas solo son compatibles con el canal de correo electrónico. Añadid usuarios a un grupo semilla para enviar copias de cada variante de mensaje de correo electrónico a todos los miembros del grupo.

Los grupos semilla no están disponibles para las campañas API, pero puedes incluirlos utilizando una entrada activada por API en la campaña. Utiliza esto para medir las métricas de capacidad de entrega y mantener un registro del contenido de tus correos electrónicos con fines históricos y de archivo. 

Después de crear un grupo interno y etiquetarlo para utilizarlo como grupo semilla, selecciónalo en el paso **«Audiencias objetivo**» del editor de campañas o en el paso **«Configuración de envío»** en un Canvas. 

Los correos electrónicos de semillas tendrán`[SEED]`  añadido al principio de la línea del asunto del correo electrónico. Ten en cuenta que los correos electrónicos semilla **no**:

- Increment envía los análisis al panel de control.
- Análisis de impacto del correo electrónico o retargeting. 
- Actualiza la lista **de campañas recibidas** del perfil de usuario.
- Limitación de frecuencia de impacto.
- Ten en cuenta o influye en los límites de velocidad de entrega.

#### Comportamiento de suscripción

Los envíos de semillas están diseñados para el control de calidad interno y la revisión, por lo que omiten intencionadamente las comprobaciones de suscripción para los usuarios de la empresa destinataria. Esto significa que los usuarios con direcciones de correo electrónico válidas que forman parte de un grupo semilla reciben el mensaje aunque no estén suscritos. Sin embargo, el mensaje debe configurarse para enviar copias iniciales a ese grupo.

{% alert tip %}
Si los miembros de tu grupo semilla informan que no ven el mensaje en su buzón de entrada, comprueba que figuran en el grupo interno, verifica que las líneas del asunto sean diferentes y que Gmail no haya agrupado los correos electrónicos, o pídeles que revisen sus carpetas de correo no deseado.
{% endalert %}

#### Para las campañas

Al redactar una campaña de envío por correo electrónico, edita tus grupos semilla en la sección **«Audiencias objetivo»** del editor.

{% alert important %}
Si configuras un grupo semilla para que se adjunte automáticamente a todas las campañas, solo se aplicará a las campañas nuevas. No se aplica cuando copias campañas existentes. Debes aplicar manualmente los grupos semillas que desees a la campaña copiada en la sección **«Audiencias objetivo**».
{% endalert %}

Los Grupos Semilla se envían una vez a cada variante de correo electrónico y se entregan la primera vez que el usuario recibe esa variante concreta. En el caso de los mensajes programados, suele ser la primera vez que se lanza la campaña. En el caso de las campañas basadas en acciones o activadas por API, este es el momento en el que se envía un mensaje al primer usuario.

Si tu campaña es multivariante y tu variante tiene un porcentaje de envío del 0 %, no se envía a los grupos semilla. Además, si la variante ya se ha enviado y no se ha actualizado para volver a enviarla en **Editar grupos semilla** en el paso **Destino**, no se vuelve a enviar de forma predeterminada.

{% alert note %}
Si tienes una campaña recurrente y se actualiza alguna de las variantes, puedes elegir entre volver a enviarla solo a las variantes actualizadas o a todas las variantes, o desactivar el envío del grupo semilla tras la actualización.
{% endalert %}

![El grupo semilla «Prueba de semillas de correo electrónico» seleccionado para recibir la campaña de correo electrónico de la variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para lienzo

Los grupos semillas en Canvas funcionan de manera similar a cualquier campaña desencadenada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los envía cuando el usuario llega por primera vez a ese paso concreto.

Si se ha actualizado un paso de correo electrónico después de enviar el grupo semilla, Braze ofrece la opción de enviar solo a los pasos actualizados, a todos los pasos o desactivar las semillas.