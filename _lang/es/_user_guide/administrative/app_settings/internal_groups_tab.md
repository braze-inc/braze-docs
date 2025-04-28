---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: "Este artículo de referencia cubre los Grupos Internos, una gran manera de obtener información sobre el SDK de su dispositivo de prueba o los registros de la API al probar la integración SDK."

---

# Grupos internos

> Los Grupos Internos son una excelente forma de crear y organizar grupos de prueba internos o de terceros. Proporcionan información sobre los registros de tu SDK o API, y son útiles para probar tu integración de SDK. Puedes crear un número ilimitado de Grupos internos personalizados con hasta 1.000 miembros.

Necesitas los [permisos de]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Access Dev Console** para tu espacio de trabajo para crear y gestionar Grupos Internos.

{% alert tip %}
Además de este artículo, también recomendamos consultar nuestro curso Braze Learning [sobre herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que trata sobre cómo utilizar grupos internos para llevar a cabo su propia solución de problemas y depuración.
{% endalert %}

## Crear un grupo

Para crear un Grupo Interno, realice los siguientes pasos: 

1. Vaya a **Configuración** > **Grupos internos**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar esta página en **Configuración** > **Consola de desarrollador** > **Grupos internos**.
{% endalert %}

{:start="2"}
2\. Haga clic en **Crear grupo interno**.
3\. Dale a tu grupo un nombre significativo.
4\. Elija uno o varios tipos de grupo, como se indica en el siguiente cuadro.

![Creación de un grupo interno en Braze][7]

| Tipo de grupo     | Casos de uso     |
| :------------- | :------------- |
| Grupo de eventos de usuarios| Se utiliza para verificar eventos o registros de su dispositivo de prueba.|
| Grupo de pruebas de contenido | Un concepto similar al de las listas de pruebas. Puede utilizarse en mensajes push, de correo electrónico e in-app para enviar una copia renderizada del mensaje.|
| Grupo semilla | Envía automáticamente una copia del correo electrónico a todas las personas del Grupo Semilla al enviarlo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Añadir usuarios de prueba

Después de crear su Grupo Interno, puede añadir usuarios de prueba como miembros de ese grupo. En la página de gestión de su grupo interno, haga clic en **Añadir usuario de prueba** y añádalos como usuarios identificados o anónimos en bloque.

![Configuración del Grupo Interno al crear un nuevo Grupo Interno][8]

| Método de adición | Descripción |
| :------------- | :------------- |
| Usuarios identificados |Buscar al usuario por su ID de usuario externo o su dirección de correo electrónico.|
|Usuarios anónimos| Busca por dirección IP. A continuación, proporcione un nombre para cada usuario de prueba que se añada. Este es el nombre con el que se asociarán todos los registros de eventos en la página [Registro de usuario de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/).|
|Añadir usuarios en bloque|Copie y pegue una lista de direcciones de correo electrónico o identificadores externos en la sección correspondiente. Sólo puede añadir usuarios ya conocidos en el panel de control. Para más información, consulte [Importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Grupos de pruebas de contenido

Similar al envío de una prueba de vista previa de un mensaje, el Grupo de prueba de contenido le ahorra tiempo y le permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente. Esta funcionalidad está disponible para mensajes push, mensajes dentro de la aplicación, SMS, correo electrónico y tarjetas de contenido dentro de Braze.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

Puedes seleccionar usuarios individuales de Braze o tantos Grupos Internos a los que enviar el mensaje. Si su mensaje incluye algún líquido u otra personalización dinámica, Braze utilizará los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tengan atributos, Braze utilizará el valor predeterminado establecido.

Además, si previsualiza el mensaje como usuario aleatorio, usuario personalizado o usuario existente, puede enviar esa versión previsualizada en su lugar. Si desactiva la casilla de verificación, podrá enviar en función de los atributos de cada usuario frente a la versión previsualizada.

Por último, si utiliza un grupo de IP para enviar un correo electrónico, puede seleccionar desde qué grupo de IP desea que se envíe el correo electrónico seleccionando el grupo en el menú desplegable disponible.

Sólo los grupos etiquetados como Grupos de prueba de contenido estarán disponibles en la sección de vista previa de un mensaje.

![Prueba de envío a grupos de prueba de contenidos][9]{: style="max-width:50%" }

### Grupos semilla

Los Grupos Semilla sólo están pensados para el canal de correo electrónico y permiten enviar una copia de cada mensaje de la variante de correo electrónico a los miembros de ese grupo. Los Grupos semilla no están disponibles para las campañas API, aunque puede incluir Grupos semilla a través de una entrada activada por API en la campaña. Esta característica se suele utilizar con socios como Return Path o 250OK para medir las métricas de capacidad de entrega. Puede utilizarse para mantener un registro del contenido del correo electrónico con fines históricos y de archivo. 

Tras crear un grupo interno y etiquetarlo para utilizarlo como grupo semilla, puede seleccionarlo en el paso **Usuarios objetivo** del compositor de campañas o en el paso **Configuración de envío** de un lienzo. Los correos electrónicos con semillas tendrán el identificador `[SEED]` añadido al principio de la línea del asunto del correo electrónico. Tenga en cuenta que los correos electrónicos semilla enviados no incrementan los envíos en los análisis del panel de control y no afectarán a los análisis de correo electrónico ni al retargeting. Tampoco actualizan la lista de **Campañas recibidas** de un perfil de usuario.

{% alert tip %}
Si los miembros de tu Grupo Semilla informan de que no ven el mensaje en su bandeja de entrada, asegúrate de que están incluidos en el Grupo Interno, comprueba que las líneas de asunto son diferentes y que Gmail no ha agrupado los mensajes, o pídeles que comprueben sus carpetas de SPAM.
{% endalert %}

#### Para las campañas

Los Grupos de Semillas pueden editarse desde la página de **Orientación** al componer una campaña de correo electrónico.

Los Grupos Semilla se envían una vez a cada variante de correo electrónico y se entregan la primera vez que el usuario recibe esa variante concreta. En el caso de los mensajes programados, suele ser la primera vez que se lanza la campaña. Para las campañas basadas en acciones o desencadenadas por la API, será el momento en que se envía un mensaje al primer usuario.

Si su campaña es multivariante y su variante tiene un porcentaje de envío del 0%, no se enviará a los grupos de semillas. Además, si la variante ya se ha enviado y no se ha actualizado para reenviarla en **Editar grupos de semillas** en el paso **Destino**, no se volverá a enviar por defecto.

{% alert note %}
Si hay una campaña recurrente y se realiza una actualización en alguna de las variantes, tiene la opción de volver a enviar sólo a las variantes actualizadas, a todas las variantes o desactivar el envío del Grupo de Semillas al actualizarse.
{% endalert %}

![Vista previa de los grupos de semillas para una campaña][11]

#### Para lienzo

Los grupos de semillas en Canvas funcionan de forma similar a la de cualquier campaña activada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los enviará cuando el usuario llegue por primera vez a ese paso concreto.

Si se actualizó un paso de correo electrónico después de enviar el grupo semilla, se presentará la opción de enviar solo a los pasos actualizados, a todos los pasos o de desactivar las semillas.


[7]: {% image_buster /assets/img_archive/internal_group.png %}
[8]: {% image_buster /assets/img_archive/UserLogs1.png %}
[9]: {% image_buster /assets/img_archive/content_test_preview.png %}
[11]: {% image_buster /assets/img_archive/seed_group_campaign.png %}
