---
nav_title: Recorridos personalizados 
article_title: Recorridos personalizados en recorridos de experimentos 
page_type: reference
description: "Las rutas personalizadas le permiten personalizar cualquier punto del recorrido de Canvas para usuarios individuales en función de la probabilidad de conversión."
tool: Canvas
---

# Recorridos personalizados en recorridos de experimentos

> Personalized Paths es similar a [Personalized Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) en campañas y le permite personalizar cualquier punto de un recorrido Canvas para usuarios individuales basándose en la probabilidad de conversión.

## Cómo funciona Personalized Paths

Cuando se activan las Rutas Personalizadas en un paso de Ruta de Experimento, el comportamiento es ligeramente diferente dependiendo de si su Lienzo está configurado para enviarse una vez o para repetirse:

- **Canvas de envío único:** Un grupo de usuarios es retenido en un grupo de retraso. Los usuarios restantes pasan a una prueba inicial para entrenar un modelo similar durante el tiempo que usted configure (al menos 24 horas para obtener los mejores resultados). Tras la prueba, se crea un modelo para saber qué comportamientos de los usuarios se asociaron a una mayor probabilidad de conversión en una ruta determinada. Por último, se envía a cada usuario del grupo de retardo por el camino que tiene más probabilidades de resultar en una conversión para ellos, basándose en los comportamientos que muestran y en lo que el modelo de semejanza aprendió durante la prueba inicial.
- **Lienzos recurrentes, desencadenantes de acciones y desencadenantes de API:** Se realiza un experimento inicial con todos los usuarios que entran en la Ruta de Experimento durante una ventana especificada. Para mantener la integridad del experimento, si un usuario recibe varios mensajes antes de que termine la ventana, se le asignará la misma variante cada vez. Tras la ventana de experimentación, se envía a cada usuario por el camino que tiene más probabilidades de resultar en una conversión para él.

## Uso de rutas personalizadas

### Paso 1: Añadir una Ruta de Experimento

Añada una [Ruta de Experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) a su Lienzo y active **las Rutas Personalizadas**.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Paso 2: Configurar los ajustes de las rutas personalizadas

