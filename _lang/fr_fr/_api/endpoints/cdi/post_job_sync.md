---
nav_title: "POST : Déclencheur de synchronisation"
article_title: "POST : Déclencher la synchronisation"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Déclencher la synchronisation."

---
{% api %}
# Déclencher une synchronisation
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Utilisez cet endpoint pour déclencher une synchronisation pour une intégration donnée.

{% alert note %}
Pour utiliser cet endpoint, il est nécessaire de générer une clé API avec `cdi.integration_sync`l'autorisation.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `integration_id` | Requis | Chaîne de caractères | ID d'intégration. Cette information est disponible dans l'URL lorsque vous consultez une intégration dans le tableau de bord de Braze. Le format de l'URL est `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

### Exemple de réponse réussie

Le code de statut `202` pourrait renvoyer le corps de réponse suivant :

```json
{
  "message": "success"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `400 Invalid integration ID` | Vérifiez que votre `integration_id` est valide. |
| `404 Integration not found` | Il n'existe pas d'intégration pour l'ID d'intégration donné. Assurez-vous que votre ID d'intégration est valide. |
| `429 Another job is in progress` | Une synchronisation est actuellement en cours pour cette intégration. Réessayez une fois la synchronisation terminée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour obtenir des codes d'état supplémentaires et les messages d'erreur associés, veuillez vous référer aux [&réponses aux erreurs fatales]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}