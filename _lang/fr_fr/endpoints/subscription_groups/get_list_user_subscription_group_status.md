---
nav_title: "GET : Liste des statuts du groupe d'abonnement des utilisateurs"
article_title: "GET : Répertorier le statut du groupe d’abonnement de l’utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Répertorier le statut du groupe d’abonnement des utilisateurs."

---
{% api %}
# Répertorier le statut du groupe d’abonnement de l’utilisateur
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Utilisez cet endpoint pour obtenir le statut d’abonnement d’un utilisateur dans un groupe d’abonnement.

Ces groupes seront disponibles sur la page des **groupes d'abonnement**. La réponse de cet endpoint inclura l’ID externe et le statut abonné, désabonné, ou inconnu pour le groupe d’abonnement spécifique demandé dans l’appel d’API. Cette option permet de mettre à jour le statut du groupe d’abonnement dans les appels d’API ultérieurs ou de l’afficher sur une page Web hébergée.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour **WhatsApp Groups :**

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `subscription.status.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids)  | Requis | Chaîne de caractères | L’`id` de votre groupe d’abonnement. |
| `external_id`  |  Obligatoire* | Chaîne de caractères | L’`external_id` de l’utilisateur (maximum 50 `external_ids`, minimum 1). <br><br>Lorsqu’un `external_id` et un `email`/`phone` sont transmis, seuls le ou les `external_id`(s) fournis seront appliqués à la requête. |
| `email` | Obligatoire* | Chaîne de caractères | L’adresse e-mail de l’utilisateur. Il peut être transmis comme un tableau de chaînes de caractères avec un maximum de 50 éléments.<br><br> Envoyer une adresse e-mail et un numéro de téléphone en même temps (sans `external_id`) entraînera une erreur. |
| `phone` | Obligatoire* | Chaîne de caractères dans [E.164](https://en.wikipedia.org/wiki/E.164) format | Le numéro de téléphone de l’utilisateur. Si l’e-mail n’est pas inclus, vous devez ajouter au moins un numéro de téléphone (avec un maximum de 50).<br><br> Envoyer une adresse e-mail et un numéro de téléphone en même temps (sans `external_id`) entraînera une erreur. |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Chaque utilisateur doit disposer d'une des options suivantes : `external_id`, `email` ou `phone`.

- Pour les groupes d'abonnement aux SMS et à WhatsApp, un `external_id` ou un `phone` est nécessaire.  Lorsque les deux sont soumis, seul l’`external_id` est utilisé pour l'interrogation et le numéro de téléphone est appliqué à cet utilisateur.
- Pour les groupes d’abonnement aux e-mails, `external_id` ou `email` est nécessaire.  Lorsque les deux sont soumis, seul l’`external_id` est utilisé pour la requête et l’adresse e-mail est appliquée à cet utilisateur.

## Exemple de demande 

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS and WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab Email %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Réponse

Toutes les réponses réussies renverront `Subscribed`, `Unsubscribed`, ou `Unknown` selon le statut et l’historique de l’utilisateur avec le groupe d’abonnement.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% endapi %}
