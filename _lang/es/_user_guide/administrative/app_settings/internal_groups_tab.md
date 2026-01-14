---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artículo de referencia trata de los grupos internos, una forma estupenda de obtener información sobre el SDK o los registros de API de tu dispositivo de prueba al probar la integración de SDK."

---

# Grupos internos

> Los grupos internos son una forma estupenda de crear y organizar grupos de prueba internos o de terceros. Proporcionan información sobre los registros de tu SDK o API y son útiles para probar tu integración de SDK. Puedes crear un número ilimitado de grupos internos personalizados con hasta 1.000 usuarios.

{% alert tip %}
También te recomendamos que eches un vistazo a nuestro curso de Braze Learning [Pruebas y solución de problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que explica cómo utilizar grupos internos para llevar a cabo tu propia solución de problemas y depuración.
{% endalert %}

## Requisitos previos

Antes de poder crear y gestionar grupos internos, necesitas el [permiso Consola Access Dev]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) para tu espacio de trabajo.

## Crear un grupo interno

Para crear un grupo interno, haz lo siguiente: 

1. Ve a **Configuración** > Grupos internos.
2. Selecciona **Crear grupo interno**.
3. Dale un nombre a tu grupo, como "Grupo de prueba de correo electrónico".
4. Elige uno o varios tipos de grupo, como se indica en la tabla siguiente.

| Tipo de grupo         | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuarios**   | Sirve para verificar los eventos o registros de tu dispositivo de prueba.                                    |
| **Grupo de Pruebas de Contenido** | Se puede utilizar en mensajes push, correo electrónico y mensajería dentro de la aplicación para enviar una copia renderizada del mensaje. |
| **Grupo semilla**         | Envía automáticamente una copia del correo electrónico a todos los miembros del grupo semilla al enviarlo.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Un grupo interno llamado "Grupo de prueba de correo electrónico".]({% image_buster /assets/img_archive/internal_group.png %})

### Añadir usuarios de prueba

Después de crear tu grupo interno, puedes añadir usuarios de prueba como miembros de ese grupo. 

1. En la página de administración de tu grupo interno, selecciona **Añadir usuarios de prueba**.
2. Elige uno de los siguientes métodos para buscar y seleccionar a tus usuarios de prueba.

| Método                  | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Añadir usuario identificado** | Busca al usuario por su ID externo, dirección de correo electrónico, número de teléfono o token de notificaciones push.                                                                                                                                                           |
| **Añadir usuario anónimo**  | Buscar por dirección IP. A continuación, proporciona un nombre para cada usuario de prueba que se añada. Este es el nombre con el que se asociarán todos los registros de usuarios del evento en la página [Registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Añadir usuarios en bloque**      | Copia y pega una lista de direcciones de correo electrónico o ID externos. Sólo puedes añadir usuarios que ya sean conocidos en el panel. Para más información, consulta [Importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Configuración del grupo interno al crear un nuevo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de pruebas de contenido

Similar al envío de una vista previa de prueba de un mensaje, el Grupo de Prueba de Contenido te ahorra tiempo y te permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente. Está disponible para push, mensajes dentro de la aplicación, SMS, correo electrónico y tarjetas de contenido en Braze. Sólo los grupos etiquetados como Grupos de prueba de contenido estarán disponibles en la vista previa de un mensaje.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

Puedes seleccionar usuarios individuales de Braze o tantos grupos internos a los que enviar el mensaje. Si tu mensaje incluye Liquid u otra personalización dinámica, Braze utilizará los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tengan atributos, Braze utilizará el valor predeterminado establecido.

Además, si previsualizas el mensaje como un usuario aleatorio, un usuario personalizado o un usuario existente, puedes enviar esa versión previsualizada en su lugar. Si desactivas la casilla de verificación, podrás realizar el envío en función de los atributos de cada usuario frente a la versión previsualizada.

Si utilizas un conjunto de IP para enviar un correo electrónico, puedes seleccionar desde qué conjunto de IP deseas que se envíe el correo electrónico seleccionando el conjunto en el desplegable disponible.

La sección Prueba del editor de mensajes dentro de la aplicación para seleccionar el Grupo de prueba de contenido.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos semilla

Los grupos semilla sólo son compatibles con el canal de correo electrónico. Puedes añadir usuarios a un grupo semilla para enviar copias de cada mensaje de variante de correo electrónico a todos los miembros del grupo.

Los Grupos semilla no están disponibles para las campañas API, pero puedes incluir Grupos semilla utilizando una entrada desencadenada por la API en la campaña. Puedes utilizarlo para medir las métricas de capacidad de entrega y para mantener un registro del contenido de tu correo electrónico con fines históricos y de archivo. 

Tras crear un grupo interno y etiquetarlo para utilizarlo como grupo semilla, puedes seleccionarlo en el paso **Audiencias** objetivo del editor de campañas, o en el paso **Configuración de envío** de un Canvas. 

Los correos electrónicos con semillas tendrán `[SEED]` añadido al principio de la línea del asunto del correo electrónico. Ten en cuenta que los envíos por correo electrónico **no lo hacen**:

- Incrementa los envíos en el panel de análisis.
- Impacta el análisis del correo electrónico o la reorientación. 
- Actualiza la lista de **campañas recibidas** de un perfil de usuario.
- Limitación de frecuencia de impacto.
- Contabiliza o influye en los límites de tasa de velocidad de entrega.

{% alert tip %}
Si los miembros de tu grupo semilla dicen que no ven el mensaje en su buzón de entrada, comprueba que están incluidos en el grupo interno, verifica que las líneas del asunto son diferentes y que Gmail no ha agrupado los mensajes, o pídeles que comprueben sus carpetas de correo no deseado.
{% endalert %}

#### Para campañas

Al componer una campaña de correo electrónico, puedes editar tus grupos semilla en la sección **Audiencias objetivo** del editor.

Los grupos semilla se envían a cada variante de correo electrónico una vez y se entregan la primera vez que tu usuario recibe esa variante concreta. Para los mensajes programados, suele ser la primera vez que se lanza la campaña. Para campañas basadas en acciones o desencadenadas por API, será el momento en que se envíe un mensaje al primer usuario.

Si tu campaña es multivariante y tu variante tiene un porcentaje de envío del 0%, no se enviará a los grupos semilla. Además, si la variante ya se ha enviado y no se ha actualizado para reenviarla en **Editar grupos semilla** en el paso **Destino**, no se volverá a enviar por predeterminado.

{% alert note %}
Si tienes una campaña recurrente y se actualiza alguna de las variantes, puedes elegir enviar de nuevo sólo a las variantes actualizadas o a todas las variantes, o desactivar el envío de Grupo semilla al actualizarse.
{% endalert %}

Se ha seleccionado el grupo semilla "Prueba de semillas de correo electrónico" al que se enviará la campaña de correo electrónico Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas

Los grupos semilla en Canvas funcionan de forma similar a cualquier campaña desencadenada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los enviará cuando tu usuario llegue por primera vez a ese paso de correo electrónico concreto.

Si se actualizó un paso de correo electrónico después de enviar el grupo semilla, se presentará la opción de enviar sólo a los pasos actualizados, a todos los pasos o de desactivar las semillas.

