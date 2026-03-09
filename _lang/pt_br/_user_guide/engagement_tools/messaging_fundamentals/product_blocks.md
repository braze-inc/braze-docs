---
nav_title: Bloco de produtos
article_title: Blocos de Produto Arrastar e Soltar
page_order: 9
description: "Este artigo de referência cobre blocos de produto arrastar e soltar, que permitem aos usuários adicionar e configurar rapidamente mostras dinâmicas ou estáticas de itens do catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Blocos de produto arrastar e soltar 

> O editor de arrastar e soltar permite que você adicione e configure rapidamente blocos de produto em suas mensagens para mostras de produtos sem costura, sem a necessidade de criar código Liquid personalizado. 

{% alert important %}
O recurso de bloco de produto arrastar e soltar está em acesso antecipado e atualmente disponível apenas para e-mail. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Solicitações 

| Requisito | Descrição |
| --- | --- |
| eventos recomendados de eCommerce | [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) fornecem esquemas de dados padronizados para eventos comportamentais chave que ocorrem antes e depois de um pedido ser feito. Esses eventos eventualmente substituirão o evento de compra legado do Braze e se tornarão o padrão para rastreamento de comportamento relacionado ao comércio. <br><br> Eventos recomendados de eCommerce são necessários para blocos de produto dinâmicos.<br><br> Eventos recomendados de eCommerce estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente do Braze se você estiver interessado em participar deste acesso antecipado. |
| modelos de Canvas de eCommerce | Os eventos recomendados de eCommerce suportam modelos pré-construídos, incluindo modelos de Canvas de eCommerce projetados para casos de uso essenciais, como navegação abandonada, carrinhos abandonados e confirmações de pedidos. <br><br>Se você planeja implementar qualquer um desses casos de uso essenciais de eCommerce usando os [modelos de Canvas de eCommerce]({{site.baseurl}}/ecommerce_use_cases/), você deve usar ou seguir o modelo de Canvas fornecido. |
| catálogo do Braze | Você deve criar um catálogo do Braze que inclua os seguintes campos, que você usará na configuração do seu bloco de produto:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| seleção de catálogo | Para blocos de produto estáticos, você deve criar uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar quais produtos incluir em seu bloco de produto. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Tipos de blocos de produto arrastar e soltar

| Bloco de produto | Finalidade | Casos de uso | Disponibilidade |
| --- | --- | --- | --- |
| Dinâmico | Personalize seu envio de mensagens com uma vitrine de produtos com base nas interações dos clientes usando [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) e catálogos dentro de nossos [modelos de Canvas de eCommerce]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navegação abandonada</li><li>Carrinho abandonado</li><li>Checkout abandonado</li><li>Confirmações de pedidos</li></ul>{:/} | Disponível apenas no Canvas. |
| Estático | Personalize produtos usando dados armazenados em um catálogo Braze. Você deve usar uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar quais produtos incluir. | Perfeito para exibir lançamentos de novos produtos ou ofertas específicas de categoria.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Configuração de conteúdo do bloco de produto

Cada tipo de bloco tem diferentes configurações de conteúdo. 

### Campos do produto

Na seção **Campos de Produto**, selecione o tipo de bloco de produto, depois ative os campos que você gostaria de incluir para cada produto. Cada campo é extraído de diferentes fontes com base no tipo de bloco de produto que você selecionar.

#### Bloco dinâmico de produtos

| Campo de produto | Origem |
| --- | --- | 
| Imagem da variante | Catálogos | 
| Título do produto | Catálogos | 
| Botão para URL do produto | Catálogos |
| Preço | Propriedade de evento recomendado de eCommerce|
| Quantidade | Propriedade de evento recomendado de eCommerce| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Campos de produto para um bloco de produto dinâmico, que são divididos em dados de catálogo e dados de evento]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloco de produto estático

| Campo de produto | Origem |
| --- | --- | --- |
| Imagem da variante | Catálogos |
| Título do produto | Catálogos |
| Botão para URL do produto | Catálogos |
| Preço | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![Campos de produto para um bloco de produto estático, que são todos categorizados como dados de catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opções de layout

Use opções de layout para personalizar como seus produtos são exibidos dentro do seu bloco de produto.

| Opção | Descrição |
| --- | --- |
| Orientação do produto | Escolha como a imagem e os campos de produto dentro do bloco são orientados. |
| Alinhamento | Ajuste o alinhamento dos campos de texto e do botão dentro do bloco. |
| Máx. de produtos por linha | Exiba até três produtos por linha, até 12 produtos no total para blocos de produtos estáticos e até 24 produtos no total para blocos de produtos dinâmicos. |
| Espaçamento do produto | Defina o espaçamento entre os produtos. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Opções de layout para orientação do produto, alinhamento, máximo de produtos por linha e espaçamento entre produtos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configurações de estilo de e-mail global 

[Configurações de estilo de e-mail global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) permitem que você aplique um estilo consistente aos seus e-mails dentro do Braze. Isso significa que você pode definir estilos específicos—como fontes, cores e designs de botões—que serão aplicados automaticamente a todos os seus e-mails.

#### Como as configurações de estilo de e-mail global funcionam com blocos de produtos

Estilos existentes para parágrafos e botões são aplicados automaticamente aos elementos de texto e botão dentro do bloco de produtos. Isso significa que seu bloco de produtos usa consistentemente qualquer formatação que você definiu para parágrafos e botões, mantendo uma aparência coesa em todo o seu e-mail.

## Configurando blocos de produtos

### Configuração do catálogo 

{% alert important %}
Se você estiver usando a integração do Braze e Shopify para [sincronização de produtos]({{site.baseurl}}/shopify_catalogs/), não precisa tomar nenhuma medida adicional para usar blocos de produtos arrastar e soltar.<br><br> Se você não tiver informações sobre variantes de produtos, precisará duplicar as informações do produto de nível superior tanto nos campos de produto quanto nos campos de variante de produto dentro das cargas de eventos e catálogos. Isso significa que você precisa fornecer os mesmos detalhes do produto para ambos os identificadores para manter a consistência para que o bloco de produtos funcione corretamente.
{% endalert %}

Para usar blocos de produtos arrastar e soltar, você precisa configurar um catálogo Braze que inclua valores de campo específicos. Você usa esses campos na configuração do seu bloco de produtos. Certifique-se de que seu catálogo inclua os seguintes campos:

| Campo | Descrição |
| --- | --- |
|`product_title` | O título do produto.|
|`product_url` | A URL onde os clientes podem visualizar ou comprar o produto. |
|`variant_image_url` | A URL da imagem variante. |

Comece com este [catálogo de produtos de amostra]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), que inclui os campos necessários. 

