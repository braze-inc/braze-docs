---
nav_title: "POST : Envoyez des e-mails transactionnels en utilisant la réception/distribution déclenchée par l'API."
article_title: "POST : Envoyez des e-mails transactionnels à l'aide de la réception/distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Braze Send transactional e-mail messages using API-triggered delivery (Envoyer des messages e-mail transactionnels en utilisant la réception/distribution déclenchée par l'API)."

---

{% api %}
# Envoyez des e-mails transactionnels en utilisant la réception/distribution déclenchée par l'API.
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages transactionnels immédiats et ponctuels à un utilisateur désigné.

Cet endpoint est utilisé parallèlement à la création d'une [campagne d'e-mails transactionnels de]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) Braze et de l'ID de campagne correspondant.

{% alert important %}
L’e-mail transactionnel est actuellement disponible dans certains forfaits Braze. Contactez votre gestionnaire du succès des clients Braze pour plus d’informations.
{% endalert %}

Similaire à l'[endpoint de campagne Send triggered]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), ce type de campagne vous permet d'héberger le contenu du message à l'intérieur du tableau de bord de Braze tout en dictant quand et à qui un message est envoyé via votre API. Contrairement au point de terminaison Send triggered campaign, qui accepte une audience ou un segment auquel envoyer des messages, une demande à ce point de terminaison doit spécifier un utilisateur unique par `external_user_id` ou `user_alias`, car ce type de campagne est créé pour l'envoi de messages 1:1 d'alertes telles que des confirmations de commande ou des réinitialisations de mot de passe.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `transactional.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `campaign_id` | Requis | Chaîne de caractères | ID de la campagne |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) see the following request parameters,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to the user in this request,
  "recipient": (required, object)
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User alias object) User alias of the user to receive message,
      "external_user_id": (optional, string) External identifier of user to receive message,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Facultatif | Chaîne de caractères |  Une chaîne de caractères compatible Base64. Validé par rapport aux expressions régulières suivantes :<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Ce champ facultatif vous permet de transmettre un identifiant interne pour cet envoi particulier, qui sera inclus dans les événements envoyés à partir du postback de l’événement HTTP transactionnel. Lorsqu’il est communiqué, cet identifiant est également utilisé comme clé de déduplication, que Braze conservera pendant 24 heures. <br><br>Le fait d’indiquer le même identifiant à une autre demande n’entraînera pas de nouvelle instance d’envoi par Braze pendant 24 heures.|
|`trigger_properties`|Facultatif|Objet|Voir les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Les paires clé-valeur de personnalisation qui s’appliquent à l’utilisateur de cette demande. |
|`recipient`|Requis|Objet| L’utilisateur que vous ciblez avec ce message. Peut contenir des `attributes` et un seul `external_user_id` ou `user_alias`.<br><br>Notez que si vous fournissez un ID utilisateur externe qui n’existe pas déjà dans Braze, la transmission d’un des champs à l’objet `attributes` aura pour effet de créer ce profil utilisateur dans Braze et d’envoyer ce message à l’utilisateur nouvellement créé. <br><br>Si vous envoyez plusieurs demandes au même utilisateur avec des données différentes dans l'objet `attributes`, les attributs `first_name`, `last_name` et `email` seront mis à jour de manière synchrone et intégrés dans votre message. Les attributs personnalisés n’ont pas cette même protection, procédez donc avec prudence lors de la mise à jour d’un utilisateur via cette API et de la transmission des différentes valeurs d’attributs personnalisés en succession rapide.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
```

## Réponse

L'endpoint d'envoi d'e-mail transactionnel répondra avec le message `dispatch_id` qui représente l'instance de cet envoi de message. Cet identifiant peut être utilisé avec les événements du postback de l’événement HTTP transactionnel pour tracer le statut d’un e-mail individuel envoyé à un utilisateur unique.

### Exemple de réponses

```json
{
    "dispatch_id": A randomly-generated unique ID of the instance of this send
    "status": Current status of the message
    "metadata" : Object containing additional information about the send instance
}
```

## Résolution des problèmes

L’endpoint peut renvoyer également, dans certains cas, un code d’erreur et un message lisible par un être humain, qui sont souvent des erreurs de validation. Voici quelques-unes des erreurs fréquentes pouvant être obtenues lorsque vous réalisez des requêtes invalides.

| Erreur | Résolution des problèmes |
| ----- | --------------- |
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | L’ID de campagne fourni n’est pas pour une campagne transactionnelle. |
| `The external reference has been queued.  Please retry to obtain send_id.` | L’external_send_id a été créé récemment, essayez un nouvel external_send_id si vous essayez d’envoyer un nouveau message. |
| `Campaign does not exist` | L’ID fourni pour la campagne ne correspond pas à une campagne existante. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | L’ID de campagne fourni correspond à une campagne archivée. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | L’ID de campagne fourni correspond à une campagne en pause. |
| `campaign_id must be a string of the campaign api identifier` | L’ID fourni pour la campagne n’est pas dans un format valide. |
| `Error authenticating credentials` | La clé API fournie est invalide |
| `Invalid whitelisted IPs `| L'adresse IP qui envoie la demande ne figure pas sur la liste blanche des adresses IP (si elle est utilisée). |
| `You do not have permission to access this resource` | La clé API n’a pas la permission d’effectuer cette action |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La plupart des endpoints Braze ont une implémentation de limites de débit qui renverra un code de réponse 429 si vous avez effectué trop de requêtes. L'endpoint d'envoi transactionnel fonctionne différemment : si vous dépassez la limite de débit qui vous a été attribuée, notre système continuera d'ingérer les appels API, de renvoyer les codes de réussite et d'envoyer les messages, mais ces derniers ne seront peut-être pas soumis à l'accord de niveau de service (SLA) contractuel pour la fonctionnalité. Veuillez nous contacter si vous désirez plus d’informations concernant cette fonctionnalité.

## Postback de l’événement HTTP transactionnel

{% multi_lang_include http_event_postback.md %}

{% endapi %}
