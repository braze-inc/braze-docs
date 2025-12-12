---
nav_title: Visão geral
article_title: Visão geral da ingestão de dados na nuvem 
page_order: 0
page_type: reference
description: "Esta página fornece uma visão geral da ingestão de dados na nuvem, práticas recomendadas e limitações do produto."

---

# Visão geral da ingestão de dados do Braze Cloud

> O Braze Cloud Data Ingestion permite que você configure uma conexão direta do seu data warehouse ou sistema de armazenamento de arquivos com o Braze para sincronizar dados relevantes do usuário ou do catálogo. Quando sincronizados com o Braze, esses dados podem ser aproveitados para casos de uso, como personalização, acionamento ou segmentação. 

## Como funciona

Com o Braze Cloud Data Ingestion (CDI), você configura uma integração entre a instância do data warehouse e o Braze Workspace para sincronizar os dados de forma recorrente. Essa sincronização é executada em uma programação definida por você, e cada integração pode ter uma programação diferente. As sincronizações podem ser executadas com a frequência de 15 minutos ou com pouca frequência, como uma vez por mês. Se precisar que as sincronizações ocorram com mais frequência do que 15 minutos, entre em contato com o gerente de sucesso do cliente ou considere o uso de chamadas à API REST para ingestão de dados em tempo real.

Quando uma sincronização é executada, o Braze se conecta diretamente à instância do seu data warehouse, recupera todos os novos dados da tabela especificada e atualiza os dados correspondentes no seu painel do Braze. Sempre que a sincronização for executada, todos os dados atualizados serão refletidos no Braze.

## Fontes de dados suportadas

A ingestão de dados na nuvem pode sincronizar dados das seguintes fontes com o Braze:

- Fontes de data warehouse 
   - Amazon Redshift
   - Telas de dados 
   - Google BigQuery
   - Microsoft Fabric
   - Floco de neve

- Fontes de armazenamento de arquivos 
   - Amazon S3

## Tipos de dados suportados 

A ingestão de dados na nuvem é compatível com os seguintes tipos de dados: 
- Atributos do usuário, incluindo:
   - Atributos personalizados aninhados
   - Matrizes de objetos
   - Status da assinatura
- Eventos personalizados
- Eventos de compra
- Itens do catálogo
- Solicitações de exclusão de usuários

Os dados do usuário podem ser atualizados por ID externo, alias de usuário, Braze ID, e-mail ou número de telefone. Os usuários podem ser excluídos por ID externo, alias de usuário ou ID Braze. 

## O que é sincronizado

Toda vez que uma sincronização é executada, o Braze procura por linhas que não foram sincronizadas anteriormente. Verificamos isso usando a coluna `UPDATED_AT` em sua tabela ou exibição. Todas as linhas em que `UPDATED_AT` for igual ou posterior ao último carimbo de data/hora `UPDATED_AT` do último trabalho de sincronização bem-sucedido serão selecionadas e puxadas para o Braze.

Em seu data warehouse, adicione os seguintes usuários e atributos à tabela, definindo o horário de `UPDATED_AT` para o horário em que você adicionou esses dados:

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

Durante a próxima sincronização programada, todas as linhas com um carimbo de data/hora `UPDATED_AT` igual ou posterior ao carimbo de data/hora mais recente serão sincronizadas com os perfis de usuário do Braze. Os campos serão atualizados ou adicionados, portanto, não é necessário sincronizar o perfil completo do usuário todas as vezes. Após a sincronização, os usuários refletirão as novas atualizações:

```json
{
  "external_id":"customer_1234",
  "email":"jane@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":{
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_2"
    },
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":false,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_3456",
  "email":"michael@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2019-07-16T19:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing"
}
```
```json
{
  "external_id":"customer_5678",
  "email":"bob@example.com",
  "attribute_1":"abcdefg",
  "attribute_2":42,
  "attribute_3":"2017-08-10T09:20:30+1:00",
  "attribute_4":true,
  "attribute_5":"testing_123"
}
```

