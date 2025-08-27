---
nav_title: Perfiles de usuario
article_title: Perfiles de usuario
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Este artículo de referencia describe cómo acceder al perfil de un usuario en el panel de control, los casos de uso del perfil y lo que contiene cada perfil."

---

# Perfiles de usuario

> Los perfiles de usuario son una excelente forma de encontrar información sobre usuarios concretos. Todos los datos persistentes asociados con un usuario se almacenan en su perfil de usuario.

## Perfiles de acceso

Para acceder al perfil de un usuario, vaya a la página **Buscar usuarios** y busque un usuario por cualquiera de los siguientes criterios:

- ID de usuario externo
- ID de Braze
- Correo electrónico
- Número de teléfono
- Token de notificaciones push
- Alias de usuario con el formato "[alias_usuario]:[nombre_alias]", como "amplitud_id:usuario_123"

Si se encuentra una coincidencia, puede ver la información que ha registrado para este usuario con el SDK Braze. De lo contrario, si su búsqueda devuelve varios perfiles de usuario, puede fusionar cada perfil individualmente o realizar una fusión de usuarios masiva. Para obtener más información, consulte [Usuarios duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

![Resultados de la búsqueda con un banner que dice "Varios usuarios coinciden con tus criterios de búsqueda" y dos botones etiquetados como Anterior y Siguiente.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Ejemplos

Los perfiles de usuario son un gran recurso para solucionar problemas y realizar pruebas, ya que se puede acceder fácilmente a información sobre el historial de participación de un usuario, su pertenencia a un segmento, su dispositivo y su sistema operativo.

Por ejemplo, si un usuario informa de un problema y no estás seguro de qué dispositivo y sistema operativo está utilizando, puedes utilizar la [pestaña Descripción general](#overview-tab) para encontrar esta información (siempre que tengas su correo electrónico o ID de usuario). También puede ver el idioma de un usuario, lo que podría ser útil si está solucionando un problema de una [campaña multilingüe]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) que no se comportó como se esperaba.

Puede utilizar la [pestaña Compromiso](#engagement-tab) para verificar si un determinado usuario ha recibido una campaña. Además, si este usuario concreto recibió la campaña, puede ver cuándo la recibió. También puedes verificar si un usuario está en un segmento determinado y si ha optado por la adhesión voluntaria al push, al correo electrónico o a ambos. Esta información es útil para solucionar problemas. Por ejemplo, debe comprobar esta información si un usuario no recibe una campaña que esperaba que recibiera o recibe una campaña que no esperaba que recibiera.

## Elementos del perfil de usuario

Hay cuatro secciones principales en el perfil de un usuario.

- **Visión general:** Información básica sobre el usuario, datos de sesión, atributos personalizados, eventos personalizados, compras y el dispositivo más reciente en el que el usuario inició sesión.
- **Compromiso:** Información sobre la configuración de contacto del usuario, campañas recibidas, segmentos, estadísticas de comunicación, atribución de instalación y número de cubo aleatorio.
- **Historia de la mensajería:** Eventos recientes relacionados con la mensajería para este usuario en los últimos 30 días.
- **Características Elegibles:** Valida para qué banderas de características es elegible actualmente un usuario a través de despliegues, pasos en Canvas y experimentos. 

### Pestaña Resumen {#overview-tab}

La pestaña **Visión general** contiene información básica sobre un usuario y sus interacciones con su aplicación o sitio web.

| Categoría general | Contiene |
| --- | --- |
| Perfil | Sexo, grupo de edad, ubicación, idioma, localidad, zona horaria y fecha de nacimiento. |
| Resumen de las sesiones | Cuántas sesiones tuvieron, cuándo fue su primera y su última sesión, y en qué aplicaciones. |
| Atributos personalizados | Qué atributos personalizados se atribuyen a este usuario y su valor asociado, incluidos los atributos personalizados anidados. |
| Dispositivos recientes | En cuántos dispositivos se conectaron, los detalles de cada dispositivo y sus identificadores de publicidad asociados (si los hubiera). |
| Eventos personalizados | Qué eventos personalizados ha realizado este usuario, cuántas veces y cuándo realizó cada evento por última vez. |
| Compras | Ingresos de por vida atribuidos a este usuario, su última compra, número total de compras y una lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más información sobre estos datos, véase [Recogida de datos de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/).

![La pestaña Resumen de un perfil de usuario.]({% image_buster /assets/img_archive/user_profile2.png %})

### Ficha de compromiso {#engagement-tab}

La pestaña **Compromiso** contiene información sobre las interacciones de un usuario con los mensajes que le enviaste utilizando Braze.

| Categoría de compromiso | Contiene |
| --- | --- |
| Configuración de contacto | Estado de suscripción para correo electrónico, SMS y push, y los grupos de suscripción a los que está asociado este usuario para estos tres canales. Esta sección también incluye información sobre el registro de cambios para las fichas push. Consulte [correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) y [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) para obtener información sobre cómo se configuran las suscripciones y los opt-ins. |
| Campañas recibidas | Las campañas recibidas se marcan cuando el usuario recibe la campaña, o cuando detectamos por primera vez datos de interacción de un usuario. Seleccione una campaña de la lista para verla. |
| Segmentos | Segmentos en los que está incluido este usuario. Seleccione un segmento de la lista para verlo. |
| Estadísticas de comunicación | Cuándo fue la última vez que este usuario recibió mensajes tuyos de cada canal. |
| Atribución de instalación | Información sobre cómo y cuándo un usuario instaló su aplicación. Más información sobre [cómo entender las instalaciones de los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Varios | El [número de cubo aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) del usuario. |
| Mensajes recibidos en Canvas | Mensajes en lienzo que este usuario ha recibido y cuándo. Seleccione un mensaje de la lista para verlo. |
| Predicciones | Puntuaciones de [predicción de churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) y [predicción de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_events/) para este usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![La pestaña de interacción de un perfil de usuario que muestra su configuración de contactos y estadísticas de comunicación.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Ficha Historial de mensajes

La pestaña **Historial de mensajes** del perfil de usuario muestra los eventos recientes relacionados con la mensajería (unos 40) de un usuario individual de los últimos 30 días. Estos eventos incluyen los mensajes que el usuario ha enviado, recibido, con los que ha interactuado, etc. Tenga en cuenta que los datos de esta pestaña no se actualizan después de fusionar un usuario.

{% alert note %}
Si tienes algún comentario sobre esta tabla o quieres ver eventos concretos, envía un correo electrónico a [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) con el asunto "Comentarios sobre la pestaña del historial de mensajes".
{% endalert %}

![La pestaña Historial de mensajería que muestra las campañas y Lienzos que ha recibido un usuario.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualización y comprensión de los acontecimientos

Para cada evento de la tabla **Historial de mensajería**, puede ver el canal de mensajería, el tipo de evento, la fecha y hora en que se produjo el evento, la campaña o el mensaje Canvas asociado y los datos del dispositivo del usuario. Para filtrar eventos específicos, haga clic en **Filtros** y seleccione eventos de la lista.

##### Eventos de participación en mensajes

Los siguientes eventos de compromiso de mensajes están disponibles para correo electrónico, SMS, push, mensajes dentro de la aplicación, tarjetas de contenido y webhooks. Para obtener más información sobre cómo se realiza el seguimiento de eventos específicos, consulte el [glosario de eventos de compromiso de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Actos de compromiso disponibles |
| --- | --- |
| Correo electrónico | Rebotar<br>Clic<br>Entrega<br>Marcar como correo no deseado<br>Abierto (ver [nota sobre el evento abierto por correo electrónico](#note-on-email-open-event))<br>Enviar<br>Rebote blando<br>Cancelar suscripción |
| SMS | Envío por operador<br>Entrega<br>Fallo de entrega<br>Recepción entrante<br>Rechazo<br>Enviar |
| Push | Rebotar<br>Apertura influida<br>Primer plano de iOS<br>Abiertos<br>Enviar |
| Mensaje dentro de la aplicación | Clic<br>Impresión |
| Tarjetas de contenido | Clic<br>Rechazar<br>Impresión<br>Enviar |
| Webhooks | Enviar |
| WhatsApp | Anular<br>Entrega<br>Fallo<br>Frecuencia limitada<br>Recepción entrante<br>Leer<br>Enviar |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Eventos de cancelación de mensajes

Los eventos de interrupción de mensajes se producen cuando un mensaje enviado a un usuario se interrumpe debido a una lógica condicional en [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), o debido a tiempos de espera de renderización de Liquid.

Los eventos de cancelación están disponibles para los siguientes canales:

- Correo electrónico
- SMS
- Push
- Webhooks

Actualmente, los eventos de cancelación no están disponibles para los mensajes dentro de la aplicación ni para las tarjetas de contenido.

##### Eventos de limitación de frecuencia

Se produce un evento de limitación de frecuencia cuando un usuario está cualificado para recibir un mensaje, pero en realidad no lo recibe debido a la [configuración de limitación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) de frecuencia. Puede personalizar los ajustes de limitación de frecuencia desde **Configuración** > **Reglas de limitación de frecuencia**.

##### Destinos en blanco

Algunos envíos de mensajes pueden aparecer en el Historial de Mensajería con destinos en blanco (señalados con "-"). Esto se debe a que algunos canales, como las tarjetas de contenido y los webhooks, no recopilan datos del dispositivo en el envío del mensaje.

Los envíos de tarjetas de contenido se registran cuando la tarjeta está disponible para ser visualizada. Dado que las tarjetas de contenido se pueden ver en varios dispositivos, los datos del dispositivo no se registran para un envío. En su lugar, esta información se registra en el momento de la impresión (cuando se visualiza realmente la tarjeta). Los webhooks se envían a un punto final del sistema (no a un dispositivo), por lo que los datos de dispositivo no son aplicables.

#### Nota sobre el evento abierto por correo electrónico {#note-on-email-open-event}

El seguimiento de apertura de correo electrónico es propenso a errores en cualquier herramienta, incluida Braze. Con una variedad de funciones de protección de la privacidad ofrecidas por diferentes clientes de correo electrónico que bloquean la carga automática de imágenes o las cargan proactivamente en el servidor, los eventos de apertura de correo electrónico son susceptibles tanto de falsos positivos como de falsos negativos.

Aunque las estadísticas de apertura de correo electrónico pueden ser útiles en conjunto, por ejemplo, para comparar la eficacia de diferentes líneas del asunto, no debes asumir que un evento de apertura individual para un usuario individual es significativo.


