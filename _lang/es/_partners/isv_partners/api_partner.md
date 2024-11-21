---
nav_title: Integración de socios de API
alias: /api_partner_integration/
hidden: true
---

# Integración de socios de API

Los socios ISV de Alloys deben añadir el nombre de su socio en el campo `partner` de sus solicitudes de API, lo que permite a Braze realizar un seguimiento del uso de la API por parte de los socios, como las solicitudes entrantes de socios. Haz referencia a la siguiente estructura de punto final [/usuarios/seguimiento]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) cuando desarrolles tu aplicación.

## Cuerpo de la solicitud del socio

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (required, string)
}
```