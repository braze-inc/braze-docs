---
nav_title: "Recueillir les abonnements des utilisateurs"
article_title: Bonnes pratiques pour la collecte des abonnements SMS des utilisateurs
page_order: 7
description: "Cet article de référence présente trois bonnes pratiques pour collecter les abonnements des utilisateurs."
page_type: reference
channel:
  - SMS
  
---

# Recueillir les abonnements des utilisateurs

> L'article suivant énumère quelques méthodes courantes d'abonnement par SMS.

## Option 1 : Demandez aux utilisateurs d'envoyer par SMS votre code court ou long.

Demandez aux utilisateurs d'envoyer par SMS "START", "UNSTOP", "YES" ou un mot-clé d'abonnement personnalisé à votre numéro pour les ajouter automatiquement à votre groupe d'abonnement. Sur votre site web, votre application mobile ou même votre publicité, vous pouvez demander aux utilisateurs de faire cela pour s'abonner, et vous pouvez proposer une incitation si c'est utile.

## Option 2 : Les utilisateurs s'abonnent via un message in-app.

Pour permettre aux utilisateurs d'opter pour les SMS à partir d'un message in-app, utilisez le [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) fourni par Braze pour créer un formulaire de marque qui vous permet de collecter des numéros de téléphone et d'augmenter votre liste de SMS.

Composez un message in-app avec un modèle de capture de numéro de téléphone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze vous recommande d'utiliser également la fonctionnalité de [double abonnement par SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)  Cette fonctionnalité fonctionne automatiquement avec le formulaire de capture du numéro de téléphone par message in-app, invitant les utilisateurs à confirmer leur intention après avoir soumis leur numéro de téléphone via le formulaire.

## Option 3 : Flux d'inscription

Lorsqu'un nouvel utilisateur s'inscrit ou s'enregistre sur le site web ou l'appli, demandez-lui son numéro de téléphone et son e-mail. Incluez une case à cocher pour recevoir des e-mails et des SMS promotionnels. 

Après l'inscription de l'utilisateur, procédez comme suit :

1. Utilisez l'[endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) pour créer l'utilisateur et enregistrer ses attributs.

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\. Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour abonner l'utilisateur aux SMS.

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

