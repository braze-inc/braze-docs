---
nav_title: "OfferFit"
article_title:OfferFit
alias: /partners/offerfit/
description:「OfferFitは手作業のA/BテストをAIテストに置き換える。カスタマーライフサイクルのマーケターは、OfferFitのAIテストを使用して、顧客ごとに最適な1対1の意思決定を行い、すべての変数を同時にテストし、市場の変化を検知して適応する。"
page_type: partner
search_tag:OfferFit

---


# OfferFit

> [OfferFitは](https://www.offerfit.ai/)手作業のA/BテストをAIテストに置き換える。カスタマーライフサイクルのマーケティング担当者は、OfferFitのAIテストを使用して、顧客ごとに最適な1対1の意思決定を行い、すべての変数を同時にテストし、市場の変化を検出して適応する。

OfferFitとBrazeの統合により、顧客データに基づいて、すべての顧客に適切なメッセージ、チャネル、タイミングを自動的に発見することができる。クロスセル、アップセル、カスタマーリテンション、リテンション、リニューアル、リファーラル、ウィンバックなどのビジネスゴールを設定し、識別済みの既存顧客に対してキャンペーンを最適化することができる。

## 前提条件

| 必要条件 | 説明 |
|-------------|-------------|
| OfferFitライセンス | このパートナーシップを利用するには、有効なOfferFitライセンスが必要である。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー： {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST APIエンドポイント | [REST APIエンドポイントのURL][1]。エンドポイントはインスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

### Braze REST APIエンドポイント

お客様のOfferFitライセンスとユースケースによって、使用するBraze REST APIエンドポイントが決定される。以下は、使用する可能性のある様々なAPIエンドポイントである。

| Braze REST APIエンドポイント | OfferFitの使い方 |
|--------------|----------------|
| [ポスト /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | キャンペーンやキャンバスの対象となる顧客リストを取得する。OfferFitはいかなるPIIデータも受け付けないため、`fields_to_export` 属性は、プラットフォーム・ユーザーと合意したデータ属性のみを取得するために使用される。 |
| [ポスト /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | 特定のセグメンテーションに属するすべてのユーザーを取得する。OfferFitはいかなるPIIデータも受け付けないため、`fields_to_export` 属性は、プラットフォーム・ユーザーと合意した非PIIフィールドのみを取得するために使用される。 |
| [ポスト /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFitはこのエンドポイントを使用して、メッセージングのパーソナライゼーションに使用できるカスタムデータ属性でユーザープロファイルを更新できる。                                                                                                                                            |
| [ポスト /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | BrazeでAPIキャンペーンをトリガーする。 |
| [ポスト /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | APIトリガー配信に設定されているキャンペーンの送信をトリガーする。 |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Brazeに設定されているすべてのキャンペーンのリストと関連するメタデータを取得する。 |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | 特定のBrazeキャンペーンの分析データを取得する。 |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | 特定のBrazeキャンペーンの詳細を取得する。 |
| [ポスト /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | APIトリガー配信に設定されているキャンバスに対して、送信をトリガーする。 |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Brazeに設定されているすべてのCanvasのリストと関連するメタデータを取得する。 |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | 特定のキャンバスの分析データを取得する。 |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | 特定のキャンバスの詳細を取得する。 |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Brazeで設定されているすべてのセグメンテーションと関連するメタデータのリストを取得する。 |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Brazeセグメントのサイズを取得する。 |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | 特定のセグメンテーションの詳細を取得する。 |
| [ポスト /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | 新しいBraze HTMLメールテンプレートを作成する。 |
| [ポスト /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | 既存のBraze HTMLメールテンプレートを更新する。 |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定のBraze HTMLメールテンプレートの詳細を取得する。 |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Brazeに設定されているすべてのBraze HTMLメールテンプレートのリストとその`subject line` 、`HTML content` を取得する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

[OfferFitを統合した](#integration)後、次のようにして実験プロセスをオートメーション化することができる：

1. 収益、コンバージョン、ARPUなど、最大化する**成功指標を**選択する。
顧客データから測定できるKPI。これは、オファーフィットがAIを使って最大化しようとする指標である。
2. テストする**ディメンションを**選択する（例：オファー、件名、クリエイティブ、チャネル、時間、曜日、頻度など）。
3. 各寸法で利用可能な**オプションを**選択する。たとえば、チャネル次元でメール、SMS、プッシュを選択し、頻度次元で毎日、週2回、週1回を選択することができる。

![使用例][2]


実験プロセスが自動化された後、OfferFitは、選択された成功指標を最大化することを目標に、顧客ごとに毎日の提案を開始する。 

OfferFitのAIは、すべての顧客との対話から学習し、そのインサイトを翌日のレコメンデーションに適用する。


| ユースケース | ゴール | 事前のアプローチ | オファーフィットのアプローチ |
|----------|------|----------------|-------------------|
| **クロスセルまたはアップセル** | インターネットサブスクリプションによるユーザー一人当たりの平均収入（ARPU）を最大化する。 | すべての顧客に次の上位プランを提供するキャンペーンを毎年実施する。 | 顧客ごとに最適なメッセージ、送信時間、割引、プランを経験的に発見し、どの顧客がリープフロッグオファーの影響を受けやすいか、どの顧客がアップグレードに割引やその他のインセンティブを必要とするかを学習する。 |
| **更新とリテンション** | 契約更新を確保し、契約期間と正味現在価値（NPV）の両方を最大化する。 | 手動でABテストを行い、大幅な割引を提供して更新を確保する。 | 自動化された実験を使用して、顧客ごとに最適な更新オファーを見つけ、価格感応度が低く、更新に大幅な割引を必要としない顧客を識別する。 |
| **リピート購入** | 購入率と買戻し率を最大化する。 | Webサイトアカウント作成後、すべての顧客が同じカスタマージャーニーを受ける（同じケイデンスで同じメールシーケンスなど）。 | 各顧客に提供する最適なメニューや、最も効果的な件名、送信時間、連絡頻度を見つけるための実験をオートメーション化する。 |
| **ウィン・バック** | 過去のサブスクライバーに再購読を促すことで、再アクティベーションを高める。 | 洗練されたABテストとセグメンテーション。 | 自動化された実験を活用して、一度に何千もの変数をテストし、各個人に最適なクリエイティブ、メッセージ、チャネル、ケイデンスを発見する。 |
| **紹介** | 既存顧客からのビジネスカード紹介を通じて新規口座の開封を最大化する。 | 全顧客を対象とした固定メールシーケンスで、広範囲に及ぶABテストを実施し、顧客集団に最適な送信時間、送信間隔などを決定した。 | 理想的なメール、クリエイティブ、送信時間、特定の顧客に提供するカードを決定するための実験をオートメーション化する。 |
| **リード育成とコンバージョン** | 収益の増加を促進し、顧客ごとに適切な金額を支払う。 | フェイスブックやその他のプラットフォームでプライバシーポリシーが変更されるにつれ、パーソナライズされた有料広告に対する以前のアプローチが最後の効果を発揮するようになる。 | 強固なカスタマーファーストデータを活用し、顧客セグメンテーション、入札方法、入札レベル、クリエイティブの自動実験を行う。 |
| **ロイヤルティとエンゲージメント** | 顧客ロイヤルティプログラムへの新規登録者による購買を最大化する。 | 顧客は、彼らのアクションに応じて、決まった一連のメールを受け取った。例えば、ロイヤルティプログラムに新規登録した人は全員、同じ旅をする。 | カスタマーエクスペリエンスでは、各顧客の購入と再購入を最大化するために、オファー、クリエイティブ、送信時間、送信頻度などを自動的に変更できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}


## 統合

### ステップ1:Brazeでターゲット・オーディエンスを定義する

Brazeで少なくとも1つのセグメンテーションを作成し、ターゲットオーディエンスを定義する。このセグメンテーションは、キャンペーンやキャンバスを適切なユーザーに送信するために使用される。

### ステップ2:APIトリガーのBrazeキャンペーンまたはキャンバスを設定し、キャンペーンアセット（HTMLテンプレート、画像写真など）を作成する。 {#step-2}

1. Brazeでキャンペーンまたはキャンバスを作成する。OfferFitは、このキャンペーンまたはキャンバスを使用して、定義したオーディエンスの中から適切なユーザーに1:1のパーソナライズされたアクティベーションイベントを送信する。 
2. キャンペーンやキャンバスにBraze[コントロールグループを]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)含めないこと。これにより、オファーフィットのコントロールグループだけがアクティブになる。
3. ディメンションに応じて、クリエイティブコンテンツにLiquidタグを設定することで、キャンペーンやキャンバスにダイナミックなOfferFitレコメンデーションを入力することができる。OfferFitは、Braze APIを介して、顧客固有のコンテンツをテンプレート内のLiquidタグに渡す。

### ステップ3:Brazeのアクティベーションイベントをオーケストレーションするために、OfferFitのユースケース設定を更新する。

OfferFitとBrazeのネイティブアクティベーション統合を活用して、ターゲットオーディエンスに1:1のパーソナライズされたレコメンデーションをオーケストレーションし、スケジュールさせることができる。

## カスタマイズ

Brazeでのアクティベーションイベントのオーケストレーションに加えて、OfferFitは、利用可能なAPIエンドポイントを通じてBrazeから顧客プロファイル（非PII）およびエンゲージメントデータを取得できるデータ統合機能を提供する。

## この統合を使う

OfferFitが設定されると、自動化された実験プラットフォームが、ターゲットオーディエンスの各ユーザーに対して1:1のパーソナライズされたアクティベーションイベントを自動的にBrazeに送信する。これらのアクティベーションイベントは、[ステップ](#step-2)2で設定したBrazeキャンペーンまたはCanvasを通じてトリガーされる。

Brazeで利用可能な分析データに加え、OfferFitは包括的なレポートレイヤーを提供し、マーケターはOfferFitが自己学習AI機能によって発見した顧客インサイトを探索することができる。




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

