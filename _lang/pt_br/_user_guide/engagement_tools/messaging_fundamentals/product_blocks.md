---
nav_title: Blocos de produtos
article_title: Blocos de produtos de arrastar e soltar
page_order: 7
description: "Este artigo de referência aborda os blocos de produtos do tipo arrastar e soltar, que permitem aos usuários adicionar e configurar rapidamente mostruários dinâmicos ou estáticos de itens de catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Blocos de produtos do tipo arrastar e soltar 

> O editor de arrastar e soltar permite que você adicione e configure rapidamente blocos de produtos às suas mensagens para exibir produtos sem interrupções, sem a necessidade de criar código Liquid personalizado. 

{% alert important %}
O recurso de arrastar e soltar blocos de produtos está em acesso antecipado e, no momento, só está disponível para envio de e-mail. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Solicitações 

| Requisito | Descrição |
| --- | --- |
| Eventos recomendados para comércio eletrônico | [Os eventos recomendados para comércio eletrônico]({{site.baseurl}}/ecommerce_events/) fornecem esquemas de dados padronizados para os principais eventos comportamentais que ocorrem antes e depois da realização de um pedido. Esses eventos acabarão substituindo o evento de compra legado do Braze e se tornarão o padrão para o rastreamento do comportamento relacionado ao comércio. <br><br> Os eventos recomendados pelo comércio eletrônico são necessários para blocos de produtos dinâmicos.<br><br> Os eventos recomendados para comércio eletrônico estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente Braze se estiver interessado em participar desse acesso antecipado. |
| Modelos de canvas para comércio eletrônico | Os eventos recomendados para comércio eletrônico suportam modelos pré-criados, incluindo modelos do eCommerce Canva projetados para casos de uso essenciais, como navegação abandonada, abandono de carrinho e confirmação de pedidos. <br><br>Se você planeja implementar qualquer um desses casos de uso essenciais de comércio eletrônico usando os [modelos do eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/), deve usar ou seguir o modelo de Canvas fornecido. |
| Catálogo Braze | Você precisa criar um catálogo do Braze que inclua os seguintes campos, que serão usados na configuração do bloco de produtos:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Tipos de blocos de produtos de arrastar e soltar

| Bloco de produtos | Finalidade | Casos de uso | Disponibilidade |
| --- | --- | --- | --- |
| Dinâmico | Personalize o envio de mensagens com uma vitrine de produtos baseada nas interações com os clientes usando [eventos]({{site.baseurl}}/ecommerce_events/) e catálogos [recomendados para comércio eletrônico]({{site.baseurl}}/ecommerce_events/) em nossos [modelos do eCommerce Canvas]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navegador abandonado</li><li>Carrinho abandonado</li><li>Checkout abandonado</li><li>Confirmações de pedidos</li></ul>{:/} | Disponível somente em canvas. |
| Estático | Personalize produtos usando apenas os dados armazenados em um catálogo Braze ou em uma [seleção de catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/). | Perfeito para apresentar lançamentos de novos produtos ou ofertas específicas de uma categoria.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Configuração do conteúdo do bloco de produtos

Cada tipo de bloco tem diferentes configurações de conteúdo. 

### Campos do produto

Na seção **Product Fields (Campos do produto** ), selecione o tipo de bloco do produto e, em seguida, ative os campos que deseja incluir para cada produto. Cada campo é extraído de fontes diferentes com base no tipo de bloco de produtos que você seleciona.

#### Bloco dinâmico de produtos

| Campo do produto | Origem |
| --- | --- | 
| Imagem da variante | Catálogos | 
| Título do produto | Catálogos | 
| Botão para URL do produto | Catálogos |
| Preço | Propriedade do evento Recommended eCommerce|
| Quantidade | Propriedade do evento Recommended eCommerce| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Campos de produto para um bloco de produto dinâmico, que são divididos em dados de catálogo e dados de evento]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloco de produto estático

| Campo do produto | Origem |
| --- | --- | --- |
| Imagem da variante | Catálogos |
| Título do produto | Catálogos |
| Botão para URL do produto | Catálogos |
| Preço | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

