---
nav_title: Catalogues
article_title: Endpoints des catalogues
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Cette page d’accueil répertorie les endpoints des catalogues de Braze."
page_type: landing

guide_top_header: "Endpoints des catalogues"
guide_top_text: "Utilisez les endpoints des catalogues de Braze pour ajouter, modifier et gérer vos catalogues et vos détails de produits du catalogue. Pour les modifications en bloc apportées à votre catalogue, utilisez les points de terminaison de catalogue asynchrones. <br><br> Vous cherchez des conseils sur la création d’un catalogue ? Consultez notre article consacré à <a href='/docs/user_guide/personalization_and_dynamic_content/catalog/'>la création et l’utilisation de catalogues</a>."

guide_featured_title: "Points de terminaison de gestion de catalogue<br><br>"
guide_featured_list:
  - name: "DELETE: Delete Catalog"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: List Catalogs"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Create Catalog"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
    image: /assets/img/braze_icons/check-square-broken.svg

optional_guide_menu_title: "Catalog items endpoints"
guide_menu_title: "<h3>Asynchronous</h3>"
guide_menu_list:
  - name: "DELETE: Delete Multiple Catalog Items Endpoints"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH: Edit Multiple Catalog Items"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Create Multiple Catalog Items"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Update Multiple Catalog Items"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title2: "<h3>Synchronous</h3>"
guide_menu_list2:  
  - name: "DELETE: Delete Catalog Item"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET: List Catalog Item Details"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: List Multiple Catalog Item Details"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH: Edit Catalog Item"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Create Catalog Item"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Update Catalog Item"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/
    image: /assets/img/braze_icons/user-circle.svg


---