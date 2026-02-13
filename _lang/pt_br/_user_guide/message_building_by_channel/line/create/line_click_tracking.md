---
nav_title: Rastreamento de cliques do LINE
article_title: Rastreamento de cliques no LINE
page_order: 2
description: "Esta página aborda como ativar o rastreamento de cliques em suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# Rastreamento de cliques do LINE

> Esta página aborda como ativar o rastreamento de cliques em suas mensagens LINE, testar links encurtados, usar seu domínio personalizado em links rastreados e muito mais.


Quando o rastreamento de cliques LINE está ativado, o Braze encurta automaticamente seus URLs, adiciona mecanismos de rastreamento e registra os cliques em tempo real. Enquanto o LINE oferece dados agregados de cliques, o Braze fornece informações granulares de usuários que são oportunas e acionáveis. Esses dados permitem criar estratégias de segmentação e redirecionamento mais direcionadas, como segmentar usuários com base no comportamento ao clicar e disparar mensagens em resposta a cliques específicos.

O rastreamento de cliques do LINE pode ser usado para mensagens de texto, ricas e baseadas em cartões. Ele oferece suporte a links em botões e áreas mapeadas por imagem que têm um URL como ação ao clicar. Você também pode personalizar URLs usando Liquid e domínios personalizados.

## Como funciona?

Você pode gerenciar as configurações de rastreamento de cliques do LINE na guia **Configurações** enquanto cria uma mensagem. Quando ativado, os URLs serão encurtados usando o domínio padrão do Braze (`https://brz.ai`) ou o domínio personalizado especificado para o grupo de inscrições e personalizado para o usuário.

Todos os URLs que começam com `http://` ou `https://` serão encurtados. Você pode ter até 25 URLs em uma mensagem. Os URLs encurtados que contêm personalização Liquid (como rastreamento no nível do usuário ou parâmetros UTM) serão válidos por dois meses.

## Configuração do rastreamento de cliques

### Envio de mensagens de texto

Para configurar o rastreamento de cliques em uma mensagem de texto:

1. Arraste uma mensagem **de texto** para o criador e adicione um URL ao campo de texto.

