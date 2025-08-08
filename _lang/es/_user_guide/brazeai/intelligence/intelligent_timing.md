---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artículo ofrece un resumen de Intelligent Timing (antes Entrega Inteligente) y de cómo puedes aprovechar esta característica en tus campañas y Lienzos."

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Utiliza Intelligent Timing para entregar tu mensaje a cada usuario cuando Braze determine que es más probable que ese usuario interactúe (abra o haga clic), lo que se conoce como su hora óptima de envío. Esto te facilita comprobar que estás enviando mensajes a tus usuarios a su hora preferida, lo que puede conducir a una mayor interacción.

## Acerca de Intelligent Timing

Braze calcula la hora óptima de envío basándose en un análisis estadístico de las interacciones anteriores de tus usuarios con tu aplicación, y de sus interacciones con cada canal de mensajería. Se utilizan los siguientes datos de interacción: 

- Horario de las sesiones
- Push Direct Opens
- Push Influenced Opens
- Clics en correos electrónicos
- Aperturas de correo electrónico (excluyendo [aperturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))

Por ejemplo, Sam puede abrir tus correos electrónicos por la mañana con regularidad, pero abre tu aplicación e interactúa con las notificaciones por la tarde. Eso significa que Sam recibiría una campaña por correo electrónico con Intelligent Timing por la mañana, mientras que recibiría campañas con notificaciones push por la tarde, cuando es más probable que interactúe.

Si un usuario no tiene suficientes datos de interacción para que Braze calcule la hora óptima de envío, puedes especificar una hora alternativa.

## Casos prácticos

- Envía campañas recurrentes sin límite de tiempo
- Automatización de campañas con usuarios de múltiples zonas horarias
- Cuando envíes mensajes a tus usuarios más interactivos (ellos tendrán la mayor cantidad de datos de interacción)

## Utilizar Intelligent Timing

Esta sección describe cómo configurar Intelligent Timing para tus campañas y Lienzos.

{% tabs local %}
{% tab Campaña %}
### Paso 1: Añadir Intelligent Timing

