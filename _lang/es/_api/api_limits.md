---
nav_title: Límites de velocidad
article_title: Límites de velocidad de la API
page_order: 4.5
description: "Este artículo de referencia cubre los límites de velocidad de la API para la infraestructura de la API de Braze."
page_type: reference

---

# Límites de velocidad

> La infraestructura de la API de Braze está diseñada para gestionar grandes volúmenes de datos de toda nuestra base de clientes. Para ello, imponemos límites de velocidad de API por espacio de trabajo.

Un límite de velocidad es el número de peticiones que puede recibir la API en un periodo de tiempo determinado. Muchos incidentes de denegación de servicio basados en la carga en grandes sistemas son involuntarios -causados por errores en el software o las configuraciones-, no ataques maliciosos. Los límites de velocidad comprueban que esos errores no privan a nuestros clientes de los recursos de la API de Braze. Si se envían demasiadas solicitudes en un periodo de tiempo determinado, es posible que veas respuestas de error con un código de estado `429`, que indica que se ha alcanzado el límite de velocidad.

{% alert warning %}
Los límites de velocidad API están sujetos a cambios en función del uso adecuado de nuestro sistema. Animamos a que se establezcan límites razonables al realizar una llamada a la API para evitar daños o usos indebidos.
{% endalert %}

## Límites de velocidad por tipo de solicitud

Consulta a continuación los límites de velocidad predeterminados de la API para distintos tipos de solicitudes. Estos límites predeterminados pueden aumentarse previa solicitud. Ponte en contacto con tu administrador del éxito del cliente para obtener más información.

### Solicitudes con diferentes límites de velocidad

