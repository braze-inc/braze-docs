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

_この統合は、Dynamics 365 Customer Insights によって管理されます。_

## 統合について

Braze と Dynamics 365 Customer Insights の統合により、顧客セグメントを Braze にエクスポートしてキャンペーンやキャンバスで使用できるようになります。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 Customer Insights アカウント | このパートナーシップを活用するには、[Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) アカウントが必要です。必要なプラグインにアクセスするために Dynamics 365 Customer Insights アカウント内で接続を表示および編集するには、管理者としてアクセスする必要があります。 |
| Braze REST API キー | Braze REST API キーには、`users.track` と `users.export.segment` の権限が必要です。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| プロファイル識別子の一致 | エクスポートされたセグメントの統一後の顧客プロファイルには、メールアドレスを表すフィールドと、Braze`external_id` が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Brazeの接続を設定する

Customer Insights で **[Admin] > [Connections]** に移動します。次に、[**Add connections**] を選択し、[**Braze**] を選択して接続を設定します。 

1. **表示名]**フィールドで、接続にわかりやすい名前を付ける。 
2. この接続を使用できる人を選択する。このフィールドを空白にすると、デフォルトはAdministratorsになる。詳細については、[共同作成者がエクスポートに接続を使用できるようにする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)を参照してください。
3. Braze API キーと REST エンドポイントを`rest.iad-03.braze.com` の形式で入力します。
4. [**I agree**] を選択して、データとプライバシーの遵守を確認します。
5. [**Connect**] を選択して、Braze への接続を初期化します。
6. [**Add yourself as export user**] を選択し、Customer Insights の認証情報を入力します。
7. [**Save**] を選択して接続を完了します。

### ステップ2: Braze セグメントを作成する

1. Brazeで、[**オーディエンス**] > [**セグメント**] に移動します。
2. Dynamics 365 Customer Insights を介して Microsoft に更新させたいユーザーのセグメントを作成します。
3. セグメントの **API 識別子**を取得します。

### ステップ 3: エクスポートを設定する

このタイプの接続にアクセスできる場合は、このエクスポートを設定できる。詳細については、「[輸出の概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)」を参照のこと。

1. Customer Insights で **[Data] > [Exports]** に移動します。新しいエクスポートを作成するには、[**Add destination**] を選択します。
2. [**Connection for export**] フィールドで、Braze セクションの接続を選択します。このセクション名が表示されない場合は、このタイプの接続はない。
3. Braze でセグメントのセグメントAPI ID を指定します。
4. **Data matching**セクションの**Email**フィールドで、顧客のEメールアドレスを表すフィールドを選択する。次に、**Braze Customer ID** フィールドで、顧客の Braze ID を表すフィールドを選択します。また、データマッチング用の追加のオプションフィールドを選択することもできます。
  a. Braze で `external_id` を Customer Insights の Braze 顧客 ID フィールドにマップすると、エクスポート時に Braze で既存のレコードが更新されます。
  b. Braze のレコードの `external_id` を表わさない別の ID フィールド、または空のフィールドをマップすると、エクスポート時に新しいレコードが Braze で作成されます。
5. 最後に、エクスポートするセグメントを選択して、[**保存**] を選択します。 

エクスポートを保存しても、すぐにエクスポートが実行されるわけではない。このエクスポートは、[スケジュールされた更新](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)ごとに実行される。[オンデマンドでデータをエクスポートする](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)こともできます。 


### この統合を使う

セグメントが正常に Braze にエクスポートされたら、ユーザープロファイルでカスタム属性として確認できます。カスタム属性には、エクスポート接続の設定時に入力された Braze Segment API 識別子が名前として設定されます。例: `"Segment_API_Identifier": "0000-0000-0000"`

Braze でこれらのユーザーのセグメントを作成するには、[**セグメント**] に移動して、新しいセグメントを作成し、フィルターとして [**カスタム属性**] を選択します。ここから、Dynamics 365 と同期したカスタム属性を選択できます。セグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

{% alert note %}
この統合の詳細については、Microsoft の [Braze 統合の記事](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)を参照してください。
{% endalert %}


