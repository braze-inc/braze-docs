
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Aplicamos el límite de velocidad predeterminado de Braze de 250 000 solicitudes por hora a este punto final, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Este punto final tiene un límite de velocidad de 5000 peticiones por día y empresa. Este límite de velocidad se comparte con los puntos finales GET, DELETE y POST de `/scim/v2/Users/`, tal como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Este punto final tiene un límite de velocidad de 5000 peticiones por día y empresa. Este límite de velocidad se comparte con los puntos finales PUT, GET, DELETE y POST de `/scim/v2/Users/`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Este punto final tiene un límite de velocidad de 5000 peticiones por día y empresa. Este límite de velocidad se comparte con los puntos finales PUT, GET y POST de `/scim/v2/Users/`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Este punto final tiene un límite de velocidad de 5000 peticiones por día y empresa. Este límite de velocidad se comparte con los puntos finales PUT, GET y DELETE de `/scim/v2/Users/`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Este punto final tiene un límite de velocidad de 5000 peticiones por día y empresa. Este límite de velocidad se comparte con los puntos finales PUT, GET, DELETE y POST de `/scim/v2/Users/`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Aplicamos un límite de velocidad de 1000 solicitudes por minuto a este punto final, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
A partir del 28 de octubre de 2024, aplicamos un límite de velocidad base de 3.000 solicitudes cada tres segundos a este punto final para todos los clientes. Cada solicitud `/users/track` puede contener hasta 75 objetos de evento, 75 objetos de atributo y 75 objetos de compra. Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno. En total, esto significa que se puede actualizar a un máximo de 225 usuarios en una sola llamada. Además, el mismo perfil de usuario puede ser actualizado por varios objetos.

Se aplican límites diferentes a los clientes que han comprado **Usuarios activos al mes - CY 24-25**. Para más detalles sobre estos límites, consulta [Usuarios activos al mes - Límites CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25).

Consulta nuestra página sobre [los límites de velocidad de la API]({{site.baseurl}}/api/api_limits/) para obtener más detalles, y ponte en contacto con tu responsable de satisfacción de los clientes si necesitas aumentar tu límite.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Si te incorporaste a Braze a partir del 22 de agosto de 2024, este punto final tiene un límite de velocidad de 250 solicitudes por minuto, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

También puedes aumentar el límite de velocidad de este punto final a 40 peticiones por segundo cumpliendo los siguientes requisitos:

- Tu espacio de trabajo tiene habilitado el límite de velocidad predeterminado (250 peticiones por minuto). Ponte en contacto con tu administrador de cuentas Braze para que te ayude a eliminar cualquier límite de velocidad preexistente que puedas tener.
- Tu solicitud incluye el parámetro `fields_to_export` para enumerar todos los campos que quieres recibir.

