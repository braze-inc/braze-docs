---
nav_title: "GET: Liste des statuts du groupe d'abonnement des utilisateurs"
article_title: "GET: Liste du statut du groupe d'abonnement de l'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de la liste des utilisateurs du statut de groupe d'abonnement Braze."
---

{% api %}
# Obtenir le statut du groupe d'abonnement des utilisateurs
{% apimethod get %}
/fr/subscription/status/get
{% endapimethod %}

Utilisez les points de terminaison ci-dessous pour obtenir l'état d'abonnement d'un utilisateur dans un groupe d'abonnement. Ces groupes seront disponibles sur la page __Groupe d'abonnement__. La réponse de ce point de terminaison inclura l'ID externe et soit souscrit, désabonné, ou inconnu pour le groupe d'abonnement spécifique demandé dans l'appel API. Ceci peut être utilisé pour mettre à jour l'état du groupe d'abonnement lors d'appels API subséquents ou pour être affiché sur une page web hébergée.

Si vous voulez voir des exemples ou tester ce point de terminaison pour les __Groupes d'abonnement par e-mail__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Si vous voulez voir des exemples ou tester ce point de terminaison pour __SMS Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Paramètres de la requête

| Paramètre                   | Requis       | Type de données                                               | Libellé                                                                                                                                                                                                                                                                               |
| --------------------------- | ------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ID de groupe d'abonnement` | Requis       | Chaîne de caractères                                          | L'id `` de votre groupe d'abonnement.                                                                                                                                                                                                                                                 |
| `id externe`                | Obligatoire* | Chaîne de caractères                                          | Le `external_id` de l'utilisateur (doit inclure au moins un et au plus 50 `external_ids`). <br><br>Quand un `external_id` et `email`/`téléphone` sont soumis, seul le `external_id`(s) fourni sera appliqué à la requête de résultat.                                     |
| `Email`                     | Obligatoire* | Chaîne de caractères                                          | L'adresse e-mail de l'utilisateur. Il peut être passé sous la forme d'un tableau de chaînes avec un maximum de 50. La soumission d'une adresse e-mail et d'un numéro de téléphone (sans `external_id`) entraînera une erreur.                                                         |
| `Téléphone`                 | Obligatoire* | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur. Si l'email n'est pas inclus, vous devez inclure au moins un numéro de téléphone (avec un maximum de 50). <br><br> Soumettre à la fois une adresse e-mail et un numéro de téléphone (sans `external_id`) résultera en une erreur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

*Un des `external_id` ou `email` ou `téléphone` est requis pour chaque utilisateur.

- Pour les groupes d'abonnement SMS, `external_id` ou `téléphone` est requis.  Lorsque les deux sont soumises, seul le `external_id` est utilisé pour les requêtes et le numéro de téléphone est appliqué à cet utilisateur.
- Pour les groupes d'abonnement aux e-mails, `external_id` ou `email` est requis.  Lorsque les deux sont soumises, seul le `external_id` est utilisé pour la requête et l'adresse e-mail est appliquée à cet utilisateur.

## Exemple de demande

{% tabs %}
{% tab Multiple Users %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab SMS %}
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

Toutes les réponses réussies retourneront `souscrites`, `désabonné`, ou `inconnu` selon le statut et l'historique de l'utilisateur avec le groupe d'abonnement.

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
