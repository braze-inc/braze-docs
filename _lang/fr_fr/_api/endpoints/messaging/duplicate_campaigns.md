---
nav_title: "POST : Dupliquer une campagne"
article_title: "POST : Dupliquer une campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Dupliquer des campagnes."

---
{% api %}
# Dupliquer des campagnes via l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Utilise ce point de terminaison pour dupliquer les campagnes. Ce point de terminaison de l'API est similaire à la [duplication des campagnes dans le tableau de bord de Braze][1].

{% alert important %}
La duplication d'une campagne via l'API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `campaigns.duplicate`.

## Limite de débit

Ce point d'accès est limité à 100 appels d’API par minute.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
| `Catalogues`campaign_id`                       | Créez et gérez des catalogues et des éléments de catalogue à référencer dans vos campagnes Braze.    |
|`name`| Obligatoire | Chaîne de caractères | Le nom de la campagne résultante. |
|`description`| Facultatif | Chaîne | Le champ de description de la campagne résultante. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Réponse

Cet endpoint renverra un code de statut `202` et la création de la campagne se fera de manière asynchrone. Tu peux utiliser le [téléchargement d'événements de sécurité][2] pour voir les enregistrements de la date à laquelle les campagnes ont été dupliquées et par quelle clé API.



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