{% alert important %}
Si incluyes `canvases_received` o `campaigns_received` en el parámetro `fields_to_export`, tu solicitud no podrá acogerse al límite de velocidad más rápido. Te recomendamos que sólo los incluyas en tu solicitud si tienes un caso de uso específico para ellos.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Aplicamos a este punto final un límite de velocidad compartido de 20.000 peticiones por minuto. Este límite de velocidad se comparte con los puntos finales `/users/alias/new`, `/users/identify`, `/users/merge`, y `/users/alias/update`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Aplicamos a este punto final un límite de velocidad compartido de 20.000 peticiones por minuto. Este límite de velocidad se comparte con los puntos finales `/users/delete`, `/users/identify`, `/users/merge`, y `/users/alias/update`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Aplicamos a este punto final un límite de velocidad compartido de 20.000 peticiones por minuto. Este límite de velocidad se comparte con los puntos finales `/users/delete`, `/users/alias/new`, `/users/identify`, y `/users/merge`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Aplicamos a este punto final un límite de velocidad compartido de 20.000 peticiones por minuto. Este límite de velocidad se comparte con los puntos finales `/users/delete`, `/users/alias/new`, `/users/merge`, y `/users/alias/update`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Aplicamos a este punto final un límite de velocidad compartido de 20.000 peticiones por minuto. Este límite de velocidad se comparte con los puntos finales `/users/delete`, `/users/alias/new`, `/users/identify`, y `/users/alias/update`, como se documenta en [Límites de tasa de la API]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Aplicamos un límite de velocidad compartido de 1.000 peticiones por hora a este punto final. Este límite de velocidad se comparte con los puntos finales `/events`, `/events/list`, y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "events" %}
Aplicamos un límite de velocidad compartido de 1.000 peticiones por hora a este punto final. Este límite de velocidad se comparte con los puntos finales `/custom_attributes`, `/events/list`, y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Aplicamos un límite de velocidad compartido de 1.000 peticiones por hora a este punto final. Este límite de velocidad se comparte con los puntos finales `/custom_attributes`, `/events`, y `/purchases/product_list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Aplicamos un límite de velocidad compartido de 1.000 peticiones por hora a este punto final. Este límite de velocidad se comparte con los puntos finales `/custom_attributes`, `/events`, y `/events/list`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Al especificar un segmento o Audiencia Conectada en tu solicitud, aplicamos un límite de velocidad de 250 solicitudes por minuto a este punto final. De lo contrario, si se especifica un `external_id`, este punto final tiene un límite de velocidad predeterminado de 250 000 solicitudes por hora compartido entre `/messages/send`, `/campaigns/trigger/send` y `/canvas/trigger/send`, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
Los correos electrónicos transaccionales Braze no están sujetos a ningún límite de velocidad. Dependiendo del paquete que hayas elegido, el SLA cubre un número determinado de correos electrónicos transaccionales por hora. Las solicitudes que superen esa tasa seguirán enviándose, pero no estarán cubiertas por el SLA. El 99,9 % de los correos electrónicos se enviarán en menos de un minuto.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
El número máximo diario de identificadores de envío personalizados que pueden crearse a través de este punto final es de 100 para un espacio de trabajo determinado. Cada combinación de `send_id` y `campaign_id` que crees contará para tu límite diario. Los encabezados de respuesta de cualquier solicitud válida incluyen el estado actual del límite de velocidad; para más detalles, consulta [los límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Este punto final tiene un límite de velocidad de 5000 solicitudes por minuto compartido entre los puntos `/subscription/status/set` y `/v2/subscription/status/set`, tal y como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Este punto final tiene un límite de velocidad de 50 peticiones por minuto.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Este punto final tiene un límite de velocidad de 20 peticiones por minuto.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Este punto final tiene un límite de velocidad de 100 peticiones por minuto.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Los puntos finales de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits/#batching-api-requests). Una única solicitud a los puntos finales de mensajería puede llegar a cualquiera de los siguientes elementos:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

{% endif %}

{% if include.category == "send messages endpoints" %}

Los puntos finales de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits/#batching-api-requests). Una única solicitud a los puntos finales de mensajería puede llegar a cualquiera de los siguientes elementos:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Este punto final tiene un límite de velocidad de 250.000 peticiones por minuto.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Los puntos finales de Braze admiten [solicitudes de API por lotes]({{site.baseurl}}/api/api_limits/#batching-api-requests). Una única solicitud a los puntos finales de mensajería puede llegar a cualquiera de los siguientes elementos:

- Hasta 50 `external_ids` específicos
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Un segmento de audiencia de cualquier tamaño, definido en la solicitud como un objeto de [audiencia conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Este punto final tiene un límite de velocidad compartido de 16 000 solicitudes por minuto entre todos los puntos finales de elementos de catálogo asíncronos, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Este punto final tiene un límite de velocidad compartido de 50 solicitudes por minuto entre todos los puntos finales de elementos de catálogo síncronos, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Este punto final tiene un límite de velocidad compartido de 50 solicitudes por minuto entre todos los puntos finales del catálogo síncrono, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Este punto final tiene un límite de velocidad compartido de 50 peticiones por minuto entre todos los puntos finales asíncronos de campos de catálogo y selecciones, como se documenta en [Límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Este punto final tiene un límite de velocidad de 50 000 peticiones por minuto.

{% endif %}

