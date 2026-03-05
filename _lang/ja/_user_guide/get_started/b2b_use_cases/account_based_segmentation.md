---
nav_title: アカウントベースのセグメンテーション
article_title: アカウントベースのセグメンテーションの設定
page_order: 2
page_type: reference
description: "B2Bアカウントベースのセグメンテーションのユースケースを強化するためのBrazeの様々な機能の使用方法を学習する。"
---

# アカウントベースのセグメンテーションの設定

> このページでは、さまざまな Braze 機能を使用して B2B アカウントベースのセグメンテーションユースケースを強化する方法について説明します。

[B2B データモデル]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/)の設定方法に応じて、次の2つの方法で B2B アカウントベースのセグメンテーションを実行できます。

- [ビジネスオブジェクトのカタログ](#option-1-when-using-catalogs-for-your-business-objects)を使用する場合
- [ビジネスオブジェクトに接続ソース](#option-2-when-using-connected-sources-for-your-business-objects)を使用する場合

## B2Bアカウントベースのセグメンテーションの設定

### オプション 1: ビジネス・オブジェクトにカタログを使う場合

#### 基本的なSQLテンプレートのセグメンテーション

まずは、シンプルなアカウントベースのセグメンテーションのための基本的なSQLテンプレートを作成した。

ターゲットのエンタープライズアカウントの従業員であるユーザーをセグメント化するとします。 

1. [**オーディエンス**] > [**セグメントエクステンション**] > [**新規エクステンションの作成**] > [**テンプレートで開始**] の順に移動し、[**イベント用のカタログセグメント**] テンプレートを選択します。<br><br> !["テンプレートの選択 "モーダルで、イベントまたは購入のカタログセグメントオプションを選択できる。]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>SQLエディタには、ユーザーイベントデータとカタログデータを結合し、特定のカタログアイテムにエンゲージしたユーザーをセグメンテーションするテンプレートが自動的に入力される。<br><br>![[変数] タブが開いた状態の新しいエクステンションの SQL エディター。]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. [**変数**] タブを使用して、セグメントを生成する前にテンプレートに必要なフィールドを指定します。<br><br>Braze がカタログアイテムへのエンゲージメントに基づいてユーザーを識別するには、次のことを行う必要があります。
- カタログフィールドを含むカタログを選択する。
- イベントプロパティを含むカスタムイベントを選択する。
- カタログのフィールドとイベントのプロパティ値を一致させる。

##### B2Bユースケースの変数ガイドライン

B2Bアカウントベースのセグメンテーションのユースケースについて、以下の変数を選択する：

| 変数 | プロパティ |
| --- | --- |
| カタログ | アカウントカタログ |
| カタログフィールド | ID |
| カスタムイベント | account_linked |
| カスタムイベントプロパティ | account_id |
| (SQL結果のフィルターで) カタログフィールド | 分類 (Classification) |
| (「SQL 結果をフィルタ」の下) 値 | 企業 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 洗練されたSQLセグメンテーション

より高度で複雑なセグメンテーションについては、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)を参照してください。B2B アカウントベースのセグメンテーションを開始するのに役立ついくつかの SQL テンプレートを次にいくつか紹介します。

1. 1つのカタログで2つのフィルターを比較するセグメンテーションを作成する（エンタープライズレベルのアカウントでレストラン業界で働くユーザーなど）。カタログ ID とアイテム ID を含める必要があります。

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
; 
```

{: start="2"}
2\.2つの別個のカタログにまたがる2つのフィルターを比較するセグメンテーションを作成する（例えば、「ステージ3」の商談を開封しているエンタープライズターゲット口座に関連するユーザーなど）。

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### オプション 2: ビジネス・オブジェクトに接続ソースを使用する場合

セグメンテーションでの接続元の基本的な使い方については、[CDI Segment拡張機能]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)を参照してください。[カタログを使用する場合](#option-1-when-using-catalogs-for-your-business-objects)」で取り上げたテンプレートは、ソーステーブルをどのようにフォーマットするかについてのヒントになる。

## セグメントでアカウントベースのエクステンションを使用する

上記のステップでアカウントレベルのセグメンテーションを作成したら、それらのセグメントエクステンションをターゲット基準に直接取り込むことができます。また、役割、以前のキャンペーンへの参加など、ユーザーの人口統計学的基準を段階的に追加して適用することも簡単です。詳しくは、[セグメントでエクステンションを使用する]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment)を参照してください。

