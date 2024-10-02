---
nav_title: SalesWings
article_title: SalesWings
description: "この参考記事では、Brazeと分析プラットフォームであるSalesWingsのパートナーシップについて概説している。SalesWingsは、スコアリングとグレーディング、セールスインサイトとアラート、マーケティングアライメント、B2Bアトリビューションレポートのトラッキングを支援する。"
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [セールスウィングスは][1]、マーケティングチームと営業チームのために構築されたB2B SaaSリードプロファイリングアドオンであり、リードスコアリングとグレーディング、営業インサイトとアラート、マーケティングアライメント、B2Bアトリビューションレポートを通じて、リードとアカウントの資格認定を管理し、セールスフォースCRMとの緊密な統合を支援する。

セールスウィングスによって、マーケティングチームとマーケティング・オペレーション・マネージャーは、営業チームのためにリードとアカウントを限定することができる。さらに、SalesWingsはBrazeとともに、リードのカスタマージャーニーとBrazeのマーケティングキャンペーンのエンゲージメントデータを営業担当者に提示することができる。

## 前提条件
 
| 必要条件 | 説明 |
| ----------- | ----------- |
| セールスウィングスアカウント | このパートナーシップを利用するには、[セールスウィングスの][1]アカウントが必要である。 |
| Braze REST API キー | `users.export.ids` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][2]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Segment.com アカウント（オプション） | Segment.com ユーザーであれば、リードのプロファイリングのために、すべてのリードのエンゲージメントとプロファイルデータを送信し、Segment.com を介してイベントを特定することができる。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

{% tabs %}
{% tab リード・スコアリング %}

SalesWingsは、[最先端のリードスコアリングと](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)リードグレーディング[機能により、](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)Brazeの顧客に[、リード、コンタクト、およびアカウントを認定する柔軟な方法を](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)提供する。すべてのリード認定データは、Salesforce CRMや、リード、コンタクト、アカウント、オポチュニティを管理しレポートしたいその他のシステムにネイティブにプッシュされる。

![セールスウィングス]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %}) におけるシンプルなクリック・ノットコード・リードスコアリングモデルの例

_セールスウィングスにおけるシンプルなクリック・ノットコード・リードスコアリングモデルの例_
{% endtab %}
{% tab 営業とマーケティングの連携 %}
SalesWingsは、マーケティングチームがマーケティングで適格とされたリードを追跡し、選別し、営業チームに引き渡すことを可能にする。SalesWingsのデータはすべてSalesforceにネイティブにプッシュされ、既存のプロセスを微調整したり、リスト、レポート、フローなどを使って新しいプロセスを作成したりするのに活用できる。

![SalesWings リードスコアリングが、Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %}) 内で、リードまたはコンタクトのリストに優先順位をつける例

_SalesWingsのリードスコアリングが、Salesforce内でリードやコンタクトのリストに優先順位をつける例_

![SalesWingsのリードスコアリングがSalesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %}) 内のアカウントリストに優先順位をつける例

_SalesWingsのリードスコアリングがSalesforceのアカウントリストに優先順位をつける例_
{% endtab %}
{% tab リードとアカウントの格付け %}
SalesWingsによって、Brazeの顧客は、プロファイルデータ（通常はCRMデータ）に基づいてリードとアカウントを限定することができる。これは「リードグレーディング」、「フィットスコアリング」、「ファームグラフィックスコアリング」とも呼ばれる。Brazeの顧客は、属性データを直接SalesWingsに送信することができ、SalesWingsは、Salesforce CRMの標準またはカスタムオブジェクトのデータとレコードを読み取り、全体的なプロファイルのスコアリングを行うことができる。
{% endtab %}
{% tab 営業担当者のためのセールスインサイト %}
SalesWingsは、リード、コンタクト、アカウントに関する営業インサイトを営業担当者に表示することができる（Marketo Sales Insightsの代替）。基本的には、ブレイズとウェブのエンゲージメント・データを営業チームに見せることができる。インサイトはSalesforce CRMにネイティブに組み込まれ、他のCRMやシステムにプッシュしたり、Brazeの電子メールを介して「セールスアラート」として送信することができる。

![Salesforce 内の営業担当者向けの Sales Insights ビューの例（他の CRM システムでも利用可能）]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）_
{% endtab %}
{% tab セールスアラート %}
SalesWingsは、EメールとSlackのネイティブアラートを提供し、営業チームが日次、週次、月次のEメールレポートを取得するためにアクセスできるSalesforceのレポート購読を設定することができる。さらに、Zapierとの統合により、セールスウィングスのリードクオリフィケーションデータに基づいた追加ワークフローを構築することができる。

