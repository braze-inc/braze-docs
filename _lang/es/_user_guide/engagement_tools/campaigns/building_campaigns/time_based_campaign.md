---
nav_title: Funcionalidades temporales para las campañas
article_title: Funcionalidades temporales para las campañas
page_order: 2
tool: Campaigns
page_type: reference
description: "Este artículo de referencia cubre las funcionalidades basadas en el tiempo para las campañas, como la entrega programada, la sincronización inteligente y la entrega basada en acciones."

---
# Funcionalidades temporales para las campañas

> Al utilizar campañas, puede utilizar las opciones de programación basadas en el tiempo para llegar a su público. Estas funcionalidades basadas en el tiempo incluyen campañas configuradas para entregas programadas y entregas basadas en acciones.

{% alert tip %}
Para más información sobre la entrega de campañas, consulta nuestro curso de Braze Learning dedicado a [la Configuración de Campañas](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
{% endalert %}

## Entrega programada

Esta sección cubre la programación basada en el tiempo y las opciones de entrega para las campañas de [entrega programada]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/).

### Enviar a una hora determinada

| Definición | Zona horaria |
| ---------- | --------- |
| Enviar un mensaje a una hora determinada, en una fecha concreta del calendario. | Zona horaria de la empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con la opción "Enviar a una hora determinada" seleccionada para enviar una vez a partir de las 9 de la mañana del 13 de julio de 2021.][2]

### Intelligent Timing

| Definición | Zona horaria |
| ---------- | --------- |
| Tiempo óptimo del usuario. Cada usuario recibirá la campaña en el momento en que sea más probable que participe. Para saber más, consulta [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/). | Si selecciona una hora específica como [alternativa]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), ésta se enviará en la hora local del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con la opción "Temporización inteligente" seleccionada para enviar una vez a la hora óptima el 13 de julio de 2021 con una hora alternativa personalizada de las 9 de la mañana para los usuarios sin suficientes datos en sus perfiles para calcular una hora óptima.][3]

### Enviar la campaña a los usuarios en su zona horaria local

| Definición | Zona horaria |
| ---------- | --------- |
| Permite enviar mensajes a un segmento en función de la [zona horaria de cada usuario]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery). | Hora local del usuario. Si la zona horaria de un usuario no está configurada, se utilizará la zona horaria de la empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con la opción "Enviar a una hora determinada" seleccionada para enviar una vez a partir de las 9 de la mañana del 13 de julio de 2021 con la casilla "Enviar campaña a usuarios en su zona horaria local" seleccionada.][4]

### Permitir que los usuarios puedan volver a recibir la campaña

| Definición | Zona horaria |
| ---------- | --------- |
| Después de que un usuario reciba un mensaje de esta campaña, especifique cuándo volverá a ser elegible para recibir la campaña de nuevo. [Más información]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/). | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con la casilla de verificación "Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña" seleccionada después de una semana.][5]

## Entrega basada en la acción

En esta sección se tratan las opciones de retraso y entrega para las campañas de [entrega basadas en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

### Planificar retraso

{% alert important %}
Cuando elijas la duración del retraso, ten en cuenta que si estableces un retraso superior a [la duración de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) la campaña, tus usuarios no recibirán tu campaña.
{% endalert %}

#### Enviar campaña inmediatamente

| Definición | Zona horaria |
| ---------- | --------- |
| Enviar mensaje inmediatamente después de que el usuario realice la acción desencadenante. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Retraso de programación establecido para enviar la campaña inmediatamente después de que se produzca el evento desencadenante.][6]

#### Enviar campaña al cabo de X días

| Definición | Zona horaria |
| ---------- | --------- |
| Enviar mensaje después de un retraso. Puede especificar un retraso en segundos, minutos, horas, días o semanas. Para [las campañas de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), puedes establecer un retraso de hasta dos horas solamente. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Retraso de programación establecido para enviar la campaña un día después de que se produzca el evento desencadenante.][7]

#### Enviar campaña el próximo [día de la semana] a X hora

| Definición | Zona horaria |
| ---------- | --------- |
| Enviar mensaje el siguiente día de la semana especificado, a una hora del día seleccionada. | Seleccione entre **la hora local del usuario** o **la hora de la empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por ejemplo, supongamos que selecciona "Enviar el sábado siguiente a las 15:15". Si un usuario realiza el evento desencadenante un sábado, recibiría ese mensaje el sábado siguiente dentro de siete días. Si entran un viernes, el sábado siguiente sería en un día.

![][8]

#### Enviar en X días naturales a la hora Y

| Definición | Zona horaria |
| ---------- | --------- |
| Envía un mensaje en un número determinado de días a una hora especificada. | Seleccione entre la **hora local del usuario** o **la hora de la empresa** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze calcula el retraso como `day of the week` + `calendar days`, y luego añade el `time`. Por ejemplo, supongamos que el usuario desencadena el evento el lunes a las 21:00, y el retraso de programación se establece en "Enviar campaña en 1 día a las 9:00". Ese mensaje se entregará el martes a las 9 de la mañana porque Braze calcula el retraso como `Monday` + `1 calendar day` y luego añade `9 am`.

![][9]

### Horas tranquilas

| Definición | Zona horaria |
| ---------- | --------- |
| Impedir el envío de mensajes durante las horas especificadas. Si un mensaje se activa durante las Horas de Silencio, puede elegir entre cancelar el mensaje o enviarlo en el siguiente momento disponible (por ejemplo, enviarlo al final de sus Horas de Silencio). | Hora local del usuario. Si la zona horaria de un usuario no está configurada, se utilizará la zona horaria de la empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con las horas de silencio activadas. En este ejemplo, los mensajes no se enviarán entre las 12 de la mañana y las 8 de la mañana en la hora local del usuario. Si se desencadena un mensaje durante las horas tranquilas, el mensaje se enviará a la siguiente hora disponible.][10]

### Permitir que los usuarios vuelvan a ser elegibles para recibir campañas

| Definición | Zona horaria |
| ---------- | --------- |
| Después de que un usuario reciba un mensaje de esta campaña, especifique cuándo [volverá a ser elegible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña de nuevo. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Una campaña con la casilla de verificación "Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña" seleccionada después de una semana.][5]

### Limitación global de frecuencias

| Definición | Zona horaria |
| ---------- | --------- |
| Limite el número de veces que cada usuario debe recibir la campaña en un plazo determinado, que puede medirse en minutos, días, semanas (7 días) y meses. Para más información, consulte la sección [de limitación de frecuencias]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Hora local del usuario. Si la zona horaria de un usuario no está configurada, se utilizará la zona horaria de la empresa. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por defecto, la limitación de frecuencia está desactivada para los nuevos lienzos. La limitación de frecuencias se aplica en el nivel de escalón, no en el nivel de entrada del lienzo.

La limitación de la frecuencia se basa en días naturales, no en un periodo de 24 horas. Esto significa que podrías establecer una regla de limitación de frecuencia de envío de no más de una campaña al día, pero si un usuario recibe un mensaje a las 11 de la noche en su hora local, todavía puede recibir otro mensaje una hora más tarde (en la medianoche del siguiente día natural). 

## Plazo de conversión

| Definición | Zona horaria |
| ---------- | --------- |
| Tiempo máximo que puede transcurrir entre que un usuario recibe una campaña y realiza la acción asignada para que se considere una conversión. Para más información, consulta los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
