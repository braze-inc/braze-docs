{% tabs %}
{% tab Abandoned browse %}

### Navegação abandonada

Use o modelo de **Navegação Abandonada** para engajar usuários que navegaram por produtos, mas não os adicionaram ao carrinho ou realizaram um pedido.

![Um modelo de Canvas "Navegação Abandonada" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuração

Na página do Canvas, selecione **Usar um Modelo de Canvas** > **modelos Braze** e, em seguida, aplique o modelo **Navegação Abandonada**. 

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:
- Tutorial 
    - Nome do Canvas: **Navegação Abandonada**
    - Evento de conversão: `ecommerce.order placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Baseado em ação quando um usuário realiza o evento `ecommerce.product_viewed`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Público alvo 
    - Público de entrada 
        - E-mail **não está em branco**
        - Você também pode modificar os critérios de público de entrada para atender às necessidades do seu negócio
    - Controles de entrada
        - Os usuários são elegíveis para reentrar neste Canvas após a duração total do Canvas ser concluída
    - Critérios de saída 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
    - 1 hora de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode referenciar [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de produtos visualizados abandonados para e-mails 

Aqui está um exemplo de como você adicionaria um bloco de produto HTML para seu e-mail de Navegação Abandonada. 

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

##### URL do produto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Carrinho abandonado

Use o modelo **Carrinho Abandonado** para cobrir vendas potenciais perdidas de clientes que adicionaram produtos ao carrinho, mas não continuaram para o checkout ou realizaram um pedido. 

![Um modelo "Carrinho Abandonado" Canvas aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuração

Na página do Canvas, selecione **Usar um Modelo Canvas** > **modelos Braze** e, em seguida, aplique o modelo **Carrinho Abandonado**. 

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:
- Tutorial 
    - Nome do Canvas: **Carrinho abandonado**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário aciona o **Executar Evento de Atualização de Carrinho** (localizado no dropdown)
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Público-alvo 
    - Público de entrada 
        - Usou esses aplicativos **mais de 0** vezes 
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente re-elegíveis para entrada no Canvas
    - Critérios de saída 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
     - 4 horas de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode referenciar [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Como funciona a lógica de reentrada do carrinho abandonado

Quando um usuário inicia o processo de checkout, seu carrinho é marcado como `checkout_started`. A partir desse ponto, quaisquer atualizações adicionais do carrinho com o mesmo ID de carrinho não qualificarão o usuário para reentrar na jornada do usuário do carrinho abandonado.

1. Quando um usuário adiciona um item ao seu carrinho, ele entra no Canvas.
2. Cada vez que eles adicionam ou atualizam itens, eles reentram no Canvas—isso mantém os dados do carrinho e o envio de mensagens atualizados.
3. Quando o usuário inicia o processo de checkout, seu carrinho é marcado como `checkout_started`, e ele sai do canva.
4. Quaisquer futuras atualizações de carrinho usando o mesmo ID de carrinho não dispararão a reentrada porque este carrinho já se moveu para a fase de checkout.

Quando os usuários avançam na jornada do usuário de checkout, eles são direcionados pelo [canva de checkout abandonado](#abandoned-checkout) em vez disso, que é projetado para usuários mais adiantados na jornada de compra.

#### Personalização de produtos de carrinho abandonado para e-mails {#abandoned-cart-checkout}

Jornadas de usuários de carrinho abandonado requerem uma tag Liquid especial `shopping_cart` para personalização de produtos. 

Aqui está um exemplo de como você adicionaria um bloco HTML com sua tag Liquid `shopping_cart` para adicionar produtos ao seu e-mail. 

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
Se você usar Shopify, adicione o nome do seu catálogo para obter a URL da imagem da variante.
{% endalert %}

##### URL do carrinho HTML

Se você quiser direcionar os usuários de volta ao seu carrinho, pode adicionar uma propriedade de evento aninhada sob o objeto de metadados, como:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Se você usar Shopify, crie sua URL de carrinho usando este modelo Liquid:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Checkout abandonado

Use o modelo **Checkout Abandonado** para direcionar clientes que iniciaram o processo de checkout, mas saíram antes de finalizar o pedido. 

![Um modelo de canva "Checkout Abandonado" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuração

Na página do canva, selecione **Usar um Modelo de Canva** > **Modelos Braze** e, em seguida, aplique o modelo **Checkout Abandonado**. 

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:

- Tutorial 
    - Nome do Canvas: **Checkout abandonado**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.checkout_started`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Público alvo 
    - Público de entrada 
        - Usou esses aplicativos **mais de 0** vezes 
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente re-elegíveis para entrada no Canvas
        - Critérios de saída 
            - Realiza os eventos `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa de postergação
    - 4 horas de postergação
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode referenciar [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de checkout abandonado para e-mails

Jornadas de usuários de checkout abandonado requerem uma tag Liquid especial `shopping_cart` para personalização de produtos. 

Aqui está um exemplo de como você adicionaria um bloco HTML com sua tag Liquid `shopping_cart` para adicionar produtos ao seu e-mail. 

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

##### URL de checkout

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmação de pedido e pesquisa de feedback

Use o modelo **Confirmação de pedido & pesquisa de feedback** para confirmar pedidos bem-sucedidos e aumentar a satisfação do cliente.

![Um modelo de Canvas "Confirmação de pedido" aplicado com "Regras de entrada" expandidas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuração

Na página do Canvas, selecione **Usar um modelo de Canvas** > **Modelos de Braze** e, em seguida, aplique o modelo **de pesquisa de feedback de confirmação de pedido &**. 

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:

- Tutorial 
    - Nome do Canvas: **Confirmação de pedido com pesquisa de feedback**
    - Evento de conversão: `ecommerce.session_start`
        - Prazo de conversão: 10 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.cart_updated`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Público alvo 
    - Público de entrada 
        - Usou esses aplicativos **mais de 0** vezes 
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente re-elegíveis para entrada no Canvas
    - Critérios de saída 
        - Não se aplica<br><br>![Filtros adicionais e controles de entrada para o Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode referenciar [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de confirmação de pedido para e-mails

Aqui está um exemplo de como você adicionaria um bloco de produto HTML à sua confirmação de pedido após um pedido ser feito.

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

##### URL de status do pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}