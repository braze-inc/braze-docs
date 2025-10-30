---
nav_title: Seleções
article_title: Seleções
page_order: 5
description: "Este artigo de referência aborda como criar e usar seleções com seus catálogos para fazer referência a dados em suas campanhas no Braze."
---

# Seleções

> As seleções são grupos de dados que podem ser usados para personalizar uma mensagem para cada usuário em sua campanha. Ao usar uma seleção, você está basicamente configurando filtros personalizados com base em colunas específicas do seu catálogo. Isso pode incluir filtros para marca, tamanho, local, data de adição e muito mais. Isso lhe dá controle sobre o que está sendo exibido aos usuários, permitindo que você defina critérios que os itens devem atender primeiro.<br><br>Esta página aborda como criar e usar seleções com seus catálogos.

Depois de criar um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/), você pode fazer referência aos dados do catálogo incorporando seleções em suas campanhas ou recomendações do Braze.

\![A seção Seleções em um catálogo de exemplo.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Coisas para saber

- Você pode criar até 30 seleções por catálogo.
- Você pode adicionar até 10 filtros por seleção.
- As seleções são ótimas para refinar as recomendações dos dados do catálogo Braze. Se estiver procurando inspiração, consulte [as recomendações do item Sobre]({{site.baseurl}}/user_guide/brazeai/recommendations/) para ver exemplos de casos de uso.

## Criação de uma seleção

Para criar uma seleção, faça o seguinte.

1. Vá para **Catalogs (Catálogos** ) e selecione seu catálogo na lista.
2. Selecione a guia **Selection (Seleção** ) e clique em **Create Selection (Criar seleção)**.
3. Dê um nome e uma descrição opcional à sua seleção.
4. Em **Filter Field (Campo de filtro**), selecione a coluna do catálogo pela qual você deseja filtrar. Os campos de cadeia de caracteres com mais de 1.000 caracteres não podem ser selecionados para filtros.
5. Termine de definir seus critérios de filtro selecionando o operador relevante (por exemplo, "igual" ou "não igual") e o atributo.
6. Na seção **Sort type (Tipo de classificação** ), determine como os resultados são classificados. Por padrão, os resultados são retornados em nenhuma ordem específica. Para especificar a classificação por um campo específico, desative a opção **Randomize Sort Order** e especifique o **Sort Field** e **a Sort Order** (ascendente ou descendente).
7. Na seção **Limite de resultados**, insira os resultados (até 50).
8. Selecione **Criar seleção**.

### Teste e visualização

Depois de criar uma seleção, você pode usar a seção **Visualizar para usuário** para ver o que uma seleção retornaria para um usuário aleatório ou um usuário específico. Para seleções que usam personalização, só é possível visualizar a pré-visualização depois de selecionar um usuário.

### Líquido nos resultados da seleção

O uso de qualquer Liquid em catálogos, como atributos personalizados e eventos personalizados, pode resultar em resultados diferentes retornados para cada usuário em sua seleção. 

{% alert note %}
O Connected Content Liquid não é compatível com essas configurações de filtro.
{% endalert %}

Configurações de filtro para seleção de catálogo em que o atributo é definido como um atributo personalizado Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Uso de seleções em mensagens

Depois de criar sua seleção, personalize suas mensagens com o Liquid para inserir os itens filtrados desse catálogo. Você pode fazer com que o Braze gere o Liquid para você na janela de personalização encontrada nos compositores de mensagens:

1. Em qualquer compositor de mensagem que ofereça suporte à personalização, selecione <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Adicionar personalização"></i> para abrir a janela de personalização.
2. Em **Personalization Type (Tipo de personalização**), selecione **Catalog Items (Itens de catálogo**).
3. Selecione o nome do catálogo.
4. Para **Método de seleção de item**, selecione **Usar uma seleção**.
4. Selecione sua seleção na lista.
5. Em **Informações a serem exibidas**, selecione quais campos do catálogo devem ser incluídos para cada item.
6. Selecione o ícone **Copiar** e cole o Liquid onde quer que ele esteja em sua mensagem.

\![O modal Add Personalization com as seguintes seleções: "Catalog Items" (Itens do catálogo) para "Personalization Type" (Tipo de personalização), "Games" (Jogos) para "Catalog Name" (Nome do catálogo), "Selections" (Seleções) para "Selection Type" (Tipo de seleção), "game_selection" para "Selection" (Seleção) e "title" (Título) e "description_en" para "Information to Display" (Informações a serem exibidas).]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Caso de uso

Digamos que você tenha um serviço de entrega de refeições e queira enviar uma mensagem personalizada aos seus usuários que têm preferências específicas de refeições com base na categoria de alimentos visualizada mais recentemente. 

Usando um catálogo com as informações do seu serviço de entrega de refeições para o nome da refeição, o preço, a imagem e a categoria da refeição, é possível criar uma seleção para recomendar três refeições com base na categoria visualizada mais recentemente por um usuário.

Exemplo de uma seleção para um serviço de entrega de refeições com dois filtros: um que identifica um tipo de produto como uma refeição e outro que identifica a categoria como a mais recentemente visualizada. A seleção é definida para randomizar a ordem em que os três resultados são retornados.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Para usar esse catálogo e essa seleção em uma campanha, use o modal **Adicionar personalização** na seção de composição de mensagens da criação de uma campanha. Neste exemplo, selecionamos o catálogo com as informações do seu serviço de entrega de refeições e a seleção para recomendações de refeições com base na categoria visualizada mais recentemente. Isso nos permite exibir o nome e o preço da refeição. Para reforçar ainda mais sua mensagem, você pode usar a seleção para adicionar também uma imagem da primeira refeição recomendada.

Um Content Card com o cabeçalho "You will LOVE these highly rated meals!" (Você vai adorar essas refeições bem avaliadas!) com a seleção "recommendations_be_recent_category" na seção de composição da mensagem.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Por exemplo, digamos que você tenha um usuário cuja categoria visualizada mais recentemente seja "Frango". Usando a personalização definida e uma campanha de Content Card, você pode enviar três recomendações de refeições que incluam frango para esse usuário.

Um Content Card com uma imagem de frango grelhado com limão e uma lista de três recomendações de refeições que incluem frango com base na categoria visualizada mais recentemente pelo usuário.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Usando a mesma personalização, você também pode enviar três recomendações de refeições para um usuário cuja categoria visualizada mais recentemente seja "Carne bovina".

\![Um Content Card com uma imagem de estrogonofe de carne e uma lista de duas recomendações de refeições que incluem carne bovina com base na categoria visualizada mais recentemente pelo usuário.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}


