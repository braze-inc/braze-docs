---
nav_title: "POST: Créer des ID d'envoi"
article_title: "POST: Créer des ID d'envoi"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Create Send IDs Braze."
---

{% api %}
# Créer des ID d'envoi pour le suivi des envois de messages
{% apimethod post %}
/fr/sends/id/create
{% endapimethod %}

L’identifiant d’envoi de Braze ajoute la possibilité d’envoyer des messages et de suivre les performances entièrement programmatiques, sans créer de campagne pour chaque envoi. Utiliser l'identifiant d'envoi pour suivre et envoyer des messages est utile si vous prévoyez de générer et d'envoyer du contenu par programme.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='sends id create' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (requis, chaîne) voir l'identifiant de la campagne,
  "send_id": (optionnel, chaîne) voir l'identifiant d'envoi
}
```

## Paramètres de la requête

| Paramètre       | Requis    | Type de données      | Libellé                                                                      |
| --------------- | --------- | -------------------- | ---------------------------------------------------------------------------- |
| `campaign_id`   | Requis    | Chaîne de caractères | Voir [l'identifiant de la campagne]({{site.baseurl}}/api/identifier_types/). |
| `id_expéditeur` | Optionnel | Chaîne de caractères | Voir [l'identifiant d'envoi]({{site.baseurl}}/api/identifier_types/).        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
"campaign_id": "campaign_identifier",
"send_id": "send_identifier"
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : "example_send_id"
}
```

{% endapi %}
