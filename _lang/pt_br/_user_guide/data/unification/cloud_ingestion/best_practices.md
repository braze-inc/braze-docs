---
nav_title: Melhores práticas
article_title: Melhores Práticas de Ingestão de Dados em Nuvem
toc_headers: h2
page_order: 0
page_type: reference
description: "Esta página fornece uma visão geral da ingestão de dados na nuvem, práticas recomendadas e limitações do produto."

---

# Melhores práticas

> Braze Cloud Data Ingestion permite que você configure uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos para o Braze para sincronizar dados relevantes de usuários ou catálogos. Quando você sincroniza esses dados com a Braze, pode aproveitá-los para casos de uso como personalização, acionamento ou segmentação. 

## Entendendo a coluna `UPDATED_AT`

{% alert note %}
`UPDATED_AT` é relevante apenas para integrações de data warehouse, não para sincronizações S3.
{% endalert %}

Quando uma sincronização é executada, o Braze se conecta diretamente à sua instância de data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes em seu dashboard do Braze. Cada vez que a sincronização é executada, a Braze reflete quaisquer dados atualizados.

{% alert important %}
A Braze CDI sincronizará linhas estritamente com base no valor `UPDATED_AT`, independentemente de o conteúdo da linha ser o mesmo do que está atualmente na Braze. Dado isso, recomendamos usar `UPDATED_AT` corretamente para sincronizar apenas dados novos ou atualizados, a fim de evitar o uso desnecessário de pontos de dados.
{% endalert %}

### Exemplo: Sincronização recorrente

Para ilustrar como `UPDATED_AT` é usado em uma sincronização CDI, considere este exemplo de sincronização recorrente para atualizar atributos de usuários:

- Fontes de armazenamento de arquivos 
   - Amazon S3

## Tipos de dados suportados 

A Ingestão de Dados na Nuvem suporta os seguintes tipos de dados: 
- Atributos do usuário, incluindo:
   - Atributos personalizados aninhados
   - Arrays de objetos
   - Status de inscrições
- Eventos personalizados
- Eventos de compra
- Itens do catálogo
- Solicitações de exclusão de usuário

Você pode atualizar dados de usuários por ID externo, alias de usuário, ID Braze, e-mail ou número de telefone. Você pode excluir usuários por ID externo, alias de usuário ou ID Braze. 

## O que é sincronizado

Cada vez que uma sincronização é executada, a Braze procura linhas que não foram sincronizadas anteriormente. Verificamos isso usando a coluna `UPDATED_AT` na sua tabela ou visualização. A Braze seleciona e importa quaisquer linhas onde `UPDATED_AT` é igual ou posterior ao último timestamp `UPDATED_AT` do último trabalho de sincronização bem-sucedido.

No seu data warehouse, adicione os seguintes usuários e atributos à sua tabela, definindo o `UPDATED_AT` horário para o momento em que você adicionar esses dados:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Durante a próxima sincronização programada, a Braze sincroniza todas as linhas com um timestamp `UPDATED_AT` igual ou posterior ao timestamp mais recente para perfis de usuários. A Braze atualiza ou adiciona campos, então você não precisa sincronizar o perfil completo do usuário a cada vez. Após a sincronização, os perfis de usuários refletem as novas atualizações:

**Sincronização recorrente, segunda execução em 20 de julho de 2022 às 12h**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Uma linha foi adicionada, mas o valor `UPDATED_AT` é anterior a `2022-07-19 09:07:23` (armazenado da primeira execução). Como resultado, nenhuma dessas linhas será sincronizada nesta execução. O último `UPDATED_AT` para a sincronização não foi alterado por esta execução e permanece como `2022-07-19 09:07:23`.

