---
nav_title: "POST: Envoyer des E-mails transactionnels via la livraison déclenchée par l'API"
article_title: "POST: Envoyer des E-mails transactionnels via la livraison déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur l'envoi de messages transactionnels par l'intermédiaire du point de terminaison de livraison Braze déclenché par l'API."
---

{% api %}
# Envoi d'emails transactionnels via livraison déclenchée par l'API
{% apimethod post %}
/fr/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
{% endapimethod %}

Le point de terminaison d'envoi d'emails transactionnels vous permet d'envoyer immédiatement des messages ad hoc aux utilisateurs désignés. Ce point de terminaison est utilisé parallèlement à la création d'une [campagne d'email transactionnelle]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) et de l'ID de campagne correspondante.

{% alert important %}
Le courrier électronique transactionnel est actuellement disponible dans le cadre de certains paquets Braze. Pour plus de détails, veuillez contacter votre Responsable du service client de Braze.
{% endalert %}

Similaire au [Envoyer le point de terminaison de la campagne déclenchée]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), ce type de campagne vous permet d'héberger le contenu des messages dans le tableau de bord Braze tout en dictant quand et à qui un message est envoyé via votre API. Contrairement au point de terminaison de la campagne déclenchée qui accepte un public ou un segment pour envoyer des messages, une requête à ce point de terminaison doit spécifier un seul utilisateur soit par un ID Utilisateur Externe, soit par un Alias Utilisateur, ce type de campagne est conçu pour la messagerie 1:1 d'alertes comme les confirmations de commande ou les réinitialisations de mot de passe.

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "external_send_id": (optionnel, string) voir external_send_id ci-dessous,
  "trigger_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à l'utilisateur dans cette requête,
  "destinataires" : (obligatoire, objet)
    [{
      // "external_user_id" ou "user_alias" est requis. Les requêtes ne doivent spécifier qu'une seule fois.
      "user_alias": (optionnel, objet alias utilisateur) alias de l'utilisateur pour recevoir le message,
      "external_user_id": (optionnel, string) Identificateur externe de l'utilisateur pour recevoir le message,
      "attributs": (optionnel, objet) les champs dans l'objet attributs créeront ou mettront à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié avant l'envoi du message et les valeurs existantes seront remplacées par
    }]
}
```

## Paramètres de la requête

| Paramètre                      | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------ | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ID externe`                   | Optionnel | Chaîne de caractères | Une chaîne compatible Base64. Validé par rapport aux expressions régulières suivantes :<br><br> `/^[a-zA-Z0-9-_+\/<unk> +$/` <br><br>Ce champ facultatif vous permet de passer un identifiant interne pour cet envoi particulier, qui seront inclus dans les événements envoyés depuis le postback de l'événement Transactional HTTP. Lorsqu'il est passé, cet identifiant sera également utilisé comme clé de déduplication que Braze stockera pendant 24 heures. <br><br>Passer le même identifiant dans une autre requête ne donnera pas lieu à une nouvelle instance d'un envoi par Braze pendant 24 heures.                                                                                                                                                                                                                                                                            |
| `format@@0 trigger_properties` | Optionnel | Objet                | Voir [les propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Paires clé-valeur de personnalisation qui s'appliqueront à l'utilisateur dans cette requête.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Destinataires`                | Requis    | Objet                | Voir l'objet [destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). L'utilisateur auquel vous vous adressez à ce message. <br><br>Notez que si vous fournissez un ID utilisateur externe qui n'existe pas déjà en Brésil, passer tous les champs à l'objet `attributs` créera ce profil utilisateur dans Braze et enverra ce message à l'utilisateur nouvellement créé. <br><br>Si vous envoyez des requêtes multiples au même utilisateur avec des données différentes dans l'objet `attributs` , Braze s'assurera que `prénom`, `nom_famille`, et `email` les attributs seront mis à jour de manière synchronisée et modélisés dans votre message. Les attributs personnalisés n'ont pas cette même protection, procédez donc avec prudence lorsque vous mettez à jour un utilisateur à travers cette API et en passant des valeurs d'attributs personnalisés différentes par la suite. |
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
          "exemple_integer_property" : VOTRE_EXAMPLE_INTEGER
        },
        "destinataires": [{
          "external_user_id": TARGETED_USER_ID_STRING
        }]
      }' \
  https://rest. ad-01.braze.com/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send
```

## Réponse

Le point de terminaison de l'e-mail transactionnel d'envoi répondra avec le message `dispatch_id` qui représente l'instance de ce message envoyé. Cet identifiant peut être utilisé avec des événements du postback d'événement HTTP transactionnel pour tracer l'état d'un e-mail individuel envoyé à un seul utilisateur.

### Exemple de réponse

```json
{
    "dispatch_id": Out-of-the-box generated Unique ID of the instance of this send
    "status": État actuel du message
    "metadata" : Objet contenant des informations supplémentaires à propos de l'instance envoyée
}
```

### Postback d'événement HTTP transactionnel

Tous les e-mails transactionnels sont complétés par des retours de statut d'événement envoyés en tant que requête HTTP à l'adresse spécifiée. Cela vous permettra d'évaluer l'état du message en temps réel et de prendre des mesures pour atteindre l'utilisateur sur un autre canal si le message n'est pas distribué, ou de revenir à un système interne si Braze est en latence.

Afin d'associer les événements entrants à une instance particulière d'envoi, vous pouvez choisir soit de capturer et stocker l'ID de Braze Dispatch retourné dans la réponse API comme détaillé ci-dessus, ou passez votre propre identifiant au champ `external_send_id`. Un exemple de valeur que vous pouvez choisir de passer à ce champ peut être un ID de commande, où après avoir complété la commande 1234, un message de confirmation de commande est déclenché pour l'utilisateur via Braze, et `external_send_id : 1234` est inclus dans la requête. Tous les postbacks d'événement suivants tels que `Envoyés` et `Livrés` incluront `external_send_id : 1234` dans le bloc vous permettant de confirmer que l'utilisateur a bien reçu son e-mail de confirmation de commande.

Pour commencer à utiliser le Postback d'événement HTTP Transactional Naviguez pour Gérer les paramètres > Paramètres de messagerie > URL WebPush transactionnelle dans votre tableau de bord Braze et entrez l'URL désirée pour recevoir des postbacks.

![Mise à jour de l'URL du Webhook transactionnel]({% image_buster /assets/img/transactional_webhook_url.png %})


### Corps du postback

```json
{
  "dispatch_id": (chaîne, Out-of-the-box a généré un ID unique de l'instance de cet envoi),
  "status": (chaîne, état actuel du message des champs ci-dessous)
  "métadonnées" : (objet, des informations supplémentaires relatives à l'exécution d'un événement)
   {
     "external_send_id" : (string, Si fourni au moment de la demande, Braze passera votre identifiant interne pour cet envoi pour tous les postbacks),
     "campaign_api_id" : (string, Identifiant API de cette campagne transactionnelle),
     "received_at": (ISO 8601 DateTime string, Horodatage du moment où la demande a été reçue par Braze, uniquement inclus pour les événements avec le statut "envoyé"),
     "queued_at": (chaîne DateTime ISO 8601, Horodatage du moment où la requête a été mise en file d'attente par Braze, uniquement pour les événements avec le statut "envoyé")
     "executed_at": (ISO 8601 DateTime string, Horodatage du moment où la requête a été traitée par Braze, uniquement pour les événements avec le statut "envoyé"),
     "sent_at": (ISO 8601 DateTime string, Horodatage du moment où la requête a été envoyée à l'ESP par Brésil, uniquement inclus pour les événements avec le statut "envoyé"),
     "processed_at" : (chaîne DateTime ISO 8601, Horodatage de l'événement a été traité par l'ESP, uniquement inclus pour les événements avec le statut "processed"),
     "delivered_at" : (chaîne DateTime ISO 8601, Horodatage de l'événement a été envoyé au fournisseur de la boîte de réception de l'utilisateur, seulement inclus pour les événements avec le statut "traité"),
     "bounced_at" : (ISO 8601 DateTime string, Horodatage de l'événement a été rejeté par le fournisseur de la boîte de réception de l'utilisateur, seulement inclus pour les événements avec le statut "rebond"),
     "aborted_at" : (ISO 8601 DateTime string, Horodatage de l'événement a été annulé par Braze, uniquement inclus pour les événements avec le statut "abandonné"),
     "raison" : (chaîne, La raison pour laquelle Braze ou le fournisseur de la boîte de réception n'a pas pu traiter ce message à l'utilisateur, uniquement inclus pour les événements avec le statut "abandonné" ou "rebond"),
   }

```

| Statut      | Libellé                                                                                                                                                                                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `envoyé`    | Message envoyé avec succès au partenaire d'envoi de l'e-mail de Braze                                                                                                                                                                                                                                     |
| `traité`    | Le partenaire d'envoi d'e-mails a bien reçu et préparé le message à envoyer au fournisseur de la boîte de réception de l'utilisateur                                                                                                                                                                      |
| `abandonné` | Braze n'a pas pu envoyer le message avec succès car l'utilisateur n'a pas d'adresse e-mail. ou la logique d'abandon de Liquid a été appelée dans le corps du message. Tous les événements abandonnés incluent un champ `raison` dans l'objet de métadonnées indiquant pourquoi le message a été abandonné |
| `livrée`    | Le message a été accepté par le fournisseur de messagerie de l'utilisateur                                                                                                                                                                                                                                |
| `rebondi`   | Le message a été rejeté par le fournisseur de messagerie de l'utilisateur. Tous les événements rebondis incluent un champ `raison` dans l'objet de métadonnées reflétant le code d'erreur fourni par le fournisseur de boîte de réception                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

### Exemple de postback
```json

// Événement Envoyé
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "sent",
    "metadata": {
      "received_at": "2020-08-31T18:58:41. 00+00:00",
      "enqueued_at": "2020-08-31T18:58:41. 00+00:00",
      "executed_at": "2020-08-31T18:58:41.000+00:00",
      "sent_at": "2020-08-31T18:58:42. 00+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Événement traité
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "processed",
    "metadata": {
      "processed_at": "2020-08-31T18:58:42. 00+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Abandonné
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "statut": "abandon",
    "métadonnées": {
      "raison": "L'utilisateur n'est pas envoyé",
      "aborted_at": "2020-08-31T19:04:51. 00+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Delivered Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "delivered",
    "metadata": {
      "delivered_at": "2020-08-31T18:27:32. 00+00:00",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

// Bounce Event
{
    "dispatch_id": "acf471119f7449d579e8089032003ded",
    "status": "bounced",
    "metadata": {
      "bounced_at": "2020-08-31T18:58:43. 00+00:00",
      "raison": "550 5.1. Le compte de messagerie que vous avez essayé d'atteindre n'existe pas",
      "campaign_api_id": "417220e4-5a2a-b634-7f7d-9ec891532368",
      "external_send_id" : "34a2ceb3cf6184132f3d816e9984269a"
    }
}

```


{% endapi %}

