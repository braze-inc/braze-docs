---
nav_title: Correlación de conversión
article_title: Correlación de conversión
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "Este artículo de referencia explica el análisis de correlación de conversiones en la página de Campaign Analytics."
tool: 
  - Reports
  
---

# Correlación de conversión

> El análisis de correlación de conversiones de la página **Análisis de campañas** le ofrece información sobre qué atributos y comportamientos de los usuarios favorecen o perjudican los resultados que establece para las campañas. 

## Resumen

Para cada campaña, Braze comprueba una lista de atributos y comportamientos de los usuarios y calcula si los usuarios están asociados de forma estadísticamente significativa con aumentos o descensos en cada uno de los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) que ha elegido para la campaña. También calculamos la probabilidad mayor o menor de conversión de los usuarios con el atributo o comportamiento en cuestión y, si es significativa, la mostramos en el lado correspondiente de la tabla. Los usuarios con cada atributo o comportamiento de interés se comparan con las tasas de toda la audiencia de la campaña en su conjunto. Los comportamientos y atributos que no tienen una correlación significativa con la conversión no se muestran en la tabla.

Para ejecutar un análisis de correlación de conversiones, seleccione el evento de conversión de interés en el menú desplegable.

![Panel de correlación de conversiones que muestra un ejemplo con "Seleccionar un evento de conversión" establecido en "Evento de conversión primaria - A" con la configuración de evento como "Realizada la compra en 12 horas (Cualquier producto)".]({% image_buster /assets/img/convcorr.png %})

## ¿Qué se comprueba?

Comprobamos los siguientes atributos tratándolos como variables categóricas. En otras palabras, un usuario tiene o no tiene cada uno de los valores posibles de estos atributos, y comprobamos si afectan a la tasa de conversión.

-  País
-  Idioma
-  Género

También comprobamos si lo siguiente afecta a la tasa de conversión:

- Realización de eventos personalizados
- Campañas y lonas recibidas en los últimos 30 días (distintas de la campaña que se está evaluando actualmente)

Por último, comprobamos varias variables de comportamiento que pueden adoptar múltiples valores. Dividimos los siguientes datos en cuatro grupos o cuartiles y luego medimos la asociación de estar en ese cuartil con aumentos o disminuciones de la conversión:

- Edad
- Total de dólares gastados
- Número de sesiones

## ¿Cuándo puedo comprobar este análisis?

Este análisis está disponible al menos 24 horas después de que se inicie el envío de una campaña y sólo tiene en cuenta los envíos realizados en los últimos 30 días. Si no hay comportamientos o atributos significativamente correlacionados con ninguno de los eventos de conversión de la campaña, el menú desplegable se desactivará y se mostrará un mensaje informándole de ello.

## Cómo comprueba Braze la significación

Comprobamos la significación estadística utilizando el [intervalo de confianza de Wilson](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). Determinamos con un 95 % de confianza la tasa de conversión de toda la audiencia de la campaña. Se denomina tasa básica. 

A continuación, para cada una de las variables, calculamos también la tasa de conversión de los usuarios con ese atributo o comportamiento de interés concreto con un 95% de confianza. Dividiéndolo por la tasa básica, podemos medir la relación. Si es mucho mayor que 1, los usuarios con ese atributo o comportamiento tienen más probabilidades de convertir. Si es mucho menor, tienen menos probabilidades. En la tabla mostramos el valor del propio coeficiente. El valor sólo se muestra si está lo suficientemente lejos de 1 como para ser significativo con un nivel de confianza del 95%.

