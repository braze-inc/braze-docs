---
nav_title: Tus informes
article_title: Sus informes
page_order: 7
layout: dev_guide
guide_top_header: "Tus informes"
guide_top_text: "Sus datos significan mucho para usted, por lo que disponemos de varias opciones de informes dentro de Braze (sin incluir <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>). Si no estás seguro de por dónde empezar, consulta el <a href='/docs/user_guide/analytics/reporting/#reports-overview'>resumen de informes</a> para obtener orientación sobre qué informes y análisis puedes utilizar para responder a las preguntas más comunes sobre estrategia de marketing."

page_type: landing
description: "Esta página contiene artículos sobre las opciones de informes disponibles en Braze (sin incluir Currents), incluidos los informes por segmentos, los informes de compromiso, el generador de informes, etc."
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
  - name: Informes de participación
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: Generador de informes
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: Generador de dashboards
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Configurar informes
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Análisis de la campaña
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
  - name: Informe global de control
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
  - name: Información del segmento
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Informe del Grupo de control global
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# Resumen de informes

## ¿Qué variante ha ganado?

{% tabs local %}
{% tab Campaign Analytics %}
**Análisis de la campaña**

Utilice [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para obtener actualizaciones en tiempo real sobre los resultados de alto nivel de cada campaña y variante dentro de esa campaña, así como detalles a nivel de mensaje. Puede ajustar el intervalo de fechas para comprender el rendimiento de la campaña a lo largo del tiempo y previsualizar sus mensajes para recordar lo que estaba probando.

{% endtab %}

{% tab Canvas Analytics %}
**Análisis de Canvas**

Utilice [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para obtener estadísticas de primera línea sobre su Canvas y ver cómo está funcionando su estrategia de mensajería. Abre cualquier Canvas en directo para ver estadísticas clave de rendimiento, como:

- Número de mensajes enviados dentro del Canvas
- Número total de veces que los clientes han entrado en el lienzo
- Cuántos clientes se han convertido
- Ingresos generados por el lienzo
- Audiencia total estimada

<br>

**Rendimiento por variante**

[Analiza variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) en un Canvas en vivo para ver las tasas de conversión calculadas automáticamente para cada evento de conversión. También puedes ver los cálculos de elevación y confianza de cada variante y evento de conversión en un formato de tabla fácil de comparar.

Más preguntas que puede responder con este informe:

- ¿Existe una confianza estadísticamente significativa?
- ¿Qué rendimiento tuvo la variante 1 frente a la variante 2?

{% endtab %}

{% tab Report Builder %}
**Generador de informes**

Utilice el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o lienzos en una sola vista y determinar rápidamente qué estrategias de captación han tenido un mayor impacto en sus métricas clave.

Consulta esta página para:

- Cree un informe de las campañas y los lienzos de la última semana o mes, calcule las métricas críticas y compártalo con sus compañeros de equipo.
- Compare el rendimiento entre variantes tanto para pruebas multivariantes como para Canvases.
- Determine qué canal de mensajería obtuvo la mayor conversión o participación para una campaña o Canvas específicos.
- Seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Canvases (como todos los mensajes relacionados con una etiqueta "newsletters").

Más preguntas que puedes responder con esta función:

- ¿Cómo se comportó la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% endtabs %}

## ¿Qué variante afectó más a la retención?

{% tabs local %}
{% tab Retention Reports %}
**Informes de retención**

Utilice los informes de retención para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) o [lienzos]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) para medir la retención de los usuarios que han realizado un evento seleccionado en una campaña específica.

Consulta este informe para:

- Determina la eficacia de un mensaje para la reactivación de la interacción de los usuarios a largo plazo analizando la aparición de diferentes eventos hasta un mes después de recibir una campaña.
- Compara la aparición de distintos eventos entre las variantes de una [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

Más preguntas que puede responder con este informe:

- ¿Qué variante afectó más a la retención?
- ¿Durante cuánto tiempo siguen utilizando mi aplicación los clientes que han recibido esta campaña?
- ¿Cómo influyó esta campaña en la retención al cabo de un día? ¿Después de 30 días?

{% alert note %} Los informes de retención no están disponibles para las campañas activadas por SMS y API. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

Utilice informes de embudo para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) o [Canvases]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analizar los recorridos que realizan sus clientes tras recibir una campaña. Puede elegir qué eventos nativos o personalizados incluir en cada análisis de embudo y, a continuación, analizar el rendimiento de cada variante en relación con el embudo de conversión seleccionado.

Consulta este informe para:

- Comprenda en qué punto del embudo de conversión los usuarios abandonaron e identifique oportunidades para volver a enviar mensajes de captación.
- Ver las conversiones de un evento que no se incluyó originalmente como evento de conversión al configurar la campaña.
- Analice el embudo de compra mediante una serie de acciones (como "¿Qué porcentaje de clientes recibieron un correo electrónico, iniciaron una sesión, añadieron un artículo a su cesta y luego compraron?").

Más preguntas que puede responder con este informe:

