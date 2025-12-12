---
nav_title: Migración de ID externo
article_title: "Migración de ID externo"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "Esta página de inicio explica y enumera la característica de migración de ID externo de Braze."
page_type: landing

guide_top_header: "Migración de ID externo"
guide_top_text: "La API de migración de ID externo te permite cambiar el nombre de los ID externos existentes (creando un nuevo ID principal y eliminando el ID existente) y eliminar los ID obsoletos después de la migración. <br><br> Hemos diseñado esta solución para permitir múltiples ID externos con el fin de permitir un periodo de migración en el que no se rompan las versiones anteriores de tus aplicaciones que todavía estén en funcionamiento y que utilicen el esquema de nomenclatura ID externo anterior. Te recomendamos encarecidamente que elimines los ID externos obsoletos cuando tu antiguo esquema de nombres ya no esté en uso."

guide_featured_title: "Puntos finales de migración de ID externo"
guide_featured_list:
  - name: "POST: Renombrar identificadores externos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Eliminar identificadores externos obsoletos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
