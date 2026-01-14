---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes sobre pruebas multivariantes y A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Este artículo trata de las preguntas más frecuentes sobre las pruebas multivariantes y A/B con Braze."
---

# Preguntas frecuentes sobre pruebas multivariantes y A/B

## Aspectos básicos de las pruebas

### ¿Cuál es la diferencia entre las pruebas A/B y las pruebas multivariantes?

#### Pruebas A/B

En las pruebas A/B, el especialista en marketing experimenta con una única variable dentro de la campaña (como las líneas del asunto del correo electrónico o la hora de envío del mensaje). Esto implica dividir aleatoriamente un subconjunto de la audiencia en dos o más grupos, presentar a cada grupo una variación diferente y observar qué variación presenta la tasa de conversión más alta. Normalmente, la variante con mejor rendimiento se envía posteriormente al resto de la audiencia.

#### Pruebas multivariantes 

Las pruebas multivariantes son una extensión de las pruebas A/B, que permiten al especialista en marketing probar múltiples variables a la vez para determinar la combinación más eficaz. Por ejemplo, puedes probar la línea del asunto de tu mensaje de correo electrónico, la imagen que acompaña al texto y el color del botón de CTA. Este tipo de pruebas te permite explorar más variables y combinaciones de variaciones en un solo experimento, y obtener información más rápida y exhaustiva que con las pruebas A/B. Sin embargo, probar más variables y combinaciones dentro de un mismo experimento requiere una audiencia mayor para obtener significación estadística.

### ¿Cómo se calculan los resultados de las pruebas A/B?

Braze prueba todas las variantes entre sí con las pruebas chi-cuadrado de Pearson, que miden si una variante supera estadísticamente a todas las demás a un nivel de significación de p < 0,05, o lo que denominamos significación del 95%. Entre todas las variantes que superan este umbral de significación, se determina que la variante con mejor rendimiento es la "ganadora".

Se trata de una prueba independiente de la puntuación de confianza, que sólo describe el rendimiento de una variante en comparación con el control con un valor numérico entre 0 y 100%. En concreto, representa nuestra confianza en que la diferencia estandarizada en la tasa de conversión entre la variante y el control es significativamente superior al azar.

### ¿Por qué la distribución de variantes no es uniforme?

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Ejecución y conclusión de las pruebas

### ¿Cuándo termina la prueba inicial?

Cuando se utiliza la Variante ganadora para campañas de un solo envío, la prueba finaliza cuando llega la Hora de envío de la Variante ganadora. Braze considerará que una variante es la ganadora si muestra la tasa de conversión más alta por un margen estadísticamente significativo.

Para campañas recurrentes, basadas en acciones y desencadenadas por API, puedes utilizar Intelligent Selection para hacer un seguimiento continuo de los datos de rendimiento de cada variante y optimizar continuamente el tráfico de la campaña hacia las variantes de mayor rendimiento. Con la Intelligent Selection, en lugar de definir explícitamente un grupo de experimentación en el que los usuarios reciban variantes aleatorias, el algoritmo Braze refinará continuamente su estimación de la variante de mejor rendimiento, lo que potencialmente permitirá una selección más rápida de la de mayor rendimiento.

### ¿Cómo gestiona Braze a los usuarios que han recibido una variante de mensaje en una campaña recurrente o en un paso en Canvas de entrada? 

Los usuarios son asignados aleatoriamente a una variante concreta antes de recibir la campaña por primera vez. Cada vez que se reciba la campaña sucesivamente (o el usuario vuelva a entrar en una variante de Canvas), recibirá la misma variante, a menos que se modifiquen los porcentajes de la variante. Si cambian los porcentajes de variantes, los usuarios pueden ser redistribuidos a otras variantes. Los usuarios permanecen en estas variantes hasta que se vuelven a modificar los porcentajes. Los usuarios sólo serán redistribuidos para las variantes que fueron editadas.

Por ejemplo, supongamos que tenemos una campaña o Canvas con tres variantes. Si sólo se modifican o actualizan la Variante A y la Variante B, los usuarios de la Variante C no se redistribuirán porque el porcentaje de variantes de la Variante C no se modificó. Los grupos de control siguen siendo coherentes si el porcentaje de variantes no varía. Los usuarios que hayan recibido mensajes anteriormente no pueden entrar en el grupo de control en un envío posterior, ni ningún usuario del grupo de control puede recibir nunca un mensaje.

#### ¿Qué pasa con las Rutas de experimentos?

Lo mismo ocurre porque las rutas Canvas que siguen a un experimento también son variantes.

#### ¿Puedo realizar acciones para redistribuir usuarios en campañas y Lienzos?

La única forma de redistribuir a los usuarios en los Canvas es utilizar [Rutas Aleatorias en las Rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), que siempre asignarán aleatoriamente las rutas cuando los usuarios vuelvan a entrar en el Canvas. Sin embargo, esto no es un experimento estándar y podría invalidar los resultados del experimento, porque el grupo de control puede contaminarse con usuarios del tratamiento.

## Confianza y sesgo

### ¿Aumenta la confianza con el tiempo?

La confianza aumenta con el tiempo si todo lo demás se mantiene constante. Mantenerlo constante significa que no hay otros factores de marketing que puedan influir en las variantes, como que la variante A hable de una rebaja del 25% que termina a mitad de la prueba.

La confianza es una medida de la seguridad que tiene Braze de que la variante es diferente del control. A medida que se envían más mensajes, aumenta la potencia estadística de la prueba, lo que aumentaría la confianza en que las diferencias de rendimiento medidas no se deben al azar. En general, un mayor tamaño de la muestra aumenta nuestra confianza a la hora de identificar pequeñas diferencias de rendimiento entre las variantes y el control.

### ¿La asignación de grupos de control y de prueba puede introducir sesgos en las pruebas?

No hay forma práctica de que los atributos o comportamientos de un usuario antes de la creación de una determinada campaña o Canvas puedan variar sistemáticamente entre las variantes y el control. 

Para asignar usuarios a variantes de mensajería, variantes en Canvas o sus respectivos grupos de control, empezamos por vincular su ID de usuario generado aleatoriamente con el ID de campaña o Canvas generado aleatoriamente. A continuación, aplicamos un algoritmo de hashing sha256 y dividimos ese resultado por 100, y nos quedamos con el resto (también conocido como módulo con 100). Por último, ordenamos a los usuarios en porciones que corresponden a las asignaciones porcentuales de variantes (y control opcional) elegidas en el panel.

### ¿Por qué no puedo utilizar el límite de velocidad con un grupo de control?

Actualmente, Braze no admite el límite de velocidad con pruebas A/B que tengan un grupo de control. Esto se debe a que el límite de velocidad no se aplica al grupo de control del mismo modo que a las variantes, lo que introduce un sesgo. En su lugar, considera la posibilidad de utilizar [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), que ajusta automáticamente el porcentaje de usuarios que recibirán cada variante en función de los análisis y el rendimiento de la campaña.
