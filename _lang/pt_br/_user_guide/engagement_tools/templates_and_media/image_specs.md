---
nav_title: Especificações da imagem
article_title: Especificações da imagem
page_order: 4.1

page_type: reference
description: "Este artigo de referência descreve os tamanhos de imagem recomendados e as especificações para cada tipo de canal."
tool:
  - Templates
  - Media

---

# Especificações da imagem

> Em geral, imagens menores e de alta qualidade serão carregadas mais rapidamente, portanto, recomendamos usar o menor ativo possível para obter o resultado desejado. Para maximizar o uso de sua imagem em canais específicos, consulte os detalhes neste artigo.

Você deve sempre [visualizar e testar suas mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) em vários dispositivos para confirmar que as áreas mais importantes da sua imagem e mensagem aparecem conforme o esperado.

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagem de mensagem no aplicativo e sobreposições de zona de segurança foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Faça o download dos modelos de design ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

{% multi_lang_include image_specs.md variable_name='payload size' %}

## Mensagens no aplicativo

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

### Fonte incrível

O Braze suporta o uso da [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) para ícones de mensagens modais no aplicativo.

## Notificações push

{% multi_lang_include image_specs.md variable_name='push notifications' %}

## E-mail

{% multi_lang_include image_specs.md variable_name='email' %}

## Comportamento de imagem

{% multi_lang_include image_specs.md variable_name='image behavior' %}
