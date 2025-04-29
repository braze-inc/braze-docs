---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 2
description: "Este artículo ofrece un resumen de Intelligent Timing (antes Entrega Inteligente) y de cómo puedes aprovechar esta característica en tus campañas y Lienzos."

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Utiliza Intelligent Timing para entregar tu mensaje a cada usuario cuando Braze determine que es más probable que ese usuario interactúe (abra o haga clic), lo que se conoce como su hora óptima de envío. Esto te facilita comprobar que estás enviando mensajes a tus usuarios a su hora preferida, lo que puede conducir a una mayor interacción.

## Casos prácticos

- Envía campañas recurrentes sin límite de tiempo
- Automatización de campañas con usuarios de múltiples zonas horarias
- Cuando envíes mensajes a tus usuarios más interactivos (ellos tendrán la mayor cantidad de datos de interacción)

## Cómo funciona

Braze calcula la hora óptima de envío basándose en un análisis estadístico de las interacciones anteriores de tus usuarios con tu aplicación, y de sus interacciones con cada canal de mensajería. Se utilizan los siguientes datos de interacción: 

- Horario de las sesiones
- Push Direct Opens
- Push Influenced Opens
- Clics en correos electrónicos
- Aperturas de correo electrónico (excluyendo [aperturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens))

Por ejemplo, Sam puede abrir tus correos electrónicos por la mañana con regularidad, pero abre tu aplicación e interactúa con las notificaciones por la tarde. Eso significa que Sam recibiría una campaña por correo electrónico con Intelligent Timing por la mañana, mientras que recibiría campañas con notificaciones push por la tarde, cuando es más probable que interactúe.

