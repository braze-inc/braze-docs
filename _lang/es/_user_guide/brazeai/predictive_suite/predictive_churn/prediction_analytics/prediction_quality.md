---
nav_title: Calidad de la predicción
title: Calidad de la predicción
description: "Este artículo de referencia analiza en profundidad la métrica de calidad de las predicciones situada en la Página de análisis de predicciones."
page_order: 1
Tool:
  - Dashboard
---

# Calidad de la predicción

> Para medir la precisión de tu modelo, la métrica _Calidad de predicción_ te mostrará la eficacia que parece tener este modelo de aprendizaje automático concreto cuando se prueba con datos históricos. Braze extrae los datos según los grupos que hayas especificado en la página de creación del modelo. El modelo se entrena con un conjunto de datos (el conjunto de "entrenamiento") y luego se prueba con otro conjunto de datos distinto (el conjunto de "prueba"). 

Nuestra medida de la _calidad de la predicción_ es [la calidad del ascensor](https://dl.acm.org/doi/10.1145/380995.381018). Probablemente estés familiarizado con la "elevación", que a menudo mide el aumento, en forma de ratio o porcentaje, de algún resultado satisfactorio, como una conversión. En este caso, el resultado satisfactorio es identificar correctamente a un usuario que habría abandonado. La calidad de elevación es la elevación media que proporciona la predicción en todos los tamaños de audiencia posibles para la mensajería del conjunto de prueba. Este enfoque mide cuánto mejor que la adivinación aleatoria es el modelo. Con esta medida, 0% significa que el modelo no es mejor que adivinar al azar quién abandonará, y 100% indica un conocimiento perfecto de quién abandonará.

Esto es lo que recomendamos para distintos rangos de _Calidad de predicción_:

| Rango de calidad de la predicción (%) | Recomendación |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisión de primer nivel. Es probable que cambiar las definiciones de audiencia no ofrezca ningún beneficio adicional. |
| 40 - 60 | Bien. Este modelo producirá predicciones precisas, pero probar una configuración de audiencia diferente podría dar mejores resultados. |
| 20 - 40| Justo. Este modelo puede ofrecer precisión y valor, pero considera probar otras definiciones de audiencia para ver si se incrementa el rendimiento. |
| 0 - 20 | Pobre. Te recomendamos que cambies las definiciones de audiencia y vuelvas a intentarlo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La predicción se entrenará de nuevo cada dos semanas y se actualizará junto con la métrica _Calidad de la predicción_ para mantener tus predicciones actualizadas sobre los patrones de comportamiento más recientes de los usuarios. Además, cada vez que esto ocurra, las predicciones de las dos últimas semanas se contrastarán con los resultados reales de los usuarios. La _calidad de la predicción_ se calculará a partir de estos resultados reales (en lugar de estimaciones). Se trata de un backtest automático (es decir, probar un modelo predictivo con datos históricos) para garantizar que la predicción es exacta en escenarios reales. La última vez que se produjo este reentrenamiento y backtesting se mostrará en la página **Predicciones** y en la página de análisis de una predicción individual. Incluso una predicción con vista previa realizará este backtest una vez después de su creación. De este modo, puedes estar seguro de la exactitud de tu predicción personalizada, incluso con la versión gratuita de la característica.

{% details Predicción Detalles de calidad %}

Por ejemplo, si el 20% de tus usuarios suelen abandonar por término medio, y eliges un subconjunto aleatorio del 20% de tus usuarios y los etiquetas como abandonados al azar (lo estén realmente o no), esperarías identificar correctamente sólo al 20% de los usuarios que abandonan realmente. Eso son suposiciones al azar. Si el modelo sólo lo hiciera así de bien, la elevación sería 1 para este caso.

Si, por el contrario, el modelo te permitiera mensajear al 20% de los usuarios y, al hacerlo, captar a todos los "verdaderos" usuarios que abandonan y a nadie más, la elevación sería del 100% / 20% = 5. Si graficas esta relación para cada proporción de los usuarios que abandonan más probablemente a los que podrías enviar mensajes, obtendrás la [Curva de Elevación](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). 

Otra forma de considerar la calidad de la predicción (y también _la calidad de la predicción_) es la distancia entre la suposición aleatoria (0%) y la perfección (100%) de la curva de predicción para identificar a los usuarios que abandonan en el conjunto de pruebas. Para consultar el artículo original sobre la calidad de la elevación, consulta [Medir la calidad de la elevación en el marketing de bases de datos](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}
