---
nav_title: "Recueillir les abonnements de l'utilisateur"
article_title: Bonnes pratiques pour recueillir les abonnements SMS de l'utilisateur
page_order: 7
description: "Cet article de référence présente trois bonnes pratiques pour recueillir les abonnements des utilisateurs."
page_type: reference
channel:
  - SMS
  
---

# Recueillir les abonnements de l'utilisateur

> L'article suivant répertorie plusieurs méthodes courantes d'abonnement SMS.

## Option 1 : Demander aux utilisateurs d'envoyer un SMS à votre code court ou code long

Demandez aux utilisateurs d'envoyer « START », « UNSTOP », « YES » ou un mot-clé d'abonnement personnalisé à votre numéro pour les ajouter automatiquement à votre groupe d'abonnement. Sur votre site Internet, votre application mobile ou même dans vos publicités, vous pouvez inviter les utilisateurs à effectuer cette démarche et proposer une contrepartie si cela s'avère utile.

## Option 2 : Les utilisateurs s'abonnent par message in-app

Pour permettre aux utilisateurs de s'abonner aux SMS à partir d'un message in-app, utilisez le [formulaire de capture de numéro de téléphone]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) fourni par Braze pour créer un formulaire à votre image qui vous permet de collecter des numéros de téléphone et d'élargir votre liste SMS.

![Éditeur de messages in-app avec un modèle pour la saisie du numéro de téléphone.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze vous recommande également d'utiliser la fonctionnalité de [double abonnement par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Cette fonctionnalité fonctionne automatiquement avec le formulaire de capture du numéro de téléphone par message in-app et invite les utilisateurs à confirmer leur intention après avoir soumis leur numéro de téléphone via le formulaire.

## Option 3 : Flux d'inscription

Lorsqu'un nouvel utilisateur s'inscrit ou crée un compte sur le site Internet ou l'application, demandez-lui son numéro de téléphone et son e-mail. Ajoutez une case à cocher pour recevoir les e-mails et les SMS promotionnels. 

Après l'inscription de l'utilisateur, procédez comme suit :

1. Utilisez l'[endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) pour créer l'utilisateur et enregistrer ses attributs.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour abonner l'utilisateur aux SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
Pour inscrire les utilisateurs dans le flux de [double abonnement par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) lorsque vous les abonnez via l'API REST, définissez le paramètre `use_double_opt_in_logic` sur `true` dans votre requête. Si vous omettez ce paramètre, les utilisateurs seront abonnés sans recevoir de confirmation de double abonnement.

Ce paramètre est pris en charge par les endpoints suivants :<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}