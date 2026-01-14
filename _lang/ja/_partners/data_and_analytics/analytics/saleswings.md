---
nav_title: SalesWings
article_title: SalesWings
description: "この参考記事では、BrazeとSalesWingsのパートナーシップについて概説している。SalesWingsは、Braze向けの営業・マーケティング業務ソリューションで、リードや属性の絞り込みを支援し、SalesforceなどのCRM内の営業インサイトやアラート、B2Bアトリビューションレポートを提供する。Brazeの興味やエンゲージメントを活用して、キャンバスでのパーソナライゼーションやセグメンテーションを行うことができる。セールスウィングスもまた、Digiohと同様にWebサイトからリードを生成する方法を提供している。"
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWingsは](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)、B2B SaaSのセールスおよびマーケティングオペレーションソリューションであり、総合的なリードスコアリングとグレーディングを通じてリードとアカウントの適格性を管理し、セールスインサイトとアラート、B2Bアトリビューションレポートを提供するとともに、Salesforce CRMとの緊密な統合を支援する。 Digiohと同様のWebサイト・エンゲージメント・アドオンを使えば、Webサイト上でリードを生み出すことができる。Braze内部の興味やエンゲージメントを活用して、キャンバスでのパーソナライゼーションやセグメンテーションを行うことができる。

_この統合は SalesWings によって管理されます。_

## 統合について

SalesWings では、マーケティングチームとマーケティングオペレーションマネージャーが、営業チームのためにリードとアカウントの適格性を評価します。これは、営業とマーケティングの連携とオペレーションの効率化に不可欠です。さらに、SalesWingsはBrazeとともに、リードとアカウントの完全なカスタマージャーニーとBrazeマーケティングキャンペーンのエンゲージメントデータを営業担当者に表示することができ、より精度の高い会話によってリードの認定率を向上させることができる。SalesWingsは、他のシグナルとともにニーズと関心を識別し、CRM内の営業チームに適格なバイヤーをオートメーションで引き渡すことを可能にする。特定されたニーズ、興味、販売準備状況を、パーソナライゼーションやセグメンテーションのためのBrazeユーザー属性として使用することができる。

## 前提条件
 
| 必要条件 | 説明 |
| ----------- | ----------- |
| SalesWings アカウント | このパートナーシップを活用するには、[SalesWings アカウント](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)が必要です。 |
| Braze REST API キー | `users.export.ids` の権限を持つREST APIキー（SalesWingsのインサイトプッシュ機能を使用する場合は、`users.track` ）。<br><br> これは、Braze ダッシュボードの [**設定**] > [**API キー**] で作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Segment.com アカウント (オプション) | Segment.com をご利用の場合は、リードプロファイリングのために、すべてのリードエンゲージメントおよびプロファイルデータを送信し、Segment.com でイベントを特定することができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

{% tabs %}
{% tab Lead and Account Scoring %}

SalesWings は、最先端のリードグレーディング機能と[リードスコアリング機能により、リード、取引先責任者、アカウントを選別する柔軟な方法](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs)を Braze のお客様に提供します。すべてのリードクオリフィケーションデータは、Salesforce CRM や、リード、取引先責任者、アカウント、商談を管理および報告するその他のシステムにネイティブにプッシュされます。

![セールスウィングスにおけるシンプルなクリック・ノットコード・リードスコアリングモデルの例]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_SalesWings のシンプルな click-not-code リードスコアリングモデルの例_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings では、マーケティングチームがマーケティング対象として適格なリードを追跡、選別し、営業チームに受け渡すことができます。SalesWingsのデータはすべてSalesforceにネイティブにプッシュされ、既存のプロセスを微調整したり、リスト、レポート、フローなどを使って新しいプロセスを作成したりするのに活用できる。

![SalesWingsのリードスコアリングが、Salesforce内でリードやコンタクトのリストに優先順位をつける例]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のリードまたは取引先担当者を優先順位付けする方法の例_

![SalesWingsのリードスコアリングがSalesforceのアカウントリストに優先順位をつける例]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_SalesWings リードスコアリングにより、Salesforce 内部でネイティブに一連のアカウントを優先順位付けする方法の例_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWings では、Braze のお客様がプロファイルデータ (通常は CRM データ) に基づいてリードとアカウントを選別できます。これは「リードグレーディング」、「フィットスコアリング」、「ファームグラフィックスコアリング」とも呼ばれる。Braze のお客様は、属性データを直接 SalesWings に送信できます。SalesWings は、全体的なプロファイルスコアリングのために Salesforce CRM の標準オブジェクトまたはカスタムオブジェクトのデータとレコードを読み取ることができます。
{% endtab %}
{% tab Sales Insights for Sales Reps %}
SalesWings では、リード、取引先担当者、アカウントに関するセールスインサイトを営業担当者に対して表示できます (Marketo Sales Insights の代替)。基本的には、Braze および Web エンゲージメントデータを営業チームに対して表示できます。インサイトは Salesforce CRM にネイティブに組み込まれ、他の CRM やシステムにプッシュするか、Braze のメールで「セールスアラート」として送信することができます。

![Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce内の営業担当者向けセールスインサイトビューの例（他のCRMシステムでも利用可能）_
{% endtab %}
{% tab Sales Alerts %}
SalesWings は、ネイティブメールと Slack アラートを提供します。Salesforce でレポートサブスクリプションを設定することで、営業チームがこのサブスクリプションを使用して日次、週次、月次のメールレポートを取得できます。さらに Zapier との統合により、SalesWings のリードクオリフィケーションデータに基づいた追加ワークフローを作成できます。

![Slackチャネルを通じたセールスアラートの例]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slackチャンネルを使ったセールスアラートの例_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
SalesWings と Salesforce のネイティブ統合により、Web エンゲージメントデータと Braze Currents のネイティブ統合によるあらゆる Braze キャンペーンエンゲージメントに基づいて、リード、取引先責任者、取引先、および商談に関する自動レポートを構築できます。例えば、特定のEメールキャンペーンをクリックした人、アプリやウェブサイトで特定のアクションを行った人など、ホットリードのリストを営業チームに見せることができる。

![Brazeのメールにリンクしたダッシュボードの例& Salesforce内のマーケティングエンゲージメントは、Brazeのキャンペーンが営業結果や成果に与える影響を見ている。]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Brazeのメールにリンクしたダッシュボードの例& Salesforce内のマーケティングエンゲージメントは、Brazeのキャンペーンがセールスの結果や成果に与える影響を見ている。_
{% endtab %}
{% endtabs %}

## 統合

### ステップ1:SalesWings アカウントと設定

SalesWings について詳しく知るために、フレンドリーな SalesWings チームとの[デモをスケジュール](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs)します。

### ステップ2:ウェブサイトやアプリに行動トラッキングを設置する

SalesWings でリードスコアリングとセールスインサイトのために行動データを収集し買い手の意図、セールスのインサイトを特定する方法はいくつかあります。
* リードを追跡して特定したい Web サイトやアプリに、[SalesWings トラッキング JavaScriptを導入する](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script)
* イベントプロパティと共に Braze イベントを Braze Currents 経由で SalesWings に取り込む
* [SalesWings と Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration) の統合を介して行動リードアクティビティデータ (およびリードプロファイルデータ) を送信する
* サードパーティのソリューションから SalesWings [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) に直接データを送信

### ステップ 3: SalesWingsとBrazeを接続する

[[**SalesWings Integrations**] ページ](https://helium.saleswings.pro/integrations)に移動し、[**Braze Integration**] セクションを展開します。

![[SalesWings Settings] ページの [Braze Integration] セクション。]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

新しく作成したキーの**Identifier**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze APIキー**フィールドにペーストする。

[API と SDK のエンドポイントの記事]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)での説明に従って Braze API エンドポイントを追加し、[**Braze API endpoint**] フィールドにこのエンドポイントを入力します。**REST Endpoint**列の値をコピーし、SalesWings**Braze Integration**セクションの**Braze API endpoint**フィールドに入力する。

次に、**Save**を選択します。

### ステップ 4: セールスウィングスのインサイトをBrazeにプッシュできるようにする（オプション）

セグメンテーション、パーソナライゼーション、またはキャンバスジャーニーのオーケストレーションのために、BrazeユーザープロファイルでSalesWingsインサイトを利用できるようにしたい場合は、[**SalesWings Integrations**](https://helium.saleswings.pro/integrations)ページにアクセスし、**Braze Integration**セクションを展開してください。

**SalesWings-to-Braze insightsデータプッシュの**下にある**Start data pushを**クリックする。

### ステップ 5: SalesWings への Currents カスタムエクスポートの設定 (オプション)

[ユーザー行動や]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) [メッセージエンゲージメントの]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events)イベントを、行動インテリジェンス、リードやアカウントのスコアリング、セールスインサイトの作成、CRMでのレポート作成に使用したい場合は、[**SalesWings Integrations**ページに](https://helium.saleswings.pro/integrations)行き、**Braze Integration**セクションを展開する。

[**API トークンの生成**] で [**生成**] を選択して、カスタム Currents エクスポートを設定します。

次に、[Current を新規作成し]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents)、Current タイプとして**カスタム Currents エクスポート**を選択します。

