---
nav_title: Dezembro
page_order: 0
noindex: true
page_type: update
description: "Este artigo contém notas de versão para dezembro de 2021."
alias: "/help/release_notes/2022/january/"
---
# Dezembro de 2021

## Atualização para exportar usuários por endpoint de segmento

A partir de dezembro de 2021, as seguintes alterações entrarão em vigor para o [endpoint Exportar usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/):

1. O campo `fields_to_export` nessa solicitação da API será obrigatório. A opção de padrão para todos os campos será removida.
2. Os campos para `custom_events`, `purchases`, `campaigns_received` e `canvases_received` conterão apenas dados dos últimos 90 dias.

## Novas propriedades para eventos de engajamento com mensagens do Currents

Novas propriedades foram adicionadas para [eventos selecionados de engajamento com mensagens]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Essa atualização se aplica aos seguintes eventos de engajamento com mensagens do Currents e a todos os parceiros que os utilizam:

- Adicione `LINK_ID`, `LINK_ALIAS` a:
  - Clique no e-mail (todos os destinos)
- Adicionar `USER_AGENT` a:
  - Abertura de e-mail
  - Clique no e-mail
  - Marcar e-mail como spam
- Adicionar `MACHINE_OPEN` a:
  - Abertura de e-mail

## Nova tag de personalização Liquid

Agora, oferecemos suporte ao direcionamento de usuários que têm o push em primeiro plano ativado em seus dispositivos com as seguintes Liquid tags:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Para saber mais, consulte [Tags de personalização com suporte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Sobre webhooks

Os webhooks são ferramentas poderosas e flexíveis, mas podem ser um pouco confusos. Se estiver se perguntando o que são webhooks e como usá-los na Braze, confira nosso novo artigo sobre [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalize

O Amazon Personalize é como ter seu próprio sistema de recomendação de machine learning da Amazon o dia todo. Com base em mais de 20 anos de experiência em recomendações, o Amazon Personalize o capacita a melhorar o engajamento dos clientes, fornecendo recomendações personalizadas de produtos e conteúdo em tempo real e promoções de marketing direcionadas. 

Se quiser saber mais, visite nosso novo artigo sobre o [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize) para entender os casos de uso que o Amazon Personalize oferece, os dados com os quais ele trabalha, como configurar o serviço e como integrá-lo ao Braze.

## Novas parcerias Braze

### Yotpo - Comércio eletrônico

A integração entre o [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) e o Braze permite extrair e exibir dinamicamente classificações com estrelas, principais avaliações e conteúdo visual gerado pelo usuário sobre produtos em e-mails e outros canais de comunicação no Braze. Também é possível incluir dados de fidelidade no nível do cliente em e-mails e outros métodos de comunicação para criar uma interação mais personalizada, aumentando as vendas e a fidelidade.

### Zeotap - Plataforma de dados do cliente

Com a integração entre o [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) e o Braze, você pode ampliar a escala e o alcance de suas campanhas sincronizando os segmentos de clientes do Zeotap para mapear os dados de usuários do Zeotap para as contas de usuários do Braze. Em seguida, é possível agir com base nesses dados, oferecendo experiências de direcionamento personalizadas aos seus usuários.