**Sincronização recorrente, terceira execução em 21 de julho de 2022 às 12h**

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-17 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_1",<br>        "attribute_b":"example_value_1"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-18 11:59:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-16 00:25:30` | `customer_9012` | {<br>    "attribute_1":"xyz",<br>    "attribute_4":false,<br>    "attribute_5":"testing_123"<br>} |
| `2022-07-21 08:30:00` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3”:”2019-07-20T19:20:30+1:00"<br>} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Nesta terceira execução, outra nova linha foi adicionada. Agora, uma linha tem um valor `UPDATED_AT` posterior ao `2022-07-19 09:07:23`, o que significa que apenas uma linha será sincronizada. O último `UPDATED_AT` agora está definido como `2022-07-21 08:30:00`.

{% alert note %}
Valores `UPDATED_AT` podem ser ainda mais tardios do que o horário de início da execução para uma sincronização dada. No entanto, isso não é recomendado, pois empurra a última marca de tempo `UPDATED_AT` "para o futuro" e as sincronizações subsequentes não sincronizarão valores anteriores.
{% endalert %}

## Use um registro de data e hora UTC para a coluna `UPDATED_AT` 

A coluna `UPDATED_AT` deve estar em UTC para evitar problemas com o horário de verão. Prefira funções apenas UTC, como `SYSDATE()` em vez de `CURRENT_DATE()` sempre que possível.

## Certifique-se de que o horário `UPDATED_AT` não seja o mesmo que o da sua sincronização.

Sua sincronização CDI pode ter dados duplicados se algum campo `UPDATED_AT` estiver exatamente no mesmo horário que a última marca de tempo `UPDATED_AT` da execução de sincronização bem-sucedida anterior. Isso ocorre porque o CDI escolherá um "limite inclusivo" quando identificar qualquer linha que tenha o mesmo horário da sincronização anterior e tornará as linhas capazes de sincronizar. O CDI irá re-ingressar essas linhas e criar dados duplicados.

Aqui estão algumas sugestões para evitar dados duplicados:

- Se você estiver configurando uma sincronização contra um `VIEW`, não use `CURRENT_TIMESTAMP` como valor padrão. Isso fará com que todos os dados sejam sincronizados toda vez que a sincronização for executada, porque o campo `UPDATED_AT` será avaliado no momento em que nossas consultas forem executadas.
- Se você tiver pipelines ou consultas de longa duração gravando dados em sua tabela de origem, evite executá-los simultaneamente com uma sincronização ou evite usar o mesmo carimbo de data/hora para cada linha inserida.
- Use uma transação para gravar todas as linhas que têm o mesmo carimbo de data/hora.

### Exemplo: Gerenciando atualizações subsequentes

Esse exemplo mostra o processo geral para sincronizar dados pela primeira vez, depois apenas atualizar os dados que mudam (deltas) nas atualizações subsequentes. Digamos que temos uma tabela `EXAMPLE_DATA` com alguns dados de usuários. No dia 1, tem os seguintes valores:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>azul</td>
            <td>380</td>
            <td>FALSO</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>azul</td>
            <td>823</td>
            <td>VERDADEIRO</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>azul</td>
            <td>384</td>
            <td>VERDADEIRO</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>vermelho</td>
            <td>349</td>
            <td>VERDADEIRO</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>vermelho</td>
            <td>813</td>
            <td>FALSO</td>
        </tr>
    </tbody>
</table>

Para obter esses dados no formato que o CDI espera, você pode executar a seguinte consulta:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nada disso foi sincronizado com a Braze antes, então adicione tudo à tabela de origem para CDI:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Uma sincronização é executada, e a Braze registra que você sincronizou todos os dados disponíveis até “2023-03-16 15:00:00”. Então, na manhã do dia 2, você tem um ETL que é executado e alguns campos na sua tabela de usuários são atualizados (destacados):

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">vermelho</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">VERDADEIRO</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>azul</td>
            <td>823</td>
            <td>VERDADEIRO</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>azul</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSO</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">verde</td>
            <td>349</td>
            <td>VERDADEIRO</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>vermelho</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSO</td>
        </tr>
    </tbody>
</table>

