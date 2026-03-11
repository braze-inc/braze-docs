---
nav_title: Criar um catálogo
article_title: Criar um Catálogo
alias: "/catalogs/"
page_order: 1
description: "Este artigo de referência aborda como criar catálogos que fazem referência a dados de não usuários em suas campanhas do Braze por meio do Liquid."
---

# Criar um catálogo

> A criação de um catálogo envolve a importação de um arquivo CSV de dados de não usuários para o Braze. Isso lhe permite acessar essas informações para enriquecer suas mensagens. Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, esses dados são algum tipo de metadados da sua empresa, como informações sobre produtos para uma empresa de comércio eletrônico ou informações sobre cursos para um provedor de educação.

## Casos de uso

Os casos de uso do Commons para catálogos incluem:

- Produtos
- Serviços
- Alimentos
- Próximos eventos
- Música
- Pacotes

Depois que essas informações forem importadas, você poderá começar a acessá-las nas mensagens de forma semelhante ao acesso a atributos personalizados ou propriedades de eventos personalizados por meio do Liquid.

## Tipos de dados suportados {#supported-data-types}

A tabela a seguir lista os tipos de dados de catálogo suportados e como eles podem ser criados ou atualizados.

| Tipo de dados    | Descrição                                   | Disponível via upload de CSV | Disponível via API e CDI |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| String       | Uma sequência de caracteres.                     | ✅ Sim                    | ✅ Sim                     |
| Número       | Um valor numérico, seja inteiro ou flutuante.     | ✅ Sim                    | ✅ Sim                     |
| Booleano      | Um valor `true` ou `false`.                    | ✅ Sim                    | ✅ Sim                     |
| Horário         | Uma string formatada no formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).                        | ✅ Sim                    | ✅ Sim                     |
| Objeto JSON  | Um objeto aninhado com pares chave-valor. Pode ser exibido na plataforma, mas só pode ser criado ou atualizado através da API ou CDI.         | ⛔ Não                     | ✅ Sim                     |
| Array de strings | Uma lista de strings. Pode ser exibido na plataforma, mas só pode ser criado ou atualizado através da API ou CDI. Máximo de 100 elementos. | ⛔ Não                     | ✅ Sim                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Criação de um catálogo

Para criar um catálogo, Acessar **Configurações de Dados** > **Catálogos**, em seguida, selecione **Criar Novo Catálogo** e escolha uma das seguintes opções:

{% tabs local %}
{% tab Upload CSV %}
### Etapa 1: Revise seu arquivo CSV

Antes de fazer upload do seu arquivo CSV, certifique-se de que seu arquivo CSV atende aos seguintes requisitos:

