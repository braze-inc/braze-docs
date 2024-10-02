---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "この参考記事では、Brazeと、パーソナライズされたレコメンデーションから収益成長を促進するAIベースのSaaSビジネスプラットフォームであるPersonalize.AIの提携について概説している。"
alias: /partners/personalize/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) はBrazeと提携し、Brazeを通じて送信されるパーソナライズされたメッセージやオファーを配信することで、収益の増加を生み出している。 

BrazeとPersonalize.AI の統合により、Personalize.AI からBrazeプラットフォームにデータをエクスポートし、メッセージのパーソナライズとターゲティングを行うことができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Personalize.AI インスタンス | このパートナーシップを利用するには、Personalize.AI インスタンスが必要である。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][1]依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

* 柔軟な層別化を含むテストを展開し、顧客からのフィードバックから結果を導き出す。
* 待遇、タイミング、内容など、アイテムやオファーに対してパーソナライズされた推奨を提供する。
* Brazeを通じて、優先順位をつけた目標を特定し、最適な視聴者をターゲットにする。
* 既に利用されなくなったユーザーを再び獲得する機会を特定する
* ジオロケーションデータを活用し、新規オープン店舗に適した顧客を見つける
* そっくりさんモデリングを使って、新規ユーザー向けの限られた利用可能なデータを構築し、最も関連性の高いレコメンデーションとマッチングさせる。
* 顧客のライフサイクル全体を通して、顧客を惹きつける適切な方法を特定する 
* 解約の可能性について顧客をプロアクティブに評価し、リスクスコアを割り当てて、解約の早期指標を見つける。
* パーソナライズされた介入策で顧客をターゲットにし、非活動的になるのを防ぐ

## 統合

### でBrazeとの接続を設定する。 Personalize.AI

1. Personalize.AI で、Personalize.AI インスタンスの「**Operationalization」の**下にある**「Integrations」**タブに移動する。
2. **Brazeを**クリックする。 
3. Brazeとの統合を設定する。
    * **コネクション名だ：**コネクションに名前をつける。これが、Personalize.AI であなたの統合が参照される方法である。
    * **同期周波数：**同期頻度は、Personalize.AI 、Brazeにデータをエクスポートする頻度を制御する。**毎日**、**毎週**、**毎月を**選択する。 
    * **APIキー：**BrazeのAPIキーを追加する。
    * **APIのURL：**Braze RESTエンドポイントURLを追加する。
4. Brazeにデータを**エクスポート**するには**EXPORTを**クリックする。

いったんデータがエクスポートされると、Personalize.AI 、統合時に設定した同期頻度によって決められた間隔で、Brazeにデータを渡し続ける。

## この統合を使う

Personalize.AI パーソナライズされたターゲティングに使用される識別子をBrazeにエクスポートする。これらのカスタム属性は、各顧客のタイミング、内容、待遇、オファーを示す。Personalize.AI は、識別子として`external_id` の使用をサポートしている。

Brazeにインポートされたデータ属性は、一貫した用語に従って、Canvasesで使用するために直感的に命名される。例えば、Personalize.AI の属性`C402_Target_Variant` は、`"P.AI_Model_Treatment"` としてBrazeにエクスポートされる。Personalize.AI 、エクスポートされる属性は、既存の属性やトラッキングに干渉しないように設計されている。これらの属性は継続的に検証され、自信を持って参照できることが確認されている。 

例えば、解約に焦点を当てたキャンバスの例に関連する顧客属性のセットである。

| Personalize.AI 属性 | 価値 |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "チャーン_ミティゲーション" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | 治療 |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | 「シーザーサラダ |
| `C4_Subject_Line` | 「寂しいよ |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/