![Campos de produto para um bloco de produto estático, que são todos categorizados como dados de catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opções de layout

Use as opções de layout para personalizar a exibição de seus produtos no bloco de produtos.

| Opção | Descrição |
| --- | --- |
| Orientação do produto | Escolha como os campos de imagem e produto dentro do bloco serão orientados. |
| Alinhamento | Ajuste o alinhamento dos campos de texto e do botão dentro do bloco. |
| Máx. de produtos por linha | Exiba até três produtos por linha, até 12 produtos no total para blocos de produtos estáticos e até 24 produtos no total para blocos de produtos dinâmicos. |
| Espaçamento do produto | Defina o espaçamento entre os produtos. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

![Opções de layout para orientação do produto, alinhamento, máximo de produtos por linha e espaçamento entre produtos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configurações globais de estilo de e-mail 

[As configurações globais de estilo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) permitem que você aplique um estilo consistente aos seus e-mails no Braze. Isso significa que você pode definir estilos específicos, como fontes, cores e designs de botões, que serão aplicados automaticamente a todos os seus e-mails.

#### Como as configurações globais de estilo de e-mail funcionam com blocos de produtos

Os estilos existentes para parágrafos e botões serão aplicados automaticamente aos elementos de texto e botão no bloco de produtos. Isso significa que qualquer formatação definida para parágrafos e botões será usada de forma consistente no bloco de produtos, mantendo uma aparência coesa em todo o e-mail.

## Configuração de blocos de produtos

### Configuração do catálogo 

{% alert important %}
Se estiver usando a integração entre o Braze e o Shopify para [sincronização de produtos]({{site.baseurl}}/shopify_catalogs/), não será necessário realizar nenhuma etapa adicional para usar blocos de produtos de arrastar e soltar.<br><br> Se não tiver informações sobre a variante do produto, será necessário duplicar as informações de nível superior do produto nos campos do produto e da variante do produto nas cargas úteis e nos catálogos do evento. Isso significa que você precisa fornecer os mesmos detalhes do produto para ambos os identificadores a fim de manter a consistência para que o bloco de produtos funcione corretamente.
{% endalert %}

Para usar blocos de produtos do tipo arrastar e soltar, você precisa configurar um catálogo do Braze que inclua valores de campo específicos. Esses campos serão usados na configuração do bloco do produto. Certifique-se de que seu catálogo inclua os seguintes campos:

| Campo | Descrição |
| --- | --- |
|`product_title` | O título do produto.|
|`product_url` | O URL onde os clientes podem visualizar ou comprar o produto. |
|`variant_image_url` | O URL da imagem variante. |

Comece a trabalhar com este [exemplo de Catálogo de Produtos]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), que inclui os campos obrigatórios. 

![Um exemplo de arquivo CSV com os campos obrigatórios, além de outros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## Criação de blocos de produtos

Este guia o guiará pelas etapas para criar, testar e garantir a funcionalidade de um bloco de produto dinâmico ou estático usando nosso editor de arrastar e soltar de e-mail.

### Etapa 1: Crie uma campanha de e-mail ou uma etapa do canva de e-mail

#### Bloco dinâmico de produtos

{% alert note %}
Os blocos de produtos dinâmicos requerem [eventos recomendados pelo comércio eletrônico]({{site.baseurl}}/ecommerce_events/) e só podem ser usados no [Canvas]({{site.baseurl}}/ecommerce_use_cases). Para os usuários do Braze Shopify, esses eventos são incluídos automaticamente como parte da integração. Para usuários que não são do Shopify, é necessário trabalhar com seus desenvolvedores para passar esses eventos para o Braze e garantir que o identificador principal do produto nos eventos seja adicionado como o ID do item do catálogo.
{% endalert %}

Crie uma nova tela que use um dos modelos Braze disponíveis para seu caso de uso específico:
- Navegação abandonada
- Carrinho abandonado
- Checkout abandonado
- Confirmações de pedidos

Para obter instruções detalhadas sobre como criar suas telas de comércio eletrônico, consulte os [casos de uso de comércio eletrônico]({{site.baseurl}}/ecommerce_use_cases/).

#### Bloco de produto estático

Crie uma campanha de e-mail de arrastar e soltar, um Canva baseado em ações ou um modelo que tenha uma etapa de envio de e-mail de arrastar e soltar.

### Etapa 2: Adicionar um bloco de produto

{% tabs %}
{% tab Bloco dinâmico de produtos %}

Na etapa de mensagem, crie um e-mail ou modifique o modelo existente usando o criador de e-mail de arrastar e soltar.
Arraste um bloco de produto para sua mensagem de e-mail.
Confirme se o tipo de bloco dinâmico está selecionado.
Selecione o catálogo de produtos que você deseja usar para personalização. Certifique-se de que ele esteja alinhado com os produtos dos eventos de entrada que você está direcionando.

{% endtab %}
{% tab Bloco de produto estático %}

Arraste um bloco de produto para sua mensagem de e-mail e selecione o tipo de bloco estático.
Selecione o catálogo que deseja usar para seu bloco de produtos. Se o catálogo tiver uma seleção, você deverá selecioná-la para restringir ainda mais os produtos exibidos no bloco de produtos.

{% endtab %}
{% endtabs %}

![A guia "Content" (Conteúdo) contém blocos do editor, como blocos de produtos.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Etapa 3: Configurar campos de produtos

Selecione quais [campos de produto](#product-fields) devem ser exibidos no bloco de produtos. Selecione **Aplicar configurações** após cada alteração para ver as atualizações no editor. 

Você também pode personalizar o texto antes de suas tags Liquid. Por exemplo, você pode acrescentar um cifrão ($) ao preço de um item ou atualizar o termo de quantidade para "quantidade" ou outro rótulo preferido.

![Bloco de produtos com um lado do dólar anexado ao preço do item.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Etapa 4: Configurar definições de layout

Altere as [opções de layout](#layout-options) para atualizar a forma como os produtos são exibidos em seu bloco de produtos e certifique-se de selecionar **Aplicar configurações** após cada alteração.

### Etapa 5: Pré-visualize e teste sua mensagem

{% tabs %}
{% tab Bloco dinâmico de produtos %}

1. Na seção **Preview & Test (Pré-visualização e teste** ), pré-visualize a mensagem como um usuário personalizado.
2. Especifique quantos itens você deseja renderizar na prévia.
3. Confirme se o número correto de itens é exibido e se suas opções de layout foram aplicadas corretamente. Note que os itens que aparecem são selecionados aleatoriamente.

![Guia "Pré-visualização como usuário" com uma seção suspensa "Bloco de produto dinâmico" que especifica a exibição de 4 itens.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Bloco de produto estático %}

Uma prévia será gerada no criador de arrastar e soltar quando você aplicar alterações ao bloco do produto. 

![Criador de e-mail de arrastar e soltar mostrando um bloco de produto gerado com diferentes blocos de itens.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Quando terminar de criar sua mensagem e confirmar que ela está de acordo com o esperado, você estará pronto para enviar!