---
nav_title: Migration de l’ID externe
article_title: "Migration de l’ID externe"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "Cette page d’accueil explique et répertorie la fonction de migration de l’ID externe de Braze."
page_type: landing

guide_top_header: "Migration de l’ID externe"
guide_top_text: "L’API de migration de l’ID externe vous permet de renommer des ID externes existants (création d’un nouvel ID principal et suppression de l’ID existant) et suppression des ID obsolètes après la migration. <br><br> Nous avons conçu cette solution pour autoriser plusieurs ID externes afin de prendre en charge une période de migration pendant laquelle les versions antérieures de vos applications encore existantes qui utilisent l’ancien schéma de nommage des ID externes ne s’interrompent pas. Nous vous recommandons vivement de supprimer les ID externes obsolètes une fois que votre ancien schéma de nommage n’est plus utilisé."

guide_featured_title: "Endpoints de migration de l’ID externe"
guide_featured_list:
  - name: "POST : renommer des ID externes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : supprimer les ID externes obsolètes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
