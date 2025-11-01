---
nav_title: 概要
article_title: クラウドデータ取り込みの概要 
page_order: 0
page_type: reference
description: "このページでは、クラウドデータ取り込みの概要、ベストプラクティス、製品の制限事項について説明します。"

---

# Braze クラウドデータ取り込みの概要

> Braze クラウドデータ取り込みを使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを同期できます。Braze に同期すると、このデータをパーソナライゼーション、トリガー、セグメンテーションなどのユースケースに活用できます。 

## 仕組み

Braze のクラウドデータ取り込み (CDI) では、データウェアハウスのインスタンスと Braze ワークスペースとの連携を設定して、定期的にデータを同期します。この同期は設定したスケジュールで実行され、連携ごとに異なるスケジュールを設定できます。同期は最大頻度で 15 分ごと、最小頻度で月に 1 回実行できます。同期を15 分以上頻繁に実行する必要がある場合は、カスタマーサクセスマネージャーに連絡するか、リアルタイムデータ取り込みにREST API コールを使用することを検討してください。

同期が実行されると、Braze はデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得し、Braze ダッシュボードの対応するデータを更新します。同期が実行されるたびに、更新されたデータが Braze に反映されます。

## サポートされるデータソース

クラウドデータ取り込みでは、以下のソースのデータを Braze に同期できます。

- データウェアハウスソース 
   - Amazon Redshift
   - Databricks 
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake

- ファイルストレージソース 
   - Amazon S3

## サポートされるデータ型 

クラウドデータ取り込みは、次のデータ型をサポートします。 
- ユーザー属性、含む：
   - 階層化カスタム属性
   - オブジェクト配列
   - サブスクリプションステータス
- カスタムイベント
- 購入イベント
- カタログ項目
- ユーザー削除リクエスト

ユーザーデータは、external ID、ユーザーエイリアス、Braze ID、メール、または電話番号を使用して更新できます。ユーザーは external ID、ユーザーエイリアス、または Braze ID を使用して削除できます。 

## 同期されるデータ

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。`UPDATED_AT` が最後に成功した同期ジョブの`UPDATED_AT` タイムスタンプと同じかそれ以降の行が選択され、Braze に取り込まれます。

データウェアハウスで、次のユーザーと属性をテーブルに追加し、`UPDATED_AT` の時間をこのデータを追加する時間に設定します。

| UPDATED_AT | EXTERNAL_ID | PAYLOAD |
| --- | --- | --- |
| `2022-07-19 09:07:23` | `customer_1234` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2": {<br>        "attribute_a":"example_value_2",<br>        "attribute_b":"example_value_2"<br>    },<br>    "attribute_3":"2019-07-16T19:20:30+1:00"<br>} |
| `2022-07-19 09:07:23` | `customer_3456` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_2":42,<br>    "attribute_3":"2019-07-16T19:20:30+1:00",<br>    "attribute_5":"testing"<br>} |
| `2022-07-19 09:07:23` | `customer_5678` | {<br>    "attribute_1":"abcdefg",<br>    "attribute_4":true,<br>    "attribute_5":"testing_123"<br>} |

次回のスケジュールされた同期では、`UPDATED_AT` タイムスタンプが最新のタイムスタンプと同じかそれ以降のすべての行がBraze ユーザープロファイルs に同期されます。フィールドの更新または追加が行われるので、毎回ユーザープロファイルをすべて同期する必要はありません。同期後に、新しい更新がユーザーに反映されます。

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

### ユースケース:初回の同期とその後の更新

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

