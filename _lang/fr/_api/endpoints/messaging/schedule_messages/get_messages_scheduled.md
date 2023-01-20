---
nav_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
article_title: "GET : Répertorier les campagnes et Canvas planifiés à venir"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Braze Obtenir les messages planifiés."

---
{% api %}
# Obtenir les campagnes et les Canvas planifiés à venir
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

Utilisez cet endpoint pour renvoyer une liste JSON des informations sur les campagnes planifiées et les Canvas saisis entre maintenant et un `end_time` spécifié dans la demande. Les messages quotidiens et récurrents n’apparaîtront qu’une seule fois lors de leur occurrence suivante. Les résultats renvoyés dans cet endpoint ne concernent que les campagnes et Canvas créés et planifiés dans Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `end_time` | Requis | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Date de fin de la plage pour récupérer les campagnes et Canvas planifiés. Ce traitement est effectué à minuit (UTC) par l’API. |
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
    {
      "name" (string) le nom de la diffusion planifiée,
      "id" (stings) the Canvas or campaign identifier,
      "type" (string) le type de diffusion, soit un Canvas, soit une campagne,
      "tags" (array) un tableau de noms de balises formatés en tant que chaînes de caractères,
      "next_send_time" (string) La prochaine date d’envoi formatée en ISO 8601 qui peut aussi comprendre le fuseau horaire si la livraison n’est pas régionale ou intelligente.,
      "schedule_type" (string) Le type de planification, local_time_zones, intelligent_delivery ou le nom du fuseau horaire de votre entreprise.,
    },
  ]
}
```

{% endapi %}
