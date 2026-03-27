---
nav_title: Informes e información
article_title: Informes e información
description: "Aprende a ver los informes de BrazeAI Decisioning Studio™ en Braze, para que puedas entender cómo afectan a tus campañas las decisiones basadas en IA."
page_order: 3
---

# Informes e información

> Aprende a ver los informes de BrazeAI Decisioning Studio™ en Braze, para que puedas entender cómo afectan a tus campañas las decisiones basadas en IA. Desde las métricas de rendimiento hasta el estado de los datos y los cambios del sistema, estos informes te ayudan a comprender los resultados, solucionar problemas y tomar decisiones informadas con confianza.

## Requisitos previos

Antes de poder ver los informes de Decisioning Studio en Braze, deberás:

- Tener un contrato activo para Braze y BrazeAI Decisioning Studio™. 
- Ponerte en contacto con tu CSM para que te habilite BrazeAI Decisioning Studio™ en tu nombre.
- Disponer de un agente de BrazeAI Decisioning Studio™ en vivo.

## Ver informes {#view}

Para ver las métricas de un agente de Decisioning Studio en Braze, ve a **AI Decisioning** > **BrazeAI Decisioning Studio™** y selecciona un agente.

![Pantalla de inicio de informes de BrazeAI Decisioning Studio™ que muestra un dashboard con varias tarjetas de informe. Cada tarjeta muestra un tipo de informe, como Rendimiento, Información, Diagnóstico y Cronología, con breves descripciones e íconos para cada uno.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Aquí puedes ver informes como los de rendimiento, información, diagnósticos y cronologías. Para más detalles, consulta [Informes disponibles](#available-reports).

## Cambiar las fechas de los informes

Tras [abrir un informe](#view), puedes cambiar el intervalo de fechas seleccionando una nueva fecha de inicio y finalización en el desplegable del calendario.

![Selector de rango de fechas de BrazeAI Decisioning Studio™ abierto con un menú desplegable de calendario. El calendario muestra fechas de inicio y finalización seleccionables para personalizar la vista del informe.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

También puedes establecer una fecha de inicio predeterminada o elegir fechas para excluir siempre. Las fechas excluidas se filtrarán de todos los informes de ese agente.

Para establecer o excluir fechas, selecciona <i class="fa-solid fa-gear"></i> **Configuración** y, a continuación, cambia la fecha predeterminada o excluye las fechas que necesites.

![Panel de configuración abierto en BrazeAI Decisioning Studio™ que muestra las opciones para establecer una fecha de inicio predeterminada y excluir fechas específicas de los informes. El panel muestra dos secciones denominadas Fecha de inicio predeterminada y Fechas excluidas. En Excluir fechas, aparecen varias fechas con casillas de verificación junto a cada una.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Informes disponibles {#available-reports}

- [Rendimiento]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/): métricas de alto nivel del agente que comparan los grupos de tratamiento con los grupos de control, con las vistas **Tendencias** y **Árbol de controladores**.
- [Información]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/): cómo se generan las opciones de recomendación en tu banco de acciones, incluyendo las preferencias del agente y los informes SHAP.
- [Diagnóstico]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/): estado de los datos de entrada y salida, incluyendo el volumen de recomendaciones y la monitorización de fuentes de datos.
- [Cronología]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/): un registro visual de eventos clave (ejecuciones de agentes, cambios de configuración, actualizaciones de barreras de seguridad) junto con las métricas de rendimiento.