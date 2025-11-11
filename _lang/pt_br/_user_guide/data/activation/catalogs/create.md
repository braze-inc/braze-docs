---
nav_title: Criação de um catálogo
article_title: Criação de um catálogo
alias: "/catalogs/"
page_order: 1
description: "Este artigo de referência aborda como criar catálogos que fazem referência a dados de não usuários em suas campanhas do Braze por meio do Liquid."
---

# Criação de um catálogo

> A criação de um catálogo envolve a importação de um arquivo CSV de dados de não usuários para o Braze. Isso permite que você acesse essas informações para enriquecer suas mensagens. Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, esses dados são algum tipo de metadados da sua empresa, como informações sobre produtos para uma empresa de comércio eletrônico ou informações sobre cursos para um provedor de educação.

## Casos de uso

Os casos de uso do Commons para catálogos incluem:

- Produtos
- Serviços
- Alimentos
- Próximos eventos
- Música
- Pacotes

Depois que essas informações forem importadas, você poderá começar a acessá-las nas mensagens de modo semelhante ao acesso a atributos personalizados ou propriedades de eventos personalizados por meio do Liquid.

## Criação de um catálogo

Para criar um catálogo, vá para **Configurações de dados** > **Catálogos**, selecione **Criar novo catálogo** e escolha uma das seguintes opções:

{% tabs local %}
{% tab Upload CSV %}
### Etapa 1: Revise seu arquivo CSV

Antes de carregar o arquivo CSV, verifique se ele atende aos seguintes requisitos:

| Requisito de CSV | Detalhes |
|-----------------|---------|
| Cabeçalhos | A primeira coluna do arquivo CSV deve ser denominada `id` e cada linha deve ter um valor exclusivo `id`. |
| Colunas | Um arquivo CSV pode ter no máximo 1.000 campos (colunas), e cada nome de coluna pode ter até 250 caracteres. |
| Tamanho do arquivo | Nos planos Free, o tamanho total de todos os arquivos CSV de uma empresa é limitado a 100 MB. Para os planos Pro, o tamanho máximo de um único arquivo CSV é de 2 GB. |
| Valores de campo | Cada célula (valor de campo) pode conter até 5.000 caracteres. |
| Caracteres válidos | A coluna `id` e todos os valores de cabeçalho só podem conter letras, números, hífens e sublinhados. |
| Tipos de dados | Os tipos de dados compatíveis com o upload de um arquivo CSV incluem string, integer, float, boolean ou datetime. |
| Formatação | Formate todo o texto em letras minúsculas para manter a consistência. |
| Codificação | Salve e carregue o arquivo CSV usando a codificação UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Precisa de mais espaço para acomodar seus arquivos CSV? Entre em contato com seu gerente de conta Braze para obter mais informações sobre a atualização de seus catálogos.
{% endalert %}

### Etapa 2: Carregar CSV

Arraste e solte seu arquivo na zona de upload ou selecione **Upload CSV** e escolha seu arquivo.

