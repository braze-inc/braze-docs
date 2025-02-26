---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "このリファレンス記事では、Braze と Dynamics 365 Customer Insights のパートナーシップについて説明します。Dynamics 365 Customer Insights は業界をリードするエンタープライズ顧客データプラットフォームであり、顧客セグメントをキャンペーンまたはキャンバスで使用するために Braze にエクスポートできます。"
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights
 
> [Dynamics 365 Customer Insightsは](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)、顧客の360度ビューでパーソナライズされたカスタマーエクスペリエンスを提供する、エンタープライズ向けの主要な顧客データプラットフォームである。

Braze と Dynamics 365 Customer Insights の統合により、顧客セグメントを Braze にエクスポートしてキャンペーンやキャンバスで使用できるようになります。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 Customer Insights アカウント | このパートナーシップを活用するには、[Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) アカウントが必要です。必要なプラグインにアクセスするために Dynamics 365 Customer Insights アカウント内で接続を表示および編集するには、管理者としてアクセスする必要があります。 |
| Braze REST API キー | すべての権限が付与されたBraze REST APIキーが必要である。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Brazeの接続を設定する

Customer Insights で **[Admin] > [Connections]** に移動します。次に、[**Add connections**] を選択し、[**Braze**] を選択して接続を設定します。 

1. **表示名]**フィールドで、接続にわかりやすい名前を付ける。 
2. この接続を使用できる人を選択する。このフィールドを空白にすると、デフォルトはAdministratorsになる。詳細については、[共同作成者がエクスポートに接続を使用できるようにする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)を参照してください。
3. サインインを続けるには、Braze APIキーを入力する。
4. [**I agree**] を選択して、データとプライバシーの遵守を確認します。
5. [**Connect**] を選択して、Braze への接続を初期化します。
6. [**Add yourself as export user**] を選択し、Customer Insights の認証情報を入力します。
7. [**Save**] を選択して接続を完了します。 

### ステップ2:エクスポートを設定する

このタイプの接続にアクセスできる場合は、このエクスポートを設定できる。詳細については、「[輸出の概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)」を参照のこと。

1. Customer Insights で **[Data] > [Exports]** に移動します。新しいエクスポートを作成するには、[**Add destination**] を選択します。
2. **Connection for export**フィールドで、Brazeセクションの接続を選択する。このセクション名が表示されない場合は、このタイプの接続はない。 
3. RESTエンドポイントを次の形式でホスト名フィールドに入力する：`rest.iad-03.braze.com`.
4. **Data matching**セクションの**Email**フィールドで、顧客のEメールアドレスを表すフィールドを選択する。次に、**Customer ID**フィールドで、顧客のBraze IDを表すフィールドを選択する。また、データを照合するための追加のオプションフィールドを選択することもできます。 
5. 最後に [**Save**] を選択します。 

エクスポートを保存しても、すぐにエクスポートが実行されるわけではない。このエクスポートは、[スケジュールされた更新](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)ごとに実行される。[オンデマンドでデータをエクスポートする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)こともできます。 

### この統合を使う

Braze に正常にエクスポートされたセグメントは、Dynamics 365 Customer Insights にあるセグメントと同名のユーザープロファイルのカスタム属性として確認できます。 

これらのユーザーのセグメントを作成するには、Brazeの「**セグメント**」に移動し、新しいセグメントを作成し、フィルターとして**「カスタム属性**」を選択する。ここから、Dynamics 365のカスタム属性を選択できる。セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

{% alert note %}
この統合の詳細については、Microsoft の [Braze 統合の記事](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)を参照してください。
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints