---
nav_title: Personalize.AI
article_title:Personalize.AI
description:「この参考記事では、Braze と Personalize.AI のパートナーシップについて概説しています。は、パーソナライズされたレコメンデーションによって収益を伸ばす AI ベースの SaaS ビジネスプラットフォームです。「
alias: /partners/personalize/
page_type: partner
search_tag:Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) は Braze と提携して、Braze を通じてパーソナライズされたメッセージやオファーを配信することで収益を増やしています。 

Braze と Personalize.AI の統合により、Personalize.AI から Braze プラットフォームにデータをエクスポートして、メッセージをパーソナライゼーションしたりターゲティングしたりできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Personalize.AI インスタンス | このパートナーシップを利用するには、Personalize.AI インスタンスが必要です。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br>これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | あなたの REST エンドポイント URL。エンドポイントは、[インスタンスの Braze URL][1] によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

* 柔軟な階層化を含むテストを導入して、顧客からのフィードバックから結果を導き出す
* 治療、タイミング、内容など、商品やオファーに関するパーソナライズされた推奨事項を提供する
* 優先順位付けされた目標を特定し、Braze を通じて最適なオーディエンスターゲットにする
* 離脱したユーザーを再エンゲージする機会を特定する
* 位置情報データを活用して、新しくオープンした店舗に適したオーディエンス見つけましょう
* ルックアライクモデリングを使用して、新規ユーザーが利用できる限られたデータを基に、最も関連性の高い推奨事項と照合します。
* ライフサイクルを通じて顧客を引き付ける正しい方法を特定する 
* 顧客離れの可能性を積極的に評価し、リスクスコアを割り当てて解約の初期指標を見つけます。
* パーソナライズされた介入で顧客をターゲットにして、顧客が非アクティブにならないようにする

## 統合

### Personalize.AI で Braze との接続を設定します

1. Personalize.AI で、Personalize.AI インスタンスの「**運用化**」の下にある「**統合**」タブに移動します。
2. **Braze** をクリックします。 
3. Braze とのインテグレーションを設定します。
    * **接続名:**接続に名前を付けます。Personalize.AI では、インテグレーションは次のように呼ばれます。
    * **同期周波数:**同期頻度は、Personalize.AI が Braze にデータをエクスポートする頻度を制御します。\[**毎日**]、\[**毎週**]、または \[**毎月**] を選択します。 
    * **API キー:**Braze API キーを追加してください。
    * **API URL:**Braze REST エンドポイント URL を追加してください。
4. \[**エクスポート**] をクリックして Braze にデータをエクスポートします。

データがエクスポートされると、Personalize.AI は統合中に設定した同期頻度で決定された間隔でデータを Braze に渡し続けます。

## このインテグレーションを使用する

Personalize.AI は、パーソナライズされたターゲティングに使用される識別子を Braze にエクスポートします。これらのカスタム属性は、各顧客タイミング、コンテンツ、治療、およびオファーを示します。インテグレーションによっては、フィールドを顧客のプロファイルに保存する代わりに、イベントとして渡したり、[Connected Content API][2] に取り込んだりすることができます。Personalize.AI は識別子`external_id`子としての使用をサポートしています。

Brazeにインポートされたデータ属性には、一貫した用語に従って、Canvasesで使用できるように直感的に名前が付けられています。たとえば、Personalize.AI `C402_Target_Variant` の属性は Braze `"P.AI_Model_Treatment"` にとしてエクスポートされます。Personalize.AI からエクスポートされた属性は、既存の属性に影響を与えたり、使用トラッキング, 追跡したりしないように設計されています。これらの属性は継続的に検証され、安心して参照できることが確認されます。 

たとえば、チャーンに焦点を当てたCanvasの例に関連する一連の顧客属性を次に示します。

| Personalize.AI 属性 | 価値 |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  「チャーン軽減」 |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | 治療 |
| `C4_Treatment` | 「P.AI_モデル」 |
| `C4_Offer_Value` | 3 ドル |
| `C4_Item_Recom` | 「シーザーサラダ」 |
| `C4_Subject_Line` | 「あなたがいなくて寂しい」 |
{: .reset-td-br-1 .reset-td-br-2}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/
