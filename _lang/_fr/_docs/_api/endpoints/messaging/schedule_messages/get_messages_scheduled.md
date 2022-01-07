---
nav_title: "GET: Lister les prochaines campagnes et toiles planifiées"
article_title: "GET: Lister les prochaines campagnes et toiles planifiées"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Get Scheduled Messages Braze."
---

{% api %}
# Obtenez des campagnes et des Canvases à venir
{% apimethod get %}
/fr/messages/scheduled_broadcasts
{% endapimethod %}

Vous pouvez afficher une liste JSON de campagnes à venir et planifiées et de Canvases en utilisant les informations et paramètres suivants. Le point de terminaison retournera des informations sur les campagnes planifiées et les Canvases d'entrée entre maintenant et le `end_time` désigné dans la requête. Chaque jour, les messages récurrents n'apparaîtront qu'une seule fois avec leur prochaine occurrence. Les résultats retournés dans ce point de terminaison ne sont que pour les campagnes et Canvases créés et planifiés en Brésil.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' category='message endpoints' %}

## Paramètres de la requête

| Paramètre      | Requis | Type de données                                                     | Libellé                                                                                                                                       |
| -------------- | ------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `heure de fin` | Requis | Chaîne au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Date de fin de la plage pour récupérer les prochaines campagnes programmées et Canvases. Ceci est traité comme minuit en heure UTC par l'API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "scheduled_broadcasts": [
      # Exemple de Canvas
      {
        "name" => String,
        "id" => chaîne,
        "type" => "Canvas",
        "tags" => [Noms de balises de chaîne],
        "next_send_time" => "AAAA-MM-JJ HH:mm:ss" (peut également inclure le fuseau horaire si pas local/intelligent de livraison)
        "schedule_type" => un de "local_time_zones", "Livraison intelligente", ou le nom du fuseau horaire de votre entreprise
      },
      # Exemple de Campagne
      {
        "name" => String,
        "id" => Chaîne,
        "type" => "Campagne",
        "tags" => [Noms de balises de chaîne],
        "next_send_time" => "AAAA-MM-JJ HH:mm:ss" (peut également inclure le fuseau horaire si pas local/intelligent delivery)
        "schedule_type" => un de "local_time_zones", "intelligent_delivery", ou le nom du fuseau horaire de votre entreprise
      },
    ]

```

{% endapi %}
