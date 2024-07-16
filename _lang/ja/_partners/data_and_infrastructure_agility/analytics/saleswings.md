---
nav_title: SalesWings
article_title:SalesWings
description:「この参考記事では、Brazeと分析プラットフォームであるSalesWingsとのパートナーシップの概要を説明しています。SalesWingsは、スコアリングとグレーディング、セールスインサイトとアラート、マーケティングアライメント、B2Bアトリビューションレポートの追跡に役立ちます。「
alias: /partners/saleswings/
page_type: partner
search_tag:Partner

---

# SalesWings

> [SalesWingsは、マーケティングチームとセールスチーム向けに構築されたB2B SaaSリードプロファイリングアドオンで、リードスコアリングとグレーディング、セールスインサイトとアラート、マーケティングアライメント、B2Bアトリビューションレポート、およびSalesforce][1] CRMとの緊密な統合を通じて、リードとアカウントの認定を管理するのに役立ちます。

SalesWingsを使用すると、マーケティングチームとマーケティングオペレーションマネージャーは、営業チームのリードと取引先を見極めることができます。これは、営業とマーケティングの連携と効率化に不可欠です。さらに、SalesWingsとBrazeを組み合わせることで、リードのカスタマージャーニーとBrazeマーケティングキャンペーンエンゲージメントデータを営業担当者に公開できるため、より知識に基づいた会話を通じてリードの資格取得率を高めることができます。

## 前提条件
 
| 必要条件 | 説明 |
| ----------- | ----------- |
| セールスウィングスアカウント | このパートナーシップを利用するには、[SalesWingsアカウントが必要です][1]。 |
| Braze REST API キー | `users.export.ids`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][2]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| Segment.com アカウント (オプション) | Segment.comのユーザーであれば、すべてのリードエンゲージメントとプロファイルデータを送信し、Segment.com経由でイベントを特定してリードプロファイリングを行うことができます。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

{% tabs %}
{% tab Lead Scoring %}

SalesWingsは[、Brazeのお客様に、最先端のリードスコアリングとリードグレーディング機能を使用して、リード、連絡先、およびアカウントを柔軟に認定する方法を提供します](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)。見込み客の資格データはすべて Salesforce CRM やその他のシステムにネイティブにプッシュされ、そこでリード、取引先、取引先、商談を管理およびレポートできます。

