---
nav_title: "Permisos geográficos para SMS"
article_title: Permisos geográficos para SMS
description: "Este artículo trata de la lista de países permitidos para los permisos geográficos de SMS, que te permite elegir a qué países pueden enviarse los SMS."
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# Permisos geográficos para SMS

> Los Permisos Geográficos SMS mejoran la seguridad y protegen contra el tráfico SMS fraudulento al imponer controles sobre los países a los que se pueden enviar mensajes SMS. Puedes especificar una lista de países permitidos para asegurarte de que los mensajes SMS sólo se envían a las regiones aprobadas. Sólo los administradores pueden modificar la lista de países permitidos. Los usuarios que no son administradores tienen acceso a una versión de sólo lectura de la lista de permitidos que indica a qué países puede enviar un grupo de suscripción.

![La sección Permisos geográficos SMS de sólo lectura para un usuario no administrador con Estados Unidos y Reino Unido seleccionados en la "Lista de países permitidos".][6]{: style="max-width:80%;"}

## Configuración de la lista de países SMS permitidos

Si eres administrador, puedes configurar los países que están en la lista de permitidos. La lista de países permitidos se configura a nivel de [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/). Puede acceder a él yendo a **Audiencia** > **Suscripciones** y seleccionando un grupo de suscripción SMS. La lista de permisos se encuentra en **Permisos geográficos SMS**.

![La sección editable Permisos geográficos de SMS para un administrador con Australia, Canadá y Estados Unidos seleccionados en la "Lista de países permitidos".][1]{: style="max-width:80%;"}

### Seleccionar países

Añada países a la lista de permitidos con el desplegable. Los países con más SMS se muestran en la parte superior, mientras que los demás aparecen a continuación. También puede buscar países escribiendo en el campo de texto.

![El desplegable "Lista de países permitidos" con los países más comunes en la parte superior.][2]{: style="max-width:80%;"}

Elimine los países seleccionados anteriormente desmarcando las casillas correspondientes situadas junto a ellos.

### Guardar los cambios

Los cambios surtirán efecto después de seleccionar **Guardar**. Si eliminas países de tu lista de permitidos, se impedirá el envío de todos los mensajes SMS y MMS a números de esos países.

![Modalidad de advertencia que confirma los países que se eliminarán de la lista permitida.][3]{: style="max-width:70%;"}

## Países de alto riesgo

Algunos países tienen un mayor riesgo de bombeo de tráfico SMS. Estos países se indican con una etiqueta de **alto riesgo** en el desplegable de países.

![El país hacia abajo con Azerbaiyán tiene una etiqueta de "Alto Riesgo".][4]{: style="max-width:80%;"}

Si permite el envío a estos países, primero debe reconocer el riesgo de hacerlo antes de que el país se añada a su lista de permitidos.

{% alert note %}
Limite los países de su lista de permitidos a sólo los necesarios para satisfacer sus necesidades empresariales. Esto minimizará su potencial de tráfico fraudulento. Para obtener más información sobre cómo evitar el tráfico ilícito de SMS, consulta [las Preguntas frecuentes sobre el tráfico ilícito de SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidad de los envíos bloqueados

Los intentos de envío a países que no estén en tu lista de permitidos serán abortados. Los mensajes abortados se registrarán en el [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) y dentro del [evento de compromiso de mensaje SMS abortado]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Los mensajes abortados causados por envíos bloqueados se mostrarán como `Abort_Type = "blocked_recipient_country"` con el registro de abortos detallando el país bloqueado.

![Registro de abortos que muestra el abort_type de blocked_recipient_country y las iniciales del país del número de teléfono bloqueado.][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}