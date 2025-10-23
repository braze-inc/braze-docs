---
nav_title: Sincronização de produtos da Shopify
article_title: Sincronização de produtos da Shopify
alias: /shopify_catalogs/
page_order: 4
description: "Este artigo de referência aborda como importar seus produtos da Shopify para os catálogos da Braze."
---

# Sincronização de produtos do Shopify 

> Você pode sincronizar todos os produtos de sua loja Shopify com um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) Braze para uma personalização mais profunda do envio de mensagens. 

Os catálogos da Shopify serão atualizados quase em tempo real à medida que você fizer edições e alterações nos produtos da sua loja da Shopify. É possível enriquecer seu carrinho abandonado, a confirmação do pedido e muito mais com os detalhes e as informações mais atualizadas do produto.

## Configurando sua sincronização de produtos da Shopify {#setting-up}

Se já tiver instalado sua loja Shopify, você ainda poderá sincronizar seus produtos seguindo as instruções abaixo. 

### Etapa 1: Ativar a sincronização

Você pode sincronizar seus produtos com um catálogo do Braze por meio do fluxo de instalação do Shopify ou na página de parceiros do Shopify. 

![Etapa 3 do processo de configuração com "Shopify Variant ID" como o "Catalog product identifier" (Identificador de produto do catálogo).]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Os produtos sincronizados com um catálogo Braze contribuirão para seu [limite de catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits).

### Etapa 2: Selecione o identificador de seu produto

Selecione o identificador de produto a ser usado como ID do catálogo:
- ID de variante da Shopify
- SKU

Os valores de ID e de cabeçalho para o identificador de produto que você escolher só podem incluir letras, números, hífens e sublinhados. Se o identificador do produto não seguir esse formato, a Braze o removerá da sincronização do catálogo.

Esse será o principal identificador que você usará para fazer referência às informações do catálogo do Braze. 

{% alert note %}
Se estiver selecionando SKU como ID do catálogo, certifique-se de que todos os seus produtos e variantes em sua loja tenham um conjunto de SKUs e que eles sejam exclusivos. 
- Se um item tiver um SKU ausente, o Braze não poderá sincronizar esse produto no catálogo. 
- Se você tiver mais de um produto com o mesmo SKU, isso pode causar um comportamento inesperado ou fazer com que as informações do produto sejam substituídas involuntariamente pelo SKU duplicado.
{% endalert %}

### Etapa 3: Sincronização em andamento

Você receberá uma notificação no dashboard e seu status será exibido como "In Progress" (Em andamento) para indicar que a sincronização inicial está começando. Note que o tempo necessário para a conclusão da sincronização depende do número de produtos e variantes que a Braze precisa sincronizar do Shopify. Durante esse período, você pode sair desta página e aguardar uma notificação do dashboard ou um e-mail para notificá-lo quando isso for concluído.

Note que, se a sincronização inicial exceder o [limite de seu catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits), o Braze interromperá a sincronização de mais produtos. Se você exceder o limite depois que a sincronização for bem-sucedida devido à adição de novos produtos ao longo do tempo, a sincronização não estará mais ativa. Em ambos os casos, as atualizações de produtos da Shopify não serão mais refletidas na Braze. Entre em contato com o gerente da sua conta para considerar a possibilidade de fazer upgrade do seu nível. 

### Etapa 4: Sincronização concluída

Você receberá uma notificação no dashboard e um e-mail depois que a sincronização for bem-sucedida. A página de parceiro da Shopify também atualizará o status dos catálogos da Shopify para "Sincronizando". Para visualizar seus produtos, clique no nome do catálogo na página de parceiro da Shopify.

Consulte [os casos de uso adicionais do Catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases) para saber mais sobre como aproveitar os dados do catálogo para personalizar sua mensagem.

