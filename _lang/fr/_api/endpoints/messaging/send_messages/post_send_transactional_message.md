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
# Envoi d’e-mails transactionnels via une livraison déclenchée par API
{% apimethod post %}
/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
{% endapimethod %}

Utilisez cet endpoint pour envoyer des messages transactionnels instantanés et ad hoc aux utilisateurs désignés. Cet endpoint est utilisé conjointement à la création d’une [campagne par e-mail transactionnel]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) et l’ID de campagne correspondant.

{% alert important %}
L’e-mail transactionnel est actuellement disponible dans certains forfaits Braze. Contactez votre gestionnaire du succès des clients Braze pour plus d’informations.
{% endalert %}

Comme pour l’[endpoint Envoyer des campagnes déclenchées]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), ce type de campagne vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API. Contrairement à l’endpoint Envoyer des campagnes déclenchées qui accepte une audience à laquelle ou un segment auquel envoyer des messages, une demande à cet endpoint doit spécifier un seul utilisateur à l’aide du `external_user_id` ou du `user_alias`, car ce type de campagne est conçu spécialement pour la messagerie 1:1 des alertes telles que les confirmations de commandes ou les réinitialisations de mot de passe.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='transactional email' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optional, string) voir les paramètres de requête suivants,
  "trigger_properties": (optional, object) les paires clé-valeur de personnalisation qui s’appliquent à l’utilisateur de cette demande,
  "recipient": (required, object)
    {
      // Soit « external_user_id » soit « user_alias » est nécessaire. Les demandes ne doivent en spécifier qu’un seul des deux.
      "user_alias": (optional, User Alias Object) l’alias utilisateur de l’utilisateur devant recevoir le message,
      "external_user_id": (optional, string) Identifiant externe de l’utilisateur pour recevoir le message,
      "attributes": (optional, object) les champs dans l’objet des attributs vont créer ou mettre à jour un attribut de ce nom avec la valeur fournie dans le profil utilisateur spécifié avant que le message ne soit envoyé et les valeurs existantes seront écrasées
    }
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`external_send_id`| Facultatif | String |  Une chaîne de caractères compatible Base64. Validé par rapport aux expressions régulières suivantes :<br><br> `/^[a-zA-Z0-9-_+\/=]+$/` <br><br>Ce champ facultatif vous permet de transmettre un identifiant interne pour cet envoi particulier, qui sera inclus dans les événements envoyés à partir du postback de l’événement HTTP transactionnel. Lorsqu’il est communiqué, cet identifiant est également utilisé comme clé de déduplication, que Braze conservera pendant 24 heures. <br><br>Le fait d’indiquer le même identifiant à une autre demande n’entraînera pas de nouvelle instance d’envoi par Braze pendant 24 heures.|
|`trigger_properties`|Optional|Objet|Voir les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Les paires clé-valeur de personnalisation qui s’appliquent à l’utilisateur de cette demande. |
|`recipient`|Required|Objet| L’utilisateur que vous ciblez avec ce message. Peut contenir des `attributs` et un seul `external_user_id` ou `user_alias`.<br><br>Notez que si vous fournissez un ID utilisateur externe qui n’existe pas déjà dans Braze, la transmission d’un des champs à l’objet `attributs` aura pour effet de créer ce profil utilisateur dans Braze et d’envoyer ce message à l’utilisateur nouvellement créé. <br><br>Si vous envoyez plusieurs demandes au même utilisateur avec des données différentes dans l’objet `attributs`, Braze s’assurera que les `first_name`, `last_name` et `e-mail` soient mis à jour de manière synchronisée et modélisés dans votre message. Les attributs personnalisés n’ont pas cette même protection, procédez donc avec prudence lors de la mise à jour d’un utilisateur via cette API et de la transmission des différentes valeurs d’attributs personnalisés en succession rapide.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
        "recipient": [
          {
            "external_user_id": TARGETED_USER_ID_STRING
          }
        ]
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
```

## Réponse 

L’endpoint d’envoi d’e-mails transactionnels répond avec le `dispatch_id` du message qui représente l’instance de ce message envoyé. Cet identifiant peut être utilisé avec les événements du postback de l’événement HTTP transactionnel pour tracer le statut d’un e-mail individuel envoyé à un utilisateur unique.

### Exemple de réponses

```json
{
    "dispatch_id": ID unique généré aléatoirement de l’instance de cet envoi 
    "status": Statut actuel du message
    "metadata" : Objet contenant des informations supplémentaires sur l’instance envoyée
}
```

L’endpoint peut renvoyer également, dans certains cas, un code d'erreur et un message lisible par un être humain, qui sont souvent des erreurs de validation. Voici quelques unes des erreurs fréquentes pouvant être obtenues lorsque vous réalisez des requêtes invalides.

| Code d’erreur | Exemple de message d’erreur | Raison |
| ---------- | ----------------------| ----- |
| 400 | La campagne n’est pas une campagne transactionnelle. Cet endpoint ne peut être utilisé que par les campagnes transactionnelles | L’ID de campagne fourni n’est pas pour une campagne transactionnelle. |
| 400 | La référence externe a été mise en attente.  Veuillez réessayer pour obtenir le send_id. | Le external_send_id a été créé récemment, essayez un nouveau external_send_id si vous essayez d’envoyer un nouveau message. |
| 400 | La campagne n’existe pas | L’ID fourni pour la campagne ne correspond pas à une campagne existante. |
| 400 | La campagne est archivée. Sortez la campagne des archives pour vous assurer que les requêtes déclenchées prennent effet. | L’ID de campagne fourni correspond à une campagne archivée. |
| 400 | La campagne est en pause. Relancez la campagne pour vous assurer que les requêtes déclenchées prennent effet. | L’ID de campagne fourni correspond à une campagne en pause. |
| 400 | campaign_id doit être une chaîne de caractères de l’identifiant API de la campagne | L’ID fourni pour la campagne n’est pas dans un format valide. |
| 401 | Erreur d’authentification des identifiants | La clé API fournie est invalide | 
| 403 | IP en liste blanche invalides | L’adresse IP qui envoie la requête n’est pas dans la liste blanche des IP (si elle est utilisée) | 
| 403 | Vous n’avez pas la permission d’accéder à cette ressource | La clé API n’a pas la permission d’effectuer cette action |

La plupart des endpoints de Braze ont une implémentation de limites de débit qui renverra un code de réponse 429 si vous avez effectué trop de requêtes. L’endpoint d’envoi transactionnel fonctionne différemment. Si vous dépassez la limitation du débit allouée, notre système continuera à ingérer les appels API, retourner des codes de réussite et envoyer les messages. Cependant, ces messages peuvent ne pas être soumis au SLA contractuel pour cette fonctionnalité. Veuillez nous contacter si vous désirez plus d’informations concernant cette fonctionnalité.

 ### Postback de l’événement HTTP transactionnel

Tous les e-mails transactionnels sont complétés par des postbacks de statut d’événement envoyés en tant que requête HTTP à l’URL spécifiée. Cela vous permet d’évaluer le statut du message en temps réel et de prendre des mesures pour atteindre l’utilisateur sur un autre canal si le message n’est pas livré ou revenir sur un système interne si Braze connaît une certaine latence.

Pour associer les événements entrants à une instance d’envoi particulière, vous pouvez choisir de capturer et de stocker le `dispatch_id` Braze renvoyé dans la [réponse d’API](#example-response), ou de transmettre votre propre identifiant au champ `external_send_id`. Un exemple de valeur que vous pouvez choisir de transmettre à ce champ peut être un ID de commande, où après avoir terminé la commande 1234, un message de confirmation de commande est envoyé à l’utilisateur par le biais de Braze, et `external_send_id : 1234` est inclus dans la demande. Tous les événements suivants, tels que `Sent` (envoyé) et `Delivered` (livré) comprennent `external_send_id : 1234` dans la charge utile vous permettant de confirmer que l’utilisateur a reçu correctement son e-mail de confirmation de commande.

Pour commencer à utiliser le postback de l’événement HTTP transactionnel, accédez à **Manage Settings (Gérer les paramètres)** > **Email Settings (Paramètres des e-mails)** > **Transactional Webpush URL (URL Webpush transactionnelle)** dans votre tableau de bord de Braze et saisissez l’URL sur laquelle vous souhaitez recevoir les postbacks.

![]({% image_buster /assets/img/transactional_webhook_url.png %})


### Corps de postback

```json
{
  "dispatch_id": (string, ID unique généré aléatoirement de l’instance de cet envoi),
  "status": (string, statut actuel du message à partir de la table de statut de message suivante,
  "metadata" : (objet, information additionnelle relative à l’exécution d’un événement)
   {
     "external_send_id" : (string, si fourni lors de la requête, Braze transmettra votre identifiant interne pour cet envoi pour tous les postbacks),
     "campaign_api_id" : (string, identifiant API pour cette campagne transactionnelle),
     "received_at": (ISO 8601 DateTime string, horodatage du moment où la requête a été reçue par Braze, inclus uniquement pour les événements ayant le statut « sent » (envoyé)),
     "enqueued_at": (ISO 8601 DateTime string, horodatage du moment où la requête a été mise en file d’attente par Braze, inclus uniquement pour les événements ayant le statut « sent » (envoyé)),
     "executed_at": ISO 8601 DateTime string, horodatage du moment où la requête a été traitée par Braze, inclus uniquement pour les événements ayant le statut « sent » (envoyé)),
     "sent_at": (ISO 8601 DateTime string, horodatage du moment où la requête a été envoyée au fournisseur de services d’e-mail par Braze, inclus uniquement pour les événements ayant le statut « sent » (envoyé)),
     "processed_at" : (ISO 8601 DateTime string, horodatage du moment où l’événement a été traité par le fournisseur de services d’e-mail, inclus uniquement pour les événements ayant le statut « processed » (traité)),
     "delivered_at" : (ISO 8601 DateTime string, horodatage du moment où l’événement a été livré au fournisseur de la boîte de réception de l’utilisateur, inclus uniquement pour les événements ayant le statut « processed » (traité)),
     "bounced_at" : (ISO 8601 DateTime string, horodatage du moment où l’événement a été retourné par le fournisseur de la boîte de réception de l’utilisateur, inclus uniquement pour les événements ayant le statut « bounced » (rejeté)),
     "aborted_at" : (ISO 8601 DateTime string, horodatage du moment où l’événement a été annulé par Braze, inclus uniquement pour les événements ayant le statut « aborted » (interrompu)),
     "reason" : (string, la raison pour laquelle Braze ou le fournisseur de boîte de réception n’a pas pu traiter ce message pour l’utilisateur, uniquement inclus pour les événements avec le statut « aborted » (interrompu) ou « bounced » (rejeté)),
   }
}
```

#### Statut du message

|  Statut | Description |
| ------------ | ----------- |
| `sent` (envoyé) | Message envoyé avec succès au partenaire d’envoi d’e-mail de Braze  |
| `processed` (traité) | Le partenaire d’envoi d’e-mail a reçu et préparé avec succès le message pour l’envoyer au fournisseur de messagerie de l’utilisateur |
| `aborted` (interrompu) | Braze n’a pas réussi à envoyer le message car l’adresse de l’utilisateur ne permet pas de recevoir des e-mails ou la logique d’interruption de Liquid a été appelée dans le corps du message. Tous les événements interrompus comprennent un champ avec la `reason` (raison) dans l’objet de métadonnées indiquant pourquoi le message a été interrompu |
|`delivered` (livré)| Le message a été accepté par le fournisseur de messagerie de l’utilisateur |
|`bounced` (rejeté)| Le message a été rejeté par le fournisseur de messagerie de l’utilisateur. Tous les événements renvoyés comprennent un champ avec la `reason` (raison) dans l’objet de métadonnées reflétant le code d’erreur de rebond indiqué par le fournisseur de messagerie |
{: .reset-td-br-1 .reset-td-br-2}

### Exemple de postback
```json

// Sent Event
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
}

// Interrompu
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "Impossible d’envoyer des e-mails à l’utilisateur",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
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
}

// Événement rejeté
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 Le compte d’e-mail que vous avez essayé de contacter n’existe pas",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}

