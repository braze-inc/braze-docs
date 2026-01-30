---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artículo de referencia describe los grupos internos, una forma estupenda de obtener información sobre los registros del SDK o de la API de tu dispositivo de prueba al probar la integración de SDK."

---

# Grupos internos

> Los grupos internos son una forma estupenda de crear y organizar grupos de prueba internos o de terceros. Proporcionan información sobre los registros de tu SDK o API y son útiles para probar tu integración de SDK. Puedes crear un número ilimitado de grupos internos personalizados con hasta 1.000 usuarios.

{% alert tip %}
También te recomendamos que eches un vistazo a nuestro curso de Braze Learning [Pruebas y solución de problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que explica cómo utilizar grupos internos para llevar a cabo tu propia solución de problemas y depuración.
{% endalert %}

## Requisitos previos

Para crear y administrar grupos internos, necesitas el [permiso Consola Dev Acceso]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) para tu espacio de trabajo.

## Crear un grupo interno

Para crear un grupo interno: 

1. Vaya a **Configuración** > **Grupos internos**.
2. Selecciona **Crear grupo interno**.
3. Dale un nombre a tu grupo, como "Grupo de prueba de correo electrónico".
4. Elige uno o varios tipos de grupo, como se indica en la tabla siguiente.

| Tipo de grupo         | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuarios**   | Utilízalo para verificar los eventos o registros de tu dispositivo de prueba.                                    |
| **Grupo de pruebas de contenido** | Utilízalo en mensajes push, correo electrónico y mensajes dentro de la aplicación para enviar una copia renderizada del mensaje. |
| **Grupo semilla**         | Envía automáticamente una copia del correo electrónico a todos los miembros del grupo semilla al enviarlo.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Un grupo interno llamado "Grupo de prueba de correo electrónico".]({% image_buster /assets/img_archive/internal_group.png %})

### Añadir usuarios de prueba

Después de crear tu grupo interno, añade usuarios de prueba como miembros de ese grupo. 

1. En la página de administración de tu grupo interno, selecciona **Añadir usuarios de prueba**.
2. Elige uno de los siguientes métodos para buscar y seleccionar a tus usuarios de prueba.

