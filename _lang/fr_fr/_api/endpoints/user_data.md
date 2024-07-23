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
guide_top_text: "Les points de terminaison Braze User Data vous permettent de suivre les informations sur vos utilisateurs en enregistrant des données sur vos utilisateurs provenant de l’extérieur de votre application mobile. Vous pouvez également utiliser cette API pour supprimer des utilisateurs à des fins de test ou à d’autres fins. <br> <br> Tous les points de terminaison d’API ont une limite de charge utile de données de 4 MO. Toute tentative de publier plus de 4 Mo de données échouera avec une entité de requête HTTP 413 trop grande. <br> <br> Les exemples de cette section contiennent l’URL https://rest.iad-01.braze.com, mais vous devrez peut-être utiliser une URL d’endpoint différente (par exemple, si vous êtes hébergé dans le centre de données Braze EU ou si vous disposez d’une installation Braze dédiée). Votre gestionnaire du succès des clients Braze vous informera si vous devez utiliser une URL d’endpoint différente."

guide_featured_title: "Endpoints des données utilisateur"
guide_featured_list:
  - name: "POST: Create a New User Alias"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Update a User Alias"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Delete User Data"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Identify a User"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Track Users"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Merge Users"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
