---
nav_title: "Objeto de destinatarios"
article_title: Objeto Destinatarios API
page_order: 9
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto Destinatario Braze."

---

# Objeto de destinatarios

> El objeto destinatarios te permite solicitar o escribir información en nuestros endpoints.

En este objeto se requiere `external_user_id`, `user_alias`, o `email`. **Las solicitudes deben especificar sólo una.**

{% alert important %}
Especificar un destinatario por dirección de correo electrónico está actualmente en acceso temprano. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

El objeto destinatario te permite combinar el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/), el [objeto propiedades de desencadenar]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) y [el objeto propiedades de entrada Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).

## Cuerpo del objeto

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas Entry Properties
}]
```

- [Alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)
- [ID usuario externo]({{site.baseurl}}/api/basics/#user-ids)
- [Priorización]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/#identifying-users-by-email)

## Desduplicación del objeto destinatario

Al realizar una llamada a la API con el objeto destinatario, **si existe un destinatario duplicado que se dirija a la misma dirección (es decir, correo electrónico, push), se dedupirá al usuario**, es decir, se eliminarán los usuarios idénticos, dejando uno solo. 

Por ejemplo, si se utiliza el mismo `external_user_id`, solo se recibirá un mensaje. Considera la posibilidad de realizar varias llamadas a la API si necesitas una solución para este comportamiento.

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}} 
]}
```