---
nav_title: Treasure Data
article_title:トレジャーデータコホートインポート
description:「この参考記事では、Treasure Dataのコホートインポート機能の概要を説明しています。「
page_type: partner
search_tag:Partner

---
# トレジャーデータコホートインポート

> この記事では、Treasure DataからBrazeにユーザーコホートをインポートして、ウェアハウスにしか存在しないデータに基づいてターゲットを絞ったキャンペーンを送信する方法について説明します。

{% alert important %}
この機能は現在ベータ版です。詳細については、トレジャーデータおよびBraze 担当者にお問い合わせください。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| トレジャーデータアカウント | このパートナーシップを利用するには、[トレジャーデータアカウントが必要です](https://www.treasuredata.com/)。 |
| Braze データインポートキー | **これは Braze ダッシュボードの \[**パートナーインテグレーション] > \[**テクノロジーパートナー****] からキャプチャし、\[ヒープ] を選択できます。** |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| トレジャーデータの静的 IP アドレス | Treasure Dataの固定IPアドレスは、本インテグレーションのアクセスポイントおよびリンク元です。固定IPアドレスを確認するには、トレジャーデータカスタマーサクセス担当者またはトレジャーデータテクニカルサポートにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2}

## データインポート統合

### ステップ1:Braze データインポートキーを取得

Braze で \[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[**トレジャーデータ**] を選択します。ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。

### ステップ2:データ接続を作成する

Treasure Data 内でデータ接続を作成する前に、認証を行う必要があります。まず、\[**インテグレーションハブ**] を選択し、次に \[**カタログ**] を選択します。

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %}) 

**カタログで** Braze インテグレーションを検索し、アイコンにカーソルを合わせて \[**認証を作成**] を選択します。認証情報を入力し、認証に名前を付けて、\[**完了**] を選択します。

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %}) 

### ステップ3:コホートオーディエンスを定義する

**Audience Studio** **でアクティベーションを行うか、データワークベンチでクエリを実行して、コホートを Braze に同期します。**

{% alert important %}
Braze内にすでに存在するユーザーのみがコホートに追加またはコホートから削除されます。コホートインポートでは、Brazeに新しいユーザーは作成されません。
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### ステップ 3.1:クエリを定義

{% alert note %}
クエリ列は、正確な列名とデータ型で指定する必要があります。クエリ列には、UI の設定と一致する列 (`user_ids``device_ids`、または braze alias 列) が少なくとも 1 つ含まれている必要があります。Braze 内に存在するユーザープロファイルのみがコホートに追加されます。コホートインポートでは新しいユーザープロファイルは作成されません。
{% endalert %}

1. 「**データワークベンチ**」>「**クエリ**」に移動します。
2. 「**新規クエリー**」を選択します。
3. クエリを実行して結果セットを検証します。

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### ユースケース:識別子によるコホートの同期

{% subtabs local %}
{% subtab Syncing External IDs %}
トレジャーデータのテーブルの例は次のとおりです。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
列名はでなければなりません。`user_ids`そうしないと同期は失敗します。
{% endalert %}

外部 ID を使用してコホートを同期するには、次のクエリを実行します。

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

クエリを実行すると、以下のユーザーエイリアスが Braze のコホートに追加されます。

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
トレジャーデータのテーブルの例は次のとおりです。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

ユーザーエイリアスを使用してコホートを同期するには、次のクエリを実行します。

```sql
SELECT
  email
FROM
  example_cohort_table
```

クエリを実行すると、以下のユーザーエイリアスが Braze のコホートに追加されます。

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
トレジャーデータのテーブルの例は次のとおりです。

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |

{% alert warning %}
列名はでなければなりません。`device_ids`そうしないと同期は失敗します。
{% endalert %}

デバイス ID を使用してコホートを同期するには、次のクエリを実行します。

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

クエリを実行すると、以下のデバイス ID が Braze のコホートに追加されます。

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### ステップ 3.2:結果のエクスポート対象を指定

