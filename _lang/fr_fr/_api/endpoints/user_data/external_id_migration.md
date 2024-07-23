---
nav_title: Migration de l’ID externe
article_title: "Migration de l’ID externe"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "Cette page d’accueil explique et répertorie la fonction de migration de l’ID externe de Braze."
page_type: landing

guide_top_header: "Migration de l’ID externe"
guide_top_text: "L'API de migration d'ID externe vous permet de renommer les ID externes existants (en créant un nouvel ID principal et en désapprouvant l'ID existant) et de supprimer les ID obsolètes après la migration. <br><br> Nous avons conçu cette solution pour autoriser plusieurs ID externes afin de prendre en charge une période de migration au cours de laquelle les anciennes versions de vos applications encore disponibles et qui utilisent le schéma de dénomination d'ID externe précédent ne sont pas interrompues. Nous vous recommandons fortement de supprimer les identifiants externes obsolètes lorsque votre ancien schéma de dénomination n'est plus utilisé."

guide_featured_title: "Endpoints de migration de l’ID externe"
guide_featured_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
