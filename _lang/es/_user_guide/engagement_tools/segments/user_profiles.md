---
nav_title: Perfiles de usuario
article_title: Perfiles de usuario
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Este artículo de referencia describe cómo acceder al perfil de un usuario en el dashboard, los casos de uso del perfil y lo que contiene cada perfil."

---

# Perfiles de usuario

> Los perfiles de usuario son una excelente forma de encontrar información sobre usuarios concretos. Todos los datos persistentes asociados con un usuario se almacenan en su perfil de usuario.

## Acceder a perfiles

Para acceder al perfil de un usuario, ve a la página **Buscar usuarios** y busca un usuario por cualquiera de los siguientes criterios:

- ID de usuario externo
- ID de Braze
- Correo electrónico
- Número de teléfono
- Token de notificaciones push
- Alias de usuario con el formato "[user_alias]:[alias_name]", como, por ejemplo "amplitude_id:user_123"

Si se encuentra una coincidencia, puedes ver la información que has registrado para este usuario con el SDK de Braze. De lo contrario, si tu búsqueda devuelve varios perfiles de usuario, puedes fusionar cada perfil individualmente o realizar una fusión de usuarios masiva. Para obtener más información, consulta [Usuarios duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

{% alert important %}
Cuando se utiliza un número de teléfono en la búsqueda, se convierte al formato [`E.164`](https://en.wikipedia.org/wiki/e.164). Los usuarios cuyos números de teléfono no se pueden convertir al formato `E.164` (por ejemplo, porque el número de teléfono tiene un código de país o de área no válido) no se pueden buscar por número de teléfono.
{% endalert %}

![Resultados de la búsqueda con un banner que dice "Varios usuarios coinciden con tus criterios de búsqueda" y dos botones denominados Anterior y Siguiente.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Casos de uso

Los perfiles de usuario son un gran recurso para la solución de problemas y las pruebas, ya que puedes acceder fácilmente a información sobre el historial de interacción de un usuario, su pertenencia a un segmento, su dispositivo y su sistema operativo.

Por ejemplo, si un usuario informa de un problema y no estás seguro de qué dispositivo y sistema operativo está utilizando, puedes usar la [pestaña Resumen](#overview-tab) para encontrar esta información (siempre que tengas su correo electrónico o ID de usuario). También puedes ver el idioma de un usuario, lo que podría ser útil si estás solucionando un problema de una [campaña multilingüe]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) que no se comportó como se esperaba.

Puedes usar la [pestaña Interacción](#engagement-tab) para verificar si un determinado usuario recibió una campaña. Además, si este usuario concreto recibió la campaña, puedes ver cuándo la recibió. También puedes verificar si un usuario está en un segmento determinado y si ha optado por la adhesión voluntaria a push, correo electrónico o ambos. Esta información es útil para la solución de problemas. Por ejemplo, deberías comprobar esta información si un usuario no recibe una campaña que esperabas que recibiera o recibe una campaña que no esperabas que recibiera.

## Elementos del perfil de usuario

Hay cuatro secciones principales en el perfil de un usuario.

- **Resumen:** Información básica sobre el usuario, datos de sesión, atributos personalizados, eventos personalizados, compras y el dispositivo más reciente en el que el usuario inició sesión.
- **Interacción:** Información sobre la configuración de contacto del usuario, campañas recibidas, segmentos, estadísticas de comunicación, atribución de instalación y número de contenedor aleatorio.
- **Historial de mensajes:** Eventos recientes relacionados con la mensajería para este usuario en los últimos 30 días.
- **Elegibilidad de conmutadores de características:** Valida para qué conmutadores de características es elegible actualmente un usuario a través de despliegues, pasos en Canvas y experimentos. 

### Pestaña Resumen {#overview-tab}

La pestaña **Resumen** contiene información básica sobre un usuario y sus interacciones con tu aplicación o sitio web.

| Categoría del resumen | Contiene |
| --- | --- |
| Perfil | Sexo, grupo de edad, ubicación, idioma, localidad, zona horaria y fecha de nacimiento. |
| Resumen de sesiones | Cuántas sesiones tuvieron, cuándo fueron la primera y la última, y en qué aplicaciones. |
| Atributos personalizados | Qué atributos personalizados se atribuyen a este usuario y su valor asociado, incluidos los atributos personalizados anidados. |
| Dispositivos recientes | En cuántos dispositivos se conectaron, los detalles de cada dispositivo y sus identificadores de publicidad asociados (si los hubiera). |
| Eventos personalizados | Qué eventos personalizados ha realizado este usuario, cuántas veces y cuándo realizó cada evento por última vez. |
| Compras | Ingresos de por vida atribuidos a este usuario, su última compra, número total de compras y una lista de cada compra. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más información sobre estos datos, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![La pestaña Resumen de un perfil de usuario.]({% image_buster /assets/img_archive/user_profile2.png %})

### Pestaña Interacción {#engagement-tab}

La pestaña **Interacción** contiene información sobre las interacciones de un usuario con los mensajes que le enviaste utilizando Braze.

| Categoría de interacción | Contiene |
| --- | --- |
| Configuración de contacto | Estado de suscripción para correo electrónico, SMS y push, y los grupos de suscripción a los que está asociado este usuario para estos tres canales. Esta sección también incluye información del registro de cambios para los tokens de notificaciones push. Consulta [correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) y [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) para obtener información sobre cómo se configuran las suscripciones y las adhesiones voluntarias. |
| Campañas recibidas | Las campañas recibidas se marcan cuando el usuario recibe la campaña, o cuando detectamos por primera vez datos de interacción de un usuario. Selecciona una campaña de la lista para verla. |
| Segmentos | Segmentos en los que está incluido este usuario. Selecciona un segmento de la lista para verlo. |
| Estadísticas de comunicación | Cuándo fue la última vez que este usuario recibió mensajes tuyos de cada canal. |
| Atribución de instalación | Información sobre cómo y cuándo un usuario instaló tu aplicación. Más información sobre [cómo entender las instalaciones de los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Varios | El [número de contenedor aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) del usuario. |
| Mensajes de Canvas recibidos | Mensajes de Canvas que este usuario ha recibido y cuándo. Selecciona un mensaje de la lista para verlo. |
| Predicciones | Puntuaciones de [predicción de abandono]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) y [predicción de eventos]({{site.baseurl}}/user_guide/brazeai/predictive_events/) para este usuario. |
{: .reset-td-br-1 .reset-td-br_2 role="presentation" }

![La pestaña Interacción de un perfil de usuario que muestra su configuración de contactos y estadísticas de comunicación.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Pestaña Historial de mensajes

La pestaña **Historial de mensajes** del perfil de usuario muestra los eventos recientes relacionados con la mensajería (unos 40) de un usuario individual de los últimos 30 días. Estos eventos incluyen los mensajes que se le enviaron al usuario, que recibió, con los que interactuó, y más. 

{% alert note %}
Los datos de esta pestaña no se actualizan después de fusionar un usuario. Además, los eventos asociados con mensajes enviados a través de la API (por ejemplo, el [punto de conexión /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)) no aparecerán en esta pestaña si no se especifica un ID de campaña en esos envíos.
{% endalert %}

![La pestaña Historial de mensajes muestra las campañas y Canvas que ha recibido un usuario.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualización y comprensión de los eventos

Para cada evento de la tabla **Historial de mensajes**, puedes ver el canal de mensajería, el tipo de evento, la marca de tiempo en que se produjo el evento, la campaña o el mensaje de Canvas asociado y los datos del dispositivo del usuario. Para filtrar eventos específicos, haz clic en **Filtros** y selecciona eventos de la lista.

##### Eventos de interacción con mensajes

Los siguientes eventos de interacción con mensajes están disponibles para correo electrónico, SMS, push, mensajes dentro de la aplicación, tarjetas de contenido y webhooks. Para obtener más información sobre cómo se realiza el seguimiento de eventos específicos, consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Eventos de interacción disponibles |
| --- | --- |
| Correo electrónico | Rebote<br>Clic<br>Eventos de aplazamiento<br>Entrega<br>Marcar como correo no deseado<br>Apertura (ver [nota sobre el evento de apertura de correo electrónico](#note-on-email-open-event))<br>Envío<br>Rebote blando<br>Cancelar suscripción |
| SMS | Envío por operador<br>Entrega<br>Fallo de entrega<br>Recepción de entrada<br>Rechazo<br>Envío |
| Push | Rebote<br>Apertura influida<br>Primer plano de iOS<br>Apertura<br>Envío |
| Mensaje dentro de la aplicación | Clic<br>Impresión |
| Tarjetas de contenido | Clic<br>Descarte<br>Impresión<br>Envío |
| Webhooks | Envío |
| WhatsApp | Cancelación<br>Entrega<br>Fallo<br>Limitación de frecuencia<br>Recepción de entrada<br>Lectura<br>Envío |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Eventos de cancelación de mensajes

Los eventos de cancelación de mensajes se producen cuando un mensaje enviado a un usuario se cancela debido a lógica condicional en [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) o [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), o por tiempos de espera en el renderizado de Liquid.

Los eventos de cancelación están disponibles para los siguientes canales:

- Correo electrónico
- SMS
- Push
- Webhooks

Actualmente, los eventos de cancelación no están disponibles para los mensajes dentro de la aplicación ni para las tarjetas de contenido.

##### Eventos de limitación de frecuencia

Un evento de limitación de frecuencia se produce cuando un usuario está cualificado para recibir un mensaje, pero en realidad no lo recibe debido a la configuración de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Puedes personalizar los ajustes de limitación de frecuencia desde **Configuración** > **Reglas de limitación de frecuencia**.

##### Destinos en blanco

Algunos envíos de mensajes pueden aparecer en el historial de mensajes con destinos en blanco (indicados con "—"). Esto se debe a que algunos canales, como las tarjetas de contenido y los webhooks, no recopilan datos del dispositivo en el envío del mensaje.

Los envíos de tarjetas de contenido se registran cuando la tarjeta está disponible para ser visualizada. Dado que las tarjetas de contenido se pueden ver en varios dispositivos, los datos del dispositivo no se registran para un envío. En su lugar, esta información se registra en el momento de la impresión (cuando se visualiza realmente la tarjeta). Los webhooks se envían a un punto de conexión del sistema (no a un dispositivo), por lo que los datos de dispositivo no son aplicables.

#### Nota sobre el evento de apertura de correo electrónico {#note-on-email-open-event}

El seguimiento de apertura de correo electrónico es propenso a errores en cualquier herramienta, incluida Braze. Con la variedad de funciones de protección de la privacidad ofrecidas por diferentes clientes de correo electrónico que bloquean la carga automática de imágenes o las cargan proactivamente en el servidor, los eventos de apertura de correo electrónico son susceptibles tanto a falsos positivos como a falsos negativos.

Aunque las estadísticas de apertura de correo electrónico pueden ser útiles en conjunto, por ejemplo, para comparar la eficacia de diferentes líneas del asunto, no debes asumir que un evento de apertura individual para un usuario individual es significativo.

#### ¿Por qué algunos campos están en blanco en la pestaña Historial de mensajes?

Algunos campos pueden estar ausentes en la pestaña **Historial de mensajes** de un usuario en los siguientes escenarios:

- Cuando en un evento faltan datos para **Mensaje enviado**, esto indica que la campaña no tiene ninguna variación de mensaje.
- Cuando a un evento le faltan datos para **Campaña/Canvas** y **Mensaje enviado**, esto indica que este mensaje se envió desde una campaña de API (no campañas desencadenadas por API) que no especificó el `campaign_id` y `message_variation_id`. Estos campos son opcionales y pueden omitirse en el cuerpo de la solicitud. Cuando se especifican estos campos, esa información se rellena en los registros del historial de mensajes.
   - Si un mensaje concreto falta por completo del historial de mensajes, pero aparece en el registro de **Campañas recibidas**, es probable que el usuario haya recibido la campaña antes de ser identificado como el usuario actual. Si un perfil existente queda huérfano, se transfiere el registro de **Campañas recibidas**, pero no el historial de mensajes. 
- Cuando faltan datos para **Campaña/Canvas**, es posible que se haya enviado una prueba manual. Las pruebas manuales se registran en la pestaña **Historial de mensajes**, pero no se registrará la campaña o Canvas que se envió.

## Artículos relacionados

- [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST: Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST: Eliminar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)