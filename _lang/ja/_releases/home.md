---
nav_title: ホーム
article_title: Brazeの新機能
description: "Braze リリースノートは毎月発行されるため、主要な製品リリース、継続的な製品改良、Braze提携、SDK変更の破棄、および機能の非推奨については最新の状態を維持できます。"
page_order: 0
search_rank: 1
page_type: reference

---

# Brazeの新機能

{% alert tip %}
このページに記載されている更新の詳細については、アカウントマネージャーにお問い合わせいただくか、サポートチケット を開封して[ までご連絡ください。また、[ SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) では、毎月のSDKのリリース、改良、および変更の更新に関する詳細を確認することもできます。
{% endalert %}

{% details November 11, 2025 %}

## 2021年11月

### データの柔軟性

#### `Live Activities Push to Start Registered for App` セグメンテーション フィルター

`Live Activities Push to Start Registered for App` フィルター Segmentは、指定したアプリのiOS プッシュ通知 s を介してLive Activity を起動するように登録されているかどうかによって、ユーザーs を起動します。

#### RFM SQLセグメント拡張

[RFM (recency, frequency, monetary) Segment Extension]({{site.baseurl}}/rfm_segments/) を作成して、購買習慣を測定することで最良のユーザーs を目標にすることができます。

RFM 解析は、カテゴリ(最新、度数、金額)ごとに0 ～3 のスケールでユーザーs をスコア化することによって、最良のユーザーs を識別するマーケティング手法です。ここで、3 が最良のスコアで、0 が最悪のスコアです。最近度、度数、金額はすべて、選択した特定の時間範囲のデータに基づいています。

#### ユーザ定義属性- 数値 

使用状況レポートを表示しているときに、[**Values**タブ]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab)を選択して、選択したカスタム属性sの最上位値をアプリの標本に基づいて、約250,000 ユーザー s 単位で表示します。

#### クラウドデータ取り込みのログとオブザーバビリティの同期

{% multi_lang_include release_type.md release="General availability" %}

クラウドデータ取り込み(CDI) [同期ログダッシュボード]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) では、CDI によって処理されたすべてのデータを監視し、データが正常に同期されたかどうかを確認し、「不正」または欠落データの問題を診断することができます。

#### マルチルールフィーチャーフラグ展開

[マルチルールフィーチャーフラグのロールアウト]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts)を使用して、ユーザーsを評価するための一連のルールを定義します。これにより、正確なセグメンテーションとコントロール主導機能のリリースが可能になります。このメソッドは、同じ機能を多様なオーディエンスs にデプロイする場合にアイデアです。

#### ドラッグアンドドロップ製品ブロックのカタログ フィールドs へのムーディング

カタログ 設定 s で、**Product ブロック s** を[ に切り替えて、特定のフィールドs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) とカタログの情報にマップできます。これにより、プロダクトタイトル、プロダクトURL、"画像 URL として使用するフィールドを選択できます。

#### Currentsでの頻度キャップ中断イベント

Currents を使用すると、チャネルのアボートイベントで`abort_type` を参照できるようになりました。これは、メッセージがフリークエンシーキャップのためにアボートされたことを示し、どのフリークエンシーキャップ規則がアボートの原因になったかを含みます。これは、フリークエンシーキャップ規則の設定方法を知らせるのに役立ちます。具体的なCurrents内容については、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)を参照してください。

### 強力なチャネル

#### 背景行"画像s 

{% multi_lang_include release_type.md release="General availability" %}

[バックグラウンド行"画像]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image)を**行プロパティー**パネルのアプリ内メッセージまたはランディングページに追加できます。**背景"画像**を切り替え、"画像 URLを入力するか、[メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)から"画像を選択します。最後に、すべてのテキスト、サイズ、位置、および"画像を繰り返して行全体にパターンを作成するかどうかを設定します。

![水平リピートパターンを持つピザの行バックグラウンド "画像。]({% image_buster /assets/img_archive/background_row.png %})

#### プレビューリンクをコピー

**コピープレビューリンク**を[バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#step-6-test-your-message-optional)、[メール カスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer)、および[メール opt-in と配信停止 pages]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) で使用して、任意のユーザーの内容がどのように見えるかを示す共有可能なリンクを生成します。

#### 配信を最適化した WhatsApp メッセージ

メタ社の高度なAIシステムを使用して、マーケティングメッセージを、最もエンゲージする可能性の高いユーザーに配信し、配信能力とメッセージエンゲージメントを大幅に向上させます。

[ 配信が最適化されたWhatsAppメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) は、Meta の新しい[ Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) を使用して送信され、従来のクラウドAPI と比較して優れたパフォーマンスを提供します。この新しい送信パイプラインは、誰が価値を持ち、あなたのメッセージを受け取りたいかをよりよくユーザーに伝えるのに役立ちます。

#### WhatsApp Flows

WhatsAppフローメッセージをBrazeキャンバスまたはキャンペーンに組み込む場合、ユーザーがフローを通じて送信する具体的な情報をキャプチャして活用することができます。Braze は、必要な階層化カスタム属性 (NCA) スキーマを生成するために、ユーザーレスポンスの構造、特にJSON レスポンスの予想される形状に関する追加情報を受け取る必要があります。

これで、[フローレスポンスをカスタム属性]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute)として保存し、テスト送信を完了することで、レスポンス構造に関する情報をBrazeに与えることができます。

#### 編集可能ユーザー プレビュー

[ランダムまたは既存のユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user)から個々のフィールドsを編集して、メッセージ内のダイナミックな内容を調べることができます。**編集**を選択して、選択したユーザーを変更可能なカスタムユーザーに変換します。

!["Preview as a User" tab with "Edit" ボタン。]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AI と ML のオートメーション

#### Brazeエージェントの新機能

{% multi_lang_include release_type.md release="Beta" %}

[ Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) をカスタマイズできるようになりました。

- エージェントの応答に従うための[ブランドガイドライン]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)の適用。 
- カタログを参照して、メールをさらにパーソナライズする。
- [出力形式]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)を指定して、エージェントの出力を構造化する。
- エージェントのアウトプットの偏差の度合いを[temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature)でAdjustします。

### BrazeAI<sup>TM</sup>演算子を持つChatGPTモデル

{% multi_lang_include release_type.md release="Beta" %}

これらのGPT モデルから、[Operator]({{site.baseurl}}/user_guide/brazeai/operator) でさまざまなリクエストタイプに使用するように選択できます。

- GPT-5 Nano
- GPT-5 ミニ(デフォルト)
- GPT-5

### 新しいBrazeのパートナーシップ

#### StackAdapt - 広告

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) は、ターゲットを絞ったパフォーマンス主導の広告を配信するAI 駆動のマーケティング プラットフォームです。これにより、Braze からStackAdapt Data Hub にユーザープロファイルデータを同期できます。2 つのプラットフォームs を接続することで、顧客s の統一されたビューを作成し、ファーストパーティデータを有効化して広告パフォーマンスを向上させることができます。

