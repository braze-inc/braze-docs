---
nav_title: Uso de catálogos
article_title: Uso de catálogos
page_order: 1.5
description: "Este artigo de referência aborda como usar catálogos para fazer referência a dados de não usuários em suas campanhas do Braze por meio do Liquid."
---

# Uso de catálogos em uma mensagem

> Depois de criar um catálogo, é possível fazer referência a dados de não usuários em suas campanhas do Braze por meio do [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Você pode usar catálogos em todos os seus canais de envio de mensagens, inclusive em qualquer lugar do editor de arrastar e soltar em que o Liquid seja compatível.

## Etapa 1: Adicionar tipo de personalização {#step-one-personalization}

No criador de mensagens de sua escolha, selecione o ícone de adição <i class="fas fa-plus-circle"></i> para abrir o modal **Add Personalization (Adicionar personalização** ) e selecione **Catalogs Items (Itens de catálogos** ) para o **tipo de personalização**. Em seguida, selecione o **nome do catálogo**. Usando nosso exemplo anterior, selecionaremos o catálogo "Games" (Jogos).

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Podemos ver imediatamente a prévia do Liquid a seguir:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

## Etapa 2: Selecione os itens do catálogo

Em seguida, é hora de adicionar seus itens de catálogo! Usando o menu suspenso, selecione os itens do catálogo e as informações a serem exibidas. Essas informações correspondem às colunas do arquivo CSV feito upload e usado para gerar seu catálogo.

Por exemplo, para fazer referência ao título e ao preço do nosso jogo Tales, poderíamos selecionar `id` para Tales (1234) como o item do catálogo e solicitar `title` e `price` para as informações exibidas.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

O resultado é o seguinte:

> Adquira o Tales por apenas 7,49!

## Exportação de catálogos

Há duas maneiras de exportar catálogos do dashboard: 

- Passe o mouse sobre a linha do catálogo na seção **Catalogs (Catálogos** ). Em seguida, selecione o botão **Exportar catálogo**.
- Selecione seu catálogo. Em seguida, selecione o botão **Exportar catálogo** na guia **Pré-visualização** do catálogo.

Você receberá um e-mail para baixar o arquivo CSV depois de iniciar a exportação. Você terá até quatro horas para recuperar esse arquivo.

## Casos de uso adicionais

### Vários itens

Você não está limitado a apenas um item em uma única mensagem. Você pode usar o modal **Add Personalization** para adicionar até três itens de catálogo por vez. Para adicionar mais itens à sua mensagem, selecione **Add Personalization (Adicionar personalização)** no criador de mensagens e selecione os itens adicionais do catálogo e as informações a serem exibidas.

Veja este exemplo em que adicionamos o endereço `id` de três jogos, Tales, Teslagrad e Acaratus, para **Catalog Items** e selecionamos `title` para **Information to Display**.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Podemos personalizar ainda mais nossa mensagem adicionando algum texto ao redor de nosso Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

O retorno é o seguinte:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Confira [as seleções]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) para criar grupos de dados para envio de mensagens mais personalizadas!
{% endalert %}

### Usando declarações do Liquid `if` 

Você pode usar itens de catálogo para criar instruções condicionais. Por exemplo, você pode disparar uma determinada mensagem para ser exibida quando um item específico for selecionado em sua campanha.

Para fazer isso, você usará uma instrução Liquid `if`, como neste exemplo:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

Neste exemplo, serão exibidas mensagens diferentes se o atributo personalizado `venue_name` tiver mais de 10 caracteres ou menos de 10 caracteres. Se `venue_name` for `blank`, nada será exibido. 

Note que você deve declarar a lista de catálogos e, se aplicável, a seleção antes de usar as declarações `if`. No exemplo, `item-list` é a lista de catálogos e `selections` é o nome da seleção.

### Usando imagens {#using-images}

Você também pode fazer referência a imagens no catálogo para usar em seu envio de mensagens. Para fazer isso, use a tag `catalogs` e o objeto `item` no campo Liquid para imagens.

