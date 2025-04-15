---
nav_title: Rebotes de correo electrónico
article_title: Rebotes de correo electrónico
page_order: 0
page_type: solution
description: "Este artículo de ayuda aclara la diferencia entre rebotes duros y rebotes blandos."
channel: email
---

# Rebotes de correo electrónico

¿Qué haces cuando un mensaje de tu campaña de correo electrónico rebota en las direcciones de correo electrónico de tus usuarios? En primer lugar, definamos y solucionemos los dos tipos de rebotes del correo electrónico: los rebotes duros y los rebotes blandos. 

## Rebotes duros

{% multi_lang_include metrics.md metric='Hard Bounce' %}

Para más información, consulta [Rebote duro]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce).

## Rebotes suaves

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

Si un correo electrónico recibe un rebote blando, normalmente, lo volveremos a intentar enviar en un plazo de 72 horas, pero el número de intentos para volver a enviar varía de un receptor a otro.

Aunque los rebotes blandos no son objeto de seguimiento en los análisis de tu campaña, puedes revisar los rebotes blandos en el [Registro de actividad de mensajes][3]. Aquí también puedes ver el motivo de los rebotes blandos y comprender las posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

Para saber más sobre la gestión de tus suscripciones y campañas por correo electrónico, consulta [Buenas prácticas para el correo electrónico][2].

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 2 de mayo de 2024_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
