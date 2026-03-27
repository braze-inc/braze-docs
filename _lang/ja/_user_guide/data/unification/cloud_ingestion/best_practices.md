---
nav_title: ベストプラクティス
article_title: クラウドデータ取り込みのベストプラクティス
toc_headers: h2
page_order: 0
page_type: reference
description: "このページでは、クラウドデータ取り込みの概要、ベストプラクティス、製品の制限事項について説明します。"

---

# ベストプラクティス

> Braze クラウドデータ取り込みを使用すると、データウェアハウスやファイルストレージシステムから Braze への直接接続を設定して、関連するユーザーデータやカタログデータを同期できます。このデータを Braze に同期すると、パーソナライゼーション、トリガー、セグメンテーションなどのユースケースに活用できます。 

## `UPDATED_AT` 列を理解する

{% alert note %}
`UPDATED_AT` はデータウェアハウス統合にのみ関連するもので、S3 同期には関係ありません。
{% endalert %}

同期が実行されると、Braze はデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得し、Braze ダッシュボードの対応するデータを更新します。同期が実行されるたびに、Braze は更新されたデータを反映します。

{% alert important %}
Braze CDI は、行の内容が Braze に現在存在するものと同一であるかどうかにかかわらず、厳密に `UPDATED_AT` の値に基づいて行を同期します。そのため、不要なデータポイント使用量を避けるために、新規または更新されたデータのみを同期するよう `UPDATED_AT` を適切に利用することを推奨します。
{% endalert %}

### 例：定期的な同期

CDI 同期における `UPDATED_AT` の使用方法を示すため、ユーザー属性を更新する定期同期の例を考えてみましょう。

- ファイルストレージソース 
   - Amazon S3

## サポートされるデータタイプ 

クラウドデータ取り込みは、次のデータタイプをサポートしています。 
- ユーザー属性（以下を含む）：
   - 階層化カスタム属性
   - オブジェクト配列
   - サブスクリプションステータス
- カスタムイベント
- 購入イベント
- カタログ項目
- ユーザー削除リクエスト

ユーザーデータは、external ID、ユーザーエイリアス、Braze ID、メール、または電話番号で更新できます。ユーザーは external ID、ユーザーエイリアス、または Braze ID で削除できます。 

## 同期されるデータ

同期が実行されるたびに、Braze は以前に同期されていない行を調べます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。Braze は、最後に同期された `UPDATED_AT` の値よりも後の `UPDATED_AT` を持つ行を選択してインポートします。境界タイムスタンプと完全に一致する行も、同じタイムスタンプで新しい行が実行間に追加された場合、再同期される可能性があります。