| Tipo de solicitud                                                                                                                                                                                                                                           | Rate limit de API predeterminado                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **Solicitudes:** 3.000 solicitudes cada tres segundos.<br><br>**Procesamiento por lote:** 75 eventos, 75 compras y 75 atributos por solicitud API. Para más información, consulta [Agrupar solicitudes de seguimiento de usuarios](#batch-user-track).<br><br>**Límites de usuarios activos al mes CY 24-25:** ver [límites de usuarios activos al mes CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **Si te incorporaste el 22 de agosto de 2024 o después:** 250 solicitudes por minuto. <br><br> **Si te incorporaste antes del 22 de agosto de 2024:** 2.500 solicitudes por minuto.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 20 000 solicitudes por minuto, repartidas entre los puntos finales.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1.000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1.000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1.000 peticiones por hora, compartidas con el punto final `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1.000 peticiones por hora, compartidas con el punto final `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 50.000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | 250 solicitudes por minuto para llamadas de difusión (cuando solo se especifica un segmento o Audiencia conectada). Por lo demás, 250 000 solicitudes por hora repartidas entre los puntos finales.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 100 solicitudes al día.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 5.000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1.000 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 10 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 50 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 16.000 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 50 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 peticiones por minuto compartidas entre los puntos finales. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 5.000 solicitudes al día, por empresa, compartidas entre los terminales.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 50 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 20 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 100 solicitudes por minuto.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Solicitudes con límites de velocidad compartidos

Las siguientes solicitudes tienen un límite de velocidad de 250.000 solicitudes por hora, compartido entre ellas.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

## Procesamiento por lotes de las solicitudes API

Las API de Braze están diseñadas para soportar la dosificación. Con el procesamiento por lotes, Braze puede recibir tantos datos como sea posible en una sola llamada a la API, para que no tengas que hacer muchas llamadas a la API. Para Braze, es más eficiente procesar los datos por lotes que procesarlos llamada a llamada. Por ejemplo, gestionar 1000 llamadas API por lotes requiere menos recursos que gestionar 75 000 llamadas individuales. El procesamiento por lotes es extremadamente importante para cualquier aplicación que pueda requerir más de 75 000 llamadas por hora.

{% alert note %}
Los aumentos del límite de velocidad de la API REST se consideran en función de las necesidades de los clientes que hacen uso de las funciones de procesamiento por lotes de la API.
{% endalert %}

### Solicitudes por lotes para el punto final Seguimiento de usuarios {#batch-user-track}

Cada solicitud `/users/track` puede contener hasta 75 objetos de evento, 75 objetos de atributo y 75 objetos de compra. Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno. En total, esto significa que se pueden actualizar hasta 225 usuarios en una sola llamada. Además, un mismo perfil de usuario puede ser actualizado por varios objetos.

Las solicitudes realizadas a este punto final, generalmente, comenzarán a procesarse en este orden:

1. Atributos
2. Eventos
3. Compras

### Procesamiento por lotes de las solicitudes de puntos finales de mensajería

Una única solicitud a [los puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging/) puede llegar a cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Usuarios que coinciden con filtros de audiencia adicionales de cualquier tamaño, definidos en la solicitud como un objeto de [audiencia conectado]({{site.baseurl}}/api/objects_filters/connected_audience/) 

### Ejemplo de solicitud por lotes

En el siguiente ejemplo, se utiliza `external_id` para realizar una llamada API para correo electrónico y SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Control de los límites de velocidad

Cada solicitud de API enviada a Braze devuelve la siguiente información en los encabezados de respuesta:

| Nombre de la cabecera             | Descripción                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | El número máximo de peticiones que puedes hacer en un intervalo especificado (tu límite de velocidad). |
| `X-RateLimit-Remaining` | El número de solicitudes que quedan en la ventana actual de límite de velocidad.                          |
| `X-RateLimit-Reset`     | La hora a la que se restablece la ventana de límite de velocidad actual en segundos de época UTC.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Esta información se incluye intencionadamente en el encabezado de la respuesta a la solicitud API en lugar de en el panel de Braze. Esto permite que tu sistema reaccione mejor en tiempo real mientras interactúas con nuestra API. Por ejemplo, si el valor de `X-RateLimit-Remaining` cae por debajo de un determinado umbral, puede que quieras ralentizar el envío para asegurarte de que se envían todos los correos electrónicos transaccionales. O, si llega a cero, es conveniente pausar todos los envíos hasta que transcurra el tiempo especificado en `X-RateLimit-Reset`.

{% alert note %}
Las cabeceras HTTP se devolverán en minúsculas. Este comportamiento se ajusta al protocolo HTTP/2, que exige que todos los nombres de los campos de encabezado estén en minúsculas. Esto difiere de HTTP/1.X, donde los nombres de los encabezados no distinguían entre mayúsculas y minúsculas, pero solían escribirse con varias mayúsculas.
{% endalert %}

Si tienes preguntas sobre los límites de la API, ponte en contacto con tu administrador del éxito del cliente o abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

{% alert tip %}
Puedes utilizar el [panel de uso de la API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) para ver y comparar el tráfico entrante con tus límites de velocidad.
{% endalert %}

### Retardo óptimo entre puntos finales

{% alert note %}
Te recomendamos que permitas un retraso de 5 minutos entre llamadas consecutivas al punto final para minimizar los errores.
{% endalert %}

Comprender el retraso óptimo entre puntos finales es crucial a la hora de realizar llamadas consecutivas a la API de Braze. Los problemas surgen cuando los puntos finales dependen del procesamiento satisfactorio de otros puntos finales y, si se los llama demasiado pronto, podrían provocar errores. Por ejemplo, si estás asignando a los usuarios un alias a través de nuestro punto final `/user/alias/new`, y luego pulsas ese alias para enviar un evento personalizado a través de nuestro punto final `/users/track`, ¿cuánto tiempo debes esperar?

En condiciones normales, el tiempo que tarda en producirse la coherencia eventual de nuestros datos es de 10-100 ms (1/10 de segundo). Sin embargo, puede haber casos en los que esa coherencia tarde más tiempo en producirse, por lo que te recomendamos que dejes pasar 5 minutos entre una llamada y otra para minimizar la probabilidad de error.

