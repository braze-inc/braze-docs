---
nav_title: Eventos predecibles
article_title: Eventos predecibles
page_order: 6.4
layout: featured
alias: /predictive_purchases/
search_rank: 1
guide_top_header: "Eventos predecibles"
guide_top_text: "Saber cuál de tus usuarios tiene más probabilidades de realizar un evento concreto -como una compra- es una información crucial para las empresas en crecimiento. Sin ella, ¿cómo decides qué campañas construir? ¿Quién debe recibir descuentos y promociones? ¿Dónde gastar un presupuesto limitado? Braze ayuda a responder a estas preguntas con Eventos predictivos (antes Compras predictivas), un modelo de aprendizaje automático que facilita a los equipos de marketing comprender el comportamiento futuro y centrar sus recursos en la interacción y en campañas que maximicen los ingresos."
description: "Este artículo trata de los Eventos predictivos (antes Compras predictivas), una herramienta que ofrece a los especialistas en marketing la posibilidad de identificar y enviar mensajes a los usuarios en función de su probabilidad de realizar un evento."

guide_featured_title: "Temas"
guide_featured_list:
- name: Crear una predicción
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/
  image: /assets/img/braze_icons/settings-01.svg
- name: Análisis de predicciones
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Usuarios de mensajería
  link: /docs/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/
  image: /assets/img/braze_icons/arrow-narrow-right.svg

---

## Resumen

![Gráfico titulado "Cómo funcionan los eventos de predicción", que muestra los datos de usuario embudados en el modelo de aprendizaje automático. La etiqueta dice "Entrena con datos históricos, compara el comportamiento de los usuarios que sí realizaron el evento en un periodo determinado con los que no". También muestra los resultados del aprendizaje automático, donde se clasifica a los usuarios de menor a mayor probabilidad de realizar el evento. La etiqueta dice "Predecir la probabilidad de sucesos futuros, asignar una puntuación de probabilidad a los usuarios para una orientación precisa y conveniente."][1]

> Los Eventos Predictivos proporcionan a los especialistas en marketing una potente herramienta para identificar y enviar mensajes a los usuarios en función de su probabilidad de realizar un evento. Cuando creas una predicción de eventos, Braze entrena un modelo de aprendizaje automático utilizando [árboles de decisión con gradiente reforzado](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender de la actividad previa y predecir la actividad futura.

Una vez elaborada la predicción, se asigna a los usuarios una [puntuación de probabilidad]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#purchase_score) entre 0 y 100, que denota la probabilidad de que realicen el evento seleccionado. Cuanto mayor sea la puntuación, más probable es que el usuario realice ese evento. Los usuarios también se clasifican por categorías de probabilidad baja, media y alta.

El verdadero valor de los Eventos Predictivos reside en utilizar los resultados de la predicción para crear un segmento o una campaña. Los especialistas en marketing pueden crear campañas específicas directamente en la página de **predicción** para obtener resultados inmediatos que aumenten los ingresos, o guardar un segmento para una futura campaña o Canvas. ¿No sabes a quién dirigirte primero? Lee nuestras [consideraciones estratégicas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/messaging_users/#strategy) para enviar mensajes a los usuarios en función de su puntuación de probabilidad.

## Acceder a eventos de predicción

La página **Predicciones** se encuentra en la sección **Análisis**. Para obtener acceso completo, ponte en contacto con tu director de cuentas.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **las predicciones** en **Interacción**.
{% endalert %}

Antes de adquirir esta característica, está disponible en modo vista previa. Esto te permitirá ver una predicción de demostración con datos sintéticos, así como crear un modelo de predicción de vista previa cada vez. Esta predicción se creará basándose en tus datos de usuario reales, pero no te permitirá dirigirte a los usuarios para enviarles mensajes según su puntuación de probabilidad. Tampoco se actualizará regularmente tras su creación.

Con la vista previa, también puedes editar y reconstruir esta única predicción o archivarla y crear otras para probar la [calidad de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/prediction_analytics/#prediction_quality) esperada de [diferentes audiencias]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/creating_an_event_prediction/#audience) y familiarizarte con los análisis.

<br><br>

[1]: {% image_buster /assets/img/how_predictive_events_works.png %}