### Caso de uso: Primeira sincronização e atualizações subsequentes

Este exemplo mostra o processo geral de sincronização de dados pela primeira vez e, em seguida, atualiza apenas os dados alterados (deltas) nas atualizações subsequentes. Digamos que tenhamos uma tabela `EXAMPLE_DATA` com alguns dados de usuário. No dia 1, ele tem os seguintes valores:

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

Para colocar esses dados no formato esperado pelo CDI, você pode executar a seguinte consulta:

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

Nada disso foi sincronizado com o Braze antes, portanto, adicione tudo isso à tabela de origem do CDI:

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Uma sincronização é executada, e o Braze registra que você sincronizou todos os dados disponíveis até "2023-03-16 15:00:00". Então, na manhã do segundo dia, você tem um ETL que é executado e alguns campos da tabela de usuários são atualizados (destacados):

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

Agora você precisa adicionar apenas os valores alterados à tabela de origem do CDI. Essas linhas podem ser anexadas em vez de atualizar as linhas antigas. Essa tabela agora tem a seguinte aparência:

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

O CDI sincronizará apenas as novas linhas, portanto, a próxima sincronização executada sincronizará apenas as últimas cinco linhas.

### Caso de uso: Atualizar um campo em uma matriz de objetos existente

Este exemplo mostra como atualizar um campo em uma matriz de objetos existente. Digamos que tenhamos uma tabela de origem com a seguinte definição:

```json 
Create table BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list (
    pet_id int IDENTITY(1,1), 
    breed VARCHAR, 
    type VARCHAR, 
    name VARCHAR, 
    owner_id VARCHAR, 
    age int
);
```

Neste exemplo, queremos adicionar uma matriz de animais de estimação pertencentes a cada usuário, o que corresponde a `owner_id`. Especificamente, queremos incluir identificação, raça, tipo e nome. Podemos usar a seguinte consulta para preencher uma tabela ou exibição:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$add', ARRAY_AGG( OBJECT_CONSTRUCT(
                'id',
                pet_id,
                'breed',
                breed,
                'type',
                type,
                'name',
                name
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID;
```

O resultado esperado seria semelhante a este:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

Em seguida, para enviar um campo de nome atualizado e um novo campo de idade para cada proprietário, podemos usar a seguinte consulta para preencher uma tabela ou exibição:

```json
SELECT 
CURRENT_TIMESTAMP as UPDATED_AT,
owner_id as EXTERNAL_ID,
TO_JSON(
    OBJECT_CONSTRUCT(
        '_merge_objects','true',
       'pets',
        OBJECT_CONSTRUCT(
           '$update', ARRAY_AGG( OBJECT_CONSTRUCT(
                '$identifier_key','id',
                '$identifier_value',pet_id,
                '$new_object',OBJECT_CONSTRUCT(
                    'name',name,
                    'age',age
                )
                )) WITHIN GROUP (ORDER BY type ASC)    
        )
    )
)
as PAYLOAD from BRAZE_CLOUD_INGESTION_DEMO.BRAZE_SCHEMA.pet_list group by EXTERNAL_ID; 
```

O resultado esperado seria semelhante a este:

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## Uso de pontos de dados

O faturamento do ponto de dados para ingestão de dados na nuvem é equivalente ao faturamento de atualizações por meio do [ponto de extremidade`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track). Consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) para obter mais informações. 

{% alert important %}
O Braze Cloud Data Ingestion conta para o limite de taxa disponível, portanto, se você estiver enviando dados usando outro método, o limite de taxa será combinado entre a API do Braze e o Cloud Data Ingestion.
{% endalert %}

## Recomendações de configuração de dados

### Gravar somente atributos novos ou atualizados para minimizar o consumo