#### クラウド- 動的コンテンツ

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) は、"画像の管理、エディット、最適化、および動画を、チャネル s およびカスタマージャーニー s のすべてのキャンペーンに大規模に提供するための"画像および動画 プラットフォームです。統合して有効にすると、Cloudinary のメディアマネジメントは、Braze キャンペーンおよびキャンバスにダイナミックな、文脈に応じた or 状況に即した、およびパーソナライズされたのアセット配信を提供します。

#### カメレオン-A/B試験

[Kameleoon]({{site.baseurl}}/partners/kameleoon/)は、1つの統一プラットフォームにおいて、実験、AIパワードパーソナライゼーション、および機能マネジメント機能を備えた最適化ソリューションです。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - `subscribeToInAppMessage`のコールバックに対するTypescript型、`Braze.Events.IN_APP_MESSAGE_RECEIVED`に対する`addListener`を修正しました。
        - これらのリスナーは、新しい`InAppMessageEvent` 型のコールバックを適切に返すようになりました。以前は、`BrazeInAppMessage` 型を返すようにメソッドに注釈が付けられていましたが、実際には`String` を返していました。
         - どちらかのサブスクリプション API を使用している場合は、このバージョンに更新した後もアプリ内メッセージの振る舞いが変更されていないことを確認してください。`BrazeProject.tsx` のサンプルコードを参照してください。
    - API `logInAppMessageClicked`、`logInAppMessageImpression`、および`logInAppMessageButtonClicked` は、現在の公開インターフェイスに合わせて`BrazeInAppMessage` オブジェクトのみを受け入れるようになりました。
        - これまでは、`BrazeInAppMessage` オブジェクトと`String` の両方を受け入れていました。
    - `BrazeInAppMessage.toString()` JSON文字列表現の代わりに、人間が読み取れる文字列を返すようになりました。
        - アプリ内メッセージのJSON ストリング表現を取得するには、`BrazeInAppMessage.inAppMessageJsonString` を使用します。
    - iOS では、`[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` が`[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]` に移動されました。
        - この新しいメソッドは、インスタンス・メソッドではなくクラス・メソッドになりました。
    - `BrazeReactUtils` メソッドにnullability アノテーションを追加します。
    - 以下の非推奨のメソッドおよびプロパティをAPI から削除します。
        - `getInstallTrackingId(callback:)` `getDeviceId` が優先されます。
        - `registerAndroidPushToken(token:)` `registerPushToken` が優先されます。
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` `setAdTrackingEnabled` が優先されます。
        - `PushNotificationEvent.push_event_type` `payload_type` が優先されます。
        - `PushNotificationEvent.deeplink` `url` が優先されます。
        - `PushNotificationEvent.content_text` `body` が優先されます。
        - `PushNotificationEvent.raw_android_push_data` `android` が優先されます。
        - `PushNotificationEvent.kvp_data` `braze_properties` が優先されます。
    - ネイティブAndroid SDK バージョンバインディング[ をBraze Android SDK 39.0.0 から40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新します。
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOS バインドを[Braze Swift SDK 9.0.0 から10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。これには、Xコード 26 サポートが含まれます。
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブAndroidブリッジを[Braze Android SDK 33.0.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## 2024年10月15日リリース

### BrazeAI Decisioning Studio™

[ BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) は、A/B テストを、あらゆるものをパーソナライズし、クリックではなく、どんなメトリックでも最大化するAI 決定に置き換えます。BrazeAI Decisioning Studio™を使用すると、任意の業務用KPIを最適化できます。標本ユースケースと主な機能については、当社の専用の項[ BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)を参照してください。

### データの柔軟性

#### Currents の新しいイベント

これらの新しいイベントは、[Currents用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に追加されました。

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

これらの新しいフィールドは、次のCurrentsに追加されました。

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id` 
  - `users.messages.whatsapp.InboundReceive`
