---
nav_title: "GET : Répertorier les groupes d’abonnement de l’utilisateur"
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

> Utilisez cet endpoint pour répertorier et obtenir les groupes d’abonnement d’un utilisateur donné.

Si tu veux voir des exemples ou tester ce point de terminaison pour les **groupes d'abonnement par courriel**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si tu veux voir des exemples ou tester ce point de terminaison pour les **groupes d'abonnement SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

Si tu veux voir des exemples ou tester ce point de terminaison pour les **groupes WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Pré-requis

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `subscription.groups.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `external_id` | Obligatoire | Chaîne | Le `external_id` de l'utilisateur (doit inclure au moins un et au plus 50 `external_ids`). |
| `email`  |  Obligatoire* | Chaîne de caractères | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50).
| `phone` | Obligatoire* | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur. Doit inclure au moins un numéro de téléphone (maximum 50).
| `limit` | Optional | Integer | La limite du nombre maximum de résultats renvoyés. La valeur par défaut (et maximale) de `limit` est de 100. |
| `offset`  |  Facultatif | Entier | Nombre de modèles à ignorer avant de renvoyer le reste des modèles qui correspondent aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
{% endapi %}
