---
nav_title: "POST: Mettre à jour le modèle d'email"
article_title: "POST: Mettre à jour les modèles d'e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails de la mise à jour du modèle de courriel Braze terminal."
---

{% api %}
# Mettre à jour les modèles d'e-mail existants
{% apimethod post %}
/fr/templates/email/update
{% endapimethod %}

Utilisez les API REST de modèle pour gérer programmatiquement les modèles d'e-mail que vous avez stockés sur le tableau de bord de Braze, sur la page Modèles & Médias. Braze fournit deux terminaux pour la création et la mise à jour de vos modèles de courriel.

Utilisez les points de terminaison ci-dessous pour mettre à jour les modèles d'e-mails sur le tableau de bord de Braze. Vous pouvez accéder à `email_template_id d'un modèle d'e-mail` en naviguant vers lui sur la page Modèles et Médias. Le point de terminaison API de création de modèles d'email retournera également une référence `email_template_id`.

Tous les champs autres que le `email_template_id` sont facultatifs, mais vous devez spécifier au moins un champ à mettre à jour.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "email_template_id": (requis, string) l'identifiant API de votre modèle de courriel,
  "template_name": (optionnel, chaîne) le nom de votre modèle de courriel,
  "subject": (optionnel, chaîne) le modèle de courriel ligne d'objet,
  "body": (optionnel, string) le corps du modèle d'email qui peut inclure HTML,
  "plaintext_body": (optionnel, string) une version en texte brut du corps du modèle d'email,
  "preheader": (optionnel, chaîne) le préen-tête d'email utilisé pour générer des aperçus dans certains clients,
  "tags" : (optionnel, tableau de chaînes) les balises doivent déjà exister,
  "should_inline_css": (optionnel, booléen) on attend un de 'true' ou 'false'
}
```

## Paramètres de la requête

| Paramètre                   | Requis    | Type de données      | Libellé                                                                                                                                                                                               |
| --------------------------- | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Identifiant de l'email`    | Requis    | Chaîne de caractères | Votre [identifiant API de votre modèle d'e-mail]({{site.baseurl}}/api/identifier_types/).                                                                                                             |
| `nom_gabarit`               | Optionnel | Chaîne de caractères | Nom de votre modèle de courriel.                                                                                                                                                                      |
| `Sujet`                     | Optionnel | Chaîne de caractères | Sujet du modèle d'e-mail.                                                                                                                                                                             |
| `Corps`                     | Optionnel | Chaîne de caractères | Corps du modèle d'e-mail qui peut inclure du HTML.                                                                                                                                                    |
| `texte brut`                | Optionnel | Chaîne de caractères | Une version en texte brut du corps du modèle de courriel.                                                                                                                                             |
| `preheader`                 | Optionnel | Chaîne de caractères | Pré-en-tête de courriel utilisé pour générer des aperçus dans certains clients.                                                                                                                       |
| `Tags`                      | Optionnel | Chaîne de caractères | [Les balises]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doivent déjà exister.                                                                                   |
| `devrait être en ligne css` | Optionnel | Boolean              | Active ou désactive la fonctionnalité `inline_css` par template. Si ce n'est pas fourni, Braze utilisera le paramètre par défaut pour le groupe d'applications. Un des `vrais` ou `faux` est attendu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de requête
```
curl --location --request POST 'https://rest.iad-01.braze. om/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Newsletter hebdomadaire",
  "objet": "Styles de cette semaine",
  "body": "Check out this week's digital lookbook to inspire your outfits. Jetez un coup d'oeil à https://www.braze.com/",
  "plaintext_body": "C'est le texte mis à jour dans mon corps de courriel et voici un lien vers https://www. raze.com/.",
  "preheader": "We want you to have the best look this Summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Erreurs possibles
- `Le nom du modèle est requis`

- `Les tags doivent être un tableau.`

- `Toutes les balises doivent être des chaînes.`

- `Certaines balises sont introuvables.`

- `"Valeur invalide pour 'should_inline_css'.  Un de 'true' ou 'false' était attendu"` - 'should_inline_css' n'accepte que les caractères booléens.  L'erreur est probablement affichée car la valeur est envoyée sous la forme d'une chaîne de caractères .


{% endapi %}
