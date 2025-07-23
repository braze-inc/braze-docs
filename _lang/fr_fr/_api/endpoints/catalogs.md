---
nav_title: Catalogues
article_title: Endpoints des catalogues
page_order: 0
layout: dev_guide

search_tag: Endpoint
description: "Cette page d’accueil répertorie les endpoints des catalogues de Braze."
page_type: landing

guide_top_header: "Endpoints des catalogues"
guide_top_text: "Utilisez les endpoints des catalogues de Braze pour ajouter, modifier et gérer vos catalogues et vos détails de produits du catalogue. Pour les modifications en masse de votre catalogue, utilisez les endpoints de catalogue asynchrones. <br><br> Vous avez besoin d’aide pour créer un catalogue ? Consultez notre article consacré à <a href='/docs/user_guide/personalization_and_dynamic_content/catalog/'>la création et l’utilisation des catalogues</a>."

guide_featured_title: "Points d'extrémité pour la gestion du catalogue"
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

guide_menu_title2: "Asynchronous catalog items endpoints"
guide_menu_list2:
  - name: "DELETE : Supprimer plusieurs endpoints des produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
    image: /assets/img/braze_icons/edit-05.svg
  - name: "PATCH : Éditer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST : Créer plusieurs produits du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT : Mise à jour de plusieurs éléments du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title3: "Synchronous catalog items endpoints"
guide_menu_list3:  
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
  - name: "PUT : Remplacer l'article du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/
    image: /assets/img/braze_icons/user-circle.svg

guide_menu_title4: "Asynchronous catalog fields endpoints"
guide_menu_list4:
  - name: "POST : Créer des champs de catalogue"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE : Supprimer un champ du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title5: "Asynchronous catalog selections endpoints"
guide_menu_list5:
  - name: "POST : Créer des sélections dans le catalogue"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "DELETE : Supprimer la sélection du catalogue"
    link: /docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/
    image: /assets/img/braze_icons/edit-05.svg

---
