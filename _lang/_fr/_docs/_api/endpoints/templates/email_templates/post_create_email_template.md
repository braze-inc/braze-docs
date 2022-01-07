---
nav_title: "POST: Créer un modèle d'email"
article_title: "POST: Créer des Modèles d'E-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Créer des Modèles d'Email Braze."
---

{% api %}
# Créer un modèle d'e-mail
{% apimethod post %}
/fr/templates/email/create
{% endapimethod %}

Utilisez les API REST de modèle pour gérer programmatiquement les modèles d'e-mail que vous avez stockés sur le tableau de bord de Braze, sur la page Modèles & Médias. Braze fournit deux terminaux pour la création et la mise à jour de vos modèles de courriel.

Le statut d'abonnement par courriel des utilisateurs peut être mis à jour et récupéré via Braze en utilisant une API RESTful . Vous pouvez utiliser l'API pour configurer la synchronisation bidirectionnelle entre Braze et d'autres systèmes de messagerie ou votre propre base de données. Toutes les requêtes API sont effectuées via HTTPS.

Utilisez les points de terminaison ci-dessous pour créer des modèles d'e-mail sur le tableau de bord de Braze. Ces modèles seront disponibles sur la page Modèles et Médias. La réponse de ce point de terminaison inclura un champ pour `email_template_id`, qui peut être utilisé pour mettre à jour le modèle dans les appels suivants de l'API.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "template_name": (obligatoire, chaîne) le nom de votre modèle de courriel,
   "objet": (obligatoire, chaîne) le sujet du modèle d'e-mail,
   "corps": (obligatoire, chaîne) le corps du modèle d'email qui peut inclure HTML,
   "plaintext_body": (optionnel, string) une version en texte brut du corps du modèle d'email,
   "preheader": (optionnel, chaîne) le préen-tête d'email utilisé pour générer des aperçus dans certains clients,
   "tags": (optionnel, Tableau de Strings) Les balises doivent déjà exister,
   "should_inline_css" : (optionnel, booléen) On attend un de 'true' ou 'false'
}
```

## Paramètres de la requête

| Paramètre                   | Requis    | Type de données      | Libellé                                                                                                                                                                                               |
| --------------------------- | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nom_gabarit`               | Requis    | Chaîne de caractères | Nom de votre modèle de courriel.                                                                                                                                                                      |
| `Sujet`                     | Requis    | Chaîne de caractères | Sujet du modèle d'e-mail.                                                                                                                                                                             |
| `Corps`                     | Requis    | Chaîne de caractères | Corps du modèle d'e-mail qui peut inclure du HTML.                                                                                                                                                    |
| `texte brut`                | Optionnel | Chaîne de caractères | Une version en texte brut du corps du modèle de courriel.                                                                                                                                             |
| `preheader`                 | Optionnel | Chaîne de caractères | Pré-en-tête de courriel utilisé pour générer des aperçus dans certains clients.                                                                                                                       |
| `Tags`                      | Optionnel | Chaîne de caractères | [Les balises]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doivent déjà exister.                                                                                   |
| `devrait être en ligne css` | Optionnel | Boolean              | Active ou désactive la fonctionnalité `inline_css` par template. Si ce n'est pas fourni, Braze utilisera le paramètre par défaut pour le groupe d'applications. Un des `vrais` ou `faux` est attendu. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "objet": "Bienvenue dans mon modèle d'e-mail! ,
  "body": "This is the text within my email body and https://www. raze.com/ Voici un lien vers Braze.com. ,
  "plaintext_body": "C'est le texte dans mon corps de courriel et voici un lien vers https://www. raze.com/.",
  "preheader": "Mon préen-tête est assez cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Erreurs possibles
- `Le nom du modèle est requis`

- `Les tags doivent être un tableau.`

- `Toutes les balises doivent être des chaînes.`

- `Certaines balises n'ont pas pu être trouvées.` - Une balise a été spécifiée qui n'existe pas dans cet environnement.

- `L'e-mail doit avoir des noms de bloc de contenu valides.` - L'e-mail contient des blocs de contenu qui n'existent pas dans cet environnement.

- `"Valeur invalide pour 'should_inline_css'.  Un de 'true' ou 'false' était attendu"` - 'should_inline_css' n'accepte que les caractères booléens.  L'erreur est probablement affichée car la valeur est envoyée sous la forme d'une chaîne de caractères .

{% endapi %}
