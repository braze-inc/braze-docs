---
nav_title: Julho
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão de julho de 2017."
---

# Julho de 2017

## Imagens grandes em web push

Adicionamos suporte para imagens grandes para web push no Chrome para Windows e Android, oferecendo capacidade de criar experiências ricas e envolventes para os clientes. Saiba mais sobre [web push][58].

## Atualizações nos campos de e-mail

Agora você pode bloquear e-mails para um conjunto específico de endereços de remetente, garantindo que você não insira acidentalmente o endereço errado. O formulário de composição de e-mail será pré-preenchido com endereços usados nos últimos 6 meses para agilizar o processo. Confira as [melhores práticas de e-mail][57] para saber mais.

## Atualizações na API de detalhes da campanha

O endpoint `/campaign/details` agora oferece informações sobre suas mensagens, permitindo que você obtenha campos de assunto, corpo HTML, endereço de remetente e resposta usando a API. Saiba mais sobre as [APIs do Braze][56].

## Atualizações para a modelagem Liquid

Adicionamos a capacidade de criar modelos de atributos das variantes em canvas e campanhas. No canva, você pode agora modelar tanto o id da API da variante quanto o nome da variante, e em campanhas você pode agora modelar a `message_api_id` e `message_name` de uma mensagem. Ambas as atualizações permitem mais flexibilidade no seu envio de mensagens para que você crie campanhas personalizadas. Saiba mais sobre [envio de mensagens personalizado][55].

## Novo editor de e-mail em HTML

Agora você pode escrever e testar e-mails facilmente com um editor de HTML em tela cheia que permite prévia ao vivo, personalização via Liquid e um editor de texto em tela cheia aprimorado com números de LINE e realce de sintaxe. Saiba mais sobre a [composição de e-mail][54].

## Atualizações para pré-visualizações

Agora você pode seguir a janela da tela enquanto rola as visualizações de mensagens em campanhas e canvas, garantindo que você sempre possa ver as mudanças refletidas. Saiba mais sobre [visualização e teste][53].

## Novo filtro de associação de segmento

Adicionamos o filtro [Segment Membership][52], permitindo que você direcione usuários com base em sua associação em qualquer um dos seus segmentos existentes. Além disso, adicionamos a capacidade de usar tanto a lógica "E" quanto a lógica "Ou" nos filtros de segmento, bem como a capacidade de aninhar segmentos uns dentro dos outros. Essas atualizações ativar você a enviar mensagens personalizadas para seus clientes com mais precisão. 

## Atualizar para a prévia do Android

Atualizamos a [prévia do Android][51] para refletir versões mais recentes do Android desde o Android N.


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