| UPDATED_AT          | EXTERNAL_ID | PAYLOAD                                                                                   |
| :------------------ | ----------- | ----------------------------------------------------------------------------------------- |
| 2023-03-16 15:00:00 | 12345       | { "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"} |
| 2023-03-16 15:00:00 | 23456       | { "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 34567       | { "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}  |
| 2023-03-16 15:00:00 | 45678       | { "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}   |
| 2023-03-16 15:00:00 | 56789       | { "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

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

CDI は新しい行だけを同期するので、次に実行される同期では最後の 5 行のみが同期されます。

### ユースケース:既存のオブジェクト配列内にあるフィールドの更新

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

クラウドデータ取り込みのデータポイント請求は、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track) を介した更新の請求に相当します。詳細については、「[データポイント]({{site.baseurl}}/user_guide/data/data_points/)」を参照してください。 

{% alert important %}
Braze のクラウドデータ取り込みは利用可能なレート制限で考慮されるため、別の方法でデータを送信する場合、レート制限は Braze API とクラウドデータ取り込みの和になります。
{% endalert %}

## データ設定に関する推奨事項

### 消費を最小限に抑えるために、新規の属性または更新された属性のみを書き込む

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。`UPDATED_AT` が最後に成功した同期ジョブの`UPDATED_AT` タイムスタンプと同じかそれ以降である行は、ユーザープロファイル上の現在のものと同じかどうかに関係なく、選択され、Braze に取り込まれます。そのため、追加または更新を行う属性のみを同期することをお勧めします。

データポイントの使用方法は、REST API やSDK s などの他の取り込み方法と同じであるため、ソーステーブルに新しいまたは更新 d 属性 s のみを追加するようにしてください。

### `UPDATED_AT`列にUTCタイムスタンプを使用します

夏時間に関する問題を防ぐために、`UPDATED_AT` 列は UTC にする必要があります。できる限り、`CURRENT_DATE()` ではなく `SYSDATE()` など、UTC のみの関数を優先します。

### `UPDATED_AT` の時刻が同期と同じでないことを確認します

`UPDATED_AT` フィールドs のいずれかが、前の正常な同期ジョブの最後の`UPDATED_AT` タイムスタンプとまったく同じ時刻にある場合、CDI 同期に重複データがある可能性があります。これは、CDI は以前の同期と同じ時刻の行を特定すると「包含境界」を選択し、それらの行を同期可能にするためです。CDI は、これらの行を再取り込みし、重複データを作成します。

### `EXTERNAL_ID` を`PAYLOAD` カラムから分離します

`PAYLOAD` オブジェクトには、external IDまたは他のIDタイプを含めないでください。 

### 属性を削除する

ユーザーのプロファイルから属性を省略する場合は、`null` に設定できます。属性を変更せずに残す場合は、更新されるまで Braze に送信しないでください。属性を完全に削除するには、`TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))` を使用します。

### 増分更新を行う

データのインクリメンタル更新を行うことで、同時更新時の意図しない上書きを防ぐことができます。

次の例では、ユーザーに2 つの属性があります。
- 色:"グリーン&クォート;
- サイズ:「大」

次に、Braze は、そのユーザに対して次の2 つの更新を同時に受信します。
- リクエスト1:色を「赤」に変更する
- リクエスト2:サイズを「中」に変更する

Request 1 が最初に発生するため、ユーザーの属性は次のように更新されます。
- 色:「赤」
- サイズ:「大」

ただし、リクエスト2が発生すると、Braze は元の属性値 (「グリーン」および「大」) で開始し、ユーザーの属性を次のように更新します。
- 色:"グリーン&クォート;
- サイズ:「中」

リクエストが完了すると、Request 2 はRequest 1 からの更新を上書きします。そのため、リクエストが上書きされないように更新をずらすことをお勧めします。

### 別のテーブルからのJSON 文字列の作成

各属性を内部的に独自の列に格納する場合は、それらの列を JSON 文字列に変換して、Braze との同期を取り込む必要があります。そのために、次のようなクエリを使用できます。

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

### `UPDATED_AT` タイムスタンプを使用する

Braze に正常に同期されたデータの追跡には、`UPDATED_AT` タイムスタンプを使用します。同期の実行中に同じタイムスタンプを持つ多くの行が書き込まれると、データが重複して Braze に同期される可能性があります。データの重複を回避するための推奨事項をいくつか示します。
- `VIEW` に対して同期を設定する場合は、`CURRENT_TIMESTAMP` をデフォルト値として使用しないでください。使用すると、同期が実行されるたびにすべてのデータが同期されます。これは、`UPDATED_AT` フィールドの評価結果がクエリの実行時間になるためです。 
- 非常に長時間実行されるパイプラインやクエリがソーステーブルにデータを書き込んでいる場合、同期と同時に実行することを避けるか、挿入される各行に同じタイムスタンプを使用することを避けてください。
- トランザクションを使用して、同じタイムスタンプを持つすべての行を書き込みます。

### テーブル構成

お客様がベストプラクティスやコードスニペットを共有できるように、[GitHub リポジトリ](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion)を公開しています。独自のスニペットを投稿するには、プルリクエストを作成してください。

### データのフォーマット

階層化カスタム属性の更新、サブスクリプションステータスの追加、カスタムイベントまたは購入の同期など、Braze の `/users/track` エンドポイントを通じて可能な操作はすべて、クラウドデータ取り込みでサポートされます。 

ペイロード内のフィールドは、対応する`/users/track`エンドポイントと同じ形式に従う必要があります。詳細な書式設定の要件については、次を参照してください。

| データタイプ | 書式設定の仕様 |
| --------- | ---------| --------- | ----------- |
| `attributes` | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください |
| `events` | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |

ネストされた属性で[日付をキャプチャする]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties)ための特別な要件に注意してください。 

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

