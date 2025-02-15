---
nav_title: Funcionalidades basadas en el tiempo
article_title: Funcionalidades basadas en el tiempo para Canvas
page_order: 1
tools: Canvas
page_type: reference
description: "En este artículo de referencia se cubren definiciones, zonas horarias y ejemplos de funcionalidades basadas en el tiempo para Canvas."

---

# Funcionalidades basadas en el tiempo para Canvas

> Este artículo de referencia cubre las funcionalidades de Canvas basadas en el tiempo para ayudar con las estrategias, la resolución de problemas y para responder a preguntas comunes. 

## Planificar retraso

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia cuando se edita el horario de un Lienzo existente creado utilizando el flujo de trabajo del Lienzo original. Para funcionalidades basadas en el tiempo para el flujo de trabajo de Canvas Flow, consulte el [componente Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
{% endalert %}

### Enviar inmediatamente

| Definición |  Zona horaria |
| --- | --- |
| Enviar mensaje inmediatamente después de que el usuario reciba el paso anterior, o si este es el primer paso, inmediatamente después de que el usuario entre en el Canvas. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### Enviar después de X días

| Definición |  Zona horaria |
| --- | --- |
| Enviar mensaje después de un retraso. Puede especificar un retraso en segundos, minutos, horas, días o semanas.  | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Enviar el próximo [día de la semana] a X hora

| Definición |  Zona horaria |
| --- | --- |
| Enviar mensaje el siguiente día de la semana especificado, a una hora del día seleccionada.  | Seleccione entre **la hora local del usuario** o **la hora de la empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por ejemplo, supongamos que selecciona "Enviar el sábado siguiente a las 15:15". Si un usuario entra en el lienzo un sábado, recibiría ese mensaje el sábado siguiente dentro de siete días. Si entran un viernes, el sábado siguiente sería en un día.

![][3]

### Enviar en X días naturales a la hora Y

| Definición |  Zona horaria |
| --- | --- |
| Envía un mensaje en un número determinado de días a una hora especificada. | Seleccione entre **la hora local del usuario** o **la hora de la empresa** |

Canvas calcula el retraso como `day of the week` + `calendar days`, y luego añade el `time`. Por ejemplo, supongamos que un componente Canvas se envía el lunes a las 21:00 horas, y que el siguiente paso está programado para "Enviar en 1 día a las 9:00 horas". Ese mensaje se entregará el martes a las 9 de la mañana, porque el Canvas calcula el retraso como `Monday` + `1 calendar day`, y luego añade `9 am`.

![][4]

### Intelligent Timing

| Definición | Zona horaria |
| ---------- | ----- |
| [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) calcula el momento óptimo de envío basándose en un análisis estadístico de las interacciones anteriores del usuario con su mensajería (por canal) y su aplicación. | Si selecciona **una hora específica** como [alternativa]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), ésta se enviará en la hora local del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## Limitación global de frecuencias

| Definición | Zona horaria |
| --- | --- |
| Limite el número de veces que cada usuario debe recibir el lienzo en un plazo determinado, que puede medirse en minutos, días, semanas (siete días) y meses. | Hora local del usuario. Si la zona horaria de un usuario no está configurada, se utilizará la zona horaria de la empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[La limitación de la frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) se basa en días naturales, no en un periodo de 24 horas. Esto significa que podrías establecer una regla de limitación de frecuencia de envío de no más de una campaña al día, pero si un usuario recibe un mensaje a las 11 de la noche en su hora local, todavía puede recibir otro mensaje una hora más tarde (en la medianoche del siguiente día natural).

![][6]

{% alert note %}
Si tiene los [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) adecuados para aprobar lienzos, verá un [paso de**resumen**]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals) en el flujo de trabajo.
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
