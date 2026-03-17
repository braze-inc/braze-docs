---
nav_title: ベストプラクティス
article_title: クラウドデータ取り込みのベストプラクティス
toc_headers: h2
page_order: 0
page_type: reference
description: "このページでは、クラウドデータ取り込みの概要、ベストプラクティス、製品の制限事項について説明します。"

---

# ベストプラクティス

> Braze クラウドデータ取り込みを使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを同期できます。このデータをBrazeに同期すると、パーソナライゼーション、トリガー、セグメンテーションなどのユースケースに活用できる。 

## コラム`UPDATED_AT`を理解する

{% alert note %}
`UPDATED_AT` データウェアハウス統合にのみ関連するもので、S3同期には関係ない。
{% endalert %}

同期が実行されると、Braze はデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得し、Braze ダッシュボードの対応するデータを更新します。同期が実行されるたびに、Brazeは更新されたデータを反映する。

{% alert important %}
Braze CDIは、行の内容がBrazeに現在存在するものと同一であるか否かにかかわらず、厳密に\``UPDATED_AT`value`に基づいて行を同期する。その点を考慮すると、不要なデータポイント使用量を避けるため、新規または更新されたデータのみを同期するように適切に`UPDATED_AT`利用することを推奨する。
{% endalert %}

### 例: 定期的な同期

CDI同期における\``UPDATED_AT``の使用方法を示すため、ユーザー属性を更新する定期同期の例を考えてみよう：

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

ユーザーデータは、外部ID、ユーザーエイリアス、Braze ID、メール、または電話番号で更新できる。ユーザーは外部ID、ユーザーエイリアス、またはBraze IDで削除できる。 

## 同期されるデータ

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。Brazeは、最後の正常な同期ジョブからの最終`UPDATED_AT`タイムスタンプと`UPDATED_AT`等しいかそれ以降の行を選択し、インポートする。

データウェアハウスで、次のユーザーと属性をテーブルに追加し、`UPDATED_AT` の時間をこのデータを追加する時間に設定します。

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

次のスケジュールされた同期時に、Brazeはタイム`UPDATED_AT`スタンプが最新のものと同等かそれ以降である全ての行をユーザープロファイルに同期する。Brazeはフィールドを更新または追加するため、毎回ユーザープロファイル全体を同期する必要はない。同期後、ユーザープロファイルは新しい更新を反映する。

**定期的な同期、2回目の実行は2022年7月20日午後12時だ。**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

行が追加されたが、その`UPDATED_AT`値は（最初の実行時に`2022-07-19 09:07:23`保存された）よりも早い。その結果、これらの行はいずれも今回の実行では同期されない。同期の`UPDATED_AT`最後の値はこの実行によって変化せず、の`2022-07-19 09:07:23`ままである。

**定期的な同期、3回目の実行は2022年7月21日午後12時だ。**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

この三度目の実行では、新たな行が追加された。さて、1つの行の`UPDATED_AT`値がより遅い`2022-07-19 09:07:23`。つまり、同期されるのは1行だけだ。最後のものは今`UPDATED_AT`、に設定された`2022-07-21 08:30:00`。

{% alert note %}
`UPDATED_AT` 値は、特定の同期に対する実行開始時刻よりもさらに遅い時刻であってもよい。ただし、これは推奨されない。なぜなら、最後の`UPDATED_AT`タイムスタンプを「未来に押しやる」ことになり、その後の同期では以前の値が同期されなくなるからだ。
{% endalert %}

## `UPDATED_AT`列にUTCタイムスタンプを使用します

夏時間に関する問題を防ぐために、`UPDATED_AT` 列は UTC にする必要があります。できる限り、`CURRENT_DATE()` ではなく `SYSDATE()` など、UTC のみの関数を優先します。

## 同期する時間`UPDATED_AT`と時間が同じでないことを確認せよ

CDI同期では、いずれかの`UPDATED_AT`フィールドが前回の正常な同期ジョブの最終`UPDATED_AT`タイムスタンプと完全に一致する場合、重複データが生じる可能性がある。これは、CDI は以前の同期と同じ時刻の行を特定すると「包含境界」を選択し、それらの行を同期可能にするためです。CDI は、これらの行を再取り込みし、重複データを作成します。

重複データを避けるための提案をいくつか挙げる：

- 同期を設定する場合`VIEW`、デフォルト値として`CURRENT_TIMESTAMP`を使用するな。使用すると、同期が実行されるたびにすべてのデータが同期されます。これは、`UPDATED_AT` フィールドの評価結果がクエリの実行時間になるためです。
- 非常に長時間実行されるパイプラインやクエリがソーステーブルにデータを書き込んでいる場合、同期と同時に実行することを避けるか、挿入される各行に同じタイムスタンプを使用することを避けてください。
- トランザクションを使用して、同じタイムスタンプを持つすべての行を書き込みます。

### 例: その後の更新を管理する

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

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

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

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI は新しい行だけを同期するので、次に実行される同期では最後の 5 行のみが同期されます。

## 追加のヒント

### 消費を最小限に抑えるために、新規の属性または更新された属性のみを書き込む

同期が実行されるたびに Braze では、以前に同期されていない行が調べられます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。Brazeは、最後の正常な同期ジョブの`UPDATED_AT`タイムスタンプより`UPDATED_AT`等しいかそれ以降の行を、ユーザープロファイル上の現在の内容と同一かどうかに関わらず、選択してインポートする。そのため、追加または更新を行う属性のみを同期することをお勧めします。

