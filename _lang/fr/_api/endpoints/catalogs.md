---
nav_title: Catalogues
article_title: Endpoints des catalogues
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Cette page d’accueil répertorie les endpoints des catalogues de Braze."
page_type: landing

guide_top_header: "Endpoints des catalogues"
guide_top_text: "Utilisez les endpoints des catalogues de Braze pour ajouter, éditer et gérer vos catalogues et vos détails de produits du catalogue. Vous pouvez utiliser des endpoints de catalogue asynchrones pour faire des modifications en gros de votre catalogue. <br><br> Vous avez besoin d’aide pour créer un catalogue ? Consultez notre article consacré à <a href='/docs/user_guide/personalization_and_dynamic_content/catalog/'>la création et l’utilisation des catalogues</a>."

guide_featured_title: "Endpoints de gestion de catalogue<br><br>"
guide_featured_list:
  - name: "SUPPRIMER : Supprimer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
    fa_icon: fas fa-pen-square
  - name: "GET : Lister des catalogues"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
    fa_icon: fas fa-list-ul
  - name: "POST : Créer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
    fa_icon: fas fa-check

optional_guide_menu_title: "Endpoints des produits du catalogue"
guide_menu_title: "<h3>Asynchrone</h3>"
guide_menu_list:
  - name: "SUPPRIMER : Supprimer plusieurs endpoints des produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
    fa_icon: fas fa-clipboard-list
  - name: "CORRECTIF : Éditer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
    fa_icon: fas fa-user-edit
  - name: "POST : Créer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
    fa_icon: fas fa-check

guide_menu_title2: "<h3>Synchrone</h3>"
guide_menu_list2:  
  - name: "SUPPRIMER : Supprimer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
    fa_icon: fas fa-dot-circle
  - name: "GET : Lister les détails du produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
    fa_icon: fas fa-check-square
  - name: "GET : Lister les détails de plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
    fa_icon: fas fa-list-alt
  - name: "CORRECTIF : Éditer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
    fa_icon: fas fa-user-edit
  - name: "POST : Créer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
    fa_icon: fas fa-check-square


---