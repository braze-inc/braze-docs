---
nav_title: Casos de uso de comércio eletrônico
article_title: Casos de uso de comércio eletrônico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artigo de referência aborda vários modelos pré-construídos do Braze adaptados especificamente para profissionais de marketing de comércio eletrônico, facilitando a implementação de estratégias essenciais."
toc_headers: h2
---

# Casos de uso de comércio eletrônico

> O Braze Canvas oferece vários modelos pré-construídos adaptados especificamente para profissionais de marketing de comércio eletrônico, facilitando a implementação de estratégias essenciais. Esta página oferece alguns modelos importantes que podem ser usados para aprimorar as jornadas de seus clientes.

{% alert important %}
[Os eventos recomendados para comércio eletrônico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente Braze se estiver interessado em participar desse acesso antecipado. <br><br>Se estiver usando o novo conector do Shopify, os eventos recomendados para comércio eletrônico estarão automaticamente disponíveis por meio da integração.
{% endalert %}

## Usando um modelo do Canvas

Para usar um modelo do Canva:
1. Acesse **Envio de mensagens** > **Canva**.
2. Selecione **Criar tela** > **Usar um modelo de tela**.
3. Procure na guia **Braze templates** o modelo que deseja usar. Você pode fazer uma prévia de um modelo selecionando seu nome.
4. Selecione **Apply Template (Aplicar modelo** ) para o modelo que deseja usar.<br><br>![A página "Modelos de tela" foi aberta na guia "Modelos do Braze" e mostra uma lista de modelos usados recentemente e modelos do Braze selecionáveis.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Modelos de comércio eletrônico

- [Navegador abandonado](#abandoned-browse)
- [Carrinho abandonado](#abandoned-cart)
- [Checkout abandonado](#abandoned-checkout)
- [Confirmação do pedido e pesquisa de feedback](#order-confirmation--feedback-survey)

## Navegador abandonado

Use o modelo **Abandono de carrinho** para engajar os usuários que navegaram pelos produtos, mas não os adicionaram ao carrinho ou fizeram um pedido.

![Um modelo aplicado do Canva "Abandoned Browse" com "Entry Rules" expandidas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos de Braze** e aplique o modelo **Abandoned browse**. 

#### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:
- Tutorial 
    - Nome da tela: **Navegador abandonado**
    - Evento de conversão: `ecommerce.order placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Baseado em ação quando um usuário executa o evento `ecommerce.product_viewed` 
    - A hora de início é quando você cria o modelo do Canva<br><br>!["Opções baseadas em ações" para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Público alvo 
    - Público de entrada 
        - O e-mail **não está em branco**
        - Também é possível modificar os critérios do público de entrada para atender às suas necessidades comerciais
    - Controles de entrada
        - Os usuários são elegíveis para entrar novamente neste Canva após a conclusão da duração total do Canvas
    - Critérios de saída 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
    - 1 hora de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de modelo Liquid para adicionar produtos à sua mensagem no modelo pré-criado. Se você usar seu próprio modelo de e-mail, também poderá fazer referência a [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

### Personalização de produtos de navegação abandonada para e-mails 

Aqui está um exemplo de como você adicionaria um bloco de produto HTML para seu e-mail Abandoned Browse. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### URL do produto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## Carrinho abandonado

Use o modelo **Abandono de carrinho** para cobrir possíveis vendas perdidas de clientes que adicionaram produtos ao carrinho, mas não continuaram a finalizar a compra ou a fazer um pedido. 

![Um modelo de tela "Abandono de carrinho" aplicado com "Regras de entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos do Braze** e aplique o modelo **Abandono de carrinho**. 

#### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:
- Tutorial 
    - Nome da tela: **Carrinho abandonado**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário dispara o **evento Perform Cart Updated** (localizado no menu suspenso)
    - A hora de início é quando você cria o modelo do Canva<br><br>!["Opções baseadas em ações" para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Público-alvo 
    - Público de entrada 
        - Já usou esses apps **mais de 0** vezes 
        - O e-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para a entrada no Canva
    - Critérios de saída 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
     - 4 horas de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de modelo Liquid para adicionar produtos à sua mensagem no modelo pré-criado. Se você usar seu próprio modelo de e-mail, também poderá fazer referência a [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

### Personalização de produtos de carrinho abandonado para envio de e-mails {#abandoned-cart-checkout}

As jornadas de usuários de carrinhos abandonados exigem uma tag especial do Liquid `shopping_cart` para personalização do produto. 

Aqui está um exemplo de como adicionar um bloco HTML com a tag `shopping_cart` Liquid para adicionar produtos ao seu e-mail. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Se você usa o Shopify, adicione o nome do catálogo para obter o URL da imagem variante.
{% endalert %}

#### URL do carrinho em HTML

Se quiser direcionar os usuários de volta ao carrinho, você pode adicionar uma propriedade de evento aninhada no objeto medata, como, por exemplo:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Se você usa o Shopify, crie o URL do carrinho usando esse modelo Liquid:

{% raw %}
```liquid
{{context.source}}/checkouts/cn/{{context.cart_id}}
```
{% endraw %}

## Checkout abandonado

Use o modelo **Abandoned checkout** para direcionar os clientes que iniciaram o processo de checkout, mas saíram antes de fazer o pedido. 

![Um modelo de Canva "Abandoned Checkout" aplicado com "Entry Rules" expandidas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos do Braze** e aplique o modelo **Abandoned checkout**. 

#### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:

- Tutorial 
    - Nome da tela: **Checkout abandonado**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Disparo baseado em ação quando um usuário executa o evento `ecommerce.checkout_started` 
    - A hora de início é quando você cria o modelo do Canva<br><br>!["Opções baseadas em ações" para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Público alvo 
    - Público de entrada 
        - Já usou esses apps **mais de 0** vezes 
        - O e-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para a entrada no Canva
        - Critérios de saída 
            - Executa os eventos do site `ecommerce.order_placed` <br><br>![Controles de entrada e critérios de saída para o Canva.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
    - 4 horas de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de modelo Liquid para adicionar produtos à sua mensagem no modelo pré-criado. Se você usar seu próprio modelo de e-mail, também poderá fazer referência a [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

### Personalização de e-mails de checkout abandonado

As jornadas do usuário de checkout abandonado exigem uma tag especial do Liquid `shopping_cart` para personalização do produto. 

Aqui está um exemplo de como adicionar um bloco HTML com a tag `shopping_cart` Liquid para adicionar produtos ao seu e-mail. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### URL de checkout

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## Confirmação do pedido e pesquisa de feedback

Use o modelo **de pesquisa de confirmação de pedido e feedback** para confirmar pedidos bem-sucedidos e aumentar a satisfação do cliente.

![Um modelo de Canva de "Confirmação de pedido" aplicado com "Regras de entrada" expandidas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### Configuração

Na página do Canvas, selecione **Usar um modelo do Canvas** > **Modelos do Braze** e, em seguida, aplique o modelo **Confirmação de pedido e pesquisa de feedback**. 

#### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:

- Tutorial 
    - Nome da tela: **Confirmação do pedido com pesquisa de feedback**
    - Evento de conversão: `ecommerce.session_start`
        - Prazo de conversão: 10 dias 
- Cronograma de entrada 
    - Disparo baseado em ação quando um usuário executa o evento `ecommerce.cart_updated` 
    - A hora de início é quando você cria o modelo do Canva<br><br>!["Opções baseadas em ações" para o Canva.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Público alvo 
    - Público de entrada 
        - Já usou esses apps **mais de 0** vezes 
        - O e-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para a entrada no Canva
    - Critérios de saída 
        - Não se aplica<br><br>![Filtros e controles de entrada adicionais para o Canva.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de modelo Liquid para adicionar produtos à sua mensagem no modelo pré-criado. Se você usar seu próprio modelo de e-mail, também poderá fazer referência a [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

### Personalização da confirmação do pedido para e-mails

Aqui está um exemplo de como você adicionaria um bloco de produto HTML à confirmação do pedido após a realização de um pedido.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### URL do status do pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## Personalização de mensagens

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) é uma poderosa linguagem de modelos usada pelo Braze que permite criar conteúdo dinâmico e personalizado para seus clientes. Ao usar Liquid tags, você pode personalizar as mensagens com base nos dados do cliente, nas informações do produto e em outras variáveis, aprimorando a experiência de compra e promovendo o engajamento.

### Principais recursos do Liquid

- **Conteúdo dinâmico:** Insira informações específicas do cliente, como nomes, detalhes do pedido e preferências em suas mensagens.
- **Lógica condicional:** Use instruções if/else para exibir conteúdo diferente com base em condições específicas (como o local do cliente e o histórico de compras).
- **Loops:** Iterate sobre coleções de produtos ou dados de clientes para exibir listas ou grades de itens.

### Introdução ao Liquid

Para começar a personalizar suas mensagens usando Liquid tags, consulte os recursos a seguir:

- Referência de [dados do Shopify]({{site.baseurl}}/shopify_features/#shopify-data) com Liquid tags predefinidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentação

Use os segmentos Braze para criar segmentos de clientes direcionados com base em atributos e comportamentos específicos e fornecer campanhas e mensagens personalizadas. Com esse poderoso recurso, você pode engajar seus clientes de forma eficaz, atingindo o público certo com a mensagem certa no momento certo.

Para saber mais sobre como começar a usar segmentos, consulte [Sobre os segmentos do Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Os eventos de comércio eletrônico são baseados em [eventos recomendados]({{site.baseurl}}/recommended_events/).
Como os eventos recomendados são eventos personalizados mais opinativos, você pode pesquisar os nomes dos eventos de comércio eletrônico recomendados selecionando qualquer [filtro de evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de comércio eletrônico

Segmente seus usuários com filtros de comércio eletrônico, como **Fonte de comércio eletrônico** e **Receita total**, acessando a seção **Comércio eletrônico** no segmentador.

![Filtros de segmento suspensos com filtros de "Comércio eletrônico".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
O evento de compra será descontinuado e substituído por [eventos recomendados pelo comércio eletrônico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/). Quando isso acontecer, os filtros de segmento não serão mais preenchidos no comportamento de compra. Para obter uma lista completa de eventos de compra, consulte [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

## Propriedades de eventos aninhados

Para segmentar por propriedades de eventos aninhados, você pode aproveitar [as extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por exemplo, você pode usar as extensões de segmento para descobrir quem comprou o produto "SKU-123" nos últimos 90 dias.

## Análise de dados

{% alert note %}
No momento, a integração com o Shopify não é compatível com o preenchimento do [evento de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) do Braze. Como resultado, os filtros de compra, as tags Liquid, as ações baseadas em gatilho e a análise de dados devem usar o evento ecommerce.order_placed.
{% endalert %}

Para criar um [relatório de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) com base em quem realizou um evento suportado pela integração, você pode especificar o [nome do evento]({{site.baseurl}}/shopify_data_features/) específico.

Para obter insights sobre as tendências relacionadas aos pedidos feitos a partir de seus Canvases lançados, será necessário configurar um [Conversions Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) e especificar seus Canvases.

Para casos de uso de relatórios mais avançados, você pode usar o Braze [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) para gerar relatórios personalizados. 