![Slackチャンネルによるセールスアラートの例]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slackチャンネルを使ったセールスアラートの例_
{% endtab %}
{% tab Salesforce CRMのレポーティング %}
SalesWingsとSalesforceの統合により、WebエンゲージメントデータとBrazeキャンペーンのエンゲージメントに基づいて、リード、コンタクト、アカウント、オポチュニティに関する自動化されたレポートを作成できる。例えば、特定のEメールキャンペーンをクリックした人、アプリやウェブサイトで特定のアクションを行った人など、ホットリードのリストを営業チームに見せることができる。

![Salesforce内のBrazeのEメールとマーケティング・エンゲージメントにリンクしたダッシュボードの例で、Brazeのキャンペーンが販売結果と成果に与える影響を見る]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Salesforce内のBrazeのEメールとマーケティングエンゲージメントにリンクしたダッシュボードの例で、Brazeのキャンペーンが販売結果と成果に与える影響を見る。_
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:セールスウィングスのアカウントと設定

フレンドリーなセールスウィングス・チームとの[デモを予約して][4]、セールスウィングスについてもっと知ろう。

### ステップ2:ウェブサイトやアプリに行動トラッキングを設置する

現在、SalesWingsでリードスコアリングとセールスインサイトのために行動データを収集するには2つの方法がある：
* [セールスウィングスのトラッキングJavaScriptを][5]、リードを追跡・特定したいウェブサイトやアプリに[導入する][5]。
* セールスウィングスとの統合により、行動リードアクティビティデータ（およびリードプロファイルデータ）を送信する。 Segment.com

### ステップ 3:SalesWingsとBrazeを接続する

[**セールスウィングスの設定**ページを][6]開き、**Braze Integration**セクションを展開する。

![SalesWings SettingsページのBraze Integrationセクション。][7]

新しく作成したキーの**Identifier**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze APIキー**フィールドにペーストする。

API and SDK endpoints article][8]]で説明されているように、Braze APIエンドポイントを追加し、**Braze APIエンドポイントフィールドに**入力する。**REST Endpoint**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze API endpoint**フィールドに入力する。

その後、セールスウィングス設定の**Save Changesを**クリックする。

### ステップ4:Braze、CRMとの統合など、SalesWingsのリードスコアリングを設定する

セールスウィングスのサービスチームに相談すれば、[ウェブサイトを][1]通じたフルオンボーディングサポートを受けることができる。

## この統合を使う 

リードスコアリングとセールスインサイトの作成をトリガーするために、セールスウィングスはウェブサイトやアプリでユーザーを特定する必要がある。これは以下のような形で起こりうる：

- **フォームを提出する：**ユーザーがウェブフォームを送信すると、セールスウィングスは自動的にすべてのウェブフォームタイプ（ログイン、ダウンロード、お問い合わせなど）を識別し、ユーザーがフォームを送信した際のアイデンティティを解決する。 
- **Braze IDまたは外部IDを持つURLクリック：**ユーザーがBrazeのマーケティングアクション（通常、Eメールクリック、バナークリックなど）をクリックし、SalesWingsでトラッキングしているページに誘導する。
- **GmailとOutlookのプラグイン（オプション）による販売メールのトラッキング：**営業担当者にEメール追跡プラグインを導入すれば、追跡可能なリンクを送信することで、ユーザーの完全なウェブサイト追跡が可能になる。
- **Segment.com イベントを特定する（オプション）：**Segment.com ユーザーであれば、Segment.com の統合でユーザーのIDを解決することもできる。

### URLクリックからユーザーを特定する

追跡可能なURL（例えば、EメールブラストやURL付きバナー）をクリックしたユーザーを自動的に特定することができる。URLを追跡可能にするには、リンクの末尾にパラメータとIDを追加して、Eメール、バナー、SMSでウェブサイトのURLを修正する2つの方法がある。

1. `?braze_id=` 、その後に続く。 {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **リンクの例** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=` 、その後に続く。 {% raw %}`{{${user_id}}}`{% endraw %}
  - **リンクの例** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id` 変数には、Brazeが生成したユーザーの識別子が設定され、常に利用可能である。変数`br_user_id` は、システム内のユーザー識別子に設定されるため、特定のシナリオ（Braze SDKで作成された匿名ユーザーの場合など）では欠落する可能性がある。リンクに`braze_id` と`br_user_id` の両方が使用されている場合、セールスウィングスは`braze_id` パラメータのみを考慮する。

コンフィギュレーションとさらなるトラブルシューティングについては、[セールスウィングスのサービスチームまで][1]お問い合わせください。

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
