---
nav_title: Rastreamento de cliques
article_title: Rastreamento de cliques
page_order: 3
description: "Este artigo de referência cobre como ativar o rastreamento de cliques em suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e mais."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Rastreamento de cliques

> Esta página cobre como ativar o rastreamento de cliques em suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e mais.

O rastreamento de cliques permite medir quando alguém toca em um link na sua mensagem do WhatsApp, dando uma visão clara sobre qual conteúdo está gerando engajamento. O Braze encurta seus URLs, adiciona rastreamento nos bastidores e registra eventos de cliques à medida que acontecem.

Você pode ativar o rastreamento de cliques em mensagens de resposta e de modelo. Funciona com links em botões e texto do corpo, e suporta URLs personalizadas e domínios personalizados. Depois de ativado, você verá dados de cliques em seus relatórios de desempenho do WhatsApp e poderá segmentar usuários com base em quem clicou em quê.

{% alert note %}
O rastreamento de cliques não funciona com links profundos. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas o Braze não pode solucionar problemas que possam surgir ao fazer isso (como quebrar a atribuição ou causar um redirecionamento).
{% endalert %}

## Como funciona?

### Envio de mensagens de resposta 

Para configurar o rastreamento de cliques para mensagens de resposta:
1. Crie uma mensagem de resposta que inclua um botão de chamada para ação (CTA) com um URL de site.
2. Ative o rastreamento de cliques clicando no botão designado na interface.

O link será encurtado para o domínio do Braze, ou o domínio personalizado especificado para o grupo de inscrições, e personalizado para o usuário.

Todos os URLs estáticos que começam com `http://` ou `https://` serão encurtados. URLs encurtados que contêm personalização Liquid (como direcionamento de rastreamento em nível de usuário) serão válidos por dois meses.

![Criador de mensagens do WhatsApp com corpo de conteúdo e um botão.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Envio de mensagens de modelo 

Para mensagens de modelo, a URL base deve ser enviada corretamente ao criar o modelo para ativar o rastreamento de cliques.

#### Etapa 1: Crie um modelo suportado por rastreamento de cliques no WhatsApp

1. No seu Gerenciador do WhatsApp, crie uma URL base que seja seu domínio personalizado ou `brz.ai`.
2. Certifique-se de que os links incluídos no modelo sejam compatíveis com o rastreamento de cliques.
3. Não altere as variáveis do modelo depois que ele estiver configurado como uma campanha no Braze; alterações posteriores não podem ser incorporadas.
4. Para links de botões CTA, selecione **Dinâmico**, e depois forneça a URL base (`brz.ai` ou seu domínio personalizado).<br><br>![Seção para criar um chamado à ação.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Para links no texto do corpo, ao escrever o modelo no seu Gerenciador de WhatsApp, remova quaisquer espaços inseridos para links contidos no corpo que você deseja rastrear.<br><br>![Caixa de texto para inserir o conteúdo do corpo para o chamado à ação.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Etapa 2: Complete seu modelo no Braze

Ao compor, o Braze detectará automaticamente quais modelos têm domínios de URL suportáveis, tanto no texto do corpo quanto para os botões de CTA. O status será exibido na parte inferior do modelo. 

![Seção "Status do Link" mostrando um status ativo para rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Links suportados:** Links que são enviados com a URL base correspondente terão o rastreamento de cliques ativado.
- **Links parcialmente suportados:** Se alguns links em um modelo forem enviados como URLs completas, o rastreamento de cliques **não** será aplicado a esses links.
- **Links não suportados:** Links sem uma URL base aprovada **não** têm capacidades de rastreamento de cliques.

A URL de destino precisará ser fornecida para qualquer link com uma URL base que corresponda a `brz.ai` ou ao seu domínio personalizado. 

![Seção "Botões" com campos para um nome de botão, URL do site e URL de rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Enviando mensagens de modelo via API**: O rastreamento de cliques do WhatsApp (usando `brz.ai` ou um domínio de rastreamento personalizado e o campo **URL de rastreamento de cliques** no criador de mensagens) não é suportado ao enviar mensagens de modelo do WhatsApp através do [`/messages/send` ponto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/).

Se você enviar uma mensagem de modelo através da API, pode preencher variáveis de URL de CTA (usando `button_variables`), mas o Braze não gera uma URL de rastreamento de cliques ou link de redirecionamento no fluxo de solicitação da API. Para usar o rastreamento de cliques, envie o modelo do painel do Braze ou através de um gatilho de campanha do Braze.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Personalização Liquid em URLs

Você pode construir dinamicamente seu URL diretamente no criador do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar aos usuários links exclusivos (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).
URLs podem ser geradas dinamicamente através do uso de quaisquer tags de personalização Liquid suportadas.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também suportamos a abreviação de variáveis Liquid definidas pelo usuário, como nos seguintes exemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Encurtar URLs renderizados por variáveis Liquid

A Braze encurta URLs que são renderizadas pelo Liquid, mesmo aquelas incluídas em propriedades acionadas por API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa uma URL válida, encurtiremos e rastrearemos essa URL antes de enviar a mensagem pelo WhatsApp.

## Testes

Antes de lançar sua campanha ou Canvas, é uma boa prática visualizar e testar sua mensagem primeiro. Para fazer isso, acesse a guia **Test** para visualizar e enviar uma mensagem de WhatsApp para grupos de teste de conteúdo ou um usuário individual.

Essa prévia será atualizada com a personalização relevante e o URL encurtado. 

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios

Quando o rastreamento de cliques está ativado ou usado com modelos suportados, a tabela de desempenho do WhatsApp inclui a coluna **Total Clicks** que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para mais detalhes sobre métricas do WhatsApp, consulte [WhatsApp message performance]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![Etapa do Canvas da Mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Os dados de cliques serão relatados automaticamente no painel de análise.

![Tabela de desempenho da mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Redirecionamento de usuários 

Você pode usar o `Clicked/Opened Step` filtro e `clicked tracked WhatsApp link` interação para segmentar usuários com base em suas interações com os links.

![Grupo de filtro com um filtro para "link do WhatsApp rastreado clicado".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando o rastreamento de cliques está ativado (ou habilitado com base na configuração do modelo), você pode redirecionar usuários que clicaram em URLs aproveitando os filtros de redirecionamento do WhatsApp ou os eventos de cliques do WhatsApp (`users.messages.whatsapp.Click`) enviados pelo Currents.

### As prévias no dispositivo WhatsApp contam como cliques? 

Não, elas não contribuem para a taxa de cliques das mensagens do WhatsApp. 

