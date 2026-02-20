---
nav_title: "Objeto de destinatarios"
article_title: Objeto Destinatarios API
page_order: 9
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto Destinatario Braze."

---

# Objeto de destinatarios

> El objeto destinatarios te permite solicitar o escribir información en nuestros endpoints.

Debes incluir uno de `external_user_id`, `user_alias`, `braze_id`, o `email` en este objeto. **Las solicitudes deben especificar sólo una.**

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
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

Cuando `send_to_existing_only` es `true`, Braze sólo envía el mensaje a los usuarios existentes. Sin embargo, no puedes utilizar esta bandera con alias de usuario. Cuando `send_to_existing_only` es `false`, debes incluir un atributo. Braze crea un usuario con la dirección `id` y sus atributos antes de enviar el mensaje.

- [ID de Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)
- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID de usuario externo]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [Priorización]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)
- [Objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/)

## Desduplicación del objeto destinatario

Al realizar una llamada a la API con el objeto destinatario, **si existe un destinatario duplicado que se dirige a la misma dirección (es decir, correo electrónico, push), Braze desduplica el usuario**, lo que significa que Braze elimina los usuarios idénticos, dejando uno solo.

Por ejemplo, si utilizas el mismo `external_user_id`, el usuario sólo recibirá un mensaje. Considera la posibilidad de realizar varias llamadas a la API si necesitas una solución para este comportamiento.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
