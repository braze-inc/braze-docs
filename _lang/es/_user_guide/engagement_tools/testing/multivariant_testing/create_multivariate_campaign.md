---
nav_title: Crear pruebas
article_title: Crear pruebas multivariantes y A/B
page_order: 1
page_type: reference
description: "Este artículo explica cómo crear pruebas multivariantes y A/B con Braze."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Crear pruebas multivariantes y A/B {#creating-tests}

> Puedes crear una [prueba multivariante o A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para cualquier campaña dirigida a un solo canal y un solo dispositivo. Por ejemplo, si quieres utilizar pruebas multivariantes o A/B para una campaña push, puedes dirigirte sólo a dispositivos iOS o sólo a dispositivos Android, no a ambos tipos de dispositivos en la misma campaña.

\![El desplegable al seleccionar el botón "Crear campaña" para elegir entre multicanal o canal único.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## Paso 1: Crea tu campaña

1. Ve a **Mensajes** > Campañas.
2. Selecciona **Crear campaña** y un canal para la campaña en la sección que permite pruebas multivariantes y A/B. Para obtener documentación detallada sobre cada canal de mensajería, consulta [Crear una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## Paso 2: Compone tus variantes

Puedes crear hasta ocho variantes de tu mensaje, diferenciando entre títulos, contenido, imágenes y mucho más. El número de diferencias entre los mensajes determina si se trata de una prueba multivariante o A/B. Una prueba A/B examina el efecto de cambiar una variable, mientras que una prueba multivariante examina dos o más.

Para algunas ideas sobre cómo empezar a diferenciar tus variantes, consulta [Consejos para diferentes canales](#tips-different-channels).

Seleccionando "Añadir variante" para una campaña.]({% image_buster /assets/img/ab_create_2.png %})

## Paso 3: Programa tu campaña

Programar tu campaña multivariante funciona igual que programar cualquier otra campaña Braze. Disponemos de todos los [tipos de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) estándar.

Una vez que comienza una prueba multivariante, no puedes hacer cambios en la campaña. Si cambias los parámetros, como la línea del asunto o el cuerpo HTML, Braze considerará que el experimento está comprometido y lo desactivará inmediatamente.

{% alert important %}
Para utilizar una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) (disponible para determinados canales), programa tu campaña para que se entregue una vez. Las optimizaciones no están disponibles para las campañas que se repiten o que tienen activada la re-elegibilidad.
{% endalert %}

## Paso 4: Elige un segmento y distribuye a tus usuarios en variantes

Selecciona los segmentos a los que dirigirte y, a continuación, distribuye a sus miembros entre tus variantes seleccionadas y el [grupo de control](#including-a-control-group) opcional. Para conocer las mejores prácticas sobre la elección de un segmento con el que realizar la prueba, consulta [Elegir un segmento](#choosing-a-segment).

Para las campañas push, correo electrónico y webhook programadas para enviarse una vez, también puedes utilizar una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Esto reservará una parte de tu audiencia objetivo de la prueba A/B y la retendrá para un segundo envío optimizado basado en los resultados de la primera prueba.

### Grupo de control {#including-a-control-group}

Puedes reservar un porcentaje de tu audiencia objetivo para un grupo de control aleatorio. Los usuarios del grupo de control no reciben la prueba, pero Braze controla su tasa de conversión durante toda la campaña.

Al ver tus resultados, puedes comparar las tasas de conversión de tus variantes con una tasa de conversión de referencia proporcionada por tu grupo de control. Esto te permite comparar tanto los efectos de tus variantes como los efectos de tus variantes frente a la tasa de conversión que se obtendría si no enviaras ningún mensaje.

\![Panel de pruebas A/B que muestra el desglose porcentual del grupo de control, la variante 1, la variante 2 y la variante 3, con un 25% para cada grupo.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
No se recomienda utilizar un grupo de control al determinar un ganador por _Aperturas_ o _Clics_. Como el grupo de control no recibirá el mensaje, esos usuarios no podrán realizar aperturas ni clics. Por tanto, la tasa de conversión de ese grupo es del 0% por definición y no constituye una comparación significativa con las variantes.
{% endalert %}

#### Grupos de control con pruebas A/B

Cuando se utiliza el límite de velocidad con una prueba A/B, el límite de velocidad no se aplica al grupo de control de la misma forma que al grupo de prueba, lo que es una fuente potencial de sesgo temporal. Utiliza ventanas de conversión adecuadas para evitar este sesgo.

#### Grupos de control con Intelligent Selection

El tamaño del grupo de control de una campaña con [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) se basa en el número de variantes. Si cada variante se envía a más del 20% de los usuarios, entonces el grupo de control es el 20%, y las variantes se reparten por igual entre el 80% restante. Sin embargo, si tienes suficientes variantes como para que cada variante se envíe a menos del 20% de los usuarios, entonces el grupo de control debe hacerse más pequeño. Cuando Intelligent Selection empieza a analizar el rendimiento de tu prueba, el grupo de control aumenta o disminuye en función de los resultados.

## Paso 5: Designa un evento de conversión (opcional)

Configurar un evento de conversión para una campaña te permite ver cuántos destinatarios de esa campaña realizaron una acción concreta después de recibirla.

Esto sólo afecta a la prueba si elegiste **Tasa de conversión primaria** en los pasos anteriores. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/). 

## Paso 6: Revisión y lanzamiento

En la página de confirmación, revisa los detalles de tu campaña multivariante y ¡lanza la prueba! A continuación, aprende a [comprender los resultados de tus pruebas]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

## Lo que debes saber

Si tu experimento ya ha comenzado a enviarse y editas el mensaje, el experimento se invalidará y se eliminará cualquier resultado del experimento.

- Para evitar cualquier interferencia con el comportamiento esperado del experimento, recomendamos evitar la edición de mensajes en el plazo de una hora desde el lanzamiento de la campaña del experimento.
- Si tu experimento ha finalizado y editas el mensaje después de enviarlo, los resultados del experimento seguirán estando disponibles en el análisis de tu panel. Sin embargo, si vuelves a lanzar la campaña, se eliminarán los resultados del experimento.

### Consejos para diferentes canales {#tips-different-channels}

Según el canal que selecciones, puedes probar distintos componentes de tu mensaje. Por ejemplo, puedes intentar componer variantes con una idea de lo que quieres probar y lo que esperas demostrar. ¿De qué palancas tienes que tirar, y cuáles son los efectos deseados? Aunque hay millones de posibilidades que puedes investigar utilizando una prueba multivariante y A/B, tenemos algunas sugerencias para que empieces:

| Canal | Aspectos del mensaje que puedes cambiar | Resultados a buscar |
| ---------------------| --------------- | ------------- |
| Push | Copia <br> Uso de imágenes y emoji <br> Vínculos profundos  <br> Presentación de las cifras (por ejemplo, "triplicar" frente a "aumentar un 200%")  <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina en 6 horas") | Abre  <br> Tasa de conversión |
| Correo electrónico | Asunto <br> Mostrar nombre <br> Saludo <br> Copia del cuerpo <br> Uso de imágenes y emoji <br> Presentación de las cifras (por ejemplo, "triplicar" frente a "aumentar un 200%") <br> Presentación del tiempo (por ejemplo, "termina a medianoche" frente a "termina en 6 horas") | Abre  <br> Tasa de conversión |
| Mensaje dentro de la aplicación | Aspectos listados para "push" <br> [Formato del mensaje]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) | Clic <br> Tasa de conversión |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Cuando realices pruebas A/B, no olvides generar [informes de embudo]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) que te permitan comprender el impacto de cada variante en tu embudo de conversión, especialmente si la "conversión" para tu negocio implica dar múltiples pasos o acciones.
{% endalert %}

Además, la duración ideal de tu prueba también puede variar en función del canal. Ten en cuenta el tiempo medio que la mayoría de los usuarios pueden necesitar para interactuar con cada canal.

Por ejemplo, si estás probando un push, puedes conseguir resultados significativos más rápidamente que al probar el correo electrónico, ya que los usuarios ven los push inmediatamente, pero pueden pasar días antes de que vean o abran un correo electrónico. Si estás probando mensajes dentro de la aplicación, ten en cuenta que los usuarios deben abrir la aplicación para ver la campaña, por lo que debes esperar más tiempo para recopilar resultados tanto de los que abren más activamente la aplicación como de los usuarios más típicos.

Si no estás seguro de cuánto tiempo debe durar tu prueba, la característica [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) puede ser útil para encontrar una variante ganadora de forma eficaz.

### Elegir un segmento {#choosing-a-segment}

Dado que los distintos segmentos de tus usuarios pueden responder de forma diferente a la mensajería, el éxito de un mensaje concreto dice algo tanto del mensaje en sí como de su segmento objetivo. Por tanto, intenta diseñar una prueba pensando en tu segmento objetivo.

Por ejemplo, mientras que los usuarios activos pueden tener tasas de respuesta iguales a "¡Esta oferta caduca mañana!" y a "¡Esta oferta caduca en 24 horas!", los usuarios que no han abierto la aplicación en una semana pueden ser más receptivos a esta última redacción, ya que crea una mayor sensación de urgencia.

Además, cuando elijas el segmento sobre el que vas a realizar la prueba, asegúrate de tener en cuenta si el tamaño de ese segmento será lo suficientemente grande para tu prueba. En general, las pruebas multivariantes y A/B con más variantes requieren un grupo de prueba mayor para conseguir resultados estadísticamente significativos. Esto se debe a que un mayor número de variantes hará que menos usuarios vean cada variante individual.

{% alert tip %}
A título orientativo, probablemente necesites unos 15.000 usuarios por variante (incluido el control) para alcanzar un 95% de confianza en los resultados de tu prueba. Sin embargo, el número exacto de usuarios que necesitas podría ser mayor o menor que ese, dependiendo de tu caso particular. Para una orientación más exacta sobre los tamaños de muestra variantes, considera la posibilidad de consultar una [calculadora de tamaño de muestra](https://www.calculator.net/sample-size-calculator.html).
{% endalert %}

### Sesgo y aleatorización

Una cuestión habitual con las asignaciones de grupos de control y de prueba es si pueden introducir sesgos en tus pruebas. Otros se preguntan a veces cómo sabemos si estas asignaciones son realmente aleatorias.

A los usuarios se les asignan variantes del mensaje, variantes en Canvas o sus respectivos grupos de control concatenando su ID de usuario (generado aleatoriamente) con el ID de campaña o Canvas (generado aleatoriamente), tomando el módulo de ese valor con 100 y, a continuación, ordenando a los usuarios en porciones que se correspondan con las asignaciones porcentuales de variantes y control opcional elegidas en el panel. Por tanto, no hay forma práctica de que los comportamientos de los usuarios antes de crear una campaña o Canvas concretos puedan variar sistemáticamente entre las variantes y el control. Tampoco es práctico ser más aleatorio (o más exactamente, pseudoaleatorio) que esta implementación.

#### Errores a evitar

Hay algunos errores comunes para evitar crear la apariencia de diferencias basadas en el canal de mensajería si las audiencias no se filtran correctamente.

Por ejemplo, si envías un mensaje push a una amplia audiencia con un control, el grupo de prueba sólo enviará mensajes a los usuarios con un token de notificaciones push. Sin embargo, el grupo de control incluirá tanto a usuarios que sí tienen un token de notificaciones push como a usuarios que no lo tienen. En este caso, tu audiencia inicial para la campaña o Canvas debe filtrar por tener un token de notificaciones push (`Foreground Push Enabled` es `true`). Lo mismo debe hacerse para ser elegible para recibir mensajes en otros canales: adhesión voluntaria, tiene un token de notificaciones push, está suscrito, etc.

{% alert note %}
Si utilizas manualmente números de contenedor aleatorios para los grupos de control, echa un vistazo a [las cosas que debes tener]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) en [cuenta]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) en tus grupos de control.
{% endalert %}