#### Dados de catálogo compatíveis com o Shopify

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Modificar o catálogo da Shopify de alguma forma pode interferir involuntariamente nas sincronizações de produtos em tempo real. Não faça edições no catálogo da Shopify, pois elas poderão ser desfeitas pela Shopify. Em vez disso, faça as atualizações necessárias do produto em sua instância da Shopify.<br><br>Para excluir seu catálogo do Shopify, acesse a página do Shopify e desative a sincronização. Não exclua o catálogo da Shopify diretamente na página de catálogos.
{% endalert %}

##### Usando `product_handle` ou `product_url`

Para acessar e usar `product_handle` e `product_url`, desconecte e reconecte seu catálogo Shopify fazendo o seguinte.

1. Acesse a página de integração do Shopify e selecione **Editar configuração**.

![Página de integração do Shopify.]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\. Na etapa **Sincronizar catálogo**, desative o catálogo e, em seguida, atualize as configurações.
3\. Ative o catálogo e atualize as configurações.

![Shopify "Sincronizar catálogo" etapa com alternância de catálogo.]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## Casos de uso de reposição de estoque e queda de preço

Para configurar notificações de chegada de estoque, siga as etapas [aqui]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications).

Para configurar notificações de queda de preço, siga as etapas [aqui]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/).

Note que, com a integração do Shopify, será necessário criar um evento personalizado que capture o status da inscrição de um usuário em seu catálogo para cada caso de uso. O evento personalizado exigirá uma propriedade de evento que mapeie o [SKU ou o ID da variante do Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) que você selecionou como parte da sincronização do produto do Shopify. 

## Alteração do ID do catálogo

Para alterar o identificador de produto de seu catálogo da Shopify, você precisará desativar a sincronização. Confirme que você parou de enviar mensagens usando esses dados do catálogo da Shopify primeiro. Execute novamente a sincronização inicial do catálogo da Shopify e selecione o identificador de produto desejado seguindo as etapas [de sincronização do produto](#setting-up).

## Desativar a sincronização do produto {#deactivate}

A desativação do recurso de sincronização de produtos da Shopify excluirá o catálogo completo e os produtos. Isso também pode afetar quaisquer mensagens que possam estar usando ativamente os dados do produto desse catálogo. Confirme se você atualizou ou pausou essas campanhas ou Canvas antes da desativação, pois isso pode resultar no envio de mensagens sem detalhes do produto. Não exclua o catálogo da Shopify diretamente na página de catálogos.

## Solução de problemas
Se sua sincronização de produtos do Shopify apresentar um problema, ele poderá ser resultado dos seguintes erros. Siga as instruções sobre como corrigir o problema e resolver a sincronização:

| Erro | Motivo | Solução |
| --- | --- | --- |
| Erro do servidor | Isso ocorre se houver um erro de servidor no lado da Shopify quando tentamos sincronizar seus produtos. | [Desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| SKU duplicada | Isso ocorre se você usar um SKU como ID do item do catálogo e tiver produtos com o mesmo SKU. Como o ID do item do catálogo deve ser exclusivo, todos os seus produtos devem ter SKUs exclusivos. | Faça uma auditoria em sua lista completa de produtos e variantes na Shopify para garantir que não haja SKUs duplicados. Se houver SKUs duplicados, atualize-os para que sejam SKUs exclusivos somente em sua conta da loja da Shopify. Depois que isso for corrigido, [desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| Limite de catálogo excedido | Isso ocorre se você exceder o limite do catálogo. O Braze não poderá concluir a sincronização ou manter a sincronização ativa devido ao fato de não haver mais disponibilidade de armazenamento. | Há duas soluções para esse problema:<br><br>1\. Entre em contato com o gerente da conta para fazer upgrade da cota e aumentar o limite do catálogo. <br><br>2\. Libere espaço de armazenamento excluindo qualquer um dos seguintes itens:<br>\- Catalogar itens de outros catálogos<br>\- Outros catálogos<br>\- Seleções criadas<br><br> Depois de usar qualquer uma das soluções, a sincronização deve ser desativada e reativada em seguida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

