---
nav_title: Análisis de eventos
article_title: Análisis predictivo de sucesos
description: "Este artículo de referencia cubre los distintos componentes incluidos en la página Análisis de predicciones y cómo pueden utilizarse para tomar decisiones basadas en la información."
page_order: 1.3

---

# Análisis predictivo de acontecimientos

> Una vez creada y entrenada tu predicción, tendrás acceso a la página **Análisis de predicciones**. Esta página te ayuda a decidir a qué usuarios debes dirigirte en función de su puntuación de probabilidad o categoría.

## Acerca del análisis predictivo de eventos

En cuanto la predicción haya terminado de entrenarse y esta página esté llena, puedes empezar a utilizar [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) en segmentos o campañas para empezar a utilizar los resultados del modelo. Si quieres ayuda para decidir a quién dirigirte y por qué, esta página puede ayudarte basándose en la precisión histórica del modelo y en tus propios objetivos de negocio.

Estos son los componentes del análisis predictivo de eventos:

- [Puntuación de probabilidad](#purchase_score)
- [Calidad de la predicción](#prediction_quality)
- [Precisión estimada](#estimated_results)
- [Tabla de correlación de sucesos](#correlation_table)

La distribución de las puntuaciones de probabilidad de toda la audiencia de predicción se muestra en la parte superior de la página. Los usuarios de los contenedores situados más a la derecha tienen puntuaciones más altas y es más probable que realicen el evento. Los usuarios de los contenedores situados más a la izquierda tienen menos probabilidades de realizar el evento. El control deslizante situado debajo del gráfico te permitirá seleccionar una sección de usuarios y estimar cuáles serían los resultados de dirigirte a esos usuarios.

A medida que muevas los controles deslizantes a diferentes posiciones, la barra de la mitad izquierda del panel te informará de cuántos usuarios de toda la audiencia de predicción se dirigirían utilizando la parte de la población que hayas seleccionado.

\![]({% image_buster /assets/img/purchasePrediction/purchaseTargeting.png %}){: style="max-width:90%"} 

## Puntuación de probabilidad {#purchase_score}

A los usuarios de la audiencia de predicción se les asignará una puntuación de probabilidad entre 0 y 100. Cuanto mayor sea la puntuación, mayor será la probabilidad de realizar el evento. 

A continuación se muestra cómo se clasifica a un usuario en función de su puntuación de probabilidad:

- **Bajo:** entre 0 y 50
- **Medio:** entre 50 y 75
- **Alta:** entre 75 y 100

Las puntuaciones y las categorías correspondientes se actualizarán según el calendario que hayas elegido en la página de **creación de predicciones**. El número de usuarios con puntuaciones de probabilidad en cada uno de los 20 contenedores de igual tamaño o en cada una de las categorías de probabilidad, se muestra en el gráfico de la parte superior de la página.

## Precisión estimada {#estimated_results}

En la mitad derecha del panel, debajo del gráfico, mostramos estimaciones de la precisión esperada de dirigirte a la parte de la audiencia de predicción que seleccionaste de dos formas: cuántos usuarios seleccionados se espera que realicen el evento y cuántos se espera que no lo hagan.

La audiencia seleccionada y la precisión estimada se muestran en el panel de Braze.]({% image_buster /assets/img/purchasePrediction/purchaseEstimatedResults.png %})

### Rendimiento esperado

Puedes utilizar la precisión estimada para comprobar cuántos usuarios seleccionados se espera que realicen el evento.

La predicción no es perfectamente exacta, y ninguna predicción lo es nunca, lo que significa que Braze no podrá identificar a todos y cada uno de los futuros usuarios que realicen el evento. Las puntuaciones de probabilidad son como un conjunto de predicciones informadas y fiables. La barra de progreso indica cuántos de los "verdaderos positivos" esperados en la audiencia de predicción se dirigirán a la audiencia seleccionada. Ten en cuenta que esperamos que este número de usuarios realice el evento aunque no les envíes ningún mensaje.

### No se espera que rinda

Puedes utilizar la precisión estimada para comprobar cuántos usuarios seleccionados se espera que no realicen el evento.

Todos los modelos de aprendizaje automático cometen errores. Puede haber usuarios en tu selección que tengan una puntuación de probabilidad alta, pero que no acaben realizando realmente el evento. No realizarían el acto si no hicieras nada. Serán objetivo de todos modos, por lo que se trata de un error o "falso positivo". La anchura total de esta segunda barra de progreso representa el número previsto de usuarios que no realizarán el evento, y la parte rellena es la de aquellos a los que se dirigirá incorrectamente utilizando la posición actual del deslizador.

Utilizando esta información, te animamos a que decidas cuántos de los verdaderos positivos quieres capturar, cuántos falsos positivos puedes aceptar que sean objetivo, y cuál es el coste de los errores para tu empresa. Si envías una promoción valiosa, quizá quieras dirigirte sólo a los no compradores (falsos positivos) favoreciendo el lado izquierdo del gráfico. O puede que quieras animar a los compradores que compran a menudo (verdaderos positivos) a que vuelvan a hacerlo seleccionando una sección de usuarios que favorezca el lado derecho del gráfico.

## Calidad de la predicción {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Tabla de correlación de sucesos {#correlation_table}

Este análisis muestra los atributos o comportamientos de los usuarios que están correlacionados con los acontecimientos de la audiencia de predicción. Los atributos evaluados son Edad, País, Sexo e Idioma. Los comportamientos que se analizan incluyen sesiones, compras, total de dólares gastados, eventos personalizados y campañas y pasos en Canvas recibidos en los últimos 30 días.

Las tablas se dividen en izquierda y derecha para los más y los menos propensos a realizar el evento, respectivamente. Para cada fila, en la columna de la derecha se muestra la proporción en la que los usuarios con el comportamiento o atributo de la columna de la izquierda tienen más o menos probabilidades de realizar el evento. Este número es el cociente de las puntuaciones de probabilidad de los usuarios con este comportamiento o atributo dividido por la probabilidad de realizar el evento de toda la audiencia de predicción.

Esta tabla sólo se actualiza cuando se reentrena la predicción y no cuando se actualizan las puntuaciones de probabilidad del usuario.

{% alert note %}
Los datos de correlación de las predicciones de la vista previa estarán parcialmente ocultos. Se requiere una compra para revelar esta información. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}
