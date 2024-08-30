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

OfferFitとBrazeインテグレーションを使用すると、顧客データに基づいて、すべての顧客の正しいメッセージ、チャネル、タイミングを自動的に検出できます。クロスセル、アップセル、再購入、リテンション、更新、照会、ウィンバックなどの業務目標を使用して、キャンペーンs を既存の識別された顧客s に最適化できます。

## 前提条件

| 要件 | 説明 |
|-------------|-------------|
| OfferFit使用許諾 | この提携の事前タグeを受けるためには、積極的なOfferFit免許が必要である。 |
| Braze REST API キー | 次の権限を持つBraze REST API キー。 {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST原薬エンドポイント | [Your REST API エンドポイント URL][1].エンドポイントは、インスタンスのBraze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**デベロッパコンソール**> **API設定**でAPI キーを作成できます。
{% endalert %}

### Braze REST原薬エンドポイント

OfferFitの使用許諾およびユースケースによって、使用するBraze REST API エンドポイントが決まります。以下に、使用できるさまざまなAPI エンドポイントを示します。

| Braze REST原薬エンドポイント | OfferFit使用量 |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | キャンペーンまたはキャンバスがターゲットとする顧客の一覧を取得します。OfferFit はPII データを一切受け付けないため、`fields_to_export` 属性は、プラットフォーム ユーザーと一致するデータ属性のみを取得するために使用されます。 |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | 指定したSegmentの一部であるすべてのユーザーを取得します。OfferFit はPII データを一切受け付けないため、`fields_to_export` 属性は、プラットフォーム ユーザーと一致する非PII フィールドs のみを取得するために使用されます。 |
| [POST/ユーザー/トラック]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit は、このエンドポイントを使用して、メッセージングをパーソナライズするために使用できるカスタムデータ属性s でs を更新 ユーザープロファイルできます。                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Braze でのAPI キャンペーンのトリガ。 |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | API-トリガー配信用に設定されたキャンペーンの送信をトリガーします。 |
| [GET/キャンペーン/リスト]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Braze で設定されているすべてのキャンペーンとその関連メタデータの一覧を取得します。 |
| [GET /キャンペーンs/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | 指定したBraze キャンペーンの分析情報を取得します。 |
| [GET/キャンペーン/詳細]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Braze キャンペーンの内容を取得します。 |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | API-トリガー配信用に設定されたキャンバスの送信をトリガーします。 |
| [GET/キャンバス/リスト]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Braze で設定されたすべてのキャンバスとその関連メタデータの一覧を取得します。 |
| [GET /キャンバス/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | 指定したキャンバスの分析情報を取得します。 |
| [GET/キャンバス/詳細]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | 特定のキャンバスの詳細を取得します。 |
| [GET/Segment/リスト]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Braze で設定されているすべてのSegmentとその関連メタデータの一覧を取得します。 |
| [GET /Segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Braze Segmentの大きさを取得します。 |
| [GET/Segment/詳細]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Braze Segmentの内容を取得します。 |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | 新しいBraze HTML メール テンプレートを作成します。 |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Braze HTML メール テンプレートをアップデートします。 |
| [取得/templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Braze HTML メール テンプレートの内容を取得します。 |
| [取得/templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Braze で設定されているすべてのBraze HTML メール テンプレートと`subject line` および`HTML content` の一覧を取得します。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

[integrate OfferFit](#integration)を実行した後、次の手順を実行して実験処理を自動化できます。

1. 収益、コンバージョン s、ARPU など、最大化する**success metric** を選択します
顧客データから測定できます。これは、人工知能で最大化しようとする測定基準OfferFitです。
2. テストする**dimensions**を選択します(オファー、件名、クリエイティブ、チャネル、時刻、曜日、頻度など)。
3. 各ディメンションで使用可能な**オプション**を選択します。たとえば、チャネルディメンションにメール、SMS、およびpush を選択し、度数ディメンションに日単位、週単位、および週単位を選択できます。

![of_use_case_example][2]


実験工程が自動化された後、OfferFitは、選択された達成基準を最大化することを目標として、顧客ごとに毎日の推奨事項の作成を開始します。 

OfferFit人工知能は、あらゆる顧客の相互アクションから学び、それらのインサイトを翌日の勧告にアプリするだろう。


| ユースケース | 目標 | 事前のアプローチ | OfferFit手法 |
|----------|------|----------------|-------------------|
| **クロスセルまたはアップセル** | ネットサブスクリプションからの1ユーザー当たり収益最大化 | 年間キャンペーンを実行すると、すべての顧客に次の最上位層プランが提供されます。 | 経験的に、それぞれの顧客に最適なメッセージ、送信時間、割引を発見し、提供する予定がある。どの顧客が飛躍的なオファーを受けやすく、どの顧客がアップグレードに割引や他の奨励金を必要とするかを学ぶ。 |
| **リニューアル&アンプ;リテンション** | 契約更新を確保し、契約期間と純現在価値(NPV)の両方を最大化する。 | A/Bは手動でテストし、更新を確保するためにかなりの割引を提供します。 | 自動化された実験を利用して、顧客ごとに最高のリニューアルオファーを見つけ、価格感応度が低く、リニューアルにあまり割引を必要としない顧客を特定する。 |
| **リピート購入** | 購入・買戻し率を最大化する。 | すべての顧客は、Web サイトアカウント(同じケイデンスの同じメール順序など)を作成した後、同じジャーニーを受け取ります。 | 実験を自動化して、それぞれの顧客に最適なメニューアイテムを見つけ、最も効果的な件名、送信時間、および通信頻度を確認します。 |
| **ウィンバック** | 過去のサブスクライバーに再申請を促すことで、再活性化を高める。 | 高度なA/Bテストとセグメンテーション。 | 自動化された実験を活用して、一度に何千もの変量をテストし、一人ひとりに最適な創造力、伝言、チャネル、ケイデンスを発見する。 |
| **紹介** | 既設顧客からの営業信用カード照会による新規口座開封の最大化 | すべての顧客 s のメール順序を固定し、顧客集団に最適な送信時間、ケイデンスなどを決定するための広範なA/B テストを行います。 | アイデア l メール、クリエイティブ、送信時刻、信用カードを決定するための実験を自動化し、具体的な顧客を提供します。 |
| **リード・ナチュアリング&アンプ;コンバージョン** | 増分収益を推進し、顧客ごとに適切な金額を支払う。 | Fac eBookなどのプラットフォームでプライバシーポリシーが変更されると、以前のアプリがパーソナライズされたの有料広告に侵入するのが最後に有効になります。 | ロバストな第一者データを活用して、顧客 Segmentの試乗、入札方法、入札水準、クリエイティブを自動的に試す。 |
| **ロイヤリティ&アンプ、エンゲージメント** | 顧客 ロイヤルティプログラムへの新規加入者による購買を最大化する。 | 顧客は、アクションsに応じて、一定のメールsを受け取った。たとえば、ロイヤルティプログラム内のすべての新規登録者は同じジャーニーを受け取ります。 | さまざまなメールの提供、クリエイティブ、送信時間、頻度を自動的に試し、それぞれの顧客の購買と再購入を最大化します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}


## 統合

### ステップ1:Braze での対象オーディエンスの定義

Braze で少なくとも1 つのSegmentを作成して、対象オーディエンスを定義します。このSegmentは、キャンペーンまたはキャンバスを正しいユーザーs に送信するために使用されます。

### ステップ2:API-トリガーのBraze キャンペーンまたはキャンバスを設定し、キャンペーンアセットを作成する(たとえば、HTML テンプレート s、"画像 s) {#step-2}

1. Braze でキャンペーンまたはキャンバスを作成します。OfferFit はこのキャンペーンまたはキャンバスを使用して、定義したオーディエンスから1:1 パーソナライズされたアクティベーションイベントを適切なユーザーs に送信します。 
2. キャンペーンまたはキャンバスにBraze[コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)を含めないでください。これにより、OfferFit コントロールグループのみが有効になります。
3. 寸法に応じて、クリエイティブコンテンツの「リキッドタグ」を設定して、キャンペーンまたはキャンバスにOfferFitの推奨事項をダイナミックな入力できます。OfferFit は、Braze API を介してテンプレートs のリキッドタグs に顧客固有のコンテンツを渡します。

### ステップ3:OfferFit ユースケース設定をアップデートして、Brazeアクティベーションイベントを調整します

OfferFitのネイティブアクティベーションインテグレーションをBraze で活用して、対象オーディエンスの1:1 パーソナライズされたの推奨を調整およびスケジュールできます。

## カスタマイズ

Braze でのアクティベーションイベントの編成に加えて、OfferFit では、Brazeから顧客 プロファイル(非PII)およびエンゲージメントデータを取得するためのデータインテグレーション機能を、使用可能なAPI エンドポイントで提供しています。

## この統合の使用

OfferFitが設定されると、自動化された実験プラットフォームは、対象オーディエンスのユーザーごとに、自動的に1:1 パーソナライズされたアクティベーションイベントをBrazeに送信します。これらのアクティベーションイベントは、[ ステップ 2](#step-2) で設定したBraze キャンペーンs またはキャンバスを介してトリガーされます。

Braze で使用可能な分析情報に加えて、OfferFit は、自己学習AI 機能を使用してOfferFit が検出した顧客 インサイトをマーケター s が探索できるようにする包括的なレポートリングレイヤーを提供します。




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