- ¿En qué punto del camino hacia la conversión se quedan mis clientes?
- ¿Cómo puedo mejorar mis estrategias de marketing?

{% endtab %}
{% endtabs%}

## ¿Cuál es el grado de compromiso de mis usuarios?

{% tabs local %}
{% tab Report Builder %}

Utilice el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o lienzos en una sola vista y determinar rápidamente qué estrategias de captación han tenido un mayor impacto en sus métricas clave.

Consulta esta página para:

- Cree un informe de las campañas y los lienzos de la última semana o mes, calcule las métricas críticas y compártalo con sus compañeros de equipo.
- Determine qué canal de mensajería obtuvo la mayor conversión o participación para una campaña o Canvas específicos.
- Seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Canvases (como todos los mensajes relacionados con una etiqueta "newsletters").

Más preguntas que puedes responder con esta función:

- ¿Cómo se comportó la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% tab Overview Data %}
**Datos generales**

Utilice la página [Visión general]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para obtener un resumen de alto nivel de las métricas clave relativas al rendimiento de su aplicación y una visión de la base de usuarios de su aplicación.

Consulte esta página para conocer estas estadísticas:

- Tiempo de vida de los usuarios
- Sesiones por ciclo de vida
- Usuarios activos mensuales (MAU)
- Usuarios activos diarios (DAU)
- Nuevos usuarios
- Adherencia de los usuarios
- Sesiones diarias
- Sesión diaria por MAU

Más preguntas que puedes responder con este cuadro de mandos:

- ¿Veo una mejora de la adherencia mes a mes?
- ¿Veo un crecimiento general de mi aplicación para iOS o Android?
- ¿Cómo es mi volumen total de correo electrónico este mes?

{% endtab %}
{% tab Engagement Reports %}
**Informes de participación**

Utilice [los informes de participación]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) para exportar periódicamente por correo electrónico las estadísticas de participación de las campañas y los lienzos seleccionados. Este informe es el más personalizable y granular disponible a través del cuadro de mandos.

Puede exportar las siguientes estadísticas en función de su canal de mensajes:

| canal| estadísticas disponibles|
| ------| --------------|
| Correo electrónico | Envíos, Aperturas, Aperturas únicas, Clics, Clics únicos, Clics para abrir, Anulaciones de suscripción, Rebotes, Entregados, Spam denunciado |
| Push  | Envíos, aperturas, Influenced Opens, rebotes, clics en el cuerpo |
| Notificación push web | Envíos, aperturas, rebotes, clics en el cuerpo |
| Mensaje dentro de la aplicación | Impresiones, clics, primeros clics del botón, segundos clics del botón |
| Webhook  |  Envíos, Errores |
| SMS | Envíos, envíos al transportista, entregas confirmadas, fallos de entrega, rechazos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Más preguntas que puede responder con este informe:

- ¿Cómo están funcionando todos mis mensajes "win-back"?
- ¿Cuál es la tasa de entrega total de mis campañas de correo electrónico?
- ¿Cómo les ha ido a todas mis campañas de Braze en junio? ¿Para 2021 hasta la fecha?
- ¿Qué tendencias se observan en las pruebas multivariantes?

{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los comportamientos de los usuarios por segmentos?

{% tabs local %}
{% tab Segment Data %}
**Datos de los segmentos**

Si ha activado el [seguimiento analítico]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) para un segmento, abra ese segmento para ver [los Datos del segmento]({{site.baseurl}}/viewing_and_understanding_segment_data/). Segment Data realiza un seguimiento de las sesiones, los eventos personalizados y los ingresos a lo largo del tiempo para los usuarios correspondientes.

Consulte esta página para conocer estas estadísticas:

- Número total de:
  - Usuarios en su segmento, y qué porcentaje de su base total de usuarios son
  - Usuarios que han optado explícitamente por la adhesión voluntaria al correo electrónico
  - Usuarios habilitados para push que han optado explícitamente por las notificaciones push.
- Valor medio de vida (LTV) de los usuarios de este segmento
- Lista de herramientas de compromiso dirigidas a este segmento
- Información del segmento

{% endtab %}
{% tab Segment Insights %}
**Información del segmento**

[Segment Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) le permite comparar segmentos entre sí para comprender cómo las siguientes métricas pueden influir en aspectos como la duración del ciclo de vida y la frecuencia de las sesiones:

- Demografía
- Plataformas
- Estado de adhesión voluntaria
- Preferencias de categoría
- Recepción de la campaña

Más preguntas que puede responder con este informe:

- ¿Cuál fue la frecuencia de las sesiones de los usuarios que recibieron mi Canvas de incorporación frente a los del grupo de control?
- ¿Cuál es la diferencia en la duración del ciclo de vida de los usuarios que han optado por el push frente a los usuarios que han optado por el correo electrónico y frente a los usuarios que han optado por ambos?

{% endtab %}
{% tab Custom Events %}
**Eventos personalizados**

Utilice la página [Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) para controlar la frecuencia con la que se ha producido un evento personalizado, así como la última vez que cada usuario lo realizó para su segmentación.

