---
nav_title: Treasure Data
article_title: Importação de coortes do Treasure Data
description: "Este artigo de referência descreve a funcionalidade de importação de coortes do Treasure Data."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Importação de coortes do Treasure Data

> Este artigo descreve como fazer a importação de coortes de usuários do Treasure Data para o Braze para que você possa enviar campanhas direcionadas com base em dados que podem existir apenas em seu data warehouse.

{% alert important %}
Esse recurso está em beta. Para saber mais, entre em contato com os representantes do Treasure Data e da Braze.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Treasure Data | É necessário ter uma conta do [Treasure Data](https://www.treasuredata.com/) para usar a parceria. |
| Chave de importação de dados do Braze | Isso pode ser capturado no dashboard do Braze em **Partner Integrations** > **Technology Partners** e, em seguida, selecione **Treasure Data**. |
| Endpoint REST  do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
| Endereço IP estático dos dados do Treasure | O endereço IP estático do Treasure Data é o ponto de acesso e a fonte da vinculação para essa integração. Para determinar o endereço IP estático, fale com o representante de sucesso do cliente do Treasure Data ou com o suporte técnico do Treasure Data. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de importação de dados

### Etapa 1: Obtenha sua chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Treasure Data**. Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente.

### Etapa 2: Criar uma conexão de dados

Antes de criar sua conexão de dados no Treasure Data, você precisará se autenticar. Primeiro, selecione **Integrations Hub** (Hub de integrações) e, em seguida, **Catalog** (Catálogo).

![Catálogo do Hub de Integrações de Dados do Tesouro]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

Procure a integração do Braze no **catálogo**, passe o mouse sobre o ícone e selecione **Create Authentication (Criar autenticação**). Digite suas credenciais, dê um nome à sua autenticação e selecione **Done** (Concluído).

![Catálogo do Hub de Integrações de Dados do Tesouro]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### Etapa 3: Defina o público de seu coorte

Sincronize seus coortes com o Braze por meio de uma ativação no **Audience Studio** ou da execução de uma consulta no **Data Workbench**.

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

{% tabs local %}
{% tab Bancada de dados %}
#### Etapa 3.1: defina sua consulta

{% alert note %}
As colunas da consulta devem ser especificadas com os nomes exatos das colunas e o tipo de dados. As colunas da consulta devem incluir pelo menos uma das colunas `user_ids` e `device_ids`, ou a coluna do alias da Braze deve corresponder à configuração na interface do usuário. Somente os perfis de usuário existentes no Braze serão adicionados a um coorte. A importação de coorte não criará novos perfis de usuário.
{% endalert %}

1. Navegue até **Data Workbench** (Workbench de dados) > **Queries** (Consultas).
2. Selecione **New Query (Nova consulta**).
3. Execute a consulta para validar o conjunto de resultados.

![Catálogo do Hub de Integrações de Dados do Tesouro]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### Caso de uso: Sincronização de coortes por identificador

{% subtabs local %}
{% subtab Syncing External IDs %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
O nome da coluna deve ser `user_ids` ou a sincronização falhará.
{% endalert %}

Para sincronizar coortes usando o ID externo, execute a seguinte consulta:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

Depois de executar a consulta, estes aliases de usuário serão adicionados à coorte na Braze:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

Para sincronizar coortes usando o alias de usuário, execute a seguinte consulta:

```sql
SELECT
  email
FROM
  example_cohort_table
```

Depois de executar a consulta, estes aliases de usuário serão adicionados à coorte na Braze:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
Aqui está um exemplo de tabela no Treasure Data:

| external_id |	e-mail	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
O nome da coluna deve ser `device_ids` ou a sincronização falhará.
{% endalert %}

Para sincronizar coortes usando o ID do dispositivo, execute a seguinte consulta:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

Depois de executar a consulta, estes IDs de dispositivo serão adicionados à coorte na Braze:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### Etapa 3.2: Especifique o direcionamento da exportação de resultados

Depois que a consulta tiver sido criada, selecione **Export Results** (Exportar resultados). Você pode selecionar uma autenticação existente, como a criada nas últimas etapas, ou criar uma nova autenticação a ser usada na saída. 

![Catálogo do Hub de Integrações de Dados do Tesouro]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| Mapeamento de resultados de exportação |	Descrição	| 
| ----------- | ----------- |
| ID do coorte	| Esse é o identificador de coorte de backend que será enviado ao Braze. 	|
| Nome do coorte (opcional)	| Esse é o nome que aparecerá no Filtro de coorte na ferramenta de segmentação do Braze. Se isso não for definido, o `Cohort ID` será usado como `Cohort Name`.	|
| Operação	| Usado para determinar se a consulta deve adicionar ou remover perfis do coorte no Braze.	| 
| Aliases (opcional) | Quando definido, o nome da coluna correspondente em sua consulta será enviado como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`.	| 
| Contagem de fios | Número de chamadas simultâneas à API. |

Siga [as etapas do Treasure Data](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget) para configurar sua exportação para atender ao seu caso de uso.

#### Etapa 3.3: Executar a consulta

Salve a consulta com um nome e execute, ou simplesmente execute a consulta. Após a conclusão bem-sucedida da consulta, o resultado é automaticamente exportado para a Braze.

{% endtab %}
{% tab Audience Studio %}
#### Etapa 3.1: Criar uma ativação

Crie um novo segmento ou escolha um segmento existente para sincronizar com o Braze como um coorte. No segmento, selecione **Criar ativação**.

#### Etapa 3.2: preencha seus dados de ativação

![Dados de ativação das integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| Configuração de detalhes de ativação |	Descrição	| 
| ----------- | ----------- |
| Nome da ativação	| O nome de sua ativação.	|
| Descrição da ativação| Uma breve descrição da ativação.	|
| Autenticação	| Selecione a autenticação de coorte da Braze criada na etapa 2.	| 
| ID do coorte	| Esse é o identificador de coorte de backend que será enviado ao Braze. 	|
| Nome do coorte (opcional)	| Esse é o nome que aparecerá no Filtro de coorte na ferramenta de segmentação do Braze. Se isso não for definido, o `Cohort ID` será usado como `Cohort Name`.	|
| Operação	| Usado para determinar se a consulta deve adicionar ou remover perfis do coorte no Braze.	| 
| Aliases (opcional) | Quando definido, o nome da coluna correspondente em sua consulta será enviado como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`.	| 
| Contagem de fios | Número de chamadas simultâneas à API. |

#### Etapa 3.3: Configurar o mapeamento de saída

![Integrações de dados do Tesouro Mapeamento de saída de ativação]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| Mapeamento de saída de ativação |	Descrição	| 
| ----------- | ----------- |
| Colunas de atribuição	| Determine as colunas de seu banco de dados de segmentos que serão mapeadas como identificadores ao sincronizar perfis com um coorte Braze.	|
| Criador de strings| O construtor de string não é necessário para a integração com o Braze.	|

{% alert important %}
 - Ao usar `device_id` como identificador, o **nome da coluna de saída** deve ser `device_ids`.
 - Ao usar aliases como identificador, o **Nome da coluna de saída** deve ser o nome da coluna correspondente em sua consulta, que será enviada como `alias_label`, e os valores de cada linha na coluna serão enviados como `alias_name`.
 - Ao usar `external_id` como identificador, o **nome da coluna de saída** deve ser `user_ids`.
{% endalert %}

Todos os nomes de colunas não relevantes ou com nomes incorretos serão ignorados. Você pode optar por usar mais de um identificador em suas sincronizações.

#### Etapa 3.4: defina seu cronograma de ativação

Defina o cronograma de sincronização desejado e salve a ativação.

![Cronograma de ativação das integrações do Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### Etapa 4: crie um segmento da Braze a partir da exportação do Treasure Data

No Braze, navegue até **Segments (Segmentos**), crie um novo segmento e selecione **Treasure Data Cohorts (Coortes de dados do Tesouro** ) como seu filtro. Nessa tela, você pode escolher qual coorte do Treasure Data deseja incluir. Depois que o segmento de coorte da Treasure Data for criado, você poderá selecioná-lo como um filtro de público ao criar uma campanha ou canva.

![Catálogo do Hub de Integrações de Treasure Data]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.
