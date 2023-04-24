---
nav_title: Données utilisateur
article_title: Endpoints des données utilisateur
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "Cette page d’accueil explique et répertorie les endpoints Braze de données utilisateur."
page_type: renvoi

guide_top_header: "Endpoints des données utilisateur"
guide_top_text: "L’API utilisateur vous permet de suivre les informations sur vos utilisateurs en enregistrant des données les concernant qui proviennent de l’extérieur de votre application mobile. Vous pouvez également utiliser cette API pour supprimer des utilisateurs à des fins de test ou autres. <br> <br> Tous les endpoints d’API ont une limite de charge utile de 4 Mo. Les tentatives de publication de données de plus de 4 Mo échoueront avec une entité de demande HTTP 413 trop grande. <br> <br> Les exemples suivants contiennent l’URL https://rest.iad-01.braze.com, mais certains clients devront utiliser une URL d’endpoint différente, par exemple si vous êtes hébergé dans le centre de données européen de Braze ou si vous avez une installation de Braze dédiée. Votre gestionnaire du succès vous informera si vous devez utiliser une URL d’endpoint différente."

guide_featured_title: "Endpoints des données utilisateur"
guide_featured_list:
  - name: "POST: Créer un nouvel alias utilisateur"
    link: /docs/api/endpoints/user_data/post_user_alias/
    fa_icon: fas fa-user
  - name: "POST : Mettre à jour un alias d’utilisateur"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    fa_icon: fas fa-user-edit
  - name: "POST: Supprimer les données utilisateur"
    link: /docs/api/endpoints/user_data/post_user_delete/
    fa_icon: fas fa-user-minus
  - name: "POST: Identifier un utilisateur"
    link: /docs/api/endpoints/user_data/post_user_identify/
    fa_icon: fas fa-user-circle
  - name: "POST: Suivi utilisateur"
    link: /docs/api/endpoints/user_data/post_user_track/
    fa_icon: fas fa-database
  - name: "POST: Fusion d’utilisateurs"
    link: /docs/api/endpoints/user_data/post_users_merge/
    fa_icon: fas fa-users

guide_menu_title: "Endpoints de migration de l’ID externe"
guide_menu_list:
  - name: "POST: Renommer des ID externes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - name: "POST: Supprimer les ID externes obsolètes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---
