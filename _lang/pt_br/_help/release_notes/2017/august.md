---
nav_title: Agosto
page_order: 5
noindex: true
page_type: update
description: "Este artigo contém notas de versão de agosto de 2017."
---

# Agosto de 2017

## Atualização para botões de ação por push

Adicionamos suporte a [botões de ação por push][70] aos nossos pontos de extremidade de envio de mensagens da API REST.

## Atualização do modelo Liquid

Agora você pode [personalizar uma mensagem][69] com base em:
- O dispositivo para o qual foi enviado,
- ID do dispositivo,
- Operadora,
- IDFA,
- Modelo,
- SO e
- Plataforma

## Canvas disparado por API

Agora é possível disparar um [Canva][68] por meio de pontos de extremidade da API (enviar, programar, atualizar, excluir) que correspondem aos existentes para campanhas, o que permite automatizar e otimizar ainda mais o seu marketing.

## Botões de ação por push na Web

Adicionamos suporte para botões de ação por push no SDK da Web para o Chrome, o que permite aumentar o engajamento oferecendo aos usuários opções contextuais que simplificam suas vidas ocupadas. Confira as [práticas recomendadas para notificações por push][66].

## Novos pontos de extremidade da API

Expusemos novos endpoints da API, /email/hard_bounces, que permite extrair hard bounces por endereço de e-mail ou em um determinado intervalo de datas, e /messages/scheduled_broadcasts, que permite extrair o próximo horário de início de início de campanhas agendadas e entrada agendada em canvas. Esses novos pontos de extremidade permitem a personalização e a otimização adicionais de suas campanhas. Saiba mais sobre nossos [pontos de extremidade de API][65].

## Geofences

Adicionamos um novo recurso, geofences, que lhe permite disparar mensagens em tempo real quando os clientes entram e saem de áreas geográficas definidas, ativando uma comunicação personalizada e relevante com seus clientes. Saiba mais sobre [marketing local][64].

## Atualização do editor de e-mail

Adicionamos o preenchimento automático dinâmico ao nosso novo editor de e-mail, de modo que agora é possível preencher automaticamente os atributos e eventos personalizados reais de seus clientes ao usar o Liquid, facilitando sua vida. Saiba mais sobre as práticas recomendadas de e-mail no [Academy][63].

## Atualização para filtros de data

Adicionamos um filtro de data "nunca" para que você possa direcionar os clientes que nunca receberam ou interagiram com uma de suas mensagens, o que lhe permite ter listas de clientes limpas e garantir a entregabilidade dos e-mails. Saiba mais sobre [filtros][62].

## Atualização do Canva

Adicionamos porcentagens à parte superior de cada variante do Canva para que você possa ver rapidamente quais variantes têm melhor desempenho. Saiba mais sobre o [Canva][61].

## Canvas com seleção inteligente

Os canvas agora têm Intelligent Selection, permitindo que você teste seus canvas com mais eficiência. Saiba mais sobre nosso [Intelligence Suite][60].

## Atualização dos nomes de exibição de e-mail

Adicionamos suporte a caracteres UTF-8 especiais em nomes de exibição de e-mail, para que você possa criar e-mails ainda mais personalizados para seus clientes. Saiba mais sobre [as práticas recomendadas de e-mail][67].

## Agregação de CSV de relatórios de engajamento

Agora, é possível receber dados consolidados de cada campanha e de cada Canvas em dois arquivos separados, independentemente do número de campanhas ou Canvas selecionados, permitindo que você tenha todos os dados de que precisa, quando precisar. Saiba mais sobre [os relatórios de engajamento][59].

> Conforme observado em nossas [notas de versão de setembro de 2017]({{site.baseurl}}/help/release_notes/2017/september/), agora é possível agregar dados de um período específico, bem como agendar exportações para serem executadas de forma recorrente.


[59]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/
[60]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[61]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters
[63]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/locations_and_geofences/
[65]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[66]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[67]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[68]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[69]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[70]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_action_buttons/#how-to-use-action-buttons
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
