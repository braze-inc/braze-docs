---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "Este artigo descreve a parceria entre a Braze e o Snowflake, abrangendo tanto o Compartilhamento de Dados (da Braze para o Snowflake) quanto a Ingestão de Dados na Nuvem (do Snowflake para a Braze)."
page_type: partner
search_tag: Partner

---

# Snowflake

> O [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) é um data warehouse de nuvem SQL criado para fins específicos e disponibilizado como software como serviço (SaaS). O Snowflake fornece um data warehouse mais rápido, mais fácil de usar e muito mais flexível do que as ofertas tradicionais. Com a arquitetura exclusiva e patenteada do Snowflake, é fácil reunir todos os seus dados, executar análises rápidas e obter insights orientados por dados para todos os seus usuários.

A Braze oferece duas integrações com o Snowflake. Juntas, elas fornecem um pipeline de dados bidirecional completo entre seus ambientes da Braze e do Snowflake.

## Escolhendo uma integração

### Compartilhamento de Dados (da Braze para o Snowflake)

O [Compartilhamento Seguro de Dados]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) do Snowflake oferece acesso seguro e em tempo real aos dados de engajamento e campanhas da Braze diretamente na sua instância do Snowflake. Nenhum dado é copiado ou transferido entre contas — todo o compartilhamento é realizado por meio da camada de serviços e do armazenamento de metadados exclusivos do Snowflake.

**Use o Compartilhamento de Dados quando quiser:**
- Consultar dados de eventos e campanhas da Braze usando SQL do Snowflake
- Criar relatórios complexos e realizar modelagem de atribuição
- Unir dados da Braze com outros dados no seu data warehouse do Snowflake
- Comparar seus dados de engajamento entre canais, setores e plataformas de dispositivos

Para instruções de configuração, consulte [Compartilhamento de Dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/).

### Ingestão de Dados na Nuvem (do Snowflake para a Braze)

A [Ingestão de Dados na Nuvem (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) permite sincronizar dados da sua instância do Snowflake diretamente para a Braze. Isso permite manter atributos de usuários, eventos e compras na Braze atualizados com os dados do seu data warehouse como fonte da verdade.

**Use a Ingestão de Dados na Nuvem quando quiser:**
- Sincronizar atributos de usuários do Snowflake para perfis de usuários na Braze
- Enviar dados de eventos ou compras do Snowflake para a Braze
- Manter a Braze sincronizada com transformações de dados que acontecem no seu data warehouse
- Evitar a construção e manutenção de pipelines ETL personalizados do Snowflake para a Braze

Para saber mais sobre o compartilhamento de dados do Snowflake, veja [Introdução ao Compartilhamento Seguro de Dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work).

## Pré-requisitos

Antes de usar este recurso, você precisará concluir o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à Braze | Para acessar este recurso na Braze, você precisará entrar em contato com seu gerente de conta ou gerente de sucesso do cliente da Braze. |
| Conta Snowflake | Uma conta Snowflake com permissões de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurando o Compartilhamento Seguro de Dados

Para o Snowflake, o compartilhamento de dados acontece entre um [fornecedor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers) e um [consumidor de dados](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers). Neste contexto, sua conta da Braze é o fornecedor de dados porque cria e envia o datashare&#8212;enquanto sua conta Snowflake é o consumidor de dados porque usa o datashare para criar um banco de dados. Para mais detalhes, veja [Snowflake: Consumindo Dados Compartilhados](https://docs.snowflake.com/en/user-guide/data-share-consumers).

### Etapa 1: Envie o datashare da Braze

1. Na Braze, acesse **Integrações com Parceiros** > **Compartilhamento de Dados**.
2. Insira os detalhes da sua conta Snowflake e o localizador. Para obter seu localizador de conta, execute `SELECT CURRENT_ACCOUNT()` na conta de destino.
3. Se estiver usando um compartilhamento CRR, especifique o provedor de nuvem e a região.
4. Quando terminar, selecione **Criar Datashare**. Isso enviará o datashare para sua conta Snowflake.

### Etapa 2: Crie o banco de dados no Snowflake

1. Após alguns minutos, você deve receber o datashare de entrada na sua conta Snowflake.
2. Usando o datashare de entrada, crie um banco de dados para visualizar e consultar as tabelas. Por exemplo:
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. Conceda privilégios para consultar o novo banco de dados.

{% alert warning %}
Se você excluir e recriar um compartilhamento no dashboard da Braze, deve descartar o banco de dados criado anteriormente e recriá-lo usando `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` para consultar o compartilhamento de entrada.
Se você tiver vários espaços de trabalho compartilhando dados para a mesma conta Snowflake, consulte as [FAQs sobre Compartilhamento de Dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) para orientações sobre como gerenciar configurações de múltiplos espaços de trabalho.
{% endalert %}

## Uso e visualização

Após o compartilhamento de dados ser provisionado, você precisará criar um banco de dados a partir do compartilhamento de dados de entrada, fazendo com que todas as tabelas compartilhadas apareçam na sua instância Snowflake e sejam consultáveis como qualquer outro dado armazenado na sua instância. No entanto, lembre-se de que os dados compartilhados são somente leitura e só podem ser consultados, mas não modificados ou excluídos de forma alguma.

Semelhante ao Currents, você pode usar o Compartilhamento Seguro de Dados do Snowflake para:

- Criar relatórios complexos
- Realizar modelagem de atribuição
- Compartilhamento seguro dentro da sua própria empresa
- Mapear dados brutos de eventos ou de usuários para um CRM (como o Salesforce)
- E mais

Para uma lista completa de tabelas e colunas disponíveis, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/). O Compartilhamento de Dados do Snowflake inclui todas as tabelas dessa referência, além de tabelas exclusivas do Snowflake para snapshots, changelogs de campanhas e Canvas, eventos do console de agentes e eventos de reenvio de mensagens.

