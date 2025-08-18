---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFitは、手動A/BテストをAIテストに置き換えます。ライフサイクルマーケターでは、OfferFitのAIテストを使用して、顧客ごとに1:1の最適な判断を行い、すべての変数を同時にテストし、マーケットの変化を検出して適応させます。"
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/) 手動A/B テストをAI テストに置き換えます。ライフサイクルマーケターでは、OfferFitのAIテストを使用して、顧客ごとに1:1の最適な判断を行い、すべての変数を同時にテストし、マーケットの変化を検出して適応させます。

_この統合は OfferFit によって管理されます。_

## 統合について

OfferFitとBrazeインテグレーションを使用すると、顧客データに基づいて、すべての顧客の正しいメッセージ、チャネル、タイミングを自動的に検出できます。ビジネス目標 (クロスセル、アップセル、再購入、リテンション、更新、紹介、ウィンバックなど) を使用して、既存の特定された顧客に合わせてキャンペーンを最適化できます。

## 前提条件

| 必要条件 | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfferFit使用許諾 | このパートナーシップを活用するには、有効な OfferFit ライセンスが必要です。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Braze REST API キー | 次の権限を持つBraze REST API キー。 {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>users.track</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.email.create</code></li><li><code>templates.email.update</code></li><li><code>templates.email.info</code></li><li><code>templates.email.list</code></li></ul>{:/} これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST API エンドポイント | [REST API エンドポイントURL][1]。エンドポイントはインスタンスの Braze URL に応じて異なります。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Braze REST API エンドポイント

OfferFitの使用許諾およびユースケースによって、使用するBraze REST API エンドポイントが決まります。以下に、使用できるさまざまなAPI エンドポイントを示します。

| Braze REST API エンドポイント | OfferFit使用量 |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | キャンペーンまたはキャンバスがターゲットとする顧客のリストを取得します。OfferFit は PII データを受け入れないため、`fields_to_export` 属性は、プラットフォームユーザーと合意したデータ属性のみを取得するために使用されます。 |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | 指定したSegmentの一部であるすべてのユーザーを取得します。OfferFit は PII データを一切受け入れないため、`fields_to_export` 属性は、プラットフォームユーザーと合意した非 PII フィールドのみを取得するために使用されます。 |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit では、このエンドポイントを使用して、メッセージングのパーソナライズに使用できるカスタムデータ属性でユーザープロファイルを更新できます。                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Braze で API キャンペーンをトリガーします。 |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | API-トリガー配信用に設定されたキャンペーンの送信をトリガーします。 |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Braze で設定されているすべてのキャンペーンとその関連メタデータの一覧を取得します。 |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | 指定したBraze キャンペーンの分析情報を取得します。 |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | 特定の Braze キャンペーンの詳細を取得します。 |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | API トリガー配信用に設定されたキャンバスの送信をトリガーします。 |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Braze で設定されたすべてのキャンバスとその関連メタデータの一覧を取得します。 |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | 特定のキャンバスの分析データを取得します。 |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | 特定のキャンバスの詳細を取得します。 |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Braze で設定されているすべてのSegmentとその関連メタデータの一覧を取得します。 |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Braze セグメントのサイズを取得します。 |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | 特定の Braze セグメントの詳細を取得します。 |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | 新しいBraze HTML メール テンプレートを作成します。 |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | 既存の Braze HTML メールテンプレートを更新します。 |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 特定の Braze HTML メールテンプレートの詳細を取得します。 |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Braze で設定されているすべてのBraze HTML メール テンプレートと`subject line` および`HTML content` の一覧を取得します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

[integrate OfferFit](#integration)を実行した後、次の手順を実行して実験処理を自動化できます。

1. 最大化する**成功指標** (収益、コンバージョン、ARPU、
または顧客データから測定できる KPIなど) を選択します。これは、人工知能で最大化しようとする測定基準OfferFitです。
2. テストする**dimensions**を選択します(オファー、件名、クリエイティブ、チャネル、時刻、曜日、頻度など)。
3. 各ディメンションで使用可能な**オプション**を選択します。たとえば、チャネルのディメンションとしてメール、SMS、およびプッシュを選択してから、頻度ディメンションとして毎日、週2回、毎週などを選択できます。

![of_use_case_example][2]


実験工程が自動化された後、OfferFitは、選択された達成基準を最大化することを目標として、顧客ごとに毎日の推奨事項の作成を開始します。 

OfferFit人工知能は、あらゆる顧客の相互アクションから学び、それらのインサイトを翌日の勧告にアプリするだろう。


| ユースケース | 目標 | 事前のアプローチ | OfferFit のアプローチ |
|----------|------|----------------|-------------------|
| **クロスセルまたはアップセル** | インターネットサブスクリプションからのユーザーあたりの平均収益 (ARPU) を最大化する。 | すべての顧客に対し次に最も高いティアプランを提供する年間キャンペーンを実行する。 | 顧客ごとに最適なメッセージ、送信時刻、割引、提案プランを経験的に特定し、リープフロッグオファーを受け入れやすい顧客や、アップグレードの際に割引やその他のインセンティブを必要とする顧客を把握する。 |
| **更新とリテンション** | 契約更新を確保し、契約期間と純現在価値 (NPV)の両方を最大化する。 | AB テストを手動で実施し、更新を確保するために大幅な割引を提示する。 | 自動化された実験を利用して、顧客ごとに最適な更新オファーを特定し、価格にそれほど敏感ではなく、更新に大幅な割引を必要としない顧客を特定する。 |
| **リピート購入** | 購入率と再購入率を最大化する。 | すべての顧客に対し、Web サイトアカウントの作成後に同じジャーニーが提供される (同じケイデンスでの同じメールシーケンスなど)。 | 実験を自動化して、それぞれの顧客に最適なメニューアイテムを見つけ、最も効果的な件名、送信時刻、およびコミュニケーションの頻度を確認する。 |
| **ウィンバック** | 以前にサブスクライブしていたユーザーに再度サブスクリプションを促すことで、再アクティベーションを増やす。 | 高度なA/Bテストとセグメンテーション。 | 自動化された実験を利用して、数千個の変数を一括でテストし、顧客ごとに最適なクリエイティブ、メッセージ、チャネル、ケイデンスを特定する。 |
| **紹介** | 既存の顧客からのビジネスクレジットカード紹介による新規アカウントの開設を最大化する。 | すべての顧客に対する固定のメールシーケンスと、顧客群に対する最適な送信時刻、ケイデンスなどを判断するための大規模な AB テスト。 | 特定の顧客に対して理想的なメール、クリエイティブ、送信時刻、クレジットカードを決定するための実験を自動化する。 |
| **リードナーチャリングとコンバージョン** | 増分収益を促進し、顧客ごとに適切な金額を支払う。 | Facebook などのプラットフォームでのプライバシーポリシーの変更に伴い、パーソナライズされた有料広告に対する以前のアプローチが最後に有効になります。 | 強固なファーストパーティデータを利用して、顧客セグメント、入札方法、入札レベル、クリエイティブに対する実験を自動的に行う。 |
| **ロイヤルティとエンゲージメント** | 顧客ロイヤルティプログラムの新規登録者による購入を最大化する。 | 顧客のアクションに対して一定の順序でメールが顧客に送信された。たとえば、ロイヤルティプログラムのすべての新規登録者が同じジャーニーを受け取った。 | 各顧客の購入と再購入を最大化するため、さまざまなメールオファー、クリエイティブ、送信時刻、および頻度で実験を行う。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## 統合

### ステップ1:Braze でターゲットオーディエンスを定義する

Braze で少なくとも1つのセグメントを作成して、ターゲットオーディエンスを定義します。このセグメントは、キャンペーンまたはキャンバスを適切なユーザーに送信するために使用されます。

### ステップ2:API によってトリガーされる Braze キャンペーンまたはキャンバスを設定し、キャンペーンアセット (HTML テンプレート、イメージなど) を作成する {#step-2}

1. Braze でキャンペーンまたはキャンバスを作成します。OfferFit はこのキャンペーンまたはキャンバスを使用して、定義したオーディエンスから1:1 パーソナライズされたアクティベーションイベントを適切なユーザーs に送信します。 
2. キャンペーンまたはキャンバスにBraze[コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)を含めないでください。これにより、OfferFit コントロールグループのみが有効になります。
3. 寸法に応じて、クリエイティブコンテンツの「リキッドタグ」を設定して、キャンペーンまたはキャンバスにOfferFitの推奨事項をダイナミックな入力できます。OfferFit は、Braze API を介して顧客固有のコンテンツをテンプレートの Liquid タグに渡します。

### ステップ 3:OfferFit ユースケース設定をアップデートして、Brazeアクティベーションイベントを調整します

OfferFitのネイティブアクティベーションインテグレーションをBraze で活用して、対象オーディエンスの1:1 パーソナライズされたの推奨を調整およびスケジュールできます。

## カスタマイズ

OfferFit は、Braze でのアクティベーションイベントのオーケストレーションの他に、データ統合機能を提供します。このデータ統合機能により、利用可能な API エンドポイントを介して顧客プロファイル (非PII) とエンゲージメントデータを Braze から取得できます。

## この統合を使う

OfferFitが設定されると、自動化された実験プラットフォームは、対象オーディエンスのユーザーごとに、自動的に1:1 パーソナライズされたアクティベーションイベントをBrazeに送信します。これらのアクティベーションイベントは、[ ステップ 2](#step-2) で設定したBraze キャンペーンs またはキャンバスを介してトリガーされます。

OfferFit では、Braze で利用可能な分析データに加えて包括的なレポートレイヤーを提供しています。このレイヤーにより、マーケターは自己学習 AI 機能により OfferFit で検出された顧客のインサイトを検討できるようになります。


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

