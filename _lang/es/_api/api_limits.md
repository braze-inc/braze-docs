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

La siguiente tabla enumera los límites de velocidad predeterminados de la API para diferentes tipos de solicitudes. Estos límites predeterminados pueden aumentarse previa solicitud. Ponte en contacto con tu administrador del éxito del cliente para obtener más información.

{% alert note %}
Las solicitudes que no figuran en esta tabla comparten un límite de velocidad predeterminado total de 250 000 solicitudes por hora.
{% endalert %}

| Tipo de solicitud                                                                                                                                                                                                                                           | Rate limit de API predeterminado                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`/users/track`][10]                                                                                                                                                                                                                                   | **Solicitudes:** 3.000 solicitudes cada tres segundos.<br><br>**Procesamiento por lote:** 75 eventos, 75 compras y 75 atributos por solicitud API. Para más información, consulta [Agrupar solicitudes de seguimiento de usuarios](#batch-user-track).<br><br>**Límites de usuarios activos al mes CY 24-25:** ver [límites de usuarios activos al mes CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **Si te incorporaste el 22 de agosto de 2024 o después:** 250 solicitudes por minuto. <br><br> **Si te incorporaste antes del 22 de agosto de 2024:** 2.500 solicitudes por minuto.                                                                                                                                                                   |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 20 000 solicitudes por minuto, repartidas entre los puntos finales.                                                                                                                                  |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1.000 solicitudes por minuto.                                                                                                                                                                 |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1.000 solicitudes por minuto.                                                                                                                                                                 |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1.000 peticiones por hora, compartidas con el punto final `/purchases/product_list`.                                                                                                               |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1.000 peticiones por hora, compartidas con el punto final `/events/list`.                                                                                                                          |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 50.000 solicitudes por minuto.                                                                                                                                                                |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | 250 solicitudes por minuto para llamadas de difusión (cuando solo se especifica un segmento o Audiencia conectada). Por lo demás, 250 000 solicitudes por hora repartidas entre los puntos finales.                     |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 100 solicitudes al día.                                                                                                                                                                      |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 5.000 solicitudes por minuto.                                                                                                                                                                 |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | 1.000 solicitudes por minuto, por espacio de trabajo.                                                                                                                                                  |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | 10 solicitudes por minuto, por espacio de trabajo.                                                                                                                                                     |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 50 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                       |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 16.000 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                   |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 50 peticiones por minuto compartidas entre los puntos finales.                                                                                                                                       |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 5.000 solicitudes al día, por empresa, compartidas entre los terminales.                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## Procesamiento por lotes de las solicitudes API

Las API de Braze están diseñadas para soportar la dosificación. Con el procesamiento por lotes, Braze puede recibir tantos datos como sea posible en una sola llamada a la API, para que no tengas que hacer muchas llamadas a la API. Para Braze, es más eficiente procesar los datos por lotes que procesarlos llamada a llamada. Por ejemplo, gestionar 1000 llamadas API por lotes requiere menos recursos que gestionar 75 000 llamadas individuales. El procesamiento por lotes es extremadamente importante para cualquier aplicación que pueda requerir más de 75 000 llamadas por hora.

{% alert note %}
Los aumentos del límite de velocidad de la API REST se consideran en función de las necesidades de los clientes que hacen uso de las funciones de procesamiento por lotes de la API.
{% endalert %}

### Procesamiento por lotes de las solicitudes de seguimiento de usuarios {#batch-user-track}

Cada solicitud `/users/track` puede contener hasta 75 objetos de evento, 75 objetos de atributo y 75 objetos de compra. Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno. En total, esto significa que se puede actualizar a un máximo de 225 usuarios en una sola llamada. Además, un mismo perfil de usuario puede ser actualizado por varios objetos.

Las solicitudes realizadas a este punto final, generalmente, comenzarán a procesarse en este orden:

1. Atributos
2. Eventos
3. Compras

### Procesamiento por lotes de las solicitudes de puntos finales de mensajería

Una única solicitud a [los puntos finales de mensajería][1] puede llegar a cualquiera de los siguientes:

- Hasta 50 `external_ids` específicos, cada uno con parámetros de mensaje individuales
- Un segmento de cualquier tamaño creado en el panel de Braze, especificado por su `segment_id`
- Usuarios que coinciden con filtros de audiencia adicionales de cualquier tamaño, definidos en la solicitud como un objeto de [audiencia conectado][2] 

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
Las cabeceras HTTP se devolverán en minúsculas. Este comportamiento se ajusta al protocolo HTTP/2, que exige que todos los nombres de los campos de encabezado estén en minúsculas. Esto difiere de HTTP/1.X, donde los nombres de los encabezados no distinguían entre mayúsculas y minúsculas, pero se solían escribir con varias mayúsculas.
{% endalert %}

Si tienes preguntas sobre los límites de la API, ponte en contacto con tu administrador del éxito del cliente o abre un [ticket de soporte][support].

### Retardo óptimo entre puntos finales

{% alert note %}
Te recomendamos que permitas un retraso de 5 minutos entre llamadas consecutivas al punto final para minimizar los errores.
{% endalert %}

Comprender el retraso óptimo entre puntos finales es crucial a la hora de realizar llamadas consecutivas a la API de Braze. Los problemas surgen cuando los puntos finales dependen del procesamiento satisfactorio de otros puntos finales y, si se los llama demasiado pronto, podrían provocar errores. Por ejemplo, si estás asignando a los usuarios un alias a través de nuestro punto final `/user/alias/new`, y luego pulsas ese alias para enviar un evento personalizado a través de nuestro punto final `/users/track`, ¿cuánto tiempo debes esperar?

En condiciones normales, el tiempo que tarda en producirse la coherencia eventual de nuestros datos es de 10-100 ms (1/10 de segundo). Sin embargo, puede haber casos en los que esa coherencia tarde más tiempo en producirse, por lo que te recomendamos que dejes pasar 5 minutos entre una llamada y otra para minimizar la probabilidad de error.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[17.3]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
[46]: {{site.baseurl}}/api/endpoints/cdi/get_integration_list/
[47]: {{site.baseurl}}/api/endpoints/cdi/job_sync/
[48]: {{site.baseurl}}/api/endpoints/cdi/job_sync_status/
