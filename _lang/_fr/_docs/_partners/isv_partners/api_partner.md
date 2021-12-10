---
nav_title: Intégration des partenaires API
alias: /fr_FR/api_partner_integration/
hidden: vrai
---

# Intégration des partenaires API

Les partenaires d'alliages ISV sont tenus d'ajouter leur nom de partenaire au champ `partenaire` dans leurs requêtes API, permettant à Braze de suivre l'utilisation des partenaires de l'API tels que les requêtes entrantes de partenaires. Veuillez consulter la structure de terminaison [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) suivante lors du développement de votre implémentation.

## Corps de la demande de partenaire

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optionnel, tableau d'Attributes Object),
   "events" : (optionnel, tableau d'objet événement),
   "achats" : (optionnel, tableau d'objet d'achat),
   "partenaire" : (obligatoire, chaîne)
}
```