Especifique el evento de conversión que debe determinar el ganador. Si no hay eventos de conversión disponibles, vuelve al primer paso de la configuración de Canvas y [asigna eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Si elige un evento de conversión con aperturas o clics para determinar el ganador, sólo el primer paso de Mensaje en la ruta que genere aperturas o clics contribuirá a determinar el ganador. No se tienen en cuenta los pasos posteriores de la ruta.

A continuación, ajuste la **Ventana de Experimento**. La **Ventana de Experimento** determina cuánto tiempo se enviará a los usuarios por todos los caminos antes de elegir el mejor camino para cada usuario del grupo de retardo. La ventana comienza cuando el primer usuario entra en el paso.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Paso 3: Determinar la alternativa

Por defecto, si los resultados de la prueba no son suficientes para determinar un ganador estadísticamente significativo, todos los futuros usuarios serán enviados por el único camino con mejor rendimiento.

Alternativamente, puedes seleccionar **Continuar enviando a todos los futuros usuarios la mezcla de rutas**.

![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Esta opción enviará a los futuros usuarios por la mezcla de rutas según los porcentajes especificados en la distribución de rutas del experimento.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Paso 4: Añade tus rutas y lanza el Canvas

{% tabs local %}
{% tab Canvas de envío único %}

Un único componente Ruta de experimento puede contener hasta cuatro rutas. Sin embargo, para los lienzos de un solo envío, puede añadir hasta tres rutas cuando las rutas personalizadas están activadas. La cuarta ruta debe reservarse para el grupo de retardo que Braze añade automáticamente a su experimento.

Termina de configurar tu Canvas como necesites y lánzalo. Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Cuando pase la ventana del experimento y éste haya finalizado, Braze enviará a los usuarios del grupo de retraso a sus respectivas rutas con la mayor probabilidad personalizada de conversión basada en la recomendación del modelo de semejanza.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Canvas recurrente o desencadenado por acción o API %}

Puede probar hasta cuatro rutas en una única Ruta de Experimento. Añade tus rutas y termina de configurar tu Canvas como necesites, luego lánzalo.  

Cuando el primer usuario haya entrado en el experimento, puedes consultar el Canvas para ver los análisis a medida que entran y [hacer un seguimiento del rendimiento de tu experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Cuando pase la ventana del experimento y éste se haya completado, todos los usuarios posteriores que entren en el Canvas serán enviados por el camino que tenga más probabilidades de resultar en una conversión para ellos.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análisis {#analytics}

Si se han activado las rutas personalizadas, la vista de análisis se divide en dos pestañas: **Experimento inicial** y **trayectorias personalizadas**.

{% tabs local %}
{% tab Experimento inicial %}

La pestaña **Experimento inicial** muestra las métricas de cada ruta durante la ventana del experimento. Puede ver un resumen del rendimiento de todas las rutas para los eventos de conversión especificados.

![Resultados de un experimento inicial enviado para determinar la ruta de mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada ruta en función de varias métricas para el canal de destino.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Por defecto, la prueba busca asociaciones entre los eventos personalizados del usuario y sus preferencias de ruta. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a una ruta determinada. Estas relaciones se utilizan para determinar a qué usuarios se asigna cada ruta una vez transcurrida la ventana del experimento.

Las relaciones entre los eventos personalizados y las preferencias de mensajes se muestran en la tabla de la pestaña **Experimento inicial**.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de ruta, la prueba volverá a un método de análisis basado en la sesión.

{% details Método de análisis retrospectivo %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar las Rutas Personalizadas, la pestaña **Experimento Inicial** muestra un desglose de las variantes preferidas por los usuarios en función de una combinación de determinadas características.

Estas características son:

- **Recencia:** La última vez que tuvieron una sesión
- **Frecuencia:** Frecuencia de las sesiones
- **Permanencia:** Cuánto tiempo llevan siendo usuarios

![La tabla de características de los usuarios, que muestra qué usuarios se prevé que prefieran la Ruta 1 y la Ruta 2 en función de los tres grupos en los que se encuentran en cuanto a recurrencia, frecuencia y permanencia.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Piensa en la recencia como cuán reciente fue la última interacción contigo, en la frecuencia como cuán seguido interactúan contigo y en la permanencia como la duración total que llevan interactuando contigo. Agrupamos a los usuarios en "cubos" en función de estas tres cosas (como se explica en la tabla **Características de los usuarios** ) y luego vemos a qué cubo le gusta más cada ruta. Es como clasificar a los usuarios en cientos de listas diferentes en función de cuándo compraron por última vez con usted, con qué frecuencia compran y cuánto tiempo llevan siendo clientes.

A la hora de elegir un mensaje para un usuario, Braze examina los grupos en los que se encuadra. Cada cubo ejerce una influencia distinta en la selección de rutas para los usuarios. Cuantificamos esta influencia utilizando un método estadístico llamado [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression), que es una forma de predecir el comportamiento futuro basándose en acciones pasadas. Este método tiene en cuenta las interacciones del usuario durante el envío inicial del mensaje. Esta tabla sólo resume los resultados mostrando el camino que los usuarios de cada grupo tendían a seguir.

En última instancia, Braze combina todos estos datos para seleccionar una ruta de mensajes personalizada para cada usuario, con el fin de garantizar que sea lo más atractiva y relevante posible para ellos.

{% alert note %}
Los intervalos de tiempo para cada cubo se determinan en función de los datos de usuario específicos de Canvas, que pueden variar entre Canvases.
{% endalert %}

**Cómo se seleccionan los itinerarios personalizados**<br>
Con este método, el mensaje recomendado de un usuario individual es la suma de los efectos de su recencia, frecuencia y permanencia específicas. La recurrencia, la frecuencia y la permanencia se dividen en categorías, como se ilustra en la tabla de **características de los usuarios**. El intervalo de tiempo de cada cubo viene determinado por los datos de los usuarios de cada lienzo individual y cambiará de un lienzo a otro.

Cada contenedor puede tener una contribución o "push" diferente hacia cada ruta. La fuerza del empuje para cada cubo se determina a partir de las respuestas de los usuarios en el experimento inicial mediante [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla sólo resume los resultados mostrando el camino que los usuarios de cada grupo tendían a seguir. La Trayectoria Personalizada real de cualquier usuario individual depende de la suma de los efectos de los tres cubos en los que se encuentra, uno por cada característica.

{% enddetails %}

{% endtab %}
{% tab Caminos personalizados %}

La pestaña **Rutas personalizadas** muestra los resultados del experimento final, en el que los usuarios del grupo de retraso fueron enviados por la ruta con mejor rendimiento para ellos.

Las tres tarjetas de esta página muestran tu aumento proyectado, los resultados globales y los resultados proyectados si en lugar de eso enviaras solo la Ruta ganadora. Incluso si no hay aumento, lo que a veces puede ocurrir, el resultado es el mismo que enviar solo la Ruta ganadora (una prueba A/B tradicional).

- **Previsión de aumento:** La mejora en su evento de conversión seleccionado debido al uso de Rutas Personalizadas en lugar de enviar a cada usuario por la ruta general de mejor rendimiento.
- **Resultados globales:** Los resultados del segundo envío basados en su evento de conversión.
- **Resultados previstos:** Los resultados previstos del segundo envío en función de la métrica de optimización elegida si en su lugar hubiera enviado sólo la Variante Ganadora.

![Pestaña Caminos personalizados para un lienzo. Las tarjetas muestran la elevación proyectada, las conversiones globales (con rutas personalizadas) y las aperturas únicas proyectadas (con ruta ganadora).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Uso de rutas personalizadas con entrega a tiempo local

No recomendamos utilizar la entrega en hora local en Lienzos con Caminos Personalizados. Esto se debe a que las ventanas de experimentación comienzan cuando pasa el primer usuario. Los usuarios que se encuentran en zonas horarias muy tempranas pueden entrar en el paso y activar el inicio de la ventana del experimento mucho antes de lo esperado, lo que puede provocar que el experimento concluya antes de que el grueso de sus usuarios en zonas horarias más típicas hayan tenido tiempo suficiente para entrar en el Canvas y convertir.

Alternativamente, si desea utilizar la entrega local, utilice una ventana de experimentación de 24-48 horas o más. De este modo, los usuarios de zonas horarias tempranas entran en el lienzo y activan el experimento para que comience, pero queda tiempo suficiente en la ventana del experimento. Los usuarios de zonas horarias más tardías aún tendrán tiempo suficiente para entrar en el Lienzo y en el Paso del Experimento con Rutas Personalizadas y posiblemente convertir antes de que expire la ventana del experimento.

