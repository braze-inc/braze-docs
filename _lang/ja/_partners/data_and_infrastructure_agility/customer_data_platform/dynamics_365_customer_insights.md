---
nav_title: ダイナミクス 365 カスタマーインサイト
article_title:ダイナミクス 365 カスタマーインサイト
description:「この参考記事では、Brazeと主要なエンタープライズ顧客データプラットフォームであるDynamics 365 Customer Insightsとのパートナーシップについて概説しています。これにより、顧客セグメントをBrazeにエクスポートしてキャンペーンやキャンバスで使用できるようになります。「
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag:Partner
---

# ダイナミクス 365 カスタマーインサイト
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) は、顧客全体像を把握してパーソナライズされた顧客体験を提供する、業界をリードする企業向け顧客データプラットフォームです。

Braze と Dynamics 365 顧客インサイトの統合により、顧客セグメントを Braze にエクスポートして、キャンペーンやキャンバスで使用できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dynamics 365 カスタマーインサイトアカウント | このパートナーシップを利用するには、[Dynamics 365 カスタマーインサイトアカウントが必要です](https://dynamics.microsoft.com/en-gb/ai/customer-insights/)。必要なプラグインにアクセスするには、Dynamics 365 Customer Insights アカウント内の接続を表示および編集するには、管理者としてアクセスする必要があります。 |
| Braze REST API キー | すべての権限が付与されるには Braze REST API キーが必要です。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Braze 接続を設定する

カスタマーインサイトで、\[**管理] > \[接続**] に移動します。次に、\[**接続を追加**] を選択し、\[**Braze**] を選択して接続を設定します。 

1. \[**表示名] フィールドに、接続にわかりやすい名前を付けます**。 
2. この接続を使用できるユーザーを選択してください。このフィールドを空白のままにすると、デフォルトは「管理者」になります。詳細については、「[コントリビューターがエクスポート用に接続を使用することを許可する](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports)」を参照してください。
3. ログインを続けるには Braze API キーを入力してください。
4. \[**データおよびプライバシーコンプライアンスの確認に同意します**] を選択します。
5. \[**接続**] を選択して Braze への接続を初期化します。
6. \[**自分をエクスポートユーザーとして追加**] を選択し、カスタマーインサイトの認証情報を入力します。
7. \[**保存**] を選択して接続を完了します。 

### ステップ2:エクスポートの設定

このタイプの接続にアクセスできる場合は、このエクスポートを設定できます。詳細については、「[エクスポートの概要](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export)」を参照してください。

1. カスタマーインサイトで、\[**データ] > \[エクスポート]** に移動します。新しいエクスポートを作成するには、\[**送信先を追加**] を選択します。
2. 「**エクスポート用接続**」フィールドで、Braze セクションの接続を選択します。このセクション名が表示されない場合、このタイプの接続は利用できません。 
3. RESTエンドポイントを次の形式でホスト名フィールドに入力します:. `rest.iad-03.braze.com`
4. \[**データ照合**] セクションの \[**電子メール**] フィールドで、顧客の電子メールアドレスを表すフィールドを選択します。次に、「**顧客 ID**」フィールドで、顧客の Braze ID を表すフィールドを選択します。データを照合するための追加のオプションフィールドを選択することもできます。 
5. 最後に、\[**保存**] を選択します。 

エクスポートを保存しても、エクスポートはすぐには実行されないことに注意してください。このエクスポートは、[スケジュールされた更新ごとに実行されます](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab)。[データをオンデマンドサービスエクスポートすることもできます](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand)。 

### このインテグレーションを使用する

セグメントが Braze に正常にエクスポートされると、Dynamics 365 Customer Insights にあるSegment と同じ名前のユーザープロファイルのカスタム属性として見つけることができます。 

**これらのユーザーのセグメントを作成するには、Braze で \[Segment] に移動して新しいSegment を作成し、フィルターとして \[**カスタム属性**] を選択します。**ここから、Dynamics 365 カスタム属性を選択できます。Segment を作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。

{% alert note %}
このインテグレーションの詳細については、マイクロソフトの Braze [インテグレーションの記事をご覧ください](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze)。
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints