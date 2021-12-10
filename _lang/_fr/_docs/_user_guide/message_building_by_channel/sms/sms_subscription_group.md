---
nav_title: "Groupes d'abonnement SMS"
article_title: Groupes d'abonnement SMS
page_order: 2
description: "Les groupes d'abonnement sont la base de l'envoi de SMS & MMS via Braze. Un groupe d'abonnement est une collection de numéros de téléphone (c.-à-d. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie."
page_type: Référence
channel:
  - SMS
---

# Groupes d'abonnement SMS

> Les groupes d'abonnement sont la base de l'envoi de SMS & MMS via Braze. Un groupe d'abonnement est une collection de [numéros de téléphone d'envoi][2] (i.e. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Par exemple, si une marque a l'intention d'envoyer des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des groupes séparés d'envoi de numéros de téléphone devront être configurés dans votre tableau de bord Braze.

## État de l'abonnement par SMS

Il y a deux états d'abonnement pour les utilisateurs de SMS : `abonné` et `désabonné`. L'état d'abonnement d'un utilisateur n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `abonné` à un groupe d'abonnement transactionnel mais `désabonné` à un groupe promotionnel. Pour les marques, cette séparation des états assure qu'ils peuvent continuer à envoyer des messages SMS pertinents à leurs utilisateurs.

| État      | Définition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inscrit   | L'utilisateur a explicitement confirmé qu'il souhaite recevoir des SMS d'un groupe d'abonnement spécifique. Un utilisateur peut être abonné soit par la mise à jour de son état d'abonnement via l'API d'abonnement à Braze, soit en envoyant une réponse par mot clé opt-in. Un utilisateur doit être abonné à un groupe d'abonnement SMS pour recevoir un SMS                                                                                                                                |
| Désabonné | L'utilisateur a explicitement choisi de ne plus recevoir de messages de votre groupe d'abonnement SMS et les numéros de téléphone d'envoi à l'intérieur du groupe d'abonnement. Ils peuvent se désabonner en envoyant une réponse par mot clé opt-out ou une marque peut se désabonner via \[l'API d'abonnement à Braze\]\[4\]. Les utilisateurs désabonnés d'un groupe d'abonnement par SMS ne recevront plus de SMS en envoyant des numéros de téléphone appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2}

### Comment les groupes d'abonnement SMS des utilisateurs sont définis

- __API de Rest :__ Les profils utilisateur peuvent être définis par programme par le point de terminaison \[/subscription/status/set\]\[4\] en utilisant l'API REST de Braze.
- __SDK Web :__ Les utilisateurs peuvent être ajoutés à un groupe d'abonnement par e-mail ou SMS en utilisant la méthode addToSubscriptionGroup pour [Android][11], [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/#433), ou [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#340).
- __Manipulation automatique lors de l'opt-in/opt-out utilisateur :__ par les utilisateurs envoyant un opt-in ou opt-out par défaut [mot-clé][7], Braze définit et met à jour automatiquement l'état d'abonnement des utilisateurs.

### Comment vérifier le groupe d'abonnement par SMS d'un utilisateur

- __Profil utilisateur :__ Les profils utilisateur individuels sont accessibles via le tableau de bord Braze en sélectionnant la recherche d'utilisateur dans la barre latérale de droite. Ici, vous pouvez rechercher des profils d'utilisateurs par adresse e-mail, numéro de téléphone ou ID d'utilisateur externe. Une fois dans un profil d'utilisateur, sous l'onglet Engagement, vous pouvez afficher les groupes d'abonnement SMS d'un utilisateur.
- __API de repos :__ Le groupe d'abonnement à des profils utilisateur individuels peut être consulté par le [Groupe d'abonnement][9] ou [Statut de groupe d'abonnement][8] en utilisant l'API REST de Braze.

## Envoi avec un groupe d'abonnement

Pour lancer une campagne de SMS via Braze, un groupe d'abonnement doit être sélectionné dans la liste déroulante (voir ci-dessous). Une fois sélectionné, un filtre d'audience sera automatiquement ajouté à votre campagne ou à Canvas automatiquement, s'assurer que seuls les utilisateurs `inscrits` au groupe d'abonnement sélectionné sont dans le public cible. Adhérer à la [conformité et aux directives internationales en matière de télécommunication][3], Braze n'enverra jamais de SMS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.

!\[picture\]\[6\]

## Processus de configuration

Au cours de votre processus d'intégration de SMS, un gestionnaire d'intégration de Braze configurera les Groupes d'abonnement pour votre compte de tableau de bord. Ils travailleront avec vous pour déterminer le nombre de Groupes d'Abonnement dont vous avez besoin et ajouter les numéros de téléphone appropriés à vos Groupes d'Abonnement. Les échéanciers de mise en place d'un groupe d'abonnement dépendront du type de numéros de téléphone que vous ajoutez. Par exemple, les applications de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord Braze, veuillez contacter votre représentant de Braze pour obtenir de l'aide.

## Activation des MMS du groupe d'abonnement

Pour envoyer un message MMS, il faut activer au moins un numéro au sein de votre groupe d'abonnement pour envoyer des MMS. Ceci est indiqué par un tag situé à côté du Groupe d'Abonnement.

!\[picture\]\[10\]{: style="max-width:40%"}
[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %} [4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/ [6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %} [10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#addtosubscriptiongroup

