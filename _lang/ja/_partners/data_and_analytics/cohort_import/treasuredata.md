---
nav_title: トレジャーデータ
article_title: トレジャーデータのコホートインポート
description: "このリファレンス記事では、トレジャーデータのコホートインポート機能について説明します。"
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# トレジャーデータのコホートインポート

> この記事では、トレジャーデータからBrazeにユーザーコホートをインポートする方法について説明します。これにより、倉庫にしか存在しないデータに基づいてターゲットキャンペーンを送信できるようになります。

{% alert important %}
この機能は現在ベータ版です。詳細については、トレジャーデータおよび Braze の担当者にお問い合わせください。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータのアカウント | このパートナーシップを利用するには、[トレジャーデータ](https://www.treasuredata.com/)のアカウントが必要です。 |
| Braze データインポートキー | これは、Braze ダッシュボードの [**パートナー連携**] > [**テクノロジーパートナー**] からキャプチャされます。その後 [**トレジャーデータ**] を選択します。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| トレジャーデータの静的IPアドレス | トレジャーデータの静的 IP アドレスは、この統合のリンクのアクセスポイントおよびソースです。静的 IP アドレスを確認するには、トレジャーデータのカスタマーサクセス担当者またはトレジャーデータの技術サポートにご連絡ください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## データインポート統合

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**トレジャーデータ** を選択します。ここで、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。

### ステップ2:データ接続を作成する

トレジャーデータ内でデータ接続を作成する前に、認証が必要になります。まず、**インテグレーションハブ**を選択し、次に**カタログ**を選択します。

![Treasure Data Integrations Hub カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

**カタログ**でBraze統合を検索し、アイコンにカーソルを合わせて**認証の作成**を選択します。資格情報を入力し、認証に名前を付けて、**完了**を選択します。

![Treasure Data Integrations Hub カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### ステップ 3:コホートオーディエンスを定義する

**Audience Studio** でのアクティベーション、または **Data Workbench** でクエリを実行して、コホートを Braze に同期します。

{% alert important %}
Braze内にすでに存在するユーザーのみが、コホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### ステップ 3.1:クエリを定義する

{% alert note %}
クエリ列は正確な列名とデータ型で指定する必要があります。クエリの列には、`user_ids`、`device_ids`、または UI の設定と一致する Braze エイリアス列のうち、1つ以上の列が含まれている必要があります。Braze内に存在するユーザーのプロファイルのみがコホートに追加されます。コホートインポートでは、新しいユーザープロファイルは作成されません。
{% endalert %}

1. **データワークベンチ** > **クエリ** に移動します。
2. **新しいクエリ**を選択します。
3. クエリを実行して結果セットを検証します。

![Treasure Data Integrations Hub カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### ユースケース:識別子によるコホートの同期

{% subtabs local %}
{% subtab Syncing External IDs %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
列名は`user_ids`である必要があります。そうでないと同期が失敗します。
{% endalert %}

external ID を使用してコホートを同期するには、次のクエリを実行します。

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

クエリを実行すると、これらのユーザーエイリアスがBrazeのコホートに追加されます:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

ユーザーエイリアスを使用してコホートを同期するには、次のクエリを実行します:

```sql
SELECT
  email
FROM
  example_cohort_table
```

クエリを実行すると、これらのユーザーエイリアスがBrazeのコホートに追加されます:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
次にトレジャーデータのテーブルの例を示します。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
列名は`device_ids`である必要があります。そうでないと同期が失敗します。
{% endalert %}

デバイスIDを使用してコホートを同期するには、次のクエリを実行します:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

クエリを実行すると、これらのデバイスIDがBrazeのコホートに追加されます:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### ステップ 3.2:結果のエクスポートターゲットを指定します

クエリが構築されたら、**結果をエクスポート**を選択します。既存の認証 (前回の手順で作成した認証など) を選択するか、または出力に使用する新しい認証を作成できます。 

![Treasure Data Integrations Hub カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| エクスポート結果マッピング |	説明	| 
| ----------- | ----------- |
| コホートID	| これは、Brazeに送信されるバックエンドのコホート識別子です。 	|
| コホート名（任意）	| これは、Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。これが設定されていない場合、`Cohort ID`は`Cohort Name`として使用されます。	|
| Operation	| クエリがBrazeのコホートからプロファイルを追加または削除するかどうかを判断するために使用されます。	| 
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前は`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。	| 
| スレッド数 | 同時API呼び出しの数。 |

[トレジャーデータ](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)の手順に従ってエクスポートを設定し、ユースケースに対応させます。

#### ステップ 3.3:クエリを実行する

クエリに名前を付けて保存して実行するか、またはクエリを実行します。クエリが正常に完了すると、クエリ結果は自動的にBrazeにエクスポートされます。

{% endtab %}
{% tab Audience Studio %}
#### ステップ 3.1:アクティベーションを作成する

新しいSegmentを作成するか、既存のSegmentを選択して、コホートとしてBrazeに同期します。セグメント内で、**アクティベーションを作成**を選択します。

#### ステップ 3.2:アクティベーションの詳細を入力する

![トレジャーデータ統合のアクティベーションの詳細]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| アクティベーション詳細設定 |	説明	| 
| ----------- | ----------- |
| アクティベーション名	| アクティベーションの名前。	|
| アクティベーションの説明| アクティベーションの簡単な説明。	|
| 認証	| ステップ2で作成されたBrazeコホート認証を選択します。	| 
| コホートID	| これは、Brazeに送信されるバックエンドのコホート識別子です。 	|
| コホート名（任意）	| これは、Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。これが設定されていない場合、`Cohort ID`は`Cohort Name`として使用されます。	|
| Operation	| クエリがBrazeのコホートからプロファイルを追加または削除するかどうかを判断するために使用されます。	| 
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前は`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。	| 
| スレッド数 | 同時API呼び出しの数。 |

#### ステップ 3.3:出力マッピングを設定する

![Treasure Data Integrations 有効化出力Mアプリing]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| アクティベーション出力マッピング |	説明	| 
| ----------- | ----------- |
| 属性カラム	| セグメントデータベースから列を特定し、プロファイルをBrazeコホートに同期する際に識別子としてマッピングされるようにします。	|
| String Builder| Braze統合には文字列ビルダーは必要ありません。	|

{% alert important %}
 - `device_id`を識別子として使用する場合、**出力列名**は`device_ids`と名付ける必要があります。
 - エイリアスを識別子として使用する場合、**出力列名**はクエリ内の対応する列の名前でなければならず、`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。
 - `external_id`を識別子として使用する場合、**出力列名**は`user_ids`と名付ける必要があります。
{% endalert %}

すべての無関係または誤った名前の列名は無視されます。同期で複数の識別子を使用することができます。

#### ステップ 3.4:アクティベーションスケジュールを定義する

希望する同期スケジュールを定義し、アクティベーションを保存します。

![Treasure Data Integrations の有効化スケジュール]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### ステップ4:Treasure Data Export から Braze セグメントを作成する

Brazeで、**Segment**に移動し、新しいセグメントを作成して、フィルターとして**トレジャーデータコホート**を選択します。ここから、どのトレジャーデータコホートを含めるかを選択できます。トレジャーデータのコホートセグメントを作成したら、キャンペーンまたはキャンバスを作成するときにこのセグメントをオーディエンスフィルターとして選択できます。

![Treasure Data Integrations Hub カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。