![Criador de mensagem LINE com uma mensagem de texto contendo um URL longo: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. Acesse a guia **Settings (Configurações** ) e confirme se **o rastreamento de cliques** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
Você pode visualizar prévias do link encurtado na guia **Configurações** ou **Pré-visualização & Teste**. O link completo será exibido no criador de mensagens enquanto você cria sua mensagem.
{% endalert %}

![Guia "Settings" do criador da mensagem LINE com " com "Click Tracking" ativado e uma prévia Mensagem de texto contendo um URL abreviado: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Envio de mensagens Rich

Para configurar o rastreamento de cliques para uma mensagem avançada:

1. Arraste uma **mensagem Rich** para o criador e selecione um modelo.
2. Selecione **o URI** para o **comportamento ao clicar** na área tocável aplicável.
3. Digite um URL no campo **Abrir URL**.

![Criador de mensagens LINE com uma Rich message com duas áreas tocáveis, cada uma com um URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. Acesse a guia **Settings (Configurações** ) e confirme se **o rastreamento de cliques** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

### Envio de mensagens por cartão

Para configurar o rastreamento de cliques para uma mensagem baseada em cartão:

1. Arraste uma **mensagem baseada em cartão** para o criador.
2. Selecione **o URI** para o **comportamento ao clicar** nas áreas aplicáveis do cartão ou do botão.

![Criador de mensagens LINE com uma mensagem baseada em cartão com dois botões, cada um com um URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. Acesse a guia **Settings (Configurações** ) e confirme se **o rastreamento de cliques** está ativado. O rastreamento de cliques é ativado por padrão para todas as novas mensagens.

{% alert note %}
Os URLs nos campos **Título** ou **Descrição** não serão encurtados porque esses campos não são clicáveis no LINE.
{% endalert %}

## Domínios personalizados

O rastreamento de cliques do LINE permite que você use seu próprio domínio para personalizar a aparência de seus URLs encurtados, ajudando a retratar uma imagem de marca consistente. Para saber mais, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Personalização Liquid em URLs

Você pode construir dinamicamente seu URL diretamente no criador do Braze, o que lhe permite adicionar parâmetros UTM dinâmicos aos seus URLs ou enviar aos usuários links exclusivos (como direcionar os usuários para o carrinho abandonado ou para um produto específico que está de volta ao estoque).
Os URLs podem ser gerados dinamicamente com o uso de qualquer tag de personalização Liquid compatível.

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

## Encurtar URLs renderizados por variáveis Liquid

O Braze encurta os URLs que são renderizados pelo Liquid, mesmo aqueles incluídos nas propriedades de disparo de API. Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representar um URL válido, encurtaremos e rastrearemos esse URL antes de enviar a mensagem LINE.

## Testes

Antes de lançar sua campanha ou Canva, é uma prática recomendada fazer uma prévia e testar sua mensagem primeiro. Para fazer isso, acesse a guia **Teste** para fazer uma prévia e enviar uma mensagem LINE para grupos de teste de conteúdo ou para um usuário individual.

Essa prévia será atualizada com a personalização relevante e o URL encurtado. 

{% alert important %}
Se um rascunho for criado em um Canva ativo, não será gerado um URL encurtado. O URL encurtado real é gerado quando o rascunho do Canva é ativado.
{% endalert %}

## Relatórios

A tabela de performance LINE inclui a coluna **Total Clicks (Total de cliques** ) que mostra uma contagem de eventos de cliques por variante e uma taxa de cliques associada. Para obter mais detalhes sobre as métricas do LINE, consulte [Performance das mensagens do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting).

![Performance para uma etapa do canva LINE.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Os dados de cliques serão informados automaticamente no dashboard de análise de dados. 

![Painel de análise de dados de desempenho do LINE.]({% image_buster /assets/img/line/line_performance.png %})

## Redirecionamento de usuários

É possível redirecionar os usuários que clicaram em um URL em uma mensagem LINE usando os seguintes filtros e disparadores de segmentação:

- Gatilhos baseados em ações
    - Interagir com campanha
    - Interagir com a etapa

![Entrega baseada em ação do LINE.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtros de segmentação
    - Campanha clicada/aberta
    - Campanha ou tela clicada/aberta com tag 
    - Clicou/abriu uma etapa

![Grupo de filtros que exibe todos os três filtros de segmentação: "Campanha clicada/aberta", "Campanha clicada/aberta ou Canva com tag" e "Etapa clicada/aberta".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Perguntas frequentes

### Os links que recebo ao testar o envio de URLs são reais?

Sim, URLs reais serão gerados durante o envio do teste. No entanto, o URL exato enviado em uma campanha lançada pode ser diferente daquele enviado em um envio de teste.

### Posso adicionar parâmetros UTM a um URL antes de ele ser encurtado?

Sim, podem ser adicionados parâmetros estáticos e dinâmicos.

### Por quanto tempo os URLs encurtados permanecem válidos?

Os URLs personalizados são válidos por dois meses a partir do momento do registro do URL.

### O SDK do Braze precisa ser instalado para encurtar URLs?

Não, o rastreamento de cliques funciona sem nenhuma integração de SDK.

### Eu sei quais usuários individuais estão clicando em um URL?

Sim. Quando o rastreamento de cliques está ativado, é possível redirecionar os usuários que clicaram em URLs usando os [filtros de redirecionamento do LINE](#retargeting-users).

### O rastreamento de cliques funciona com deep links ou links universais?

O rastreamento de cliques não funciona com deep linkings. Você pode encurtar links universais de provedores como Branch ou Appsflyer, mas o Braze não é capaz de solucionar problemas que possam surgir ao fazer isso (como quebra de atribuição ou falha no redirecionamento).

### As prévias no app LINE contam como cliques?

Não, eles não contribuem para a taxa de cliques das mensagens do LINE.