Você também pode [baixar os esquemas de tabela brutos]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) como um arquivo de texto.

### Esquema de ID do usuário

Note as seguintes diferenças entre as convenções de nomenclatura da Braze e do Snowflake para IDs de usuário.

| Esquema da Braze | Esquema do Snowflake | Descrição |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | O identificador exclusivo que é atribuído automaticamente pela Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | O identificador exclusivo do perfil de um usuário que é definido pelo cliente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Informações importantes e limitações

### Alterações interruptivas e não interruptivas

#### Alterações não interruptivas

Alterações não interruptivas podem ocorrer a qualquer momento e geralmente trazem funcionalidades adicionais. Exemplos de alterações não interruptivas:
- Adição de uma nova tabela ou visualização
- Adição de uma coluna a uma tabela ou visualização existente

{% alert important %}
Como novas colunas são consideradas não interruptivas, a Braze recomenda enfaticamente listar de modo explícito as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Como alternativa, você pode criar visualizações que nomeiem explicitamente as colunas e, em seguida, consultar essas visualizações em vez das tabelas diretamente.
{% endalert %}

#### Alterações interruptivas

Quando possível, as alterações interruptivas serão precedidas de um anúncio e de um período de migração. Exemplos de alterações interruptivas incluem:
- Remoção de uma tabela ou visualização
- Remoção de uma coluna de uma tabela ou visualização existente
- Alteração do tipo ou da nulabilidade de uma coluna existente

### Regiões do Snowflake

A Braze atualmente hospeda todos os dados em nível de usuário nas regiões Snowflake AWS US East-1, EU-Central (Frankfurt), AP-Southeast-2 (Sydney) e AP-Southeast-3 (Jacarta). Para usuários fora dessas regiões, a Braze pode fornecer compartilhamento de dados para clientes conjuntos que hospedem sua infraestrutura do Snowflake em qualquer região da AWS, Azure ou GCP.

### Retenção de dados

#### Política de retenção

Todos os dados com mais de dois anos serão arquivados e transferidos para o armazenamento de longo prazo. Como parte do processo de arquivamento, todos os eventos são anonimizados e todos os campos sensíveis de informações de identificação pessoal (IPI) são removidos (isso inclui campos de IPI opcionais, como `properties`). Os dados arquivados ainda contêm o campo `user_id`, que permite a análise de dados por usuário em todos os dados de eventos.

Você poderá consultar os dois anos mais recentes de dados de cada evento na visualização correspondente `USERS_*_SHARED`. Além disso, cada evento terá uma visualização `USERS_*_SHARED_ALL` que pode ser consultada para retornar dados anonimizados e não anonimizados.

#### Dados históricos

O arquivo de dados históricos de eventos no Snowflake remonta a abril de 2019. Nos primeiros meses em que a Braze armazenou dados no Snowflake, foram feitas alterações no produto que podem ter resultado em alguns desses dados com aparência ligeiramente diferente ou com alguns valores nulos (já que não estávamos passando dados para todos os campos disponíveis naquele momento). É melhor presumir que os resultados que incluam dados anteriores a agosto de 2019 poderão ser ligeiramente diferentes das expectativas.

### Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR)

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### Velocidade, performance e custo das consultas

A velocidade, a performance e o custo de qualquer consulta executada nos dados são determinados pelo tamanho do data warehouse que você usa para consultar os dados. Em alguns casos, dependendo da quantidade de dados que estiver acessando para análise de dados, talvez seja necessário usar um tamanho de warehouse maior para que a consulta seja bem-sucedida. O Snowflake tem excelentes recursos disponíveis sobre a melhor forma de determinar o tamanho a ser usado, incluindo [Visão geral dos warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) e [Considerações sobre warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html).

> Para obter um conjunto de exemplos de consultas como referência ao configurar o Snowflake, confira nossos exemplos de [consultas]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/) e de [configuração do pipeline de eventos ETL]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/).

Para instruções de configuração, consulte [Ingestão de Dados na Nuvem: integrações com data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/).