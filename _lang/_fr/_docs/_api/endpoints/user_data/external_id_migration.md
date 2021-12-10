---
nav_title: Migration d'ID externe
article_title: "Migration d'ID externe"
search_tag: Endpoint
page_order: 5
layout: dev_guide
description: "Cette page d'accueil explique et liste la fonction de migration des identifiants externes de Braze."
page_type: atterrissage
guide_top_header: "Migration d'ID externe"
guide_top_text: "L'API de migration d'ID externe vous permet de renommer les identifiants externes existants (création d'un nouvel ID primaire et dépréciation de l'ID existant) et de supprimer la post-migration des identifiants obsolètes. <br><br> Nous avons conçu cette solution pour permettre de multiples identifiants externes afin de supporter une période de migration dans laquelle les anciennes versions de vos applications encore dans le sauvage qui utilisent le schéma de nommage d'ID externe précédent ne se casseront pas. Nous vous recommandons fortement de supprimer les identifiants externes obsolètes une fois que votre ancien schéma de nommage n'est plus utilisé."
guide_featured_title: "Points de terminaison de migration d'ID externe"
guide_featured_list:
  - 
    name: "POST: Renommer les identifiants externes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - 
    name: "POST: Supprimer les identifiants externes obsolètes"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---