Consulta esta página para:

- Supervisar la frecuencia de los eventos personalizados
- Seguimiento de eventos personalizados por segmento
- Analizar cómo afectan las campañas a la actividad de los eventos personalizados
- Creación y seguimiento de [fórmulas de KPI]({{site.baseurl}}/user_guide/data/creating_a_formula/)
- Solucionar problemas de seguimiento de eventos personalizados

{% endtab %}
{% endtabs %}

## ¿Mi campaña ha rentabilizado la inversión?

{% tabs local %}
{% tab Revenue Data %}
**Datos de ingresos**

Utilice la página [Ingresos]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) para realizar un seguimiento de los ingresos y las compras durante periodos específicos o de los ingresos o compras totales de su aplicación.

Consulte esta página para conocer estas estadísticas:

- Resultados de la fórmula KPI
- Número de compras de productos
- Ingresos por diferentes segmentos
- Ingresos por diferentes productos
- Ingresos por hora
- Ingresos por hora en los distintos segmentos
- Ingresos por usuario

{% endtab %}
{% tab Global Control Group Report %}
**Informe del Grupo de control global**

Una vez que haya configurado un [Grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/), utilice el [Informe de control global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para evaluar el impacto de su marketing Braze en su conjunto. Este informe le permite comparar los comportamientos de los usuarios que reciben mensajes con los comportamientos de los usuarios que no los reciben, lo que proporciona una mejor comprensión de cómo sus campañas y Canvases están contribuyendo a sus objetivos empresariales.

Consulta esta página para:

- Mida fácilmente el impacto y el incremento de las campañas y los lienzos en las sesiones y los eventos personalizados.
- Aleatorice y excluya automáticamente a los miembros del grupo de control de la recepción de mensajes.
- Exportación de los miembros del grupo de control para su posterior análisis.

Más preguntas que puede responder con un informe:

- ¿Cuál fue el efecto global del envío de mensajes Braze en el comportamiento de los clientes?
- ¿Cuál es el ROI de Braze como plataforma (para renovación o debates entre partes interesadas)?

{% endtab %}
{% endtabs %}

## ¿Qué campañas debo realizar a continuación?

{% tabs local %}
{% tab Funnel Report %}

Utilice informes de embudo para [campañas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) o [Canvases]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) para analizar los recorridos que realizan sus clientes tras recibir una campaña. Puede elegir qué eventos nativos o personalizados incluir en cada análisis de embudo y, a continuación, analizar el rendimiento de cada variante en relación con el embudo de conversión seleccionado.

Consulta este informe para:

- Comprenda en qué punto del embudo de conversión los usuarios abandonaron e identifique oportunidades para volver a enviar mensajes de captación.
- Ver las conversiones de un evento que no se incluyó originalmente como evento de conversión al configurar la campaña.
- Analice el embudo de compra mediante una serie de acciones (como "¿Qué porcentaje de clientes recibieron un correo electrónico, iniciaron una sesión, añadieron un artículo a su cesta y luego compraron?").

Más preguntas que puede responder con este informe:

- ¿En qué punto del camino hacia la conversión se quedan mis clientes?
- ¿Cómo puedo mejorar mis estrategias de marketing?

{% endtab %}
{% tab Predictive Churn %}
**Predictive Churn**

Utiliza [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) para definir y generar predicciones, proporcionando un enfoque proactivo para minimizar futuros abandonos.

Dado que cada empresa define la rotación y la retención de forma diferente, sólo tiene que introducir sus definiciones en Predictive Churn y Braze hará el resto. También puede crear campañas o lienzos para actuar a partir de las predicciones o crear segmentos para análisis posteriores.

Más preguntas que puedes responder con esta función:

- ¿Cuántos de mis usuarios ideales corren el riesgo de darse de baja?
- ¿Qué comportamientos o atributos tienen en común mis usuarios de riesgo?

{% endtab %}
{% tab Report Builder %}
**Generador de informes**

Utilice el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) para comparar los resultados de varias campañas o lienzos en una sola vista y determinar rápidamente qué estrategias de captación han tenido un mayor impacto en sus métricas clave.

Consulta esta página para:

- Cree un informe de las campañas y los lienzos de la última semana o mes, calcule las métricas críticas y compártalo con sus compañeros de equipo.
- Compare el rendimiento entre variantes tanto para pruebas multivariantes como para Canvases.
- Determine qué canal de mensajería obtuvo la mayor conversión o participación para una campaña o Canvas específicos.
- Seguimiento de las tendencias generales de rendimiento de un grupo de campañas o Canvases (como todos los mensajes relacionados con una etiqueta "newsletters").

Más preguntas que puedes responder con esta función:

- ¿Cómo se comportó la primera versión de mi correo electrónico de bienvenida frente a la segunda?
- ¿Cuáles han sido mis tarifas abiertas push medias de este mes en comparación con las del mes pasado, para una etiqueta concreta?
- ¿Qué boletín de noticias del mes tuvo más conversiones?

{% endtab %}
{% endtabs %}
