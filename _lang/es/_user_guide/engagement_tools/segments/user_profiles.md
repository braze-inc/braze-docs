---
nav_title: Perfiles de usuario
article_title: Perfiles de usuario
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Este artículo de referencia describe cómo acceder al perfil de un usuario en el panel, los casos de uso del perfil y lo que contiene cada perfil."

---

# Perfiles de usuario

> Los perfiles de usuario son una forma estupenda de encontrar información sobre usuarios concretos. Todos los datos persistentes asociados a un usuario se almacenan en su perfil de usuario.

## Perfiles de acceso

Para acceder al perfil de un usuario, ve a la página **Buscar usuarios** y busca un usuario por cualquiera de las siguientes opciones:

- ID usuario externo
- ID de Braze
- Correo electrónico
- Número de teléfono
- Token de notificaciones push
- Alias de usuario con el formato "[user_alias]:[alias_name]", como, por ejemplo "amplitude_id:user_123"

Si se encuentra una coincidencia, puedes ver la información que has registrado para este usuario con el SDK de Braze. De lo contrario, si tu búsqueda devuelve varios perfiles de usuario, puedes fusionar cada perfil individualmente o realizar una fusión masiva de usuarios. Para una guía completa, consulta [Usuarios duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

Resultados de la búsqueda con un banner que dice "Varios usuarios coinciden con tus criterios de búsqueda" y dos botones denominados Anterior y Siguiente.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso

Los perfiles de usuario son un gran recurso para la solución de problemas y las pruebas, porque puedes acceder fácilmente a información sobre el historial de interacción de un usuario, su pertenencia a un segmento, su dispositivo y su sistema operativo.

Por ejemplo, si un usuario informa de un problema y no estás seguro de qué dispositivo y sistema operativo está utilizando, puedes utilizar la [pestaña Resumen](#overview-tab) para encontrar esta información (siempre que tengas su correo electrónico o ID de usuario). También puedes ver el idioma de un usuario, lo que podría ser útil si estás solucionando problemas de una [campaña multilingüe]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) que no se comportó como se esperaba.

Puedes utilizar la [pestaña Interacción](#engagement-tab) para verificar si un determinado usuario ha recibido una campaña. Además, si este usuario concreto recibió la campaña, puedes ver cuándo la recibió. También puedes verificar si un usuario está en un segmento determinado y si ha optado por la adhesión voluntaria al push, al correo electrónico o a ambos. Esta información es útil para la solución de problemas. Por ejemplo, debes comprobar esta información si un usuario no recibe una campaña que esperabas que recibiera o recibe una campaña que no esperabas que recibiera.

## Elementos del perfil de usuario

Hay cuatro secciones principales en el perfil de un usuario.

- **Resumen:** Información básica sobre el usuario, datos de sesión, atributos personalizados, eventos personalizados, compras y el dispositivo más reciente en el que el usuario inició sesión.
- **La interacción:** Información sobre la configuración de contacto del usuario, campañas recibidas, segmentos, estadísticas de comunicación, atribución de instalación y número de contenedor aleatorio.
- **Historial de mensajería:** Eventos recientes relacionados con la mensajería para este usuario en los últimos 30 días.
- **Características Elegibles:** Valida para qué banderas de características es elegible actualmente un usuario a través de despliegues, pasos en Canvas y experimentos. 

### Pestaña Resumen {#overview-tab}

La pestaña **Resumen** contiene información básica sobre un usuario y sus interacciones con tu aplicación o sitio web.

| Resumen categoría | Contiene |
| --- | --- |
| Perfil | Sexo, grupo de edad, ubicación, idioma, localidad, zona horaria y fecha de nacimiento. |
| Resumen de las sesiones | Cuántas sesiones tuvieron, cuándo fueron la primera y la última, y en qué aplicaciones. |
| Atributos personalizados | Qué atributos personalizados se atribuyen a este usuario y su valor asociado, incluidos los atributos personalizados anidados. |
| Dispositivos recientes | En cuántos dispositivos se conectaron, los detalles de cada dispositivo y sus ID de publicidad asociados (si los hay). |
| Eventos personalizados | Qué eventos personalizados ha realizado este usuario, cuántas veces y cuándo realizó cada evento por última vez. |
| Compras | Ingresos de por vida atribuidos a este usuario, su última compra, el número total de compras y una lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más información sobre estos datos, consulta [Recogida de datos de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/).

\![La pestaña Resumen de un perfil de usuario.]({% image_buster /assets/img_archive/user_profile2.png %})

### Pestaña de interacción {#engagement-tab}

La pestaña **"Interacción"** contiene información sobre las interacciones de un usuario con los mensajes que le enviaste utilizando Braze.

| Categoría de interacción | Contiene |
| --- | --- |
| Configuración de los contactos | Estado de suscripción para correo electrónico, SMS y push, y los grupos de suscripción a los que está asociado este usuario para estos tres canales. Esta sección también incluye información del registro de cambios para los tokens de notificaciones push. Consulta [correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) y [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) para obtener información sobre cómo se configuran las suscripciones y las adhesiones voluntarias. |
| Campañas recibidas | Las campañas recibidas se marcan cuando el usuario recibe la campaña, o cuando detectamos por primera vez datos de interacción de un usuario. Selecciona una campaña de la lista para verla. |
| Segmentos | Segmentos en los que está incluido este usuario. Selecciona un segmento de la lista para verlo. |
| Estadísticas de comunicación | Cuándo fue la última vez que este usuario recibió mensajes tuyos de cada canal. |
| Atribución de instalación | Información sobre cómo y cuándo un usuario instaló tu aplicación. Más información sobre [cómo entender las instalaciones de los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Varios | El [número de contenedor]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) aleatorio del usuario [.]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) |
| Mensajes de Canvas recibidos | Mensajes de Canvas que ha recibido este usuario y cuándo. Selecciona un mensaje de la lista para verlo. |
| Predicciones | Puntuaciones de [predicción de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) y [predicción de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_events/) de este usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![La pestaña de interacción de un perfil de usuario que muestra su configuración de contactos y estadísticas de comunicación.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Pestaña Historial de mensajes

La pestaña **Historial de mensajes** del perfil de usuario muestra los eventos recientes relacionados con la mensajería (unos 40) de un usuario individual de los últimos 30 días. Estos eventos incluyen los mensajes que el usuario ha enviado, recibido, con los que ha interactuado, etc. Ten en cuenta que los datos de esta pestaña no se actualizan después de fusionar un usuario.

{% alert note %}
Si tienes algún comentario sobre esta tabla o quieres ver eventos concretos, envía un correo electrónico a [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) con el asunto "Comentarios sobre la pestaña del historial de mensajes".
{% endalert %}

\![La pestaña Historial de mensajería que muestra las campañas y Lienzos que ha recibido un usuario.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Ver y comprender acontecimientos

Para cada evento de la tabla **Historial de mensajería**, puedes ver el canal de mensajería, el tipo de evento, la fecha y hora en que se produjo el evento, la campaña o mensaje Canvas asociado y los datos de dispositivo del usuario. Para filtrar por eventos concretos, haz clic en **Filtros** y selecciona los eventos de la lista.

##### Actos de interacción con mensajes

Los siguientes eventos de interacción de mensajes están disponibles para correo electrónico, SMS, push, mensajes dentro de la aplicación, tarjetas de contenido y webhooks. Para saber más sobre cómo se realiza el seguimiento de determinados eventos, consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Eventos de interacción disponibles |
| --- | --- |
| Correo electrónico | Rebotar<br>Clic<br>Eventos de aplazamiento<br>Entrega<br>Marcar como correo no deseado<br>Abierto (ver [nota sobre el evento abierto por correo electrónico](#note-on-email-open-event))<br>Envía<br>Rebote blando<br>Cancelar suscripción |
| SMS | Envío de operador<br>Entrega<br>Fallo en la entrega<br>Recepción entrante<br>Rechazo<br>Envía |
| Push | Rebotar<br>Influenced Opens<br>Primer plano iOS<br>Abre<br>Envía |
| Mensaje dentro de la aplicación | Clic<br>Impresión |
| Tarjetas de contenido | Clic<br>Desestimar<br>Impresión<br>Envía |
| Webhooks | Envía |
| WhatsApp | Aborta<br>Entrega<br>Fallo<br>Limitación de frecuencia<br>Recepción entrante<br>Leer<br>Envía |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Eventos de cancelación de mensajes

Los eventos de cancelación de mensajes se producen cuando un mensaje enviado a un usuario se cancela debido a una lógica condicional en [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) o en [el contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), o debido a tiempos de espera de renderización de Liquid.

Los eventos de cancelación están disponibles para los siguientes canales:

- Correo electrónico
- SMS
- Push
- Webhooks

Actualmente, los eventos de cancelación no están disponibles para los mensajes dentro de la aplicación ni para las tarjetas de contenido.

##### Eventos de limitación de frecuencia

Se produce un evento de limitación [de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) frecuencia cuando un usuario está cualificado para recibir un mensaje, pero en realidad no lo recibe debido a la configuración [de limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Puedes personalizar la configuración de limitación de frecuencia desde **Configuración** > Reglas de limitación de frecuencia.

##### Destinos en blanco

Algunos envíos de mensajes pueden aparecer en el Historial de mensajería con destinos en blanco (señalados con "-"). Esto se debe a que algunos canales, como las tarjetas de contenido y los webhooks, no recopilan datos de dispositivo en el envío de mensajes.

Los envíos de tarjetas de contenido se registran cuando la tarjeta está disponible para ser vista. Como las tarjetas de contenido pueden verse en varios dispositivos, los datos de dispositivo no se registran para un envío. En cambio, esta información se registra en el momento de la impresión (cuando se ve realmente la tarjeta). Los webhooks se envían a un punto final del sistema (no a un dispositivo), por lo que los datos de dispositivo no son aplicables.

#### Nota sobre el evento abierto por correo electrónico {#note-on-email-open-event}

El seguimiento de apertura de correo electrónico es propenso a errores en cualquier herramienta, incluida Braze. Con una variedad de características de protección de la privacidad ofrecidas por diferentes clientes de correo electrónico que bloquean la carga automática de imágenes o las cargan proactivamente en el servidor, los eventos de apertura de correo electrónico son susceptibles tanto de falsos positivos como de falsos negativos.

Aunque las estadísticas de apertura de correo electrónico pueden ser útiles en conjunto, por ejemplo, para comparar la eficacia de diferentes líneas del asunto, no debes asumir que un evento de apertura individual para un usuario individual es significativo.

#### ¿Por qué algunos campos están en blanco en la pestaña Historial de mensajes?

Algunos campos pueden estar ausentes en la pestaña **Historial de mensajes** de un usuario en los siguientes escenarios:

- Cuando en un evento faltan datos para **Mensaje enviado**, esto indica que la campaña no tiene ninguna variación de mensaje.
- Cuando a un evento le faltan datos para **Campaña/Canvas** y **Mensaje enviado**, esto indica que este mensaje fue enviado desde una campaña API (no campañas desencadenadas por API) que no especificó el `campaign_id` y `message_variation_id`. Estos campos son opcionales y pueden omitirse en el cuerpo de la solicitud. Cuando se especifican estos campos, esa información se rellena en los registros del historial de mensajes.
   - Si un mensaje concreto falta por completo del historial de mensajes, pero aparece en el registro de **Campañas recibidas**, es probable que el usuario haya recibido la campaña antes de ser identificado como el usuario actual. Si un perfil existente queda huérfano, se transfiere el registro de **campañas recibidas**, pero no el historial de mensajes. 
- Si faltan datos para **Campaign/Canvas**, es posible que se haya enviado una prueba manual. Las pruebas manuales se registran en la pestaña **Historial de mensajería**, pero no se registrará la campaña o Canvas que se envió.


