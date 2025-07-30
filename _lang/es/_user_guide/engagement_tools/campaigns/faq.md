---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre las campañas
page_order: 10
page_type: FAQ
description: "Esta página ofrece respuestas a las preguntas más frecuentes sobre las campañas."
tool: Campaigns

---

# Preguntas más frecuentes

> Este artículo da respuesta a algunas preguntas frecuentes sobre las campañas.

### ¿Cómo creo una campaña multicanal?

Para crear una campaña multicanal, selecciona **Mensajería** > Campañas. A continuación, selecciona **Crear campaña** > **Multicanal**. Desde aquí, puedes seleccionar uno de los siguientes canales de mensajería: Tarjetas de contenido, correo electrónico, LINE, notificaciones push, SMS/MMS/RCS, webhook, o WhatsApp.

### ¿Puedo añadir un grupo de control a mi campaña multicanal?

No, los grupos de control de las campañas están pensados para mensajes de un solo canal, como el correo electrónico A frente al correo electrónico B. Como alternativa, pruebe a utilizar [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) para probar diferentes canales, contenidos de mensajes y plazos de entrega. 

### ¿Cómo puedo empezar a probar y optimizar las campañas?

Las campañas multivariantes y los lienzos con múltiples variantes son una buena forma de empezar. Por ejemplo, puede realizar una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para probar un mensaje con diferentes copias o líneas de asunto. Los lienzos con múltiples variantes pueden ayudar a probar flujos de trabajo completos.

### ¿Por qué ha disminuido la tasa de apertura de mi campaña?

Las bajas tasas de apertura no siempre están relacionadas con un problema técnico. Puede haber problemas con el recorte del correo electrónico, lo que hace que falte un píxel de seguimiento. Sin embargo, también es posible que haya menos usuarios que abran sus correos electrónicos debido al contenido o a cambios en el tamaño de la audiencia. 

### ¿Cómo se evalúa el público de las campañas?

Por defecto, las campañas comprueban los filtros de audiencia en el momento de la entrada. Para las campañas basadas en acciones con retardo, existe la opción de reevaluar los criterios de segmento en el momento del envío para garantizar que los usuarios siguen formando parte del público objetivo cuando se envía el mensaje. 

### ¿Por qué existe una diferencia entre el número de destinatarios únicos y el número de envíos para una campaña o un Canvas determinados?

Una posible explicación podría ser que la campaña o Canvas tenga activada la re-elegibilidad, lo que significa que los usuarios elegibles para el segmento y la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, la explicación probable de la diferencia entre los envíos y los destinatarios únicos puede deberse a que los usuarios tienen varios dispositivos, en distintas plataformas, asociados a sus perfiles. 

Por ejemplo, si tienes un Canvas con notificaciones push tanto para iOS como para la web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

### ¿Por qué mi campaña tiene una base de usuarios alcanzable menor que el segmento que estoy utilizando para la campaña?

Si tiene configurado un [Grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), esto impedirá que un porcentaje de su audiencia alcanzable reciba campañas. Esto significa que el número de usuarios alcanzables para su segmento a veces puede ser mayor que el número de usuarios alcanzables para su campaña, incluso si la campaña está utilizando ese mismo segmento.

### ¿Qué ofrece la entrega en zona horaria local?

La entrega en zona horaria local le permite entregar campañas de mensajería a un segmento en función de la zona horaria individual de un usuario. Sin entrega en zona horaria local, las campañas se programarán en función de la configuración de zona horaria de su empresa en Braze. 

Por ejemplo, una empresa con sede en Londres que envíe una campaña a las 12 de la noche llegará a los usuarios de la costa oeste de Estados Unidos a las 4 de la madrugada. Si tu aplicación sólo está disponible en determinados países, puede que esto no suponga un riesgo para ti. De lo contrario, te recomendamos encarecidamente que evites enviar notificaciones push de madrugada a tu base de usuarios.

### ¿Cómo reconoce Braze la zona horaria de un usuario?

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Esto garantiza la precisión de la zona horaria y la cobertura total de tus usuarios. Los usuarios creados a través de la API de usuario o de otro modo sin zona horaria tendrán la zona horaria de su empresa como zona horaria por defecto hasta que sean reconocidos en su aplicación por el SDK. 

Puede comprobar la zona horaria de su empresa en [los ajustes de su empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) en el panel de control.

### ¿Cuándo evalúa Braze a los usuarios para la entrega según la zona horaria local?

Para la entrega en zona horaria local, Braze evalúa la elegibilidad de los usuarios para la entrada durante estas dos instancias:

- A la hora de Samoa (UTC +13) del día programado
- A la hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible para ambas comprobaciones. Por ejemplo, si el lanzamiento de un Canvas está programado para el 7 de agosto de 2021 a las 14.00 horas (zona horaria local), la selección de un usuario ubicado en Nueva York requeriría las siguientes comprobaciones de elegibilidad:

