---
nav_title: Integração com parceiros da API
alias: /api_partner_integration/
hidden: true
---

# Integração com parceiros da API

Os parceiros Alloys de ISV precisam adicionar o nome do parceiro ao campo `partner` nas solicitações de API, permitindo que a Braze rastreie o uso da API do parceiro, como as solicitações recebidas de parceiros. Consulte a estrutura de endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) ao desenvolver sua implementação.

## Corpo da solicitação do parceiro

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