Agora você precisa adicionar apenas os valores alterados na tabela de origem CDI. Essas linhas podem ser anexadas em vez de atualizar as linhas antigas. Essa tabela agora se parece com isso:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 12345       | { "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"} |
| 2023-03-17 09:30:00 | 23456       | { "ATTRIBUTE_1": "15"} |
| 2023-03-17 09:30:00 | 34567       | { "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-17 09:30:00 | 45678       | { "ATTRIBUTE_2":"green"} |
| 2023-03-17 09:30:00 | 56789       | { "ATTRIBUTE_3":"693"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O CDI sincronizará apenas as novas linhas, então a próxima sincronização que ocorrer sincronizará apenas as últimas FIVE linhas.

## Dicas adicionais

### Traduza o seguinte texto do inglês para o português (Brasil) e nada mais:

Cada vez que uma sincronização é executada, a Braze procura linhas que não foram sincronizadas anteriormente. Verificamos isso usando a coluna `UPDATED_AT` na sua tabela ou visualização. A Braze seleciona e importa quaisquer linhas onde `UPDATED_AT` é igual ou posterior ao último timestamp `UPDATED_AT` do último trabalho de sincronização bem-sucedido, independentemente de serem as mesmas que estão atualmente no perfil do usuário. Dito isso, recomendamos sincronizar apenas os atributos que você deseja adicionar ou atualizar.

O uso de pontos de dados é idêntico usando CDI em comparação com outros métodos de ingestão, como APIs REST ou SDKs, portanto, cabe a você garantir que está apenas adicionando novos ou atributos atualizados em suas tabelas de origem.

### Separe a coluna `EXTERNAL_ID` da coluna `PAYLOAD` 

O objeto `PAYLOAD` não deve incluir um ID externo ou outro tipo de ID. 

### Remover um atributo

É possível defini-lo como `null` se quiser omitir uma atribuição do perfil de um usuário. Se você deseja que um atributo permaneça inalterado, não o envie para a Braze até que ele tenha sido atualizado. Para remover completamente uma atribuição, use `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Faça atualizações incrementais

Faça atualizações incrementais em seus dados para evitar substituições não intencionais quando forem feitas atualizações simultâneas.

No exemplo a seguir, um usuário tem duas atribuições:
- Cor: "Verde"
- Tamanho: "Grande"

Em seguida, o Braze recebe as duas atualizações a seguir para esse usuário simultaneamente:
- Solicitação 1: Alterar a cor para "Vermelho"
- Solicitação 2: Alterar o tamanho para "Medium" (Médio)

Como a Solicitação 1 ocorre primeiro, as atribuições do usuário são atualizadas para o seguinte:
- Cor: "Vermelho"
- Tamanho: "Grande"

No entanto, quando a Solicitação 2 ocorre, o Braze começa com os valores de atribuição originais ("Verde" e "Grande") e, em seguida, atualiza os atributos do usuário para o seguinte:
- Cor: "Verde"
- Tamanho: "Médio"

Quando as solicitações forem concluídas, a Solicitação 2 substituirá a atualização da Solicitação 1, portanto, é melhor espaçar suas atualizações para evitar que solicitações sejam sobrescritas.

### Criar uma string JSON a partir de outra tabela

Se você preferir armazenar cada atributo em sua própria coluna internamente, você precisa converter essas colunas em uma string JSON para preencher a sincronização com a Braze. Para fazer isso, você pode usar uma consulta como:

{% tabs local %}
{% tab Snowflake %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Use o registro de data e hora `UPDATED_AT` 

Usamos o `UPDATED_AT` timestamp para rastrear quais dados foram sincronizados com sucesso para a Braze. Se muitas linhas forem escritas com o mesmo carimbo de data/hora enquanto uma sincronização está em execução, isso pode levar à duplicação de dados sendo sincronizados para a Braze. Algumas sugestões para evitar dados duplicados:
- Se estiver configurando uma sincronização com um `VIEW`, não use `CURRENT_TIMESTAMP` como o valor padrão. Isso fará com que todos os dados sejam sincronizados toda vez que a sincronização for executada, porque o campo `UPDATED_AT` será avaliado no momento em que nossas consultas forem executadas. 
- Se você tiver pipelines ou consultas de longa duração gravando dados em sua tabela de origem, evite executá-los simultaneamente com uma sincronização ou evite usar o mesmo carimbo de data/hora para cada linha inserida.
- Use uma transação para gravar todas as linhas que têm o mesmo carimbo de data/hora.

### Configuração da tabela

Temos um [repositório GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) público para os clientes compartilharem melhores práticas ou trechos de código. Para contribuir com seus próprios trechos, crie uma solicitação de pull!

### Formatação de dados

Qualquer operação possível através do endpoint Braze `/users/track` é suportada pela Ingestão de Dados na Nuvem, incluindo a atualização de atributos personalizados aninhados, a adição de status de inscrição e a sincronização de eventos ou compras personalizadas. 

Os campos dentro da carga útil devem seguir o mesmo formato que o endpoint correspondente `/users/track`. Para obter requisitos detalhados de formatação, consulte o seguinte:

| Tipo de dados | Especificações de formatação |
| --------- | ---------| --------- | ----------- |
| `attributes` | Veja [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Veja [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Veja [compras objeto]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Observe o requisito especial para [capturar datas]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) em atributos aninhados. 

{% tabs local %}
{% tab Nested Custom Attributes %}
Você pode incluir atributos personalizados aninhados na coluna de carga útil para uma sincronização de atributos personalizados. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Event %}
Para sincronizar eventos, é necessário um nome de evento. Formate o campo `time` como uma string ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, a Braze usa o valor da coluna `UPDATED_AT` como o horário do evento. Outros campos, incluindo `app_id` e `properties`, são opcionais. 

Observe que você só pode sincronizar um evento por linha.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Purchase %}
Para sincronizar eventos de compra, `product_id`, `currency` e `price` são obrigatórios. Formate o campo `time`, que é opcional, como uma string ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, a Braze usa o valor da coluna `UPDATED_AT` como o horário do evento. Outros campos, incluindo `app_id`, `quantity` e `properties` são opcionais.

Observe que você só pode sincronizar um evento de compra por linha.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99, },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99, }
        ]
    }
}
```

{% endtab %}
{% tab Subscription Groups %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Evite timeouts para consultas de data warehouse

Recomendamos que as consultas sejam concluídas dentro de uma hora para obter uma performance ideal e evitar possíveis erros. Se as consultas excederem esse período, considere revisar a configuração do seu data warehouse. A otimização dos recursos alocados ao seu armazém pode ajudar a melhorar a velocidade de execução da consulta.

## Limitações do produto

| Limitação            | Descrição                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações | Não há limite para quantas integrações você pode configurar. No entanto, você só poderá configurar uma integração por tabela ou visualização.                                             |
| Número de linhas         | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. A Braze interrompe qualquer sincronização com mais de 500 milhões de novas linhas. Se você precisar de um limite maior do que isso, entre em contato com seu gerente de sucesso do cliente da Braze ou com o Suporte da Braze. |
| Atributos por linha     | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, um vetor conta como um atributo). |
| Tamanho da carga útil           | Cada linha pode conter uma carga útil de até 1 MB. A Braze rejeita cargas úteis maiores que 1 MB e registra o erro "A carga útil era maior que 1MB" no log de sincronização junto com o ID externo associado e a carga útil truncada. |
| Tipo de dados              | Você pode sincronizar atributos de usuário, eventos e compras através da Ingestão de Dados na Nuvem.                                                                                                  |
| região Braze           | Este produto está disponível em todas as regiões da Braze. Qualquer região da Braze pode se conectar a qualquer região de origem de dados.                                                                              |
| Região de origem       | A Braze se conectará ao seu data warehouse ou ambiente de nuvem em qualquer região ou provedor de nuvem.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
