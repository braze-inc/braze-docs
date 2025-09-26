---
nav_title: Envio de mensagens sobre o produto
article_title: Envio de mensagens sobre o produto
page_order: 1
description: "Esta página aborda como usar o envio de mensagens de produto do WhatsApp para enviar mensagens interativas do WhatsApp que exibem produtos de seu catálogo do Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Envio de mensagens sobre o produto

> As mensagens de produtos permitem o envio de mensagens interativas do WhatsApp que exibem produtos diretamente do seu catálogo do Meta.

{% alert important %}
As mensagens do produto WhatsApp estão atualmente em acesso antecipado e estão planejadas para receber atualizações contínuas durante o período de acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

Quando você envia uma mensagem de produto do WhatsApp para um usuário, ele acessa a seguinte jornada do cliente:

1. O usuário recebe a mensagem do seu produto ou catálogo no WhatsApp.
2. O usuário adiciona produtos ao carrinho diretamente do WhatsApp.
3. O usuário toca em **Fazer pedido** no WhatsApp.
4. Seu site ou app recebe os dados do carrinho do Braze e gera um link de checkout.
5. O usuário é direcionado ao seu site ou app para concluir o checkout.

Quando os usuários adicionam itens ao carrinho por meio de mensagens de catálogo, o Braze recebe dados de webhook para ações de acompanhamento.

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Conta do WhatsApp Business | Para usar as mensagens de produtos do WhatsApp, você deve ter uma conta do WhatsApp Business conectada ao Braze. |
| Catálogo da Meta | Você precisa configurar um catálogo Meta em seu Commerce Manager. |
| Conformidade com o prazo | Cumprir os [Termos e Políticas do Meta Commerce](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Modelos de mensagens de produtos

{% tabs %}
{% tab Envio de mensagens do catálogo %}

As mensagens do catálogo exibem todo o seu catálogo de produtos em um formato interativo.

{% alert note %}
Não é necessário fazer seleções adicionais de produtos no Braze, pois a conexão do catálogo é gerenciada pelo Meta e, portanto, é herdada em seu catálogo de produtos.
{% endalert %}


{% endtab %}
{% tab Envio de mensagens para vários produtos %}

As mensagens de vários produtos destacam produtos específicos de seu catálogo, com até 30 itens destacados por mensagem. Atualmente, não há um seletor de produtos integrado, portanto, é necessário consultar manualmente o catálogo Meta para obter os SKUs dos produtos.

{% alert important %}
Há um problema conhecido de exibição de cabeçalho com modelos de mensagens de vários produtos no Meta. A Meta está ciente do problema e está trabalhando em uma correção.
{% endalert %}


{% endtab %}
{% endtabs %}

## Configuração de mensagens de produtos

1. No [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), siga [as instruções do Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) para criar seu catálogo Meta. Certifique-se de que você esteja no mesmo Meta Business Portfolio onde reside sua conta do WhatsApp Business conectada ao Braze.
2. Siga as instruções do Meta para [conectar seu catálogo Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) à sua conta do WhatsApp Business conectada ao Braze, atribuindo a permissão "Manage Catalog" (Gerenciar catálogo) no Meta Business Manager. 

![Meta página "Catalogs" (Catálogos) com uma seta apontando para o botão "Assign partner" (Atribuir parceiro) para o catálogo chamado "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:80%;"}

Certifique-se de usar a ID do Braze Business Manager, `332231937299182`, como a ID do negócio do parceiro.

![Janela para compartilhar um catálogo com um parceiro que contém campos para inserir um ID comercial do parceiro e atribuir a permissão "Gerenciar catálogo".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Selecione as configurações do catálogo Meta. Você deve selecionar **Mostrar ícone de catálogo no cabeçalho do bate-papo** para enviar mensagens de catálogo.

![Página de configurações do WhatsApp Manager para o catálogo "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:80%;"}

{: start="4"}
4\. No Braze, passe pelo processo [de registro incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) para fornecer permissões. Isso desbloqueará o seletor de produtos integrados Braze.

{% alert tip %}
Para conhecer as práticas recomendadas a serem seguidas ao criar catálogos Meta, consulte [Dicas para criar um catálogo de alta qualidade no Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Criação de uma mensagem de produto

1. Em seu gerenciador do Meta Business, acesse **Modelos de mensagens**.
2. Selecione **Catálogo** como formato e, em seguida, escolha entre **Mensagem de catálogo** (exibe o catálogo completo) e **Mensagem de catálogo de vários produtos** (destaca itens específicos).
3. No Braze, crie uma campanha do WhatsApp ou uma etapa do Canva Message.
4. Selecione o grupo de inscrições que corresponde ao local onde você enviou o modelo.
5. Selecione **WhatsApp Template Message**. (As mensagens de produtos e catálogos ainda não estão disponíveis nas mensagens de resposta).
6. Selecione o modelo que você gostaria de usar.
    - Se selecionar um modelo de vários produtos, forneça o título da seção e os IDs de conteúdo dos produtos a serem destacados.

![Lista de itens com campos para inserir os títulos das seções e o ID do conteúdo.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

{: start="7"}
7\. Continue construindo sua mensagem.

## Gerenciamento de produtos

### Acesso ao Commerce Manager

Em seu Meta Business Manager, acesse o **Commerce Manager** e selecione sua organização. Aqui, você pode gerenciar seus ativos de catálogo, como:
- Criar novos catálogos
- Adicionar produtos a catálogos existentes
- Atualizar informações sobre o produto
- Remover itens descontinuados

{% alert important %}
Se você remover produtos referenciados de seu catálogo, as mensagens associadas não serão enviadas.
{% endalert %}

## Check-out: Processamento de carrinhos e webhooks

Quando os usuários interagem com as mensagens de produtos do WhatsApp, eles podem navegar pelos produtos e adicionar itens ao carrinho. No entanto, atualmente não há funcionalidade de checkout integrada para informações de envio ou processamento de pagamentos. Em vez disso, recomendamos que você crie um carrinho em seu próprio app ou site e direcione os usuários para esse carrinho usando um link personalizado.

### Considerações

- **Não há checkout no app:** Os usuários não podem concluir compras diretamente no WhatsApp. Todas as transações devem ser redirecionadas para seu site ou app.
- **É necessário um link personalizado:** Você precisa criar um link personalizado que direcione os usuários para o carrinho na sua plataforma.
- **Configuração manual:** O processo de instalação requer a configuração manual de seu carrinho e fluxos de trabalho de envio de mensagens.

{% alert note %}
No momento, não oferecemos suporte a pagamentos que ocorrem diretamente no WhatsApp, e o suporte futuro será específico para cada país (atualmente, a Meta o oferece apenas para empresas sediadas e que trabalham diretamente com usuários na Índia, no Brasil e em Cingapura).
{% endalert %}

### Configuração de disparadores de eventos de carrinho

Quando um cliente faz um pedido no WhatsApp, o Braze automaticamente:
1. Recebe o conteúdo do carrinho do WhatsApp (IDs de produtos, quantidades e outros dados do pedido).
2. Cria um evento de comércio eletrônico `ecommerce.cart_update` com todos os dados relevantes, incluindo `source = whats_app`.
3. Dispara uma resposta, permitindo que você configure campanhas automatizadas para responder ao pedido.

O evento de comércio eletrônico `ecommerce.cart_update` só aparece listado no Braze após o envio de um evento, o que pode ser feito gerando uma mensagem de produto de teste do Braze e enviando um evento de carrinho.
O evento do carrinho inclui:

- **ID do carrinho:** Identificador exclusivo do carrinho
- **Produtos:** Lista de itens com IDs de produtos, quantidades e preços
- **Valor total:** Soma de todos os itens
- **Moeda:** A moeda do carrinho
- **Origem:** Marcado como "whats_app"
- **Metadados:** Dados adicionais, como ID do catálogo e texto da mensagem

Você pode encontrar informações adicionais sobre o evento do carrinho do Braze em [Tipos de eventos recomendados para comércio eletrônico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events).

### Configuração de uma resposta disparada

1. Crie um disparo de evento personalizado para `ecommerce.cart_updated`.
2. Adicionar um filtro de propriedade para `source = "whats_app"`.

![Etapa do canva para um disparo de evento personalizado `ecommerce.cart_updated` com a propriedade básica de "source" igual a `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\. Configure ações de acompanhamento com base nos dados do carrinho.

### Implementações de checkout recomendadas 

{% tabs %}
{% tab Links de carrinho simples baseados em Liquid %}

Use o Liquid para criar URLs de carrinho diretamente em sua mensagem de resposta. Isso é melhor se você tiver IDs de produto consistentes entre o WhatsApp e sua plataforma de comércio eletrônico.

#### Exemplo Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configuração

1. Crie uma campanha de mensagens de resposta do WhatsApp com o disparo de um evento de comércio eletrônico `ecommerce.cart_update`.
2. Crie uma mensagem subsequente com o URL do carrinho.
3. Crie o URL de seu carrinho com o Liquid. Se você usa o Shopify, pode [criar um permalink de carrinho](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) com o exemplo anterior Liquid.

![Diagrama mostrando o fluxo de trabalho da experiência de checkout para um carrinho gerado pelo Liquid: O Meta envia uma mensagem de recebimento de pedido para o Braze, que dispara uma ação-gatilho e, em seguida, cria uma mensagem com um link de carrinho, que envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Conteúdo conectado %}

Faça uma chamada de API para o seu sistema de comércio eletrônico para gerar um URL de checkout personalizado. Isso é melhor se você precisar de geração dinâmica de URL de carrinho ou mapeamento complexo de produtos.

#### Configuração

1. Crie uma campanha de webhook ou etapa do Canva disparada pelo evento [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) eCommerce, que enviará os dados do carrinho para o seu sistema de comércio eletrônico.
2. Crie uma campanha de mensagens do WhatsApp ou uma etapa do Canva Message disparada pelo mesmo evento de comércio eletrônico para enviar uma mensagem de resposta do WhatsApp com o URL do carrinho para o usuário. Siga as instruções na mensagem de resposta subsequente para usar o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content).

![Diagrama mostrando o fluxo de trabalho da experiência de checkout para uma chamada de Connected Content: A Meta envia uma mensagem de recebimento de pedido para a Braze, que tem chamadas de ida e volta com uma plataforma de comércio eletrônico e, em seguida, envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook e eventos personalizados %}

Use webhooks para enviar dados do carrinho para seu sistema e, em seguida, disparar mensagens de acompanhamento por meio de eventos personalizados. Isso é melhor para integrações complexas que exigem processamento extensivo de carrinhos ou fluxos de trabalho de várias etapas.

#### Configuração

Crie uma campanha de webhook ou uma etapa do Canva disparada pelo evento de comércio eletrônico `ecommerce.cart_update`, que enviará os dados do carrinho ao seu sistema de comércio eletrônico. Sua API será então:
1. Receber dados do carrinho
2. Crie um carrinho em seu sistema
3. Gerar o URL de checkout
4. Envie um evento `checkout_started` para o Braze, disparando sua mensagem do WhatsApp para envio com o link de checkout

![Diagrama mostrando o fluxo de trabalho da experiência de checkout para webhooks e eventos personalizados: O Meta envia uma mensagem de recebimento de pedido para a Braze, que tem chamadas de ida e volta com uma plataforma de comércio eletrônico e, em seguida, envia uma mensagem do WhatsApp com o URL do carrinho.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Testes e validação

### Requisitos de mensagens de teste

A funcionalidade do carrinho é transferida entre as mensagens de teste, mas o processamento do resultado de entrada não é transferido.

### Prévia da mensagem

- As imagens e os detalhes do produto são extraídos de seu catálogo Meta.
- A prévia interativa mostra marcadores de posição até que a integração seja concluída.

### Códigos de erro 

- Se um ID de produto não existir no catálogo, você receberá o erro `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Se um catálogo for desconectado da WABA, você receberá o erro `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
