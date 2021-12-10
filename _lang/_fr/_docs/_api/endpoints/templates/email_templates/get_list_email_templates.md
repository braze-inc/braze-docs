---
nav_title: "GET: Liste des modèles d'e-mails disponibles"
article_title: "GET: Liste des modèles d'e-mails disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur la liste des modèles de courriel disponibles Braze terminpoint de terminaison de Braze."
---

{% api %}
# Liste des modèles d'e-mail disponibles
{% apimethod get %}
/fr/templates/email/list
{% endapimethod %}

Utilisez ce point de terminaison pour obtenir une liste de modèles disponibles dans votre compte Braze.

Utilisez les API REST de modèle pour gérer programmatiquement les modèles d'e-mail que vous avez stockés sur le tableau de bord de Braze, sur la page Modèles & Médias. Braze fournit deux terminaux pour la création et la mise à jour de vos modèles de courriel.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Paramètres de la requête

| Paramètre       | Requis    | Type de données                                                     | Libellé                                                                                                                     |
| --------------- | --------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `Modifié_après` | Optionnel | Chaîne au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les modèles mis à jour à ou après l'heure donnée.                                                      |
| `modifié_avant` | Optionnel | Chaîne au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les modèles mis à jour à ou avant l'heure donnée.                                                      |
| `limite`        | Optionnel | Nombre positif                                                      | Nombre maximum de modèles à récupérer. Valeur par défaut à 100 si non fournie, avec une valeur maximale acceptable de 1000. |
| `décalage`      | Optionnel | Nombre positif                                                      | Nombre de modèles à ignorer avant de retourner le reste des modèles qui correspondent aux critères de recherche.            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

{% alert important %}
Les modèles construits à l'aide de l'éditeur Drag & Drop ne sont pas fournis dans cette réponse.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "count": number of templates returned
  "templates": [template with the following properties] :
    "email_template_id": (string) your email template API Identifier,
    "template_name": (chaîne) le nom de votre modèle de courriel,
    "created_at": (chaîne, dans ISO 8601),
    "updated_at": (chaîne, dans ISO 8601),
    "tags" : (tableau de chaînes) balises ajoutées au modèle
}
```
{% endapi %}



