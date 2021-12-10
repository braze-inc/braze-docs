---
nav_title: Septembre
page_order: 4
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour septembre 2017."
---

# Septembre 2017

## Nouvelles fonctionnalités pour les rapports d'engagement

Vous pouvez maintenant utiliser [Rapports d'engagement][72] pour agréger des métriques pour une campagne sur des périodes de temps spécifiques. Par exemple, vous pouvez exporter le nombre total d'ouvertures à partir d'un trimestre, ou le nombre total de clics de toute la durée de vie d'une campagne ou de Canvas. Tout ce que vous avez à faire est :
- Sélectionnez un intervalle de temps à partir duquel exporter les données,
- Planifier un rapport d'engagement qui envoie régulièrement à un ou plusieurs destinataires, et
- Ajoutez des campagnes et des Canvases à votre rapport en fonction de leurs tags.

## Mises à jour vers la page de profil de l'utilisateur

La [page de profil utilisateur][73] a été mise à jour.

## Notifications push Web qui nécessitent une action de l'utilisateur pour rejeter

Vous pouvez maintenant configurer le comportement de fermeture de message pour les pushes Web Chrome qui nécessitent que le destinataire interagisse avec le message afin qu'il soit rejeté. Cette fonctionnalité nécessite le Web SDK version 1.6.13 ou supérieure.

## Pré-en-têtes d'email

Lors de la création d'un message électronique dans Braze, vous pouvez maintenant facilement insérer un préen-tête dans la section « Infos d'envoi ».

## Nouveau point de terminaison API pour l'exportation d'événements bruts

Nous avons ajouté un nouveau [API endpoint][71], /raw_data/status, qui vous permet de demander si un jour donné a été chargé dans le Raw Event Export. Vous pouvez l'utiliser pour vérifier si des données brutes d'une journée particulière sont disponibles, pour aider au débogage et à l'automatisation.



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