{% alert important %}
CDI は、最後に同期された `UPDATED_AT` の値における行数を追跡します。同じタイムスタンプで新しい行が実行間に追加された場合、CDI は包含境界（`>=`）に切り替え、そのタイムスタンプのすべての行（すでに処理済みのものを含む）を再同期します。重複同期や不要なデータポイント消費を避けるために、同期実行間でユニークな `UPDATED_AT` の値を使用してください。詳細については、[重複タイムスタンプによる行の再同期を避ける](#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。
{% endalert %}

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

次のスケジュールされた同期時に、Braze は最新の同期済みタイムスタンプよりも後の `UPDATED_AT` タイムスタンプを持つすべての行を同期します。Braze はフィールドを更新または追加するため、毎回ユーザープロファイル全体を同期する必要はありません。同期後、ユーザープロファイルは新しい更新を反映します。

**定期的な同期、2回目の実行：2022年7月20日午後12時**

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

`customer_9012` の新しい行が追加されましたが、その `UPDATED_AT` の値（`2022-07-16 00:25:30`）は保存されたタイムスタンプ（`2022-07-19 09:07:23`）よりも前であるため、同期されません。ただし、`customer_5678` の既存の行は保存されたタイムスタンプと等しい `UPDATED_AT` の値を持つため、包含境界により再同期されます。この動作の詳細については、[UPDATED_AT の時間が同期の時間と同じでないことを確認する](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync)を参照してください。保存された `UPDATED_AT` は `2022-07-19 09:07:23` のままです。

**定期的な同期、3回目の実行：2022年7月21日午後12時**

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

この3回目の実行では、`customer_1234` の新しい行が追加され、その `UPDATED_AT` の値（`2022-07-21 08:30:00`）は保存されたタイムスタンプよりも後です。この新しい行と、`customer_5678` の既存の行（保存されたタイムスタンプと等しい `UPDATED_AT` を持つ）の両方が同期されます。保存された `UPDATED_AT` は `2022-07-21 08:30:00` に設定されます。

{% alert note %}
`UPDATED_AT` の値は、特定の同期の実行開始時刻よりもさらに後の時刻であっても構いません。ただし、これは推奨されません。最後の `UPDATED_AT` タイムスタンプが「未来に押しやられる」ことになり、その後の同期ではそれ以前の値が同期されなくなるためです。
{% endalert %}

## `UPDATED_AT` 列に UTC タイムスタンプを使用する

夏時間に関する問題を防ぐために、`UPDATED_AT` 列は UTC にする必要があります。できる限り、`CURRENT_DATE()` ではなく `SYSDATE()` など、UTC のみの関数を使用してください。

## 重複タイムスタンプによる行の再同期を避ける {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI は、最後に同期された `UPDATED_AT` タイムスタンプにおける行数を追跡します。CDI が前回の実行以降に同じタイムスタンプで新しい行が追加されたことを検出すると、包含境界（`>=`）を使用してそのタイムスタンプのすべての行（すでに処理済みのものを含む）を再選択します。それ以外の場合、CDI は排他境界（`>`）を使用し、最後に同期された値よりも厳密に後の行のみを選択します。

例えば、同期が `UPDATED_AT = 2025-04-01 00:00:00` の5行を処理し、後から同じタイムスタンプで6行目が追加された場合、次の同期はカウントの変化を検出し、6行すべてを再同期します。これにより、重複データや不要なデータポイント消費が発生する可能性があります。

これを避けるには：

- `VIEW` に対して同期を設定する場合、デフォルト値として `CURRENT_TIMESTAMP` を使用しないでください。使用すると、同期が実行されるたびにすべてのデータが同期されます。これは、`UPDATED_AT` フィールドの評価結果がクエリの実行時間になるためです。
- 長時間実行されるパイプラインやクエリがソーステーブルにデータを書き込んでいる場合、同期と同時に実行することを避けるか、挿入される各行に同じタイムスタンプを使用することを避けてください。
- トランザクションを使用して、同じタイムスタンプを持つすべての行を書き込みます。
- ユニークで単調増加する `UPDATED_AT` の値を使用して、処理済みの行が再選択されることを防ぎます。

### 例：その後の更新を管理する

この例では、最初にデータを同期し、その後の更新では変更されたデータ（差分）のみを更新する一般的なプロセスを説明します。いくつかのユーザーデータを含むテーブル `EXAMPLE_DATA` があるとします。1日目のテーブルには次の値があります。

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

このデータを CDI が期待する形式に変換するには、次のクエリを実行します。

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

このデータはどれも Braze に同期されていないため、CDI のソーステーブルにすべて追加します。

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

同期が実行され、Braze により「2023-03-16 15:00:00」まで利用可能なすべてのデータを同期したと記録されます。次に、2日目の朝に ETL が実行され、ユーザーテーブルの一部のフィールドが更新されます（強調表示）。

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

ここで、変更された値のみを CDI ソーステーブルに追加する必要があります。古い行を更新するのではなく、これらの行を追加できます。そのテーブルは次のようになります。

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

CDI は新しい行だけを同期するので、次に実行される同期では最後の5行のみが同期されます。

## 追加のヒント

### 消費を最小限に抑えるために、新規の属性または更新された属性のみを書き込む

同期が実行されるたびに、Braze は以前に同期されていない行を調べます。このときに、テーブルまたはビューの `UPDATED_AT` 列がチェックされます。Braze は、最後に同期された `UPDATED_AT` の値よりも後の `UPDATED_AT` を持つ行を、ユーザープロファイル上の現在の内容と同一かどうかにかかわらず、選択してインポートします。境界タイムスタンプの行も、新しい行がそのタイムスタンプを共有している場合、再同期される可能性があります。そのため、追加または更新する属性のみを同期することをお勧めします。

CDI を使用したデータポイント使用量は、REST API や SDK などの他の取り込み方法と同じです。したがって、ソーステーブルに追加するのは新規または更新された属性のみであることを確認するのは、お客様の責任です。

### `EXTERNAL_ID` を `PAYLOAD` 列から分離する

`PAYLOAD` オブジェクトには、external ID またはその他の ID タイプを含めないでください。 

### 属性を削除する

ユーザーのプロファイルから属性を省略する場合は、`null` に設定できます。属性を変更せずに残す場合は、更新されるまで Braze に送信しないでください。属性を完全に削除するには、`TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))` を使用します。

### 増分更新を行う

データの増分更新を行うことで、同時更新時の意図しない上書きを防ぐことができます。

{% alert important %}
* **異なる属性の更新：**ほとんどの場合、2つの更新がユーザーの同じ属性に影響を与えないなら、それらの結果は完全に独立しています。例えば、あるユーザーの `Color` 属性を更新し、別に `Size` 属性を更新した場合、たとえ両方の更新が数秒以内に発生したとしても、両方の更新は正しく適用されます。
* **同じ属性への更新：**複数の更新が単一の同期実行内で同じ属性を対象とする場合、競合が発生する可能性があります。こうした稀なケースでは、ある更新が別の更新を上書きすることがあります。この動作を防ぐ最善の方法は、CDI 同期のソースデータが各ユーザーの最新の状態のみを反映していること、あるいは特定のユーザーまたはユーザーと属性の組み合わせに対するすべての更新が単一の行に収められていることを保証することです。
* **オブジェクト配列演算子：**独立した更新の唯一の例外は、オブジェクト配列に対する `$add`、`$remove`、`$update` 演算子による更新です。これらの演算子では、同一の配列に対する更新が互いに干渉し合う可能性があります。
* **イベント：**競合はイベントに影響を与えません。各イベントはユニークであり、それにタイムスタンプが関連付けられているためです。
{% endalert %}

この動作を防ぐ最善の方法は、CDI 同期のソースデータが各ユーザーの最新の状態のみを反映していること、あるいは特定のユーザーまたはユーザーと属性の組み合わせに対するすべての更新が単一の行に収められていることを保証することです。

### 別のテーブルから JSON 文字列を作成する

各属性を内部的に独自の列に格納している場合は、それらの列を JSON 文字列に変換して Braze との同期に使用する必要があります。そのために、次のようなクエリを使用できます。

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

Braze は `UPDATED_AT` タイムスタンプを使用して、正常に同期されたデータを追跡します。CDI は最後に同期されたタイムスタンプにおける行数も追跡します。同じタイムスタンプで新しい行が実行間に追加された場合、CDI はそのタイムスタンプのすべての行を再同期するため、重複データが発生する可能性があります。詳細とヒントについては、[重複タイムスタンプによる行の再同期を避ける](#avoid-resyncing-rows-with-duplicate-timestamps)を参照してください。

### テーブル設定

お客様がベストプラクティスやコードスニペットを共有できるように、[GitHub リポジトリ](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion)を公開しています。独自のスニペットを投稿するには、プルリクエストを作成してください。

### データのフォーマット

階層化カスタム属性の更新、サブスクリプションステータスの追加、カスタムイベントまたは購入の同期など、Braze の `/users/track` エンドポイントを通じて可能な操作はすべて、クラウドデータ取り込みでサポートされています。 

ペイロード内のフィールドは、対応する `/users/track` エンドポイントと同じ形式に従う必要があります。詳細なフォーマット要件については、次を参照してください。

| データタイプ | フォーマットの仕様 |
| --------- | ---------| --------- | ----------- |
| `attributes` | [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object/)を参照してください |
| `events` | [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください |
| `purchases` | [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

階層化属性で[日付をキャプチャする]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties)ための特別な要件に注意してください。 

{% tabs local %}
{% tab Nested Custom Attributes %}
カスタム属性の同期では、階層化カスタム属性をペイロード列に含めることができます。 

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
イベントを同期するには、イベント名が必要です。`time` フィールドを ISO 8601 形式の文字列、または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式でフォーマットします。`time` フィールドが存在しない場合、Braze は `UPDATED_AT` 列の値をイベント時刻として使用します。`app_id` と `properties` を含むその他のフィールドはオプションです。 

同期できるのは、行ごとに1つのイベントのみであることに注意してください。

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
購入イベントを同期するには、`product_id`、`currency`、`price` が必須です。`time` フィールドはオプションであり、ISO 8601 形式の文字列または `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 形式でフォーマットします。`time` フィールドが存在しない場合、Braze は `UPDATED_AT` 列の値をイベント時刻として使用します。`app_id`、`quantity`、`properties` を含むその他のフィールドはオプションです。

1行につき1つの購入イベントのみを同期できることに注意してください。

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

最適なパフォーマンスを実現し、潜在的なエラーを回避するために、クエリは1時間以内に完了することをお勧めします。クエリがこの時間枠を超える場合は、データウェアハウスの設定を見直すことを検討してください。ウェアハウスに割り当てられたリソースを最適化することで、クエリ実行速度を向上させることができます。

## 製品の制限事項

| 制限            | 説明                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 統合の数 | 設定できる統合の数に制限はありません。ただし、テーブルまたはビューごとに1つの統合しか設定できません。                                             |
| 行数         | デフォルトでは、1回の実行で最大5億行まで同期できます。Braze は新規行が5億を超える同期を停止します。これよりも高い制限が必要な場合は、Braze カスタマーサクセスマネージャーまたは Braze サポートにお問い合わせください。 |
| 行ごとの属性     | 各行には単一のユーザー ID と最大250の属性を持つ JSON オブジェクトが含まれている必要があります。JSON オブジェクトの各キーは1つの属性としてカウントされます（つまり、配列は1つの属性としてカウントされます）。 |
| ペイロードサイズ           | 各行に最大1 MB のペイロードを含めることができます。Braze は1&nbsp;MB を超えるペイロードを拒否し、同期ログに「ペイロードが1MBを超えました」というエラーを、関連する external ID と切り詰められたペイロードと共に記録します。 |
| データタイプ              | クラウドデータ取り込みを通じて、ユーザー属性、イベント、および購入を同期できます。                                                                                                  |
| Braze リージョン           | この製品はすべての Braze リージョンで利用可能です。任意の Braze リージョンを任意のソースデータリージョンに接続できます。                                                                              |
| ソースリージョン       | Braze は、あらゆるリージョンまたはクラウドプロバイダーのデータウェアハウスやクラウド環境に接続できます。                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>