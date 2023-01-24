---
nav_title: Intégration des partenaires API
alias: /api_partner_integration/
hidden: true
---

# Intégration des partenaires API

Les partenaires ISV (Independent Software Vendor) Alloys sont tenus d’ajouter leur nom de partenaire au champ `partner` dans leurs demandes API, pour permettre à Braze de suivre l’utilisation du partenaire API, comme les demandes entrantes des partenaires. Indiquez la structure d’endpoint suivante [/utilisateurs/suivi]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) lors du développement de votre mise en œuvre.

## Corps de demande de partenaire

```
Content-Type: application/json
Authorization: Bearer VOTRE-CLÉ-API-REST
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (required, string)
}
```