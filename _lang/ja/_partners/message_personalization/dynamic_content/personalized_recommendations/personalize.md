---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "このリファレンス記事では、Braze と Personalize.AI のパートナーシップについて説明します。Personalize.AI は、パーソナライズされたレコメンデーションによる収益成長を促進する AI ベースの SaaS ビジネスプラットフォームです。"
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) は Braze と連携し、Braze から送信されるパーソナライズされたメッセージやオファーを配信することで、収益の増加を実現します。 

Braze とPersonalize.AI の統合により、メッセージのパーソナライゼーションとターゲティングのために Personalize.AI から Braze プラットフォームにデータをエクスポートできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Personalize.AI インスタンス | このパートナーシップを利用するには、Personalize.AI インスタンスが必要である。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

* 柔軟な層別化を含むテストを展開し、顧客からのフィードバックから結果を導き出す。
* 待遇、タイミング、内容など、アイテムやオファーに対してパーソナライズされた推奨を提供する。
* 優先する目標を特定し、Braze を通じて最適なオーディエンスをターゲティングする
* 既に利用されなくなったユーザーを再び獲得する機会を特定する
* ジオロケーションデータを活用し、新規オープン店舗に適した顧客を見つける
* そっくりさんモデリングを使って、新規ユーザー向けの限られた利用可能なデータを構築し、最も関連性の高いレコメンデーションとマッチングさせる。
* 顧客のライフサイクル全体を通して顧客に関与するための適切な方法を特定する 
* 解約の可能性について顧客を事前対応的に評価し、リスクスコアを割り当て、解約の早期徴候を見つける
* パーソナライズされた介入策で顧客をターゲットにし、非活動的になるのを防ぐ

## 統合

### Personalize.AI で Braze との接続を設定する

1. Personalize.AI で、Personalize.AI インスタンスの [**Operationalization**] にある [**Integrations**] タブに移動します。
2. [**Braze**] をクリックします。 
3. Brazeとの統合を設定する。
    * **Connection Name:**コネクションに名前をつける。これは、Personalize.AI で統合を参照する方法です。
    * **同期周波数：**同期の頻度により、Personalize.AI が Braze にデータをエクスポートする頻度が制御されます。[**Daily**]、[**Weekly**]、[**Monthly**.] のいずれかを選択します。 
    * **API Key:**BrazeのAPIキーを追加する。
    * **API URL:**Braze RESTエンドポイントURLを追加する。
4. [**EXPORT**] をクリックして Braze にデータをエクスポートします。

いったんデータがエクスポートされると、Personalize.AI 、統合時に設定した同期頻度によって決められた間隔で、Brazeにデータを渡し続ける。

## この統合を使用する

Personalize.AI により、パーソナライズされたターゲティングに使用される識別子が Braze にエクスポートされます。これらのカスタム属性は、各顧客のタイミング、内容、待遇、オファーを示します。統合によっては、フィールドを顧客のプロファイルに保存する代わりに、イベントとして渡すか、[コネクテッドコンテンツ API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/) に取り込むことができます。Personalize.AI では、`external_id` を識別子として使用することがサポートされています。

Braze にインポートされたデータ属性には、一貫した用語に従って、キャンバスで使用するために直感的な名前が指定されます。たとえば Personalize.AI の属性 `C402_Target_Variant` は、Braze に `"P.AI_Model_Treatment"` としてエクスポートされます。Personalize.AI からエクスポートされる属性は、既存の属性や使用状況のトラッキングを妨げないように設計されています.。これらの属性は継続的に検証されるため、確実に参照できます。 

たとえば、解約に焦点を当てたキャンバスの例に関連する顧客属性のセットを次に示します。

| Personalize.AI 属性 | 値 |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | 治療 |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


