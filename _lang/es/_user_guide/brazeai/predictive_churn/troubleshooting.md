---
nav_title: Solución de problemas
article_title: Solución de problemas de Predictive Churn
description: "Este artículo de referencia cubre algunos pasos para la solución de problemas y consideraciones a tener en cuenta al utilizar Predictive Churn."
page_order: 3

---

# Solución de problemas

> El Predictive Churn (y cualquier modelo de aprendizaje automático) sólo es tan bueno como los datos de que dispone el modelo. También depende en gran medida de disponer de ciertos volúmenes de datos con los que trabajar. 

## Posibles errores

### No hay suficientes datos para entrenar 

Este mensaje de error aparece cuando tu definición de abandono es demasiado restrictiva y devuelve muy pocos usuarios abandonados. 

Para solucionarlo, tendrás que cambiar el número de días y/o las acciones que definen el abandono para captar más usuarios. Asegúrate de que utilizas correctamente los filtros de `AND/OR` para no crear definiciones demasiado restrictivas. 

{% alert important %}
Aunque Predictive Churn esté activado a nivel de empresa, algunos espacios de trabajo pueden no tener suficientes usuarios para construir predicciones. Normalmente, necesitas 300.000 usuarios activos al mes en un único espacio de trabajo.
{% endalert %}

### Problemas con la predicción del tamaño de la audiencia

Cuando construyas tu audiencia de predicción para afinar el tipo de uso con el que quieres entrenar tu modelo, puede que te encuentres con este mensaje que te notifica que tu audiencia de predicción tiene muy pocos usuarios: 

"No hay suficientes usuarios que abandonen para construir de forma fiable la predicción"

Los datos de predicción de requisitos muestran 31 usuarios que abandonan (cumplen los requisitos) y 0 usuarios que no abandonan (por debajo del mínimo). Un mensaje de advertencia indica que no hay suficientes usuarios que abandonen para construir la predicción.]({% image_buster /assets/img/churn/audience_size_error.png %})

Si la definición de tu audiencia de predicción es demasiado estricta, es posible que no dispongas de un conjunto suficientemente amplio de usuarios históricos y activos con los que trabajar. Para solucionarlo, tendrás que cambiar el número de días y el tipo de atributos utilizados en esta definición, cambiar las acciones que definen el abandono, o ambas cosas. 

Si tu audiencia de predicción sigue siendo un problema incluso después de cambiar tus definiciones, puede que tengas muy pocos usuarios para admitir esta característica opcional. Te sugerimos que intentes hacer una predicción sin capas ni filtros adicionales. 

### El tamaño de la audiencia de predicción es demasiado grande

La definición de una audiencia de predicción no puede superar los 100 millones de usuarios. Si ves un mensaje que dice que tu audiencia es demasiado grande, te recomendamos que añadas más capas a tu audiencia o que cambies la ventana de tiempo en la que se basa.

### La predicción tiene mala calidad

\![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Si tu modelo tiene una [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) del 40% o superior, ¡estás en un buen lugar! Pero si la calidad de tu predicción desciende al 39% o menos, puede que tengas que editar las definiciones de tus audiencias de abandono y predicción para que sean más específicas o tengan ventanas temporales diferentes. 

Si no puedes cumplir tanto el requisito del tamaño de la audiencia al construir tus definiciones de predicción como lograr una calidad de predicción superior al 40%, probablemente significa que los datos enviados a Braze no son ideales para este caso de uso, que no hay suficientes usuarios con los que construir un modelo, o que el ciclo de vida de tu producto es más largo de lo que admite nuestra ventana de revisión retrospectiva actual de 60 días. 

## Consideraciones sobre los datos

Las siguientes son preguntas que debes hacerte al configurar Predictive Churn. Los modelos de aprendizaje automático sólo son tan buenos como los datos que los entrenan, por lo que tener buenas prácticas de higiene de datos y comprender lo que entra en el modelo marcará una gran diferencia.

- ¿Qué acciones de alto valor conducen a la retención y la fidelización?
- ¿Has configurado eventos personalizados que se mapeen con estas acciones específicas? Predictive Churn funciona con eventos personalizados, no con atributos personalizados.
- ¿Piensas en ventanas de tiempo dentro de las cuales definirás el abandono? Puedes definir el abandono como algo que ocurre hasta en 60 días.
- ¿Has tenido en cuenta las épocas del año que dan lugar a comportamientos atípicos de los usuarios, como las vacaciones? Los rápidos cambios en el comportamiento de los consumidores afectarán a tus predicciones. 

