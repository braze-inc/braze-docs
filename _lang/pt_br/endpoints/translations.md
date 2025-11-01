---
nav_title: Traduções
article_title: Endpoints de Tradução
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Esta landing page lista os endpoints de tradução da Braze."
page_type: landing

guide_top_header: "Endpoints de Tradução"
guide_top_text: "Use os endpoints de tradução da Braze para gerenciar e atualizar traduções em suas campanhas e canvas."

guide_featured_title: "Pontos finais da campanha"
guide_featured_list:
  - name: "OBTER: Exibir tradução para uma campanha"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "OBTER: Ver todas as traduções de uma campanha"
    link: /docs/api/endpoints/translations/campaigns/get_bulk_translations_campaigns/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar Tradução em uma Campanha"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "OBTER: Ver Tradução para uma Canva"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "OBTER: Exibir todas as traduções de um Canvas"
    link: /docs/api/endpoints/translations/canvas/get_bulk_translations_canvases/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Atualizar a conversão em uma tela"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  
guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "OBTER: Exibir tradução da fonte"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "OBTER: Exibir tradução e local específicos"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: Ver todas as traduções e localidades"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Atualizar traduções em um modelo de e-mail"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
Os endpoints de tradução do Braze estão atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Como funcionam nossos endpoints de tradução

Nossos endpoints de tradução funcionam com [composição multilíngue]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), em que uma mensagem pode ter versões diferentes que podem ser renderizadas dependendo do usuário que recebe a mensagem.

### Pré-requisitos

Antes de usar esses endpoints, você deve [adicionar suas localidades]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### Como testar suas traduções

Há duas maneiras de validar o suporte à tradução usando a API e o painel do Braze em campanhas, Canvases (incluindo etapas individuais) e modelos de e-mail:

- Durante a composição (antes do lançamento)
- Após o lançamento (usando rascunhos pós-lançamento)

Antes de testar a atualização das traduções, você deve:

1. [Adicione suas localidades]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Crie uma mensagem e use tags de tradução quando apropriado.
3. Salvar a mensagem.
4. Selecione as localidades a serem incluídas.
