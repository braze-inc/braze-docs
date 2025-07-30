---
nav_title: Rastreamento de clique e pixel de abertura de e-mail
article_title: Rastreamento de clique e pixel de abertura de e-mail
page_order: 1
page_type: reference
description: "Este artigo de referência cobre como implementar rastreamento de pixel aberto e clique."

---

# Pixel de abertura de e-mail e rastreamento de cliques

> [Rastreamento de pixel aberto]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) e rastreamento de clique podem ser ativados ou desativados para cada perfil de usuário. Essa flexibilidade ajuda você a seguir as leis regionais de privacidade, onde um perfil de usuário individual pode indicar que não deseja mais ser rastreado.

## Ativação de pixel de abertura ou rastreamento de clique

Ao importar ou atualizar um perfil de usuário via [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) ou [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv), dois campos estão disponíveis para você modificar:

- `email_open_tracking_disabled`: Aceita `true` ou `false`. Defina para `false` para adicionar o pixel de rastreamento de abertura a todos os futuros e-mails enviados para este usuário. Disponível apenas para SparkPost e SendGrid.
- `email_click_tracking_disabled`: Aceita `true` ou `false`. Defina para `false` para adicionar rastreamento de cliques a todos os links dentro de um futuro e-mail, enviado para este usuário. Disponível apenas para SparkPost e SendGrid.

Para referência, esta informação é refletida no perfil do usuário no e-mail **Configurações de Contato**, localizado na guia **engajamento**.

![Campos de pixel de rastreamento de abertura e clique de e-mail na guia Engajamento do perfil de um usuário]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

