---
nav_title: Análisis
article_title: Análisis multivariante y pruebas A/B
page_order: 10
page_type: reference
description: "Este artículo explica cómo ver e interpretar los resultados de una campaña multivariante o A/B."
---

# Análisis multivariante y pruebas A/B

> Este artículo explica cómo ver los resultados de una prueba multivariante o A/B. Si aún no ha configurado su prueba, consulte [Crear pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para conocer los pasos a seguir.

Una vez lanzada la campaña, puede comprobar el rendimiento de cada variante seleccionando la campaña en la sección **Campañas** del panel de control. 

## Opción de análisis por optimización

Su vista de análisis variará dependiendo de si seleccionó una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) durante su configuración inicial.

### Sin optimización

Si seleccionó **Sin optimización** al configurar su campaña, su vista de análisis permanecerá igual. La página **de Análisis de Campaña** de su campaña mostrará el rendimiento de sus variantes frente a su grupo de control, si incluyó uno.

![Sección de rendimiento de los análisis de campaña para una campaña de correo electrónico con múltiples variantes. La tabla enumera diversas métricas de rendimiento para cada variante, como destinatarios, rebotes, clics y conversiones.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para obtener más información, consulte el artículo [Análisis de campañas]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para su canal de mensajería.

### Variante ganadora

Si seleccionó **Variante ganadora** para su optimización al configurar su campaña, tendrá acceso a una pestaña adicional de sus análisis de campaña denominada **Resultado de la prueba A/B**. Después de enviar la Variante Ganadora al resto de usuarios de la prueba, esta pestaña muestra los resultados de ese envío.

El **resultado de la prueba A/B** se divide en dos pestañas: **Prueba inicial** y **variante ganadora**.

{% tabs local %}
{% tab Prueba inicial %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de su segmento objetivo. Puede ver un resumen de cómo se comportaron todas las variantes y si hubo o no un ganador durante la prueba.

Si una variante supera a todas las demás con una [confianza]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) superior al 95%, Braze marca esa variante con la etiqueta "Ganador".

Si ninguna variante supera a todas las demás con un 95% de confianza y usted opta por enviar la variante con mejores resultados de todos modos, se seguirá enviando la variante con mejores resultados y se indicará con la etiqueta "Ganador".

![Resultados de una prueba inicial enviada para determinar la Variante Ganadora en la que ninguna variante obtuvo mejores resultados que las demás con la confianza suficiente para alcanzar el umbral de confianza del 95% para la significación estadística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Cómo se selecciona la Variante Ganadora

Braze prueba todas las variantes entre sí con [las pruebas chi-cuadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Mide si una variante supera estadísticamente a todas las demás a un nivel de significación de p < 0,05, o lo que denominamos significación del 95%. Si es así, la variante ganadora se indica con la etiqueta "Ganador".

Se trata de una prueba independiente de la puntuación de confianza, que sólo describe el rendimiento de una variante en comparación con el control con un valor numérico entre 0 y 100%.

Una variante puede obtener mejores resultados que el grupo de control, pero la prueba chi-cuadrado comprueba si una variante es mejor que todas las demás. [Las pruebas de seguimiento](#recommended-follow-ups) pueden aportar más detalles.

{% endtab %}
{% tab Variante ganadora %}

La pestaña **Variante ganadora** muestra los resultados del segundo envío, en el que a cada usuario restante se le envió la variante con mejor rendimiento de la prueba inicial. Su **Audiencia %** sumará el porcentaje del segmento objetivo que reservó para el grupo Variante ganadora.

![Resultados de la Variante Ganadora enviados al grupo de Variantes Ganadoras.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si desea ver el rendimiento de la Variante ganadora durante toda la campaña, incluidos los envíos de la prueba A/B, consulte la página **Análisis de campaña**.

### Variante personalizada {#personalized-variant}

Si seleccionó **Variante personalizada** para su optimización al configurar su campaña, el **Resultado de la prueba A/B** se divide en dos pestañas: **Prueba inicial** y **variante personalizada**.

{% tabs local %}
{% tab Prueba inicial %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de su segmento objetivo.

![Resultados de una prueba inicial enviada para determinar la variante de mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada variante en función de diversas métricas para el canal de destino.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por defecto, la prueba busca asociaciones entre los eventos personalizados del usuario y sus preferencias de variantes de mensajes. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a una determinada variante de mensaje. Estas relaciones se utilizan después para determinar qué usuarios reciben qué variante de mensaje en el envío final.

Las relaciones entre los eventos personalizados y las preferencias de mensajes se muestran en la tabla de la pestaña **Envío inicial**.

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de variantes, la prueba volverá a un método de análisis basado en sesiones.

{% details Método de análisis retrospectivo %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar las Variantes Personalizadas, la pestaña **Prueba Inicial** muestra un desglose de las variantes preferidas por los usuarios en función de una combinación de determinadas características. 

Estas características son:

- **Recencia:** La última vez que tuvieron una sesión
- **Frecuencia:** Frecuencia de las sesiones
- **Permanencia:** Cuánto tiempo llevan siendo usuarios

Por ejemplo, la prueba puede descubrir que la mayoría de los usuarios prefieren la Variante A, pero los usuarios que tuvieron una sesión hace unos 3-12 días, tienen entre 1-12 días entre sesiones y fueron creados en los últimos 67-577 días tienden a preferir la Variante B. Por lo tanto, los usuarios de esa subpoblación recibieron la Variante B en el segundo envío, mientras que el resto recibió la Variante A.

![La tabla de características de los usuarios, que muestra qué usuarios se prevé que prefieran la variante A y la variante B en función de los tres grupos en los que se clasifican por antigüedad, frecuencia y permanencia.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Cómo se seleccionan las variantes personalizadas**<br>
Con este método, el mensaje recomendado de un usuario individual es la suma de los efectos de su recencia, frecuencia y permanencia específicas. La recurrencia, la frecuencia y la permanencia se dividen en categorías, como se ilustra en la tabla de **características de los usuarios**. El intervalo de tiempo de cada cubo viene determinado por los datos de los usuarios de cada campaña individual y cambiará de una campaña a otra. 

Cada cubo puede tener una contribución o "empuje" diferente hacia cada variante de mensaje. La fuerza del push para cada contenedor se determina a partir de las respuestas de los usuarios en el envío inicial mediante [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla sólo resume los resultados mostrando la variante con la que los usuarios de cada grupo tienden a interactuar. La Variante Personalizada real de cualquier usuario individual depende de la suma de los efectos de los tres cubos en los que se encuentra: uno por cada característica.

{% enddetails %}

{% endtab %}
{% tab Variante personalizada %}

La pestaña **Variante personalizada** muestra los resultados del segundo envío, en el que se envió a cada usuario restante la variante con la que era más probable que interactuara.

Las tres tarjetas de esta página muestran su ascensor proyectado, los resultados globales y los resultados proyectados si en su lugar enviara sólo la Variante Ganadora. Aunque no se produzca un aumento, lo que a veces puede ocurrir, el resultado es el mismo que enviar sólo la variante ganadora (una prueba A/B tradicional). 

- **Previsión de aumento:** La mejora en su métrica de optimización seleccionada para este envío debido al uso de Variantes Personalizadas en lugar de una prueba A/B estándar (si los usuarios restantes sólo recibieron la Variante Ganadora).
- **Resultados globales:** Los resultados del segundo envío basados en la métrica de optimización elegida*(Aperturas Únicas*, *Clics Únicos* o *Evento de Conversión Principal*).
- **Resultados previstos:** Los resultados previstos del segundo envío en función de la métrica de optimización elegida si en su lugar hubiera enviado sólo la Variante Ganadora. 

![Ficha Variante personalizada para una campaña optimizada para aperturas únicas. Las tarjetas muestran el Ascenso Proyectado, las Aperturas Únicas Globales (con Variante Personalizada) y las Aperturas Únicas Proyectadas (con Variante Ganadora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

La tabla de esta página muestra las métricas de cada variante del envío de Variantes Personalizadas. Su **Audiencia %** suma el porcentaje del segmento objetivo que reservó para el grupo Variante personalizada.

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Comprender la confianza {#understanding-confidence}

La confianza es la medida estadística de nuestra certeza de que una diferencia en los datos, como las tasas de conversión, es real y no se debe al azar.

{% alert note %}
¿No ves confianza en tus resultados? La confianza sólo aparecerá si tienes un grupo de control.
{% endalert %}

Una parte importante de sus resultados es la confianza en los mismos. Por ejemplo, ¿qué pasaría si el grupo de control tuviera una tasa de conversión del 20 % y la variante A tuviera una tasa de conversión del 25 %? Esto parece indicar que enviar la Variante A es más eficaz que no enviar ningún mensaje. Tener una confianza del 95% significa que la diferencia entre los dos índices de conversión se debe probablemente a una diferencia real en las respuestas de los usuarios y que sólo hay un 5% de probabilidades de que la diferencia se haya producido por casualidad.

Braze compara la tasa de conversión de cada variante con la tasa de conversión del control mediante un procedimiento estadístico denominado [prueba Z](https://en.wikipedia.org/wiki/Z-test). Un resultado del 95 % o más de confianza, como en el ejemplo anterior, indica que la diferencia es estadísticamente significativa. Esto es cierto en cualquier lugar en el que vea una métrica de confianza en el cuadro de mandos de Braze que describa la diferencia entre dos mensajes o poblaciones de usuarios.

En general, es necesario un nivel de confianza de al menos el 95% para demostrar que los resultados reflejan las preferencias reales de los usuarios y no se deben al azar. En las pruebas científicas rigurosas, el 95 % de confianza (o lo que es lo mismo, que el valor "p" sea inferior a 0,05) es el punto de referencia habitual para determinar la significación estadística. Si continuamente no consigues un 95 % de confianza, prueba a aumentar el tamaño de la muestra o a disminuir el número de variantes. 

La confianza no describe si una variante es mejor que las demás. Es puramente una medida de lo seguros que estamos de que las dos (o más) tasas de conversión son realmente diferentes entre sí. Esto sólo depende del tamaño de la muestra y de las diferencias entre las tasas de conversión aparentes. Que las tasas globales sean altas o bajas no afecta a la solidez de la medida de confianza. Es posible que una variante tenga una tasa de conversión muy diferente de otra y, sin embargo, no tenga una confianza del 95 % o superior. También es posible que dos conjuntos de variantes tengan tasas de conversión/elevación similares y, sin embargo, una confianza diferente.

### Resultados estadísticamente insignificantes

Una prueba que no tenga una confianza del 95 % puede contener información importante. He aquí algunas cosas que puedes aprender de una prueba con resultados estadísticamente insignificantes:

- Es posible que todas sus variantes tuvieran más o menos el mismo efecto. Saber esto te ahorra el tiempo que habrías dedicado a hacer estos cambios. A veces, puede que las tácticas de marketing convencionales, como repetir la llamada a la acción, no funcionen necesariamente con su público.
- Aunque los resultados pueden deberse al azar, pueden servir de base para la hipótesis de la próxima prueba. Si varias variantes parecen tener aproximadamente los mismos resultados, ejecute algunas de ellas de nuevo junto con nuevas variantes para ver si puede encontrar una alternativa más eficaz. Si una variante obtiene mejores resultados, pero no por una cantidad significativa, puede realizar otra prueba en la que la diferencia de esta variante sea más exagerada.
- ¡Sigue probando! Una prueba con resultados insignificantes debería llevar a plantearse ciertas preguntas. ¿Realmente no había diferencia entre sus variantes? ¿Debería haber estructurado la prueba de otra manera? Puedes responder a estas preguntas realizando pruebas de seguimiento.
- Aunque las pruebas son útiles para descubrir qué tipo de mensajería genera la mayor respuesta de tu audiencia, también es importante comprender qué alteraciones en la mensajería tienen solo un efecto insignificante. Esto le permite seguir probando otra alternativa más eficaz o ahorrar el tiempo que podría haber empleado en decidir entre dos mensajes alternativos.

Tanto si la prueba tiene un claro ganador como si no, puede ser útil realizar una [prueba de seguimiento](#recommended-follow-ups) para confirmar los resultados o aplicarlos a un escenario ligeramente distinto.

## Seguimientos recomendados {#recommended-follow-ups}

Una prueba multivariante y A/B puede (¡y debe!) inspirar ideas para pruebas futuras, así como guiarle hacia cambios en su estrategia de mensajería. Entre las posibles acciones de seguimiento se incluyen las siguientes:

#### Cambie su estrategia de mensajería en función de los resultados de las pruebas

Sus resultados multivariantes pueden llevarle a cambiar la forma de redactar o dar formato a sus mensajes.

#### Cambiar la forma de entender a los usuarios

Cada prueba arrojará luz sobre los comportamientos de sus usuarios, cómo responden a los distintos canales de mensajería y las diferencias (y similitudes) entre sus segmentos.

#### Mejorar la estructura de los futuros exámenes

¿La muestra era demasiado pequeña? ¿Eran demasiado sutiles las diferencias entre sus variantes? Cada prueba brinda la oportunidad de aprender a mejorar las pruebas futuras. Si tu confianza es baja, el tamaño de tu muestra es demasiado pequeño y deberías ampliarlo para futuras pruebas. Si no encuentra una diferencia clara entre los resultados de sus variantes, es posible que las diferencias fueran demasiado sutiles para tener un efecto perceptible en las respuestas de los usuarios.

#### Realiza una prueba de seguimiento con una muestra de mayor tamaño

Las muestras más grandes aumentarán las posibilidades de detectar pequeñas diferencias entre variantes.

#### Haz una prueba de seguimiento utilizando un canal de mensajería diferente

Si comprueba que una estrategia concreta es muy eficaz en un canal, puede ponerla a prueba en otros. Si un tipo de mensaje es eficaz en un canal pero no en otro, puede llegar a la conclusión de que ciertos canales son más propicios para determinados tipos de mensajes. O tal vez haya una diferencia entre los usuarios más propensos a activar las notificaciones push y los más propensos a prestar atención a los mensajes in-app. En última instancia, realizar este tipo de pruebas le ayudará a conocer cómo interactúa su público con sus diferentes canales de comunicación.

#### Realice una prueba de seguimiento en un segmento diferente de usuarios.

Para ello, cree otra prueba con el mismo canal de mensajería y variantes, pero elija un segmento diferente de usuarios. Por ejemplo, si un tipo de mensajería resulta muy eficaz para los usuarios comprometidos, puede ser útil investigar su efecto en los usuarios no comprometidos. Es posible que los usuarios caducados respondan de forma similar, o que prefieran otra de las otras variantes. Esta prueba le ayudará a conocer mejor sus diferentes segmentos y cómo responden a los distintos tipos de mensajes. ¿Por qué hacer suposiciones sobre sus segmentos cuando puede basar su estrategia en datos?

#### Realiza una prueba de seguimiento basada en la información de una prueba anterior

Utiliza la información que obtengas de las pruebas anteriores para orientar las futuras. ¿Insinúa una prueba anterior que una técnica de mensajería es más eficaz? ¿No está seguro de qué aspecto concreto de una variante la hizo mejor? La realización de pruebas de seguimiento basadas en estas preguntas le ayudará a obtener resultados reveladores sobre sus usuarios.

#### Comparar el impacto a largo plazo de las distintas variantes

Si está realizando pruebas A/B con mensajes de reenganche, no olvide comparar el impacto a largo plazo de las distintas variantes mediante [los Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/). Puedes utilizar los Informes de retención para analizar el impacto de cada variante en el comportamiento de cualquier usuario que elijas días, semanas o un mes después de la recepción del mensaje, y ver si hay una mejora.
