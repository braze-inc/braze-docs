---
nav_title: Pixel de abertura de e-mail e rastreamento de cliques
article_title: Pixel de abertura de e-mail e rastreamento de cliques
page_order: 1
page_type: reference
description: "Este artigo de referência cobre como implementar rastreamento de pixel aberto e clique."

---

# Pixel de abertura de e-mail e rastreamento de cliques

> [Rastreamento de pixel aberto]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) e rastreamento de clique podem ser ativados ou desativados para cada perfil de usuário. Essa flexibilidade ajuda você a seguir as leis regionais de privacidade, onde um perfil de usuário individual pode indicar que não deseja mais ser rastreado.

## Ativação de pixel de abertura ou rastreamento de clique

Ao importar ou atualizar um perfil de usuário por meio de [API]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields), [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) ou [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/), dois campos estão disponíveis para modificação:

- `email_open_tracking_disabled`: Aceita `true` ou `false`. Defina para `false` para adicionar o pixel de rastreamento de abertura a todos os futuros e-mails enviados para este usuário. Disponível apenas para SparkPost e SendGrid.
- `email_click_tracking_disabled`: Aceita `true` ou `false`. Defina para `false` para adicionar rastreamento de cliques a todos os links dentro de um futuro e-mail, enviado para este usuário. Disponível apenas para SparkPost e SendGrid.

Para referência, esta informação é refletida no perfil do usuário no e-mail **Configurações de Contato**, localizado na guia **engajamento**.

![Campos de pixel de abertura de e-mail e rastreamento de clique na guia de rastreamento de engajamento do perfil de um usuário]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