| Requisito CSV | Informações |
|-----------------|---------|
| Cabeçalhos | A primeira coluna no arquivo CSV deve ser nomeada `id`, e cada linha deve ter um valor `id` único. |
| Colunas | Um arquivo CSV pode ter um máximo de 1.000 campos (colunas), e cada nome de coluna pode ter até 250 caracteres de comprimento. |
| Tamanho do arquivo | Para planos Gratuitos, o tamanho total de todos os arquivos CSV em uma empresa é limitado a 100 MB. Para planos Pro, o tamanho máximo do arquivo para um único arquivo CSV é de 2 GB. |
| Valores de campo | Cada célula (valor do campo) pode conter até 5.000 caracteres. |
| Caracteres válidos | A coluna `id` e todos os valores de cabeçalho podem conter apenas letras, números, hífens e sublinhados. |
| Tipos de dados | Os tipos de dados suportados para uploads de CSV incluem string, número, booleano e hora. Para a lista completa de tipos de dados, incluindo aqueles disponíveis apenas através da API e CDI, consulte [Tipos de dados suportados](#supported-data-types). |
| Formatação | Formate todo o texto em letras minúsculas para manter a consistência. |
| Codificação | Salve e faça upload do arquivo CSV usando a codificação UTF-8. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Precisa de mais espaço para acomodar seus arquivos CSV? Entre em contato com seu gerente de conta Braze para saber mais sobre como fazer upgrade de seus catálogos.
{% endalert %}

### Etapa 2: Fazer upload de CSV

Arraste e solte seu arquivo na zona de upload ou selecione **Fazer upload de CSV** e escolha seu arquivo.

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

Selecione um tipo de dado para cada coluna.

{% alert note %}
Esse tipo de dados não pode ser editado após a configuração do catálogo. Além disso, o valor `NULL` não é compatível com o upload de CSV e será tratado como uma string.
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

Digite um nome e uma descrição opcional para seu catálogo. Mantenha os seguintes requisitos em mente ao nomear seu catálogo:

  - Deve ser exclusivo
  - Máximo de 250 caracteres
  - Só pode incluir números, letras, hífens e sublinhados

{% alert tip %}
Você também pode [usar modelos em um nome de catálogo](#template-catalog-names), permitindo gerar nomes de catálogo dinamicamente com base em variáveis como idioma ou campanha.
{% endalert %}

![Um catálogo nomeado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

Selecione **Processar catálogo** para criar o catálogo.

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

![Quatro nomes de colunas do catálogo: "id", "título", "preço", "image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

Em seguida, nomearemos este catálogo "games_catalog" e selecionaremos o botão **Processar Catálogo**. Em seguida, a Braze verificará se há erros no catálogo antes da criação do catálogo.

![Um catálogo nomeado "games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

Note que você não poderá editar esse nome depois que o catálogo for criado. Você pode excluir um catálogo e fazer upload novamente de uma versão atualizada usando o mesmo nome de catálogo.

Depois de criar o catálogo, você pode começar a fazer referência ao [catálogo em uma campanha]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/).
{% endtab %}

{% tab Create in browser %}
### Pré-requisitos

Antes de poder editar ou criar catálogos no navegador, você precisa das seguintes [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) para seu espaço de trabalho:

- Ver catálogos
- Editar catálogos
- Exportar catálogo
- Excluir catálogos

{% multi_lang_include deprecations/user_permissions.md %}

### Etapa 1: Insira os detalhes do catálogo

Digite um nome e uma descrição opcional para seu catálogo. Mantenha os seguintes requisitos em mente ao nomear seu catálogo:

- Deve ser exclusivo
- Máximo de 250 caracteres
- Só pode incluir números, letras, hífens e sublinhados

{% alert tip %}
Você também pode [usar modelos em um nome de catálogo](#template-catalog-names), permitindo gerar nomes de catálogo dinamicamente com base em variáveis como idioma ou campanha.
{% endalert %}

![Um catálogo nomeado "my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### Etapa 2: Crie seu catálogo

Selecione seu catálogo na lista e, em seguida, selecione **Atualizar Catálogo** > **Adicionar campos**. Insira o **Nome do campo** e use o menu suspenso para selecionar o tipo de dado. Repita conforme necessário.

![Dois campos de exemplo: "rating" e "name".]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

Selecione **Update Catalog** > **Add items** para adicionar um item ao seu catálogo, inserindo as informações com base nos campos adicionados anteriormente. Em seguida, selecione **Salvar item** ou **Salvar e adicionar outro** para continuar adicionando seus itens.

![Adicionar um item de catálogo.]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
A Braze processa valores de tempo com base no registro de data e hora do dashboard. Por exemplo, se uma coluna tiver um valor de "03/13/2024" e seu fuso horário for o fuso horário do Pacífico, esse horário será importado para o Braze como "Mar 12, 2024, 5:00 PM".
{% endalert %}
{% endtab %}
{% endtabs %}

## Tipos de dados do catálogo

Os catálogos suportam vários tipos de dados para ajudar você a organizar e estruturar suas informações de forma eficaz. A tabela a seguir descreve cada tipo de dado suportado e como ele se mapeia para os nomes de tipo CSV e API:

| Tipo de dados | Formato | Exemplo | Descrição |
|-----------|--------|---------|-------------|
| String | Texto | `"Hello World"` | Qualquer sequência de caracteres usada para dados de texto, como nomes, descrições e IDs. Equivalente ao tipo `string` em importações CSV e API. |
| Horário | ISO 8601 ou timestamp Unix (segundos) | `"2024-03-15T14:30:00Z"` | Valores de data e hora formatados como ISO 8601 ou timestamp Unix em segundos. Equivalente ao tipo `time` na API e ao tipo `datetime` em importações CSV. |
| Booleano | `true` ou `false` | `true` | Valores lógicos representando estados verdadeiro ou falso. Equivalente ao tipo `boolean` em importações CSV e API. |
| Número | Inteiro ou decimal | `42` ou `19.99` | Valores numéricos, incluindo inteiros e números de ponto flutuante para preços, quantidades, classificações e mais. Equivalente aos tipos `integer` e `float` em importações CSV e ao tipo `number` na API. |
| Objeto | Objeto JSON | `{"key": "value", "price": 10}` | Estruturas de dados complexas aninhadas. O valor da API `type` é `object`. Exibido como Objeto JSON no dashboard. Disponível apenas via API ou Ingestão de Dados na Nuvem (CDI). |
| Vetor | Array de strings | `["red", "blue", "green"]` | Listas de valores de string. O valor da API `type` é `array`. Exibido como array de String no dashboard. Disponível apenas através da API ou CDI. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Usando templates em nomes de catálogo {#template-catalog-names}

Ao nomear seu catálogo, você também pode usar templates em um nome de catálogo. Isso permite gerar dinamicamente nomes de catálogo com base em variáveis como idioma ou campanha. Por exemplo, você pode usar o seguinte:

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## Gerenciando catálogos

### No dashboard

Para atualizar seu catálogo após fazer upload de um CSV ou criar um catálogo no navegador, selecione **Atualizar Catálogo > Fazer Upload de CSV**, e então selecione se deseja atualizar, adicionar ou excluir itens no seu catálogo.

### Usando a API REST

À medida que você cria mais catálogos, também pode usar o [ponto de extremidade List catalogs]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) para retornar uma lista dos catálogos em um espaço de trabalho.

A API REST suporta todos os [tipos de dados de catálogo](#supported-data-types), incluindo objetos JSON e arrays de string. Objetos JSON e arrays de string só podem ser criados ou atualizados através da API REST.

### Usando Ingestão de Dados na Nuvem

Você pode manter catálogos através da [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) sincronizando dados de catálogo diretamente do seu data warehouse (como Snowflake, Redshift, BigQuery, Databricks, Microsoft Fabric ou S3) em uma base programada.

## Gerenciamento de itens do catálogo

Além de gerenciar seus catálogos, você também pode usar endpoints assíncronos e síncronos para gerenciar os itens do catálogo. Isso inclui a capacidade de editar e excluir itens de catálogo e de listar detalhes de itens de catálogo. 

Por exemplo, para editar um item de catálogo individual, use o [endpoint `/catalogs/catalog_name/items/item_id`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/).

## Armazenamento de catálogo {#tiers}

A versão gratuita do Catalogs suporta tamanhos de arquivo CSV de até 100 MB para todos os arquivos CSV combinados em sua empresa, enquanto a versão Catalogs Pro suporta tamanhos de arquivo CSV de até 2 GB para um único arquivo CSV.

{% alert important %}
O direito ao pacote mostrado no dashboard da Braze é arredondado para a unidade mais próxima para fins visuais; no entanto, você ainda tem direito ao direito total adquirido. Para solicitar um upgrade para o armazenamento de catálogos, entre em contato com seu gerente de conta Braze.
{% endalert %}

#### Versão gratuita

O tamanho do armazenamento da versão gratuita dos catálogos é de até 100 MB. Você pode ter itens ilimitados desde que estejam abaixo de 100 MB. 

#### Catálogos Pro

Em nível de empresa, o armazenamento máximo do Catalogs Pro é baseado no tamanho dos dados do catálogo. As opções de tamanho de armazenamento são: 5 GB, 10 GB ou 15 GB. Note que o armazenamento da versão gratuita (100 MB) está incluído em cada um desses planos.
