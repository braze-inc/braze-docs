---
nav_title: "GET : Liste des groupes subscription groups d'utilisateurs"
article_title: "GET : Répertorier les groupes d’abonnement de l’utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Répertorier les groupes d’abonnement de l’utilisateur."

---
{% api %}
# Répertorier les groupes d’abonnement de l’utilisateur
{% apimethod get %}
/subscription/user/status
{% endapimethod %}

> Utilisez cet endpoint pour répertorier et obtenir les groupes d'abonnement avec l'historique d'un certain utilisateur.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour **WhatsApp Groups :**

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `subscription.groups.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `external_id`  | Requis | Chaîne de caractères | L’`external_id` de l’utilisateur (maximum 50 `external_ids`, minimum 1). |
| `email`  |  Obligatoire* | Chaîne de caractères | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). |
| `phone` | Obligatoire* | Chaîne de caractères dans [E.164](https://en.wikipedia.org/wiki/E.164) format | Le numéro de téléphone de l’utilisateur. Doit inclure au moins un numéro de téléphone (maximum 50). |
| `limit` | Facultatif | Entier | La limite du nombre maximum de résultats renvoyés. La `limit` par défaut (et au maximum) est de 100. |
| `offset`  |  Facultatif | Entier | Nombre de modèles à ignorer avant de renvoyer le reste des modèles qui correspondent aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
S’il existe plusieurs utilisateurs (plusieurs `external_ids`) qui partagent la même adresse e-mail, tous les utilisateurs seront renvoyés en tant qu’utilisateurs distincts (même s’ils ont la même adresse e-mail ou le même groupe d’abonnement).
{% endalert %}

## Exemple de demande 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&limit=100&offset=1&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Exemple de réponse

Seuls les groupes d'abonnement dont le statut d'abonnement a été mis à jour dans l'historique de l'utilisateur seront inclus dans une réponse positive. Cela signifie que les groupes d'abonnement nouvellement créés ne seront pas répertoriés.

```json
{
  "success": true,
  "subscription_groups": [
    {
      "subscription_group_id": "group_id_1",
      "subscription_status": "subscribed"
    },
    {
      "subscription_group_id": "group_id_2",
      "subscription_status": "unsubscribed"
    }
  ]
}
```

{% endapi %}
