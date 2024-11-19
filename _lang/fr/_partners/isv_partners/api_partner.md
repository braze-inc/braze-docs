---
nav_title: Intégration des partenaires API
alias: /api_partner_integration/
hidden: true
---

# Intégration des partenaires API

Les partenaires ISV Alloys sont tenus d'ajouter le nom de leur partenaire dans le champ `partner` de leurs requêtes d'API, ce qui permet à Braze de suivre l'utilisation des partenaires d'API, telles que les requêtes entrantes des partenaires. Référez-vous à la structure d’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) suivante lorsque vous développez votre implémentation.

## Corps de la requête du partenaire

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