![Um arquivo CSV de amostra com os campos necessários além de outros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mapeamento para campos do catálogo

Na aba **Configurações** do seu catálogo, você pode selecionar o toggle **Blocos de produtos** para mapear campos e informações específicas no seu catálogo. Isso permite que você selecione quais campos usar como título do produto, URL do produto e URL da imagem. Observe que os campos do catálogo do Shopify são mapeados por padrão e não podem ser alterados.

{% alert note %}
Se você não estiver usando Shopify, pode entrar em contato com seu gerente de conta para ativar o mapeamento de campos, que permite conectar qualquer catálogo a blocos de produtos e mapear seus campos para o `product_title`, `product_url` e `variant_image_url`.
{% endalert %}

## Criando blocos de produtos

Este guia irá orientá-lo pelos passos para criar, testar e garantir a funcionalidade de um bloco de produto dinâmico ou estático usando nosso editor de arrastar e soltar para e-mail.

### Etapa 1: Crie uma campanha de e-mail ou etapa do Canvas de e-mail

#### Bloco dinâmico de produtos

{% alert note %}
Blocos de produtos dinâmicos requerem [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) e só podem ser usados dentro de [Canvases]({{site.baseurl}}/ecommerce_use_cases). Para usuários do Braze Shopify, esses eventos são incluídos automaticamente como parte da integração. Para usuários que não são do Shopify, você precisa trabalhar com seus desenvolvedores para passar esses eventos para o Braze e garantir que o identificador principal do produto dentro dos eventos seja adicionado como o ID do item do catálogo.
{% endalert %}

Crie um novo Canvas que use um dos modelos disponíveis do Braze para seu caso de uso específico:
- Navegação abandonada
- Carrinho abandonado
- Checkout abandonado
- Confirmações de Pedido

Para instruções detalhadas sobre como criar seus Canvases de eCommerce, consulte [casos de uso de eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

#### Bloco de produto estático

Crie uma campanha de e-mail arrastar e soltar, um Canvas baseado em ação ou um modelo que tenha uma etapa de Mensagem de e-mail arrastar e soltar.

### Etapa 2: Adicione um bloco de produto

{% tabs %}
{% tab Dynamic product block %}

Dentro da etapa de mensagem, crie um e-mail ou modifique o modelo existente usando o criador de e-mail arrastar e soltar.
Arraste um bloco de produto para sua mensagem de e-mail.
Confirme se o tipo de bloco dinâmico está selecionado.
Selecione o catálogo de produtos que deseja usar para personalização. Certifique-se de que está alinhado com os produtos dos eventos de entrada que você está direcionando.

{% endtab %}
{% tab Static product block %}

Arraste um bloco de produto para sua mensagem de e-mail e selecione o tipo de bloco estático.
Selecione o catálogo que deseja usar para seu bloco de produto. Você deve selecionar uma seleção de catálogo para especificar quais produtos serão exibidos em seu bloco de produto.

{% endtab %}
{% endtabs %}

![A guia "Conteúdo" contendo blocos de editor, como blocos de produto.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Etapa 3: Configure os campos do produto

Selecione quais [campos do produto](#product-fields) devem ser exibidos no bloco de produto. Selecione **Aplicar Configurações** após cada alteração para ver as atualizações no editor. 

Você também pode personalizar o texto antes de suas tags Liquid. Por exemplo, você pode adicionar um sinal de dólar ($) ao preço de um item ou atualizar o termo para quantidade para "quantidade" ou outro rótulo preferido.

![Bloco de produto com um lado de dólar adicionado ao preço do item.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Etapa 4: Configure as configurações de layout

Altere as [opções de layout](#layout-options) para atualizar como os produtos são exibidos dentro do seu bloco de produto e certifique-se de selecionar **Aplicar configurações** após cada alteração.

### Etapa 5: Pré-visualize e teste sua mensagem

{% tabs %}
{% tab Dynamic product block %}

1. Na seção **Prévia & Teste**, visualize a mensagem como um usuário personalizado.
2. Especifique quantos itens você deseja renderizar na prévia.
3. Confirme se o número correto de itens aparece e se suas opções de layout estão aplicadas corretamente. Observe que os itens que aparecem são selecionados aleatoriamente.

!["Prévia como Usuário" guia com uma seção suspensa "Bloco de produto dinâmico" que especifica mostrar 4 itens.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

Uma prévia será gerada dentro do criador de arrastar e soltar quando você aplicar alterações ao seu bloco de produto. 

![E-mail criador de arrastar e soltar mostrando um bloco de produto gerado com diferentes azulejos de itens.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Depois de terminar de criar sua mensagem e confirmar que ela está como esperado, você está pronto para enviar!