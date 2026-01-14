---
nav_title: Rastreamento de cliques LINE
article_title: Rastreamento de cliques do LINE
page_order: 2
description: "Esta página aborda como ativar o rastreamento de cliques em suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Rastreamento de cliques LINE

> Esta página aborda como ativar o rastreamento de cliques em suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.


Quando o rastreamento de cliques LINE está ativado, o Braze encurta automaticamente seus URLs, adiciona mecanismos de rastreamento e registra os cliques em tempo real. Enquanto o LINE oferece dados agregados de cliques, o Braze fornece informações granulares do usuário que são oportunas e acionáveis. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como a segmentação de usuários com base no comportamento de cliques e o acionamento de mensagens em resposta a cliques específicos.

O rastreamento de cliques do LINE pode ser usado para mensagens de texto, ricas e baseadas em cartões. Ele oferece suporte a links em botões e áreas mapeadas por imagem que têm um URL como ação ao clicar. Você também pode personalizar URLs usando o Liquid e domínios personalizados.

## Como funciona

Você pode gerenciar as configurações de rastreamento de cliques do LINE na guia **Settings (Configurações** ) ao redigir uma mensagem. Quando ativado, os URLs serão encurtados usando o domínio padrão do Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de assinatura e personalizado para o usuário.

Todos os URLs que começarem com `http://` ou `https://` serão encurtados. Você pode ter até 25 URLs em uma mensagem. Os URLs encurtados que contêm personalização do Liquid (como rastreamento no nível do usuário ou parâmetros UTM) serão válidos por dois meses.

## Configuração do rastreamento de cliques

### Mensagens de texto

Para configurar o rastreamento de cliques para uma mensagem de texto:

1. Arraste uma mensagem **de texto** para o compositor e adicione um URL ao campo de texto.

\![Compositor de mensagem LINE com uma mensagem de texto contendo um URL longo: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. Vá para a guia **Settings (Configurações** ) e confirme se **o Click Tracking (Rastreamento de cliques** ) está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
Você pode visualizar prévias do link encurtado na guia **Configurações** ou **Visualizar & Teste**. O link completo será exibido no compositor enquanto você cria sua mensagem.
{% endalert %}

\![Mensagem de linha que compõe a guia "Settings" (Configurações) com " com "Click Tracking" (Rastreamento de cliques) ativado e uma mensagem de texto de visualização contendo um URL abreviado: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Mensagens ricas

Para configurar o rastreamento de cliques para uma mensagem avançada:

1. Arraste uma **mensagem Rich** para o compositor e selecione um modelo.
2. Selecione **o URI** para o **comportamento ao clicar** na área tocável aplicável.
3. Digite um URL no campo **Abrir URL**.

\![LINE message composer with a Rich message with two tappable areas that each have a URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. Vá para a guia **Settings (Configurações** ) e confirme se **o Click Tracking (Rastreamento de cliques** ) está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

### Mensagens baseadas em cartões

Para configurar o rastreamento de cliques para uma mensagem baseada em cartão:

1. Arraste uma **mensagem baseada em cartão** para o compositor.
2. Selecione **o URI** para o **comportamento ao clicar** nas áreas aplicáveis do cartão ou do botão.

\![LINE message composer with a card-based message with two buttons that each have a URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. Vá para a guia **Settings (Configurações** ) e confirme se **o Click Tracking (Rastreamento de cliques** ) está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
Os URLs nos campos **Título** ou **Descrição** não serão encurtados porque esses campos não são clicáveis no LINE.
{% endalert %}

## Domínios personalizados

O rastreamento de cliques do LINE permite que você use seu próprio domínio para personalizar a aparência de seus URLs encurtados, ajudando a retratar uma imagem de marca consistente. Para obter mais informações, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Personalização líquida em URLs

Você pode construir dinamicamente seu URL diretamente no compositor do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar links exclusivos aos usuários (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).
Os URLs podem ser gerados dinamicamente por meio do uso de qualquer tag de personalização do Liquid compatível.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Você também pode encurtar as variáveis Liquid definidas de forma personalizada, conforme mostrado no exemplo a seguir:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Encurtar URLs renderizados por variáveis do Liquid

O Braze encurta os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades de acionamento de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem LINE.

## Testes

Antes de lançar sua campanha ou Canvas, a melhor prática é visualizar e testar sua mensagem primeiro. Para isso, vá para a guia **Teste** para visualizar e enviar uma mensagem LINE para grupos de teste de conteúdo ou para um usuário individual.

Essa visualização será atualizada com a personalização relevante e o URL encurtado. 

{% alert important %}
Se um rascunho for criado em um Canvas ativo, não será gerado um URL abreviado. O URL encurtado real é gerado quando o rascunho do Canvas é ativado.
{% endalert %}

## Relatórios

A tabela de desempenho do LINE inclui a coluna **Total Clicks (Total de cliques** ) que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para obter mais detalhes sobre as métricas do LINE, consulte [Desempenho da mensagem do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting).

\![Desempenho para uma etapa do LINE Canvas.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Os dados de cliques serão informados automaticamente no painel de análise. 

Painel de análise de desempenho da LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Redirecionamento de usuários

É possível redirecionar os usuários que clicaram em um URL em uma mensagem LINE usando os seguintes filtros e acionadores de segmentação:

- Gatilhos baseados em ações
    - Interaja com a campanha
    - Interagir com a etapa

\![LINE acionador de entrega baseado em ação.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtros de segmentação
    - Campanha clicada/aberta
    - Campanha clicada/aberta ou Canvas com tag 
    - Etapa clicada/aberta

Grupo de filtros que exibe todos os três filtros de segmentação: "Campanha clicada/aberta", "Campanha clicada/aberta ou Canvas com tag" e "Etapa clicada/aberta".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Perguntas frequentes

### Os links que recebo ao testar o envio de URLs são reais?

Sim, URLs reais serão gerados durante o envio do teste. No entanto, o URL exato enviado em uma campanha lançada pode ser diferente daquele enviado em um envio de teste.

### Posso adicionar parâmetros UTM a um URL antes que ele seja encurtado?

Sim, podem ser adicionados parâmetros estáticos e dinâmicos.

### Por quanto tempo os URLs encurtados permanecem válidos?

Os URLs personalizados são válidos por dois meses a partir do momento do registro do URL.

### O SDK do Braze precisa ser instalado para encurtar URLs?

Não, o rastreamento de cliques funciona sem nenhuma integração com o SDK.

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando o rastreamento de cliques está ativado, você pode redirecionar os usuários que clicaram em URLs usando os [filtros de redirecionamento do LINE](#retargeting-users).

### O rastreamento de cliques funciona com links diretos ou links universais?

O rastreamento de cliques não funciona com links diretos. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas o Braze não pode solucionar problemas que possam surgir ao fazer isso (como quebra de atribuição ou falha no redirecionamento).

### As visualizações no aplicativo LINE contam como cliques?

Não, eles não contribuem para a taxa de cliques das mensagens do LINE.