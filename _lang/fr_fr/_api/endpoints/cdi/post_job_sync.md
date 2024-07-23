---
nav_title: "POST : Synchronisation du déclencheur"
article_title: "POST : Synchronisation du déclencheur"
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

> Utilise ce point de terminaison pour déclencher une synchronisation pour une intégration donnée.

{% alert note %}
Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `cdi.integration_sync`.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `integration_id` | Obligatoire | Chaîne | ID d'intégration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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
| `400 Invalid integration ID` | Vérifie que ton `integration_id` est valide. |
| `404 Integration not found` | Il n'existe pas d'intégration pour l'ID d'intégration donné. Assure-toi que ton identifiant d'intégration est valide. |
| `429 Another job is in progress` | Une synchronisation est actuellement en cours pour cette intégration. Essaie à nouveau une fois la synchronisation terminée. |
{: .reset-td-br-1 .reset-td-br-2}

Pour les codes d'état supplémentaires et les messages d'erreur associés, tu peux te référer à [Erreurs fatales et réponses]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}