Currents 作成フォームの**認証情報**セクションで、[**SalesWings の「統合」**ページ](https://helium.saleswings.pro/integrations)で生成した API トークンを「**ベアラートークン**」に `https://helium.saleswings.pro/api/braze/currents/events` を「**エンドポイント**」に入力します。

### ステップ 6: Braze用のSalesWingsリードとアカウントスコアリング、CRM統合などを設定する

[Web サイト](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)での完全なオンボーディングサポートについては、SalesWings のサービスチームにお問い合わせください。

## この統合を使う 

行動データやその他のデータをリードや取引先にトリガーするためには、SalesWings は、Webサイトやアプリで、またはサードパーティの統合を通じて、ユーザーを識別する必要があります。これは次の方法で行われます。

- **フォームの送信:**ユーザーが Web フォームを送信すると、SalesWings はすべての Webフォームタイプ (ログイン、ダウンロード、お問い合わせなど) を自動的に識別し、フォームの送信時にユーザーの身元を特定します。 
- **Braze IDまたは外部IDを持つURLクリック：**ユーザーがBrazeのマーケティングアクション（通常、Eメールクリック、バナークリックなど）をクリックし、SalesWingsでトラッキングしているページに誘導する。
- **Braze Currents イベント (オプション):**カスタム Currents の SalesWings へのエクスポートが設定されている場合、SalesWings は、Current に送信されるイベントを含むメールを使用して、すべての Braze ユーザーに対して識別されたプロファイルを作成します。
- **GmailとOutlookのプラグイン（オプション）による販売メールのトラッキング：**営業担当者にEメール追跡プラグインを導入すれば、追跡可能なリンクを送信することで、ユーザーの完全なウェブサイト追跡が可能になる。
- **Segment.com 識別イベント (オプション)**Segment.com ユーザーの場合は、Segment.com 統合でユーザーの身元を特定することもできます。

### URLクリックからユーザーを特定する

追跡可能なURL（例えば、EメールブラストやURL付きバナー）をクリックしたユーザーを自動的に特定することができる。URLを追跡可能にするには、リンクの末尾にパラメータとIDを追加して、Eメール、バナー、SMSでウェブサイトのURLを修正する2つの方法がある。

1. `?braze_id=` と {% raw %}`{{${braze_id}}}`{% endraw %} をこの順序で付加する 
  - **リンクの例** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=` と {% raw %}`{{${user_id}}}`{% endraw %} をこの順序で付加する
  - **リンクの例** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id` 変数には、Braze により生成されたユーザーの識別子が設定されます。この変数はいつでも使用できます。`br_user_id` 変数には、システム内のユーザーの識別子が設定されます。この変数は、特定の状況 (Braze SDK により作成された匿名ユーザーなど) では使用されない可能性があります。リンクに`braze_id` と`br_user_id` の両方が使用されている場合、セールスウィングスは`braze_id` パラメータのみを考慮する。

### SalesWingsのインサイトをBrazeにプッシュする

BrazeへのSalesWingsインサイトプッシュを有効にすると、SalesWingsは以下の[カスタム属性で]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes)Brazeユーザープロファイルを更新する：