- `message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### 抑制リスト

{% multi_lang_include release_type.md release="General availability" %}

[除外リスト]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)は、自動的にキャンペーンsやキャンバスを受信しないユーザーsのグループです。除外リストはSegment フィルターs で定義され、ユーザーs はフィルター基準を満たすときに除外リストに入り、終了します。

#### ゼロコピーのカスタマイズ

{% multi_lang_include release_type.md release="Early access" %}

[ゼロコピーパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)のクラウドデータ取り込みを使用してキャンバストリガーを同期します。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、それを送信先キャンバスに渡します。キャンバスステップs には、オプションで、Braze ユーザープロファイルs に保持されていないパーソナライゼーション フィールドs を含めることができます。

#### オーディエンスパスとディシジョン分割ステップのキャンバスコンテキスト変数

{% multi_lang_include release_type.md release="Early access" %}

[create context variable フィルター s]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-filters) は、[Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) および[Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) ステップ s で事前に宣言されたコンテキスト変数を使用できます。

### 創造性を引き出す

#### メール用ディールカード

[Deal Cards]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab)を使用して、メール本体の上部に直接的にキーディール情報を提供します。これにより、受信者 s はオファーの詳細をすばやく理解し、アクションを負うことができます。

#### バナーのテンプレート

[ バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns) を作成すると、空白のテンプレートから始めたり、Braze テンプレートを使用したり、保存済みのバナーテンプレートを選択したりできます。

### 強力なチャネル

#### 抑制リスト

{% multi_lang_include release_type.md release="General availability" %}
 
[除外リスト]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/)は、メッセージを受信しないユーザーグループを指定します。管理者は、セグメントフィルターを使用して除外リストを作成し、ユーザーグループをセグメンテーションと同じように絞り込むことができます。

#### LINE クリックトラッキング

{% multi_lang_include release_type.md release="General availability" %}

[LINEクリック"トラッキング]({{site.baseurl}}/line/click_tracking/)が有効になっている場合、Brazeは自動的にURLを短縮し、"トラッキングメカニズムを追加し、クリックをリアルタイムで記録します。LINEでは、集約クリックデータが提供されますが、Brazeでは、タイムリーでアクションに利用できる詳細なユーザー情報が提供されます。このデータにより、クリックビヘイビアに基づくユーザーのSegmentや、クリックに応じたメッセージのトリガーなど、よりターゲットを絞ったセグメンテーションおよびリターゲティングストラテジを作成できます。

#### SMS/RCSボットクリックフィルター中

{% multi_lang_include release_type.md release="General availability" %}

[SMSおよびRCSボットクリックフィルター ing]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/)は、ボットクリックの疑いを除外することでキャンペーン 分析とワークフローを強化します。「ボットクリック」とは、ウェブクローラ、AndroidおよびiOSリンクプレビューs、またはCPaSセキュリティソフトウェアからのものなど、SMSおよびRCSメッセージの短縮されたリンクを自動クリックすることを意味する。この機能により、AC キュレート レポート のing、セグメンテーション、およびオーケストレーションが実際のユーザーs に関与しやすくなります。

#### 通信WhatsAppの電話番号

WhatsAppの法人取引先(WABA)の電話番号とそれに関連付けられたサブスクリプショングループ[を、Braze内のあるワークスペースから別の]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/)に移動します。

#### WhatsAppフローレスポンスメッセージとプレビュー

キャンバスでは、[レスポンスメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses)とフローメッセージを使用するWhatsAppメッセージステップを作成できます。また、** プレビュー Flow** を選択して、Braze でFlow を直接的にプレビューし、期待どおりに動作することを確認することもできます。

#### WhatsApp 製品メッセージ

製品メッセージを使用すると、Meta カタログから直接製品を表示するインタラクティブな WhatsApp メッセージを送信できます。

#### BrazeとWhatsAppを外部と統合

[AIチャットボットとライブエージェントハンドオフ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/)の力をWhatsApp チャネルに活用して、顧客支援業務を合理化しましょう。日常的な問い合わせを自動化し、必要に応じて人への移行をシームレスにすることで、応答時間を大幅に改善し、総合的なカスタマーエクスペリエンスを向上させることができます。

### AI と ML のオートメーション

#### Braze エージェント

{% multi_lang_include release_type.md release="Beta" %}

[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) は、Braze 内で作成できるAI パワーのヘルパーです。エージェントは、コンテンツを生成し、インテリジェントな決定を行い、より多くのパーソナライズされた カスタマーエクスペリエンスを配信できるようにデータを拡張できます。

### 新しいBrazeのパートナーシップ

#### Jasper - テンプレート

Braze との[Jasper]({{site.baseurl}}/partners/jasper/) の統合により、コンテンツ作成とキャンペーン実行を効率化できます。ジャスパーでは、マーケティングチームが高品質でオンブランドのコピーを数分で作成できます。そして、Brazeは、これらの情報を最適な時期に適切なオーディエンスに配信することを容易にする。この統合により、シームレスなワークフローが促進され、手作業の労力が削減され、より強力なエンゲージメント成果がもたらされます。

#### スウィム-ロイヤルティとリターゲティング

[Swym]({{site.baseurl}}/partners/swym/)は、eCommerceブランドがWishlists、Save for Later、Gift Registry、Back-in-Stockアラートでショッピングインテントを獲得するのに役立ちます。豊富な権限ベースのデータを使用して、ハイパーターゲットのキャンペーンを作成し、エンゲージメントを促進し、コンバージョンを向上させ、ロイヤルティを向上させるパーソナライズされたなショッピングエクスペリエンスを提供できます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。ブレーク更新s を以下に示します。対応するSDK変更ログを確認することで、他のすべての更新s を検索できます。

- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジを[Braze Android SDK 32.1.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - 最小限必要なGradlePluginKotlinVersion は2.1.0 です。
    - ネイティブiOSブリッジを[Braze Swift SDK 10.3.0から11.9.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。これには、Xコード 26 サポートが含まれます。
    - ニュースフィードのサポートを削除します。以下のAPI が削除されました。
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 15.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - ネイティブAndroid SDK バージョンバインディング[ をBraze Android SDK 37.0.0 から39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新します。
    - ニュースフィードのサポートを削除します。以下のAPI が削除されました。
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 3.11.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOSブリッジを[Braze Swift SDK 10.3.0から11.9.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。これには、Xコード 26 サポートが含まれます。

{% enddetails %}
{% details September 16, 2025 %}

## 2024年9月17日リリース

### データの柔軟性

#### Braze データプラットフォーム

Brazeデータプラットフォームは、包括的で構成可能な一連のデータ機能とパートナー連携で、カスタマーライフサイクル全体でパーソナライズされたでインパクトのあるエクスペリエンスを作成できます。実行する3 つのデータ関連ジョブについて詳しくは、以下を参照してください。 

- [データ統合]({{site.baseurl}}/user_guide/data/unification)
- データの有効化
- [データ配信]({{site.baseurl}}/user_guide/data/distribution)

#### ユーザープロファイルの削除

{% multi_lang_include release_type.md release="Early access" %}

これで、個々のユーザー s またはユーザー s のSegmentをBraze ダッシュボードを介して直接的に削除できるようになりました。Braze REST API のみに依存するのではありません。 早めのアクセスに参加したい場合は、顧客のサクセスマネージャーに連絡する必要があります。開始するには、[ユーザーの削除s]({{site.baseurl}}/user_guide/data/unification/user_data/delete_users/)を参照してください。

#### カスタムバナープロパティ

{% multi_lang_include release_type.md release="Early access" %}

バナーキャンペーンからカスタムプロパティを使用して、SDKからキーと値のデータを取得し、アプリの動作やアプリの認識を変更できます。詳細については、[カスタムバナープロパティ]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties)を参照してください。

#### トークン認証

{% multi_lang_include release_type.md release="General availability" %}

Braze コネクテッドコンテンツを使用する場合、特定の API では、ユーザー名とパスワードの代わりにトークンが必要になることがあります。Brazeは、[トークン 認証 ヘッダー値]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication)を保持する認証情報sを格納できます。

#### プロモーションコード

プロモーションコードをユーザーのプロファイルに保存するには、ユーザーアップデートステップを使用します。詳細については、[プロモーションコードsをユーザープロファイルs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile)に保存するを参照してください。

### 創造性を引き出す

#### Braze操縦士

[ Braze パイロット]({{site.baseurl}}/user_guide/getting_started/braze_pilot) は、Android およびiOS で一般に利用可能なアプリで、Braze ダッシュボードからスマートフォンにメッセージを起動できます。[Braze パイロット]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) の使用開始を確認し、アプリの概要、Braze ダッシュボードへの接続の初期化、および設定の完了を確認します。

### 新しいBrazeのパートナーシップ

#### Blings - ビジュアルコンテンツとインタラクティブコンテンツ

[Blings]({{site.baseurl}}/partners/blings/) は、リアルタイム、対話型、およびデータドリブン型の 動画の体験を、スケールでチャネル s 間で配信できる次世代パーソナライズされた 動画 プラットフォームです。

#### サードパーティ製工具とのShopifyスタンダード統合

Shopifyのオンラインストアでは、Braze のスタンダードインテグレーションメソッドを使用して、サイトのBraze SDKを支援することをお勧めします。

ただし、Google Tag Manager などのサードパーティツールを使用することをお勧めすると理解していますので、どのようにすればよいかについてのガイドをまとめました。開始するには、[Shopifyを参照してください。サードパーティのタグ ging]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/)。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Braze Flutter SDK 15.0.](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Braze Android SDK`36.0.0` から`39.0.0` にネイティブAndroid ブリッジを更新します。
    - Braze Swift SDK `12.0.0` から`13.2.0` にネイティブiOS ブリッジをアップデートします。これには、Xコード 26 サポートが含まれます。

- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - `13.0.0+` SemVer 仕様のリリースを必要とするように Braze Swift SDK バインディングを更新します。これにより、Braze SDK の`13.0.0`から`14.0.0`までのあらゆるバージョンとの互換性が確保されます (11.0.0は含まれません)。

{% enddetails %}
{% details August 19, 2025 %}

## 2024年8月20日リリース

### Canvas コンテキストへのタイムゾーン整合性の標準化

{% multi_lang_include release_type.md release="Early access" %}

[Canvas Context ステップ early access]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) に参加している場合、アクション ベースのCanvases のトリガーイベントプロパティーの日時型を持つすべてのタイムスタンプは、必ず[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) に正規化されます。詳細については、[タイムゾーン整合性標準化]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization)を参照してください。

### データの柔軟性

#### セルフサービスカスタムドメイン

{% multi_lang_include release_type.md release="General access" %}

[セルフサーブカスタムドメイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) は、SMS、RCS、およびWhatsApp用の独自のカスタムドメインをBraze ダッシュボードから直接設定および管理する権限を与えます。1 か所で最大10 個のカスタムドメインを簡単に追加、監視、管理できます。

#### セグメントファンネル統計

[ファネル統計の表示]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics)を選択して、そのフィルターグループの統計を表示し、追加されたフィルターがSegment統計にどのように影響するかを確認します。その時点までのすべてのフィルターs によってターゲットされているユーザーs の推定数とパーセンテージe が表示されます。フィルターグループの統計が表示されると、フィルターs を変更するたびに自動的に更新されます。 

#### プッシュ通知sの`/campaigns/details`エンドポイントに対する新しいレスポンスフィールドs

プッシュ通知s の`messages` レスポンスに2 つの新しいフィールドs が含まれるようになりました。

- `image_url`:"画像は、Android 通知 "画像、iOS 通知 "画像、またはWeb プッシュのアイコン"画像です。
- `large_image_url`:Android Chrome およびWindows Web プッシュ アクション s のWeb 通知 "画像。

#### PIIフィールドの定義

選択および[特定のフィールドをPIIフィールドとして定義するs]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii)は、ユーザがBraze ダッシュボードで表示できるものにのみ影響し、そのようなPIIフィールドのエンドユーザデータの処理方法には影響しません。

ダッシュボードの設定を、[データリテンション]({{site.baseurl}}/api/data_retention/)に関連するものを含め、御社に許諾可能なあらゆるプライバシー規則およびポリシーアプリと整合させるために、法務部にご相談ください。

#### レポートビルダを読み込むで共有する

[ ** Share** を選択し、** リンクを共有する** または** メール** を送信またはスケジュールすることで、レポートへのダッシュボードリンク]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) を共有できます。

### 創造性を引き出す

#### ドラッグアンドドロップメール用のカスタムヘッドタグs

`<head>` タグ s を使用して、CSSとメタデータをメールに追加します。たとえば、これらのタグs を使用してスタイルシートまたはファビコンを追加できます。リキッドは、`<head>` タグ s でサポートされます。

### 強力なチャネル

#### ファジィ・アウト・ベストプラクティス

私たちは[ベストプラクティスセクション]({{site.baseurl}})を追加しました。これは、あなたのファジィオプトアウトメッセージを思慮深く設定し、あなたのサブスクライバーsのために明確で、準拠し、肯定的な体験を作るのに役立ちます。

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[ WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) は、既存のWhatsApp チャネルの拡張機能であり、インタラクティブでダイナミックな メッセージングなエクスペリエンスを作成できます。 

#### WhatsAppのインバウンド商品の問題

ユーザは、[製品質問]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions)で製品またはカタログのメッセージに応答できます。これらは受信メッセージとして到着し、アクションパスでソートできます。

さらに、Brazeはこれらの質問から製品IDとカタログ IDを抽出します。そのため、回答を自動化したり、他のチーム(顧客サポートなど)に質問を送信したりする場合は、それらの詳細を含めることができます。

### AI と ML のオートメーション

#### 新しいBrazeAI™ユースケースアーティクル

BrazeAI™を最大限に活用するために、新しいユースケースアーティクルを追加しました。これらのガイドでは、ly AI をエンゲージメントストラテジにアプリするための実用的な方法を示します。

- 解約予測撹拌の危険がある顧客を特定し、アクションを早めに服用する。
- 予測イベント重要なユーザー アクションを予測し、リアルタイムで体験を形成する。
- [レコメンデーション]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ):顧客行動に基づき、より関連性の高い内容・商品をお届けします。

#### MCPサーバ

{% multi_lang_include release_type.md release="Beta" %}

セキュアで読み取り専用のコネクションである[ Braze MCP サーバ]({{site.baseurl}}/user_guide/brazeai/mcp_server/) は、Claude やCursor などのAI ツールが非PII Brazeデータにアクセスして、疑問に答え、傾向を分析し、データを変更せずにインサイトを提供します。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` の機能を拡張し、" Optional" 認証 エラー s でトリガー化します。
        - デリゲートメソッド`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` は、"Required"および"Optional" 認証 エラー s の両方でトリガーされます。
        - "Required" SDK 認証 エラー s のみを処理する場合は、このデリゲートメソッドのインプリメンテーション内で`BrazeSDKAuthError.optional` がfalse であることを確認する確認を追加します。
    - `Braze.Configuration.sdkAuthentication` の使用を有効にしたときに有効になるように修正しました。
        - 以前は、この構成の価値はSDKによって消費されず、トークンが存在する場合は必ずリクエストにアタッチされていました。
        - これで、SDKは、この設定が有効になっている場合にのみ、SDK 認証 トークンを送信ネットワークリクエストにアタッチします。
    - `Braze.FeatureFlag` のすべてのプロパティと`Braze.Banner` のすべてのプロパティの設定は`private` になりました。これらのクラスのプロパティは読み取り専用になりました。
    - `Braze.Banner.id` プロパティを削除します。これはバージョン`11.4.0` で非推奨になりました。
        - 代わりに、`Braze.Banner.trackingId` を使用してバナーのキャンペーン "トラッキング ID を読み取ります。
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroid SDK バージョンバインディングを[Braze Android SDK 36.0.0 から37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新します。
    - ネイティブのSwift SDK バージョンバインディングを[Braze Swift SDK 12.0.0 から13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) にアップデートします。
        - `sdkAuthenticationError` イベントが"Required"および"Optional" 認証 エラー s の両方でトリガーされるようになりました。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - iOS およびAndroidバインディングの。NET 9.0 への対応を追加しました。
        - これにより、。NET 7.0 のサポートが削除されます。
        - これには、[iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0)の最小バージョンが必要です。
    - Android バインドを[Braze Android 30.4.0 から32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。
    - iOS バインドを[Braze Swift SDK 9.0.0 から10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。
    - このリリースには、バナー機能のAPI が含まれていますが、現在このSDKでは完全にサポートされていません。.NET MAUI アプリでバナーを使用する場合は、顧客のサポートマネージャーに連絡してから、アプリのライケーションに統合してください。
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - 内部 iOS の`enableSdk` メソッドの実装を更新し、`_requestEnableSDKOnNextAppRun` ではなく`setEnabled`: を使用しました。これは、Swift SDKでは廃止されました。
    - このメソッドを呼び出すと、アプリを再起動して有効にする必要がなくなりました。SDKは、このメソッドが実行されるとすぐに有効になります。
    - 本来のAndroidブリッジを[Braze Android SDK`36.0.0`から`37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。

{% enddetails %}
{% details July 22, 2025 %}

## 2024年7月23日リリース

### Amazon S3 でのセキュリティイベントのエクスポート

セキュリティイベントは、クラウドストレージプロバイダであるAmazon S3 に自動的にエクスポートできます。日次ジョブはUTC の午前0 時に実行されます。一度設定すると、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はありません。

### データの柔軟性

#### CSV インポート

{% multi_lang_include release_type.md release="General availability" %}

CSV インポートを使用して、`first_name`、`last_destination_searched`、および`trip_booked` などのBrazeでs およびカスタムイベントs をレコードおよび更新 ユーザー 属性できます。開始するには、「[CSV インポート]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import)」を参照してください。

#### API 使用アラート

{% multi_lang_include release_type.md release="General availability" %}

API 使用状況アラートは、API 使用状況の重要な可視性を提供し、予期しないトラフィックを事前に検出できます。これらのアラートを設定して主要なAPI リクエストボリュームを追跡することで、リアルタイムの通知s を受信し、マーケティング キャンペーンに影響を与える前に問題に対処できます。

#### ワークスペースAPI レート制限

ワークスペース API レート制限 s では、ワークスペース が特定の取り込みエンドポイントに対して実行できるAPI リクエストの最大数を設定できます(`/users/track` やSDK データなど)。ly レート制限 s をワークスペースs のグループにアプリすることもできます。つまり、制限はそのグループ内のすべてのワークスペースs 間で共有されます。

#### Currents の新しいイベント

これらの新しい事象は、Currents用語集に追加されました。

- [バナー中止イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [バナークリックイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [バナーインプレッションイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [バナー表示イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook 失敗イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### キャンペーン 分析の初期値

デフォルトでは、[**Campaign Analytics**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/)の時間範囲は、現在の時刻から最後の90 日間を表示します。つまり、キャンペーンが90 日以上前に起動された場合、分析は指定された期間に"0" として表示されます。古いキャンペーン s のすべての分析を表示するには、レポートの時間範囲を調整します。

#### キャンバスペディメンションパスステップのビヘイビアを更新

キャンバスにアクティブまたは進行中の実験パスステップがあり、アクティブなキャンバスを更新した場合 (それが実験パスステップでなくても)、進行中の実験は終了します。実験を再開するには、既存の実験パスをを解除して新しい実験パスを開始するか、キャンバスを複製して新しいキャンバスを起動します。 

詳細については、「[開始後のキャンバスの編集]({{site.baseurl}}/post-launch_edits/)」を参照してください。

#### `/users/export/ids` エンドポイントで利用可能な高速レート制限

次の条件を満たすことで、/ユーザー s/export/ids エンドポイント の[ レート制限を1 秒あたり40 リクエストに増やすこともできます。

- ワークスペースでデフォルト レート制限(1 分あたり 250 リクエスト)が有効になっている。既存のレート制限を削除するには、Braze アカウントマネージャーにお問い合わせください。
- リクエストには、fields_to_export パラメータが含まれており、受信するすべてのフィールドが一覧表示されます。

#### メール テンプレート s エンドポイント s の新しい変換

{% multi_lang_include release_type.md release="Early access" %}

以下のエンドポイントs を使用して、メール テンプレートs の変換およびロケールを表示および更新します。

- [GET: ソース翻訳を表示する]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: 「メールテンプレートの特定の翻訳とロケールを表示」エンドポイント
- [GET: メールテンプレートのすべての翻訳とロケールを表示
- [PUT: メールテンプレートの翻訳を更新

### 創造性を引き出す

#### ランディングページ

ランディングページ[ をユーザーのデバイス]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) のサイズにレスポンシブするには、より小さなスクリーンに縦に列を重ねます。これを有効にするには、レスポンシブする行に列を追加し、****カラムのカスタマイズ**セクションの小さいスクリーンに垂直に重ねます。

### 強力なチャネル

#### メールのボットフィルタリング

{% multi_lang_include release_type.md release="General availability" %}

[[メール設定]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings)] でボットフィルタリングを設定して、すべての疑わしいマシンまたはボットクリックを除外します。メールの「ボットクリック」とは、自動プログラムにより生成されたメール内のハイパーリンのクリックを指します。これらのボットクリックをフィルタリングすることで、メッセージを意図的にトリガーし、参加している受信者に配信できます。

#### 製品ブロックのドラッグ&ドロップ

{% multi_lang_include release_type.md release="Early access" %}

ドラッグ＆ドロップエディターでは、カスタムの Liquid コードを作成しなくても、メッセージに製品ブロックをすばやく追加、設定できます。ドラッグアンドドロッププロダクトのブロック機能は、現在メールでのみ使用できます。

#### ランディングページとアプリ内メッセージs のスパンテキスト

スパンテキストを使用すると、[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page)および[アプリ内メッセージs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks)のカスタムコードなしで、テキストブロックに固有のスタイルをアプリできます。そのためには、スタイルするテキストを強調表示し、**スタイル**のスパンでラップを選択します。 

#### WhatsAppへのアドクリック

[WhatsAppにクリックする広告]({{site.baseurl}}/whatsapp_use_cases/)は、Fac eBook、Ins タグ ram、または他のプラットフォームs のメタ広告から、新規および既存の両方の顧客を取得する効率的な方法です。これらの広告を使って、ユーザーにあなたのWhatsAppの存在を認識させながら、あなたの商品やサービスを宣伝しましょう。 

### 新しいBrazeのパートナーシップ

#### Shopify訪問API - eコマース

Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報は Shopify に送信されます。このデータは、加盟店が来店者を把握し、よりパーソナライズされたショッピング体験を提供するための手がかりとなります。

#### 大建堂-eコマース

Braze および[Okendo]({{site.baseurl}}/partners/okendo/) インテグレーションは、レビュー、ロイヤルティ、照会、調査、クイズなど、Okendo のプラットフォームの複数の製品間で機能します。おけどは、カスタムイベントやユーザー 属性をBrazeに送信します。これは、カスタマイズやトリガーに使用できます。

#### Lemnisk - 顧客データプラットフォーム

Brazeと[Lemnisk]({{site.baseurl}}/partners/lemnisk/)インテグレーションは、リアルタイムでユーザーデータをプラットフォーム間で統一するCDP主導のインテリジェンスレイヤーとして機能し、収集したユーザーの情報と行動をリアルタイムでユーザーに送信することで、ブランドと企業がBrazeの可能性を最大限に引き出すことを可能にします。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - `Banner.html` プロパティ、`logBannerClick`、`logBannerImpressions` メソッドを削除しました。代わりに、インプレッションとクリック"トラッキングを自動的に処理する[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)を使用します。
    - 従来のニュースフィード機能のサポートを削除しました。これには、Feed クラスとその関連メソッドの削除が含まれます。
    - 従来のニュースフィードカードで使用された作成済みおよびカテゴリフィールドs は、[`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) サブクラスから削除されました。
    - linkText フィールドも[`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)カードサブクラスとそのコンストラクタから削除されました。
    - SDKが初期化されていない場合、特定のSDKメソッドが明示的に未定義を返し、実際の実行時の動作に合わせて型付けが整列することに注意するために、定義と更新 d型を明確にしました。これにより、以前の(不完全な)タイプに依存していたプロジェクトに新しいタイプスクリプトエラーs が導入される可能性があります。
    - `cropType` が`CENTER_CROP`(デフォルトでは`FullScreenMessage`など)のアプリ内メッセージsの"画像sは、アクセシビリティを向上させるために`<img>`タグではなく`<img>`を使用してレンダリングされるようになりました。これにより、`.ab-center-cropped-img` クラスまたはその子クラスのCSSのカスタマイズが破られる可能性があります。
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - 内部 iOS の`enableSdk` メソッドの実装を更新し、`_requestEnableSDKOnNextAppRun` の代わりにsetEnabled: を使用しました。これは、Swift SDKでは非推奨でした。
        - このメソッドを呼び出すと、アプリを再起動して有効にする必要がなくなりました。SDKは、このメソッドが実行されるとすぐに有効になります。
    - ネイティブAndroidブリッジを[Braze Android SDK 32.1.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Android SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## 2025年6月24日リリース

### BrazeAI Decisioning Studio™

[ BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) は、すべてをパーソナライズするAI デシジョンでA/B テストを置き換え、クリックではなく、どんなメトリクスでも最大化します。BrazeAI Decisioning Studio™では、どんなビジネスKPI でも最適化できます。標本ユースケースと主な機能については、当社の専用の項[ BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)を参照してください。

### 新しいSDKチュートリアル

各Braze SDK チュートリアルでは、詳細なサンプルコードとともに、段階的な手順が提供されます。以下のチュートリアルを選んで使用を開始してください。

- [バナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [アプリ内メッセージのスタイリングをカスタマイズする]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [アプリ内メッセージの条件付き表示]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [トリガーされたアプリ内メッセージの遅延]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### データの柔軟性

#### SAMLジャストインタイムプロビジョニング

{% multi_lang_include release_type.md release="General availability" %}

[SAML ジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)を使用して、新規のダッシュボードユーザーが最初のサインイン時に Braze アカウントを作成できるようにします。これにより、管理者が新しいダッシュボード ユーザーのアカウントを手動で作成し、権限を選択してワークスペースに割り当て、アカウントの有効化を待機する必要がなくなります。

#### 選択ごとのフィルター

[選択]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections)ごとに最大10 個のフィルタを追加できるようになりました。

#### カタログストレージ

[catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage)の空きバージョンのストレージサイズは、最大100MBです。100MB 未満であれば、アイテムに制限はありません。

#### クラウドデータ取り込みで同期された行数

クラウドデータ取り込みでは、デフォルトで、1回の実行で5億行まで同期できます。新しい行が5億 を超える同期はすべて停止されます。

詳細については、[クラウドデータ取り込み製品の制限]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations)を参照してください。

### 強力なチャネル

#### Inbox Visionでのアクセシビリティテスト

{% multi_lang_include release_type.md release="General availability" %}

Inbox Vision の[アクセシビリティテスト]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing)を使用して、メールに存在する可能性のあるアクセシビリティの問題を浮き彫りにします。 

アクセシビリティテストでは、いくつかの[Webコンテンツアクセシビリティガイドライン](https://www.w3.org/WAI/standards-guidelines/wcag/)(WCAG)2.2 AA要件に対してメールコンテンツを分析します。これにより、どの要素がアクセシビリティ基準を満たしていないかについてのインサイトが得られます。

#### WhatsApp のクリック追跡

{% multi_lang_include release_type.md release="General availability" %}

レスポンスメッセージとテンプレートメッセージの両方で[クリックトラッキングを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking)有効にすると、WhatsAppパフォーマンスレポートでクリックデータを確認したり、誰が何をクリックしたかに基づいてユーザー群をセグメンテーションすることができる。

#### WhatsApp用動画

{% multi_lang_include release_type.md release="General availability" %}

送信WhatsAppメッセージの本文には、[動画]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features)を埋め込むことができます。これらのファイルは URL または [Braze メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)でホストされていなければなりません。

### 新しいBrazeのパートナーシップ

#### Stripe - eコマース

Braze と[Stripe]({{site.baseurl}}/partners/stripe) インテグレーションを使用すると、トライアルの開始、サブスクリプションの有効化、サブスクリプション キャンセルの開始などのStripe イベントに基づいてBrazeをトリガー メッセージングできます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - ネイティブAndroidブリッジを[Braze Android SDK 35.0.0から36.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブiOSブリッジを[Braze Swift SDK 11.6.1から12.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [セグメンテーション Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Braze Android SDK を[35.0.0から36.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。

{% enddetails %}
{% details May 27, 2025 %}

## 2025年5月27日リリース

### データの柔軟性

#### ワークスペース間でキャンバスをコピーする

{% multi_lang_include release_type.md release="General availability" %}

キャンバスをワークスペース間でコピーできるようになりました。これによって、別のワークスペースにあるキャンバスのコピーから始めることで、メッセージの構成をジャンプスタートさせることができる。コピーされる内容については、[ワークスペース間でキャンペーンとキャンバスをコピーするを]({{site.baseurl}}/copying_to_workspaces/)参照のこと。

#### 承認ワークフローのメッセージングルール 

{% multi_lang_include release_type.md release="General availability" %}

承認ワークフローで[メッセージングルールを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules)使用し、追加承認が必要になる前に到達可能なユーザー数を制限することで、より多くのオーディエンスをターゲットにする前にキャンペーンやキャンバスを見直すことができる。

#### SnowflakeとBrazeの実体関係図

今年の初め、我々はSnowflakeとBrazeの間で共有されるデータのためにエンティティ関係テーブルを作成した。今月は、各テーブルの詳細をパンしたり、掴んだり、ズームしたりできる[新しいインタラクティブなダイアグラムを]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/)追加し、データがBrazeとどのように相互作用するのか、より良いアイデアを提供する。

### 創造性を引き出す

#### おすすめイベント

{% multi_lang_include release_type.md release="Early access" %}

[推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events)は、最も一般的な e コマースのユースケースに対応しています。推奨イベントを使用することで、事前に作成されたキャンバステンプレート、カスタマーライフサイクルにマッピングされたレポートダッシュボードなどをアンロックすることができる。

### 強力なチャネル

#### バナーチャネル

{% multi_lang_include release_type.md release="General availability" %}

[バナーを]({{site.baseurl}}/user_guide/message_building_by_channel/banners)使えば、ユーザーにパーソナライズされたメッセージングを作成することができ、同時にメールやプッシュ通知など、他のチャネルのリーチを広げることができる。アプリやWebサイトに直接バナーを埋め込むことができるので、自然な感覚でユーザーとエンゲージメントできる。

#### リッチコミュニケーションサービス（RCS）チャネル

{% multi_lang_include release_type.md release="General availability" %}

[リッチ・コミュニケーション・サービス（RCS）は]({{site.baseurl}}/about_rcs/)、従来のSMSを強化するもので、ブランドは情報提供だけでなく、はるかにエンゲージメントの高いメッセージを配信することができる。現在、Android と iOS の両方でサポートされている RCS では、高品質のメディア、インタラクティブなボタン、ブランド化された送信者プロファイルなどの機能がユーザーのプリインストール済みメッセージングアプリで直接使用可能になるため、別のアプリをダウンロードする必要がなくなります。

#### プッシュ設定ページ

{% multi_lang_include release_type.md release="General availability" %}

[**プッシュ設定**ページを]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings)使用して、プッシュTTL（Time to Live）やAndroidキャンペーンのデフォルトFCM優先度など、プッシュ通知の主要設定を行う。これらの設定は、プッシュ通知の配信と効果を最適化し、ユーザーにとってより良いエクスペリエンスを保証するのに役立つ。

#### アプリ内メッセージキャンペーン用プロモーションコード

{% multi_lang_include release_type.md release="Early access" %}

アプリ内メッセージキャンペーンのメッセージ本文に[プロモーションコードのリストスニペットを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list)挿入することで、アプリ内メッセージキャンペーンで[プロモーションコードを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes)使用することができる。

#### Webhookエラーとレート制限の処理

「[Webhook について]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting)」に Braze が Webhook エラーとレート制限をどのように扱うかを説明する新しいセクションが追加されました。

#### アプリ内メッセージのロケール

ワークスペースに[ローカライゼーションを追加]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales)すると、1つのアプリ内メッセージで異なる言語のユーザーをターゲットにすることができる。

#### メール送信プロバイダー（ESP）としてのAmazon SES

SendGridやSparkPostを使うのと同じように、Amazon SESをメールサービスプロバイダー（ESP）として使えるようになった。SSLの設定とリンク間のクリック追跡のニュアンスについては、[BrazeのSSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it)、[ユニバーサルリンクとアプリリンクを]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis)参照のこと。

### 新しいBrazeのパートナーシップ

#### Eagle Eye - ロイヤルティ

Brazeと[Eagle Eyeの]({{site.baseurl}}/partners/eagle_eye/)双方向統合により、ロイヤルティやプロモーションデータをBrazeで直接有効化することができ、マーケターはポイント残高、プロモーション、報酬活動などのリアルタイムデータを使用して顧客エンゲージメントをパーソナライズすることができる。

#### Eppo - AB テスト

Brazeと[Eppoの]({{site.baseurl}}/partners/eppo/)統合により、BrazeでABテストを設定し、Eppoで結果を分析することで、インサイトを明らかにし、メッセージパフォーマンスを収益やリテンションなどの長期的なビジネス指標に結びつけることができる。

#### メンション・ミー - 紹介

[Mention Me](https://www.mention-me.com/) と Braze を組み合わせることで、プレミアム顧客を獲得し、揺るぎないブランドロイヤリティを育むための入り口とすることができます。ファーストパーティの紹介データをシームレスに Braze に統合することで、ブランドのファンをターゲットにした、パーソナライズされたオムニチャネル体験を提供することができます。まずは、「[テクノロジーパートナー:Mention Me]({{site.baseurl}}/partners/mention_me)」をご覧ください。

#### Shopify - eコマース

単一のワークスペースに[複数の Shopify ストアドメインを接続]({{site.baseurl}}/shopify_connecting_multiple_stores/)して、すべての市場における顧客の全体像を把握できます。地域の店舗間で作業を重複させることなく、単一のワークスペースでオートメーションプログラムとジャーニーを構築し、起動します。

### その他

#### Braze でアクセシブルなメッセージを作成するための更新

[Brazeでアクセシブルなメッセージを作成する]({{site.baseurl}}/help/accessibility/)」の記事を更新し、アクセシブルなメッセージを作成するための、より明確で規定的なガイダンスを掲載した。この記事には、コンテンツ構造、altテキスト、ボタン、色のコントラストに関するベストプラクティスの拡張と、カスタムHTMLメッセージのARIAハンドリングに関する新しいセクションが含まれている。 

この更新は、Braze でよりアクセシブルなメッセージング体験をサポートするための幅広い取り組みの一環です。アクセシビリティは進化し続ける分野です。当社は今後も、学んだことを共有し続けます。

{% multi_lang_include accessibility/feedback.md %}

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - このリリースでは、34.0.0で導入された Braze Android SDK の最小バージョンの API 21から API 25への引き上げが取り消されました。これにより、SDK は再び、API 21までをサポートするアプリにコンパイルできるようになりました。コンパイル機能は再導入されましたが、API 25未満の正式なサポートは再導入されておらず、SDK が当該のバージョンを実行するデバイスで意図したとおりに動作するという保証はないことにご注意ください。
    - アプリがこれらのバージョンをサポートしている場合、以下を行う必要があります。
        - SDK の統合が、その API バージョンの物理デバイス (エミュレーターだけでなく) 上で意図したとおりに動作することを検証する。
        - 期待される動作を確認できない場合、[disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) を呼び出すか、それらのバージョンで SDK を初期化しないようにする必要がある。そうしない場合、エンドユーザーのデバイスに意図しない副作用やパフォーマンスの低下を引き起こす可能性がある。
    - アプリ内メッセージによってメインスレッドで既読が発生する問題を修正した。
    `BrazeInAppMessageManager.displayInAppMessage` が Kotlin のサスペンド関数になりました。
        - この関数を直接呼び出さない場合は、何も変更する必要はありません。
    - Jetpack Compose APIsの更新に対応するため、AndroidX Compose BOMを2025.04.01に更新した。
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジをBraze Android SDK 35.0.0から36.0.0に更新。
    - Braze Swift SDK 11.9.0から12.0.0にネイティブiOSバージョンバインディングを更新。
    - iOS の PushNotificationEvent.timestamp の単位表現をミリ秒に更新しました。
        - これまで iOS では、この値は秒単位で表示されていました。これで、既存の Android の実装と一致することになります。
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - このリリースでは、34.0.0で導入された Braze Android SDK の最小バージョンの API 21から API 25への引き上げが取り消されました。これにより、SDK は再び、API 21までをサポートするアプリにコンパイルできるようになりました。ただし、API 25 未満の正式なサポートは再導入されません。詳しくは、[こちら](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600)をご覧ください。
    - ネイティブAndroidブリッジをBraze Android SDK 35.0.0から36.0.0に更新。
    - ネイティブiOSブリッジをBraze Swift SDK 11.9.0から12.0.0に更新。

{% enddetails %}
{% details April 29, 2025 %}

## 2025年4月29日リリース

### Brazeアクセスのトラブルシューティング

[Braze Accessのトラブルシューティングは]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/)、アカウントからロックアウトされたり、Brazeダッシュボードが期待通りに動作しないなど、Brazeにアクセスしようとする際に発生する可能性のある問題をナビゲートするのに役立つ。

### データの柔軟性

#### Currents に関するよくある質問

カレントに関するよくある質問については、新しい「[よくある質問」の]({{site.baseurl}}/user_guide/data/braze_currents/faq/)ページで回答を見ることができる。

#### 匿名ユーザー

匿名ユーザーがどのように機能するのか、またなぜユーザーエイリアスを割り当てたいのかについての詳細は、[匿名ユーザーの]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)次のセクションを参照のこと：
- [CDI の仕組み]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [ユーザーエイリアスの割り当て]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### キャンペーン下書き

[下書きを保存する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts)ことで、アクティブなキャンペーンに大規模な変更を加えることができます。下書きを作成することで、次回のローンチ前に計画した変更を試験的に行うことができる。

#### ユーザーを識別してマージする

ユーザーを[識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)または[マージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)する際、`prioritization` 配列の `least_recently_updated` パラメータを使用して、最も最近更新されたユーザーを優先できるようになりました。

#### スケジュールされたユーザーのマージ

[スケジュールされたマージにより]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging)、事前に設定されたルールを使用して、ユーザープロファイルのマージを毎日自動化することができる。Braze は、スケジュールされたマージが発生する24時間前にワークスペースの管理者に通知し、設定を確認するためのリマインダーと時間を提供します。

#### 受信者オブジェクト

`braze_id` を[受信者オブジェクトに]({{site.baseurl}}/api/objects_filters/recipient_object/)含めることができるようになった。これにより、我々のエンドポイントに情報をリクエストしたり、書き込んだりすることができる。

#### 新しいデータセンター

Braze は2つの新しい[データセンター]({{site.baseurl}}/user_guide/data/data_centers/)、US-10と ID-01を立ち上げました。Braze アカウントを設定する際に、地域別のデータセンターに登録することができます。 

### 創造性を引き出す

#### ランディングページテンプレート

[ランディングページのテンプレートを使って]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates)、次のキャンペーンのテンプレートを作成しよう。これらのテンプレートは、ランディングページエディターとダッシュボードの [**テンプレート**] セクションの両方でアクセスし、管理することができます。

#### ランディングページのフォームフィールド

ランディングページをカスタマイズする際、フォームフィールドを[必須か任意かを]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page)選ぶことができる。必須フィールドは、フォームを送信する前に記入する必要があります。任意フィールドは、ユーザーが空白のままにしたり、選択しないようにすることができます。

#### キャンバスの構築済みテンプレート

Braze キャンバスには、e コマースマーケター向けにカスタマイズされた[事前構築済みのテンプレート]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)がいくつか用意されており、必要な戦略を簡単に実行することができます。このページでは、カスタマージャーニーを強化するために使用できる主なテンプレートをいくつか紹介する。

### 強力なチャネル

#### WhatsApp動画

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp 動画ファイル]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages)を URL または Braze メディアライブラリーでホストできるようになりました。

#### WhatsApp リストメッセージ

[リストメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/)は、クリック可能なオプションのリストを含む本文メッセージとして表示されます。各リストは複数のセクションを持つことができ、最大10行まで含めることができます。

#### プレビューリンクをコピー

HTMLやドラッグ＆ドロップの[メールメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information)、[メールテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message)、[コンテンツブロックに]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) **プレビューリンクをコピーして**、ランダムなユーザーにコンテンツがどのように見えるかを示す共有可能なリンクを生成しよう。

#### プッシュ登録図

ユーザーガイドのプッシュ通知ドキュメントを刷新し、[プッシュ登録がどのようなものかを大規模に]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale)視覚化するのに役立つ新しい図を追加した。

### 新しいBrazeのパートナーシップ

#### パートナーカテゴリーの更新

[テクノロジーパートナーのセクションを]({{site.baseurl}}/partners/home/)更新し、新しいカテゴリーとサブカテゴリーを追加した。

#### Shopify（新バージョン） - eコマース

Shopify統合の新バージョンは、Shopifyストアの種類と最初の統合設定に使用された外部IDに基づいて、4月から段階的にリリースされる。

**旧バージョンの統合は2025年8月28日に廃止予定です。2025年8月28日までに、より新しいバージョンの統合に更新する必要があります。**

Braze の新規顧客: 2025年4月より、Braze は新規オンボーディングと既存顧客のアップグレードのために、新しい Shopify コネクターを順次展開していきます。新しい標準統合の詳細については、[Shopify標準統合を]({{site.baseurl}}/shopify_standard_integration/)参照のこと。

#### Just Words - ダイナミックなコンテンツ

[Just Words]({{site.baseurl}}/partners/just_words/) は、ライフサイクルマーケティングチャネルのメッセージングを大規模にパーソナライズし、何百ものバリエーションをダイナミックな方法でテストし、パフォーマンスの低いコンテンツを自動的に更新します。

#### Tapcart - e コマース

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) は Shopify を採用したブランド向けの業界をリードするモバイルコマースプラットフォームで、顧客が好むパーソナライズされた魅力的なショッピング体験を提供するカスタムモバイルアプリの作成を可能にします。

### SDK

#### Braze SDKバージョン管理

Braze SDKの[バージョン管理について]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)学べるようになったので、あなたのアプリは最新機能と品質向上で常に最新の状態に保つことができる。

#### SDKドキュメント監査

Braze では現在、[開発者向けの SDK コンテンツ]({{site.baseurl}}/developer_guide/)をすべて監査し、すべてのコードサンプルが有用かつ正確であることを確認しています。現在まで、当社は Android と Swift のドキュメントに様々な更新を行っており、今後さらに多くの更新が予定されています。

### Braze ドキュメントへの貢献

#### Braze コントリビューターのオフラインサポート

Braze Docsのコントリビューターであれば、ローカルのドキュメントサイトを完全にオフラインで生成できるようになった。まずは、「[Braze ドキュメントへの貢献]({{site.baseurl}}/contributing/home/)」をご覧ください。

#### Braze Docsフォークのトラブルシューティング

Braze ドキュメントの寄稿者が自分たちのフォークから Braze のリポジトリをターゲットにする際にトラブルが発生した場合に、復旧に役立つ[トラブルシューティングのステップ]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository)を作成しました。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Braze Unity SDK 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - ネイティブiOSブリッジを[Braze Swift SDK 10.3.0から11.9.0に](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブAndroidブリッジを[Braze Android SDK 32.1.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - 最低限必要なAndroid SDKのバージョンは25である。詳細については、[こちら](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)をご覧ください。
- [Braze Segment Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Braze Android SDK を[32.1.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - 最低限必要なAndroid SDKのバージョンは25である。詳細については、[こちら](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)をご覧ください。
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - 分散型の静的 XCFramework は、外部リソースバンドルに依存する代わりに、リソースを直接含めるようになりました。
        - 静的 XCFramework を手動で統合する場合、ターゲットの [*一般設定*] の [&Frameworks, Libraries, and Embedded Content&] セクションで、各 XCFramework の [*Embed & Sign*] オプションを選択する必要があります。
        - Swift パッケージマネージャーや CocoaPods の統合に対する変更は不要です。
- [Braze Segment Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - `12.0.0` 以上の SemVer のリリースを要求するように、Braze Swift SDK バインディングを更新しました。
        - これにより、Braze SDK の`12.0.0`から`13.0.0`までのあらゆるバージョンとの互換性が確保されます (11.0.0は含まれません)。
        - 変更内容の詳細については、[`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) の変更履歴エントリを参照してください。

{% enddetails %}
