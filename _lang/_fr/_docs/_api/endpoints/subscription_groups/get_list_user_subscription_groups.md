---
nav_title: "GET: Liste des groupes d'abonnement de l'utilisateur"
article_title: "GET: Liste des groupes d'abonnement de l'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison d'abonnement de la Liste de l'utilisateur Groupes d'abonnement Braze."
---

{% api %}
# Obtenir les groupes d'abonnement des utilisateurs
{% apimethod get %}
/fr/subscription/user/status
{% endapimethod %}

Utilisez les points de terminaison ci-dessous pour lister et obtenir les groupes d'abonnement d'un certain utilisateur.

Si vous voulez voir des exemples ou tester ce point de terminaison pour les __Groupes d'abonnement par e-mail__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470 {% endapiref %}

Si vous voulez voir des exemples ou tester ce point de terminaison pour __SMS Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666 {% endapiref %}

## Paramètres de la requête

| Paramètre    | Requis       | Type de données                                               | Libellé                                                                                                                                                     |
| ------------ | ------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id externe` | Requis       | Chaîne de caractères                                          | Le `external_id` de l'utilisateur (doit inclure au moins un et au plus 50 `external_ids`).                                                                  |
| `Email`      | Obligatoire* | Chaîne de caractères                                          | L'adresse email de l'utilisateur, peut être passée sous la forme d'un tableau de chaînes. Doit inclure au moins une adresse e-mail (avec un maximum de 50). |
| `Téléphone`  | Obligatoire* | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur. Doit inclure au moins un numéro de téléphone (avec un maximum de 50).                                              |
| `limite`     | Optionnel    | Nombre entier                                                 | La limite sur le nombre maximum de résultats retournés. La valeur par défaut (et max) `limite` est 100.                                                     |
| `décalage`   | Optionnel    | Nombre entier                                                 | Nombre de modèles à ignorer avant de retourner le reste des modèles qui correspondent aux critères de recherche.                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert tip %}
S'il y a plusieurs utilisateurs (plusieurs identifiants externes) qui partagent la même adresse e-mail, tous les utilisateurs seront renvoyés en tant qu'utilisateur séparé (même s'ils ont la même adresse e-mail ou le même groupe d'abonnement).
{% endalert %}

## Exemple de demande

{% tabs %}
{% tab Multiple Users %}
{% raw %}
`https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&external_id[]=2`
{% endraw %}
{% endtab %}
{% tab SMS %}
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
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&email=example@braze.com&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}
{% endapi %}
