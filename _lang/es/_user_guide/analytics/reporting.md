---
nav_title: Tus informes
article_title: Tus informes
page_order: 7
layout: dev_guide
guide_top_header: "Tus informes"
guide_top_text: "Tus datos significan mucho para ti, por lo que disponemos de varias opciones de informes dentro de Braze (sin incluir <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>). Si no estás seguro de por dónde empezar, consulta el <a href='/docs/user_guide/analytics/reporting/#reports-overview'>resumen de informes</a> para obtener orientación sobre qué informes y análisis puedes utilizar para responder a las preguntas más comunes sobre estrategia de marketing."

page_type: landing
description: "Esta página de inicio contiene artículos sobre las opciones de informes disponibles en Braze (sin incluir Currents), incluidos los informes de segmentos, los informes de interacción, el generador de informes y mucho más."
tool: Reports
search_rank: 2
guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Glosario de métricas de los informes
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Datos de los segmentos
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Informes de interacción
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: Generador de informes
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: Constructor de paneles
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Configurar los informes
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Análisis de campaña
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Análisis de Canvas
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: Eventos personalizados
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Informe de embudo
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Informe de control global
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: Informe de retención
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Datos de ingresos
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Informe de ingresos
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Información por segmentos
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Informe del grupo de control global
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# Resumen de los informes

## ¿Qué variante ha ganado?

{% tabs local %}
{% tab Campaign Analytics %}
**Análisis de campaña**

Utiliza [el Análisis de Campañas]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para obtener actualizaciones en tiempo real de los resultados de alto nivel de cada campaña y variante dentro de esa campaña, así como detalles a nivel de mensaje. Puedes ajustar el intervalo de fechas para comprender el rendimiento de la campaña a lo largo del tiempo y previsualizar tus mensajes para recordar lo que estabas probando.

{% endtab %}

{% tab Canvas Analytics %}
**Análisis de Canvas**

Utiliza [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obtener estadísticas de primera línea sobre tu Canvas y comprobar el rendimiento de tu estrategia de mensajería. Abre cualquier Canvas en vivo para ver estadísticas clave de rendimiento, como:

- Número de mensajes enviados dentro del Canvas
- Número total de veces que los clientes han entrado en el Canvas
- ¿Cuántos clientes se han convertido?
- Ingresos generados por el Canvas
- Audiencia total estimada

<br>

**Rendimiento por variante**

[Analiza variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) en un Canvas en vivo para ver las tasas de conversión calculadas automáticamente para cada evento de conversión. También puedes ver los cálculos de elevación y confianza de cada variante y evento de conversión en un formato de tabla fácil de comparar.

Más preguntas que puedes responder con este informe:

- ¿Hubo una confianza estadísticamente significativa?
- ¿Qué rendimiento tuvo la variante 1 frente a la variante 2?

{% endtab %}

{% tab Report Builder %}
**Generador de informes**

Utiliza el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o Canvases en una sola vista y determinar rápidamente qué estrategias de interacción tuvieron un mayor impacto en tus métricas clave.

Consulta esta página para:

- Crea un informe de campañas y Lienzos de la última semana o mes, calcula métricas críticas y compártelo con tus compañeros de equipo.
- Compara el rendimiento entre variantes tanto para pruebas multivariantes como para Lienzos.
- Determina qué canal de mensajería obtuvo la mayor conversión o interacción para una campaña o Canvas específico.
- Haz un seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Lienzos (como todos los mensajes relacionados con una etiqueta "boletines").

Puedes responder a más preguntas con esta característica:

- ¿Qué rendimiento tuvo la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% endtabs %}

## ¿Qué variante afectó más a la retención?

{% tabs local %}
{% tab Retention Reports %}
**Informes de retención**

Utiliza los Informes de retención para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) o [Lienzos]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) para medir la retención de los usuarios que han realizado un evento seleccionado en una campaña específica.

Consulta este informe para:

- Determina la eficacia de un mensaje para la reactivación de la interacción de los usuarios a largo plazo analizando la aparición de diferentes eventos hasta un mes después de recibir una campaña.
- Compara la aparición de distintos eventos entre las variantes de una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

Más preguntas que puedes responder con este informe:

- ¿Qué variante afectó más a la retención?
- ¿Durante cuánto tiempo siguen utilizando mi aplicación los clientes que han recibido esta campaña?
- ¿Cómo influyó esta campaña en la retención al cabo de un día? ¿Después de 30 días?

{% alert note %} Los informes de retención no están disponibles para las campañas desencadenadas por SMS y API. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

Utiliza informes de embudo para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) o [Lienzos]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analizar los recorridos que realizan tus clientes tras recibir una campaña. Puedes elegir qué eventos nativos o personalizados incluir en cada análisis de embudo y, a continuación, sumergirte en cómo rinde cada variante frente a su embudo de conversión seleccionado.

Consulta este informe para:

