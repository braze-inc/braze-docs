Tous les e-mails transactionnels sont complétés par des postbacks de statut d’événement envoyés en tant que requête HTTP à l’URL spécifiée. Cela vous permet d’évaluer le statut du message en temps réel et de prendre des mesures pour atteindre l’utilisateur sur un autre canal si le message n’est pas reçu ou recourir à un système interne si Braze connaît une certaine latence.

Vous pouvez associer ces mises à jour à des messages individuels à l'aide d'identifiants uniques :

- `dispatch_id` : Un ID unique est généré automatiquement par Braze pour chaque message.
- `external_send_id` : Un identifiant personnalisé que vous fournissez, tel qu'un numéro de commande, pour faire correspondre les mises à jour avec vos systèmes internes.

Par exemple, si vous incluez `external_send_id: 1234` dans la requête lors de l'envoi d'un e-mail de confirmation de commande, toutes les rétrocessions d'événements ultérieures pour cet e-mail - comme `Sent` ou `Delivered`- incluront `external_send_id: 1234`. Cela vous permet de confirmer que le client de la commande n°1234 a bien reçu l'e-mail de confirmation de sa commande.

### Mise en place de postbacks

Dans votre tableau de bord de Braze :

1. Allez dans **Paramètres** > **Préférences e-mail.**
2. Sous **Postback d'état d'événement transactionnel**, entrez l'URL où Braze doit envoyer des mises à jour d'état pour vos e-mails transactionnels.
3. Testez le postback.

![]({% image_buster /assets/img/transactional_webhook_url.png %})

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

|  État | Description |
| ------------ | ----------- |
| `sent` | Message envoyé avec succès à un partenaire d'envoi d'e-mail de Braze |
| `processed` | Le partenaire d’envoi d’e-mail a reçu et préparé avec succès le message pour l’envoyer au fournisseur de messagerie de l’utilisateur |
| `aborted` | Braze n’a pas réussi à envoyer le message, car l’adresse de l’utilisateur ne permet pas de recevoir des e-mails ou la logique d’interruption de Liquid a été appelée dans le corps du message. Tous les événements abandonnés comprennent un champ `reason` dans l’objet de métadonnées indiquant pourquoi le message a été abandonné |
|`delivered`| Le message a été accepté par le fournisseur de messagerie de l’utilisateur |
|`bounced`| Le message a été rejeté par le fournisseur de messagerie de l’utilisateur. Tous les événements renvoyés comprennent un champ `reason` dans l’objet de métadonnées reflétant le code d’erreur de rebond indiqué par le fournisseur de messagerie |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

// Processed Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Aborted
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "aborted",
    "metadata": {
      "reason": "User not emailable",
      "aborted_at": "2020-08-31T19:04:51.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32.000+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounced Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43.000+00:00",
      "reason": "550 5.1.1 The email account that you tried to reach does not exist",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```

