---
nav_title: septembre
page_order: 4
noindex: true
page_type: update
description: "Cet article contient les notes de version de septembre 2017."
---

# Septembre 2017

## Nouvelle fonctionnalité pour les rapports d'engagement

Vous pouvez désormais utiliser les [rapports d'engagement][72] pour regrouper les indicateurs d'une campagne sur des périodes spécifiques. Par exemple, vous pouvez exporter le nombre total d’ouvertures d’un trimestre ou le nombre total de clics de toute la durée de vie d’une campagne ou d’un Canvas. Tout ce que vous avez à faire, c’est :
- Sélectionner une période pour l’exportation des données,
- Planifier un rapport sur l’engagement envoyé régulièrement à un ou plusieurs destinataires, et
- Ajouter des campagnes et des Canvas à votre rapport en fonction de leurs balises.

## Mises à jour de la page de profil utilisateur

La [page du profil utilisateur][73] a été mise à jour.

## Notifications push Web nécessitant une action de l’utilisateur pour le rejet

Vous pouvez maintenant configurer le comportement de fermeture des messages push Web sur Chrome de façon à exiger que le destinataire interagisse avec le message pour pouvoir se désabonner. Cette fonctionnalité nécessite la version 1.6.13 ou ultérieure du SDK Web.

## Accroches d’e-mail

Lors de la création d'un message e-mail dans Braze, vous pouvez désormais facilement insérer un accroche dans la section **Info d'envoi.** 

## Nouvel endpoint de l’API pour l’exportation d’événements bruts

Nous avons ajouté un nouvel [endpoint API][71], /raw_data/status, qui vous permet de vérifier si un jour donné a été chargé dans l'exportation d'événements bruts. Vous pouvez l’utiliser pour vérifier si les données brutes d’un jour particulier sont disponibles, pour faciliter le débogage et l’automatisation.



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
