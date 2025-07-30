---
nav_title: Criação de um catálogo
article_title: Criação de um catálogo
alias: "/catalogs/"
page_order: 1
description: "Este artigo de referência aborda como criar catálogos que fazem referência a dados de não usuários em suas campanhas do Braze por meio do Liquid."
---

# Criação de um catálogo

> A criação de um catálogo envolve a importação de um arquivo CSV de dados de não usuários para o Braze. Isso lhe permite acessar essas informações para enriquecer suas mensagens. Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, esses dados são algum tipo de metadados da sua empresa, como informações sobre produtos para uma empresa de comércio eletrônico ou informações sobre cursos para um provedor de educação.<br><br>Esta página aborda como preparar e fazer upload de um arquivo CSV para criar um catálogo, como gerenciar catálogos e muito mais.

Os casos de uso do Commons para catálogos incluem:

- Produtos
- Serviços
- Alimentos
- Próximos eventos
- Música
- Pacotes

Depois que essas informações forem importadas, você poderá começar a acessá-las nas mensagens de forma semelhante ao acesso a atributos personalizados ou propriedades de eventos personalizados por meio do Liquid.

## Preparando seu arquivo CSV

Antes de criar um catálogo, prepare seu arquivo CSV se seu método preferido de criação de catálogo for upload.

{% alert note %}
Precisa de mais espaço para acomodar seus arquivos CSV? Entre em contato com seu gerente de conta Braze para saber mais sobre como fazer upgrade de seus catálogos.
{% endalert %}

### Diretrizes para o arquivo CSV

Observe estas diretrizes ao criar seu arquivo CSV. A primeira coluna do arquivo CSV deve ser um cabeçalho de `id`, e o `id` de cada item deve ser exclusivo. Todos os outros nomes de colunas devem ser exclusivos. Além disso, as seguintes limitações se aplicam aos arquivos CSV do catálogo:

- Máximo de 1.000 campos (colunas)
- Nome máximo do campo (coluna) de 250 caracteres
- Máximo de 100 MB para todos os arquivos CSV combinados em sua empresa (gratuito)
- Tamanho máximo do arquivo CSV de 2 GB (Pro)
- Valor máximo do campo (célula) de 5.000 caracteres
- Somente letras, números, hífens e sublinhados para `id` e valores de cabeçalho

Também recomendamos a formatação de todo o texto em seus arquivos CSV em letras minúsculas. Codifique o arquivo CSV usando o formato UTF-8 para fazer upload do arquivo CSV na próxima etapa.

## Escolha do método

Para criar um catálogo, acesse **Configurações de dados** > **Catálogos**.

Selecione **Criar novo catálogo** e, em seguida, escolha fazer **upload de CSV** ou **criar no navegador**.

### Método 1: Fazer upload de CSV

