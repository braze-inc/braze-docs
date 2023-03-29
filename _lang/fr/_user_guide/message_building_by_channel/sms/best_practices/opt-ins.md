---
nav_title: "Abonnements de l’utilisateur"
article_title: Bonnes pratiques pour recueillir les abonnements SMS de l’utilisateur
page_order: 7
description: "Cet article de référence couvre trois bonnes pratiques pour recueillir les abonnements des utilisateurs."
page_type: reference
channel:
  - SMS
  
---

# Recueillir les abonnements de l’utilisateur

L’article suivant répertorie plusieurs méthodes courantes d’abonnement SMS.

## Option 1 : Demandez aux utilisateurs d’envoyer un code long ou court

Demandez aux utilisateurs d’envoyer « START », « UNSTOP », « YES » ou un mot-clé d’abonnement personnalisé vers votre numéro pour les ajouter automatiquement à votre groupe d’abonnement. Sur votre site Internet, application mobile ou même vos annonces, vous pouvez demander aux utilisateurs d’effectuer cet abonnement et proposer un encouragement s’il est utile.

## Option 2 : Les utilisateurs d’abonnement par message in-app

Si vous désirez que les utilisateurs s’abonnent aux SMS depuis un message in-app, consultez les étapes d’implémentation ci-dessous. Nous vous conseillons de commencer par le tester dans un groupe d’apps mis en scène. 

1. Lancez une campagne de messages dans le navigateur ou in-app qui demande le numéro de téléphone de l’utilisateur en leur recommandant de s’abonner. Lorsqu’un utilisateur clique sur « envoyer », vous devrez enregistrer un nouvel événement personnalisé tel que `phone_number_captured`.<br><br>
2. Tirez ensuite parti de Canvas pour abonner officiellement l’utilisateur et envoyer une confirmation. Définissez l’entrée dans le Canvas pour qu’elle soit par événement, selon le déclencheur `phone_number_captured` de l’événement personnalisé qui a été enregistré dans le message in-app ci-dessus. Vous pouvez également cibler les utilisateurs pour lesquels « ID utilisateur externe n’est pas vide » ou tout autre attribut pertinent pour l’audience d’entrée, comme nécessaire. <br><br>
3. Ajoutez un webhook à l’endpoint [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) en tant que première étape du Canvas. Ceci transmet le numéro de téléphone de l’utilisateur dans le groupe d’abonnement pour l’abonner officiellement. <br>![][1]<br><br>
4. La seconde et dernière étape du Canvas est un SMS de confirmation aux utilisateurs, validant leur statut d’abonnement.<br>![][2]

## Option 3 : Flux d’inscription

Lorsqu’un nouvel utilisateur s’inscrit ou s’enregistre sur le site Internet ou l’application, demandez-lui son numéro de téléphone et son e-mail. Ajoutez une case à cocher pour recevoir les e-mails et les SMS promotionnels. Une fois que l’utilisateur s’est inscrit, utilisez l’endpoint [/subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status) :

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

[1]: {% image_buster /assets/img/sms/opt-in1.png %}
[2]: {% image_buster /assets/img/sms/opt-in2.png %}