同期できるのは、行ごとに1 つのイベントのみであることに注意してください。

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
購入イベントを同期するには、`product_id`、`currency`、`price` が必要です。`time` フィールドはオプションですが、ISO 8601 文字列または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式でフォーマットする必要があります。`time` フィールドが存在しない場合、`UPDATED_AT` 列の値がイベント時刻として使用されます。`app_id`、`quantity`、`properties` を含むその他のフィールドはオプションです。

1 行につき1 つの購入イベントのみを同期できることに注意してください。

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

### データウェアハウスのクエリのタイムアウトを回避する

最適なパフォーマンスを実現し、潜在的なエラーを回避するために、クエリは 1 時間以内に完了することをお勧めします。クエリがこの時間枠を超える場合は、データウェアハウスの構成を見直すことを検討してください。倉庫に割り当てられたリソースを最適化することで、クエリ実行速度を向上させることができます。

## 製品の制限事項

| 制限            | 説明                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 統合の数 | 設定できる統合の数に制限はありません。ただし、テーブルまたはビューごとに1つの統合しか設定できません。                                             |
| 行数         | デフォルトでは、1回の実行で5億行まで同期できます。新しい行が5億 を超える同期はすべて停止されます。これよりも高い制限が必要な場合は、Braze カスタマーサクセスマネージャーまたはBraze サポートにお問い合わせください。 |
| 行ごとの属性     | 各行には単一のユーザー ID と最大 250 の属性を持つ JSON オブジェクトが含まれている必要があります。JSONオブジェクトの各キーは1つの属性としてカウントされます（つまり、配列は1つの属性としてカウントされます）。 |
| ペイロードサイズ           | 各行に最大 1 MB のペイロードを含めることができます。ペイロードが1 MB を超えると拒否され、「ペイロードが 1 MB を超えました」というエラーが、関連する external ID および切り捨てられたペイロードと共に同期ログに記録されます。 |
| データタイプ              | クラウドデータ取り込みを通じて、ユーザー属性、イベント、および購入を同期できます。                                                                                                  |
| Braze リージョン           | この商品はすべての Braze リージョンで利用可能です。任意の Braze リージョンを任意のソースデータリージョンに接続できます。                                                                              |
| ソースリージョン       | Braze は、あらゆるリージョンまたはクラウドプロバイダーのデータウェアハウスやクラウド環境に接続できます。                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
