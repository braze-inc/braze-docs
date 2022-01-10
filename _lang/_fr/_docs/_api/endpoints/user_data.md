---
nav_title: Données de l'utilisateur
article_title: Points de terminaison des données utilisateur
search_tag: Endpoint
page_order: 6
local_redirect:  #event-object-specification #purchase-object-specification
  event-object-specification: '/fr/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/fr/docs/api/objects_filters/purchase_object/'
layout: dev_guide
#Required
description: "Cette page de destination explique et énumère les points de terminaison des données utilisateur de Braze."
page_type: atterrissage
guide_top_header: "Points de terminaison des données utilisateur"
guide_top_text: "L'API utilisateur vous permet de suivre les informations sur vos utilisateurs en enregistrant les données sur vos utilisateurs provenant de l'extérieur de votre application mobile. Vous pouvez également utiliser cette API pour supprimer des utilisateurs à des fins de test ou autres. <br> <br> Tous les points de terminaison de l'API ont une limite de charge utile de données de 4 Mo. Les tentatives d'afficher plus de données que 4 Mo échoueront avec une entité de requête HTTP 413 trop grande. <br> <br> Les exemples ci-dessous contiennent l'URL https://rest.iad-01.braze. om, mais certains clients devront utiliser une URL de terminaison différente, par exemple si vous êtes hébergé dans le centre de données européen de Braze ou si vous avez une installation dédiée à Braze. Votre gestionnaire de succès vous informera si vous devez utiliser une URL de terminaison différente."
guide_featured_title: "Points de terminaison des données utilisateur"
guide_featured_list:
  - 
    name: "POST: Créer un nouvel alias d'utilisateur"
    link: /fr/docs/api/endpoints/user_data/post_user_alias/
    fa_icon: fas fa-user
  - 
    name: "POST: Supprimer les données utilisateur"
    link: /fr/docs/api/endpoints/user_data/post_user_delete/
    fa_icon: fas fa-user-minus
  - 
    name: "POST: Identifier un utilisateur"
    link: /fr/docs/api/endpoints/user_data/post_user_identify/
    fa_icon: fas fa-users
  - 
    name: "POST: Piste utilisateur"
    link: /fr/docs/api/endpoints/user_data/post_user_track/
    fa_icon: fas fa-base de données
guide_menu_title: "Points de terminaison de migration d'ID externe"
guide_menu_list:
  - 
    name: "POST: Renommer les identifiants externes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - 
    name: "POST: Supprimer les identifiants externes obsolètes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---