Por exemplo, para adicionar o `image_link` do nosso catálogo de jogos à nossa mensagem promocional para Tales, selecione `id` para o campo **Catalog Items (Itens do catálogo** ) e `image_link` para o campo **Information to Display (Informações a serem exibidas** ). Isso adiciona as seguintes tags Liquid ao nosso campo de imagem:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Criador do cartão de conteúdo com a tag Liquid do catálogo usada no campo de imagem.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Veja como isso se parece quando o Liquid é renderizado:

![Exemplo de cartão de conteúdo com as tags Liquid do catálogo renderizadas.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Modelo de itens de catálogo

Você também pode usar modelos para extrair dinamicamente itens do catálogo com base em atributos personalizados. Por exemplo, digamos que um usuário tenha o atributo personalizado `wishlist`, que contém uma matriz de IDs de jogos do seu catálogo.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
Os objetos JSON nos catálogos só são ingeridos por meio da API. Não é possível fazer upload de um objeto JSON usando um arquivo CSV.
{% endalert %}

Usando o envio de mensagens Liquid, você pode extrair dinamicamente os IDs da lista de desejos e usá-los em sua mensagem. Para fazer isso, [atribua uma variável]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) ao seu atributo personalizado e, em seguida, use o modal **Add Personalization** para extrair um item específico da matriz. As variáveis referenciadas como ID do item de catálogo devem ser colocadas entre colchetes para serem referenciadas corretamente, como `{{result}}`.

{% alert tip %}
Lembre-se de que as matrizes começam em `0`, e não em `1`.
{% endalert %}

Por exemplo, para informar a um usuário que o Tales (um item do nosso catálogo que ele desejou) está em promoção, podemos adicionar o seguinte ao nosso criador de mensagens:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Que será exibido da seguinte forma:
> Adquira o Tales agora, por apenas 7,49!

Com o modelo, é possível renderizar um item de catálogo diferente para cada usuário com base em seus atributos personalizados individuais, propriedades de eventos ou qualquer outro campo modelável.

### Fazendo upload de um CSV

Você pode fazer upload de um CSV de novos itens de catálogo a serem adicionados ou de itens de catálogo a serem atualizados. Para excluir uma lista de itens, você pode fazer upload de um CSV de IDs de itens para excluí-los.

### Usando Liquid

Você também pode reunir manualmente os catálogos com a lógica Liquid. No entanto, note que se você digitar um ID que não existe, a Braze ainda retornará um vetor de itens sem objetos. Recomendamos que você inclua o tratamento de erros, como a verificação do tamanho da matriz e o uso de uma instrução `if` para considerar o caso de uma matriz vazia.

{% alert note %}
Atualmente, o Liquid não pode ser usado dentro de catálogos. Se a personalização Liquid estiver listada dentro de uma célula em seu catálogo, o valor dinâmico não será renderizado e somente o Liquid real será exibido.
{% endalert %}

#### Modelo de itens de catálogo, incluindo Liquid

Semelhante ao [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), você deve usar o sinalizador `:rerender` em uma tag Liquid para renderizar o conteúdo Liquid de um item de catálogo. Observe que o sinalizador `:rerender` tem apenas um nível de profundidade, o que significa que não se aplicará a nenhuma chamada de tag Liquid aninhada.

Se um item de catálogo contiver campos de perfil de usuário (dentro de uma tag de personalização do Liquid), esses valores deverão ser definidos no Liquid no início da mensagem e antes do modelo para que o Liquid seja renderizado corretamente. Se o sinalizador `:rerender` não for fornecido, ele renderizará o conteúdo bruto do Liquid.

Por exemplo, se um catálogo chamado "Messages" tiver um item com este Liquid:

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Para renderizar o seguinte conteúdo Liquid:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Isso será exibido da seguinte forma:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
As Liquid tags do catálogo não podem ser usadas recursivamente dentro de catálogos.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
