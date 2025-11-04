---
nav_title: Adhesión voluntaria y exclusión palabras clave
article_title: Palabras clave de la adhesión voluntaria por SMS
page_order: 0
description: "Este artículo de referencia explica cómo Braze procesa las palabras clave básicas de adhesión voluntaria y exclusión voluntaria para la mensajería SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Palabras clave de adhesión voluntaria y exclusión voluntaria

> La normativa exige que haya respuestas a todas las respuestas de adhesión voluntaria, exclusión voluntaria y palabras clave de ayuda/información. Braze procesa automáticamente los siguientes mensajes _exactos, de una sola palabra y que no distinguen mayúsculas de minúsculas_, actualizando automáticamente el [estado]({{site.baseurl}}/sms_rcs_subscription_groups/) del [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) para el usuario y su número de teléfono asociado en todas las solicitudes entrantes.

## Resumen de palabras clave

Braze procesará automáticamente las siguientes palabras clave y actualizará el estado del grupo de suscripción para el número de teléfono en todas las solicitudes entrantes. Ten en cuenta que estas palabras clave y respuestas predeterminadas también se pueden personalizar. 

| Tipo Palabra clave Cambio
\|-|-------|---|
|Adhesión voluntaria `START`<br> `YES`<br> `UNSTOP` | Cualquier solicitud entrante con una de estas palabras clave `Opt-In` provocará un cambio de estado del grupo de suscripción a `subscribed`. Además, el conjunto de remitentes asociados a ese grupo de suscripción podrá ahora enviar un mensaje SMS, MMS o RCS a ese cliente (dependiendo del tipo de mensajería que admitan los remitentes). <br><br>El usuario recibirá tu respuesta automática de adhesión voluntaria definida.  |
|Opción de no participar `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Cualquier solicitud entrante con una de estas palabras clave `Opt-Out` provocará un cambio de estado del grupo de suscripción a `unsubscribed`. Además, el conjunto de números asociados a ese grupo de suscripción ya no podrá enviar mensajes a ese cliente.<br><br>El usuario recibirá tu respuesta automática de exclusión definida. |
| Ayuda `HELP`<br> `INFO` | El usuario recibirá tu respuesta automática de Ayuda definida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sólo se procesará el **mensaje exacto, de una sola palabra** (sin distinguir mayúsculas de minúsculas). Las palabras clave como `STOP PLEASE` se ignorarán a menos que se active [la adhesión voluntaria difusa]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/).

Si un destinatario utiliza las palabras clave `HELP` o `INFO`, se desencadenará automáticamente una respuesta. La respuesta predeterminada para estos mensajes de respuesta automática se establecerá durante el periodo de [incorporación]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) y adquisición del número de teléfono. Ten en cuenta que puedes seguir actualizando estas respuestas después del periodo inicial de incorporación.

{% alert tip %}
¿Te interesa ampliar tu procesamiento de adhesión voluntaria? Prueba [la exclusión difusa]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/), una característica que intenta reconocer cuándo un mensaje entrante no coincide con una palabra clave de exclusión, pero indica intención de exclusión.
{% endalert %}

