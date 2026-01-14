---
nav_title: "Suppression des utilisateurs via l'API"
article_title: "Suppression des utilisateurs via l'API"
page_order: 0

page_type: reference
description: "Cet article d'aide décrit les implications de la suppression d'un profil utilisateur via l'API REST de Braze."
tool: Dashboard
platform: API
---

# Suppression des utilisateurs via l'API

Lorsque vous [supprimez un utilisateur via l'API REST de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), les données suivantes sont supprimées (nulles) :
- Tous les attributs de l’utilisateur
- Adresse e-mail
- Numéro de téléphone
- ID utilisateur externe 
- Genre
- Pays
- Langue

Lorsque vous [supprimez un utilisateur via l'API REST de Braze]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), les événements suivants se produisent :
- Le profil utilisateur est supprimé (nulled).
- Le nombre d'[utilisateurs à vie]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) sera mis à jour pour tenir compte des nouveaux utilisateurs supprimés.	
- L'utilisateur supprimé sera toujours pris en compte dans le pourcentage de conversion agrégé. Les comptes d'événements personnalisés et les comptes d'achats ne seront pas mis à jour pour les utilisateurs supprimés.

## Plusieurs profils avec une adresse e-mail partagée

Supposons que vous souhaitiez fusionner plusieurs profils d’utilisateurs partageant la même adresse e-mail. 

Pour fusionner ces profils utilisateur :

 1. Identifiez tous les utilisateurs avec des adresses e-mail en double. 
 2. Exportez tous les attributs d’un seul profil. 
 3. Importez ces attributs dans le profil utilisateur via API ou CSV. 
 4. Supprimez les utilisateurs via l'API, en veillant de supprimer notamment les utilisateurs en double et les données décrites ci-dessus.

_Dernière mise à jour le 13 septembre 2023_

