---
nav_title: Dynamics 365カスタマーインサイト
article_title: Dynamics 365カスタマーインサイト
description: "この参考記事では、BrazeとDynamics 365 Customer Insights（主要な企業顧客データプラットフォーム）のパートナーシップについて概説している。"
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365カスタマーインサイト
 
> [Dynamics 365 Customer Insightsは](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)、顧客の360度ビューでパーソナライズされたカスタマーエクスペリエンスを提供する、エンタープライズ向けの主要な顧客データプラットフォームである。

BrazeとDynamics 365 Customer Insightsの統合により、キャンペーンやCanvasesで使用する顧客セグメントをBrazeにエクスポートできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 Customer Insightsアカウント | このパートナーシップを利用するには、[Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)アカウントが必要である。必要なプラグインにアクセスするには、Dynamics 365 Customer Insightsアカウント内で接続を表示および編集するための管理者としてのアクセス権が必要である。 |
| Braze REST API キー | すべての権限が付与されたBraze REST APIキーが必要である。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Brazeの接続を設定する

Customer Insightsで、**Admin > Connectionsに**移動する。次に、**Add connectionsを**選択し、**Brazeを**選択して接続を設定する。 

1. **表示名]**フィールドで、接続にわかりやすい名前を付ける。 
2. この接続を使用できる人を選択する。このフィールドを空白にすると、デフォルトはAdministratorsになる。詳細については、[投稿者がエクスポートに接続を使用できるようにするを](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)参照のこと。
3. サインインを続けるには、Braze APIキーを入力する。
4. データおよびプライバシーの遵守を確認することに**同意するを**選択する。
5. **Connectを**選択し、Brazeとの接続を初期化する。
6. **Add yourself as export userを**選択し、Customer Insightsの認証情報を入力する。
7. **Saveを**選択して接続を完了する。 

### ステップ2:エクスポートを設定する

このタイプの接続にアクセスできる場合は、このエクスポートを設定できる。詳細については、「[輸出の概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)」を参照のこと。

1. Customer Insightsで、**Data > Exportsに**進む。新しいエクスポートを作成するには、**Add destinationを**選択する。
2. **Connection for export**フィールドで、Brazeセクションの接続を選択する。このセクション名が表示されない場合は、このタイプの接続はない。 
3. RESTエンドポイントを次の形式でホスト名フィールドに入力する：`rest.iad-03.braze.com`.
4. **Data matching**セクションの**Email**フィールドで、顧客のEメールアドレスを表すフィールドを選択する。次に、**Customer ID**フィールドで、顧客のBraze IDを表すフィールドを選択する。また、マッチング・データ用に、追加のオプション・フィールドを選択することもできる。 
5. 最後に**Saveを**選択する。 

エクスポートを保存しても、すぐにエクスポートが実行されるわけではない。このエクスポートは、[スケジュールされた更新](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)ごとに実行される。[オンデマンドでデータをエクスポートする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)こともできる。 

### この統合を使う

セグメントがBrazeに正常にエクスポートされると、Dynamics 365 Customer Insightsのセグメントと同じ名前で、ユーザープロファイルのカスタム属性として見つけることができる。 

これらのユーザーのセグメントを作成するには、Brazeの「**セグメント**」に移動し、新しいセグメントを作成し、フィルターとして**「カスタム属性**」を選択する。ここから、Dynamics 365のカスタム属性を選択できる。セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

{% alert note %}
この統合の詳細については、マイクロソフトのBraze[統合の記事を](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)参照のこと。
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints