---
nav_title: Mensagens do produto
article_title: Mensagens do produto
page_order: 2
description: "Esta página aborda como usar as mensagens de produto do WhatsApp para enviar mensagens interativas do WhatsApp que exibem produtos de seu catálogo do Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Mensagens do produto

> As mensagens de produtos permitem que você envie mensagens interativas do WhatsApp que exibem produtos diretamente do seu catálogo do Meta.

Quando você envia uma mensagem de produto do WhatsApp para um usuário, ele passa pela seguinte jornada do cliente:

1. O usuário recebe a mensagem do seu produto ou catálogo no WhatsApp.
2. O usuário adiciona produtos ao carrinho diretamente do WhatsApp.
3. O usuário toca em **Fazer pedido** no WhatsApp.
4. Seu site ou aplicativo recebe os dados do carrinho do Braze e gera um link de checkout.
5. O usuário é direcionado ao seu site ou aplicativo para concluir o checkout.

Quando os usuários adicionam itens ao carrinho por meio de mensagens de catálogo, o Braze recebe dados de webhook para ações de acompanhamento.

## Requisitos

| Requisito | Descrição |
| --- | --- |
| Conta do WhatsApp Business | Para usar as mensagens de produtos do WhatsApp, você deve ter uma conta do WhatsApp Business conectada ao Braze. |
| Meta catálogo | Você precisa configurar um catálogo Meta em seu Commerce Manager. |
| Conformidade com o prazo | Cumprir os [Termos e Políticas do Meta Commerce](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tipos de mensagens de produtos

{% alert note %}
Aprimore sua experiência de mensagens de produtos com o seletor de produtos integrado, que é acessado durante a etapa 4 de [Configuração de mensagens de produtos](#setting-up-product-messages).
{% endalert %}

{% tabs local %}
{% tab Catalog messages %}

As mensagens de catálogo exibem todo o seu catálogo de produtos em um formato interativo. Elas estão disponíveis como [modelo e mensagens de resposta](#building-a-product-message).

Se tiver ativado as permissões de catálogo para o Braze durante a [configuração](#setting-up-product-messages), você poderá selecionar qual miniatura estará visível para os usuários. 

{% alert note %}
Você não precisa fazer seleções adicionais de produtos no Braze, pois a conexão do catálogo é gerenciada pelo Meta e, portanto, é herdada em seu catálogo de produtos.
{% endalert %}


{% endtab %}
{% tab Multi-product messages %}

As mensagens multiproduto destacam produtos específicos de seu catálogo, com até 30 itens destacados por mensagem. Elas estão disponíveis como [modelo e mensagens de resposta](#building-a-product-message).

Você pode selecionar os produtos manualmente com IDs ou, se tiver ativado as permissões de catálogo durante a [configuração](#setting-up-product-messages), usar o seletor de produtos suspenso.

{% alert important %}
Há um problema conhecido de exibição de cabeçalho com modelos de mensagens de vários produtos no Meta. A Meta está ciente do problema e está trabalhando em uma correção.
{% endalert %}

{% endtab %}
{% tab Single product %}

As mensagens de produto único destacam um produto específico de seu catálogo de produtos. Elas estão disponíveis como [mensagens de resposta](#building-a-product-message).

Você pode selecionar os produtos manualmente com IDs ou, se tiver ativado as permissões de catálogo durante a [configuração](#setting-up-product-messages), usar o seletor de produtos suspenso.

{% endtab %}
{% endtabs %}

## Configuração de mensagens de produtos

1. No [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), siga [as instruções do Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) para criar seu catálogo Meta. Verifique se você está no mesmo Meta Business Portfolio em que reside sua conta do WhatsApp Business conectada ao Brasil.
2. Siga as instruções do Meta para [conectar seu catálogo Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) à sua conta do WhatsApp Business conectada ao Brasil, atribuindo a permissão "Manage Catalog" (Gerenciar catálogo) no Meta Business Manager. 

\![Meta página "Catálogos" com uma seta apontando para o botão "Atribuir parceiro" do catálogo chamado "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Certifique-se de usar o ID do Braze Business Manager, `332231937299182`, como o ID do negócio do parceiro.

Janela para compartilhar um catálogo com um parceiro que contém campos para inserir um ID comercial do parceiro e atribuir a permissão "Manage catalog" (Gerenciar catálogo).]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Selecione as configurações do catálogo Meta. Você deve selecionar **Mostrar ícone do catálogo no cabeçalho do bate-papo** para enviar mensagens do catálogo.

Página de configurações do WhatsApp Manager para o catálogo "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4\. No Braze, passe pelo processo [de registro incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) para fornecer permissões. Certifique-se de selecionar **todos os** catálogos para os quais você deseja fornecer permissões. Isso desbloqueará o seletor de produtos integrados Braze.

\![Janela com cinco catálogos selecionados fornece permissões.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Para conhecer as práticas recomendadas a serem seguidas ao criar catálogos Meta, consulte [Dicas para criar um catálogo de alta qualidade no Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Criação de uma mensagem de produto

Você pode criar uma mensagem de produto usando uma mensagem modelo do WhatsApp ou uma mensagem de resposta.

{% tabs local %}
{% tab WhatsApp message template %}

1. Em seu gerenciador do Meta Business, vá para **Modelos de mensagem**.
2. Selecione **Catalog** como formato e, em seguida, escolha entre **Catalog message** (exibe o catálogo completo) e **Multi-product catalog message** (destaca itens específicos).
3. No Braze, crie uma campanha do WhatsApp ou uma etapa do Canvas Message.
4. Selecione o grupo de assinatura que corresponde ao local onde você enviou o modelo.
5. Selecione **WhatsApp Template Message**.
6. Selecione o modelo que você gostaria de usar.
    - Se você selecionar um modelo de vários produtos, forneça o título da seção e os IDs de conteúdo dos produtos a serem destacados. Você pode copiar o Content ID diretamente do seu Meta Commerce Manager ou, se tiver ativado as permissões para o seletor de produtos integrado, selecionar os itens.

Lista de itens com campos para inserir os títulos das seções e o ID do conteúdo.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

\![Lista de itens com menu suspenso de itens para seleção.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7\. Continue construindo sua mensagem.

{% endtab %}
{% tab Response message %}

1. No Braze, crie uma campanha do WhatsApp ou uma etapa do Canvas Message.
2. Selecione um grupo de assinaturas.
3. Selecione **Response Message (Mensagem de resposta**).
4. Selecione **Meta Product Messages**.

\![Opções para selecionar um tipo de mensagem e o layout da mensagem de resposta, com "Response Message" e "Meta Product Messages" destacados.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5\. Selecione o [tipo de mensagem](#product-message-types) que você gostaria de usar.

Seleção do layout da mensagem de "Multiproduto".]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6\. Continue construindo sua mensagem.

\![Exemplo de mensagem de metaproduto com informações preenchidas para produtos.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Gerenciamento de produtos

### Acesso ao Commerce Manager

Em seu Meta Business Manager, vá para **Commerce Manager** e selecione sua organização. Aqui, você pode gerenciar os ativos do seu catálogo, como:
- Criar novos catálogos
- Adicionar produtos a catálogos existentes
- Atualizar informações sobre o produto
- Remover itens descontinuados

{% alert important %}
Se você remover produtos referenciados de seu catálogo, as mensagens associadas não serão enviadas.
{% endalert %}

## Recebimento de perguntas sobre produtos 

Os usuários podem responder à mensagem do seu produto ou catálogo com perguntas sobre o produto. Elas chegam como mensagens de entrada, que podem ser classificadas com um [Action Path]({{site.baseurl}}/action_paths/). 

Além disso, o Braze extrai a ID do produto e a ID do catálogo dessas perguntas, portanto, se desejar automatizar as respostas ou enviar perguntas para outra equipe (como o suporte ao cliente), você poderá incluir esses detalhes. Por exemplo, você pode personalizar as respostas com as propriedades do WhatsApp `inbound_product_id` ou `inbound_catalog_id`.

\!["Adicionar personalização" com um tipo de personalização de "Propriedades do WhatsApp" e um atributo destacado de "inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Check-out: Processamento de carrinhos e webhooks

Quando os usuários interagem com as mensagens de produto do WhatsApp, eles podem navegar pelos produtos e adicionar itens ao carrinho. No entanto, atualmente não há funcionalidade de checkout integrada para informações de remessa ou processamento de pagamentos. Em vez disso, recomendamos que você crie um carrinho em seu próprio aplicativo ou site e direcione os usuários para esse carrinho usando um link personalizado.

### Considerações

- **Não há checkout no aplicativo:** Os usuários não podem concluir compras diretamente no WhatsApp. Todas as transações devem ser redirecionadas para seu site ou aplicativo.
- **É necessário um link personalizado:** Você precisa criar um link personalizado que direcione os usuários para o carrinho na sua plataforma.
- **Configuração manual:** O processo de instalação requer a configuração manual de seu carrinho e fluxos de trabalho de mensagens.

{% alert note %}
No momento, não oferecemos suporte a pagamentos que ocorrem diretamente no WhatsApp, e o suporte futuro será específico para cada país (atualmente, o Meta oferece isso apenas para empresas sediadas e que trabalham diretamente com usuários na Índia, no Brasil e em Cingapura).
{% endalert %}

### Configuração de acionadores de eventos de carrinho

Quando um cliente faz um pedido no WhatsApp, o Braze automaticamente:
1. Recebe o conteúdo do carrinho do WhatsApp (IDs de produtos, quantidades e outros dados do pedido).
2. Cria um evento de comércio eletrônico `ecommerce.cart_update` com todos os dados relevantes, incluindo `source = whats_app`.
3. Aciona uma resposta, permitindo que você configure campanhas automatizadas para responder ao pedido.

O evento de comércio eletrônico `ecommerce.cart_update` só aparece listado no Braze após o envio de um evento, o que pode ser feito gerando uma mensagem de produto de teste do Braze e enviando um evento de carrinho.
O evento do carrinho inclui:

- **ID do carrinho:** Identificador exclusivo do carrinho
- **Produtos:** Lista de itens com IDs de produtos, quantidades e preços
- **Valor total:** Soma de todos os itens
- **Moeda:** A moeda do carrinho
- **Fonte:** Marcado como "whats_app"
- **Metadados:** Dados adicionais, como ID do catálogo e texto da mensagem

Você pode encontrar informações adicionais sobre o evento do carrinho do Braze em [Tipos de eventos recomendados para comércio eletrônico]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events).

### Configuração de uma resposta acionada

1. Crie um acionador de eventos personalizado para `ecommerce.cart_updated`.
2. Adicionar um filtro de propriedade para `source = "whats_app"`.

\![Etapa de tela para um acionador de evento personalizado `ecommerce.cart_updated` com a propriedade básica de "source" igual a `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\. Configure ações de acompanhamento com base nos dados do carrinho.

### Implementações de checkout recomendadas 

{% tabs local %}
{% tab Simple Liquid-based cart links %}

Use o Liquid para criar URLs de carrinho diretamente em sua mensagem de resposta. Isso é melhor se você tiver IDs de produto consistentes entre o WhatsApp e sua plataforma de comércio eletrônico.

#### Exemplo de líquido

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

1. Crie uma campanha de mensagem de resposta do WhatsApp com o acionador de um evento de comércio eletrônico `ecommerce.cart_update`.
2. Crie uma mensagem subsequente com o URL do carrinho.
3. Crie o URL do seu carrinho com o Liquid. Se você usa o Shopify, pode [criar um permalink de carrinho](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) com o exemplo anterior do Liquid.

Diagrama mostrando o fluxo de trabalho da experiência de checkout para um carrinho gerado pelo Liquid: O Meta envia uma mensagem de recebimento de pedido para a Braze, que aciona um acionador baseado em ação e, em seguida, cria uma mensagem com um link de carrinho, que envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

Faça uma chamada de API para o seu sistema de comércio eletrônico para gerar um URL de checkout personalizado. Isso é melhor se você precisar de geração dinâmica de URL de carrinho ou mapeamento complexo de produtos.

#### Configuração

1. Crie uma campanha de webhook ou uma etapa do Canvas acionada pelo evento [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) eCommerce, que enviará os dados do carrinho para o seu sistema de comércio eletrônico.
2. Crie uma campanha do WhatsApp ou uma etapa do Canvas Message acionada pelo mesmo evento de comércio eletrônico para enviar uma mensagem de resposta do WhatsApp com o URL do carrinho para o usuário. Siga as instruções na mensagem de resposta subsequente para usar o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content).

Diagrama mostrando o fluxo de trabalho da experiência de checkout para uma chamada de Connected Content: A Meta envia uma mensagem de recebimento de pedido para a Braze, que faz chamadas de ida e volta com uma plataforma de comércio eletrônico e, em seguida, envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook and custom events %}

Use webhooks para enviar dados do carrinho de compras para o seu sistema e, em seguida, acione mensagens de acompanhamento por meio de eventos personalizados. É a melhor opção para integrações complexas que exigem processamento extensivo de carrinhos ou fluxos de trabalho de várias etapas.

#### Configuração

Crie uma campanha de webhook ou uma etapa do Canvas acionada pelo evento de comércio eletrônico `ecommerce.cart_update`, que enviará os dados do carrinho para o seu sistema de comércio eletrônico. Sua API será então:
1. Receber dados do carrinho
2. Crie um carrinho em seu sistema
3. Gerar o URL de checkout
4. Envie um evento `checkout_started` para a Braze, acionando sua mensagem do WhatsApp para enviar o link de checkout

Diagrama mostrando o fluxo de trabalho da experiência de checkout para webhooks e eventos personalizados: O Meta envia uma mensagem de recebimento de pedido para a Braze, que faz chamadas de ida e volta com uma plataforma de comércio eletrônico e, em seguida, envia uma mensagem do WhatsApp com o URL do carrinho.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Testes e validação

### Requisitos de mensagens de teste

A funcionalidade do carrinho é transferida entre as mensagens de teste, mas o processamento do resultado de entrada não é transferido.

### Visualização da mensagem

- As imagens e os detalhes do produto são extraídos de seu catálogo Meta.
- A visualização interativa mostra marcadores de posição até que a integração seja concluída.

### Códigos de erro 

- Se um ID de produto não existir no catálogo, você receberá o erro `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Se um catálogo for desconectado da WABA, você receberá o erro `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
