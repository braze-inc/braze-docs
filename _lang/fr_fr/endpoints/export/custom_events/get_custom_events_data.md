---
nav_title: "GET : Exporter des événements personnalisés"
article_title: "GET : Exportation d'événements personnalisés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Exportation d'événements personnalisés Braze."

---
{% api %}
# Exporter des événements personnalisés
{% apimethod get %}
/événements
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste d'événements personnalisés enregistrés pour votre appli. Les événements sont renvoyés par groupes de 50, triés par ordre alphabétique.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `events.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='events' %}

## Paramètres de recherche

Notez que chaque appel à cet endpoint renverra 50 événements. Pour plus de 50 événements, utilisez l'en-tête `Link` pour récupérer les données sur la page suivante, comme le montre l'exemple de réponse suivant.

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `cursor` | Facultatif | Chaîne de caractères | Détermine la pagination des événements personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de requêtes

### Sans curseur

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Avec curseur

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Codes de réponse des erreurs fatales {#fatal-export}

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre requête rencontre une erreur fatale, reportez-vous à la section [Erreurs fatales.]({{site.baseurl}}/api/errors/#fatal-errors)

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
