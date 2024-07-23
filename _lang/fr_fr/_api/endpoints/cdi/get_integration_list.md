---
nav_title: "GET : Intégrations de listes"
article_title: "GET : Intégrations de listes"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Lister des intégrations."

---
{% api %}
# Intégration de listes
{% apimethod get %}
/cdi/integrations
{% endapimethod %}

> Utilisez ce point de terminaison pour renvoyer une liste des intégrations existantes.


{% alert note %}
Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `cdi.integration_list`.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Paramètres de recherche

Chaque appel à ce point de terminaison renvoie 10 éléments. Pour une liste avec plus de 10 intégrations, utilisez l’en-tête `Link` pour récupérer les données de la page suivante, comme indiqué dans l’exemple de réponse.

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `cursor` | Facultatif | Chaîne | Détermine la pagination de la liste d’intégration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

### Sans curseur

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Avec curseur

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

### Exemple de réponse réussie

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

{% alert note %}
L’en-tête `Link` n’existera pas s’il y a, au total, 10 intégrations ou moins. Pour les appels sans curseur, `prev` ne s’affichera pas. Lors de la consultation de la dernière page de produits, `next` ne s’affichera pas.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Dépannage |
| --- | --- |
| `400 Invalid cursor` | Vérifiez que votre `cursor` est valide. |
{: .reset-td-br-1 .reset-td-br-2}

Pour obtenir des codes d’état supplémentaires et les messages d’erreur associés, reportez-vous à [la section Erreurs et réponses fatales]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
