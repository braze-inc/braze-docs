---
nav_title: Integration von API-Partnern
alias: /api_partner_integration/
hidden: true
---

# Integration von API-Partnern

Alloys ISV-Partner müssen ihren Partnernamen in das Feld `partner` in ihren API-Anfragen eintragen, damit Braze die Nutzung der API durch die Partner verfolgen kann, z. B. eingehende Anfragen von Partnern. Beziehen Sie sich bei der Entwicklung Ihrer Implementierung auf die folgende Endpunktstruktur [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

## Partner Anfrage Körper

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