クエリを作成したら、\[**結果をエクスポート**] を選択します。前のステップで作成したような既存の認証を選択することも、出力に使用する新しい認証を作成することもできます。 

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %}) 


| エクスポート結果マッピング |	説明	| 
| ----------- | ----------- |
| コホートID	| これは Braze に送信されるバックエンドコホート識別子です。 	|
| コホート名 (オプション)	| この名前は、Braze セグメンテーションツールのコホートフィルターに表示されます。これが設定されていない場合は、`Cohort ID`がとして使用されます`Cohort Name`。	|
| オペレーション	| クエリでBrazeのコホートにプロファイルを追加するか、コホートから削除するかを決定するために使用されます。	| 
| エイリアス (オプション) | 定義すると、クエリ内の対応する列の名前がとして送信され`alias_label`、列の各行の値がとして送信されます`alias_name`。	| 
| スレッドカウント | 同時 API 呼び出しの数。 |

[Treasure Dataの手順に従って](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)、ユースケースに合わせてエクスポートを構成してください。

#### ステップ 3.3:クエリを実行する

クエリに名前を付けて保存して実行するか、単にクエリを実行します。クエリが正常に完了すると、クエリ結果は自動的に Braze にエクスポートされます。

{% endtab %}
{% tab Audience Studio %}
#### ステップ 3.1:アクティベーションを作成する

新しいセグメントを作成するか、既存のセグメントを選択して Braze にコホートとして同期します。セグメント内で、\[**アクティベーションを作成**] を選択します。

#### ステップ 3.2:アクティベーションの詳細を記入してください

![Treasure Data Integrations Activation Details]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %}) 

| アクティベーション詳細設定 |	説明	| 
| ----------- | ----------- |
| アクティベーション名	| アクティベーションの名前。	|
| アクティベーションの説明| アクティベーションの簡単な説明。	|
| 認証	| ステップ 2 で作成した Braze コホート認証を選択します。	| 
| コホートID	| これは Braze に送信されるバックエンドコホート識別子です。 	|
| コホート名 (オプション)	| この名前は、Braze セグメンテーションツールのコホートフィルターに表示されます。これが設定されていない場合は、`Cohort ID`がとして使用されます`Cohort Name`。	|
| オペレーション	| クエリでBrazeのコホートにプロファイルを追加するか、コホートから削除するかを決定するために使用されます。	| 
| エイリアス (オプション) | 定義すると、クエリ内の対応する列の名前がとして送信され`alias_label`、列の各行の値がとして送信されます`alias_name`。	| 
| スレッドカウント | 同時 API 呼び出しの数。 |

#### ステップ 3.3:出力マッピングをセットアップ

![Treasure Data Integrations Activation Output Mapping]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %}) 

| アクティベーション出力マッピング |	説明	| 
| ----------- | ----------- |
| 属性列	| プロフィールをBrazeコホートに同期する際に識別子としてマッピングされるセグメントデータベースの列を決定します。	|
| ストリングビルダー| Braze インテグレーションには文字列ビルダーは必要ありません。	|

{% alert important %}
 - 識別子`device_id`として使用する場合、**出力列名に名前を付ける必要があります**`device_ids`。
 - エイリアスを識別子として使用する場合、**出力列名はクエリ内の対応する列の名前でなければならず**`alias_label`、`alias_name`列の各行の値はとして送信されます。
 - 識別子`external_id`として使用する場合、**出力列名に名前を付ける必要があります**`user_ids`。
{% endalert %}

関連性のない、または名前が間違っている列名はすべて無視されます。同期には複数の識別子を使用することを選択できます。

#### ステップ 3.4:アクティベーションスケジュール定義

希望の同期スケジュールを定義し、アクティベーションを保存します。

![Treasure Data Integrations Activation Schedule]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### ステップ 4:トレジャーデータエクスポートからBraze Segment を作成

Braze で \[**Segment**] に移動して新しいセグメントを作成し、フィルターとして \[**トレジャーデータコホート**] を選択します。ここから、どのトレジャーデータコホートを含めるかを選択できます。Treasure DataコホートSegment を作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %}) 
