---
nav_title: Testes de Banners
article_title: Testes de Banners
page_order: 2
description: "Aprenda a testar a mensagem do seu Banner antes de lançar sua campanha para garantir que todos os meios, textos, personalização e atributos personalizados sejam exibidos corretamente."
channel:
  - banners
noindex: true
---

# Testes de Banners

> Aprenda a testar a mensagem do seu Banner antes de lançar sua campanha para garantir que todos os meios, textos, personalização e atributos personalizados sejam exibidos corretamente. Para mais informações gerais, veja [Sobre Banners]({{site.baseurl}}/developer_guide/banners).

## Pré-requisitos

Antes de testar mensagens de Banner no Braze, você precisará criar uma [campanha de Banner no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/). Além disso, verifique se a colocação que você deseja testar já está [colocada em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements). 

Para enviar um teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, o push deve estar ativado nos dispositivos de teste com tokens por push válidos registrados para o usuário teste antes do envio.

## Testando um Banner

{% multi_lang_include banners/testing.md page="testing" %}