1. Arraste e solte seu arquivo na zona de upload ou selecione **Fazer upload de CSV** e escolha seu arquivo. <br>![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"} <br><br>
2. Selecione um dos seguintes tipos de dados para cada coluna: booleano, número, string ou hora.
<br> ![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"} <br><br>
3. Dê um nome ao seu catálogo. Tenha em mente os seguintes requisitos para um nome de catálogo:
- Deve ser exclusivo
- Máximo de 250 caracteres
- Só pode incluir números, letras, hífens e sublinhados<br><br>
4. (Opcional) Adicione uma descrição para o catálogo.
5. Selecione **Processar catálogo** para criar o catálogo.

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do catálogo. Além disso, o valor `NULL` não é compatível com o upload de CSV e será tratado como uma string.
{% endalert %}

Também é possível usar modelos em um nome de catálogo. Por exemplo, você pode usar o seguinte:
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
Seu arquivo CSV pode ser rejeitado se você ultrapassar seu [nível](#tiers).
{% endalert %}

Você também pode atualizar o arquivo CSV depois de selecionar a criação de um catálogo no navegador. Selecione **Fazer upload de catálogo > Fazer upload de CSV** e, em seguida, selecione se deseja atualizar, adicionar ou excluir itens em seu catálogo.

### Método 2: Criar no navegador

Para editar ou criar catálogos no navegador, você precisará da permissão "Manage Catalogs Dashboard".

1. Digite um nome para seu catálogo. Tenha em mente os seguintes requisitos para o nome do seu catálogo:
- Deve ser exclusivo
- Até 250 caracteres
- Só pode incluir números, letras, hífens e sublinhados <br> ![Um catálogo chamado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"} <br><br>
2. (Opcional) Digite uma descrição para seu catálogo.
3. Selecione o catálogo que você acabou de criar na página List **Catalogs** para atualizar seu catálogo.
4. Selecione **Update Catalog** > **Add fields** para adicionar seus campos. Em seguida, digite o **nome do campo** e use a lista suspensa para selecionar o tipo de dados. Repita conforme necessário.<br> ![Dois campos de exemplo "rating" e "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}<br><br>
5. Selecione **Update Catalog** > **Add items** para adicionar um item ao seu catálogo, inserindo as informações com base nos campos adicionados anteriormente. Em seguida, selecione **Salvar item** ou **Salvar e adicionar outro** para continuar adicionando seus itens. <br> ![Adicionar um item de catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

Também é possível fazer upload de um arquivo CSV depois de selecionar a criação de um catálogo no navegador.

{% alert note %}
A Braze processa valores de tempo com base no registro de data e hora do dashboard. Por exemplo, se uma coluna tiver um valor de "03/13/2024" e seu fuso horário for o fuso horário do Pacífico, esse horário será importado para o Braze como "Mar 12, 2024, 5:00 PM".
{% endalert %}

#### Tutorial: Criação de um catálogo a partir de um arquivo CSV

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
    <td class="tg-0pky">Tales</td>
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

Criaremos o catálogo fazendo upload de um arquivo CSV. Os tipos de dados para `id`, `title`, `price` e `image_link` são string, string, number e string, respectivamente. 

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do catálogo.
{% endalert %}

![Quatro nomes de colunas de catálogo: "id", "title", "price", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Em seguida, nomearemos esse catálogo como "games_catalog" e selecionaremos o botão **Processar catálogo**. Em seguida, a Braze verificará se há erros no catálogo antes da criação do catálogo.

![Um catálogo chamado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Note que você não poderá editar esse nome depois que o catálogo for criado. Você pode excluir um catálogo e fazer upload novamente de uma versão atualizada usando o mesmo nome de catálogo.

Depois de criar o catálogo, você pode começar a fazer referência ao [catálogo em uma campanha]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/).

## Gerenciamento de catálogos por meio da API

À medida que cria mais catálogos, você também pode usar o [ponto de extremidade List catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) para retornar uma lista dos catálogos em um espaço de trabalho.

### Gerenciamento de itens do catálogo

Além de gerenciar seus catálogos, você também pode usar endpoints assíncronos e síncronos para gerenciar os itens do catálogo. Isso inclui a capacidade de editar e excluir itens de catálogo e de listar detalhes de itens de catálogo. 

Por exemplo, para editar um item de catálogo individual, use o [endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Níveis de catálogo {#tiers}

A versão gratuita do Catalogs suporta tamanhos de arquivo CSV de até 100 MB para todos os arquivos CSV combinados em sua empresa, enquanto a versão Catalogs Pro suporta tamanhos de arquivo CSV de até 2 GB para um único arquivo CSV.

### Armazenamento do catálogo

{% alert important %}
O direito ao pacote mostrado no dashboard da Braze é arredondado para a unidade mais próxima para fins visuais; no entanto, você ainda tem direito ao direito total adquirido. Para solicitar um upgrade para o armazenamento de catálogos, entre em contato com seu gerente de conta Braze.
{% endalert %}

#### Versão gratuita

O tamanho do armazenamento da versão gratuita dos catálogos é de até 100 MB. Você pode ter itens ilimitados, desde que eles tenham menos de 100 MB. 

#### Catálogos Pro

Em nível de empresa, o armazenamento máximo do Catalogs Pro é baseado no tamanho dos dados do catálogo. As opções de tamanho de armazenamento são: 5 GB, 10 GB ou 15 GB. Note que o armazenamento da versão gratuita (100 MB) está incluído em cada um desses planos.

