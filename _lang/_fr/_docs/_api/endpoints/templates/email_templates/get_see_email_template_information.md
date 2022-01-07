---
nav_title: "GET: Voir les informations du modèle d'e-mail"
article_title: "GET: Voir les informations du modèle d'e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de Braze du modèle de courriel."
---

{% api %}
# Voir les informations du modèle d'e-mail
{% apimethod get %}
/fr/templates/email/info
{% endapimethod %}

Utilisez pour obtenir des informations sur vos modèles de courriel.

Utilisez les API REST de modèle pour gérer programmatiquement les modèles d'e-mail que vous avez stockés sur le tableau de bord de Braze, sur la page Modèles & Médias. Braze fournit deux terminaux pour la création et la mise à jour de vos modèles de courriel.

{% alert important %}
Les modèles construits à l'aide de l'éditeur Drag & Drop ne sont pas acceptés
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre                | Requis | Type de données      | Libellé                                                                      |
| ------------------------ | ------ | -------------------- | ---------------------------------------------------------------------------- |
| `Identifiant de l'email` | Requis | Chaîne de caractères | See [email template API identifier]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Demander des composants
- [Identifiant du modèle]({{site.baseurl}}/api/identifier_types/)

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "email_template_id": (string) your email template API Identifier,
  "template_name": (chaîne) le nom de votre modèle de courriel,
  "description": (chaîne) description du modèle d'email,
  "objet": (chaîne) le sujet du modèle d'email,
  "preheader": (optionnel, chaîne) le préen-tête de courriel utilisé pour générer des aperçus dans certains clients),
  "body": (optionnel, chaîne) le corps du modèle d'e-mail qui peut inclure HTML,
  "plaintext_body": (optionnel, string) une version en texte brut du corps du modèle d'email,
  "should_inline_css": (optionnel, booléen) s'il y a des CSS en ligne dans le corps du modèle - valeur par défaut de la valeur css inlining pour le groupe d'applications,
  "tags": (string) noms de tags,
  "created_at": (string, in ISO 8601),
  "updated_at": (string, in ISO 8601)
}
```

Les images dans cette réponse apparaîtront dans la variable `body` en tant que HTML.

{% endapi %}
