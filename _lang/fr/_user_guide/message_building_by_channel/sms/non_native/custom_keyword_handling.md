---
nav_title: Gestion personnalisée des mots-clés
article_title: Gestion des mots clés personnalisés pour SMS non natif
page_order: 1.5
description: "Le présent article de référence traite de la manière dont Braze traite les mots clés personnalisés pour les utilisateurs SMS non-natifs."
page_type: reference
channel:
  - SMS

---

# Messagerie bidirectionnelle (réponses aux mots-clés personnalisés)

La messagerie bidirectionnelle utilise des codes courts et des mots clés pour envoyer des messages texte aux utilisateurs mobiles. Il faut que les utilisateurs finaux envoient un mot-clé à Braze et l’utilisateur recevra une réponse automatique. Appliquée correctement, la messagerie bidirectionnelle peut être une solution simple, immédiate et dynamique pour le marketing client, et qui permet de gagner du temps et des ressources tout au long du processus. 

## Vitesses de messagerie bidirectionnelle

La messagerie bidirectionnelle tire parti des événements personnalisés pour rendre possible cet échange client de clients apparemment fluide. En raison de la nature de la messagerie bidirectionnelle, vous pouvez noter une légère augmentation du temps de réponse. Voici une liste de conséquences de l’inclusion de la messagerie bidirectionnelle :

| Type | Vitesse | Remarques | 
| ----- | ----- | ---- | 
| Numéros de téléphone connus | 3 à 5 secondes | Un numéro connu est un numéro auquel on a déjà attribué un attribut de téléphone et qui est déjà inscrit dans un groupe d’abonnement chez Braze.
| Numéros de téléphone inconnus |  10 à 15 secondes | Un numéro inconnu est un numéro qui n’a pas encore été identifié. Pour plus d’informations sur la manière dont les numéros de téléphone inconnus sont traités, consultez [Codes courts et codes longs][unknown].|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Si vous avez besoin de vitesses d’envoi plus rapides pour les numéros de téléphone inconnus, contactez votre gestionnaire du succès des clients ou contactez le service d’assistance pour discuter de vos options.

## Gestion de messagerie avec mots-clés personnalisés

| Événement personnalisé déclenché |
| ------- | ------ |
| `sms_response_subscriptionName_custom` | Exemples de réponse => Statut, Coupons, Actualités |
{: .reset-td-br-1 .reset-td-br-2}

| Propriétés de l’événement incluses |
| ------- | ------ |
| - `message_body` : réponse SMS des utilisateurs<br>- `to_number` : généralement un code court que les clients ont utilisé pour envoyer un SMS<br>- `from_number` : numéro de téléphone de l’utilisateur<br>- `sms_message_id` : ID du service d’envoi de messages | Corps du message => <br>Réponse de l’utilisateur renvoyée en minuscules |
{: .reset-td-br-1 .reset-td-br-2}

- Chaque fois qu’un utilisateur envoie une réponse SMS qui n’est pas un mot-clé par défaut à un numéro de téléphone qui fait partie d’un groupe d’abonnement donné, un événement personnalisé comme `sms_response_SubscriptionGroupName_custom` avec les propriétés de l’événement `message_body`, `to_number`, `from_number`, et `sms_message_id` sera envoyé à Braze. 
- Utilisez cet événement personnalisé avec la propriété `message_body` attribuée comme mot clé personnalisé pour déclencher une campagne SMS à partir de Braze.
- La `message_body` valeur du mot-clé personnalisé doit être **en minuscules**.

![][IMAGE2]

Cette fonctionnalité s’appuie sur les alias des utilisateurs pour attribuer correctement des événements personnalisés à des profils utilisateur dans Braze. S’il n‘existe aucun profil Braze avec un alias utilisateur du numéro de téléphone de l’utilisateur au format E.164, l’appel vers l’endpoint de l’utilisateur échoue en silence. L’alias doit être défini au format suivant soit par le SDK soit par [l’endpoint du nouvel alias utilisateur][endpoint] :

1. alias_label : `phone` et alias_name : `users_phone_number`
2. Les numéros de téléphone doivent être au format E.164 (par ex. +19173337578). 

Si vous utilisez le nouvel endpoint d’alias d’utilisateur pour assurer la conformité E.164, ajoutez un préfixe plus « + »" car le champ téléphone par défaut n’inclut pas automatiquement ce symbole.

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#handling-unknown-phone-numbers
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}