- Comprende en qué parte del embudo de conversión han caído los usuarios e identifica las oportunidades de mensajes de reactivación de la interacción.
- Ver las conversiones de un evento que no se incluyó originalmente como evento de conversión al configurar la campaña.
- Analiza el embudo de compra mediante una serie de acciones (como "¿Qué porcentaje de clientes recibió un correo electrónico, inició una sesión, añadió un artículo a su cesta y luego compró?").

Más preguntas que puedes responder con este informe:

- ¿En qué punto del camino hacia la conversión se quedan mis clientes?
- ¿Cómo puedo mejorar mis estrategias de marketing?

{% endtab %}
{% endtabs%}

## ¿Cuál es el grado de interacción de mis usuarios?

{% tabs local %}
{% tab Report Builder %}

Utiliza el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o Canvases en una sola vista y determinar rápidamente qué estrategias de interacción tuvieron un mayor impacto en tus métricas clave.

Consulta esta página para:

- Crea un informe de campañas y Lienzos de la última semana o mes, calcula métricas críticas y compártelo con tus compañeros de equipo.
- Determina qué canal de mensajería obtuvo la mayor conversión o interacción para una campaña o Canvas específico.
- Haz un seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Lienzos (como todos los mensajes relacionados con una etiqueta "boletines").

Puedes responder a más preguntas con esta característica:

- ¿Qué rendimiento tuvo la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% tab Overview Data %}
**Datos generales**

Utiliza la página [Resumen]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para obtener un resumen de alto nivel de las métricas clave relativas al rendimiento de tu aplicación y obtener información sobre la base de usuarios de tu aplicación.

Consulta estas estadísticas en esta página:

- Usuarios de toda la vida
- Sesiones de por vida
- Usuarios activos al mes (MAU)
- Usuarios activos diarios (DAU)
- Nuevos usuarios
- Adherencia
- Sesiones diarias
- Sesión diaria por MAU

Puedes responder a más preguntas con este panel:

- ¿Veo una mejora de la adherencia mes a mes?
- ¿Veo un crecimiento general de mi aplicación para iOS o Android?
- ¿Cómo es mi volumen total de correo electrónico este mes?

{% endtab %}
{% tab Engagement Reports %}
**Informes de interacción**

Utiliza [los Informes de interacción]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) para configurar una exportación recurrente por correo electrónico de las estadísticas de interacción de las campañas y Lienzos seleccionados. Este informe es el más personalizable y granular disponible a través del panel.

Puedes exportar las siguientes estadísticas en función de tu canal de mensajería:

| canal| estadísticas disponibles|
| ------| --------------|
| Correo electrónico | Envíos, Aperturas, Aperturas únicas, Clics, Clics únicos, Clic para abrir, Desuscripciones, Rebotes, Entregados, Spam reportado |
| Push  | Envíos, Aperturas, Influenced Opens, Rebotes, Clics Corporales |
| Web push | Envíos, aperturas, rebotes, clics en el cuerpo |
| Mensaje dentro de la aplicación | Impresiones, Clics, Clics en el primer botón, Clics en el segundo botón |
| Webhook  |  Envíos, Errores |
| SMS | Envíos, Envíos al operador, Entregas confirmadas, Fallos de entrega, Rechazos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Más preguntas que puedes responder con este informe:

- ¿Cómo están rindiendo todos mis mensajes de "recuperación"?
- ¿Cuál es la tasa de entrega total de mis campañas de correo electrónico?
- ¿Cómo les ha ido a todas mis campañas de Braze en junio? ¿Para 2021 hasta la fecha?
- ¿Qué tendencias observo con las pruebas multivariantes?

{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los comportamientos de los usuarios por segmentos?

{% tabs local %}
{% tab Segment Data %}
**Datos de los segmentos**

Si has habilitado [el seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) para un segmento, abre ese segmento para ver [los Datos del segmento]({{site.baseurl}}/viewing_and_understanding_segment_data/). Los Datos de Segmento hacen un seguimiento de las sesiones, los eventos personalizados y los ingresos a lo largo del tiempo para los usuarios correspondientes.

Consulta estas estadísticas en esta página:

- Número total de:
  - Usuarios de tu segmento, y qué porcentaje de tu base total de usuarios son
  - Usuarios que han optado explícitamente por la adhesión voluntaria al correo electrónico
  - Usuarios habilitados para push que han optado explícitamente por las notificaciones push.
- Valor medio de duración del ciclo de vida (LTV) de los usuarios de este segmento
- Lista de herramientas de interacción dirigidas a este segmento
- Información por segmentos

{% endtab %}
{% tab Segment Insights %}
**Información por segmentos**

[Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) te permite comparar segmentos entre sí para comprender cómo las siguientes métricas pueden influir en aspectos como la duración del ciclo de vida y la frecuencia de las sesiones:

- Demografía
- Plataformas
- Estado de adhesión voluntaria
- Categoría preferencias
- Recibo de campaña

Más preguntas que puedes responder con este informe:

- ¿Cuál fue la frecuencia de sesión de los usuarios que recibieron mi Canvas de incorporación frente a los del grupo de control?
- ¿Cuál es la diferencia en la duración del ciclo de vida de los usuarios que optan por el push frente a los usuarios que optan por el correo electrónico y frente a los usuarios que optan por ambos?

{% endtab %}
{% tab Custom Events %}
**Eventos personalizados**

Utiliza la página [Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) para controlar la frecuencia con la que se ha producido un evento personalizado, así como la última vez que lo realizó cada usuario para la segmentación.

Consulta esta página para:

- Monitoriza la frecuencia de eventos personalizados
- Monitoriza eventos personalizados por segmento
- Analiza cómo afectan las campañas a la actividad de los eventos personalizados
- Crear y supervisar [fórmulas de KPI]({{site.baseurl}}/user_guide/data/creating_a_formula/)
- Solucionar problemas de seguimiento de eventos personalizados

{% endtab %}
{% endtabs %}

## ¿Proporcionó mi campaña un retorno de la inversión?

{% tabs local %}
{% tab Revenue Data %}
**Datos de ingresos**

Utiliza la página [Ingresos]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) para hacer un seguimiento de los ingresos y compras durante periodos concretos o de los ingresos o compras totales de tu aplicación.

