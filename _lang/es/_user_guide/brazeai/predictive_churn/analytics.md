---
nav_title: Análisis del abandono de clientes
article_title: Análisis predictivo del abandono de clientes
description: "Este artículo de referencia cubre los distintos componentes incluidos en la página Análisis de predicciones de abandono y cómo pueden utilizarse para tomar decisiones impulsadas y con conocimiento de causa."
page_order: 1.5

---

# Análisis predictivos del abandono de clientes

> Una vez creada y entrenada tu predicción, tendrás acceso a la página **Análisis de predicciones**. Esta página te ayuda a decidir a qué usuarios debes dirigirte en función de su _puntuación de riesgo de abandono_ o categoría. 

## Acerca del análisis predictivo del abandono de clientes

En cuanto la predicción haya terminado de entrenarse y esta página esté llena, puedes pasar a utilizar simplemente [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) en segmentos o campañas para empezar a utilizar los resultados del modelo. Pero, si quieres ayuda para decidir a quién dirigirte y por qué, esta página puede ayudarte basándose en la precisión histórica del modelo y en tus propios objetivos de negocio. 

Estos son los componentes del análisis predictivo del abandono:

- [Puntuación de abandono y categoría](#churn_score)
- [Calidad de la predicción](#prediction_quality)
- [Precisión estimada](#estimated_results)
- [Tabla de correlación de abandonos](#correlation_table)

La distribución de las puntuaciones de toda la audiencia de predicción se muestra en la parte superior de la página en un gráfico que puedes ver, por categoría o por puntuación. Los usuarios de las casillas situadas más a la derecha tienen puntuaciones más altas y es más probable que abandonen. Los usuarios de las casillas situadas más a la izquierda tienen menos probabilidades de abandonar. El control deslizante situado bajo el gráfico te permitirá seleccionar una franja de usuarios y estimar cuáles serían los resultados de dirigirte a usuarios en el rango seleccionado de _Puntuación de Riesgo de Abandono_ o categoría.

A medida que muevas el control deslizante, la barra de la mitad izquierda del panel inferior te informará de a cuántos usuarios de toda la audiencia de predicción se dirigiría la predicción.

![]({% image_buster /assets/img/churn/churnTargeting.gif %})

## Puntuación de abandono y categoría {#churn_score}

A los usuarios de la audiencia de predicción se les asignará una _Puntuación de Riesgo de Abandono_ entre 0 y 100. Cuanto mayor sea la puntuación, mayor será la probabilidad de abandono. 
- Los usuarios con puntuaciones entre 0 y 50 serán etiquetados en la categoría de _Riesgo Bajo_. 
- Los usuarios con puntuaciones entre 50 y 75, y entre 75 y 100 serán etiquetados en las categorías de _Riesgo Medio_ y _Riesgo Alto_, respectivamente. 

Las puntuaciones y las categorías correspondientes se actualizarán según el calendario que hayas elegido en la página de creación del modelo. El número de usuarios con puntuaciones de abandono en cada uno de los 20 contenedores de igual tamaño se muestra en el gráfico de la parte superior de la página. Esto puede ayudarte a determinar cómo es el riesgo de abandono en toda la población según esta predicción.

## Calidad de la predicción {#prediction_quality}

{% multi_lang_include brazeai/predictive_suite/prediction_quality.md %}

## Precisión estimada {#estimated_results}

En la mitad derecha del panel, debajo del gráfico, mostramos estimaciones de la precisión esperada al dirigirnos a esta franja de la audiencia de predicción. Basándose en los datos sobre los usuarios de la audiencia de predicción en el pasado, y en la aparente precisión del modelo para discriminar entre los usuarios que abandonan y los que no abandonan en esos datos pasados, estas barras de progreso hacen una estimación para un futuro mensaje potencial utilizando la audiencia resaltada con el control deslizante:

![]({% image_buster /assets/img/churn/churnEstimatedResults.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

- Cuántos usuarios seleccionados se prevé que cancelen
- ¿Cuántos usuarios seleccionados se espera que **no** abandonen?

Con esta información, te animamos a que decidas cuántos de los usuarios que abandonan quieres captar y cuál es el coste de un error falso positivo para tu empresa. Si envías una promoción valiosa, es posible que quieras reducir al mínimo el número de usuarios que no abandonan, y conseguir tantos usuarios que abandonan como permita el modelo. O, si eres menos sensible a los falsos positivos y los usuarios reciben mensajes adicionales, puedes enviar mensajes a una mayor parte de la audiencia para captar a más usuarios que abandonan e ignorar los errores probables.

### Usuarios que se espera que abandonen

Es una estimación del número de usuarios que abandonan correctamente. Por supuesto, no conocemos el futuro a la perfección, así que no sabemos con precisión qué usuarios de la audiencia de predicción abandonarán en el futuro. Pero la predicción es una inferencia fiable. Basándose en rendimientos anteriores, esta barra de progreso indica cuántos de los usuarios que abandonan "reales" o "verdaderos" que se esperan en la audiencia de predicción (basándose en las tasas de abandono anteriores) serán el objetivo de la selección de objetivos actual. Es de esperar que este número de usuarios abandone si no les envías mensajes adicionales o inusuales.

### Se espera que los usuarios no abandonen 

Se trata de una estimación del número de usuarios que no habrían abandonado y a los que se dirigirá incorrectamente. Todos los modelos de aprendizaje automático cometen errores. Puede haber usuarios en tu selección que tengan una _Puntuación de Riesgo de Abandono_ alta, pero que no acaben abandonando. No abandonarían aunque no hicieras nada. Serán objetivo de todos modos, por lo que se trata de un error o "falso positivo". La anchura total de esta segunda barra de progreso representa el número previsto de usuarios que no abandonarán, y la parte rellena representa a los que se dirigirán incorrectamente utilizando la posición actual del deslizador.

## Tabla de correlación de abandonos {#correlation_table}

Este análisis muestra cualquier atributo o comportamiento del usuario que esté correlacionado con el abandono de usuarios en la audiencia de predicción histórica. Las tablas se dividen en izquierda y derecha para los más y los menos propensos al abandono, respectivamente. Para cada fila, en la columna de la derecha se muestra la proporción en la que los usuarios con el comportamiento o atributo de la columna de la izquierda son más o menos propensos al abandono. Este número es el cociente de la probabilidad de abandono de los usuarios con este comportamiento o atributo dividido por la probabilidad de abandono de toda la audiencia de predicción.

Esta tabla sólo se actualiza cuando se reentrena la predicción y no cuando se actualizan _las puntuaciones de riesgo de abandono de_ usuarios.

{% alert note %}
Los datos de correlación de las predicciones de la vista previa estarán parcialmente ocultos. Se requiere una compra para revelar esta información. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}