- Nueva York el 6 de agosto de 2021 a las 9 pm
- Nueva York el 7 de agosto de 2021 a las 2 pm

Tenga en cuenta que el usuario debe estar en el segmento 24 horas antes del lanzamiento. Si el usuario no cumple los requisitos en la primera comprobación, Braze no intentará la segunda.

Por ejemplo, si está previsto que una campaña se entregue a las 19:00 UTC, empezamos a poner en cola los envíos de la campaña en cuanto se identifica una zona horaria (como Samoa). Esto significa que nos estamos preparando para enviar el mensaje, no para enviar la campaña. Si los usuarios no coinciden con ningún filtro cuando comprobamos su elegibilidad, no entrarán en la audiencia objetivo.

Otro ejemplo: cree dos campañas programadas para enviarse el mismo día, una por la mañana y otra por la tarde, y añada un filtro para que los usuarios sólo puedan recibir la segunda campaña si ya han recibido la primera. Con la entrega en zona horaria local, es posible que algunos usuarios no reciban la segunda campaña. Esto se debe a que comprobamos la elegibilidad cuando se identifica la zona horaria del usuario, por lo que si la hora programada aún no se ha producido en su zona horaria, no ha recibido la primera campaña, lo que significa que no será elegible para la segunda campaña.

### ¿Cómo programar una campaña de zona horaria local?

Cuando programes una campaña, elige enviarla a una hora determinada y luego selecciona **Enviar campaña a los usuarios de su zona horaria local**.

Braze recomienda encarecidamente que todas las campañas de zonas horarias locales se programen con 24 horas de antelación. Dado que una campaña de este tipo debe enviarse durante todo un día, programarla con 24 horas de antelación garantiza que tu mensaje llegará a todo tu segmento. Sin embargo, puedes programar estas campañas con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a ningún usuario que haya incumplido la hora de envío en más de 1 hora. 

Por ejemplo, si es la 1 de la tarde y programa una campaña de zona horaria local para las 3 de la tarde, la campaña se enviará inmediatamente a todos los usuarios cuya hora local esté entre las 3 y las 4 de la tarde, pero no a los usuarios cuya hora local sea las 5 de la tarde. Además, la hora de envío que elija para su campaña tiene que no haber ocurrido todavía en la zona horaria de su empresa.

La edición de una campaña de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decide editar una campaña de zona horaria local para enviarla a una hora posterior (por ejemplo, a las 19:00 en lugar de a las 18:00), los usuarios que se encontraban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (18:00). Si edita una zona horaria local para que se envíe a una hora más temprana (por ejemplo, a las 16:00 en lugar de a las 17:00), la campaña se seguirá enviando a todos los miembros del segmento a la hora original (17:00). 

{% alert note %}
Para los componentes de Canvas, los usuarios no necesitan estar en el componente durante 24 horas para recibir el siguiente componente en el viaje del usuario para la entrega de zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser elegibles para la campaña, volverán a recibirla a la hora original (17:00 h). Sin embargo, para todas las apariciones posteriores de tu campaña, tus mensajes sólo se enviarán a la hora que hayas actualizado.

### ¿Cuándo entran en vigor los cambios en las campañas de la zona horaria local?

Los segmentos objetivo para campañas en zonas horarias locales deben incluir al menos una ventana de 48 horas para cualquier filtro basado en la hora para garantizar la entrega a todo el segmento. Por ejemplo, considere un segmento dirigido a usuarios en su segundo día con los siguientes filtros:

- Aplicación utilizada por primera vez hace más de 1 día
- La primera vez que usé la aplicación fue hace menos de 2 días

La entrega en zona horaria local puede pasar por alto a los usuarios de este segmento en función de la hora de entrega y de la zona horaria local de los usuarios. Esto se debe a que un usuario puede abandonar el segmento en el momento en que su zona horaria activa la entrega.

### ¿Qué cambios puedo hacer en las campañas programadas antes de su lanzamiento?

Cuando la campaña está programada, es necesario editar todo lo que no sea la composición de los mensajes antes de ponerlos en cola para su envío. Como en todas las campañas, no se pueden editar los eventos de conversión después de su lanzamiento.

### He actualizado mi campaña programada. ¿Por qué no se lanzó?

Esto puede ocurrir cuando una campaña está programada para lanzarse en el momento exacto en que se actualizó. Por ejemplo, si actualmente son las 15:10 y cambiaste la campaña para que se lanzara a las 15:10 y seleccionaste **Actualizar campaña**, ahora son más de las 15:10, lo que significa que ha pasado la hora programada para el lanzamiento. En lugar de programar la campaña para la misma hora, seleccione **Enviar en cuanto se lance la campaña**.

### ¿Cuál es la "zona segura" antes de que se pongan en cola los mensajes de una campaña programada?

Recomendamos realizar cambios en los mensajes dentro de los siguientes plazos:

