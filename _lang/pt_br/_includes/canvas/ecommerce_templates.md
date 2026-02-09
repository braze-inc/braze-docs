{% tabs %}
{% tab Abandoned browse %}

### Navegador abandonado

Use o modelo **Abandono de carrinho** para engajar os usuários que navegaram pelos produtos, mas não os adicionaram ao carrinho ou fizeram um pedido.

![Um modelo de Canva "Abandoned Browse" aplicado com "Entry Rules" expandidas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos de Braze** e aplique o modelo **Abandoned browse**. 

##### Configurações padrão

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
        - Também é possível modificar os critérios de público-alvo de entrada para atender às suas necessidades comerciais
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

#### Personalização de produtos de navegação abandonada para e-mails 

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

##### URL do produto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Carrinho abandonado

Use o modelo **Abandono de carrinho** para cobrir possíveis vendas perdidas de clientes que adicionaram produtos ao carrinho, mas não continuaram a finalizar a compra ou a fazer um pedido. 

![Um modelo de Canva "Abandoned Cart" aplicado com "Entry Rules" expandidas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos do Braze** e aplique o modelo **Abandono de carrinho**. 

##### Configurações padrão

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

#### Como funciona a lógica de reentrada de carrinho abandonado

Quando um usuário inicia o processo de checkout, seu carrinho é marcado como `checkout_started`. Desse ponto em diante, quaisquer outras atualizações de carrinho com o mesmo ID de carrinho não qualificarão o usuário para entrar novamente na jornada do usuário do carrinho abandonado.

1. Quando um usuário adiciona um item ao carrinho, ele entra no Canva.
2. Sempre que adicionam ou atualizam itens, eles entram novamente no Canva - isso mantém os dados do carrinho e o envio de mensagens atualizados.
3. Quando o usuário inicia o processo de checkout, seu carrinho é taggeado como `checkout_started`, e ele sai do Canva.
4. Qualquer atualização futura do carrinho usando o mesmo ID de carrinho não disparará a reentrada porque esse carrinho já passou para o estágio de checkout.

Quando os usuários passam para a jornada do usuário de checkout, eles são direcionados pelo [Canva de checkout abandonado](#abandoned-checkout), que é projetado para usuários mais avançados na jornada de compra.

#### Personalização de produtos de carrinho abandonado para envio de e-mails {#abandoned-cart-checkout}

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

##### URL do carrinho em HTML

Se quiser direcionar os usuários de volta ao carrinho, você pode adicionar uma propriedade de evento aninhada no objeto de metadados, como, por exemplo:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Se você usa o Shopify, crie o URL do carrinho usando esse modelo Liquid:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Checkout abandonado

Use o modelo **Abandoned checkout** para direcionar os clientes que iniciaram o processo de checkout, mas saíram antes de fazer o pedido. 

![Um modelo de Canva "Abandoned Checkout" aplicado com "Regras de entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuração

Na página Canvas, selecione **Usar um modelo de canvas** > **Modelos do Braze** e aplique o modelo **Abandoned checkout**. 

##### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:

- Tutorial 
    - Nome da tela: **Checkout abandonado**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.checkout_started` 
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

#### Personalização de e-mails de checkout abandonado

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

##### URL de checkout

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmação do pedido e pesquisa de feedback

Use o modelo **de pesquisa de feedback de confirmação de pedido & ** para confirmar pedidos bem-sucedidos e aumentar a satisfação do cliente.

![Um modelo de Canva de "Confirmação de pedido" aplicado com "Regras de entrada" expandidas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuração

Na página do Canvas, selecione **Usar um modelo do Canvas** > **Modelos do Braze** e aplique o modelo **de pesquisa de feedback de confirmação de pedido & **. 

##### Configurações padrão

As seguintes configurações são pré-configuradas em seu Canva:

- Tutorial 
    - Nome da tela: **Confirmação do pedido com pesquisa de feedback**
    - Evento de conversão: `ecommerce.session_start`
        - Prazo de conversão: 10 dias 
- Cronograma de entrada 
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.cart_updated` 
    - A hora de início é quando você cria o modelo do Canva<br><br>!["Opções baseadas em ações" para o Canva.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Público alvo 
    - Público de entrada 
        - Já usou esses apps **mais de 0** vezes 
        - O e-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para a entrada no Canva
    - Critérios de saída 
        - Não se aplica<br><br>![Filtros adicionais e controles de entrada para o Canva.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Enviar configurações 
    - Usuários inscritos ou que aceitaram 
- Etapa da mensagem 
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de modelo Liquid para adicionar produtos à sua mensagem no modelo pré-criado. Se você usar seu próprio modelo de e-mail, também poderá fazer referência a [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização da confirmação do pedido para e-mails

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

##### URL do status do pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}