---
nav_title: トレジャーデータ
article_title: トレジャーデータ コホート インポート
description: "このリファレンス記事は、トレジャーデータのコホートインポート機能について説明しています。"
page_type: partner
search_tag: Partner

---
# トレジャーデータコホートインポート

> この記事では、トレジャーデータからBrazeにユーザーコホートをインポートする方法について説明します。これにより、倉庫にしか存在しないデータに基づいてターゲットキャンペーンを送信できるようになります。

{% alert important %}
この機能は現在ベータ版です。詳細については、トレジャーデータおよびBrazeの担当者にお問い合わせください。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| トレジャーデータアカウント | このパートナーシップを利用するには、[トレジャーデータ](https://www.treasuredata.com/)アカウントが必要です。 |
| Braze データインポートキー | これは、**パートナー統合** > **テクノロジーパートナー** からBrazeダッシュボードでキャプチャでき、その後**Heap**を選択します。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| トレジャーデータの静的IPアドレス | トレジャーデータの静的IPアドレスは、この統合のリンクのアクセス ポイントおよびソースです。静的IPアドレスを決定するには、トレジャーデータのカスタマーサクセス担当者またはトレジャーデータの技術サポートに連絡してください。 |
{: .reset-td-br-1 .reset-td-br-2}

## データインポート統合

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**トレジャーデータ** を選択します。ここで、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成された後、新しいキーを作成するか、既存のキーを無効にすることができます。

### ステップ2:データ接続を作成する

トレジャーデータ内でデータ接続を作成する前に、認証が必要です。まず、**インテグレーションハブ**を選択し、次に**カタログ**を選択します。

![トレジャーデータ インテグレーションズ ハブ カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

**カタログ**でBraze統合を検索し、アイコンにカーソルを合わせて**認証の作成**を選択します。資格情報を入力し、認証に名前を付けて、**完了**を選択します。

![トレジャーデータ インテグレーションズ ハブ カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### ステップ 3:コホートオーディエンスを定義する

オーディエンススタジオ**Audience Studio**またはデータワークベンチ**Data Workbench**でクエリを実行することによって、Brazeにコホートを同期します。

{% alert important %}
Braze内に既に存在するユーザーのみがコホートに追加または削除されます。コホートインポートはBrazeに新しいユーザーを作成しません。
{% endalert %}

{% tabs ローカル %}
{% tab データワークベンチ %}
#### ステップ 3.1:クエリを定義する

{% alert note %}
クエリ列は正確な列名とデータ型で指定する必要があります。クエリ列には、少なくとも次の列のいずれかが含まれている必要があります: `user_ids`、`device_ids`、またはBrazeエイリアス列がUIの構成と一致します。Braze内に存在するユーザーのプロファイルのみがコホートに追加されます。コホートインポートでは、新しいユーザープロファイルは作成されません。
{% endalert %}

1. **データワークベンチ** > **クエリ** に移動します。
2. **新しいクエリ**を選択します。
3. クエリを実行して結果セットを検証します。

![トレジャーデータ インテグレーションズ ハブ カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### ユースケース:識別子によるコホートの同期

{% subtabs local %}
{% subtab Syncing External IDs %}
こちらはトレジャーデータの例のテーブルです：

| external_id |	email	| デバイスID |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
列名は`user_ids`である必要があります。そうでないと同期が失敗します。
{% endalert %}

コホートをexternal IDを使用して同期するには、次のクエリを実行します:

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
こちらはトレジャーデータの例のテーブルです：

| external_id |	email	| デバイスID |
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
こちらはトレジャーデータの例のテーブルです：

| external_id |	email	| デバイスID |
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

クエリが構築されたら、**結果をエクスポート**を選択します。既存の認証を選択するか、最後の手順で作成した認証を選択するか、新しい認証を作成して出力に使用できます。 

![トレジャーデータ インテグレーションズ ハブ カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| エクスポート結果マッピング |	説明	| 
| ----------- | ----------- |
| コホートID	| これは、Brazeに送信されるバックエンドのコホート識別子です。 	|
| コホート名（任意）	| これは、Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。これが設定されていない場合、`Cohort ID`は`Cohort Name`として使用されます。	|
| 操作	| クエリがBrazeのコホートからプロファイルを追加または削除するかどうかを判断するために使用されます。	| 
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前は`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。	| 
| スレッド数 | 同時API呼び出しの数。 |

[トレジャーデータ](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)の手順に従ってエクスポートを設定し、ユースケースに対応させます。

#### ステップ 3.3:クエリを実行する

クエリを名前で保存して実行するか、クエリを実行するだけです。クエリが正常に完了すると、クエリ結果は自動的にBrazeにエクスポートされます。

{% endtab %}
{% tab オーディエンス スタジオ %}
#### ステップ 3.1:アクティベーションを作成する

新しいSegmentを作成するか、既存のSegmentを選択して、コホートとしてBrazeに同期します。セグメント内で、**アクティベーションを作成**を選択します。

#### ステップ 3.2:アクティベーションの詳細を記入してください

![トレジャーデータインテグレーションのアクティベーション詳細]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| アクティベーション詳細設定 |	説明	| 
| ----------- | ----------- |
| アクティベーション名	| アクティベーションの名前。	|
| アクティベーションの説明| アクティベーションの簡単な説明。	|
| 認証	| ステップ2で作成されたBrazeコホート認証を選択します。	| 
| コホートID	| これは、Brazeに送信されるバックエンドのコホート識別子です。 	|
| コホート名（任意）	| これは、Brazeのセグメンテーションツール内のコホートフィルターに表示される名前です。これが設定されていない場合、`Cohort ID`は`Cohort Name`として使用されます。	|
| 操作	| クエリがBrazeのコホートからプロファイルを追加または削除するかどうかを判断するために使用されます。	| 
| 別名（オプション） | 定義されている場合、クエリ内の対応する列の名前は`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。	| 
| スレッド数 | 同時API呼び出しの数。 |

#### ステップ 3.3:出力マッピングを設定する

![トレジャーデータ インテグレーション アクティベーション 出力 マッピング]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| アクティベーション出力マッピング |	説明	| 
| ----------- | ----------- |
| 属性カラム	| セグメントデータベースから列を特定し、プロファイルをBrazeコホートに同期する際に識別子としてマッピングされるようにします。	|
| 文字列ビルダー| Braze統合には文字列ビルダーは必要ありません。	|

{% alert important %}
 - `device_id`を識別子として使用する場合、**出力列名**は`device_ids`と名付ける必要があります。
 - エイリアスを識別子として使用する場合、**出力列名**はクエリ内の対応する列の名前でなければならず、`alias_label`として送信され、列内の各行の値は`alias_name`として送信されます。
 - `external_id`を識別子として使用する場合、**出力列名**は`user_ids`と名付ける必要があります。
{% endalert %}

すべての無関係または誤った名前の列名は無視されます。同期で複数の識別子を使用することができます。

#### ステップ 3.4:アクティベーションスケジュールを定義する

希望する同期スケジュールを定義し、アクティベーションを保存します。

![トレジャーデータ インテグレーションの有効化スケジュール]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### ステップ 4:トレジャーデータエクスポートからBrazeセグメントを作成する

Brazeで、**Segment**に移動し、新しいセグメントを作成して、フィルターとして**トレジャーデータコホート**を選択します。ここから、含めたいトレジャーデータのコホートを選択できます。トレジャーデータコホートSegmentが作成された後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![トレジャーデータ インテグレーションズ ハブ カタログ]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 
