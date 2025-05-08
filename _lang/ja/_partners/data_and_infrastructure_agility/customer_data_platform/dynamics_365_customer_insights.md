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

_この統合は、Dynamics 365 Customer Insightsによって維持されている。_

## 統合について

Braze と Dynamics 365 Customer Insights の統合により、顧客セグメントを Braze にエクスポートしてキャンペーンやキャンバスで使用できるようになります。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 Customer Insights アカウント | このパートナーシップを活用するには、[Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) アカウントが必要です。必要なプラグインにアクセスするために Dynamics 365 Customer Insights アカウント内で接続を表示および編集するには、管理者としてアクセスする必要があります。 |
| Braze REST API キー | RESTAPIキーは、`users.track` 、`users.export.segment` 権限が必要である。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| プロファイル識別子の一致 | エクスポートされたセグメントの統一された顧客プロファイルには、メールアド レスを表すフィールドと、Braze`external_id` 。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Brazeの接続を設定する

Customer Insights で **[Admin] > [Connections]** に移動します。次に、[**Add connections**] を選択し、[**Braze**] を選択して接続を設定します。 

1. **表示名]**フィールドで、接続にわかりやすい名前を付ける。 
2. この接続を使用できる人を選択する。このフィールドを空白にすると、デフォルトはAdministratorsになる。詳細については、[共同作成者がエクスポートに接続を使用できるようにする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)を参照してください。
3. Braze APIキーとRESTエンドポイントを`rest.iad-03.braze.com`.
4. [**I agree**] を選択して、データとプライバシーの遵守を確認します。
5. [**Connect**] を選択して、Braze への接続を初期化します。
6. [**Add yourself as export user**] を選択し、Customer Insights の認証情報を入力します。
7. [**Save**] を選択して接続を完了します。

### ステップ2:セグメンテーションを作る

1. Brazeで、**オーディエンス**> セグメンテーションに進む。
2. Dynamics 365 Customer Insightsを通じてMicrosoftに更新させたいユーザーのセグメンテーションを作成する。
3. セグメントの**API識別子を**取得する。

### ステップ 3:エクスポートを設定する

このタイプの接続にアクセスできる場合は、このエクスポートを設定できる。詳細については、「[輸出の概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)」を参照のこと。

1. Customer Insights で **[Data] > [Exports]** に移動します。新しいエクスポートを作成するには、[**Add destination**] を選択します。
2. **Connection for export**フィールドで、Brazeセクションの接続を選択する。このセクション名が表示されない場合は、このタイプの接続はない。
3. BrazeのセグメントのAPI識別子を入力する。
4. **Data matching**セクションの**Email**フィールドで、顧客のEメールアドレスを表すフィールドを選択する。次に、**Braze Customer ID**フィールドで、顧客のBraze IDを表すフィールドを選択する。また、マッチング・データの追加フィールド（オプション）を選択することもできる。
  a. Brazeの`external_id` 、Customer InsightsのBraze顧客IDフィールドにマッピングすると、エクスポート時に既存のレコードがBrazeで更新される。
  b. Brazeのレコードの`external_id` を表さない別のIDフィールド、または空のフィールドをマッピングすると、エクスポート時にBrazeで新しいレコードが作成される。
5. 最後に、エクスポートしたいセグメンテーションを選択し、**Saveを**選択する。 

エクスポートを保存しても、すぐにエクスポートが実行されるわけではない。このエクスポートは、[スケジュールされた更新](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)ごとに実行される。[オンデマンドでデータをエクスポートする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)こともできます。 


### この統合を使う

セグメンテーションが正常にBrazeにエクスポートされると、ユーザープロファイルのカスタム属性として見つけることができる。カスタム属性には、エクスポート接続の設定時に入力されたBrazeセグメントAPI識別子が付けられる。例: `"Segment_API_Identifier": "0000-0000-0000"`

Brazeでこれらのユーザーのセグメントを作成するには、**セグメントに**移動し、新しいセグメントを作成し、フィルターとして**カスタム属性を**選択する。ここから、Dynamics 365と同期したカスタム属性を選択できる。セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

{% alert note %}
この統合の詳細については、Microsoft の [Braze 統合の記事](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)を参照してください。
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
