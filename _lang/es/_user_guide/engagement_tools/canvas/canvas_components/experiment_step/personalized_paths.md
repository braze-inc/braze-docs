---
nav_title: Caminos personalizados
article_title: Rutas personalizadas en Rutas de experimentos 
page_type: reference
description: "Las rutas personalizadas te permiten personalizar cualquier punto del recorrido de Canvas para usuarios individuales en función de la probabilidad de conversión."
tool: Canvas
---

# Rutas personalizadas en Rutas de experimentos

> Los Trayectos personalizados son similares a [la Variante personalizada]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) en las campañas y te permiten personalizar cualquier punto de un trayecto de Canvas para usuarios individuales en función de la probabilidad de conversión.

## Cómo funcionan los Caminos Personalizados

Cuando se activan las Rutas personalizadas en un paso de ruta de experimentos, el comportamiento es ligeramente diferente dependiendo de si tu Canvas está configurado para enviarse una vez o para repetirse:

- **Canvas de envío único:** Un grupo de usuarios es retenido en un grupo de retraso. Los usuarios restantes pasan a una prueba inicial para entrenar un modelo de predicción durante un tiempo que tú configures: al menos 24 horas para obtener los mejores resultados. Tras la prueba, se crea un modelo para saber qué comportamientos del usuario se asociaron a una mayor probabilidad de conversión en una ruta determinada. Por último, se envía a cada usuario del grupo de retraso por el camino que tiene más probabilidades de dar lugar a una conversión para él, basándose en los comportamientos que muestra y en lo que el modelo predictivo aprendió durante la prueba inicial.
- **Lienzos recurrentes, desencadenantes de acciones y desencadenantes de API:** Se realiza un experimento inicial con todos los usuarios que entran en la Ruta de experimentos durante una ventana especificada. Para mantener la integridad del experimento, si un usuario recibe varios mensajes antes de que finalice la ventana, se le asignará cada vez a la misma variante. Después de la ventana de experimentos, se envía a cada usuario por la ruta que tenga más probabilidades de resultar en una conversión para él.

## Utilizar rutas personalizadas

### Paso 1: Añadir una ruta de experimentos

Añade una [Ruta de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) a tu Canvas y, a continuación, activa **las Rutas personalizadas**.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Paso 2: Configurar los ajustes de las Rutas Personalizadas

Especifica el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración de Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Si eliges aperturas o clics como evento de conversión, asegúrate de que el primer paso de la ruta sea un [paso de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). Braze sólo cuenta la interacción a partir del primer paso de Mensaje en cada ruta respectiva. Si la ruta comienza con un paso diferente (como un paso de Retraso o de Ruta de audiencia) y el mensaje llega más tarde, ese mensaje no se incluirá al evaluar el rendimiento.

A continuación, configura la **Ventana de Experimento**. La **Ventana de Experimentos** determina durante cuánto tiempo se enviará a los usuarios por todas las rutas antes de elegir la mejor ruta para cada usuario del grupo de retraso. La ventana comienza cuando el primer usuario entra en el paso.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Paso 3: Determinar la alternativa

Por predeterminado, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los usuarios futuros serán enviados por la única ruta con mejor rendimiento.

Alternativamente, puedes seleccionar **Continuar enviando a todos los futuros usuarios la mezcla de rutas**.

\![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Esta opción enviará a los futuros usuarios por la mezcla de rutas según los porcentajes especificados en la distribución de rutas de experimentos.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Paso 4: Añade tus rutas y lanza el Canvas

{% tabs local %}
{% tab Single-send Canvas %}

Un único componente Ruta de experimentos puede contener hasta cuatro rutas. Sin embargo, para los Lienzos de un solo envío, puedes añadir hasta tres rutas cuando las Rutas personalizadas están activadas. La cuarta ruta debe reservarse para el Grupo de Retraso que Braze añade automáticamente a tu experimento.

Termina de configurar tu Canvas como necesites, y luego lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Cuando pase la ventana del experimento y éste se complete, Braze enviará a los usuarios del grupo de retraso a sus respectivas rutas con la mayor probabilidad personalizada de conversión basada en la recomendación del modelo predictivo.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Recurring or action-triggered or API-triggered Canvas %}

Puedes probar hasta cuatro rutas en una única Ruta de experimentos. Añade tus rutas y termina de configurar tu Canvas como necesites, luego lánzalo.  

Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Cuando pase la ventana del experimento y éste se haya completado, todos los usuarios posteriores que entren en el Canvas serán enviados por la ruta que tenga más probabilidades de dar lugar a una conversión para ellos.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análisis {#analytics}

Si se activaron las rutas personalizadas, tu vista de análisis se separa en dos pestañas: **Rutas de****experimentos iniciales** y **personalización**.

{% tabs local %}
{% tab Initial Experiment %}

La pestaña **Experimento inicial** muestra las métricas de cada ruta durante la ventana de experimentos. Puedes ver un resumen del rendimiento de todas las rutas para los eventos de conversión especificados.

\![Resultados de un experimento inicial enviado para determinar la ruta de mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada ruta en función de varias métricas para el canal de destino.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Por defecto, la prueba busca asociaciones entre los eventos personalizados del usuario y sus preferencias de ruta, o la variante de mensaje a la que mejor responde un usuario. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a una ruta concreta. Estas relaciones se utilizan después para determinar a qué usuarios se asigna cada ruta de experimentos una vez transcurrida la ventana de experimentos.

Las relaciones entre los eventos personalizados y las preferencias de ruta se muestran en la tabla de la pestaña **Experimento inicial**.

\![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de ruta, la prueba volverá a un método de análisis basado en la sesión.

{% details Fallback analysis method %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar rutas personalizadas, la pestaña **Experimento inicial** muestra un desglose de las variantes preferidas por los usuarios en función de una combinación de determinadas características.

Estas características son:

- **Recencia:** Cuándo fue la última vez que tuvieron una sesión
- **Frecuencia:** Con qué frecuencia tienen sesiones
- **Tenencia:** Cuánto tiempo llevan siendo usuarios

\![La tabla de características de los usuarios, que muestra qué usuarios se prevé que prefieran la Ruta 1 y la Ruta 2 en función de los tres contenedores en los que se encuentran por antigüedad, frecuencia y permanencia.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Piensa en la frecuencia como la frecuencia con la que interactúan contigo, y en la permanencia como el tiempo total que llevan interactuando contigo. Agrupamos a los usuarios en "cubos" en función de estas tres cosas (como se explica en la tabla de **Características de los usuarios** ) y luego vemos a qué cubo le gusta más qué ruta. Es como clasificar a los usuarios en cientos de listas diferentes en función de cuándo compraron contigo por última vez, con qué frecuencia compran y cuánto tiempo llevan siendo clientes.

A la hora de elegir un mensaje para un usuario, Braze examina los contenedores en los que se encuentra. Cada contenedor ejerce una influencia distinta en la selección de rutas para los usuarios. Cuantificamos esta influencia utilizando un método estadístico llamado [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression), que es una forma de predecir el comportamiento futuro basándose en acciones pasadas. Este método tiene en cuenta las interacciones del usuario durante el envío inicial del mensaje. Esta tabla sólo resume los resultados mostrando la ruta con la que los usuarios de cada contenedor tendían a interactuar.

En última instancia, Braze combina todos estos datos para seleccionar una ruta de mensajes personalizada para cada usuario, para asegurarse de que sea lo más atractiva y relevante posible para ellos.

{% alert note %}
Los intervalos de tiempo de cada contenedor se determinan en función de los datos de usuario específicos de Canvas, que pueden variar de un Canvas a otro.
{% endalert %}

**Cómo se seleccionan las rutas personalizadas**<br>
Con este método, el mensaje recomendado a un usuario individual es la suma de los efectos de su recencia, frecuencia y permanencia específicas. La recurrencia, la frecuencia y la permanencia se dividen en contenedores, como se ilustra en la tabla **Características del usuario**. El intervalo de tiempo de cada contenedor viene determinado por los datos de los usuarios de cada Canvas individual y cambiará de un Canvas a otro.

Cada contenedor puede tener una contribución o "push" diferente hacia cada camino. La fuerza del push para cada contenedor se determina a partir de las respuestas de los usuarios en el experimento inicial mediante [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla sólo resume los resultados mostrando la ruta con la que los usuarios de cada contenedor tendían a interactuar. La Trayectoria Personalizada real de cualquier usuario individual depende de la suma de los efectos de los tres contenedores en los que se encuentra: uno por cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Paths %}

La pestaña **Rutas personalizadas** muestra los resultados del experimento final, en el que los usuarios del Grupo de Retraso fueron enviados por la ruta de mejor rendimiento para ellos.

Las tres tarjetas de esta página muestran tu ascensor proyectado, los resultados globales y los resultados proyectados si en lugar de eso enviaras sólo la Senda Ganadora. Incluso si no hay subida, lo que a veces puede ocurrir, el resultado es el mismo que enviar sólo la ruta ganadora (una prueba A/B tradicional).

- **Ascensor proyectado:** La mejora en tu evento de conversión seleccionado debido al uso de rutas personalizadas en lugar de enviar a cada usuario por la ruta general de mejor rendimiento.
- **Resultados globales:** Los resultados del segundo envío basados en tu evento de conversión.
- **Resultados previstos:** Los resultados previstos del segundo envío en función de la métrica de optimización que hayas elegido, si en lugar de eso hubieras enviado sólo la variante ganadora.

\![Pestaña de rutas personalizadas para un Canvas. Las tarjetas muestran el Ascenso Proyectado, las Conversiones Globales (con Rutas Personalizadas) y las Aperturas Únicas Proyectadas (con Ruta Ganadora).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Uso de rutas personalizadas con entrega según la zona horaria local

No recomendamos utilizar la entrega según la zona horaria local en Lienzos con rutas personalizadas. Esto se debe a que las ventanas de experimentación comienzan cuando pasa el primer usuario. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y desencadenar el inicio de la ventana del experimento mucho antes de lo que esperas, lo que puede dar lugar a que el experimento concluya antes de que el grueso de tus usuarios en zonas horarias más típicas haya tenido tiempo suficiente para entrar en el Canvas y convertirse.

Alternativamente, si deseas utilizar la entrega local, utiliza una ventana de experimentación de 24-48 horas o más. De este modo, los usuarios de zonas horarias tempranas entran en el Canvas y desencadenan el inicio del experimento, pero queda mucho tiempo en la ventana del experimento. Los usuarios que se encuentren en zonas horarias más tardías aún tendrán tiempo suficiente para entrar en el Canvas y en el Paso de experimentos con rutas personalizadas y, posiblemente, convertirse antes de que expire la ventana del experimento.