Toda vez que uma sincronização é executada, o Braze procura por linhas que não foram sincronizadas anteriormente. Verificamos isso usando a coluna `UPDATED_AT` em sua tabela ou exibição. Todas as linhas em que `UPDATED_AT` for igual ou posterior ao último carimbo de data/hora `UPDATED_AT` do último trabalho de sincronização bem-sucedido serão selecionadas e puxadas para o Braze, independentemente de serem iguais ao que está atualmente no perfil do usuário. Por isso, recomendamos sincronizar apenas os atributos que você deseja adicionar ou atualizar.

O uso de pontos de dados é idêntico ao uso de CDI e de outros métodos de ingestão, como APIs REST ou SDKs, portanto, cabe a você certificar-se de que está adicionando apenas atributos novos ou atualizados às suas tabelas de origem.

### Use um registro de data e hora UTC para a coluna `UPDATED_AT` 

A coluna `UPDATED_AT` deve estar em UTC para evitar problemas com o horário de verão. Prefira funções somente UTC, como `SYSDATE()` em vez de `CURRENT_DATE()`, sempre que possível.

### Certifique-se de que o horário de `UPDATED_AT` não seja o mesmo horário de sua sincronização

Sua sincronização de CDI pode ter dados duplicados se algum dos campos `UPDATED_AT` estiver exatamente no mesmo horário que o último carimbo de data/hora `UPDATED_AT` do trabalho de sincronização anterior bem-sucedido. Isso ocorre porque o CDI escolherá um "limite inclusivo" ao identificar qualquer linha que tenha a mesma hora da sincronização anterior e fará com que as linhas possam ser sincronizadas. O CDI testará novamente essas linhas e criará dados duplicados.

### Separe a coluna `EXTERNAL_ID` da coluna `PAYLOAD` 

O objeto `PAYLOAD` não deve incluir uma ID externa ou outro tipo de ID. 

### Remover um atributo

