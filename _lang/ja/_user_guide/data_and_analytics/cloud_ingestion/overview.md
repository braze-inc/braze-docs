---
nav_title: 概要
article_title: クラウドデータ取り込みの概要 
page_order: 0
page_type: reference
description: "このリファレンス記事では、クラウドデータ取り込みの概要、ベストプラクティス、製品の制限事項について説明します。"

---

# Braze クラウドデータ取り込みの概要

> Braze クラウドデータ取り込みを使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを同期できます。Braze に同期すると、このデータをパーソナライゼーション、トリガー、セグメンテーションなどのユースケースに活用できます。 

## 仕組み

Braze のクラウドデータ取り込み (CDI) では、データウェアハウスのインスタンスと Braze ワークスペースとの連携を設定して、定期的にデータを同期します。この同期は設定したスケジュールで実行され、連携ごとに異なるスケジュールを設定できます。同期は最大頻度で 15 分ごと、最小頻度で月に 1 回実行できます。15 分より短い間隔で頻繁に同期を実行する必要がある場合は、カスタマーサクセスマネージャーに相談するか、REST API 呼び出しを使用するリアルタイムのデータ取り込みを検討してください。

同期が実行されると、Braze はデータウェアハウスのインスタンスに直接接続し、指定されたテーブルから新しいデータをすべて取得して、Braze ダッシュボードで対応するデータを更新します。同期が実行されるたびに、更新されたデータが Braze に反映されます。

## サポートされるデータソース

クラウドデータ取り込みでは、以下のソースのデータを Braze に同期できます。

- データウェアハウスソース 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Snowflake

- ファイルストレージソース 
   - Amazon S3

## サポートされるデータ型 

クラウドデータ取り込みは、次のデータ型をサポートします。
\- ユーザー属性。以下を含みます。
   \- 階層化カスタム属性
   \- オブジェクトの配列
   \- サブスクリプションステータス
\- カスタムイベント
\- 購入イベント
\- カタログアイテム
\- ユーザー削除リクエスト

ユーザーデータは、external ID、ユーザーエイリアス、Braze ID、メール、または電話番号を使用して更新できます。ユーザーは external ID、ユーザーエイリアス、または Braze ID を使用して削除できます。 

## 同期されるデータ

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。最後に同期された行よりも `UPDATED_AT` が後にある行がすべて選択され、Braze に取り込まれます。

データウェアハウスで、次のユーザーと属性をテーブルに追加し、`UPDATED_AT` の時間をこのデータを追加する時間に設定します。

| UPDATED\_AT | EXTERNAL\_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribute\_1":"abcdefg",<br>    "attribute\_2": {<br>        "attribute\_a":"example\_value\_2",<br>        "attribute\_b":"example\_value\_2"<br>    },<br>    "attribute\_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribute\_1":"abcdefg",<br>    "attribute\_2":42,<br>    "attribute\_3":"2019-07-16T19:20:30+1:00",<br>    "attribute\_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute\_1":"abcdefg",<br>    "attribute\_4":true,<br>    "attribute\_5":"testing\_123"<br>} |

スケジュールされた次回の同期時に、最新のタイムスタンプより後の `UPDATED_AT` タイムスタンプを持つすべての行が Braze ユーザープロファイルに同期されます。フィールドの更新または追加が行われるので、毎回ユーザープロファイルをすべて同期する必要はありません。同期後に、新しい更新がユーザーに反映されます。

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

### 例: 初回の同期とその後の更新

この例では、最初にデータを同期し、その後の更新では変更されたデータ (差分) のみを更新する一般的なプロセスを説明します。いくつかのユーザーデータを含むテーブル `EXAMPLE_DATA` があるとします。1 日目のテーブルには次の値があります。

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
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

このデータを CDI の必要とする形式に変換するには、次のクエリを実行します。

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

このデータはどれも Braze に同期されていないため、CDI のソーステーブルにすべて追加されます。

| UPDATED\_AT          | EXTERNAL\_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

同期が実行され、Braze により「2023-03-16 15:00:00」まで利用可能なすべてのデータを同期したと記録されます。次に、2 日目の朝に ETL が実行され、ユーザーテーブルの一部のフィールドが更新されます(強調表示)。

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
            <td style="background-color: #FFFF00;">red</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

ここで、変更された値のみを CDI ソーステーブルに追加する必要があります。古い行を更新するのではなく、これらの行を追加することができます。そのテーブルは次のようになります。

| UPDATED\_AT          | EXTERNAL\_ID | PAYLOAD                                                                                   |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

CDI は新しい行だけを同期するので、次に実行される同期では最後の 5 行のみが同期されます。

### 例: 既存のオブジェクト配列内にあるフィールドの更新

この例では、既存のオブジェクト配列内にあるフィールドを更新する方法を説明しします。次のように定義されたソーステーブルがあるとします。

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

この例では、各ユーザー (`owner_id` に対応) の所有するペットの配列を追加します。具体的には、識別、血統、種類、名前を含めます。次のクエリを使用してテーブルまたはビューにデータを入力できます。

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