| Método                  | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Añadir usuario identificado** | Busca al usuario por su ID externo, dirección de correo electrónico, número de teléfono o token de notificaciones push.                                                                                                                                                           |
| **Añadir usuario anónimo**  | Busca por dirección IP. A continuación, proporciona un nombre para cada usuario de prueba que añadas. Este es el nombre con el que se asocian todos los registros de usuarios del evento en la página [Registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Añadir usuarios en bloque**      | Copia y pega una lista de direcciones de correo electrónico o ID externos. Sólo puedes añadir usuarios ya conocidos en el panel. Para más información, consulta [Importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configuración del grupo interno al crear un nuevo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de pruebas de contenido

Similar al envío de una vista previa de prueba de un mensaje, el Grupo de Prueba de Contenido te ahorra tiempo y te permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente. Está disponible para push, mensajes dentro de la aplicación, SMS, correo electrónico y tarjetas de contenido en Braze. Sólo los grupos etiquetados como Grupos de prueba de contenido están disponibles en la vista previa de un mensaje.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

Selecciona usuarios individuales de Braze o cualquier número de grupos internos a los que enviar el mensaje. Si tu mensaje incluye Liquid u otra personalización dinámica, Braze utiliza los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tienen atributos, Braze utiliza el conjunto de valores predeterminado.

Además, si previsualizas el mensaje como un usuario aleatorio, un usuario personalizado o un usuario existente, puedes enviar esa versión previsualizada en su lugar. Desmarcando la casilla de verificación, puedes enviar en función de los atributos de cada usuario frente a la versión previsualizada.

Si utilizas un conjunto de IP para enviar un correo electrónico, selecciona desde qué conjunto de IP enviar el correo electrónico seleccionando el conjunto en el desplegable disponible.

![La sección Prueba del editor de mensajes dentro de la aplicación para seleccionar el Grupo de prueba de contenido.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos semilla

Los grupos semilla sólo son compatibles con el canal de correo electrónico. Añade usuarios a un grupo semilla para enviar copias de cada mensaje de variante de correo electrónico a todos los miembros del grupo.

Los Grupos semilla no están disponibles para las campañas API, pero puedes incluir Grupos semilla utilizando una entrada desencadenada por la API en la campaña. Utilízalo para medir las métricas de capacidad de entrega y para mantener un registro del contenido de tu correo electrónico con fines históricos y de archivo. 

Tras crear un grupo interno y etiquetarlo para utilizarlo como grupo semilla, selecciónalo en el paso **Audiencias** objetivo del editor de campaña, o en el paso **Configuración de envío** de un Canvas. 

Los correos electrónicos con semillas tendrán `[SEED]` añadido al principio de la línea del asunto del correo electrónico. Ten en cuenta que los envíos por correo electrónico **no lo hacen**:

- Incrementa los envíos en el panel de análisis.
- Impacta el análisis del correo electrónico o la reorientación. 
- Actualiza la lista de **campañas recibidas** de un perfil de usuario.
- Limitación de frecuencia de impacto.
- Contabiliza o influye en los límites de tasa de velocidad de entrega.

#### Comportamiento de suscripción

Los envíos semilla están diseñados para el control de calidad y la revisión internos, por lo que omiten intencionadamente las comprobaciones de suscripción de los usuarios del panel sembrado. Esto significa que los usuarios con direcciones de correo electrónico válidas que forman parte de un grupo semilla reciben el mensaje aunque no estén suscritos. Sin embargo, el mensaje debe estar configurado para enviar copias de semillas a ese grupo.

{% alert tip %}
Si los miembros de tu grupo semilla dicen que no ven el mensaje en su buzón de entrada, comprueba que están incluidos en el grupo interno, verifica que las líneas del asunto son diferentes y que Gmail no ha agrupado los mensajes, o pídeles que comprueben sus carpetas de correo no deseado.
{% endalert %}

#### Para las campañas

Al componer una campaña de correo electrónico, edita tus grupos semilla en la sección **Audiencias objetivo** del editor.

{% alert important %}
Si configuras un Grupo semilla para que se adjunte automáticamente a todas las campañas, sólo se aplicará a las campañas nuevas. No se aplica cuando copias campañas existentes. Debes aplicar manualmente los grupos semilla que desees a la campaña copiada en la sección **Audiencias objetivo**.
{% endalert %}

Los Grupos Semilla se envían una vez a cada variante de correo electrónico y se entregan la primera vez que el usuario recibe esa variante concreta. En el caso de los mensajes programados, suele ser la primera vez que se lanza la campaña. En las campañas basadas en acciones o desencadenadas por API, éste es el momento en que se envía un mensaje al primer usuario.

Si tu campaña es multivariante y tu variante tiene un porcentaje de envío del 0%, no se envía a los grupos semilla. Además, si la variante ya se ha enviado y no se ha actualizado para reenviarla en **Editar grupos semilla** en el paso **Destino**, no se vuelve a enviar por predeterminado.

{% alert note %}
Si tienes una campaña recurrente y se actualiza alguna de las variantes, puedes elegir enviar de nuevo sólo a las variantes actualizadas o a todas las variantes, o desactivar el envío de Grupo semilla al actualizarse.
{% endalert %}

![El Grupo semilla "Prueba de correo electrónico" seleccionado para que se le envíe la campaña de correo electrónico Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para lienzo

Los grupos semilla en Canvas funcionan de forma similar a cualquier campaña desencadenada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los envía cuando tu usuario llega por primera vez a ese paso de correo electrónico concreto.

Si se actualizó un paso de correo electrónico después de enviar el grupo semilla, Braze presenta la opción de enviar sólo a los pasos actualizados, a todos los pasos o desactivar las semillas.