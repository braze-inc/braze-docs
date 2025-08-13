---
nav_title: SalesWings
article_title: SalesWings
description: "この参考記事では、Brazeと分析プラットフォームであるSalesWingsのパートナーシップについて概説している。SalesWingsは、スコアリングとグレーディング、セールスインサイトとアラート、マーケティングアライメント、B2Bアトリビューションレポートのトラッキングを支援する。"
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] は、マーケティングチームとセールスチームを対象に構築された B2B SaaS リードプロファイリングアドオンです。Salesforce CRM と緊密に連携しており、リードスコアリングとリードグレーディング、セールスインサイトとセールスアラート、マーケティングとの連携、B2B アトリビューションレポートにより、リードとアカウントの適格性を管理するのに役立ちます。

_この統合は SalesWings によって管理されます。_

## 統合について

SalesWings では、マーケティングチームとマーケティングオペレーションマネージャーが、営業チームのためにリードとアカウントの適格性を評価します。これは、営業とマーケティングの連携と効率化に不可欠です。さらに SalesWings と Braze の統合により、リードのカスタマージャーニーと、Braze マーケティングキャンペーンエンゲージメントを営業担当者に提示できるため、知識に基づく会話を通じてリードクオリフィケーション率を高めることができます。

## 前提条件
 
| 必要条件 | 説明 |
| ----------- | ----------- |
| SalesWings アカウント | このパートナーシップを活用するには、[SalesWings アカウント][1]が必要です。 |
| Braze REST API キー | `users.export.ids` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][2]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Segment.com アカウント (オプション) | Segment.com をご利用の場合は、リードプロファイリングのために、すべてのリードエンゲージメントおよびプロファイルデータを送信し、Segment.com でイベントを特定することができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

{% tabs %}
{% tab リードスコアリング %}

SalesWings は、最先端のリードグレーディング機能と[リードスコアリング機能により、リード、取引先責任者、アカウントを選別する柔軟な方法](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)を Braze のお客様に提供します。すべてのリードクオリフィケーションデータは、Salesforce CRM や、リード、取引先責任者、アカウント、商談を管理および報告するその他のシステムにネイティブにプッシュされます。

![SalesWings のシンプルな click-not-code のリードスコアリングモデルの例]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_SalesWings のシンプルな click-not-code リードスコアリングモデルの例_
{% endtab %}
{% tab 営業とマーケティングの連携 %}
SalesWings では、マーケティングチームがマーケティング対象として適格なリードを追跡、選別し、営業チームに受け渡すことができます。SalesWingsのデータはすべてSalesforceにネイティブにプッシュされ、既存のプロセスを微調整したり、リスト、レポート、フローなどを使って新しいプロセスを作成したりするのに活用できる。

![SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のリードまたは取引先担当者を優先順位付けする方法の例]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のリードまたは取引先担当者を優先順位付けする方法の例_

![SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のアカウントを優先順位付けする方法の例]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のアカウントを優先順位付けする方法の例_
{% endtab %}
{% tab リードとアカウントのグレーディング %}
SalesWings では、Braze のお客様がプロファイルデータ (通常は CRM データ) に基づいてリードとアカウントを選別できます。これは「リードグレーディング」、「フィットスコアリング」、「ファームグラフィックスコアリング」とも呼ばれる。Braze のお客様は、属性データを直接 SalesWings に送信できます。SalesWings は、全体的なプロファイルスコアリングのために Salesforce CRM の標準オブジェクトまたはカスタムオブジェクトのデータとレコードを読み取ることができます。
{% endtab %}
{% tab 営業担当者のためのセールスインサイト %}
SalesWings では、リード、取引先担当者、アカウントに関するセールスインサイトを営業担当者に対して表示できます (Marketo Sales Insights の代替)。基本的には、Braze および Web エンゲージメントデータを営業チームに対して表示できます。インサイトは Salesforce CRM にネイティブに組み込まれ、他の CRM やシステムにプッシュするか、Braze のメールで「セールスアラート」として送信することができます。

