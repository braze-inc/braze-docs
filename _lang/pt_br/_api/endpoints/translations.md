---
nav_title: Traduções
article_title: Endpoints de Tradução
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta landing page lista os endpoints de tradução da Braze."
page_type: landing

guide_top_header: "Endpoints de Tradução"
guide_top_text: "Use os endpoints de tradução do Braze para gerenciar e atualizar traduções em suas campanhas, canvases e blocos de conteúdo."

guide_featured_title: "Endpoints de campanha"
guide_featured_list:
  - name: "OBTER: Exibir tradução para uma campanha"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar Tradução em uma Campanha"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: Ver traduções padrão da campanha"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "OBTER: Ver tradução para uma canva"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar a conversão em uma tela"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: Ver traduções padrão do canvas"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "OBTER: Ver traduções padrão do template de e-mail"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "OBTER: Ver tradução e localidade específicas"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: Ver todas as traduções e localidades"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Atualizar traduções em um template de e-mail"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Content Block endpoints"
guide_menu_list3:
  - name: "OBTER: Ver todas as traduções para um bloco de conteúdo"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar tradução em um bloco de conteúdo"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block/
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## Como funcionam nossos endpoints de tradução

Nossos endpoints de tradução funcionam com [composição multilíngue]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), onde uma mensagem pode ter diferentes versões que podem ser renderizadas dependendo do usuário que recebe a mensagem.

### Pré-requisitos

Antes de usar esses endpoints, você deve [adicionar suas localidades]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### Como testar suas traduções

Existem duas maneiras de validar o suporte à tradução usando a API e o dashboard do Braze em campanhas, canvases (incluindo etapas individuais), blocos de conteúdo e templates de e-mail:

- Durante a composição (antes do lançamento)
- Após o lançamento (usando rascunhos pós-lançamento)

Antes de testar a atualização de traduções, você deve:

1. [Adicionar suas localidades]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Criar uma mensagem e usar tags de tradução onde apropriado.
3. Salve a mensagem.
4. Selecione os locais a serem incluídos.