- **Campañas programadas una sola vez:** Edita hasta la hora de envío programada.
- **Campañas programadas recurrentes:** Edita hasta la hora de envío programada.
- **Campañas locales de tiempo de envío:** Edita hasta 24 horas antes de la hora de envío programada.
- **Campañas con tiempo de envío óptimo:** Edita hasta 24 horas antes del día previsto para el envío de la campaña.

Si realizas cambios en tu mensaje fuera de estas recomendaciones, es posible que no veas reflejadas las actualizaciones en el mensaje enviado. Por ejemplo, si editas la hora de envío tres horas antes de que una campaña esté programada para enviarse a las 12 pm hora local, puede ocurrir lo siguiente:

- Braze no enviará mensajes a los usuarios que hayan incumplido la hora de envío en más de una hora.
- Los mensajes previamente en cola pueden seguir enviándose a la hora originalmente en cola, en lugar de a la hora ajustada.

Si necesitas hacer cambios, te recomendamos que detengas la campaña actual (esto cancelará cualquier mensaje en cola). A continuación, puedes duplicar la campaña, realizar los cambios necesarios y lanzar la nueva campaña. Es posible que tenga que excluir de esta campaña a los usuarios que ya hayan recibido la primera campaña. Asegúrese de reajustar las horas de programación de la campaña para tener en cuenta el envío según la zona horaria.

### ¿Por qué el número de usuarios que entran en una campaña no coincide con el esperado?

El número de usuarios que entran en una campaña puede diferir del número esperado debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, un público se evalúa antes del desencadenante (a menos que se utilice un desencadenante de [cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Esto hará que los usuarios abandonen la campaña si no forman parte inicialmente de tu audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de la campaña, asegúrate de ponerte en contacto con el soporte de Braze en los 30 días siguientes a la aparición del problema, ya que sólo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

### ¿Cuál es la diferencia entre las opciones Exportar datos de usuario CSV y Exportar dirección de correo electrónico CSV en la página de análisis de mi campaña?

Al seleccionar la opción **CSV Exportar direcciones de correo electrónico** sólo se descargarán los datos de los usuarios que tengan direcciones de correo electrónico. Por ejemplo, si tiene un segmento de 100.000 usuarios, pero sólo 50.000 de ellos tienen direcciones de correo electrónico, y hace clic en **CSV Exportar direcciones de correo electrónico**, sólo verá 50.000 filas de datos en el archivo CSV. En comparación, si selecciona **CSV Exportar datos de usuario**, se exportarán todos los datos de usuario.

### ¿Puedo buscar una campaña por su identificador API?

Sí, utilice el filtro `api_id:YOUR_API_ID` en la página **Campañas** para buscar una campaña por su identificador API. Consulte la [búsqueda de campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) para obtener más información.

### ¿Cuál es la diferencia entre las campañas API y las campañas desencadenadas por API?

Las campañas desencadenadas por API te permiten gestionar la copia de la campaña, las pruebas multivariantes y las reglas de reelegibilidad dentro del panel de Braze, a la vez que desencadenan la entrega de ese contenido desde tus propios servidores y sistemas. Estos mensajes también pueden incluir datos adicionales que se incluirán en plantillas en los mensajes en tiempo real.

Las campañas API se utilizan para hacer un seguimiento de los mensajes enviados mediante la API. A diferencia de la mayoría de las campañas, no especificas el mensaje, los destinatarios ni el horario, sino que pasas los identificadores a tus llamadas a la API. 

### ¿Cuál es la diferencia entre las campañas basadas en acciones y las activadas por API?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basada en acciones

Las campañas de entrega basadas en acciones o las campañas activadas por eventos son muy eficaces para los mensajes transaccionales o basados en logros y le permiten activarlas para que se envíen después de que un usuario complete un determinado evento. 

| Pros | Contras | 
| ---- | ---- |
| \- Visibilidad de las cargas JSON entrantes en la plataforma (si el evento ha sido activado por el usuario de prueba) a través del **registro de actividad de mensajes**.<br><br>\- Los elementos de personalización se incluyen en las propiedades de los eventos personalizados<br><br>\- El evento personalizado se puede utilizar para crear segmentos de usuarios elegibles para el mensaje. | \- Consume puntos de datos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Activada por API

Las campañas activadas por API y por servidor son ideales para gestionar transacciones más avanzadas, permitiéndote desencadenar la entrega del contenido de la campaña desde tus propios servidores y sistemas. La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán a la plantilla del mensaje en tiempo real.

| Beneficios | Consideraciones | 
| ---- | ---- |
| \- No consume puntos de datos<br><br>\- Los elementos de personalización se incluyen en las propiedades de la carga útil JSON | \- No permite crear un segmento de usuarios elegibles para el mensaje en las propiedades de la carga útil JSON.<br><br>\- No se pueden ver las cargas útiles JSON entrantes con el **registro de actividad de mensajes**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

