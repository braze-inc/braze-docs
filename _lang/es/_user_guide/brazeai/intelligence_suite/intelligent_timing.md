---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artículo ofrece una visión general de Intelligent Timing (anteriormente Intelligent Delivery) y cómo puedes aprovechar esta función en tus campañas y Canvas."
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Usa Intelligent Timing para enviar tu mensaje a cada usuario cuando Braze determina el momento de envío óptimo del usuario, es decir, cuando es más probable que el usuario interactúe (abrir o hacer clic). Así puedes comprobar más fácilmente que envías mensajes a tus usuarios en su momento preferido, lo que puede aumentar la interacción.

## Acerca de Intelligent Timing

Braze calcula el momento de envío óptimo a partir de un análisis estadístico de las interacciones pasadas de tus usuarios con tu app y con cada canal de mensajería. Se utilizan los siguientes datos de interacción:

- Horas de sesión
- Aperturas directas de push
- Aperturas influidas de push
- Clics en correo electrónico
- Aperturas de correo electrónico (excluyendo [aperturas de máquina]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))
- Clics en SMS (solo si [acortamiento de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) y seguimiento avanzado están activados)

Si un usuario no tiene datos de interacción relevantes para calcular el momento óptimo, puedes especificar una hora de alternativa.

## Casos de uso

- Enviar campañas recurrentes que no son sensibles al tiempo
- Automatizar campañas con usuarios en varias zonas horarias
- Al enviar mensajes a tus usuarios más involucrados (tendrán la mayoría de los datos de interacción)

Para los pasos de configuración detallados en campañas y Canvas, horas silenciosas, hora de alternativa, limitaciones y FAQ, consulta la versión completa de este artículo en el índice de la izquierda o la ayuda del dashboard de Braze.
