---
nav_title: Teste de banners
article_title: Teste de banners
page_order: 2
description: "Saiba como testar sua mensagem de banner antes de lançar sua campanha para garantir que toda a mídia, cópia, personalização e atributos personalizados sejam renderizados corretamente."
channel:
  - banners
noindex: true
---

# Teste de banners

> Saiba como testar sua mensagem de banner antes de lançar sua campanha para garantir que toda a mídia, cópia, personalização e atributos personalizados sejam renderizados corretamente. Para saber mais sobre informações gerais, consulte [Sobre banners]({{site.baseurl}}/developer_guide/banners).

## Pré-requisitos

Antes de testar o envio de mensagens de banner no Braze, você precisará criar uma [campanha de banner no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/). Além disso, verifique se o posicionamento que deseja testar já está [colocado em seu app ou site]({{site.baseurl}}/developer_guide/banners/creating_placements). 

Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado nos dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio.

## Teste de um banner

{% multi_lang_include banners/testing.md page="testing" %}