Si un usuario no tiene suficientes datos de interacción para que Braze calcule la hora de envío óptima, puedes especificar una [hora alternativa](#fallback-time).

## Utilizar Intelligent Timing

Esta sección describe cómo configurar Intelligent Timing para tus campañas y Lienzos.

### Campañas

Para utilizar Intelligent Timing en tus campañas:

1. Crea una campaña y redacta tu mensaje.
2. Selecciona **Entrega programada** como tipo de entrega.
3. En **Opciones de programación temporal**, selecciona **Temporización inteligente**.
4. Selecciona la fecha de envío. Consulta las consideraciones sobre [los matices de la campaña](#campaign-nuances).
5. Determina si [sólo quieres enviar mensajes en horas concretas](#sending-within-specific-hours).
6. Especifica una [hora de alternativa](#fallback-time). En este momento se enviará el mensaje si el perfil de un usuario no tiene suficientes datos para calcular un tiempo óptimo.

![Programar una campaña con Intelligent Timing][1]

#### Envío de mensajes en horas concretas {#sending-within-specific-hours}

Si lo deseas, puedes elegir limitar el tiempo óptimo a una ventana de tiempo concreta. Esto es útil si tu campaña se refiere a un acontecimiento, venta o promoción específicos, pero generalmente no se recomienda en otros casos. Enviar dentro de unas horas concretas funciona de forma similar a las Horas Tranquilas, que no se recomienda con Intelligent Timing, ya que es contraproducente. Para más información, consulta la sección de este artículo sobre [limitaciones](#limitations).

1. Al configurar Intelligent Timing, selecciona **Sólo enviar mensajes en horas concretas**.
2. Introduce la hora de inicio y fin de la ventana de entrega.

![Casilla de verificación para "Enviar mensajes sólo en horas específicas" seleccionada, donde la ventana de tiempo se establece entre las 8 am y las 12 am en la hora local del usuario.][4]

Cuando se especifica una ventana de entrega, Braze sólo tiene en cuenta los datos de interacción dentro de la ventana para determinar la hora óptima de un usuario. Si no hay suficientes datos de interacción dentro de esa ventana, el mensaje se envía a la [hora alternativa](#fallback-time) especificada.

#### Vista previa de los plazos de entrega

Para ver una estimación de cuántos usuarios recibirán el mensaje en cada hora del día, utiliza el gráfico de vista previa (sólo campañas).

1. Añade segmentos o filtros en el paso Audiencias objetivo.
2. En la sección **Vista previa de horas de entrega para** (que aparece tanto en los pasos Audiencias objetivo como en Programar entrega), selecciona tu canal.
3. Haz clic en **Actualizar datos**.

![][2]

Siempre que cambies cualquier configuración sobre Intelligent Timing o la audiencia de tu campaña, actualiza de nuevo los datos para ver un gráfico actualizado.

El gráfico muestra en azul a los usuarios que tenían datos suficientes para calcular una hora óptima y en rojo a los usuarios que utilizarán la hora alternativa. Utiliza los filtros de cálculo para ajustar la vista previa y obtener una visión más granular de cualquiera de los grupos de usuarios.

#### Matices de la campaña

He aquí algunos matices que debes tener en cuenta al programar campañas con Intelligent Timing.

##### Lanzamiento de la campaña

Lanza tu campaña al menos 48 horas antes de la fecha de envío programada. Esto se debe a las variaciones en las zonas horarias. Braze calcula la hora óptima a medianoche en la hora de Samoa (UTC+13), uno de los primeros husos horarios del mundo. Un solo día abarca unas 48 horas en todo el mundo, lo que significa que si lanzas una campaña dentro de ese margen de 48 horas, es posible que la hora óptima de un usuario ya haya pasado en su zona horaria, y el mensaje no se envíe.

{% alert important %}
Si se lanza una campaña y el tiempo óptimo de un usuario es inferior a una hora en el pasado, el mensaje se envía inmediatamente. Si la hora óptima ha pasado más de una hora, el mensaje no se envía.
{% endalert %}

##### Elección de segmentos

Si te diriges a una audiencia que ha realizado una acción en un periodo de tiempo determinado, deja al menos un margen de 3 días en tus filtros de segmento. Por ejemplo, en lugar de `First used these apps more than 1 day ago` y `First used these apps less than 3 days ago`, utiliza 1 día y 4 días.

![Filtros para la audiencia objetivo donde la campaña se dirige a los usuarios que utilizaron por primera vez estas aplicaciones hace entre 1 y 4 días.][3]

Esto también se debe a las zonas horarias: seleccionar un periodo inferior a 3 días puede hacer que algunos usuarios salgan del segmento antes de alcanzar su hora óptima de envío.

Más información sobre [cuándo comprueba Braze los criterios de elegibilidad para segmentos y filtros]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

##### Pruebas A/B con optimizaciones

Si aprovechas [las pruebas A/B con una optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como el envío automático de la variante ganadora una vez finalizada la prueba A/B, la duración de la campaña aumentará. Por defecto, las campañas de Intelligent Timing enviarán la variante ganadora a los usuarios restantes al día siguiente de la prueba inicial, pero puedes cambiar esta fecha de envío.

Te recomendamos que, si utilizas tanto Intelligent Timing como pruebas A/B, programes el envío de la variante ganadora 2 días después de la prueba inicial, en lugar de 1 día.

![Sección Pruebas A/B del paso Audiencias objetivo donde finaliza la prueba y envía la Variante ganadora dos días después de que comience la prueba inicial.][5]

### Canvas

Esta sección describe cómo utilizar Intelligent Timing en tus Lienzos. Los pasos varían ligeramente dependiendo del flujo de trabajo Canvas que estés utilizando.

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear ni duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona Intelligent Timing en el editor original.<br><br>Braze recomienda a los clientes que utilicen la experiencia original de Canvas que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los Lienzos. Más información sobre la [clonación de tus lienzos en el flujo de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

{% tabs %}
{% tab Flujo Canvas %}

En el Flujo Canvas, Intelligent Timing se configura en los pasos de Mensaje. Para utilizar Intelligent Timing en tu Canvas:

1. Añade un [paso en Canvas con un mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).
2. Ve a **Configuración de la entrega**.
3. Selecciona **Utilizar Intelligent Timing**.
4. Especifica una [hora de alternativa](#fallback-time).

Un usuario que entre en este paso recibirá el mensaje a la hora óptima del día en que entre SI esa hora aún no ha pasado. Ten en cuenta que si la hora óptima de un usuario (en hora local) ha pasado el día en que introduce un paso de mensaje, se enviará al día siguiente a la hora óptima. Los pasos de mensajes que se dirigen a varios canales pueden enviar o intentar enviar mensajes en momentos diferentes para canales diferentes. Cuando se intenta enviar el primer mensaje en un paso de Mensajería, se avanza automáticamente a todos los usuarios.

#### Pasos de retardo y Temporización Inteligente

Cuando utilices Intelligent Timing después de un [paso de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) Retraso, la fecha de entrega puede ser diferente dependiendo de cómo calcules el retraso. Esto sólo se aplica cuando tu retraso está configurado para **Después de una duración**, ya que hay una diferencia entre cómo se calculan los "días" y los "días de calendario".

- **Días:** 1 día son 24 horas, calculadas desde que el usuario entra en el paso Retraso.
- **Días del calendario:** 1 día es el periodo que transcurre desde que el usuario introduce el paso Retraso hasta medianoche en su zona horaria. Esto significa que 1 día natural puede ser tan corto como unos minutos.

Cuando utilices Intelligent Timing, te recomendamos que utilices días naturales para tus retrasos en lugar de días de 24 horas. Esto se debe a que con los días del calendario, el mensaje se enviará el último día del retraso, a la hora óptima. Con un día de 24 horas, existe la posibilidad de que la hora óptima del usuario sea antes de entrar en el paso, lo que significa que se añadirá un día más a su retraso.

Por ejemplo, supongamos que la hora óptima de Luka son las 14:00 h. Entra en el paso Retraso a las 14:01 del 1 de marzo, y el retraso se establece en 2 días.

- El día 1 termina el 2 de marzo a las 14:01 h
- El día 2 termina el 3 de marzo a las 14:01 horas

Sin embargo, Intelligent Timing está configurado para entregar a las 14 h, que ya ha pasado. Así que Luka no recibirá el mensaje hasta el día siguiente: 4 de marzo a las 14:00 h.

![Gráfico que muestra la diferencia entre días y días de calendario, en el que si la hora óptima de un usuario son las 14:00, pero entra en el paso de retraso a las 14:01 y el retraso se establece en 2 días. Días entrega el mensaje 3 días más tarde porque el usuario entró en el paso después de su hora óptima, mientras que días calendario entrega el mensaje 2 días más tarde, en el último día de retraso.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab Flujo de trabajo de Original Canvas %}

En el flujo de trabajo original de Canvas, Intelligent Timing se establece en la sección de retardo de un Paso Completo. Para utilizar Intelligent Timing en tu Canvas:

1. Añade un paso en Canvas.
2. Abre el **Retraso** de tu paso.
3. Selecciona **Programado**.
4. Establece un retardo utilizando *después*, *dentro* o *a continuación*.
   - Si seleccionas *después*, establece el retraso en días o semanas. Los retrasos se calculan automáticamente utilizando días del calendario, lo que significa que el mensaje se envía el último día del retraso a la hora óptima del usuario. Intelligent Timing no está disponible para retrasos inferiores a 1 día.
5. Selecciona **Utilizar Intelligent Timing**.
6. Especifica una [hora de alternativa](#fallback-time).

{% endtab %}
{% endtabs %}

#### Iniciar el Canvas

A diferencia de las campañas, no tienes que preocuparte de lanzar tu Canvas 48 horas antes de la fecha de envío. Esto se debe a que la Temporización Inteligente se establece en el nivel del paso, no en el nivel del Canvas. En su lugar, recomendamos que haya al menos un retraso de 48 horas entre que el usuario entra en el Canvas y recibe el paso en el que se utiliza Intelligent Timing.

### Tiempo de alternativa {#fallback-time}

Tienes que elegir una hora alternativa para el envío del mensaje a los usuarios de tu audiencia que no tengan suficientes datos de interacción para que Braze calcule una hora de envío óptima. Hay dos opciones:

- el momento más popular para utilizar la aplicación entre todos los usuarios
- una hora alternativa personalizada concreta (en la zona horaria local del usuario)

#### Hora de la aplicación más popular

La hora más popular de la aplicación viene determinada por la hora media de inicio de sesión de tu espacio de trabajo (en hora local). Este tiempo se muestra en rojo en el [gráfico de vista previa](#preview-delivery-times) (sólo campañas).

Para las campañas, si especificaste una [ventana de entrega](#sending-within-specific-hours) y el momento más popular para utilizar tu aplicación cae fuera de esa ventana, el mensaje se enviará más cerca del borde de la ventana de entrega. Por ejemplo, si tu ventana de entrega es de 13:00 a 20:00 y la hora más popular de la aplicación es las 22:00, el mensaje se enviará a las 20:00.

**No hay suficientes datos de la sesión**<br>
En el raro caso de que tu aplicación no tenga suficientes datos de sesión para calcular cuándo se utiliza más la aplicación (una aplicación completamente nueva sin datos), el mensaje se enviará a las 5 de la tarde en la zona horaria local del usuario. Si se desconoce la hora local del usuario, se enviará a las 17:00 en la zona horaria de tu empresa.

Es importante ser consciente de las limitaciones de utilizar el Intelligent Timing al principio del ciclo de vida de un usuario, cuando se dispone de datos limitados. Puede seguir siendo valioso, ya que incluso los usuarios con pocas sesiones grabadas pueden ofrecer información sobre su comportamiento. Sin embargo, Braze puede calcular más eficazmente la hora óptima de envío más adelante en el ciclo de vida del usuario.

#### Tiempo de alternativa personalizado

Utiliza la hora alternativa personalizada para elegir una hora diferente para enviar el mensaje. De forma similar a la hora de la aplicación más popular, el mensaje se enviará a la hora alternativa de la zona horaria local del usuario. Si se desconoce la zona horaria local del usuario, se enviará en la zona horaria de tu empresa.

Para las campañas con una hora alternativa personalizada especificada, si lanzas la campaña dentro de las 24 horas siguientes a la fecha de envío, los usuarios cuyas horas óptimas ya hayan pasado recibirán la campaña a la hora alternativa personalizada. Si la hora alternativa personalizada ya ha pasado en su zona horaria, el mensaje se enviará inmediatamente.

## Limitaciones

- Los mensajes dentro de la aplicación, las tarjetas de contenido y los webhooks se entregan inmediatamente y no se les da un tiempo óptimo.
- Intelligent Timing no está disponible para campañas basadas en acciones o desencadenadas por API.
- Intelligent Timing no debe utilizarse en los siguientes casos:
    - **Horas tranquilas:** Utilizar tanto las Horas tranquilas como la Temporización inteligente es contraproducente, ya que las Horas tranquilas se basan en una suposición descendente sobre el comportamiento de los usuarios, como no enviar mensajes a alguien en mitad de la noche, mientras que la Temporización inteligente se basa en la actividad de los usuarios. Puede que Sam compruebe mucho las notificaciones de su aplicación a las 3 de la madrugada. No juzgamos.
    - **Límite de velocidad:** Si se utilizan tanto el límite de tasa como el Intelligent Timing, no hay garantías sobre cuándo se entregará el mensaje. Las campañas recurrentes diarias con Intelligent Timing no admiten con precisión un tope total de envío de mensajes.
    - **Campañas de calentamiento de IP:** Algunos comportamientos de Intelligent Timing pueden causar dificultades para alcanzar los volúmenes diarios necesarios cuando estás calentando tu IP por primera vez. Esto se debe a que Intelligent Timing evalúa los segmentos dos veces: una vez cuando se crea por primera vez la campaña o el Canvas, y otra vez antes de enviarlos a los usuarios para verificar que deben seguir estando en ese segmento. Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

## Solución de problemas

### Gráfico de vista previa que muestra pocos usuarios con tiempos óptimos

Braze necesita una cierta cantidad de datos de interacción para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura (como los nuevos usuarios), Braze predeterminará el tiempo de espera. Dependiendo de tu configuración, podría ser la hora de la aplicación más popular o una hora alternativa personalizada.

### Envío fuera de plazo

Tu campaña de Intelligent Timing podría estar enviándose más allá de la fecha programada si estás aprovechando las [pruebas A/B con una optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Las campañas que utilizan optimizaciones de pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba inicial, lo que aumenta la duración de la campaña. Por defecto, las campañas con una optimización enviarán la variante ganadora a los usuarios restantes al día siguiente de la prueba inicial, pero puedes cambiar esta fecha de envío.

Si utilizas Intelligent Timing, te recomendamos dejar más tiempo para que finalice la prueba A/B y programar el envío de la Variante Ganadora para 2 días después de la prueba inicial en lugar de 1 día.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
