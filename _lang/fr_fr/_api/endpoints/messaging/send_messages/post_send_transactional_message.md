---
nav_title: "POST : Envoyer des e-mails transactionnels via une livraison déclenchée par API"
article_title: "POST : Envoyer des e-mails transactionnels via une livraison déclenchée par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Envoyer des e-mails transactionnels via une livraison déclenchée par API."

---

{% api %}
# Envoyer des e-mails transactionnels via une livraison déclenchée par API
{% apimethod post %}
/transactional/v1/campaigns/{campaign_id}/send
{% endapimethod %}

> Utilise ce point de terminaison pour envoyer des messages transactionnels immédiats et ponctuels à un utilisateur désigné. 

Cet endpoint est utilisé conjointement à la création d’une []({{site.baseurl}}/api/api_campaigns/transactional_campaigns)campagne par e-mail transactionnel et l’ID de campagne correspondant.

{% alert important %}
L’e-mail transactionnel est actuellement disponible dans certains forfaits Braze. Contactez votre gestionnaire du succès des clients Braze pour plus d’informations.
{% endalert %}

Comme pour l’[]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)endpoint Envoyer des campagnes déclenchées, ce type de campagne vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API. Contrairement au point de terminaison Send triggered campaign, qui accepte un public ou un segment auquel envoyer des messages, une demande à ce point de terminaison doit spécifier un utilisateur unique soit par `external_user_id` ou `user_alias`, car ce type de campagne est conçu pour l'envoi de messages 1:1 d'alertes telles que des confirmations de commande ou des réinitialisations de mot de passe.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `transactional.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Paramètres de chemin

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `campaign_id` | Obligatoire | Chaîne | ID de la campagne |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

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
|`external_send_id`| Facultatif | Chaîne | Une chaîne de caractères compatible Base64. Validé par rapport aux expressions régulières suivantes :<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Ce champ facultatif vous permet de transmettre un identifiant interne pour cet envoi particulier, qui sera inclus dans les événements envoyés à partir du postback de l’événement HTTP transactionnel. Lorsqu’il est communiqué, cet identifiant est également utilisé comme clé de déduplication, que Braze conservera pendant 24 heures. <br><br>Le fait d’indiquer le même identifiant à une autre demande n’entraînera pas de nouvelle instance d’envoi par Braze pendant 24 heures
|`trigger_properties`|Optionnel|Objet|Voir les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Les paires clé-valeur de personnalisation qui s’appliquent à l’utilisateur de cette demande.
|`recipient`|Obligatoire|Objet| L’utilisateur que vous ciblez avec ce message. Peut contenir des `attributes` et un seul `external_user_id` ou `user_alias`.<br><br>Notez que si vous fournissez un ID utilisateur externe qui n’existe pas déjà dans Braze, la transmission d’un des champs à l’objet `attributes` aura pour effet de créer ce profil utilisateur dans Braze et d’envoyer ce message à l’utilisateur nouvellement créé. <br><br>Si tu envoies plusieurs demandes au même utilisateur avec des données différentes dans l'objet `attributes`, les attributs `first_name`, `last_name` et `email` seront mis à jour de manière synchrone et intégrés dans ton message. Les attributs personnalisés n’ont pas cette même protection, procédez donc avec prudence lors de la mise à jour d’un utilisateur via cette API et de la transmission des différentes valeurs d’attributs personnalisés en succession rapide
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}\`

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

L’endpoint d’envoi d’e-mails transactionnels répond avec le `dispatch_id` du message qui représente l’instance de ce message envoyé. Cet identifiant peut être utilisé avec les événements du postback de l’événement HTTP transactionnel pour tracer le statut d’un e-mail individuel envoyé à un utilisateur unique.

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
| `The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint` | L'identifiant de campagne fourni n'est pas celui d'une campagne transactionnelle. |
| `The external reference has been queued.  Please retry to obtain send_id.` | L'identifiant d'envoi externe a été créé récemment, essayez un nouvel identifiant d'envoi externe si vous avez l'intention d'envoyer un nouveau message. |
| `Campaign does not exist` | L'identifiant de campagne fourni ne correspond pas à une campagne existante. |
| `The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.` | L'identifiant de campagne fourni correspond à une campagne archivée. |
| `The campaign is paused. Resume the campaign in order for trigger requests to take effect.` | L'identifiant de campagne fourni correspond à une campagne en pause. |
`campaign_id must be a string of the campaign api identifier` | L'identifiant de la campagne fourni n'est pas un format valide. |
| `Error authenticating credentials` | La clé API fournie n'est pas valide |
| `Invalid whitelisted IPs `| L'adresse IP qui envoie la requête ne figure pas dans la liste blanche des adresses IP (si elle est utilisée) |
| `You do not have permission to access this resource` | La clé API utilisée n'a pas la permission d'effectuer cette action |
{: .reset-td-br-1 .reset-td-br-2}

La plupart des endpoints Braze ont une implémentation de limites de débit qui renverra un code de réponse 429 si vous avez effectué trop de requêtes. L’endpoint d’envoi transactionnel fonctionne différemment. Si vous dépassez la limitation du débit allouée, notre système continuera à ingérer les appels API, retourner des codes de réussite et envoyer les messages. Cependant, ces messages peuvent ne pas être soumis au SLA contractuel pour cette fonctionnalité. Veuillez nous contacter si vous désirez plus d’informations concernant cette fonctionnalité.

## Postback de l’événement HTTP transactionnel

Tous les e-mails transactionnels sont complétés par des postbacks de statut d’événement envoyés en tant que requête HTTP à l’URL spécifiée. Cela vous permet d’évaluer le statut du message en temps réel et de prendre des mesures pour atteindre l’utilisateur sur un autre canal si le message n’est pas reçu ou recourir à un système interne si Braze connaît une certaine latence.

Pour associer les événements entrants à une instance d’envoi particulière, vous pouvez choisir de capturer et de stocker le `dispatch_id` Braze renvoyé dans la [](#example-response)réponse d’API`external_send_id`, ou de transmettre votre propre identifiant au champ . Un exemple de valeur que vous pouvez choisir de transmettre à ce champ peut être un ID de commande, où après avoir terminé la commande 1234, un message de confirmation de commande est envoyé à l’utilisateur par le biais de Braze, et l’`external_send_id : 1234` est inclus dans la demande. Tous les postbacks d’événements suivants, tels que `Sent` et `Delivered` comprennent `external_send_id : 1234` dans la charge utile vous permettant de confirmer que l’utilisateur a reçu correctement son e-mail de confirmation de commande.

Pour commencer à utiliser le retour d'événement HTTP transactionnel, navigue vers **Paramètres** > **Préférences de messagerie** dans ton tableau de bord Braze et repère la section **Retour d'état d'événement transactionnel**. Saisis l'URL que tu souhaites pour recevoir des messages de retour.

{% alert note %}
Si tu utilises l'[ancienne navigation]({{site.baseurl}}/navigation), cette page se trouve dans **Gérer les paramètres** > Paramètres **de messagerie**.
{% endalert %}

![\]({% image_buster /assets/img/transactional_webhook_url.png %})

### Corps de postback

```json
{
  "dispatch_id": (string, a randomly-generated unique ID of the instance of this send),
  "status": (string, Current status of message from the following message status table,
  "metadata" : (object, additional information relating to the execution of an event)
   {
     "external_send_id" : (string, If provided at the time of the request, Braze will pass your internal identifier for this send for all postbacks),
     "campaign_api_id" : (string, API identifier of this transactional campaign),
     "received_at": (ISO 8601 DateTime string, Timestamp of when the request was received by Braze, only included for events with "sent" status),
     "enqueued_at": (ISO 8601 DateTime string, Timestamp of when the request was enqueued by Braze, only included for events with "sent" status),
     "executed_at": (ISO 8601 DateTime string, Timestamp of when the request was processed by Braze, only included for events with "sent" status),
     "sent_at": (ISO 8601 DateTime string, Timestamp of when the request was sent to the ESP by Braze, only included for events with "sent" status),
     "processed_at" : (ISO 8601 DateTime string, Timestamp the event was processed by the ESP, only included for events with "processed" status),
     "delivered_at" : (ISO 8601 DateTime string, Timestamp the event was delivered to the user's inbox provider, only included for events with "processed" status),
     "bounced_at" : (ISO 8601 DateTime string, Timestamp the event was bounced by the user's inbox provider, only included for events with "bounced" status),
     "aborted_at" : (ISO 8601 DateTime string, Timestamp the event was Aborted by Braze, only included for events with "aborted" status),
     "reason" : (string, The reason Braze or the Inbox provider was unable to process this message to the user, only included for events with "aborted" or "bounced" status),
   }
}
```

#### Statut du message

| Statut | Description |
| ------------ | ----------- |
| `sent` | Message envoyé avec succès à un partenaire d'envoi de courriels de Braze.
| `processed` | Le partenaire d'envoi de l'email a reçu et préparé avec succès le message pour l'envoyer au fournisseur de la boîte de réception de l'utilisateur.
| `aborted` | Braze n’a pas réussi à envoyer le message, car l’adresse de l’utilisateur ne permet pas de recevoir des e-mails ou la logique d’interruption de Liquid a été appelée dans le corps du message. Tous les événements abandonnés comprennent un champ  dans l’objet de métadonnées indiquant pourquoi le message a été abandonné
|`delivered`| Le message a été accepté par le fournisseur d'accès à la boîte aux lettres électronique de l'utilisateur.
|`bounced`| Le message a été rejeté par le fournisseur de la boîte de réception de l'utilisateur. Tous les événements renvoyés comprennent un champ  dans l’objet de métadonnées reflétant le code d’erreur de rebond indiqué par le fournisseur de messagerie
{: .reset-td-br-1 .reset-td-br-2}

### Exemple de postback
\`\`\`json

// Événement envoyé
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "sent",
"metadata": {
"received_at": "2020-08-31T18:58:41.000+00:00",
"enqueued_at": "2020-08-31T18:58:41.000+00:00",
"executed_at": "2020-08-31T18:58:41.000+00:00",
"sent_at": "2020-08-31T18:58:42.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    

// Événement traité
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "processed",
"metadata": {
"processed_at": "2020-08-31T18:58:42.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    

// Interrompu
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "aborted",
"metadata": {
"reason": "User not emailable",
"aborted_at": "2020-08-31T19:04:51.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    

// Événement livré
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "delivered",
"metadata": {
"delivered_at": "2020-08-31T18:27:32.000+00:00",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    

// Événement rejeté
{
"dispatch_id": "acf471119f7449d579e8089032003ded",
"status": "bounced",
"metadata": {
"bounced_at": "2020-08-31T18:58:43.000+00:00",
"reason": "550 5.1.1 The email account that you tried to reach does not exist",
"campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
"external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
}
    

\`\`\`


{% endapi %}

