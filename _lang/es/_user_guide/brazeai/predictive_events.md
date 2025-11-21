---
nav_title: Eventos de predicción
article_title: Eventos de predicción
description: "Este artículo trata de los Eventos predictivos (antes Compras predictivas), una herramienta que ofrece a los especialistas en marketing la posibilidad de identificar y enviar mensajes a los usuarios en función de su probabilidad de realizar un evento."
page_order: 2.1
alias: /predictive_purchases/
search_rank: 1
---

# Eventos de predicción

> Los Eventos Predictivos proporcionan a los especialistas en marketing una potente herramienta para identificar y enviar mensajes a los usuarios en función de su probabilidad de realizar un evento. Cuando creas una predicción de evento, Braze entrena un modelo de aprendizaje automático utilizando [árboles de decisión con gradiente reforzado](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender de la actividad previa y predecir la actividad futura.

## Acerca de los eventos de predicción

Una vez elaborada la predicción, se asigna a los usuarios una [puntuación de probabilidad]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) entre 0 y 100, que denota la probabilidad de que realicen el evento seleccionado. Cuanto mayor sea la puntuación, más probable es que el usuario realice ese evento. Los usuarios también se clasifican por categorías de probabilidad baja, media y alta.

El verdadero valor de los Eventos Predictivos reside en utilizar los resultados de la predicción para crear un segmento o una campaña. Los especialistas en marketing pueden crear campañas específicas directamente en la página de **predicción** para obtener resultados inmediatos que aumenten los ingresos, o guardar un segmento para una futura campaña o Canvas. ¿No sabes a quién dirigirte primero? Lee nuestras [consideraciones estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para enviar mensajes a los usuarios en función de su puntuación de probabilidad.

\![Gráfico titulado "Cómo funcionan los eventos de predicción", que muestra cómo se embudan los datos de usuario en el modelo de aprendizaje automático. La etiqueta dice "Entrena con datos históricos, compara el comportamiento de los usuarios que sí realizaron el evento en un periodo determinado con los que no". También muestra los resultados del aprendizaje automático, donde se clasifica a los usuarios de menor a mayor probabilidad de realizar el evento. La etiqueta dice "Predecir la probabilidad de sucesos futuros, asignar una puntuación de probabilidad a los usuarios para una orientación precisa y conveniente."]({% image_buster /assets/img/how_predictive_events_works.png %})

## Acceso a los eventos de predicción

La página **Predicciones** se encuentra en la sección **Análisis**. Para obtener acceso completo, ponte en contacto con tu director de cuentas.

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de demostración con datos sintéticos, así como crear un modelo de predicción de vista previa cada vez. Esta predicción se creará basándose en tus datos de usuario reales, pero no te permitirá dirigirte a los usuarios para enviarles mensajes según su puntuación de probabilidad. Tampoco se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir esta única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) esperada de [diferentes audiencias]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) y familiarizarte con los análisis.
