---
nav_title: "POST : Renommer des ID externes"
article_title: "POST : Renommer l'ID externe"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Renommer des ID externes."

---
{% api %}
# Renommer des ID externes
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Utilisez cet endpoint pour renommer les ID externes de vos utilisateurs. 

Vous pouvez envoyer jusqu’à 50 objets renommés par demande. 

Cet endpoint définit un nouvel `external_id` (principal) pour l’utilisateur et rend son `external_id` existant obsolète. Cela signifie que l’utilisateur peut être identifié par l’un ou l’autre des `external_id` jusqu’à ce que celui qui est obsolète soit supprimé. La présence de plusieurs ID externes permet de prévoir une période de migration pour que les versions antérieures de vos applications qui utilisent l’ancien schéma de nommage des ID externes ne s’interrompent pas. 

Une fois que votre ancien schéma de nommage n'est plus utilisé, nous vous recommandons vivement de supprimer les ID externes obsolètes à l'aide de l'[endpoint`/users/external_ids/remove`.]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)

{% alert warning %}
Assurez-vous de supprimer les ID externes obsolètes à l’aide de l’endpoint `/users/external_ids/remove` plutôt que `/users/delete`. L’envoi d’une demande à `/users/delete` avec l’ID externe obsolète supprime entièrement le profil utilisateur et ne peut pas être annulé.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.external_ids.rename`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Requis | Tableau des objets Renommer des identifiants externes | Afficher l’exemple de demande et les limitations suivantes pour la structure de l’objet Renommer des identifiants externes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez ce qui suit :

- L'adresse `current_external_id` doit être l'ID principal de l'utilisateur et ne peut pas être un ID obsolète.
- Le site `new_external_id` ne doit pas être déjà utilisé en tant qu'ID primaire ou ID déprécié.
- Les sites `current_external_id` et `new_external_id` ne peuvent pas être les mêmes.

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Réponse

La réponse confirmera tous les renommages réussis et les renommages infructueux avec toutes les erreurs associées. Les messages d’erreur dans le champ `rename_errors` référenceront l’index de l’objet dans le tableau de la demande d’origine.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

Le champ `message` renverra `success` pour toutes les demandes valides. Des erreurs plus spécifiques sont saisies dans le tableau `rename_errors`. Le champ `message` renvoie une erreur dans les cas suivants :

- Clé API non valide
- Tableau `external_id_renames` vide
- Tableau `external_id_renames` avec plus de 50 objets
- Limite de débit atteinte (plus de 1 000 demandes par minute)

## Foire aux questions

### Cela a-t-il un impact sur le MAU ?
Non, puisque le nombre d’utilisateurs restera le même, ils auront simplement un nouvel `external_id`.

### Le comportement des utilisateurs change-t-il au cours du temps ?
Non, étant donné que l’utilisateur est toujours le même et que tous ses comportements historiques sont toujours liés à lui.

### Peut-il être exécuté sur des espaces de travail de développement ou de mise à l'essai ?
Oui. En fait, nous vous recommandons vivement d'effectuer un test de migration sur un espace de travail de développement ou de mise à disposition, et de vous assurer que tout s'est bien déroulé avant d'exécuter la migration sur les données de production.

### Ce système enregistre-t-il des points de données ?
Cette fonctionnalité ne permet pas d'enregistrer des points de données.

### Quel est le délai d’obsolescence recommandé ?
Nous n'avons pas de limite stricte quant à la durée pendant laquelle vous pouvez conserver des ID externes dépréciés, mais nous vous recommandons vivement de les supprimer lorsqu'il n'est plus nécessaire de référencer les utilisateurs par l'ID déprécié.

{% endapi %}
