---
nav_title: Migração de ID externa
article_title: "Migração de ID externa"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "Esta landing page explica e lista o recurso de migração de ID externo do Braze."
page_type: landing

guide_top_header: "Migração de ID externa"
guide_top_text: "A API de migração de ID externo permite que você renomeie os IDs externos existentes (criando um novo ID primário e descontinuando o ID existente) e remova IDs descontinuados após a migração. <br><br> Projetamos essa solução para permitir vários IDs externos a fim de dar suporte a um período de migração em que as versões mais antigas de seus apps que ainda estão em uso e que usam o esquema de nomenclatura de ID externo anterior não sejam interrompidas. É altamente recomendável remover IDs externas obsoletas quando o esquema de nomenclatura antigo não estiver mais em uso."

guide_featured_title: "Pontos de extremidade de migração de ID externa"
guide_featured_list:
  - name: "POST: Renomear IDs externos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remover IDs externas obsoletas"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
