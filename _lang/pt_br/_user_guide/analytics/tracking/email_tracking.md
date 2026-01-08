---
nav_title: Pixel de abertura de e-mail e rastreamento de cliques
article_title: Pixel de abertura de e-mail e rastreamento de cliques
page_order: 1
page_type: reference
description: "Este artigo de referência aborda como implementar o pixel aberto e o rastreamento de cliques."

---

# Pixel de abertura de e-mail e rastreamento de cliques

> O [rastreamento de pixel aberto]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) e o rastreamento de cliques podem ser ativados ou desativados para cada perfil de usuário. Essa flexibilidade ajuda a seguir as leis de privacidade regionais, em que um perfil de usuário individual pode indicar que não deseja mais ser rastreado.

## Ativação do pixel aberto ou do rastreamento de cliques

Ao importar ou atualizar um perfil de usuário via [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) ou [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), dois campos estão disponíveis para modificação:

- `email_open_tracking_disabled`: Aceita `true` ou `false`. Defina como `false` para adicionar o pixel de rastreamento de abertura a todos os futuros e-mails enviados a esse usuário. Disponível apenas para SparkPost e SendGrid.
- `email_click_tracking_disabled`: Aceita `true` ou `false`. Defina como `false` para adicionar rastreamento de cliques a todos os links em um e-mail futuro enviado a esse usuário. Disponível apenas para SparkPost e SendGrid.

Para referência, essas informações são refletidas no perfil do usuário no e-mail **Contact Settings (Configurações de contato**), localizado na guia **Engagement (Engajamento** ).

Campos de pixel de rastreamento de cliques e abertura de e-mail na guia Envolvimento do perfil de um usuário]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

