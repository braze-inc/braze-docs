---
nav_title: "Groupes d'abonnement SMS"
article_title: Groupes d'abonnement SMS
page_order: 5
description: "Cet article de référence couvre les SMS Subscription Groups, une collection de numéros de téléphone qui sont utilisés pour un type spécifique de messagerie."
page_type: Référence
noindex: vrai
channel:
  - SMS
---

# Groupes d'abonnement SMS

> Les groupes d'abonnement par SMS sont le fondement de l'envoi de SMS via Braze. Un groupe d'abonnement est une collection de [numéros de téléphone d'envoi][2] (i.e. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Par exemple, si une marque a l'intention d'envoyer des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des groupes séparés d'envoi de numéros de téléphone devront être configurés dans votre tableau de bord Braze.

## Groupes de base d'abonnement par SMS

Les groupes d'abonnement sont nécessaires pour tout message SMS envoyé via Braze. Un groupe d'abonnement est un groupement de chiffres pour un cas d'utilisation de messagerie donné (par exemple, des messages commerciaux ou transactionnels). Les utilisateurs de ce groupe d'abonnement peuvent être abonnés ou désabonnés au groupe indépendamment et, s'ils sont abonnés, recevront des messages envoyés à ce groupe.

1. __Groupes d'Abonnement__
- Un groupe d'abonnement est requis pour chaque groupe d'application Braze avec lequel vous prévoyez d'envoyer des SMS.
- Les utilisateurs peuvent se désabonner de la messagerie dans un message SMS ou par l'utilisation d'autres types d'invite de désinscription (par exemple, page du compte ou flux web dans l'application). Votre équipe doit mettre à jour le statut d'abonnement de tout utilisateur qui se désabonne en dehors de la messagerie SMS.<br><br>
2. __Gestion des mises à jour des utilisateurs__
- Vous devez ajouter des utilisateurs à un groupe d'abonnement via REST API. - Les filtres de rapport [du groupe d'abonnement et de segmentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) sont disponibles pour la création et le ciblage de campagnes et de Canvases. - Deux états d'abonnement sont disponibles pour les utilisateurs de SMS : `abonné` et `désabonné`

## État de l'abonnement par SMS

Il y a deux états d'abonnement pour les utilisateurs de SMS : `abonné` et `désabonné`. L'état d'abonnement d'un utilisateur n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `abonné` à un groupe d'abonnement transactionnel mais `désabonné` à un groupe promotionnel. Pour les marques, cette séparation des états assure qu'ils peuvent continuer à envoyer des messages SMS pertinents à leurs utilisateurs.

| État      | Définition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inscrit   | L'utilisateur a explicitement confirmé qu'il souhaite recevoir des SMS d'un groupe d'abonnement spécifique. Un utilisateur peut être abonné soit par la mise à jour de son état d'abonnement via l'API d'abonnement à Braze, soit en envoyant une réponse par mot clé opt-in. Un utilisateur doit être abonné à un groupe d'abonnement SMS pour recevoir un SMS                                                                                                                                              |
| Désabonné | L'utilisateur a explicitement choisi de ne plus recevoir de messages de votre groupe d'abonnement SMS et les numéros de téléphone d'envoi à l'intérieur du groupe d'abonnement. Ils peuvent se désabonner en envoyant une réponse par mot clé opt-out ou une marque peut désabonner les utilisateurs via \[l'API d'abonnement à Braze\]\[4\]. Les utilisateurs désabonnés d'un groupe d'abonnement par SMS ne recevront plus de SMS en envoyant des numéros de téléphone appartenant au groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2}

### Comment les groupes d'abonnement SMS des utilisateurs sont définis

- __Rest API Set__: Les profils utilisateur peuvent être définis par le programme \[/subscription/status/set endpoint\]\[4\] en utilisant l'API REST de Braze.
- __Manipulation automatique lors de l'opt-in/opt-out__: Par les utilisateurs envoyant un mot clé par défaut [opt-in ou opt-out][7], Braze définit et met à jour automatiquement l'état d'abonnement des utilisateurs.

### Comment vérifier le groupe d'abonnement par SMS d'un utilisateur

- __Profil utilisateur__: Les profils utilisateur individuels sont accessibles via le tableau de bord Braze en sélectionnant **Recherche d'utilisateur** dans la barre latérale droite. Ici, vous pouvez rechercher des profils d'utilisateurs par adresse e-mail, numéro de téléphone ou ID d'utilisateur externe. Une fois dans un profil utilisateur, sous l'onglet **Engagement** , vous pouvez afficher les groupes d'abonnement SMS d'un utilisateur.
- __Rest API Get__: Le groupe d'abonnement à des profils utilisateur individuels peut être consulté par le point de terminaison [Get Subscription Group][9] ou [Subscription Group Status][8] en utilisant l'API REST de Braze.

## Envoi avec un groupe d'abonnement

Pour lancer une campagne de SMS via Braze, un groupe d'abonnement doit être sélectionné dans la liste déroulante (voir ci-dessous). Une fois sélectionné, un filtre d'audience sera automatiquement ajouté à votre campagne ou à Canvas automatiquement, s'assurer que seuls les utilisateurs `inscrits` au groupe d'abonnement sélectionné sont dans le public cible. Adhérer à la [conformité et aux directives internationales en matière de télécommunication][3], Braze n'enverra jamais de SMS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.

!\[picture\]\[6\]

## Processus de configuration

Au cours de votre processus d'intégration de SMS, un gestionnaire d'intégration de Braze configurera les Groupes d'abonnement pour votre compte de tableau de bord. Ils travailleront avec vous pour déterminer le nombre de Groupes d'Abonnement dont vous avez besoin et ajouter les numéros de téléphone appropriés à vos Groupes d'Abonnement. Les échéanciers de mise en place d'un groupe d'abonnement dépendront du type de numéros de téléphone que vous ajoutez. Par exemple, les applications de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord Braze, veuillez contacter votre représentant de Braze pour obtenir de l'aide.

## Activation des MMS du groupe d'abonnement

Pour envoyer un message MMS, il faut activer au moins un numéro au sein de votre groupe d'abonnement pour envoyer des MMS. Ceci est indiqué par un tag situé à côté du Groupe d'Abonnement.

!\[picture\]\[10\]{: style="max-width:40%"}
[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %} [4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/ [6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %} [10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}

[2]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/
[3]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_laws_and_regulations/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/

