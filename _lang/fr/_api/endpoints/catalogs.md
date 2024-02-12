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
  - name: "DELETE : Supprimer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET : Lister des catalogues"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
    image: /assets/img/braze_icons/list.svg
  - name: "POST : Créer un catalogue"
    link: /docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
    image: /assets/img/braze_icons/check-square-broken.svg

optional_guide_menu_title: "Endpoints des produits du catalogue"
guide_menu_title: "<h3>Asynchrone</h3>"
guide_menu_list:
  - name: "DELETE : Supprimer plusieurs endpoints des produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH : Éditer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : créer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT : créer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title2: "<h3>Synchrone</h3>"
guide_menu_list2:  
  - name: "DELETE : Supprimer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "GET : Lister les détails du produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
    image: /assets/img/braze_icons/list.svg
  - name: "GET : Lister les détails de plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
    image: /assets/img/braze_icons/list.svg
  - name: "PATCH : Éditer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : Créer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT : Créer un produit du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/
    image: /assets/img/braze_icons/user-circle.svg


---