\![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Selecione um tipo de dados para cada coluna.

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do catálogo. Além disso, um valor `NULL` não é compatível com o upload de CSV e será tratado como uma cadeia de caracteres.
{% endalert %}

\![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Digite um nome e uma descrição opcional para seu catálogo. Tenha em mente os seguintes requisitos ao nomear seu catálogo:

  - Deve ser exclusivo
  - Máximo de 250 caracteres
  - Só pode incluir números, letras, hífens e sublinhados

{% alert tip %}
Também é possível [usar modelos em um nome de catálogo](#template-catalog-names), o que permite gerar dinamicamente nomes de catálogos com base em variáveis como idioma ou campanha.
{% endalert %}

\![Um catálogo chamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Selecione **Process Catalog** para criar o catálogo.

{% alert important %}
Seu arquivo CSV pode ser rejeitado se você ultrapassar seu [nível](#tiers).
{% endalert %}

### Tutorial: Criação de um catálogo a partir de um arquivo CSV

Para este tutorial, estamos usando um catálogo que lista dois jogos, seu custo e um link de imagem.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">título</th>
    <th class="tg-0pky">preço</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Contos</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneração</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

Criaremos o catálogo fazendo o upload de um arquivo CSV. Os tipos de dados para `id`, `title`, `price` e `image_link` são string, string, number e string, respectivamente. 

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do catálogo.
{% endalert %}

\![Quatro nomes de coluna do catálogo: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Em seguida, nomearemos esse catálogo como "games_catalog" e selecionaremos o botão **Process Catalog (Processar catálogo** ). Em seguida, o Braze verificará se há erros no catálogo antes da criação do catálogo.

\![Um catálogo chamado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Observe que você não poderá editar esse nome depois que o catálogo for criado. Você pode excluir um catálogo e fazer o upload novamente de uma versão atualizada usando o mesmo nome de catálogo.

Depois de criar o catálogo, você pode começar a fazer referência ao [catálogo em uma campanha]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Pré-requisitos

Antes de poder editar ou criar catálogos no navegador, você precisará da permissão **Manage Catalogs Dashboard**.

### Etapa 1: Insira os detalhes do catálogo

Digite um nome e uma descrição opcional para seu catálogo. Tenha em mente os seguintes requisitos ao nomear seu catálogo:

- Deve ser exclusivo
- Máximo de 250 caracteres
- Só pode incluir números, letras, hífens e sublinhados

{% alert tip %}
Também é possível [usar modelos em um nome de catálogo](#template-catalog-names), o que permite gerar dinamicamente nomes de catálogos com base em variáveis como idioma ou campanha.
{% endalert %}

\![Um catálogo chamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Etapa 2: Crie seu catálogo

Selecione seu catálogo na lista e, em seguida, selecione **Update Catalog** > **Add fields**( **Atualizar catálogo** > **Adicionar campos**). Digite o **nome do campo** e use o menu suspenso para selecionar o tipo de dados. Repita conforme necessário.

\![Dois campos de exemplo "rating" e "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Selecione **Update Catalog** > **Add items** para adicionar um item ao seu catálogo, inserindo as informações com base nos campos adicionados anteriormente. Em seguida, selecione **Salvar item** ou **Salvar e adicionar outro** para continuar adicionando seus itens.

\![Adicionar um item de catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
O Braze processa valores de tempo com base no registro de data e hora do painel. Por exemplo, se uma coluna tiver um valor de "03/13/2024" e seu fuso horário for o fuso horário do Pacífico, esse horário será importado para o Braze como "Mar 12, 2024, 5:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Uso de modelos em nomes de catálogos {#template-catalog-names}

Ao nomear seu catálogo, você também pode usar modelos em um nome de catálogo. Isso permite que você gere dinamicamente nomes de catálogos com base em variáveis como idioma ou campanha. Por exemplo, você pode usar o seguinte:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gerenciamento de catálogos

### No painel de controle

Para atualizar o catálogo após carregar um CSV ou criar um catálogo no navegador, selecione **Update Catalog > Upload CSV** e, em seguida, selecione se deseja atualizar, adicionar ou excluir itens do catálogo.

### Usando a API REST

À medida que você cria mais catálogos, também pode usar o [ponto de extremidade List catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) para retornar uma lista dos catálogos em um espaço de trabalho.

Os tipos de dados compatíveis com o uso da API incluem: string, integer, float, boolean ou datetime. Você também pode fazer upload de matrizes e objetos ao gerenciar seus catálogos com a API.

## Gerenciamento de itens de catálogo

Além de gerenciar seus catálogos, você também pode usar endpoints assíncronos e síncronos para gerenciar os itens do catálogo. Isso inclui a capacidade de editar e excluir itens de catálogo e de listar detalhes de itens de catálogo. 

Por exemplo, se você quiser editar um item de catálogo individual, poderá usar o [ponto de extremidade`/catalogs/catalog_name/items/item_id` ]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Armazenamento do catálogo {#tiers}

A versão gratuita do Catalogs suporta tamanhos de arquivo CSV de até 100 MB para todos os arquivos CSV combinados em sua empresa, enquanto a versão Catalogs Pro suporta tamanhos de arquivo CSV de até 2 GB para um único arquivo CSV.

{% alert important %}
O direito ao pacote mostrado no painel do Braze é arredondado para a unidade mais próxima para fins visuais; no entanto, você ainda tem direito ao direito total adquirido. Para solicitar um upgrade para o armazenamento de catálogo, entre em contato com o gerente da sua conta Braze.
{% endalert %}

#### Versão gratuita

O tamanho do armazenamento da versão gratuita dos catálogos é de até 100 MB. Você pode ter itens ilimitados, desde que eles tenham menos de 100 MB. 

#### Catálogos Pro

Em nível de empresa, o armazenamento máximo do Catalogs Pro é baseado no tamanho dos dados do catálogo. As opções de tamanho de armazenamento são: 5 GB, 10 GB ou 15 GB. Observe que o armazenamento da versão gratuita (100 MB) está incluído em cada um desses planos.
