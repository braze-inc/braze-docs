---
nav_title: Septembre
page_order: 5
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2018."
---
# Septembre 2018

## Groupes de notification iOS 12 : Capacités supplémentaires

Vous pouvez maintenant accéder aux [Fonctions Groupe de notification d’Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) en utilisant Braze ! Vous pouvez ajouter des arguments et des groupes récapitulatifs, utiliser les alertes critiques, filtrer les utilisateurs authentifiés provisoirement et voir les profils utilisateur qui ont un statut Authentifié Provisoirement.

## Période creuse

Si vous le souhaitez, indiquez des [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (période pendant laquelle vos messages ne seront pas envoyés) pour votre Canvas. Allez sur vos **Paramètres d’envoi Canvas** et cochez « Enable Quiet Hours (Activer les heures calmes) ». Puis sélectionnez vos Heures calmes dans l’heure locale de vos utilisateurs et l’action qui suivra si le message se déclenche pendant ces heures calmes.

Les campagnes utilisent désormais les périodes creuses plutôt que « envoyer ce message à un moment spécifique de la journée ».

## Clients d’Adjust

Les clients de Braze qui utilisent [Adjust]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) peuvent maintenant voir leur clé API Braze et l’URL de leur instance Braze, et les utiliser pour intégrer leur plateforme Adjust.

## Filtre « Pas dans le segment »

Les clients peuvent désormais créer un segment avec les utilisateurs [non inclus dans un segment donné]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportations des destinataires Canvas sur CSV 

Les clients peuvent maintenant [exporter les données]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/) sur les utilisateurs entrés dans un Canvas. Le CSV généré sera similaire au CSV de Campagne.

## Filtre de segmentation « iOS 12 » autorisé provisoirement

Nous avons ajouté un [filtre de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) qui vous permet de trouver les utilisateurs provisoirement autorisés sur iOS 12 pour une application donnée.

## Chargeur d’images pour les messages in-app

Le chargeur d’images pour les messages in-app a été déplacé du panneau de conception vers le panneau de composition.

## Autorisations en lecture seule sur la page User Profile (Profil utilisateur)

Avant cette version, les clients pouvaient modifier leur statut d’abonnement et leur adresse e-mail dans leur profil utilisateur avec des [autorisations en lecture seule]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Nous avons renommé l’autorisation `import_user` en autorisation `import_and_update_user` et restreint l’accès au statut d’abonnement et à l’adresse e-mail. Désormais si un développeur imite le mode lecture seule ou n’a pas cette autorisation, il ne peut pas modifier le statut d’abonnement ou l’adresse e-mail.