| カスタム属性 | タイプ | 説明 |
| ----------- | ----------- | ----------- |
| `sw_favorite` | ブーリアン | リードがセールスウィングスまたはセールスフォースCRMでお気に入りとしてマークされているかどうか |
| `sw_last_active_at` | date | リードがWebサイトで最後に活動した瞬間 |
| `sw_lead_link_open` | ストリング | セールスウィングスのリードプロファイルにアクセスするためのリンク（セールスウィングスのダッシュボードアカウントがない場合） |
| `sw_lead_link_protected` | ストリング | セールスウィングスのリードプロファイルにアクセスするためのリンク（セールスウィングスのダッシュボードアカウントが必要） |
| `sw_lead_owner` | ストリング | セールスウィングスまたはセールスフォースCRMでリードに設定された所有者 |
| `sw_lead_score` | フロート | [セールスウィングスルールエンジンで](https://helium.saleswings.pro/falcon)設定されたセールスウィングスリードスコアの主な値 |
| `sw_predictive_score` | ストリング | セールスウィングスの[予測スコアの](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score)値で、トラッキングされたアクティビティの回数と反復性に基づいてリードのエンゲージメントを評価する。設定可能な値は、`HOT` 、`WARM` 、`NORMAL` 、`COLD` または `FROZEN` |
| `sw_salesforce_record_id` | ストリング | Salesforce CRM のリードまたはコンタクトレコードの ID |
| `sw_salesforce_record_url` | ストリング | Salesforce CRM のリードレコードまたはコンタクトレコードの URL |
| `sw_session_count` | 整数 | このリードのWebサイトでのトラッキング, 追跡セッション数 |
| `sw_tags` | 文字列の配列 | セールスウィングスが識別したニーズと興味は、「タグ」として表される。このリードに適用される、[セールスウィングスルールエンジンで](https://helium.saleswings.pro/falcon)設定されたセールスウィングスタグの名前 |
| その他のリードスコア属性 | フロート | [セールスウィングスルールエンジンで](https://helium.saleswings.pro/falcon)設定されたリードスコアにカスタム属性を1つ追加する。例えば、`Likeliness to meet` というスコアは、カスタム属性`sw_likeliness_to_meet` として送信される。スコアが作成された後に名前を変更した場合、セールスウィングスは最初のカスタム属性名で同期を継続する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

プッシュを有効にすると、セールスウィングスのリードプロファイルで基礎となるデータポイントが変更されると、セールスウィングスは即座にアトリビューションへのカスタム属性の送信を開始し、新しい更新がなくても、すべての既存のリードを徐々に同期する。

セールスウィングスは、セールスウィングスのリードプロファイルのメールアドレスと一致するメールをすべてのBrazeユーザーに更新する。Brazeに一致するユーザーがいない場合、セールスウィングスは新しいユーザーを作成しない。 

### CRM で Braze Currents イベントを使用する

Braze Current と SalesWings を接続する場合、SalesWings は、メールを持つすべての Braze ユーザーの特定されたリードプロファイルを作成し、サポートされている Braze イベントをリードアクティビティとして記録します。CRM では、すべてのデータをリードのアカウントレベルで自動的に集計できます。記録されたアクティビティやデータは、SalesWings のトラッキングスクリプトや Segment.com で収集された行動データ、または他のデータを SalesWings API に送信することで、さらに組み合わせることができます。また、見込み顧客のニーズや購入意欲を特定し、リードおよびアカウント管理プロセスに活用できます。

次の表は、SalesWings がサポートする Braze イベントタイプと、SalesWings のリードアクティビティ履歴およびルールエンジンにおけるそれらの表現を示します。

| イベントカテゴリー | イベントタイプ | SalesWings のイベント名 |
| ----------- | ----------- | ----------- |
| キャンバスイベント | エントリー | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| 顧客行動イベント | カスタムイベント | `[Custom Event tracked] $name` |
| 顧客行動イベント | 初回セッション | `[User Action] Today marks the user's first session` |
| 顧客行動イベント | 帰属をインストールする | `[User Action] User installed app from $source` |
| 顧客行動イベント | 購入イベント | `[Purchase] Customer purchased $product_id for $price $currency` |
| メッセージイベント | コンテンツカードのクリック | `[Content Card engagement] Clicked on $campaign_name content card` |
| メッセージイベント | メールバウンス | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| メッセージイベント | メールのクリック | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| メッセージイベント | メール配信 | `[Nurturing] Received email $campaign_name` |
| メッセージイベント | メール開封 | `[Email campaign engagement] Opened email $campaign_name` |
| メッセージイベント | メールの購読解除 | `[Subscription status change] Unsubscribed from $campaign_name` |
| メッセージイベント | アプリ内メッセージのクリック | `[In-app campaign engagement] Clicked on message $campaign_name` |
| メッセージイベント | プッシュオープン | `[Push notification engagement] Clicked on notification $campaign_name` |
| メッセージイベント | SMS/MMS インバウンド受信 | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| メッセージイベント | SMS/MMS 短縮リンクのクリック | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| メッセージイベント | WhatsApp インバウンド受信 | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| メッセージイベント | WhatsApp 読み取り | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| 購読 | グローバル購読のステータスの変更 | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| 購読 | 購読グループのステータスの変更 | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

次に、上の表の SalesWings イベント名に対して、SalesWings タグおよびスコアの [**カスタムイベント**] > [**イベント名**] および [**カスタムイベント**] > [**イベントプロパティ**] 条件を設定できます。条件に対して使用可能なイベントプロパティのリストは、よく使用されるエントリがあらかじめ入力されており、[[ルールエンジン設定ページ](https://helium.saleswings.pro/falcon)] の [**イベントプロパティ**] セクションでいつでも新しいものを追加できます。

![イベント名の条件例。]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

設定とトラブルシューティングの詳細については、[SalesWings サービスチーム](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs)に連絡して、オンボーディングサポートを受けてください。

