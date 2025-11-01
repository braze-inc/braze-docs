---
nav_title: "Permisos geográficos"
article_title: Permisos geográficos
description: "Este artículo trata de la lista de países permitidos para los Permisos Geográficos, que te permite elegir a qué países se pueden entregar SMS, MMS y RCS."
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# Permisos geográficos

> Los Permisos geográficos mejoran la seguridad y protegen contra el tráfico fraudulento de SMS, MMS y RCS al imponer controles sobre los países a los que puedes enviar mensajes. Puedes especificar una lista de países permitidos para asegurarte de que los mensajes SMS, MMS y RCS sólo se envían a las regiones aprobadas. Sólo los administradores pueden modificar la lista de países permitidos. Los usuarios que no son administradores tienen acceso a una versión de sólo lectura de la lista de permitidos que indica a qué países puede enviar un grupo de suscripción.

Si eres administrador, puedes configurar los países que están en la lista de permitidos. La lista de países permitidos se configura a nivel de [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/). Puedes acceder a ella yendo a **Audiencia** > **Suscripciones** y seleccionando un grupo de suscripción SMS, MMS o RCS. La lista de permisos está en **Permisos geográficos**.

La sección de permisos geográficos SMS editables para un administrador con varios países seleccionados en la "Lista de países permitidos".]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### Seleccionar países

Añade países a la lista de permitidos con el desplegable. Los países más comunes de SMS y RCS se muestran en la parte superior, y otros se muestran a continuación. También puedes buscar países escribiendo en el campo de texto.

El desplegable "Lista de países permitidos" con los países más comunes en la parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

Elimina los países previamente seleccionados desmarcando las casillas correspondientes junto a ellos.

### Guardar tus cambios

Los cambios surtirán efecto después de seleccionar **Guardar**. Eliminar países de tu lista de permitidos impedirá que todos los mensajes SMS, MMS y RCS se envíen a números de esos países.

Modalidad de advertencia que confirma los países que se eliminarán de la lista permitida.]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## Países de alto riesgo

Ciertos países tienen un mayor riesgo de bombeo de tráfico SMS y RCS. Estos países se indican con una etiqueta **de Alto Riesgo** en el desplegable de países.

El menú desplegable de países con Azerbaiyán tiene una etiqueta de "Alto riesgo".]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

Si permites el envío en estos países, primero debes reconocer el riesgo de hacerlo antes de que el país se añada a tu lista de permitidos.

{% alert note %}
Limita los países de tu lista de permitidos a sólo los necesarios para satisfacer tus necesidades empresariales. Esto minimizará tu potencial de tráfico fraudulento. Para obtener más orientación sobre cómo evitar el [bombeo de tráfico SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/), consulta [las Preguntas frecuentes sobre el fraude por bombeo de tráfico SMS]({{site.baseurl}}/sms_traffic_pumping_fraud/).
{% endalert %}

## Visibilidad de los envíos bloqueados

Los intentos de envío a países que no estén en tu lista de permitidos serán abortados. Los mensajes abortados se registrarán en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) y dentro del [evento de interacción de mensajes SMS abortados]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). 

Los mensajes abortados causados por envíos bloqueados se muestran como **Errores de mensaje abortado** y tienen el mensaje "El número de teléfono del destinatario se encuentra en un país bloqueado".

Registro cancelado que muestra varios envíos de SMS bloqueados porque el número de teléfono está en un país bloqueado.]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

