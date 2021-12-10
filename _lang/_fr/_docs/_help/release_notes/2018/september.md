---
nav_title: Septembre
page_order: 5
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour septembre 2018."
---

# Septembre 2018

## Groupes de notification iOS 12 : Capacités supplémentaires

Vous pouvez maintenant accéder aux fonctionnalités du [Groupe de Notifications d'Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) en utilisant Braze ! Vous pouvez ajouter des arguments de résumé et des groupes, utiliser des alertes critiques, filtrer pour les utilisateurs authentifiés Provisionally et afficher le statut authentifié Provisionally sur les profils des utilisateurs.

## Temps de silence

Les clients peuvent maintenant spécifier [Heures silencieuses]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (l'heure pendant laquelle vos messages ne seront pas envoyés) pour Canvas. Allez simplement dans vos __Paramètres d'envoi de Canvas__ et cochez "Activer les heures silencieures". Ensuite, sélectionnez vos heures silencieuses dans l'heure locale de votre utilisateur et quelle action suivra si le message se déclenche à l'intérieur de ces heures silencieuses.

Les campagnes utilisent maintenant le temps silencieux au lieu de « envoyer ce message pendant une partie spécifique de la journée ».

## Ajuster les clients

Les clients Braze utilisant [Ajuster]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) sont maintenant en mesure de voir leur clé API Braze et leur URL d'instance Braze, qu'ils utiliseront ensuite dans la plate-forme Ajuster pour s'intégrer.

## Pas dans le filtre de segment

Les clients peuvent maintenant créer un segment parmi les utilisateurs qui ne sont [pas inclus dans un certain segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exports CSV des destinataires de Canvas

Les clients peuvent maintenant [exporter des données sur les utilisateurs qui sont entrés dans une Canvas]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/). Le CSV généré sera similaire au CSV de la campagne.

## Filtre de segment iOS 12 provisoirement autorisé

Un [filtre de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) qui vous permet de trouver des utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée a été ajouté.

## Chargeur d'image de message dans l'application

Le chargeur d'images pour les messages intégrés à l'application a été déplacé du panneau de conception (paintbrush) vers le panneau de composition (crayon).

## Autorisations en lecture seule sur la page du profil utilisateur

Avant cette version, les clients étaient en mesure de changer le statut d'abonnement et l'adresse e-mail dans le profil de l'utilisateur avec la [permission en lecture seule]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Nous avons renommé la permission `import_user` en la permission `import_and_update_user` et restreint l'accès aux statuts d'abonnement et à l'adresse e-mail. Maintenant, lorsqu'un développeur est en lecture seule en usurpant l'identité ou en l'absence de cette autorisation, il ne peut pas changer le statut d'abonnement ou l'adresse e-mail.