CDIを使用したデータポイント使用量は、REST APIやSDKなどの他の取り込み方法と全く同じである。したがって、ソーステーブルに追加するのは新規または更新された属性のみであることを確認するのは、あなた次第だ。

### `EXTERNAL_ID` を`PAYLOAD` カラムから分離します

`PAYLOAD` オブジェクトには、external IDまたは他のIDタイプを含めないでください。 

### 属性を削除する

ユーザーのプロファイルから属性を省略する場合は、`null` に設定できます。属性を変更せずに残す場合は、更新されるまで Braze に送信しないでください。属性を完全に削除するには、`TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))` を使用します。

### 増分更新を行う

データのインクリメンタル更新を行うことで、同時更新時の意図しない上書きを防ぐことができます。

{% alert important %}
* **異なる属性の更新：**ほとんどの場合、二つの更新がユーザーの同じ属性に影響を与えないなら、それらの結果は完全に独立している。例えば、ある`Color`ユーザーの属性を更新し、別の更新`Size`で別の属性を更新した場合、たとえ両方の更新が数秒以内に発生したとしても、両方の更新は正しく適用されるべきだ。
* **同じ属性への更新：**複数の更新が単一の同期実行内で同じ属性を対象とする場合、競合が発生する可能性がある。こうした稀なケースでは、ある更新が別の更新を上書きすることがある。この動作を防ぐ最善の方法は、CDI同期のデータソースが各ユーザーの最新の状態のみを反映していること、あるいは特定のユーザーまたはユーザーと属性の組み合わせに対する全ての更新が単一の行に含まれていることを保証することだ。
* **オブジェクト配列演算子：**オブジェクト配列に対する , `$remove`, および`$update`  演算子による更新は`$add`、独立系更新の唯一の例外である。これらの演算子では、同一の配列に対する更新が互いに干渉し合う可能性がある。
* **イベント：**競合はイベントに影響を与えない。各イベントは一意であり、それにタイムスタンプが関連付けられているからだ。
{% endalert %}

この動作を防ぐ最善の方法は、CDI同期のデータソースが各ユーザーの最新の状態のみを反映していること、あるいは特定のユーザーまたはユーザーと属性の組み合わせに対する全ての更新が単一の行に含まれていることを保証することだ。

### 別のテーブルからのJSON 文字列の作成

各属性を内部的に独自の列に格納する場合は、それらの列を JSON 文字列に変換して、Braze との同期を取り込む必要があります。そのために、次のようなクエリを使用できます。

{% tabs local %}
{% tab Snowflake %}
```sql
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
```sql
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
```sql
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
```sql
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
```sql
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

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
イベントを同期するには、イベント名が必要です。フィールド`time`をISO 8601形式の文字列、または形式`yyyy-MM-dd'T'HH:mm:ss:SSSZ`でフォーマットする。フィールド`time`が存在しない場合、Brazeは列`UPDATED_AT`の値をイベント時刻として使用する。`app_id` と `properties` を含むその他のフィールドはオプションです。 

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
購入イベントを同期するには、`product_id`、`currency`、`price` が必要です。この`time`フィールドは任意であり、ISO 8601 形式の文字列または  形式`yyyy-MM-dd'T'HH:mm:ss:SSSZ`でフォーマットする。フィールド`time`が存在しない場合、Brazeは列`UPDATED_AT`の値をイベント時刻として使用する。`app_id`、`quantity`、`properties` を含むその他のフィールドはオプションです。

1 行につき1 つの購入イベントのみを同期できることに注意してください。

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
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

### データウェアハウスクエリのタイムアウトを避ける

最適なパフォーマンスを実現し、潜在的なエラーを回避するために、クエリは 1 時間以内に完了することをお勧めします。クエリがこの時間枠を超える場合は、データウェアハウスの構成を見直すことを検討してください。倉庫に割り当てられたリソースを最適化することで、クエリ実行速度を向上させることができます。

## 製品の制限事項

| 制限            | 説明                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 統合の数 | 設定できる統合の数に制限はありません。ただし、テーブルまたはビューごとに1つの統合しか設定できません。                                             |
| 行数         | デフォルトでは、1回の実行で5億行まで同期できます。Brazeは新規行が5億を超える同期を停止する。これよりも高い制限が必要な場合は、Braze カスタマーサクセスマネージャーまたはBraze サポートにお問い合わせください。 |
| 行ごとの属性     | 各行には単一のユーザー ID と最大 250 の属性を持つ JSON オブジェクトが含まれている必要があります。JSONオブジェクトの各キーは1つの属性としてカウントされます（つまり、配列は1つの属性としてカウントされます）。 |
| ペイロードサイズ           | 各行に最大 1 MB のペイロードを含めることができます。Brazeは1MBを超えるペイロードを拒否し、同期ログに「ペイロードが1MBを超えました」というエラーを、関連する外部IDと切り詰められたペイロードと共に記録する。 |
| データタイプ              | クラウドデータ取り込みを通じて、ユーザー属性、イベント、および購入を同期できます。                                                                                                  |
| Braze リージョン           | この商品はすべての Braze リージョンで利用可能です。任意の Braze リージョンを任意のソースデータリージョンに接続できます。                                                                              |
| ソースリージョン       | Braze は、あらゆるリージョンまたはクラウドプロバイダーのデータウェアハウスやクラウド環境に接続できます。                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>
