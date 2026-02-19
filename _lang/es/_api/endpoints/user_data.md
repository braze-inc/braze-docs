---
nav_title: Datos de usuario
article_title: Puntos finales de datos de usuario
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "Esta página de destino enumera los puntos finales de datos de usuario de Braze."
page_type: landing

guide_top_header: "Puntos finales de datos de usuario"
guide_top_text: "Los puntos finales de datos de usuario Braze le permiten rastrear información sobre sus usuarios mediante el registro de datos sobre sus usuarios que proceden de fuera de su aplicación móvil. También puede utilizar esta API para eliminar usuarios con fines de prueba o de otro tipo. <br> <br> Todos los puntos finales de la API tienen un límite de carga útil de datos de 4 MB. Los intentos de publicar datos por encima de los 4 MB fallarán con un error HTTP «413 Request Entity Too Large». <br> <br> Los ejemplos de esta sección contienen la URL https://rest.iad-01.braze.com, pero puede que necesite utilizar una URL de punto final diferente (por ejemplo, si está alojado en el centro de datos Braze EU o tiene una instalación Braze dedicada). Tu administrador del éxito del cliente de Braze te informará si debes utilizar una URL de punto final diferente."

guide_featured_title: "Puntos finales de datos de usuario"
guide_featured_list:
  - name: "POST: Crear un nuevo alias de usuario"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Actualizar un alias de usuario"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Borrar datos de usuario"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Identificar un usuario"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Seguimiento de usuarios"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "PUBLICAR: Seguimiento de usuarios (sincrónico)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "PUBLICAR: Fusionar usuarios"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Renombrar identificadores externos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Eliminar identificadores externos obsoletos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
