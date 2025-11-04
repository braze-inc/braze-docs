---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes sobre las campañas
page_order: 10
page_type: FAQ
description: "Esta página ofrece respuestas a las preguntas más frecuentes sobre las campañas."
tool: Campaigns

---

# Preguntas más frecuentes

> Este artículo responde a algunas preguntas frecuentes sobre las campañas.

### ¿Cómo creo una campaña multicanal?

Para crear una campaña multicanal, selecciona **Mensajería** > Campañas. A continuación, selecciona **Crear campaña** > **Multicanal**. Desde aquí, puedes seleccionar uno de los siguientes canales de mensajería: Tarjetas de contenido, correo electrónico, LINE, notificaciones push, SMS/MMS/RCS, webhook o WhatsApp.

### ¿Puedo añadir un grupo de control a mi campaña multicanal?

No, los grupos de control en las campañas están pensados para mensajes de un solo canal, como el correo electrónico A frente al correo electrónico B. Como alternativa, prueba a utilizar [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) para probar diferentes canales, contenidos de mensajería y plazos de entrega. 

### ¿Cómo puedo empezar a probar y optimizar las campañas?

¡Las campañas multivariantes y los Lienzos en funcionamiento con múltiples variantes son una forma estupenda de empezar! Por ejemplo, puedes realizar una [campaña multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para probar un mensaje que tenga diferentes copias o líneas del asunto. Los lienzos con múltiples variantes pueden ayudar a probar flujos de trabajo completos.

### ¿Por qué ha disminuido la tasa de apertura de mi campaña?

Las bajas tasas de apertura no siempre están relacionadas con un problema técnico. Puede haber problemas con el recorte del correo electrónico, lo que hace que falte un píxel de seguimiento. Sin embargo, también es posible que haya menos usuarios que abran sus correos electrónicos debido al contenido o a cambios en el tamaño de la audiencia. 

### ¿Cómo se evalúan las audiencias de las campañas?

Por defecto, las campañas comprueban los filtros de audiencia en el momento de la entrada. Para las campañas basadas en acciones con retraso, existe la opción de reevaluar los criterios de segmento en el momento del envío para garantizar que los usuarios siguen formando parte de la audiencia objetivo cuando se envía el mensaje. 

### ¿Por qué hay una diferencia entre el número de destinatarios únicos y el número de envíos para una campaña o Canvas determinado?

Una posible explicación podría ser que la campaña o Canvas tenga activada la re-elegibilidad, lo que significa que los usuarios elegibles para el segmento y la configuración de entrega podrán recibir el mensaje más de una vez. Si la reelegibilidad no está activada, la explicación probable de la diferencia entre envíos y destinatarios únicos puede deberse a que los usuarios tienen varios dispositivos, en distintas plataformas, asociados a sus perfiles. 

Por ejemplo, si tienes un Canvas que tiene notificaciones push tanto de iOS como de Web, un usuario determinado con dispositivos móviles y de escritorio podría recibir más de un mensaje.

### ¿Por qué mi campaña tiene una base de usuarios alcanzable menor que el segmento que estoy utilizando para la campaña?

Si tienes configurado un [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), esto impedirá que un porcentaje de tu audiencia alcanzable reciba campañas. Esto significa que el número de usuarios alcanzables para tu segmento a veces puede ser mayor que el número de usuarios alcanzables para tu campaña, aunque la campaña esté utilizando ese mismo segmento.

### ¿Qué ofrece la entrega según la zona horaria local?

La entrega según la zona horaria local te permite entregar campañas de mensajería a un segmento basado en la zona horaria individual de un usuario. Sin entrega según la zona horaria local, las campañas se programarán según la configuración de la zona horaria de tu empresa en Braze. 

Por ejemplo, una empresa con sede en Londres que envíe una campaña a las 12 de la noche llegará a los usuarios de la costa oeste de Estados Unidos a las 4 de la madrugada. Si tu aplicación sólo está disponible en determinados países, puede que esto no suponga un riesgo para ti. De lo contrario, te recomendamos encarecidamente que evites enviar notificaciones push de madrugada a tu base de usuarios.

### ¿Cómo reconoce Braze la zona horaria de un usuario?

Braze determinará automáticamente la zona horaria del usuario a partir de su dispositivo. Esto garantiza la precisión de la zona horaria y la cobertura total de tus usuarios. Los usuarios creados a través de la API de usuario o de otra forma sin zona horaria tendrán la zona horaria de tu empresa como zona horaria predeterminada hasta que sean reconocidos en tu aplicación por el SDK. 

Puedes comprobar la zona horaria de tu empresa en la [configuración de tu empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) en el panel.

### ¿Cuándo evalúa Braze a los usuarios para la entrega según la zona horaria local?

Para la entrega según la zona horaria local, Braze evalúa a los usuarios para determinar si son elegibles para la entrada durante estas dos instancias:

- A la hora de Samoa (UTC+13) del día programado
- A la hora local del día programado

Para que un usuario sea elegible para la entrada, debe ser elegible para ambas comprobaciones. Por ejemplo, si el lanzamiento de un Canvas está programado para el 7 de agosto de 2021 a las 14.00 h de la zona horaria local, dirigirse a un usuario ubicado en Nueva York requeriría las siguientes comprobaciones para ser elegible:

- Nueva York el 6 de agosto de 2021 a las 21.00 horas
- Nueva York el 7 de agosto de 2021 a las 2 pm

Ten en cuenta que el usuario tiene que estar en el segmento 24 horas antes del lanzamiento. Si el usuario no es elegible en la primera comprobación, Braze no intentará la segunda comprobación.

Por ejemplo, si está previsto que una campaña se entregue a las 19:00 UTC, empezamos a poner en cola los envíos de la campaña en cuanto se identifica una zona horaria (como Samoa). Esto significa que nos estamos preparando para enviar el mensaje, no para enviar la campaña. Si los usuarios no coinciden con ningún filtro cuando comprobamos su elegibilidad, no entrarán en la audiencia objetivo.

Como otro ejemplo, digamos que quieres crear dos campañas programadas para enviarse el mismo día -una por la mañana y otra por la tarde- y añadir un filtro para que los usuarios sólo puedan recibir la segunda campaña si ya han recibido la primera. Con la entrega según la zona horaria local, es posible que algunos usuarios no reciban la segunda campaña. Esto se debe a que comprobamos la elegibilidad cuando se identifica la zona horaria del usuario, por lo que si la hora programada aún no se ha producido en su zona horaria, no ha recibido la primera campaña, lo que significa que no será elegible para la segunda campaña.

### ¿Cómo programo una campaña de zona horaria local?

Cuando programes una campaña, elige enviarla a una hora determinada y luego selecciona **Enviar campaña a los usuarios de su zona horaria local**.

Braze recomienda encarecidamente que todas las campañas de zonas horarias locales se programen con 24 horas de antelación. Dado que una campaña de este tipo debe enviarse durante todo un día, programarla con 24 horas de antelación garantiza que tu mensaje llegará a todo tu segmento. Sin embargo, puedes programar estas campañas con menos de 24 horas de antelación si es necesario. Ten en cuenta que Braze no enviará mensajes a los usuarios que hayan incumplido la hora de envío en más de 1 hora. 

Por ejemplo, si es la 1 de la tarde y programas una campaña de zona horaria local para las 3 de la tarde, la campaña se enviará inmediatamente a todos los usuarios cuya hora local esté entre las 3 y las 4 de la tarde, pero no a los usuarios cuya hora local sea las 5 de la tarde. Además, la hora de envío que elijas para tu campaña tiene que no haber ocurrido todavía en la zona horaria de tu empresa.

Editar una campaña de zona horaria local programada con menos de 24 horas de antelación no alterará la programación del mensaje. Si decides editar una campaña de zona horaria local para enviarla a una hora posterior (por ejemplo, a las 19:00 en lugar de a las 18:00), los usuarios que estaban en el segmento objetivo cuando se eligió la hora de envío original seguirán recibiendo el mensaje a la hora original (18:00). Si editas una zona horaria local para que se envíe a una hora más temprana (por ejemplo, a las 16:00 en lugar de a las 17:00), la campaña se seguirá enviando a todos los miembros del segmento a la hora original (17:00). 

{% alert note %}
En el caso de los componentes Canvas, los usuarios no necesitan estar en el componente durante 24 horas para recibir el siguiente componente en el recorrido del usuario para la entrega según la zona horaria local.
{% endalert %}

Si has permitido que los usuarios vuelvan a ser elegibles para la campaña, volverán a recibirla a la hora original (17:00 h). Sin embargo, para todas las apariciones posteriores de tu campaña, tus mensajes sólo se enviarán a la hora que hayas actualizado.

### ¿Cuándo entran en vigor los cambios en las campañas de las zonas horarias locales?

Los segmentos objetivo de las campañas en zonas horarias locales deben incluir al menos un margen de 48 horas para cualquier filtro basado en la hora, con el fin de garantizar la entrega a todo el segmento. Por ejemplo, considera un segmento dirigido a usuarios en su segundo día con los siguientes filtros:

- Aplicación utilizada por primera vez hace más de 1 día
- Aplicación utilizada por primera vez hace menos de 2 días

La entrega según la zona horaria local puede pasar por alto a los usuarios de este segmento en función de la hora de entrega y de la zona horaria local de los usuarios. Esto se debe a que un usuario puede abandonar el segmento en el momento en que su zona horaria desencadena la entrega.

### ¿Qué cambios puedo hacer en las campañas programadas antes del lanzamiento?

Cuando la campaña está programada, hay que editar todo lo que no sea la composición del mensaje antes de poner en cola los mensajes que se van a enviar. Como en todas las campañas, no puedes editar los eventos de conversión una vez lanzada.

### He actualizado mi campaña programada. ¿Por qué no se lanzó?

Esto puede ocurrir cuando una campaña está programada para lanzarse en el momento exacto en que se actualizó. Por ejemplo, si actualmente son las 15:10 y cambiaste la campaña para que se lanzara a las 15:10 y seleccionaste **Actualizar campaña**, ahora son más de las 15:10, lo que significa que ha pasado la hora programada para el lanzamiento. En lugar de programar la campaña para el mismo momento, selecciona **Enviar en cuanto se lance la campaña**.

### ¿Qué es la "zona segura" antes de que se pongan en cola los mensajes de una campaña programada?

Recomendamos realizar cambios en los mensajes dentro de los siguientes plazos:

- **Campañas programadas una sola vez:** Edita hasta la hora de envío programada.
- **Campañas programadas recurrentes:** Edita hasta la hora de envío programada.
- **Campañas locales de tiempo de envío:** Edita hasta 24 horas antes de la hora de envío programada.
- **Campañas con tiempo de envío óptimo:** Edita hasta 24 horas antes del día previsto para el envío de la campaña.

Si realizas cambios en tu mensaje fuera de estas recomendaciones, es posible que no veas reflejadas las actualizaciones en el mensaje enviado. Por ejemplo, si editas la hora de envío tres horas antes de que una campaña esté programada para enviarse a las 12 pm hora local, puede ocurrir lo siguiente:

- Braze no enviará mensajes a los usuarios que hayan sobrepasado la hora de envío en más de una hora.
- Los mensajes previamente en cola pueden seguir enviándose a la hora originalmente en cola, en lugar de a la hora ajustada.

Si necesitas hacer cambios, te recomendamos que detengas la campaña actual (esto cancelará cualquier mensaje en cola). A continuación, puedes duplicar la campaña, realizar los cambios necesarios y lanzar la nueva campaña. Puede que tengas que excluir de esta campaña a usuarios que ya hayan recibido la primera campaña. Asegúrate de reajustar las horas de programación de la campaña para permitir el envío según la zona horaria.

### ¿Por qué el número de usuarios que entran en una campaña no coincide con el esperado?

El número de usuarios que entran en una campaña puede diferir del que esperabas debido a cómo se evalúan las audiencias y los desencadenantes. En Braze, la audiencia se evalúa antes del desencadenamiento (a menos que se utilice un desencadenamiento [por cambio de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Esto hará que los usuarios abandonen la campaña si no forman parte inicialmente de tu audiencia seleccionada antes de que se evalúe cualquier acción desencadenante.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de la campaña, asegúrate de ponerte en contacto con el soporte de Braze en los 30 días siguientes a la aparición del problema, ya que sólo disponemos de los registros de diagnóstico de los últimos 30 días.
{% endalert %}

### ¿Cuál es la diferencia entre las opciones Exportar datos de usuario CSV y Exportar dirección de correo electrónico CSV de la página de análisis de mi campaña?

Si seleccionas la opción **CSV Exportar direcciones de correo electrónico**, sólo se descargarán los datos de los usuarios con direcciones de correo electrónico. Por ejemplo, si tienes un segmento de 100.000 usuarios, pero sólo 50.000 de ellos tienen direcciones de correo electrónico, y haces clic en **CSV Exportar direcciones de correo electrónico**, entonces deberías esperar ver sólo 50.000 filas de datos en el archivo CSV. En comparación, si seleccionas **Exportar datos de usuario CSV**, se exportarán todos los datos de usuario.

### ¿Puedo buscar una campaña por su identificador API?

Sí, utiliza el filtro `api_id:YOUR_API_ID` en la página de **Campañas** para buscar una campaña por su identificador API. Consulta la [búsqueda de campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) para obtener más información.

### ¿Cuál es la diferencia entre las campañas API y las campañas desencadenadas por API?

Las campañas desencadenadas por API te permiten gestionar la copia de la campaña, las pruebas multivariantes y las reglas de reelegibilidad dentro del panel de Braze, a la vez que desencadenan la entrega de ese contenido desde tus propios servidores y sistemas. Estos mensajes también pueden incluir datos adicionales que se incluirán en plantillas en los mensajes en tiempo real.

Las campañas API se utilizan para hacer un seguimiento de los mensajes enviados mediante la API. A diferencia de la mayoría de las campañas, no especificas el mensaje, los destinatarios ni el horario, sino que pasas los identificadores a tus llamadas a la API. 

### ¿Cuál es la diferencia entre las campañas basadas en acciones y las desencadenadas por API?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Basado en la acción

Las campañas de entrega basadas en acciones o las campañas desencadenadas por eventos son muy eficaces para los mensajes transaccionales o basados en logros, y te permiten desencadenar su envío después de que un usuario complete un determinado evento. 

| Pros | Contras | 
| ---- | ---- |
| \- Visibilidad de las cargas útiles JSON entrantes en la plataforma (si el evento ha sido desencadenado por un usuario de prueba) a través del **Registro de Actividad de Mensajes**<br><br>\- Los elementos de personalización se incluyen en las propiedades del evento personalizado<br><br>\- Se puede utilizar un evento personalizado para crear Segmentos de usuarios elegibles para el mensaje | \- Consume puntos de datos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Desencadenado por API

Las campañas activadas por API y por servidor son ideales para gestionar transacciones más avanzadas, permitiéndote desencadenar la entrega del contenido de la campaña desde tus propios servidores y sistemas. La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se plantillasen en el mensaje en tiempo real.

| Beneficios | Consideraciones | 
| ---- | ---- |
| \- No registra puntos de datos<br><br>\- Los elementos de personalización se incluyen en las propiedades de la carga útil JSON | \- No permite crear un segmento de usuarios elegibles para el mensaje en las propiedades de la carga útil JSON<br><br>\- No se pueden ver las cargas útiles JSON entrantes con el **registro de actividad de mensajes**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

