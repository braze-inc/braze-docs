---
nav_title: Supprimer des utilisateurs via l’API
article_title: Supprimer des utilisateurs via l’API
page_order: 0

page_type: reference
description: "Cet article d’aide décrit les implications de la suppression d’un profil utilisateur via l’API REST de Braze."
tool: Tableau de bord
platform: API
---

# Supprimer des utilisateurs via l’API

Lorsque vous [supprimez un utilisateur via l’API REST de Braze][1], les événements suivants se produisent :

- Le nombre de [Lifetime Users][2] (Utilisateurs à vie) sera mis à jour pour tenir compte des utilisateurs supprimés.	
- Le profil utilisateur complet sera supprimé.	
- L’utilisateur supprimé comptera toujours vers le pourcentage de conversion agrégé. Les compteurs d’événements personnalisés et d’achat ne seront pas mis à jour pour les utilisateurs supprimés.

Après la suppression d’un utilisateur, Braze ne conserve aucune des données suivantes :
- Tous les attributs de l’utilisateur
- Adresse e-mail
- Numéro de téléphone
- ID utilisateur externe 
- Genre
- Pays
- Langue
- D’autres données similaires

## Plusieurs profils avec une adresse e-mail partagée

Supposons que vous souhaitiez fusionner plusieurs profils d’utilisateurs partageant la même adresse e-mail. 

Pour fusionner ces profils utilisateur :

 1. Identifiez tous les utilisateurs avec des adresses e-mail en double. 
 2. Exportez tous les attributs d’un seul profil. 
 3. Importez ces attributs dans le profil utilisateur via API ou CSV. 
 4. Supprimez les utilisateurs via API, en supprimant essentiellement ces utilisateurs en double et les données décrites ci-dessus.

_Dernière mise à jour le 24 octobre 2022_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users