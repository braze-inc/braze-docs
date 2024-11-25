---
nav_title: Análisis de predicciones
article_title: Análisis de predicciones
description: "Este artículo de referencia cubre los distintos componentes incluidos en la página Análisis de predicciones de abandono y cómo pueden utilizarse para tomar decisiones impulsadas y con conocimiento de causa."
page_order: 2

---

# Análisis de predicciones

> Una vez creada y entrenada tu predicción, tendrás acceso a la página **Análisis de predicciones**. Esta página te ayuda a decidir a qué usuarios debes dirigirte en función de su _puntuación de riesgo de abandono_ o categoría. 

En cuanto la predicción haya terminado de entrenarse y esta página esté llena, puedes pasar a utilizar simplemente [filtros]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/messaging_users/#filters) en segmentos o campañas para empezar a utilizar los resultados del modelo. Pero, si quieres ayuda para decidir a quién dirigirte y por qué, esta página puede ayudarte basándose en la precisión histórica del modelo y en tus propios objetivos de negocio. 

**Componentes de análisis**<br>
- [Puntuación de abandono y categoría](#churn_score)<br>
- [Calidad de la predicción](#prediction_quality)<br>
- [Resultados estimados](#estimated_results)<br>
- [Tabla de correlación de abandonos](#correlation_table)

## Resumen

La distribución de las puntuaciones de toda la audiencia de predicción se muestra en la parte superior de la página en un gráfico que puedes ver, por categoría o por puntuación. Los usuarios de las casillas situadas más a la derecha tienen puntuaciones más altas y es más probable que abandonen. Los usuarios de las casillas situadas más a la izquierda tienen menos probabilidades de abandonar. El control deslizante situado bajo el gráfico te permitirá seleccionar una franja de usuarios y estimar cuáles serían los resultados de dirigirte a usuarios en el rango seleccionado de _Puntuación de Riesgo de Abandono_ o categoría.

![][4]{: style="max-width:90%"}

A medida que muevas el control deslizante, la barra de la mitad izquierda del panel inferior te informará de a cuántos usuarios de toda la audiencia de predicción se dirigiría la predicción.

## Puntuación de abandono y categoría {#churn_score}

A los usuarios de la audiencia de predicción se les asignará una _Puntuación de Riesgo de Abandono_ entre 0 y 100. Cuanto mayor sea la puntuación, mayor será la probabilidad de abandono. 
- Los usuarios con puntuaciones entre 0 y 50 serán etiquetados en la categoría de _Riesgo Bajo_. 
- Los usuarios con puntuaciones entre 50 y 75, y entre 75 y 100 serán etiquetados en las categorías de _Riesgo Medio_ y _Riesgo Alto_, respectivamente. 

Las puntuaciones y las categorías correspondientes se actualizarán según el calendario que hayas elegido en la página de creación del modelo. El número de usuarios con puntuaciones de abandono en cada uno de los 20 contenedores de igual tamaño se muestra en el gráfico de la parte superior de la página. Esto puede ayudarte a determinar cómo es el riesgo de abandono en toda la población según esta predicción.

## Dirigirse a los usuarios para reducir la tasa de abandonos

### Calidad de la predicción {#prediction_quality}

Para medir la precisión de tu modelo, la métrica _Calidad de predicción_ te mostrará la eficacia que parece tener este modelo de aprendizaje automático concreto cuando se prueba con datos históricos. Consulta [Calidad de la predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn/prediction_analytics/prediction_quality/) para saber más sobre la métrica.

Esto es lo que recomendamos para distintos rangos de _Calidad de predicción_:

| Rango de calidad de la predicción (%) | Recomendación |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisión de primer nivel. Es probable que cambiar las definiciones de audiencia no ofrezca ningún beneficio adicional. |
| 40 - 60 | Bien. Este modelo producirá predicciones precisas, pero probar una configuración de audiencia diferente podría dar mejores resultados. |
| 20 - 40| Justo. Este modelo puede ofrecer precisión y valor, pero considera probar otras definiciones de audiencia para ver si se incrementa el rendimiento. |
| 0 - 20 | Pobre. Te recomendamos que cambies las definiciones de audiencia y vuelvas a intentarlo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La predicción se entrenará de nuevo cada dos semanas y se actualizará junto con la métrica de calidad de la predicción para mantener tus predicciones actualizadas sobre los patrones de comportamiento más recientes de los usuarios. La última vez que se produjo este reentrenamiento se mostrará en la página de la lista de predicciones, así como en la página de análisis de tu predicción.

## Resultados estimados {#estimated_results}

![][6]{: style="float:right;max-width:30%;margin-left:15px;"}

En la mitad derecha del panel, debajo del gráfico, mostramos estimaciones de la precisión esperada al dirigirnos a esta franja de la audiencia de predicción. Basándose en los datos sobre los usuarios de la audiencia de predicción en el pasado, y en la aparente precisión del modelo para discriminar entre los usuarios que abandonan y los que no abandonan en esos datos pasados, estas barras de progreso hacen una estimación para un futuro mensaje potencial utilizando la audiencia resaltada con el control deslizante:

1. Una estimación de cuántos usuarios que abandonan se seleccionarán correctamente <br><br> Por supuesto, no conocemos el futuro a la perfección, así que no sabemos con precisión qué usuarios de la audiencia de predicción abandonarán en el futuro. Pero la predicción es una inferencia fiable. Basándose en rendimientos anteriores, esta barra de progreso indica cuántos de los usuarios que abandonan "reales" o "verdaderos" que se esperan en la audiencia de predicción (basándose en las tasas de abandono anteriores) serán el objetivo de la selección de objetivos actual. Es de esperar que este número de usuarios abandone si no les envías mensajes adicionales o inusuales. <br><br>

2. Una estimación de cuántos usuarios que en realidad no habrían abandonado se seleccionarán incorrectamente.<br><br>Todos los modelos de aprendizaje automático cometen errores. Puede haber usuarios en tu selección que tengan una _Puntuación de Riesgo de Abandono_ alta, pero que no acaben abandonando. No abandonarían aunque no hicieras nada. Serán objetivo de todos modos, por lo que se trata de un error o "falso positivo". La anchura total de esta segunda barra de progreso representa el número previsto de usuarios que no abandonarán, y la parte rellena es la de aquellos a los que se dirigirá incorrectamente utilizando la posición actual del deslizador.

Con esta información, te animamos a que decidas cuántos de los usuarios que abandonan quieres captar y cuál es el coste de un error falso positivo para tu empresa. Si envías una promoción valiosa, es posible que quieras reducir al mínimo el número de usuarios que no abandonan, y conseguir tantos usuarios que abandonan como permita el modelo. O, si eres menos sensible a los falsos positivos y los usuarios reciben mensajes adicionales, puedes enviar mensajes a una mayor parte de la audiencia para captar a más usuarios que abandonan e ignorar los errores probables.

## Tabla de correlación de abandonos {#correlation_table}

Este análisis muestra cualquier atributo o comportamiento del usuario que esté correlacionado con el abandono de usuarios en la audiencia de predicción histórica. Las tablas se dividen en izquierda y derecha para los más y los menos propensos al abandono, respectivamente. Para cada fila, en la columna de la derecha se muestra la proporción en la que los usuarios con el comportamiento o atributo de la columna de la izquierda son más o menos propensos al abandono. Este número es el cociente de la probabilidad de abandono de los usuarios con este comportamiento o atributo dividido por la probabilidad de abandono de toda la audiencia de predicción.

Esta tabla sólo se actualiza cuando se reentrena la predicción y no cuando se actualizan _las puntuaciones de riesgo de abandono de_ usuarios.

{% alert note %}
Los datos de correlación de las predicciones de la vista previa estarán parcialmente ocultos. Se requiere una compra para revelar esta información. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}

[6]: {% image_buster /assets/img/churn/churnEstimatedResults.png %}
[4]: {% image_buster /assets/img/churn/churnTargeting.gif %}