1. Crea una campaña y redacta tu mensaje.
2. Selecciona la **Entrega programada** como tipo de entrega.
3. En **Opciones de programación temporal**, selecciona **Temporización inteligente**.
4. Configura la frecuencia de entrada. Para envíos únicos, selecciona **Una vez** y elige una fecha de envío. Para los envíos recurrentes, selecciona **Diario**, **Semanal** o **Mensual** y configura las opciones de recurrencia. Consulta las [limitaciones](#limitations) para obtener más orientación.
5. Opcionalmente, configura [Horas tranquilas](#quiet-hours).
6. Especifica una [hora de alternativa](#campaign-fallback). En este momento se enviará el mensaje si el perfil de un usuario no tiene suficientes datos para calcular un tiempo óptimo.

![Pantalla de programación de campaña mostrando Intelligent Timing con hora alternativa y configuración de horas tranquilas]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Horas tranquilas {#quiet-hours}

Utiliza Horas tranquilas para impedir el envío de mensajes durante horas concretas. Esto es útil cuando quieres evitar enviar mensajes durante las primeras horas de la mañana o durante la noche, al tiempo que permites que Intelligent Timing determine la mejor ventana de entrega.

{% alert note %}
Horas tranquilas ha sustituido a la configuración **Sólo enviar en horas concretas**. En lugar de elegir cuándo se pueden enviar mensajes, ahora eliges cuándo no se deben enviar. Por ejemplo, para enviar mensajes entre las 16:00 y las 18:00, configura Horas tranquilas de 18:00 a 16:00 del día siguiente.
{% endalert %}

1. Selecciona **Habilitar horas tranquilas**.
2. Selecciona la hora de inicio y fin en la que **no** enviar mensajes.

![Horas tranquilas alternar activado con la hora de inicio y fin configurada para bloquear la entrega de mensajes durante la noche]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Cuando las horas tranquilas están activadas, Braze no enviará mensajes durante el periodo tranquilo, aunque coincida con la hora óptima de envío del usuario. Si la hora óptima de un usuario cae dentro de la ventana de silencio, el mensaje se enviará en su lugar en el borde más cercano de la ventana.

Por ejemplo, si las horas tranquilas están configuradas de 22:00 a 6:00, y la hora óptima de un usuario son las 5:30, Braze retendrá el mensaje y lo entregará a las 6:00, la hora más cercana fuera de la ventana tranquila.

#### Vista previa de los plazos de entrega

Para ver una estimación de cuántos usuarios recibirán el mensaje en cada hora del día, utiliza el gráfico de vista previa (sólo campañas).

1. Añade segmentos o filtros en el paso Audiencias objetivo.
2. En la sección **Vista previa de horas de entrega para** (que aparece tanto en los pasos Audiencias objetivo como en Programar entrega), selecciona tu canal.
3. Haz clic en **Actualizar datos**.

![Gráfico de vista previa de entrega para Android Push que muestra la hora de máxima interacción entre las 12 y las 14 horas, siendo la hora más popular de la aplicación las 14 horas.]({% image_buster /assets/img/intel-timing-preview.png %})

### Paso 2: Elige una fecha de envío

A continuación, selecciona una fecha de envío para tu campaña. Ten en cuenta lo siguiente cuando programes campañas con Intelligent Timing:

#### Lanza la campaña con 48 horas de antelación

Lanza tu campaña al menos 48 horas antes de la fecha de envío programada. Esto se debe a las variaciones en las zonas horarias. Braze calcula la hora óptima a medianoche en la hora de Samoa (UTC+13), uno de los primeros husos horarios del mundo. Un solo día abarca unas 48 horas en todo el mundo, lo que significa que si lanzas una campaña dentro de ese margen de 48 horas, es posible que la hora óptima de un usuario ya haya pasado en su zona horaria, y el mensaje no se envíe.

{% alert important %}
Si se lanza una campaña y el tiempo óptimo de un usuario es inferior a una hora en el pasado, el mensaje se envía inmediatamente. Si la hora óptima ha pasado más de una hora, el mensaje no se envía.
{% endalert %}

#### Ventana de 3 días para filtrar segmentos

Si te diriges a una audiencia que ha realizado una acción en un periodo de tiempo determinado, deja al menos un margen de 3 días en tus filtros de segmento. Por ejemplo, en lugar de `First used app more than 1 day ago` y `First used app less than 3 days ago`, utiliza 1 día y 4 días.

![Filtros para la audiencia objetivo donde la campaña se dirige a los usuarios que utilizaron la aplicación por primera vez hace entre 1 y 4 días.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Esto también se debe a las zonas horarias: seleccionar un periodo inferior a 3 días puede hacer que algunos usuarios salgan del segmento antes de alcanzar su hora óptima de envío.

Para más información, consulta [FAQ: Intelligent Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Programar variantes ganadoras 2 días después de la prueba A/B

Si aprovechas [las pruebas A/B con una optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/), como el envío automático de la **variante ganadora** o el uso de una **variante personalizada**, Intelligent Timing puede afectar a la duración y el calendario de tu campaña.

Cuando utilices Intelligent Timing, te recomendamos programar la hora de envío de la variante ganadora al menos **2 días después de que** comience la prueba A/B. Por ejemplo, si tu prueba A/B comienza el 16 de abril a las 16:00, programa el envío de la variante ganadora no antes del 18 de abril a las 16:00. Esto da a Braze tiempo suficiente para evaluar el comportamiento del usuario y enviar mensajes en el momento óptimo.

![Secciones de pruebas A/B que muestran la prueba A/B con la variante ganadora seleccionada, con los criterios ganadores, la fecha de envío y la hora local de envío seleccionados]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Paso 3: Elige una ventana de entrega (opcional)

Opcionalmente, puedes elegir limitar la ventana de entrega. Esto puede ser útil si tu campaña pertenece a un evento, venta o promoción específicos, pero generalmente no se recomienda cuando se utiliza Intelligent Timing. Para más información, consulta las [limitaciones](#limitations).

Cuando se especifica, Braze sólo utiliza los datos de interacción dentro de esa ventana para determinar la hora óptima de entrega de un usuario. Si no hay suficientes datos de interacción dentro de esa ventana, el mensaje se envía a la hora alternativa que hayas establecido.

Para configurar una ventana de entrega:

1. Al configurar Intelligent Timing, selecciona **Sólo enviar mensajes en horas concretas**.
2. Introduce la hora de inicio y fin de la ventana de entrega.

![Casilla de verificación para "Sólo enviar mensajes dentro de horas específicas" seleccionada, donde la ventana de tiempo se establece entre las 8 am y las 12 am en la hora local del usuario.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Paso 4: Elige una hora alternativa {#campaign-fallback}

Elige una hora alternativa para utilizar si el perfil de un usuario no tiene suficientes datos para calcular una hora de entrega óptima.

![Programar una campaña con Intelligent Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Paso 5: Vista previa de los plazos de entrega

Para ver una estimación de cuántos usuarios recibirán el mensaje en cada hora del día, utiliza el gráfico de vista previa.

1. Añade segmentos o filtros en el paso Audiencias objetivo.
2. En la sección **Vista previa de horas de entrega para** (que aparece tanto en los pasos Audiencias objetivo como en Programar entrega), selecciona tu canal.
3. Selecciona **Actualizar Datos**.

![Ejemplo de vista previa de los plazos de entrega para Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Siempre que cambies cualquier configuración sobre Intelligent Timing o la audiencia de tu campaña, actualiza de nuevo los datos para ver un gráfico actualizado.

El gráfico muestra en azul a los usuarios que tenían datos suficientes para calcular una hora óptima y en rojo a los usuarios que utilizarán la hora alternativa. Utiliza los filtros de cálculo para ajustar la vista previa y obtener una visión más granular de cualquiera de los grupos de usuarios.
{% endtab %}

{% tab Canvas %}
{% alert important %}
A partir del 28 de febrero de 2023, ya no se podrán crear ni duplicar lienzos que utilicen el editor original. Para saber cómo pasar al nuevo Flujo de Canvas, consulta [Clonar lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Paso 1: Añadir Intelligent Timing

En tu Canvas, añade un [paso en Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), luego ve a **Configuración de entrega** y selecciona **Utilizar Intelligent Timing**.

Los mensajes se enviarán a los usuarios que hayan entrado en el paso ese día a su hora local óptima. Sin embargo, si su hora óptima ya ha pasado ese día, en su lugar se entregará a esa hora durante el día siguiente. Los pasos de mensajes que se dirigen a varios canales pueden enviar o intentar enviar mensajes en momentos diferentes para canales diferentes. Cuando se intenta enviar el primer mensaje en un paso de Mensajería, se avanza automáticamente a todos los usuarios.

### Paso 2: Elige una hora alternativa

Elige una hora alternativa para enviar el mensaje a los usuarios de tu audiencia que no tengan suficientes datos de interacción para que Braze calcule una hora de envío óptima. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Paso 4: Añadir un paso de Retraso

A diferencia de lo que ocurre con las campañas, no necesitas lanzar tu Canvas 48 horas antes de la fecha de envío, porque el Intelligent Timing se establece en el nivel del paso, no en el del Canvas.

En su lugar, añade un [paso de Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) de al menos dos días naturales entre que el usuario entra en el Canvas y cuando recibe el paso de Intelligent Timing.

#### Calendario vs. Días de 24 horas

Cuando utilices Intelligent Timing después de un paso de Retraso, la fecha de entrega puede variar dependiendo de cómo calcules el retraso. Esto sólo se aplica cuando tu retraso está configurado para **Después de una duración**, ya que hay una diferencia entre cómo se calculan los "días" y los "días de calendario".

- **Días:** 1 día son 24 horas, calculadas desde que el usuario entra en el paso Retraso.
- **Días del calendario:** 1 día es el periodo que transcurre desde que el usuario introduce el paso Retraso hasta medianoche en su zona horaria. Esto significa que 1 día natural puede ser tan corto como unos minutos.

Cuando utilices Intelligent Timing, te recomendamos que utilices días naturales para tus retrasos en lugar de días de 24 horas. Esto se debe a que con los días del calendario, el mensaje se enviará el último día del retraso, a la hora óptima. Con un día de 24 horas, existe la posibilidad de que la hora óptima del usuario sea antes de entrar en el paso, lo que significa que se añadirá un día más a su retraso.

Por ejemplo, supongamos que la hora óptima de Luka son las 14:00 h. Entra en el paso Retraso a las 14:01 del 1 de marzo, y el retraso se establece en 2 días.

- El día 1 termina el 2 de marzo a las 14:01 h
- El día 2 termina el 3 de marzo a las 14:01 horas

Sin embargo, Intelligent Timing está configurado para entregar a las 14 h, que ya ha pasado. Así que Luka no recibirá el mensaje hasta el día siguiente: 4 de marzo a las 14:00 h.

![Gráfico que muestra la diferencia entre días y días de calendario, en el que si la hora óptima de un usuario son las 14:00, pero entra en el paso de retraso a las 14:01 y el retraso se establece en 2 días. Días entrega el mensaje 3 días más tarde porque el usuario entró en el paso después de su hora óptima, mientras que días calendario entrega el mensaje 2 días más tarde, en el último día de retraso.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Limitaciones

- Los mensajes dentro de la aplicación, las tarjetas de contenido y los webhooks se entregan inmediatamente y no se les da un tiempo óptimo.
- Intelligent Timing no está disponible para campañas basadas en acciones o desencadenadas por API.
- Intelligent Timing no debe utilizarse en los siguientes casos:
    - **Límite de velocidad:** Si se utilizan tanto el límite de tasa como el Intelligent Timing, no hay garantías sobre cuándo se entregará el mensaje. Las campañas recurrentes diarias con Intelligent Timing no admiten con precisión un tope total de envío de mensajes.
    - **Campañas de calentamiento de IP:** Algunos comportamientos de Intelligent Timing pueden causar dificultades para alcanzar los volúmenes diarios necesarios cuando estás calentando tu IP por primera vez. Esto se debe a que Intelligent Timing evalúa los segmentos dos veces: una vez cuando se crea por primera vez la campaña o el Canvas, y otra vez antes de enviarlos a los usuarios para verificar que deben seguir estando en ese segmento. Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

## Solución de problemas

### Gráfico de vista previa que muestra pocos usuarios con tiempos óptimos

Braze necesita una cierta cantidad de datos de interacción para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura (como los nuevos usuarios), Braze predeterminará el tiempo de espera. Dependiendo de tu configuración, podría ser la hora de la aplicación más popular o una hora alternativa personalizada.

### Envío fuera de plazo

Tu campaña de Intelligent Timing podría estar enviándose más allá de la fecha programada si estás aprovechando las [pruebas A/B con una optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Las campañas que utilizan optimizaciones de pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba inicial, lo que aumenta la duración de la campaña. Por defecto, las campañas con una optimización enviarán la variante ganadora a los usuarios restantes al día siguiente de la prueba inicial, pero puedes cambiar esta fecha de envío.

Si utilizas Intelligent Timing, te recomendamos dejar más tiempo para que finalice la prueba A/B y programar el envío de la Variante Ganadora para 2 días después de la prueba inicial en lugar de 1 día.

## Preguntas más frecuentes (FAQ) {#faq}

### General

#### ¿Qué predice el Intelligent Timing?

Intelligent Timing se centra en predecir cuándo es más probable que un usuario abra o haga clic en tus mensajes para garantizar que tus mensajes lleguen a los usuarios en los momentos óptimos de interacción.

#### ¿Se calcula el Intelligent Timing por separado para cada día de la semana?

No, el Intelligent Timing no está vinculado a días concretos. En su lugar, personaliza los tiempos de envío en función de los patrones de interacción únicos de cada usuario y del canal que estés utilizando, como el correo electrónico o las notificaciones push. Esto garantiza que tus mensajes lleguen a los usuarios cuando están más receptivos.

### Cálculos

#### ¿Qué datos se utilizan para calcular el tiempo óptimo para cada usuario?

Para calcular el tiempo óptimo, Intelligent Timing:

1. Analiza los datos de interacción de cada usuario registrados por el SDK de Braze. Esto incluye lo siguiente:
  - Horario de las sesiones
  - Push Direct Opens
  - Push Influenced Opens
  - Clics en el correo electrónico
  - Aperturas de correo electrónico (excluyendo aperturas de máquina)
2. Agrupa estos eventos por hora, identificando la hora de envío óptima para cada usuario.

#### ¿Se incluyen las Aperturas de Máquina al calcular el tiempo óptimo?

No, [las Aperturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) se excluyen de los cálculos del tiempo óptimo. Esto significa que los tiempos de envío se basan únicamente en la interacción real de los usuarios, lo que proporciona una sincronización más precisa para tus campañas.

#### ¿Cómo de preciso es el momento óptimo?

Intelligent Timing programa mensajes durante la "hora de mayor interacción" de cada usuario, basándose en los eventos de inicio de sesión y apertura de mensajes. Dentro de esa hora, la hora del mensaje se redondea a los cinco minutos más próximos. Por ejemplo, si la hora óptima de un usuario se calcula a las 16:58, el mensaje se programará para las 17:00. Puede haber ligeros retrasos en la entrega debido a la actividad del sistema durante los periodos de mayor actividad.

#### ¿Cuáles son los cálculos alternativos si no hay datos suficientes?

Si hay menos de cinco eventos relevantes para un usuario, Intelligent Timing utiliza la hora alternativa de tu configuración de mensajes. 

### Campañas

#### ¿Con cuánta antelación debo lanzar una campaña de Intelligent Timing para entregarla con éxito a todos los usuarios de todas las zonas horarias?

Braze calcula la hora óptima a medianoche en la hora de Samoa, uno de los primeros husos horarios del mundo. En un solo día, abarca aproximadamente 48 horas. Por ejemplo, alguien cuya hora óptima son las 12:01 de la mañana y vive en Australia ya ha pasado su hora óptima, y es "demasiado tarde" para enviársela. Por estas razones, necesitas programar con 48 horas de antelación para entregar con éxito a todas las personas del mundo que utilicen tu aplicación.

#### ¿Por qué mi campaña de Intelligent Timing muestra pocos o ningún envío?

Braze necesita un número base de puntos de datos para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura de correo electrónico (como los nuevos usuarios), Intelligent Timing puede predeterminar la hora más popular del espacio de trabajo en ese día de la semana. Si no hay suficiente información sobre el espacio de trabajo, volvemos a la hora predeterminada de las 17 h. También puedes elegir establecer una hora específica de alternativa.

#### ¿Por qué mi campaña de Intelligent Timing se envía pasada la fecha programada?

Puede que tu campaña de Intelligent Timing esté enviando más allá de la fecha programada porque estás aprovechando las pruebas A/B. Las campañas que utilizan pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba A/B, lo que aumenta la duración del envío de la campaña. Por defecto, las campañas de Intelligent Timing se programarán para enviar la variante ganadora a los usuarios restantes para el día siguiente, pero puedes cambiar esta fecha de envío.

Te recomendamos que, si tienes campañas con Intelligent Timing, dejes más tiempo para que finalice la prueba A/B y programes el envío de la variante ganadora para dentro de dos días en lugar de uno. 

### Funcionalidad

#### ¿Cuándo comprueba Braze los criterios de elegibilidad de los filtros de segmento y audiencia?

Braze realiza dos comprobaciones cuando se lanza una campaña:

1. **Comprobación inicial:** A medianoche en la primera zona horaria del día de envío.
2. **Comprobación de la hora programada:** Justo antes de enviar a la hora Intelligent Timing seleccionada por el usuario.

Ten cuidado al filtrar en función de otros envíos de campaña para evitar dirigirte a segmentos no elegibles. Por ejemplo, si enviaras dos campañas el mismo día para horas distintas, y añades un filtro que sólo permita a los usuarios recibir la segunda campaña si han recibido la primera, los usuarios no recibirán la segunda campaña. Esto se debe a que nadie era elegible cuando se creó la campaña y se formaron los segmentos.

#### ¿Puedo utilizar horas tranquilas en mi campaña de Intelligent Timing?

Las Horas tranquilas pueden utilizarse en una campaña que utilice Intelligent Timing. El algoritmo de Intelligent Timing evitará las horas tranquilas para seguir enviando el mensaje a todos los usuarios elegibles. Dicho esto, te recomendamos que desactives las Horas tranquilas, a menos que haya implicaciones legales, de cumplimiento de normas o de otro tipo sobre cuándo se pueden enviar mensajes y cuándo no.

#### ¿Qué ocurre si la hora óptima para un usuario está dentro de las horas tranquilas? 

Si la hora óptima determinada cae dentro de las Horas Tranquilas, Braze encuentra el límite más cercano de las Horas Tranquilas y programa el mensaje para la siguiente hora permitida antes o después de las Horas Tranquilas. El mensaje se pone en cola para enviarse en el límite más cercano de las horas tranquilas en relación con la hora óptima.

#### ¿Puedo utilizar Intelligent Timing y la limitación de tasas?

El límite de velocidad puede utilizarse en una campaña que utilice Intelligent Timing. Sin embargo, la naturaleza del límite de velocidad implica que algunos usuarios pueden recibir su mensaje en un momento que no sea el óptimo, sobre todo si un gran número de usuarios en relación con el tamaño del límite de velocidad están programados en el momento alternativo debido a la insuficiencia de datos. 

Recomendamos utilizar el límite de velocidad en una campaña de Intelligent Timing sólo cuando haya requisitos técnicos que deban cumplirse utilizando el límite de tasa.

#### ¿Puedo utilizar Intelligent Timing durante el calentamiento de IP?

Braze no recomienda utilizar Intelligent Timing cuando los usuarios estén calentando de IP por primera vez, ya que algunos de sus comportamientos pueden causar dificultades para alcanzar los volúmenes diarios. Esto se debe a que Intelligent Timing evalúa dos veces los segmentos de la campaña. Una vez cuando se construye la campaña por primera vez, y una segunda vez antes de enviarla a los usuarios para verificar que deben seguir estando en ese segmento.

Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

#### ¿Cómo se determina la hora de la aplicación más popular?

La hora de la aplicación más popular viene determinada por la hora media de inicio de sesión del espacio de trabajo (en hora local). Esta métrica se puede encontrar en el panel al previsualizar los tiempos de una campaña, se muestra en rojo.

#### ¿Tiene en cuenta el Intelligent Timing la apertura de la máquina?

Sí, las aperturas de la máquina son filtradas por Intelligent Timing, por lo que no influyen en su rendimiento.

#### ¿Cómo puedo asegurarme de que Intelligent Timing funciona lo mejor posible?

Intelligent Timing utiliza el historial individual de interacción con mensajes de cada usuario en cualquier momento en que haya recibido mensajes. Antes de utilizar Intelligent Timing, asegúrate de que has enviado mensajes a los usuarios a distintas horas del día. De ese modo, puedes "muestrear" cuándo puede ser el mejor momento para cada usuario. Un muestreo inadecuado de las distintas horas del día puede hacer que Intelligent Timing elija una hora de envío que no sea la óptima para un usuario.