予測される出力は次のようになります。

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:56:17.377 +0000	03409324	{"_merge_objects":"true","pets":{"$add":[{"breed":"parakeet","id":5,"name":"Mary","type":"bird"}]}}
2023-10-02 19:56:17.377 +0000	21231234	{"_merge_objects":"true","pets":{"$add":[{"breed":"calico","id":2,"name":"Gerald","type":"cat"},{"breed":"beagle","id":1,"name":"Gus","type":"dog"}]}}
2023-10-02 19:56:17.377 +0000	12335345	{"_merge_objects":"true","pets":{"$add":[{"breed":"corgi","id":3,"name":"Doug","type":"dog"},{"breed":"salmon","id":4,"name":"Larry","type":"fish"}]}}
```

次に、更新された名前フィールドと新しい年齢フィールドを所有者ごとに送信するために、次のクエリを使用してテーブルまたはビューにデータを入力できます。

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

予測される出力は次のようになります。

```json
UPDATED_AT	EXTERNAL_ID	PAYLOAD
2023-10-02 19:50:25.266 +0000	03409324	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":5,"$new_object":{"age":7,"name":"Mary"}}]}}
2023-10-02 19:50:25.266 +0000	21231234	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":2,"$new_object":{"age":3,"name":"Gerald"}},{"$identifier_key":"id","$identifier_value":1,"$new_object":{"age":3,"name":"Gus"}}]}}
2023-10-02 19:50:25.266 +0000	12335345	{"_merge_objects":"true","pets":{"$update":[{"$identifier_key":"id","$identifier_value":3,"$new_object":{"age":6,"name":"Doug"}},{"$identifier_key":"id","$identifier_value":4,"$new_object":{"age":1,"name":"Larry"}}]}}
```

## データポイント使用量

1 人のユーザーについて送信される各属性は、データポイントを 1 だけ消費します。必要なデータのみを送信するかどうかは、ユーザーが判断します。クラウドデータ取り込みのデータポイント追跡は、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) 経由の追跡と同じです。詳細については、「[データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)」を参照してください。

{% alert important %}
Braze のクラウドデータ取り込みは利用可能なレート制限で考慮されるため、別の方法でデータを送信する場合、レート制限は Braze API とクラウドデータ取り込みの和になります。
{% endalert %}

## データ設定に関する推奨事項

### 消費を最小限に抑えるために、新規の属性または更新された属性のみを書き込む

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。最後に同期された行よりも `UPDATED_AT` が後にある行は、現在ユーザープロファイルにある行と同じかどうかにかかわらず、選択されて Braze に取り込まれます。そのため、追加または更新を行う属性のみを同期することをお勧めします。

CDI を使用したデータポイントの消費は、REST API や SDK などの他の取り込み方法と同じであるため、ソーステーブルに新規の属性または更新された属性のみを追加するかどうかはお客様次第です。

### UPDATED\_AT 列で UTC タイムスタンプを使用する

夏時間に関する問題を防ぐために、`UPDATED_AT` 列は UTC にする必要があります。できる限り、`CURRENT_DATE()` ではなく `SYSDATE()` など、UTC のみの関数を優先します。

### EXTERNAL\_ID を PAYLOAD 列から分離する

PAYLOAD オブジェクトに external ID や他の ID タイプを含めるべきではありません。 

### 属性を削除する

ある属性をユーザープロファイルから完全に削除する場合は、`null` に設定できます。属性を変更せずに残す場合は、更新されるまで Braze に送信しないでください。

### 別のテーブルから JSON 文字列を作成する

各属性を内部的に独自の列に格納する場合は、それらの列を JSON 文字列に変換して、Braze との同期を取り込む必要があります。そのために、次のようなクエリを使用できます。

{% tabs local %}
{% tab Snowflake %}
\`\`\`json
CREATE TABLE "EXAMPLE\_USER\_DATA"
    (attribute\_1 string,
     attribute\_2 string,
     attribute\_3 number,
     my\_user\_id string);

SELECT
    CURRENT\_TIMESTAMP as UPDATED\_AT,
    my\_user\_id as EXTERNAL\_ID,
    TO\_JSON(
        OBJECT\_CONSTRUCT (
            'attribute\_1',
            attribute\_1,
            'attribute\_2',
            attribute\_2,
            'yet\_another\_attribute',
            attribute\_3)
    )as PAYLOAD FROM "EXAMPLE\_USER\_DATA";
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE "EXAMPLE\_USER\_DATA"
    (attribute\_1 string,
     attribute\_2 string,
     attribute\_3 number,
     my\_user\_id string);

SELECT
    CURRENT\_TIMESTAMP as UPDATED\_AT,
    my\_user\_id as EXTERNAL\_ID,
    JSON\_SERIALIZE(
        OBJECT (
            'attribute\_1',
            attribute\_1,
            'attribute\_2',
            attribute\_2,
            'yet\_another\_attribute',
            attribute\_3)
    ) as PAYLOAD FROM "EXAMPLE\_USER\_DATA";
```
{% endtab %}
{% tab BigQuery %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE\_USER\_DATA (attribute\_1 string,
     attribute\_2 STRING,
     attribute\_3 NUMERIC,
     my\_user\_id STRING);

SELECT
    CURRENT\_TIMESTAMP as UPDATED\_AT,
    my\_user\_id as EXTERNAL\_ID,
    TO\_JSON(
      STRUCT(
        'attribute\_1' AS attribute\_1,
        'attribute\_2'AS attribute\_2,
        'yet\_another\_attribute'AS attribute\_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE\_USER\_DATA;
```
{% endtab %}
{% tab Databricks %}
```json
CREATE OR REPLACE TABLE BRAZE.EXAMPLE\_USER\_DATA (
    attribute\_1 string,
    attribute\_2 STRING,
    attribute\_3 NUMERIC,
    my\_user\_id STRING
);

SELECT
    CURRENT\_TIMESTAMP as UPDATED\_AT,
    my\_user\_id as EXTERNAL\_ID,
    TO\_JSON(
      STRUCT(
        attribute\_1,
        attribute\_2,
        attribute\_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE\_USER\_DATA;
\`\`\`
{% endtab %}
{% endtabs %}

### UPDATED\_AT タイムスタンプの使用

Braze に正常に同期されたデータの追跡には、`UPDATED_AT` タイムスタンプを使用します。同期の実行中に同じタイムスタンプを持つ多くの行が書き込まれると、データが重複して Braze に同期される可能性があります。データの重複を回避するための推奨事項をいくつか示します。
- `VIEW` に対して同期を設定する場合は、デフォルト値として `CURRENT_TIMESTAMP` を使用しないでください。使用すると、同期が実行されるたびにすべてのデータが同期されます。これは、`UPDATED_AT` フィールドの評価結果がクエリの実行時間になるためです。
\- ソーステーブルにデータを書き込むパイプラインやクエリの実行時間が非常に長い場合は、これらを同期と同時に実行することを避けるか、挿入される各行に同じタイムスタンプを使用することを避けます。
\- トランザクションを使用して、同じタイムスタンプを持つすべての行を書き込みます。

### テーブルの設定例

お客様がベストプラクティスやコードスニペットを共有できるように、[GitHub リポジトリ](https://github.com/braze-inc/braze-examples/tree/main/data-ingestion)を公開しています。独自のスニペットを投稿するには、プルリクエストを作成してください。

### サンプルデータのフォーマット

階層化カスタム属性の更新、サブスクリプションステータスの追加、カスタムイベントまたは購入の同期など、Braze の `/users/track` エンドポイントを通じて可能な操作はすべて、クラウドデータ取り込みでサポートされます。 

{% tabs local %}
{% tab Nested Custom Attributes %}
カスタム属性を同期するために、階層化カスタム属性をペイロード列に含めることができます。 

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
イベントを同期するには、イベント名が必要です。`time` フィールドは、ISO 8601 文字列または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式でフォーマットする必要があります。`time` フィールドが存在しない場合、`UPDATED_AT` 列の値がイベント時刻として使用されます。`app_id` と `properties` を含むその他のフィールドはオプションです。
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
購入イベントを同期するには、イベント名、`product_id`、`currency`、および `price` が必要です。`time` フィールドはオプションですが、ISO 8601 文字列または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式でフォーマットする必要があります。`time` フィールドが存在しない場合、`UPDATED_AT` 列の値がイベント時刻として使用されます。`app_id`、`quantity`、`properties` を含むその他のフィールドはオプションです。 

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
{% endtabs %}

## 製品の制限事項

| 制限            | 説明                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 連携の数 | 設定できる連携の数に制限はありません。ただし、テーブルまたはビューごとに設定できる連携は 1 つのみです。                                             |
| 行数         | 同期できる行数に制限はありません。各行は `UPDATED` 列に基づいて一度だけ同期されます。                                                            |
| 行ごとの属性     | 各行には、単一のユーザー ID と最大 250 の属性を持つ JSON オブジェクトが 1 つ必要です。JSON オブジェクト内の各キーは 1 つの属性としてカウントされます (つまり、配列は 1 つの属性としてカウントされる)。 |
| ペイロードサイズ           | 各行に最大 1 MB のペイロードを含めることができます。1 MB を超えるペイロードは拒否され、「Payload was greater than 1MB」(ペイロードが 1 MB を超えていました) というエラーが、関連する external ID と切り詰められたペイロードとともに同期ログに記録されます。
| データ型              | クラウドデータ取り込みを通じて、ユーザー属性、イベント、および購入を同期できます。                                                                                                  |
| Braze の地域           | この製品はすべての Braze の地域で利用できます。どの Braze の地域も任意のソースデータの地域に接続できます。                                                                              |
| ソースの地域 | Brazeは、あらゆる地域またはクラウドプロバイダーのデータウェアハウスやクラウド環境に接続できます。                                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

<br><br>
