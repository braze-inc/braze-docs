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
description: "Cette page d’accueil liste les endpoints Braze de données utilisateur."
page_type: landing

guide_top_header: "Endpoints des données utilisateur"
guide_top_text: "Les endpoints de données utilisateur de Braze vous permettent de suivre les informations sur vos utilisateurs en enregistrant des données les concernant qui proviennent de l'extérieur de votre application mobile. Vous pouvez également utiliser cette API pour supprimer des utilisateurs à des fins de test ou autres. <br> <br> Tous les endpoints de l'API ont une limite de 4 Mo de données. Les tentatives d'envoi de plus de 4 Mo de données échoueront avec un message HTTP 413 Request Entity Too Large. <br> <br> Les exemples de cette section contiennent l'URL https://rest.iad-01.braze.com, mais il se peut que vous deviez utiliser une URL d'endpoint différente (par exemple, si vous êtes hébergé dans le centre de données européen de Braze ou si vous disposez d'une installation Braze dédiée). Votre gestionnaire du succès des clients Braze vous informera si vous devez utiliser une URL d’endpoint différente."

guide_featured_title: "Endpoints des données utilisateur"
guide_featured_list:
  - name: "POST : Créer un nouvel alias utilisateur"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : Mise à jour d'un alias d'utilisateur"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : Supprimer les données utilisateur"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST : Identifier un utilisateur"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST : Suivre les utilisateurs"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST : Suivi des utilisateurs (synchrone)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST : Fusionner les utilisateurs"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST : Renommer des ID externes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : Supprimer les ID externes obsolètes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
