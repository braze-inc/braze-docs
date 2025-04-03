---
nav_title: Creación de pruebas
article_title: Creación de pruebas multivariante y A/B
page_order: 1
page_type: reference
description: "Este artículo explica cómo crear pruebas multivariantes y A/B con Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Creación de pruebas multivariantes y A/B {#creating-tests}

> Puede crear una [prueba multivariante o A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para cualquier campaña dirigida a un único canal.

![][2]{: style="max-width:25%;float:right;margin-left:15px;" }

## Paso 1: Crea tu campaña

Haga clic en **Crear campaña** y seleccione un canal para la campaña en la sección que permite realizar pruebas multivariantes y A/B. Para obtener documentación detallada sobre cada canal de mensajería, consulta [Crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Paso 2: Compone tus variantes

Puede crear hasta 8 variantes de su mensaje, diferenciando entre títulos, contenidos, imágenes, etc. El número de diferencias entre los mensajes determina si se trata de una prueba multivariante o A/B. Una prueba A/B examina el efecto de cambiar una variable, mientras que una prueba multivariante examina dos o más.

Para algunas ideas sobre cómo empezar a diferenciar tus variantes, consulta [Consejos para diferentes canales](#tips-different-channels).

![][3]

## Paso 3: Programa tu campaña

La programación de su campaña multivariante funciona igual que la programación de cualquier otra campaña Braze. Todos los [tipos de entrega][4] estándar están disponibles.

Una vez que comienza una prueba multivariante, no puede realizar cambios en la campaña. Si cambia los parámetros, como la línea de asunto o el cuerpo HTML, Braze considerará que el experimento está comprometido y lo desactivará inmediatamente.

{% alert important %}
Si desea utilizar una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponible para determinados canales), programe su campaña para que se entregue una vez. Las optimizaciones no están disponibles para las campañas que se repiten o que tienen activada la reelección.
{% endalert %}

## Paso 4: Elija un segmento y distribuya a sus usuarios por variantes

Seleccione los segmentos a los que dirigirse y, a continuación, distribuya sus miembros entre las variantes seleccionadas y el [grupo de control](#including-a-control-group) opcional. Si desea conocer las mejores prácticas para elegir un segmento con el que realizar las pruebas, consulte [Elegir un segmento](#choosing-a-segment).

Para las campañas push, de correo electrónico y webhook programadas para enviarse una vez, también puede utilizar una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Esto reservará una parte de su público objetivo de la prueba A/B y los retendrá para un segundo envío optimizado basado en los resultados de la primera prueba.

### Grupo de control {#including-a-control-group}

Puede reservar un porcentaje de su público objetivo para un grupo de control aleatorio. Los usuarios del grupo de control no reciben la prueba, pero Braze controla su tasa de conversión durante toda la campaña.

Al visualizar sus resultados, puede comparar las tasas de conversión de sus variantes con una tasa de conversión de referencia proporcionada por su grupo de control. Esto le permite comparar tanto los efectos de sus variantes como los efectos de sus variantes frente a la tasa de conversión que resultaría si no enviara ningún mensaje.

![Panel de pruebas A/B que muestra el desglose porcentual del grupo de control, la variante 1, la variante 2 y la variante 3, con un 25 % para cada grupo.][5]

{% alert important %}
No se recomienda utilizar un grupo de control para determinar el ganador por aperturas o clics. Como el grupo de control no recibirá el mensaje, esos usuarios no podrán realizar aperturas ni clics. Por tanto, el índice de conversión de ese grupo es del 0% por definición y no constituye una comparación significativa con las variantes.
{% endalert %}

#### Grupos de control con pruebas A/B

Cuando se utiliza la limitación de la tasa con una prueba A/B, el límite de la tasa no se aplica al grupo de control de la misma manera que al grupo de prueba, lo que es una fuente potencial de sesgo temporal. Utilice ventanas de conversión adecuadas para evitar este sesgo.

#### Grupos de control con selección inteligente

El tamaño del grupo de control para una campaña con [Selección Inteligente][1] se basa en el número de variantes. Si cada variante se envía a más del 20% de los usuarios, entonces el grupo de control es el 20% y las variantes se reparten equitativamente entre el 80% restante. Sin embargo, si tiene suficientes variantes como para que cada una de ellas se envíe a menos del 20% de los usuarios, entonces el grupo de control debe ser más pequeño. Cuando Intelligent Selection empieza a analizar el rendimiento de su prueba, el grupo de control aumenta o disminuye en función de los resultados.

## Paso 5: Designar un evento de conversión (opcional)

Establecer un evento de conversión para una campaña le permite ver cuántos destinatarios de esa campaña realizaron una acción concreta después de recibirla.

Esto sólo afecta a la prueba si eligió **Tasa de conversión primaria** en los pasos anteriores. Para más información, consulta los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). 

## Paso 6: Revisión y lanzamiento

En la página de confirmación, revise los detalles de su campaña multivariante e inicie la prueba. A continuación, aprenda a [comprender los resultados de sus pruebas]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Lo que hay que saber

{% alert important %}
Si edita los mensajes una vez iniciado el experimento, los resultados de la prueba quedarán invalidados.

- Si tu experimento está en mitad del envío y editas el mensaje, el experimento quedará inutilizado y se eliminarán los resultados del mismo.
- Si su experimento ha finalizado y edita el mensaje después de enviarlo, los resultados del experimento seguirán estando disponibles en la página de análisis del panel de control. Si vuelve a lanzar la campaña, se eliminarán los resultados del experimento.
{% endalert %}

### Consejos para distintos canales {#tips-different-channels}

Dependiendo del canal que elija, podrá probar distintos componentes de su mensaje. Intente componer variantes con una idea de lo que quiere probar y lo que espera demostrar.

¿De qué palancas hay que tirar y cuáles son los efectos deseados? Aunque hay millones de posibilidades que puedes investigar utilizando una prueba multivariante y A/B, tenemos algunas sugerencias para que empieces:

| Canal | Aspectos del mensaje que puede cambiar | Resultados |
| ---------------------| --------------- | ------------- |
| Push | Copiar <br> Uso de imágenes y emoji <br> Vínculos profundos  <br> Presentación de las cifras (por ejemplo, "triplicar" frente a "aumentar un 200%").  <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina dentro de 6 horas") | Aperturas  <br> Tasa de conversión |
| Correo electrónico | Asunto <br> Nombre para mostrar <br> Saludo <br> Copia del cuerpo <br> Uso de imágenes y emoji <br> Presentación de las cifras (por ejemplo, "triplicar" frente a "aumentar un 200%"). <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina dentro de 6 horas") | Aperturas  <br> Tasa de conversión |
| Mensaje dentro de la aplicación | Aspectos listados para "push" <br> [Formato del mensaje][7] | Clic <br> Tasa de conversión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Cuando ejecute pruebas A/B, no olvide generar [informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) que le permitan comprender el impacto de cada variante en su embudo de conversión, especialmente si la "conversión" para su negocio implica realizar múltiples pasos o acciones.
{% endalert %}

Además, la duración ideal de su prueba también puede variar en función del canal. Tenga en cuenta el tiempo medio que la mayoría de los usuarios necesitan para interactuar con cada canal.

Por ejemplo, si está probando un push, puede obtener resultados significativos más rápidamente que cuando prueba el correo electrónico, ya que los usuarios ven los push inmediatamente, pero pueden pasar días antes de que vean o abran un correo electrónico. Si está probando mensajes dentro de la aplicación, tenga en cuenta que los usuarios deben abrir la aplicación para ver la campaña, por lo que debe esperar más tiempo para recopilar resultados tanto de los usuarios más activos que abren la aplicación como de los usuarios más habituales.

Si no está seguro de cuánto tiempo debe durar su prueba, la función [Selección inteligente][6] puede ser útil para encontrar una Variante Ganadora de forma eficiente.

### Elegir un segmento {#choosing-a-segment}

Dado que los distintos segmentos de sus usuarios pueden responder de forma diferente a los mensajes, el éxito de un mensaje concreto dice algo tanto del mensaje en sí como de su segmento objetivo. Por lo tanto, intente diseñar una prueba pensando en su segmento objetivo.

Por ejemplo, mientras que los usuarios activos pueden tener tasas de respuesta iguales a "¡Esta oferta caduca mañana!" y "¡Esta oferta caduca en 24 horas!", los usuarios que no han abierto la aplicación durante una semana pueden ser más receptivos a la última formulación, ya que crea una mayor sensación de urgencia.

Además, a la hora de elegir el segmento sobre el que realizar la prueba, asegúrese de considerar si el tamaño de ese segmento será lo suficientemente grande para su prueba. En general, las pruebas multivariantes y A/B con más variantes requieren un grupo de prueba mayor para conseguir resultados estadísticamente significativos. Esto se debe a que un mayor número de variantes hará que menos usuarios vean cada variante individual.

{% alert tip %}
A título orientativo, es probable que necesite unos 15.000 usuarios por variante (incluido el control) para alcanzar un 95% de confianza en los resultados de sus pruebas. Sin embargo, el número exacto de usuarios que necesita podría ser mayor o menor que ese dependiendo de su caso particular. Para obtener una orientación más exacta sobre las variantes del tamaño de la muestra, considere la posibilidad de consultar una [calculadora del tamaño de la muestra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Sesgo y aleatorización

Una cuestión común con las asignaciones de grupos de control y de prueba es preguntarse si pueden introducir sesgos en sus pruebas. Otros se preguntan a veces cómo sabemos si estas asignaciones son realmente aleatorias.

Los usuarios se asignan a variantes de mensajes, variantes de Canvas o a sus respectivos grupos de control concatenando su ID de usuario (generado aleatoriamente) con el ID de campaña o Canvas (generado aleatoriamente), tomando el módulo de ese valor con 100 y, a continuación, ordenando a los usuarios en porciones que se correspondan con las asignaciones porcentuales de variantes y control opcional elegidas en el cuadro de mandos. Por lo tanto, no hay forma práctica de que los comportamientos de los usuarios antes de la creación de una campaña o Canvas en particular puedan variar sistemáticamente entre las variantes y el control. Tampoco es práctico ser más aleatorio (o más exactamente, pseudoaleatorio) que esta implementación.

#### Errores a evitar

Si no se filtran correctamente las audiencias, hay que evitar algunos errores comunes que crean la apariencia de diferencias basadas en el canal de mensajería.

Por ejemplo, si envía un mensaje push a un público amplio con un control, el grupo de prueba sólo enviará mensajes a los usuarios con un token push. Sin embargo, el grupo de control incluirá tanto a los usuarios que tienen un token push como a los que no. En este caso, su audiencia inicial para la campaña o Canvas debe filtrar por tener un token push (`Push Enabled` es `true`). Lo mismo debe hacerse para ser elegible para recibir mensajes en otros canales: adhesión voluntaria, tiene un token de notificaciones push, está suscrito, etc.

{% alert note %}
Si utiliza manualmente números de cubo aleatorios para los grupos de control, consulte esta lista de [cosas que debe tener en cuenta]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) en sus grupos de control.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
