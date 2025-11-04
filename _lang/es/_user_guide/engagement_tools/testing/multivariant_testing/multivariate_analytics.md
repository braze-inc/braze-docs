---
nav_title: Análisis
article_title: Análisis de pruebas multivariantes y A/B
page_order: 10
page_type: reference
description: "Este artículo explica cómo ver e interpretar los resultados de una campaña multivariante o A/B."
---

# Análisis de pruebas multivariantes y A/B

> Este artículo explica cómo ver los resultados de una prueba multivariante o A/B. Si aún no has configurado tu prueba, consulta [Crear pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para ver los pasos a seguir.

Una vez lanzada tu campaña, puedes comprobar el rendimiento de cada variante seleccionando tu campaña en la sección **Campañas** del panel. 

## Análisis por opción de optimización

Tu vista de análisis variará dependiendo de si seleccionaste una [optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) durante la configuración inicial.

### Sin optimización

Si seleccionaste **Sin optimización** al configurar tu campaña, tu vista de análisis seguirá siendo la misma. La página de **análisis de** campaña de tu campaña mostrará el rendimiento de tus variantes en comparación con tu grupo de control, si incluiste uno.

\![Sección de rendimiento de los análisis de campaña de una campaña de correo electrónico con múltiples variantes. La tabla enumera diversas métricas de rendimiento para cada variante, como destinatarios, rebotes, clics y conversiones.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para más detalles, consulta el artículo [Análisis de campaña]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para tu canal de mensajería.

### Variante ganadora

Si seleccionaste **Variante ganadora** para tu optimización al configurar tu campaña, tendrás acceso a una pestaña adicional de tus análisis de campaña llamada **Resultado de las pruebas A/B**. Después de enviar la variante ganadora al resto de usuarios de tu prueba, esta pestaña muestra los resultados de ese envío.

El **resultado de las pruebas A/B** se divide en dos pestañas: **Prueba inicial** y **variante ganadora**.

{% tabs local %}
{% tab Initial Test %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de tu segmento objetivo. Puedes ver un resumen de cómo rindieron todas las variantes y si hubo o no un ganador durante la prueba.

Si una variante supera a todas las demás con una [confianza]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) superior al 95%, Braze marca esa variante con la etiqueta "Ganador".

Si ninguna variante supera a todas las demás con un 95% de confianza y eliges enviar la variante de mejor rendimiento de todos modos, se seguirá enviando la variante de mejor rendimiento y se indicará con la etiqueta "Ganador".

\![Resultados de una prueba inicial enviada para determinar la Variante Ganadora en la que ninguna variante rindió mejor que las demás con la suficiente confianza como para alcanzar el umbral de confianza del 95% para la significación estadística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Cómo se selecciona la Variante Ganadora

Braze comprueba todas las variantes entre sí con [las pruebas chi-cuadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Mide si una variante supera estadísticamente a todas las demás con un nivel de significación de p < 0,05, o lo que denominamos significación del 95%. Si es así, la variante ganadora se indica con la etiqueta "Ganador".

Se trata de una prueba independiente de la puntuación de confianza, que sólo describe el rendimiento de una variante en comparación con el control con un valor numérico entre 0 y 100%.

Una variante puede obtener mejores resultados que el grupo de control, pero la prueba de ji al cuadrado comprueba si una variante es mejor que todas las demás. [Las pruebas de seguimiento](#recommended-follow-ups) pueden aportar más detalles.

{% endtab %}
{% tab Winning Variant %}

La pestaña **Variante ganadora** muestra los resultados del segundo envío, en el que a cada usuario restante se le envió la variante con mejor rendimiento de la prueba inicial. Tu **% de audiencia** sumará el porcentaje del segmento objetivo que reservaste para el grupo de la variante ganadora.

\![Resultados de la Variante Ganadora enviados al grupo Variante Ganadora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Si quieres ver el rendimiento de la variante ganadora durante toda la campaña, incluidos los envíos de las pruebas A/B, consulta la página **Análisis de campaña**.

### Variante personalizada {#personalized-variant}

Si seleccionaste **Variante personalizada** para tu optimización al configurar tu campaña, el **Resultado de la prueba A/B** se divide en dos pestañas: **Prueba inicial** y **variante personalizada**.

{% tabs local %}
{% tab Initial Test %}

La pestaña **Prueba inicial** muestra las métricas de cada variante de la prueba A/B inicial enviada a una parte de tu segmento objetivo.

\![Resultados de una prueba inicial enviados para determinar la variante de mejor rendimiento para cada usuario. Una tabla muestra el rendimiento de cada variante en función de diversas métricas para el canal de destino.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por defecto, la prueba busca asociaciones entre los eventos personalizados del usuario y sus preferencias de variantes de mensajes. Este análisis detecta si los eventos personalizados aumentan o disminuyen la probabilidad de responder a una variante de mensaje concreta. Estas relaciones se utilizan después para determinar qué usuarios reciben qué variante de mensaje en el envío final.

Las relaciones entre los eventos personalizados y las preferencias de mensajes se muestran en la tabla de la pestaña **Envío inicial**.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Si la prueba no puede encontrar una relación significativa entre los eventos personalizados y las preferencias de variantes, la prueba volverá a un método de análisis basado en sesiones.

{% details Fallback analysis method %}

**Método de análisis basado en sesiones**<br>
Si se utiliza el método alternativo para determinar las variantes personalizadas, la pestaña **Prueba inicial** muestra un desglose de las variantes preferidas por los usuarios en función de una combinación de determinadas características. 

Estas características son:

- **Recencia:** Cuándo fue la última vez que tuvieron una sesión
- **Frecuencia:** Con qué frecuencia tienen sesiones
- **Tenencia:** Cuánto tiempo llevan siendo usuarios

Por ejemplo, la prueba puede descubrir que la mayoría de los usuarios prefieren la variante A, pero los usuarios que tuvieron una sesión hace unos 3-12 días, tienen entre 1-12 días entre sesiones y fueron creados en los últimos 67-577 días tienden a preferir la variante B. Por lo tanto, los usuarios de esa subpoblación recibieron la variante B en el segundo envío, mientras que el resto recibió la variante A.

\![La tabla de características de los usuarios, que muestra qué usuarios se prevé que prefieran la variante A y la variante B en función de los tres contenedores en los que se encuentran por antigüedad, frecuencia y permanencia.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Cómo se seleccionan las variantes personalizadas**<br>
Con este método, el mensaje recomendado a un usuario individual es la suma de los efectos de su recencia, frecuencia y permanencia específicas. La recurrencia, la frecuencia y la permanencia se dividen en contenedores, como se ilustra en la tabla **Características del usuario**. El intervalo de tiempo de cada contenedor viene determinado por los datos de los usuarios de cada campaña individual y cambiará de una campaña a otra. 

Cada contenedor puede tener una contribución o "push" diferente hacia cada variante de mensaje. La fuerza del push para cada contenedor se determina a partir de las respuestas de los usuarios en el envío inicial mediante [regresión logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabla sólo resume los resultados mostrando con qué variante tendían a interactuar los usuarios de cada contenedor. La Variante Personalizada real de cualquier usuario individual depende de la suma de los efectos de los tres contenedores en los que se encuentra: uno por cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

La pestaña **Variante personalizada** muestra los resultados del segundo envío, en el que se envió a cada usuario restante la variante con la que tenía más probabilidades de interactuar.

Las tres tarjetas de esta página muestran tu ascensor proyectado, los resultados globales y los resultados proyectados si en lugar de eso enviaras sólo la variante ganadora. Aunque no haya subida, lo que a veces puede ocurrir, el resultado es el mismo que enviar sólo la variante ganadora (una prueba A/B tradicional). 

- **Ascensor proyectado:** La mejora en tu métrica de optimización seleccionada para este envío debido al uso de Variantes Personalizadas en lugar de una prueba A/B estándar (si los usuarios restantes sólo recibieron la Variante Ganadora).
- **Resultados globales:** Los resultados del segundo envío se basan en la métrica de optimización que hayas elegido*(Unique Opens*, *Unique Clics* o *evento de conversión primaria*).
- **Resultados previstos:** Los resultados previstos del segundo envío en función de la métrica de optimización que hayas elegido, si en lugar de eso hubieras enviado sólo la variante ganadora. 

\![pestaña Variante personalizada para una campaña optimizada para Unique Opens. Las tarjetas muestran el Ascenso Proyectado, las Aperturas Únicas Totales (con Variante Personalizada) y las Aperturas Únicas Proyectadas (con Variante Ganadora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

La tabla de esta página muestra las métricas de cada variante del envío Variante personalizada. **El % de** tu **audiencia** suma el porcentaje del segmento objetivo que reservaste para el grupo de la variante personalizada.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Comprender la confianza {#understanding-confidence}

La confianza es la medida estadística de nuestra certeza de que una diferencia en los datos, como las tasas de conversión, es real y no se debe al azar.

{% alert note %}
¿No ves confianza en tus resultados? La confianza sólo aparecerá si tienes un grupo de control.
{% endalert %}

Una parte importante de tus resultados es la confianza en ellos. Por ejemplo, ¿qué pasaría si el grupo de control tuviera una tasa de conversión del 20% y la variante A tuviera una tasa de conversión del 25%? Esto parece indicar que enviar la variante A es más eficaz que no enviar ningún mensaje. Tener una confianza del 95% significa que la diferencia entre las dos tasas de conversión se debe probablemente a una diferencia real en las respuestas de los usuarios y que sólo hay un 5% de probabilidades de que la diferencia se haya producido por casualidad.

Braze compara la tasa de conversión de cada variante con la tasa de conversión del control mediante un procedimiento estadístico llamado [Prueba Z](https://en.wikipedia.org/wiki/Z-test). Un resultado del 95% o más de confianza, como en el ejemplo anterior, indica que la diferencia es estadísticamente significativa. Esto es así en cualquier lugar en el que veas una métrica de confianza en el panel de Braze que describa la diferencia entre dos mensajes o poblaciones de usuarios.

En general, es necesaria una confianza de al menos el 95% para demostrar que tus resultados reflejan las preferencias reales de los usuarios, y no se deben al azar. En las pruebas científicas rigurosas, el 95% de confianza (o lo que es lo mismo, que el valor "p" sea inferior a 0,05) es el punto de referencia habitual para determinar la significación estadística. Si continuamente no consigues un 95% de confianza, prueba a aumentar el tamaño de la muestra o a disminuir el número de variantes. 

La confianza no describe si una variante es mejor que las demás. Es puramente una medida de lo seguros que estamos de que las dos (o más) tasas de conversión son realmente diferentes entre sí. Esto sólo depende del tamaño de la muestra y de las diferencias entre las tasas de conversión aparentes. Que las tasas globales sean altas o bajas no afecta a la solidez de la medida de confianza. Es posible que una variante tenga una tasa de conversión muy diferente de otra y, sin embargo, no tenga una confianza del 95% o superior. También es posible que dos conjuntos de variantes tengan tasas de conversión/elevación similares y, sin embargo, una confianza diferente.

### Resultados estadísticamente insignificantes

Una prueba que no tenga una confianza del 95% puede contener información importante. He aquí algunas cosas que puedes aprender de una prueba con resultados estadísticamente insignificantes:

- Es posible que todas tus variantes tuvieran aproximadamente el mismo efecto. Saber esto te ahorra el tiempo que habrías empleado en hacer estos cambios. A veces, puedes descubrir que las tácticas de marketing convencionales, como repetir tu llamada a la acción, no funcionan necesariamente para tu audiencia.
- Aunque tus resultados pueden haberse debido al azar, pueden informar la hipótesis de tu próxima prueba. Si varias variantes parecen tener aproximadamente los mismos resultados, vuelve a ejecutar algunas de ellas junto con nuevas variantes para ver si puedes encontrar una alternativa más eficaz. Si una variante obtiene mejores resultados, pero no por una cantidad significativa, puedes realizar otra prueba en la que la diferencia de esta variante sea más exagerada.
- ¡Sigue probando! Una prueba con resultados no significativos debería llevar a plantearse ciertas preguntas. ¿Realmente no había diferencia entre tus variantes? ¿Deberías haber estructurado tu prueba de otra manera? Puedes responder a estas preguntas realizando pruebas de seguimiento.
- Aunque las pruebas son útiles para descubrir qué tipo de mensajería genera la mayor respuesta de tu audiencia, también es importante comprender qué alteraciones en la mensajería tienen un efecto insignificante. Esto te permite seguir probando otra alternativa más eficaz, o ahorrarte el tiempo que podrías haber empleado en decidir entre dos mensajes alternativos.

Tanto si tu prueba tiene un claro ganador como si no, puede ser útil realizar una [prueba de seguimiento](#recommended-follow-ups) para confirmar tus resultados o aplicar tus conclusiones a un escenario ligeramente distinto.

## Discrepancias entre el grupo de control y la variante

En las campañas de mensajes dentro de la aplicación, la forma en que se realiza el seguimiento de los usuarios y cómo se registran las impresiones puede causar discrepancias en la división prevista entre el grupo de control y la variante. Esto se debe a que las impresiones reales registradas pueden no reflejar esta división, y en última instancia Braze no tiene control sobre el comportamiento individual del usuario que desencadenará la acción.

Por ejemplo, supongamos que una campaña tiene una audiencia objetivo de 200 usuarios en su lanzamiento, con 100 usuarios en el grupo de control y 100 usuarios en la variante.

Los 100 usuarios de la variante reciben la carga útil del mensaje dentro de la aplicación, y 50 de ellos realizan la acción desencadenante y ven el mensaje dentro de la aplicación. Los 100 usuarios del grupo de control sólo son objeto de seguimiento si realizan la acción desencadenante de la campaña, y 75 de ellos realizan la acción desencadenante y registran una impresión, pero no ven el mensaje dentro de la aplicación.

A pesar del 50/50 inicial, las impresiones únicas registradas no están equilibradas. El grupo de variantes tiene 50 impresiones, mientras que el grupo de control tiene 75 impresiones.

### Retrasos en los mensajes dentro de la aplicación 

Para las campañas de mensajes dentro de la aplicación desencadenadas que incluyan visualizaciones diferidas, las impresiones del grupo de control se registrarán cuando el usuario final hubiera recibido originalmente el mensaje dentro de la aplicación. Por ejemplo, si una campaña está configurada para retrasar la visualización una hora, las impresiones del grupo de control no se registrarán hasta que haya transcurrido el retraso de una hora. Esto ayuda a realizar un seguimiento preciso de las impresiones relacionadas con el momento previsto de la entrega del mensaje.

## Seguimiento recomendado {#recommended-follow-ups}

Una prueba multivariante y A/B puede (¡y debe!) inspirar ideas para pruebas futuras, así como guiarte hacia cambios en tu estrategia de mensajería. Entre las posibles acciones de seguimiento se incluyen las siguientes

#### Cambia tu estrategia de mensajería en función de los resultados de las pruebas

Tus resultados multivariantes pueden llevarte a cambiar la forma en que redactas o formateas tu mensajería.

#### Cambia la forma de entender a tus usuarios

Cada prueba arrojará luz sobre los comportamientos de tus usuarios, cómo responden a los distintos canales de mensajería y las diferencias (y similitudes) entre tus segmentos.

#### Mejora la forma de estructurar los futuros tests

¿El tamaño de tu muestra era demasiado pequeño? ¿Eran demasiado sutiles las diferencias entre tus variantes? Cada prueba ofrece la oportunidad de aprender a mejorar las pruebas futuras. Si tu confianza es baja, el tamaño de tu muestra es demasiado pequeño y deberías ampliarlo para futuras pruebas. Si no encuentras una diferencia clara entre el rendimiento de tus variantes, es posible que las diferencias fueran demasiado sutiles para tener un efecto perceptible en las respuestas de los usuarios.

#### Realiza una prueba de seguimiento con una muestra de mayor tamaño

Las muestras más grandes aumentarán las posibilidades de detectar pequeñas diferencias entre variantes.

#### Haz una prueba de seguimiento utilizando un canal de mensajería diferente

Si descubres que una estrategia concreta es muy eficaz en un canal, quizá quieras probar esa estrategia en otros canales. Si un tipo de mensaje es eficaz en un canal pero no en otro, puedes llegar a la conclusión de que ciertos canales son más propicios para determinados tipos de mensajes. O tal vez haya una diferencia entre los usuarios que son más propensos a habilitar las notificaciones push y los que son más propensos a prestar atención a los mensajes dentro de la aplicación. En última instancia, realizar este tipo de pruebas te ayudará a conocer cómo interactúa tu audiencia con tus distintos canales de comunicación.

#### Realiza una prueba de seguimiento en un segmento diferente de usuarios

Para ello, crea otra prueba con el mismo canal de mensajería y variantes, pero elige un segmento diferente de usuarios. Por ejemplo, si un tipo de mensajería fue extremadamente eficaz para los usuarios comprometidos, puede ser útil investigar su efecto en los usuarios que ya no la utilizan. Es posible que los usuarios caducados respondan de forma similar, o que prefieran otra de las otras variantes. Esta prueba te ayudará a conocer mejor tus diferentes segmentos y cómo responden a distintos tipos de mensajería. ¿Por qué hacer suposiciones sobre tus segmentos cuando puedes basar tu estrategia en los datos?

#### Realiza una prueba de seguimiento basada en la información de una prueba anterior

Utiliza la información que obtengas de las pruebas anteriores para orientar las futuras. ¿Una prueba anterior indica que una técnica de mensajería es más eficaz? ¿No estás seguro de qué aspecto concreto de una variante la hacía mejor? Realizar pruebas de seguimiento basadas en estas preguntas te ayudará a generar información reveladora sobre tus usuarios.

#### Compara el impacto a largo plazo de las distintas variantes

Si estás haciendo pruebas A/B con mensajes de reactivación de la interacción, no olvides comparar el impacto a largo plazo de las distintas variantes utilizando [los Informes de retención]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/). Puedes utilizar los Informes de retención para analizar el impacto de cada variante en el comportamiento de cualquier usuario que elijas días, semanas o un mes después de la recepción del mensaje, y ver si hay una mejora.
