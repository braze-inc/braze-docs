---
nav_title: Rastreamento de cliques
article_title: Rastreamento de cliques
page_order: 2
description: "Este artigo de referência aborda como ativar o rastreamento de cliques em suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Rastreamento de cliques

> Esta página aborda como ativar o rastreamento de cliques em suas mensagens do WhatsApp, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.

O rastreamento de cliques permite medir quando alguém toca em um link na sua mensagem do WhatsApp, oferecendo uma visão clara de qual conteúdo está gerando engajamento. O Braze encurta seus URLs, adiciona rastreamento nos bastidores e registra os eventos de cliques à medida que eles acontecem.

Você pode ativar o rastreamento de cliques nas mensagens de resposta e de modelo. Ele funciona com links em botões e no corpo do texto e oferece suporte a URLs personalizados e domínios personalizados. Depois de ativada, você verá os dados de cliques nos relatórios de performance do WhatsApp e poderá segmentar os usuários com base em quem clicou em quê.

## Como funciona?

### Envio de mensagens de resposta 

Para configurar o rastreamento de cliques para envios de mensagens de resposta:
1. Crie uma mensagem de resposta que inclua um botão de chamada para ação (CTA) com o URL de um site.
2. Ative o rastreamento de cliques clicando no botão designado na interface.

O link será encurtado para o domínio Braze ou para o domínio personalizado especificado para o grupo de inscrições e personalizado para o usuário.

Todos os URLs estáticos que começam com `http://` ou `https://` serão encurtados. Os URLs encurtados que contêm personalização Liquid (como direcionamento de rastreamento no nível do usuário) serão válidos por dois meses.

![Criador de mensagens do WhatsApp com corpo de conteúdo e um botão.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Envio de mensagens de modelo 

Para mensagens de modelo, o URL de base deve ser enviado corretamente ao criar o modelo para ativar o rastreamento de cliques.

#### Etapa 1: Crie um modelo compatível com rastreamento de cliques no WhatsApp

1. No Gerenciador do WhatsApp, crie uma URL de base que seja seu domínio personalizado ou `brz.ai`.
2. Certifique-se de que os links incluídos no modelo sejam compatíveis com o rastreamento de cliques.
3. Não altere as variáveis do modelo depois que ele for configurado como uma campanha no Braze; as alterações posteriores não poderão ser incorporadas.
4. Para links de botões de CTA, selecione **Dynamic (Dinâmico**) e, em seguida, forneça o URL de base (`brz.ai` ou seu domínio personalizado).<br><br>![Seção para criar uma chamada para ação.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Para links no corpo do texto, ao escrever o modelo em seu Gerenciador do WhatsApp, remova todos os espaços inseridos para links contidos no corpo que você deseja rastrear.<br><br>![Caixa de texto para inserir o corpo do conteúdo da chamada para ação.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Etapa 2: Complete seu modelo no Braze

Ao criar, o Braze detectará automaticamente quais modelos têm domínios de URL compatíveis, tanto no corpo do texto quanto nos botões de CTA. O status será mostrado na parte inferior do modelo. 

![A seção "Link Status" mostra um status ativo para rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Links compatíveis:** Os links enviados com o URL de base correspondente terão o rastreamento de cliques ativado.
- **Links com suporte parcial:** Se alguns links em um modelo forem enviados como URLs completos, o rastreamento de cliques **não será** aplicado a esses links.
- **Links sem suporte:** Os links sem um URL de base aprovado **não terão** recursos de rastreamento de cliques.

O URL de destino precisará ser fornecido para qualquer link com um URL de base que corresponda a `brz.ai` ou ao seu domínio personalizado. 

![Seção "Buttons" com campos para o nome do botão, URL do site e URL de rastreamento de cliques.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include click_tracking.md section='Domínios personalizados' %}

## Personalização Liquid em URLs

Você pode construir dinamicamente seu URL diretamente no criador do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar aos usuários links exclusivos (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).
Os URLs podem ser gerados dinamicamente com o uso de qualquer tag de personalização Liquid compatível.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Também apoiamos a redução de variáveis Liquid definidas de forma personalizada, como nestes exemplos:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Encurtar URLs renderizados por variáveis Liquid

O Braze encurta os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades de disparo de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem do WhatsApp.

## Testes

Antes de lançar sua campanha ou Canva, é uma prática recomendada fazer uma prévia e testar sua mensagem primeiro. Para fazer isso, acesse a guia **Teste** para fazer uma prévia e enviar um WhatsApp para grupos de teste de conteúdo ou para um usuário individual.

Essa prévia será atualizada com a personalização relevante e o URL encurtado. 

{% alert important %}
Se um rascunho for criado em um Canva ativo, não será gerado um URL abreviado. O URL encurtado real é gerado quando o rascunho do Canva é ativado.
{% endalert %}

## Relatórios

Quando o rastreamento de cliques está ativado ou é usado com modelos compatíveis, a tabela de performance do WhatsApp inclui a coluna **Total Clicks**, que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para obter mais detalhes sobre as métricas do WhatsApp, consulte [Performance das mensagens do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![Etapa do canva de mensagens do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Os dados de cliques serão informados automaticamente no dashboard de análise de dados.

![Tabela de performance de envio de mensagens do WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Redirecionamento de usuários 

Você pode usar o filtro `Clicked/Opened Step` e a interação `clicked tracked WhatsApp link` para segmentar os usuários com base em suas interações com os links.

![Grupo de filtros com um filtro para "clicou no link rastreado do WhatsApp".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include click_tracking.md section='Perguntas frequentes' %}

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando o rastreamento de cliques está ativado (ou ativado com base na configuração do modelo), é possível redirecionar os usuários que clicaram em URLs, aproveitando os filtros de redirecionamento do WhatsApp ou os eventos de clique do WhatsApp (`users.messages.whatsapp.Click`) enviados pelo Currents.

### O rastreamento de cliques funciona com deep links ou links universais?

O rastreamento de cliques não funciona com deep linkings. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas o Braze não pode solucionar problemas que possam surgir ao fazer isso (como quebrar a atribuição ou causar um redirecionamento).

### As prévias no dispositivo WhatsApp contam como cliques? 

Não, eles não contribuem para a taxa de cliques das mensagens do WhatsApp. 

