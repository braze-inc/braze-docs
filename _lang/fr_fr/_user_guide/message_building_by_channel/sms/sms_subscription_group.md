---
nav_title: "Groupes d’abonnement SMS"
article_title: Groupes d’abonnement SMS
page_order: 4
description: "Cet article de référence traite des groupes d'abonnement SMS, des états d'abonnement et de la configuration des groupes d'abonnement."
page_type: reference
channel:
  - SMS
  
---

# Groupes d’abonnement SMS

> Les groupes d'abonnement constituent la base de l'envoi de SMS et de MMS par l'intermédiaire de Braze. Un groupe d'abonnement est un ensemble de [numéros de téléphone d'envoi][2] (tels que des codes courts, des codes longs et/ou des ID d'expéditeur alphanumériques) qui sont utilisés pour un type spécifique d'envoi de messages. Par exemple, si une marque prévoit d'envoyer à la fois des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des pools distincts de numéros de téléphone d'envoi devront être configurés dans votre tableau de bord de Braze.

## États d’abonnement SMS

Il existe deux états d’abonnement pour les utilisateurs de SMS : `subscribed` et `unsubscribed`. L'état de l'abonnement d'un utilisateur n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `subscribed` dans un groupe d'abonnement transactionnel mais `unsubscribed` dans un groupe d'abonnement promotionnel. Pour les marques, cette séparation des états assure qu’ils peuvent continuer à envoyer des SMS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L'utilisateur a explicitement confirmé qu'il souhaite recevoir des SMS d'un groupe d'abonnement spécifique. Un utilisateur peut souscrire soit en faisant mettre à jour son état d’abonnement par l’API d’abonnement de Braze, soit en envoyant une réponse avec un mot clé d’abonnement. Un utilisateur doit être abonné à un groupe d'abonnement SMS pour pouvoir recevoir un SMS. |
| Désabonné | L'utilisateur a explicitement choisi de ne plus recevoir de messages de votre groupe d'abonnement SMS et des numéros de téléphone d'envoi au sein du groupe d'abonnement. Il peut se désabonner en envoyant une réponse avec un mot clé de désabonnement ou une marque peut désabonner des utilisateurs au moyen de l’[API d’abonnement de Braze][4]. Les utilisateurs désabonnés d'un groupe d'abonnement SMS ne recevront plus de SMS provenant des numéros de téléphone d'envoi appartenant au groupe d'abonnement.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comment les groupes d’abonnement SMS d’utilisateurs sont mis en place 

- **API REST :** Les profils utilisateurs peuvent être définis de manière programmatique par l'endpoint [`/subscription/status/set`][4] en utilisant l'API REST de Braze.
- **Intégration SDK** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement e-mail ou SMS à l'aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web][11].
- **Traitement automatique en cas d'abonnement/de désabonnement de l'utilisateur :** En envoyant par SMS un message d'abonnement ou de désabonnement par défaut [mot-clé :][7]], Braze définit et met à jour automatiquement l'état de l'abonnement de l'utilisateur.
- **Import d'utilisateurs**: Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail ou SMS via l'**importation d'utilisateurs.** Si vous mettez à jour le statut du groupe d’abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV : `subscription_group_id` et `subscription_state`. Reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) pour plus d'informations.

Lorsqu'un numéro de téléphone est mis à jour dans un profil utilisateur, le nouveau numéro de téléphone hérite du statut du groupe d'abonnement de l'utilisateur. Si le numéro de téléphone est mis à jour vers un numéro qui existe déjà dans Braze, le statut d'abonnement de ce numéro de téléphone existant est hérité.

Par exemple, si l'utilisateur A a un numéro de téléphone abonné à plusieurs groupes d'abonnement et que ce numéro de téléphone est ensuite ajouté à l'utilisateur B, l'utilisateur B sera abonné aux mêmes groupes d'abonnement. Pour empêcher un utilisateur d'hériter des abonnements existants, vous pouvez réinitialiser les groupes d'abonnement de l'ancien numéro via l'API REST chaque fois qu'un utilisateur change de numéro. Si plusieurs utilisateurs partagent ce numéro de téléphone, ils seront tous désabonnés.

### Comment vérifier le groupe d’abonnement SMS d’un utilisateur

- **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze en sélectionnant User Search dans la barre latérale. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Dans le profil d'un utilisateur, sous l'onglet Engagement, vous pouvez voir les groupes d'abonnement SMS d'un utilisateur. 
- **API REST :** Le groupe d’abonnement des profils utilisateur individuels peut être consulté par l’[endpoint Lister les groupes d’abonnement de l’utilisateur][9] ou de l’[endpoint Lister le statut des groupes d’abonnement de l’utilisateur][8] en utilisant l'API REST de Braze. 

## Envoi avec un groupe d’abonnement

Pour lancer une campagne SMS via Braze, un groupe d'abonnement doit être sélectionné dans le menu déroulant, comme le montre l'image suivante. Une fois sélectionné, un filtre d'audience sera automatiquement ajouté à votre campagne ou Canvas, garantissant que seuls les utilisateurs `subscribed` au groupe d’abonnement sélectionné font partie de l'audience cible. Afin de se conformer aux [règles et directives internationales en matière de télécommunications][3], Braze n'enverra jamais de SMS aux utilisateurs qui ne se sont pas abonnés au groupe d'abonnement sélectionné.  

![Composeur de messages SMS avec le menu déroulant Groupe d’abonnement ouvert et « Service de messagerie A pour SMS » mis en surbrillance par l’utilisateur.][6]

## Processus de configuration

Au cours de votre processus d’onboarding par SMS, un gestionnaire d’onboarding de Braze configurera les groupes d’abonnement pour votre compte de tableau de bord. Ils détermineront avec vous le nombre de groupes d'abonnement dont vous avez besoin et ajouteront les numéros de téléphone d'envoi appropriés à vos groupes d'abonnement. Les délais de mise en place d'un groupe d'abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les applications de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord de Braze, contactez votre conseiller Braze pour obtenir de l’aide.  

## Habilitation MMS du groupe d’abonnement

Pour envoyer un message MMS, au moins un numéro de votre groupe d'abonnement doit être autorisé à envoyer des MMS. Ceci est indiqué par une étiquette située à côté du groupe d’abonnement. 

![La liste déroulante Groupe d’abonnement apparaît avec « Service de messagerie A pour SMS » mis en surbrillance. L'entrée est précédée de l'étiquette « MMS ».][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
Il y a [11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
