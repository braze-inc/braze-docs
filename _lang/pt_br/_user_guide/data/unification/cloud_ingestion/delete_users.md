---
nav_title: Excluir usuários com CDI
article_title: Excluir usuários com ingestão de dados na nuvem
page_order: 30
page_type: reference
description: "Esta página fornece uma visão geral do processo de exclusão de usuários com Cloud Data Ingestion."

---

# Excluir usuários com Cloud Data Ingestion

> Esta página aborda o processo de exclusão de usuários com Cloud Data Ingestion.

As sincronizações de exclusão de usuários são compatíveis com todas as fontes de dados disponíveis do Cloud Data Ingestion. 

## Configuração da integração 

Siga o processo padrão para [criar uma nova integração no dashboard da Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views) para o data warehouse ao qual você deseja se conectar. Certifique-se de incluir uma função que possa acessar a tabela de exclusão. Na página **Criar sincronização de importação**, defina o **Tipo de dados** como **Excluir usuários** para que as ações adequadas sejam tomadas durante a execução da integração para excluir usuários.

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## Configuração de dados de origem

As tabelas de origem para exclusões de usuários devem incluir um ou mais tipos de identificadores de usuários e um carimbo de data/hora `UPDATED_AT`. Não há suporte para colunas de carga útil para dados de exclusão de usuários.

### `UPDATED_AT`

Adicione um carimbo de data/hora `UPDATED_AT` à sua tabela de origem. Esse carimbo de data/hora indica o momento em que a linha foi atualizada ou adicionada à tabela. A Braze sincroniza as linhas em que `UPDATED_AT` é posterior ao último valor sincronizado. Linhas no limite exato do carimbo de data/hora podem ser sincronizadas novamente se novas linhas compartilharem o mesmo carimbo de data/hora.

### Colunas de identificador de usuário

Sua tabela pode conter uma ou mais colunas de identificador de usuário. Cada linha deve conter apenas um identificador: `external_id`, a combinação de `alias_name` e `alias_label`, ou `braze_id`. Uma tabela de origem pode conter colunas para um, dois ou todos os três tipos de identificadores.
- `EXTERNAL_ID` - Identifica o usuário que você deseja atualizar. Esse valor deve corresponder ao valor `external_id` usado na Braze. 
- `ALIAS_NAME` e `ALIAS_LABEL` - Essas duas colunas criam um objeto de alias de usuário. `alias_name` deve ser um identificador exclusivo e `alias_label` especifica o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.
- `BRAZE_ID` - O identificador de usuário da Braze. Ele é gerado pelo SDK da Braze, e não é possível criar novos usuários usando um Braze ID por meio do Cloud Data Ingestion. Para criar novos usuários, especifique um ID de usuário externo ou um alias de usuário. 

{% alert important %}
Não inclua uma coluna `PAYLOAD` na sua tabela para remoção de usuários. Para evitar a remoção acidental e permanente de usuários, a sincronização falhará se uma coluna de carga útil for fornecida na tabela de origem. Quaisquer outras colunas são permitidas, mas serão ignoradas pela Braze.
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```sql
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
Crie uma tabela com os seguintes campos:

| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBRIGATÓRIO |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}

{% tab Databricks %}
Crie uma tabela com os seguintes campos:

| Nome do campo | Tipo | Modo |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | OBRIGATÓRIO |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### Como funciona

Com o Cloud Data Ingestion da Braze, você configura uma integração entre sua instância de data warehouse e o espaço de trabalho da Braze para sincronizar dados de forma recorrente. Essa sincronização é executada em uma programação definida por você, e cada integração pode ter uma programação diferente. As sincronizações podem ser executadas com frequência a cada 15 minutos ou com pouca frequência, como uma vez por mês. Para os clientes que precisam que as sincronizações ocorram com mais frequência do que a cada 15 minutos, fale com seu gerente de sucesso do cliente ou considere o uso de chamadas de API REST para ingestão de dados em tempo real.

Quando uma sincronização é executada, a Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e exclui os perfis de usuários correspondentes no seu dashboard da Braze. 

{% alert warning %}
A exclusão de perfis de usuário não pode ser desfeita. Ela removerá permanentemente os usuários, o que pode causar discrepâncias nos seus dados. Consulte [excluir um perfil de usuário]({{site.baseurl}}/help/help_articles/api/delete_user/) para saber mais.
{% endalert %}

<br><br>