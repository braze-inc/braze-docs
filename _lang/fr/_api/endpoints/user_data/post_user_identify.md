---
nav_title: "POST : Identifier les utilisateurs"
article_title: "POST : Identifier les utilisateurs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Identifier les utilisateurs."

---
{% api %}
# Identifier les utilisateurs
{% apimethod post %}
/users/identify
{% endapimethod %}

Utilisez cet endpoint pour identifier un utilisateur non identifié (alias uniquement). 

Appeler `/users/identify` combine le profil alias uniquement avec le profil identifié, et supprime le profil alias uniquement. Pour éviter une perte inattendue de données lors de l’identification des utilisateurs, nous vous recommandons vivement de consulter d’abord les [bonnes pratiques en matière de collecte de données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) pour en savoir plus sur la capture des données utilisateur lorsque des informations utilisateur alias uniquement sont déjà présentes.

{% alert note %}
Vous pouvez ajouter jusqu’à 50 alias utilisateur par demande.
{% endalert %}

Identifier un utilisateur nécessite un `external_id` à inclure dans l’objet `aliases_to_identify`. Si aucun utilisateur ne porte cet `external_id`, l’`external_id` sera simplement ajouté au dossier de l’utilisateur alias, et l’utilisateur sera considéré comme identifié.

Vous pouvez associer plusieurs alias utilisateur supplémentaires à un seul `external_id`. Lorsque l’une de ces associations est effectuée, seuls les jetons de notification push et l’historique des messages associés à l’alias utilisateur sont conservés ; tous les attributs, événements ou achats seront « orphelins » et non disponibles sur l’utilisateur identifié. Une solution consiste à exporter les données de l’utilisateur alias avant l’identification en utilisant l’[endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), puis à réassocier les attributs, événements et achats à l’utilisateur identifié.

{% alert important %}
Les champs de demande et leurs valeurs sont sensibles à la casse. Utiliser différents cas pour référencer un `external_id` entraînera des profils dupliqués. Par exemple, « abc123 » et « ABC123 » sont deux `external_ids` différents.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects)
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Requis | Tableau d’alias pour identifier l’objet | Voir [alias pour identifier l’objet]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) et [objet Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
        "alias_name" : "example_alias",
        "alias_label" : "example_label"
      }
    }
  ]
}'
```

Pour plus d’informations sur `alias_name` et `alias_label`, consultez notre documentation sur les [alias utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).

{% endapi %}


