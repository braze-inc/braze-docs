---
nav_title: Dados de usuários
article_title: Pontos de extremidade de dados de usuários
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "Essa landing page lista os endpoints de dados de usuários do Braze."
page_type: landing

guide_top_header: "Pontos de extremidade de dados de usuários"
guide_top_text: "Os endpoints Braze User Data permitem rastrear informações sobre seus usuários por meio do registro de dados de usuários que vêm de fora do seu app móvel. Também é possível usar essa API para excluir usuários para testes ou outros fins. <br> <br> Todos os endpoints da API têm um limite de carga útil de dados de 4 MB. As tentativas de publicar mais dados do que 4 MB falharão com uma mensagem HTTP 413 Request Entity Too Large. <br> <br> Os exemplos nesta seção contêm o URL https://rest.iad-01.braze.com, mas talvez seja necessário usar um URL de endpoint diferente (por exemplo, se você estiver hospedado no data center da Braze EU ou tiver uma instalação dedicada da Braze). Seu gerente de sucesso do cliente da Braze o informará se for necessário usar um URL de endpoint diferente."

guide_featured_title: "Pontos de extremidade de dados de usuários"
guide_featured_list:
  - name: "POST: Criar um novo alias de usuário"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Atualizar um alias de usuário"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Excluir dados de usuários"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Identificar um usuário"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Rastreamento de usuários"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Rastreamento de usuários (síncrono)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Mesclar usuários"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Renomear IDs externos"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remover IDs externas obsoletas"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