![Salesforce 内の営業担当者向けのセールスインサイトビューの例 (他の CRM システムでも利用可能)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）_
{% endtab %}
{% tab セールスアラート %}
SalesWings は、ネイティブメールと Slack アラートを提供します。Salesforce でレポートサブスクリプションを設定することで、営業チームがこのサブスクリプションを使用して日次、週次、月次のメールレポートを取得できます。さらに Zapier との統合により、SalesWings のリードクオリフィケーションデータに基づいた追加ワークフローを作成できます。

![Slackチャンネルによるセールスアラートの例]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slackチャンネルを使ったセールスアラートの例_
{% endtab %}
{% tab Salesforce CRMのレポーティング %}
SalesWings と Salesforce の統合により、Web エンゲージメントデータと Braze キャンペーンエンゲージメントに基づいて、リード、取引先担当者、アカウント、商談に関する自動レポートを作成できます。例えば、特定のEメールキャンペーンをクリックした人、アプリやウェブサイトで特定のアクションを行った人など、ホットリードのリストを営業チームに見せることができる。

![Salesforce内のBrazeのEメールとマーケティング・エンゲージメントにリンクしたダッシュボードの例で、Brazeのキャンペーンが販売結果と成果に与える影響を見る]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Salesforce内のBrazeのEメールとマーケティングエンゲージメントにリンクしたダッシュボードの例で、Brazeのキャンペーンが販売結果と成果に与える影響を見る。_
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:SalesWings アカウントと設定

SalesWings について詳しく知るために、フレンドリーな SalesWings チームとの[デモをスケジュール][4]します。

### ステップ2:ウェブサイトやアプリに行動トラッキングを設置する

現在、SalesWings でリードスコアリングとセールスインサイトのために行動データを収集するには、次の2種類の方法があります。
* リードを追跡して特定したい Web サイトやアプリに、[SalesWings トラッキング JavaScriptを導入する][5]
* SalesWings とSegment.com の統合を介して行動リードアクティビティデータ (およびリードプロファイルデータ) を送信する。

### ステップ 3:SalesWingsとBrazeを接続する

[[**SalesWings Settings**] ページ][6]に移動し、[**Braze Integration**] セクションを展開します。

![[SalesWings Settings] ページの [Braze Integration] セクション。][7]

新しく作成したキーの**Identifier**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze APIキー**フィールドにペーストする。

[API と SDK のエンドポイントの記事][8]での説明に従って Braze API エンドポイントを追加し、[**Braze API endpoint**] フィールドにこのエンドポイントを入力します。**REST Endpoint**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze API endpoint**フィールドに入力する。

次に、SalesWings 設定で [**Save Changes**] をクリックします。

### ステップ4:Braze、CRMとの統合など、SalesWingsのリードスコアリングを設定する

[Web サイト][1]での完全なオンボーディングサポートについては、SalesWings のサービスチームにお問い合わせください。

## この統合を使う 

リードスコアリングとセールスインサイトの作成をトリガーするために、SalesWings は Web サイトまたはアプリでユーザーを識別する必要があります。これは次の方法で行われます。

- **フォームの送信:**ユーザーが Web フォームを送信すると、SalesWings はすべての Webフォームタイプ (ログイン、ダウンロード、お問い合わせなど) を自動的に識別し、フォームの送信時にユーザーの身元を特定します。 
- **Braze IDまたは外部IDを持つURLクリック：**ユーザーがBrazeのマーケティングアクション（通常、Eメールクリック、バナークリックなど）をクリックし、SalesWingsでトラッキングしているページに誘導する。
- **GmailとOutlookのプラグイン（オプション）による販売メールのトラッキング：**営業担当者にEメール追跡プラグインを導入すれば、追跡可能なリンクを送信することで、ユーザーの完全なウェブサイト追跡が可能になる。
- **Segment.com 識別イベント (オプション)**Segment.com ユーザーの場合は、Segment.com 統合でユーザーの身元を特定することもできます。

### URLクリックからユーザーを特定する

追跡可能なURL（例えば、EメールブラストやURL付きバナー）をクリックしたユーザーを自動的に特定することができる。URLを追跡可能にするには、リンクの末尾にパラメータとIDを追加して、Eメール、バナー、SMSでウェブサイトのURLを修正する2つの方法がある。

1. `?braze_id=` と {% raw %}`{{${braze_id}}}`{% endraw %} をこの順序で付加する 
  - **リンクの例** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=` と {% raw %}`{{${user_id}}}`{% endraw %} をこの順序で付加する
  - **リンクの例** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id` 変数には、Braze により生成されたユーザーの識別子が設定されます。この変数はいつでも使用できます。`br_user_id` 変数には、システム内のユーザーの識別子が設定されます。この変数は、特定の状況 (Braze SDK により作成された匿名ユーザーなど) では使用されない可能性があります。リンクに `braze_id` と `br_user_id` の両方が使用されている場合、SalesWings は`braze_id` パラメーターのみを考慮します。

設定とトラブルシューティングの詳細については、[SalesWings サービスチーム][1]に連絡して、オンボーディングサポートを受けてください。


[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
