---
nav_title: "POST: Suppression de l'utilisateur"
article_title: "POST: Suppression de l'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur la suppression des informations utilisateur Braze terminal."
---

{% api %}
# Utilisateur supprime le point de terminaison
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/users/delete
{% endapimethod %}


Ce point de terminaison vous permet de supprimer n'importe quel profil utilisateur en spécifiant un identifiant utilisateur connu. Jusqu'à 50 `external_ids`, `user_aliases`, ou `braze_ids` peuvent être inclus dans une seule requête. Un seul des `external_ids`, `user_aliases`, ou `braze_ids` peut être inclus dans une seule requête.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992 {% endapiref %}

{% alert warning %}
La suppression des profils d'utilisateur ne peut pas être annulée. Cela supprimera définitivement les utilisateurs qui peuvent causer des divergences dans vos données. En savoir plus sur ce qui se passe lorsque vous [supprimez un profil utilisateur via l'API]({{site.baseurl}}/help/help_articles/api/delete_user/) dans notre documentation d'aide.
{% endalert %}

## Limite de taux

{% include rate_limits.md endpoint='users delete' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (optionnel, table de chaîne) IDs externes à supprimer pour les utilisateurs,
  "user_aliases" : (optionnel, tableau des objets alias utilisateurs) Alias utilisateur pour que les utilisateurs puissent supprimer,
  "braze_ids" : (optionnel, tableau de chaîne) Braze les identifiants utilisateur pour que les utilisateurs suppriment
}
```
### Paramètres de la requête

| Paramètre           | Requis    | Type de données                           | Libellé                                                                                                             |
| ------------------- | --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `ID_externe`        | Optionnel | Tableau de chaînes                        | Identifiants externes à supprimer pour les utilisateurs.                                                            |
| `Alias utilisateur` | Optionnel | Tableau de l'objet alias de l'utilisateur | [Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) pour que les utilisateurs à supprimer. |
| `braze_ids`         | Optionnel | Tableau de chaînes                        | Braze les identifiants de l'utilisateur pour que les utilisateurs à supprimer.                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "user_aliases": ["user_alias1", "user_alias2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "deleted" : (required, integer) number of user ids queued for deletion
}
```
{% endapi %}