![Example of a simple, click-not-code lead scoring model in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_SalesWingsのシンプルなコード不要のリードスコアリングモデルの例_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWingsを使用すると、マーケティングチームはマーケティングに適したリードを追跡して見極め、営業チームに引き渡すことができます。SalesWingsのデータはすべてSalesforceにネイティブにプッシュされ、既存のプロセスを微調整したり、リスト、レポート、フローなどを使用して新しいプロセスを作成したりするために活用できます。

![Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_SalesWingsのリードスコアリングが、Salesforce内でネイティブにリードまたは連絡先のリストに優先順位を付ける方法の例_

![Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_SalesWingsのリードスコアリングがSalesforce内のアカウントのリストにネイティブに優先順位を付ける方法の例_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWingsを使用すると、Brazeの顧客はプロファイルデータ（通常はCRMデータ）に基づいてリードとアカウントを特定できます。これは、「リードグレーディング」、「フィットスコア」、または「ファーモグラフィースコアリング」とも呼ばれます。Brazeのお客様は属性データをSalesWingsに直接送信でき、SalesWingsはSalesforce CRM標準またはカスタムオブジェクトのデータやレコードを読み取って、全体的なプロファイルスコアリングを行うことができます。
{% endtab %}
{% tab Sales Insights for Sales Reps %}
SalesWingsを使用すると、営業担当者にリード、連絡先、取引先に関するセールスインサイトを表示できます（Marketo Sales Insightsの代替手段）。基本的に、Braze や Web のエンゲージメントデータはすべて営業チームに公開できます。インサイトはSalesforce CRMにネイティブに組み込まれており、他のCRMやシステムにプッシュしたり、Brazeメールで「セールスアラート」として送信したりできます。

![Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce 内の営業担当者向けのセールスインサイトビューの例 (他の CRM システムでも利用可能)_
{% endtab %}
{% tab Sales Alerts %}
SalesWingsはネイティブなメールアラートとSlackアラートを提供しており、Salesforceでレポートサブスクリプションを設定して、営業チームが毎日、毎週、毎月のメールレポートを入手できるようにすることができます。さらに、Zapier との統合により、SalesWingsのリード資格データに基づいて追加のワークフローを構築できます。

![Example of sales alert via Slack channel]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slack チャネル経由のセールスアラートの例_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
SalesWingsとSalesforceの統合により、WebエンゲージメントデータおよびBrazeキャンペーンエンゲージメントに基づいて、リード、取引先、取引先、商談を含む自動レポートを作成できます。たとえば、特定のメールキャンペーンをクリックしたり、アプリやWeb サイトで特定のアクションを実行したりしたすべてのユーザーを対象に、ホットリードのリストを営業チームに表示できます。

![Example dashboard linked to Braze email & marketing engagement within Salesforce, looking at impact of Braze campaigns on sales results and outcomes]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Brazeキャンペーンが販売結果と成果に与える影響を確認した、Salesforce内のBrazeメールとマーケティングエンゲージメントにリンクされたダッシュボードの例_
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:セールスウィングスのアカウントと設定

[親切なSalesWingsチームと一緒にデモを予約して][4]、SalesWingsについて詳しく学んでください。

### ステップ2:Web サイトまたはアプリへの行動トラッキング, 追跡のインストール

現在、リードスコアリングとセールスインサイトのためにSalesWingsで行動データを収集する方法は2つあります。
* [見込み客を追跡して特定したいウェブサイトやアプリに SalesWings のトラッキング JavaScript を導入してください][5]
* SalesWingsとSegment.comの統合により、行動に関するリードアクティビティデータ（およびリードプロファイルデータ）を送信します

### ステップ3:セールスウィングとBraze をつなぐ

[**SalesWings の設定ページに移動し**][6]、**Braze インテグレーションセクションを展開してください**。

![SalesWings 設定ページのBraze インテグレーションセクション][7]

**新しく作成したキーの識別子列の値をコピーして****、SalesWings **Braze インテグレーションセクションの Braze API キーフィールド**貼り付けます。**

\[API および SDK エンドポイント] の記事で説明されているように Braze API エンドポイントを追加し][8]、**Braze API** エンドポイントフィールドに入力します。**REST エンドポイント****列の値をコピーして、SalesWings **Braze インテグレーションセクションの Braze API エンドポイントフィールドに入力します**。**

次に、SalesWings の設定で \[**変更を保存**] をクリックします。

### ステップ 4:Braze、CRM インテグレーションなどのための SalesWings リードスコアリングの設定

[Web サイトからの完全なオンボーディングサポートについては、SalesWingsサービスチームにご相談ください。][1]

## このインテグレーションを使用する 

リードスコアリングとセールスインサイトの作成をトリガーするには、SalesWingsがWeb サイトまたはアプリ上のユーザーを識別する必要があります。このような状況は次のような場合に発生します。

- **フォーム送信:**ユーザー Webフォームを送信すると、SalesWingsはすべてのWebフォームタイプ（ログイン、ダウンロード、お問い合わせなど）を自動的に識別し、ユーザーがフォームを送信したときにユーザー身元を確認します。 
- **Braze IDまたは外部IDによるURLクリック:**ユーザー Brazeのマーケティングアクション（通常はメールクリック、バナークリックなど）をクリックすると、SalesWingsでトラッキング, 追跡しているページにつながります。
- **GmailおよびOutlookプラグインによるセールスメールトラッキング, 追跡（オプション）：**営業担当者にメール追跡プラグインを提供することにした場合、追跡可能なリンクを送信することで、営業担当者がユーザーのWeb サイト全体をトラッキング, 追跡できるようになります。
- **Segment.com 識別イベント (オプション):**Segment.comのユーザーであれば、Segment.comとの統合によりユーザー身元を確認することもできます。

### URL クリックによるユーザーの識別

追跡可能なURL（たとえば、E メールブラスト、URL 付きのバナー）をクリックしたときに、ユーザーを自動的に識別できます。URL を追跡可能にするには、リンクの末尾にパラメータと ID を追加して、電子メール、バナー、SMS のWeb サイト URL を変更する方法が 2 つあります。

1. `?braze_id=`追記に続いて続く {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **リンク例:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=`追記に続いて続く {% raw %}`{{${user_id}}}`{% endraw %}
  - **リンク例:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id`変数はBrazeによって生成されたユーザーの識別子に設定され、いつでも使用できます。`br_user_id`変数はシステム内のユーザー識別子に設定されており、特定のシナリオ（Braze SDKで作成された匿名ユーザーなど）では見つからない場合があります。`braze_id``br_user_id`リンクでとの両方が使用されている場合、`braze_id` SalesWingsはパラメータのみを考慮します。

設定やその他のトラブルシューティングについては、[SalesWingsサービスチームに連絡してオンボーディングサポートを受けてください][1]。

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