Consulta estas estadísticas en esta página:

- Resultados de la fórmula KPI
- Número de compras de productos
- Ingresos de los distintos segmentos
- Ingresos por diferentes productos
- Ingresos por hora
- Ingresos por hora de los distintos segmentos
- Ingresos por usuario

{% endtab %}
{% tab Global Control Group Report %}
**Informe del grupo de control global**

Cuando hayas configurado un [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), utiliza el [Informe de control global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para evaluar el impacto de tu marketing Braze en su conjunto. Este informe te permite comparar los comportamientos de los usuarios que reciben mensajería con los comportamientos de los usuarios que no la reciben, proporcionándote una mejor comprensión de cómo tus campañas y Canvases están contribuyendo a tus objetivos de negocio.

Consulta esta página para:

- Mide fácilmente el impacto y el aumento incremental de las campañas y los Canvases en sesiones y eventos personalizados.
- Aleatoriza y excluye automáticamente a los miembros del grupo de control de la recepción de mensajes.
- Exporta los miembros del grupo de control para su posterior análisis.

Más preguntas que puedes responder con un informe:

- ¿Cuál fue el efecto global del envío de mensajes Braze en el comportamiento del cliente?
- ¿Cuál es el ROI de Braze como plataforma (para la renovación o los debates de las partes interesadas)?

{% endtab %}
{% endtabs %}

## ¿Qué campañas debería hacer a continuación?

{% tabs local %}
{% tab Funnel Report %}

Utiliza informes de embudo para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) o [Lienzos]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analizar los recorridos que realizan tus clientes tras recibir una campaña. Puedes elegir qué eventos nativos o personalizados incluir en cada análisis de embudo y, a continuación, sumergirte en cómo rinde cada variante frente a su embudo de conversión seleccionado.

Consulta este informe para:

- Comprende en qué parte del embudo de conversión han caído los usuarios e identifica las oportunidades de mensajes de reactivación de la interacción.
- Ver las conversiones de un evento que no se incluyó originalmente como evento de conversión al configurar la campaña.
- Analiza el embudo de compra mediante una serie de acciones (como "¿Qué porcentaje de clientes recibió un correo electrónico, inició una sesión, añadió un artículo a su cesta y luego compró?").

Más preguntas que puedes responder con este informe:

- ¿En qué punto del camino hacia la conversión se quedan mis clientes?
- ¿Cómo puedo mejorar mis estrategias de marketing?

{% endtab %}
{% tab Predictive Churn %}
**Predictive Churn**

[Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) es el primer modelo de la [línea de productos Braze Predictive Suite]({{site.baseurl}}/user_guide/brazeai/). Utiliza Predictive Churn para definir y generar predicciones, proporcionando un enfoque proactivo para minimizar futuros abandonos.

Como cada empresa define el abandono y la retención de forma diferente, sólo tienes que introducir tus definiciones en Predictive Churn, y Braze hará el resto. También puedes crear campañas o Lienzos para actuar a partir de las predicciones o crear segmentos para un análisis más detallado.

Puedes responder a más preguntas con esta característica:

- ¿Cuántos de mis usuarios ideales corren riesgo de abandono?
- ¿Qué comportamientos o atributos tienen en común mis usuarios de riesgo?

{% endtab %}
{% tab Report Builder %}
**Generador de informes**

Utiliza el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o Canvases en una sola vista y determinar rápidamente qué estrategias de interacción tuvieron un mayor impacto en tus métricas clave.

Consulta esta página para:

- Crea un informe de campañas y Lienzos de la última semana o mes, calcula métricas críticas y compártelo con tus compañeros de equipo.
- Compara el rendimiento entre variantes tanto para pruebas multivariantes como para Lienzos.
- Determina qué canal de mensajería obtuvo la mayor conversión o interacción para una campaña o Canvas específico.
- Haz un seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Lienzos (como todos los mensajes relacionados con una etiqueta "boletines").

Puedes responder a más preguntas con esta característica:

- ¿Qué rendimiento tuvo la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% endtabs %}
