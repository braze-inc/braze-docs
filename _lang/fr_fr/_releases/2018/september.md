---
nav_title: septembre
page_order: 5
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2018."
---
# Septembre 2018

## Groupes de notification iOS 12 : Capacités supplémentaires

Vous pouvez désormais accéder aux [fonctionnalités du groupe de notification d'Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) à l'aide de Braze ! Vous pouvez ajouter des arguments et des groupes récapitulatifs, utiliser les alertes critiques, filtrer les utilisateurs authentifiés provisoirement et voir les profils utilisateur qui ont un statut Authentifié Provisoirement.

## Période creuse

Les clients peuvent désormais spécifier des [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (pendant lesquelles vos messages ne seront pas envoyés) pour Canvas. Il vous suffit de vous rendre dans les **paramètres d'envoi de Canvas** et de cocher la case "Activer les heures calmes". Puis sélectionnez vos Heures calmes dans l’heure locale de vos utilisateurs et l’action qui suivra si le message se déclenche pendant ces heures calmes.

Les campagnes utilisent désormais les périodes creuses plutôt que « envoyer ce message à un moment spécifique de la journée ».

## Clients d’Adjust

Les clients de Braze qui utilisent [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) sont désormais en mesure de voir leur clé API et leur URL d'instance Braze, qu'ils utiliseront ensuite dans la plateforme Adjust pour s'intégrer.

## Filtre « Pas dans le segment »

Les clients peuvent désormais créer un segment à partir des utilisateurs qui [ne sont pas inclus dans un certain segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportations des destinataires Canvas sur CSV 

Les clients peuvent désormais [exporter des données]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/) sur les utilisateurs qui ont saisi un Canvas. Le fichier CSV généré sera similaire à celui de la campagne.

## Filtre de segmentation « iOS 12 » autorisé provisoirement

Un [filtre de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) permettant de trouver les utilisateurs provisoirement autorisés sur iOS 12 pour une app donnée a été ajouté.

## Chargeur d’images pour les messages in-app

Le chargeur d’images pour les messages in-app a été déplacé du panneau de conception vers le panneau de composition.

## Autorisations en lecture seule sur la page User Profile (Profil utilisateur)

Avant cette version, les clients pouvaient modifier le statut de l'abonnement et l'adresse e-mail dans le profil utilisateur avec des [autorisations en lecture seule.]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) Nous avons renommé l’autorisation `import_user` en autorisation `import_and_update_user` et restreint l’accès au statut d’abonnement et à l’adresse e-mail. Désormais si un développeur imite le mode lecture seule ou n’a pas cette autorisation, il ne peut pas modifier le statut d’abonnement ou l’adresse e-mail.
