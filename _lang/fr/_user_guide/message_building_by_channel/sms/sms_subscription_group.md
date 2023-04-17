---
nav_title: "Groupes d’abonnement SMS"
article_title: Groupes d’abonnement SMS
page_order: 2
description: "Cet article de référence présente les groupes d’abonnement SMS, les statuts d’abonnement et le processus de configuration des groupes d’abonnements."
page_type: reference
channel:
  - SMS
  
---

# Groupes d’abonnement SMS

> Les groupes d’abonnement sont la base pour envoyer des SMS et MMS au moyen de Braze. Un groupe d’abonnement est une collection de [numéros de téléphone expéditeurs][2] (c.-à-d. codes courts, codes longs et/ou identifiants alphanumériques d’expéditeurs) qui sont utilisés pour envoyer un type spécifique de message. Par exemple, si une marque prévoit d’envoyer des messages SMS transactionnels et promotionnels, deux groupes d’abonnement avec des pools distincts de numéros de téléphone émetteurs devront être configurés dans votre tableau de bord de Braze.

## États d’abonnement SMS

Il existe deux états d’abonnement pour les utilisateurs de SMS : `subscribed` et `unsubscribed`. L’état d’abonnement d’un utilisateur n’est pas partagé entre les groupes d’abonnement, ce qui signifie qu’un utilisateur peut être `subscribed` pour un groupe d’abonnement transactionnel, `unsubscribed` pour un groupe promotionnel. Pour les marques, cette séparation des états assure qu’ils peuvent continuer à envoyer des SMS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaite recevoir des SMS de la part d’un groupe d’abonnement spécifique. Un utilisateur peut souscrire soit en faisant mettre à jour son état d’abonnement par l’API d’abonnement de Braze, soit en envoyant une réponse avec un mot clé d’abonnement. Un utilisateur doit être abonné à un groupe d’abonnement SMS pour recevoir un SMS |
| Non inscrit | L’utilisateur s’est explicitement désabonné de la messagerie de votre groupe d’abonnement SMS et des numéros de téléphone d’envoi au sein du groupe d’abonnement. Il peut se désabonner en envoyant une réponse avec un mot clé de désabonnement ou une marque peut désabonner des utilisateurs au moyen de l’[API abonnement de Braze][4]. Les utilisateurs désabonnés d’un groupe d’abonnement SMS ne reçoivent plus de SMS des numéros de téléphone émetteurs appartenant au groupe d’abonnement.|
{: .reset-td-br-1 .reset-td-br-2}

### Comment les groupes d’abonnement SMS d’utilisateurs sont mis en place 

- **API Rest :** Des profils d’utilisateur peuvent être définis en programmation par l’endpoint [/subscription/status/set][4] en utilisant l’API REST de Braze.
- **Intégration SDK** Les utilisateurs peuvent être ajoutés à un groupe d’abonnement e-mail ou SMS à l’aide la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) ou [Web][11].
- **Automatiquement géré lors de l’abonnement/désabonnement de l’utilisateur :** Lorsque les utilisateurs envoient un [mot-clé][7] d’abonnement ou de désabonnement par défaut, Braze configure et met à jour automatiquement l’état d’abonnement des utilisateurs.
- **User Import** : Les utilisateurs peuvent être ajoutés dans des groupes d’abonnement e-mail ou SMS via l’importation d’utilisateurs. Si vous mettez à jour le statut du groupe d’abonnement, vous devez avoir les deux colonnes suivantes dans votre CSV : `subscription_group_id` et `subscription_state`. Pour plus d’informations, consultez [User Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Comment vérifier le groupe d’abonnement SMS d’un utilisateur

- **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze en sélectionnant User Search dans la barre latérale. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet Engagement, vous pouvez afficher les groupes d’abonnement SMS d’un utilisateur. 
- **API Rest :** Le groupe d’abonnement de profils d’utilisateurs individuels peut être consulté par l’endpoint [Obtenir un groupe d’abonnement][9] ou l’endpoint [Statut du groupe d’abonnement][8] au moyen de l’API REST de Braze. 

## Envoi avec un groupe d’abonnement

Pour lancer une campagne SMS via Braze, un groupe d’abonnement doit être sélectionné dans la liste déroulante, comme illustré dans l’image suivante. Après la sélection, un filtre d’audience sera ajouté à votre campagne ou Canvas automatiquement, ce qui assure que seuls les utilisateurs `subscribed` au groupe d’abonnement sélectionné font partie de l’audience cible. Pour se conformer aux [lignes directrices internationales de conformité pour les télécommunications][3], Braze n’enverra jamais de SMS aux utilisateurs qui n’ont pas souscrit au groupe d’abonnement sélectionné.  

![L’éditeur de messages SMS apparaît avec le menu déroulant Groupe d’abonnement ouvert et « Service de messagerie A pour SMS » mis en surbrillance par l’utilisateur.][6]

## Processus de configuration

Au cours de votre processus d’intégration SMS, un gestionnaire d’onboarding de Braze configurera les groupes d’abonnement pour votre compte de tableau de bord. Il ou elle travaillera avec vous pour déterminer le nombre de groupes d’abonnement dont vous avez besoin et ajouter les numéros de téléphone émetteurs appropriés pour vos groupes d’abonnement. Les délais de configuration d’un groupe d’abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les applications de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord de Braze, contactez votre conseiller Braze pour obtenir de l’aide.  

## Habilitation MMS du groupe d’abonnement

Pour envoyer un message MMS, au moins un numéro au sein de votre groupe d’abonnement doit être activé pour envoyer MMS. Ceci est indiqué par une balise située à côté du groupe d’abonnement. 

![La liste déroulante Groupe d’abonnement apparaît avec « Service de messagerie A pour SMS » mis en surbrillance. L’entrée est préfixée par le tag « MMS ».][10]{: style="max-width:40%"}


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
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
