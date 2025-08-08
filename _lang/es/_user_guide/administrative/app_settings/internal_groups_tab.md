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

1. Vaya a **Configuración** > **Grupos internos**.
2. Selecciona **Crear grupo interno**.
3. Dale a tu grupo un nombre, como "Grupo de prueba de correo electrónico".
4. Elige uno o varios tipos de grupo, como se indica en la tabla siguiente.

| Tipo de grupo         | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuarios**   | Se utiliza para verificar eventos o registros de su dispositivo de prueba.                                    |
| **Grupo de pruebas de contenido** | Puede utilizarse en mensajes push, de correo electrónico e in-app para enviar una copia renderizada del mensaje. |
| **Grupo semilla**         | Envía automáticamente una copia del correo electrónico a todas las personas del Grupo Semilla al enviarlo.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Un grupo interno llamado "Grupo de prueba de correo electrónico".]({% image_buster /assets/img_archive/internal_group.png %})

### Añadir usuarios de prueba

Después de crear tu grupo interno, puedes añadir usuarios de prueba como miembros de ese grupo. 

1. En la página de administración de tu grupo interno, selecciona **Añadir usuarios de prueba**.
2. Elige uno de los siguientes métodos para buscar y seleccionar a tus usuarios de prueba.

| Método                  | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Añadir usuario identificado** | Busca al usuario por su ID externo, dirección de correo electrónico, número de teléfono o token de notificaciones push.                                                                                                                                                           |
| **Añadir usuario anónimo**  | Busca por dirección IP. A continuación, proporcione un nombre para cada usuario de prueba que se añada. Este es el nombre con el que se asociarán todos los registros de eventos en la página [Registro de usuario de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
| **Añadir usuarios en bloque**      | Copia y pega una lista de direcciones de correo electrónico o ID externos. Sólo puede añadir usuarios ya conocidos en el panel de control. Para más información, consulta [Importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Configuración del grupo interno al crear un nuevo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de pruebas de contenido

Similar al envío de una prueba de vista previa de un mensaje, el Grupo de prueba de contenido le ahorra tiempo y le permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente. Está disponible para push, mensajes dentro de la aplicación, SMS, correo electrónico y tarjetas de contenido en Braze. Sólo los grupos etiquetados como Grupos de prueba de contenido estarán disponibles en la sección de vista previa de un mensaje.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

Puedes seleccionar usuarios individuales de Braze o tantos grupos internos a los que enviar el mensaje. Si su mensaje incluye algún líquido u otra personalización dinámica, Braze utilizará los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tengan atributos, Braze utilizará el valor predeterminado establecido.

Además, si previsualiza el mensaje como usuario aleatorio, usuario personalizado o usuario existente, puede enviar esa versión previsualizada en su lugar. Si desactiva la casilla de verificación, podrá enviar en función de los atributos de cada usuario frente a la versión previsualizada.

Si utilizas un conjunto de IP para enviar un correo electrónico, puedes seleccionar desde qué conjunto de IP deseas que se envíe el correo electrónico seleccionando el conjunto en el desplegable disponible.

![La sección Pruebas del editor de mensajes dentro de la aplicación para seleccionar el Grupo de Pruebas de Contenido.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos semilla

Los grupos semilla sólo son compatibles con el canal de correo electrónico. Puedes añadir usuarios a un grupo semilla para enviar copias de cada mensaje de variante de correo electrónico a todos los miembros del grupo.

Los Grupos semilla no están disponibles para las campañas API, pero puedes incluir Grupos semilla utilizando una entrada desencadenada por la API en la campaña. Puedes utilizarlo para medir las métricas de capacidad de entrega y para mantener un registro del contenido de tu correo electrónico con fines históricos y de archivo. 

Tras crear un grupo interno y etiquetarlo para utilizarlo como grupo semilla, puedes seleccionarlo en el paso **Audiencias** objetivo del editor de campañas, o en el paso **Configuración de envío** de un Canvas. 

Los correos electrónicos con semillas tendrán `[SEED]` añadido al principio de la línea del asunto del correo electrónico. Ten en cuenta que los envíos por correo electrónico **no lo hacen**:

- Incrementa los envíos en el panel de análisis.
- Impacta el análisis del correo electrónico o la reorientación. 
- Actualiza la lista de **campañas recibidas** de un perfil de usuario.
- Limitación de frecuencia de impacto.

{% alert tip %}
Si los miembros de tu grupo semilla dicen que no ven el mensaje en su buzón de entrada, comprueba que están incluidos en el grupo interno, verifica que las líneas del asunto son diferentes y que Gmail no ha agrupado los mensajes, o pídeles que comprueben sus carpetas de correo no deseado.
{% endalert %}

#### Para las campañas

Al componer una campaña de correo electrónico, puedes editar tus grupos semilla en la sección **Audiencias objetivo** del editor.

Los Grupos Semilla se envían una vez a cada variante de correo electrónico y se entregan la primera vez que el usuario recibe esa variante concreta. En el caso de los mensajes programados, suele ser la primera vez que se lanza la campaña. Para las campañas basadas en acciones o desencadenadas por la API, será el momento en que se envía un mensaje al primer usuario.

Si tu campaña es multivariante y tu variante tiene un porcentaje de envío del 0%, no se enviará a los grupos semilla. Además, si la variante ya se ha enviado y no se ha actualizado para reenviarla en **Editar grupos semilla** en el paso **Destino**, no se volverá a enviar por predeterminado.

{% alert note %}
Si tienes una campaña recurrente y se actualiza alguna de las variantes, puedes elegir enviar de nuevo sólo a las variantes actualizadas o a todas las variantes, o desactivar el envío de Grupo semilla al actualizarse.
{% endalert %}

![El grupo semilla seleccionado para el envío de la campaña de correo electrónico Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para lienzo

Los grupos de semillas en Canvas funcionan de forma similar a la de cualquier campaña activada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los enviará cuando el usuario llegue por primera vez a ese paso concreto.

Si se actualizó un paso de correo electrónico después de enviar el grupo semilla, se presentará la opción de enviar solo a los pasos actualizados, a todos los pasos o de desactivar las semillas.

