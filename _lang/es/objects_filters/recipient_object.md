---
nav_title: "Objeto de destinatarios"
article_title: Objeto Destinatarios API
page_order: 9
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto Destinatario Braze."

---

# Objeto de destinatarios

> El objeto destinatarios te permite solicitar o escribir información en nuestros endpoints.

En este objeto se requiere `external_user_id`, `user_alias`, `braze_id`, o `email`. **Las solicitudes deben especificar sólo una.**

El objeto destinatarios te permite combinar el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/), el [objeto propiedades desencadenantes]({{site.baseurl}}/api/objects_filters/trigger_properties_object/), el [objeto propiedades de entrada Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) y el [objeto atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

## Cuerpo del objeto

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases,
  "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
}]
```

Cuando `send_to_existing_only` es `true`, Braze sólo enviará el mensaje a los usuarios existentes. Sin embargo, esta bandera no puede utilizarse con alias de usuario. Cuando `send_to_existing_only` es `false`, debe incluirse un atributo. Braze creará un usuario con la dirección `id` y los atributos antes de enviar el mensaje.

- [ID de Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Priorización]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [Objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Desduplicación del objeto destinatario

Al realizar una llamada a la API con el objeto destinatario, **si existe un destinatario duplicado que se dirija a la misma dirección (es decir, correo electrónico, push), se dedupirá al usuario**, es decir, se eliminarán los usuarios idénticos, dejando uno solo. 

Por ejemplo, si se utiliza el mismo `external_user_id`, solo se recibirá un mensaje. Considera la posibilidad de realizar varias llamadas a la API si necesitas una solución para este comportamiento.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```