Você pode defini-lo como `null` se quiser omitir um atributo do perfil de um usuário. Se você quiser que um atributo permaneça inalterado, não o envie para o Braze até que ele tenha sido atualizado. Para remover completamente um atributo, use `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Faça atualizações incrementais

Faça atualizações incrementais em seus dados para evitar substituições não intencionais quando forem feitas atualizações simultâneas.

No exemplo a seguir, um usuário tem dois atributos:
- Cor: "Verde"
- Tamanho: "Grande"

Em seguida, o Braze recebe simultaneamente as duas atualizações a seguir para esse usuário:
- Solicitação 1: Alterar a cor para "Vermelho"
- Solicitação 2: Alterar o tamanho para "Medium" (Médio)

Como a Solicitação 1 ocorre primeiro, os atributos do usuário são atualizados para o seguinte:
- Cor: "Vermelho"
- Tamanho: "Grande"

No entanto, quando a Solicitação 2 ocorre, o Braze começa com os valores originais dos atributos ("Verde" e "Grande") e, em seguida, atualiza os atributos do usuário para o seguinte:
- Cor: "Verde"
- Tamanho: "Médio"

Quando as solicitações forem concluídas, a Solicitação 2 substituirá a atualização da Solicitação 1, portanto, é melhor escalonar suas atualizações para evitar que as solicitações sejam substituídas.

### Criar uma cadeia de caracteres JSON a partir de outra tabela

Se preferir armazenar cada atributo em sua própria coluna internamente, você precisará converter essas colunas em uma cadeia de caracteres JSON para preencher a sincronização com o Braze. Para fazer isso, você pode usar uma consulta como:

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

Usamos o registro de data e hora `UPDATED_AT` para rastrear quais dados foram sincronizados com sucesso com o Braze. Se muitas linhas forem gravadas com o mesmo registro de data e hora enquanto uma sincronização estiver em execução, isso poderá fazer com que dados duplicados sejam sincronizados com o Braze. Algumas sugestões para evitar dados duplicados:
- Se estiver configurando uma sincronização com um `VIEW`, não use `CURRENT_TIMESTAMP` como o valor padrão. Isso fará com que todos os dados sejam sincronizados toda vez que a sincronização for executada, pois o campo `UPDATED_AT` será avaliado de acordo com a hora em que nossas consultas forem executadas. 
- Se você tiver pipelines ou consultas de execução muito longa gravando dados na tabela de origem, evite executá-los simultaneamente com uma sincronização ou evite usar o mesmo carimbo de data/hora para cada linha inserida.
- Use uma transação para gravar todas as linhas que tenham o mesmo registro de data e hora.

### Configuração da tabela

Temos um [repositório](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) público [no GitHub](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion) para que os clientes compartilhem práticas recomendadas ou trechos de código. Para contribuir com seus próprios snippets, crie uma solicitação pull!

### Formatação de dados

Todas as operações possíveis por meio do endpoint do Braze `/users/track` são compatíveis com a ingestão de dados na nuvem, inclusive a atualização de atributos personalizados aninhados, a adição de status de assinatura e a sincronização de eventos ou compras personalizados. 

Os campos dentro da carga útil devem seguir o mesmo formato do ponto de extremidade `/users/track` correspondente. Para obter requisitos de formatação detalhados, consulte o seguinte:

| Tipo de dados | Especificações de formatação |
| --------- | ---------| --------- | ----------- |
| `attributes` | Consulte [objeto de atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Ver [objeto de eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |

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
Para sincronizar eventos, é necessário um nome de evento. O campo `time` deve ser formatado como uma cadeia de caracteres ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, o valor da coluna `UPDATED_AT` será usado como a hora do evento. Outros campos, incluindo `app_id` e `properties`, são opcionais. 

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
Para sincronizar eventos de compra, são necessários os sites `product_id`, `currency` e `price`. O campo `time`, que é opcional, deve ser formatado como uma cadeia de caracteres ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Se o campo `time` não estiver presente, o valor da coluna `UPDATED_AT` será usado como a hora do evento. Outros campos, incluindo `app_id`, `quantity` e `properties` são opcionais.

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

### Evitar timeouts para consultas de data warehouse

Recomendamos que as consultas sejam concluídas em uma hora para otimizar o desempenho e evitar possíveis erros. Se as consultas excederem esse período, considere a possibilidade de revisar a configuração do data warehouse. A otimização dos recursos alocados ao seu warehouse pode ajudar a melhorar a velocidade de execução das consultas.

## Limitações do produto

| Limitação            | Descrição                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de integrações | Não há limite para o número de integrações que você pode configurar. No entanto, você só poderá configurar uma integração por tabela ou visualização.                                             |
| Número de linhas         | Por padrão, cada execução pode sincronizar até 500 milhões de linhas. Todas as sincronizações com mais de 500 milhões de novas linhas serão interrompidas. Se precisar de um limite maior do que esse, entre em contato com o gerente de sucesso do cliente Braze ou com o Suporte Braze. |
| Atributos por linha     | Cada linha deve conter um único ID de usuário e um objeto JSON com até 250 atributos. Cada chave no objeto JSON conta como um atributo (ou seja, uma matriz conta como um atributo). |
| Tamanho da carga útil           | Cada linha pode conter uma carga útil de até 1 MB. As cargas úteis maiores que 1 MB serão rejeitadas, e o erro "Payload was greater than 1MB" será registrado no log de sincronização, juntamente com a ID externa associada e a carga útil truncada. |
| Tipo de dados              | Você pode sincronizar atributos de usuário, eventos e compras por meio da ingestão de dados na nuvem.                                                                                                  |
| Região de brasagem           | Esse produto está disponível em todas as regiões do Brasil. Qualquer região do Braze pode se conectar a qualquer região de dados de origem.                                                                              |
| Região de origem       | O Braze se conectará ao seu data warehouse ou ambiente de nuvem em qualquer região ou provedor de nuvem.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
