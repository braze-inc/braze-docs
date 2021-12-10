---
nav_title: Manipulation des mots clés personnalisés
article_title: Gestion des mots clés personnalisés non natifs par SMS
page_order: 1.5
description: "Cet article de référence décrit comment Braze traite les mots-clés personnalisés pour les utilisateurs non natifs de SMS."
page_type: Référence
channel:
  - SMS
---

# Messagerie bidirectionnelle (réponses personnalisées aux mots-clés)

La messagerie bidirectionnelle utilise des codes courts et des mots-clés pour livrer des messages texte aux utilisateurs de téléphones mobiles. Il faut que les utilisateurs envoient un mot clé à Braze auquel cet utilisateur recevra une réponse automatique. Appliquée correctement, la messagerie bidirectionnelle peut être une solution simple, immédiate et dynamique pour le marketing de la clientèle, en économisant du temps et des ressources.

## Vitesse de messagerie bidirectionnelle

La messagerie bidirectionnelle tire parti des événements personnalisés pour rendre possible cet échange client en apparence fluide. En raison de la nature des messages bidirectionnels, il se peut que vous trouviez une légère augmentation du temps de réponse. Voici les implications de l'inclusion du message bidirectionnel :

| Type de texte                 | Rapidité       | Notes                                                                                                                                                                                                    |
| ----------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numéros de téléphone connus   | 3-5 secondes   | Un nombre connu est un nombre qui a déjà été assigné à un attribut téléphone et est déjà abonné à un groupe d'abonnement au Brésil.                                                                      |
| Numéros de téléphone inconnus | 10-15 secondes | Un numéro inconnu est un numéro qui n'a pas encore été identifiant. Pour plus d'informations sur la façon dont les numéros de téléphone inconnus sont traités, consultez notre [documentation][unknown]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Si vous avez besoin de vitesses d'envoi plus rapides pour des numéros de téléphone inconnus, contactez votre Responsable du service clientèle ou contactez le support pour discuter de vos options.

## Gestion de la messagerie par mot clé personnalisé

| Événement personnalisé déclenché                                                            |
| ------------------------------------------------------------------------------------------- |
| `sms_response_subscriptionName_custom` | Exemples de réponse => Status, Coupons, Actualités |
{: .reset-td-br-1 .reset-td-br-2}

| Propriétés de l'événement incluses                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - `message_body`: réponse SMS des utilisateurs<br>- `to_number`: généralement code court les clients utilisés pour envoyer des SMS<br>- `from_number`: numéro de téléphone de l'utilisateur<br>- `sms_message_id`: service de messagerie ID | Message Body => <br>La réponse des utilisateurs est retournée en minuscule |
{: .reset-td-br-1 .reset-td-br-2}

- Chaque fois qu'un utilisateur envoie une réponse par SMS qui n'est pas un mot clé par défaut à un numéro de téléphone dans un groupe d'abonnement, un événement personnalisé comme `sms_response_SubscriptionGroupName_custom` avec les propriétés d'événement `message_body`, `to_number`, `from_number`, et `sms_message_id` seront envoyés au Brésil.
- Utilisez cet événement personnalisé avec la propriété `message_body` assigné comme mot-clé personnalisé pour déclencher une campagne SMS de Braze.
- La valeur du `message_body` mot clé personnalisé doit être __minuscule__.

!\[picture\]\[IMAGE2\]

Note : Cette fonctionnalité repose sur des alias d'utilisateurs afin d'assigner correctement des événements personnalisés aux profils d'utilisateurs en Brésil. Si aucun profil Braze n'existe avec un alias utilisateur du numéro de téléphone de l'utilisateur en E. 64 format, l'appel à la terminaison utilisateur/piste échouera silencieusement. L'alias doit être défini dans le format ci-dessous soit via le SDK soit le [nouveau point de terminaison d'alias utilisateur][endpoint]:
1. alias_label : `téléphone` et alias : `users_phone_number`
2. Les numéros de téléphone doivent être au format E.164 (par exemple +19173337578).

Si vous utilisez le nouveau point de terminaison d'alias de l'utilisateur, pour assurer E. 64 conformité, veuillez ajouter un préfixe "+" car le champ "téléphone" par défaut n'inclut pas automatiquement ce symbole.
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %} [2]: {% image_buster /assets/img/sms/keyword_home.png %} [IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}

[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#handling-unknown-phone-numbers
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/