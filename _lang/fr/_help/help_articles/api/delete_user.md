---
nav_title: Supprimer des utilisateurs via l’API
article_title: Supprimer des utilisateurs via l’API
page_order: 0

page_type: reference
description: "Cet article décrit les implications de la suppression d’un profil utilisateur via l’API REST de Braze."
tool: Dashboard
platform: API
---

# Suppression d’utilisateurs via l’API

Lorsque vous [supprimez un utilisateur via l’API REST de Braze][1], les événements suivants se produisent :

- Le nombre de [Lifetime Users][2] (Utilisateurs à vie) sera mis à jour pour tenir compte des utilisateurs supprimés.	
- Le profil utilisateur complet sera supprimé.	
- L’utilisateur supprimé comptera toujours vers le pourcentage de conversion agrégé. Les compteurs d’événements personnalisés et d’achat ne seront pas mis à jour pour les utilisateurs supprimés.	

_Dernière mise à jour le 8 octobre 2019_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/#lifetime-users