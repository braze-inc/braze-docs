---
nav_title: リリースノート
article_title: リリースノート
page_order: 4
layout: dev_guide
guide_top_header: "リリースノート"
guide_top_text: "ここではBrazeプラットフォームのすべてのアップデートを見ることができ、以下の<a href='/docs/help/release_notes/#most-recent'>最新のプラットフォームアップデート</a>があります。<a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDKの変更履歴</a>もご覧ください。"
page_type: landing
search_rank: 1
description: "このランディングページには、Brazeのリリースノートが掲載されています。ここでは、BrazeプラットフォームとSDKのすべてのアップデート、および非推奨機能のリストをご覧いただけます。"

guide_featured_title: "リリースノート"
guide_featured_list:
  - name: 2024
    link: /docs/help/release_notes/2024/
    fa_icon: fas fa-calendar-alt
  - name: 2023
    link: /docs/help/release_notes/2023/
    fa_icon: fas fa-calendar-alt
  - name: 2022
    link: /docs/help/release_notes/2022/
    fa_icon: fas fa-calendar-alt
  - name: 2021
    link: /docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code

---

# 最新のBrazeリリースノート {#most-recent}

> Brazeは、メジャー・プロダクト・リリースに合わせて、製品のアップデート情報を毎月リリースしていますが、週ごとに雑多な改良が加えられています。
> <br>
> <br>
> このセクションに記載されているアップデートの詳細については、アカウントマネージャーにお問い合わせいただくか、[サポートチケットをご請求]({{site.baseurl}}/help/support/)ください。また、[SDK Changelogsで]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/)毎月のSDKリリース、アップデート、改良に関する詳細情報をご覧いただけます。

## 2024年3月5日リリース

### Google EUユーザー同意ポリシー

Googleは、2024年3月6日より施行される[デジタル市場法（DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)）の変更に対応するため、[EUユーザー同意ポリシーを](https://www.google.com/about/company/user-consent-policy/)更新します。この新たな変更により、広告主はEEAおよび英国のエンドユーザーに対して特定の情報を開示し、彼らから必要な同意を得る必要がある。今度の変更の一環として、[Brazeで両方の同意シグナルをカスタム属性として収集]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)することができます。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期します。

### データの柔軟性

#### 重複ユーザーのマージ

{% multi_lang_include release_type.md release="Early access" %}

Brazeのダッシュボードで、[重複ユーザーを検索してマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)し、キャンペーンやキャンバスの効果を最大化できるようになりました。ユーザプロファイルを個別にマージすることも、識別子が一致するすべてのプロファイルを最新の更新されたユーザプロファイルにマージする一括マージを実行することもできます。

#### アーカイブコンテンツの検索

Brazeダッシュボードで、**アーカイブされたコンテンツを表示**するを選択することで、[検索結果にアーカイブされた]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)コンテンツを含めることができるようになりました。

#### AWS S3およびGoogle Cloud Storageのメッセージ・アーカイブ・サポート

[メッセージアーカイブを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)使用すると、アーカイブやコンプライアンス目的でユーザーに送信したメッセージのコピーをAWS S3バケット、Azure Blob Storageコンテナ、またはGoogle Cloud Storageバケットに保存できます。

#### SQLテーブル・リファレンス

[SQL テーブル・リファレンスに]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)アクセスして、クエリ・ビルダーまたは SQL Segment Extensions の生成時にクエリ可能なテーブルとカラムを確認してください。

### 創造性を解き放つ

#### AIコピーライティングのためのトーンコントロール

AIコピーライティングアシスタントで生成されるコピーのスタイルを決定するために、[メッセージトーンを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)選択できるようになりました。

### 堅牢なチャンネル

#### カード作成

Brazeが新しいコンテンツカードキャンペーンとキャンバスのステップについて、オーディエンスの適格性とパーソナライズを評価するタイミングは、カードが[作成さ]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)れるタイミングを指定することで選択できます。 

#### ユーザーパスのプレビュー

{% multi_lang_include release_type.md release="General availability" %}

ユーザーが受け取るタイミングやメッセージをプレビューするなど、ユーザーのために作成したキャンバスの旅を体験してください。これらの[テスト実行は]({{site.baseurl}}/preview_user_paths/)、Canvasを送信する前に、メッセージが適切なオーディエンスに送信されているかどうかの品質保証として機能します。

#### クイック・プッシュ・キャンペーン

{% multi_lang_include release_type.md release="General availability" %}

Brazeでプッシュキャンペーンを作成する際、複数のプラットフォームやデバイスを選択し、[クイックプッシュと]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/)呼ばれる1回の編集で、すべてのプラットフォーム向けに1つのメッセージを作成することができます。この機能はキャンペーンでのみ利用可能です。

#### カスタムの list-unsubscribe ヘッダー

{% multi_lang_include release_type.md release="General availability" %}

メールメッセージに[カスタムリスト・アンサブスクライブヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)追加することで、受信者がオプトアウトできるようになります。この方法で、あなた自身が設定したワンクリック配信停止エンドポイントと、オプションの "mailto: "を追加することができます。Brazeでは、カスタムlist-unsubscribeヘッダをサポートするためにURLの入力が必要です。これは、ワンクリックでunsubscribe HTTPができることが、YahooやGmailの大量送信者の要件だからです。

#### アプリ内メッセージ用の複数ページ

{% multi_lang_include release_type.md release="Early access" %}

[アプリ内メッセージにページを追加する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page)ことで、オンボーディングフローやウェルカムジャーニーのような連続したフローでユーザーを誘導することができます。**Build**タブの**Pages**セクションからページを管理することができます。

#### 実験パスのランダム化

実験パスのステップで[パスの割り当てを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)常に[ランダム化]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)するには、ステップの**Experiment PathsでRandomized Pathsを**選択します。このオプションは、ウイニング・パスまたはパーソナライズド・パスを使用している場合は利用できない。

#### メールキャプチャフォーム

[Eメールキャプチャメッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/)使用すると、簡単にサイトのユーザーにEメールアドレスの送信を促すことができます。

### SDKアップデート
 
以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - これは、2024年3月1日にObjective-C SDKが終了する前の最後のリリースとなります（[Swift SDKの](https://github.com/braze-inc/braze-swift-sdk/)使用が優先されます）。
    - SDWebImageの最小必要バージョンを5.8.2から5.18.7に更新しました。このバージョンには、[プライバシーに影響を与えるSDKの](https://developer.apple.com/support/third-party-SDK-requirements/)リストに表示されるSDWebImageのプライバシーマニフェストが含まれています。
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [ユニティ 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDKバージョン4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-コードバ SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジを[Braze Android SDK 27.0.1から30.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
    - ネイティブiOSブリッジを[Braze Swift SDK 6.6.0から7.6.0](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。
    - `Banner` コンテンツ・カード・タイプの名前を`ImageOnly` に変更：
        - `ContentCardTypes.BANNER`から`ContentCardTypes.IMAGE_ONLY`
        - Androidでは、プロジェクト内のXMLファイルにコンテンツカードのバナーという単語が含まれている場合、それを`image_only` に置き換える必要があります。
    - `BrazePlugin.getFeatureFlag(id)` はfeatureフラグが存在しない場合、`null` を返すようになった。
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` は、リフレッシュ要求が成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがあった場合、最初のサブスクリプション時にのみトリガーされます。
    - 非推奨のメソッド`registerAppboyPushMessages` を削除した。代わりに`setRegisteredPushToken` 。

## 2024年2月6日リリース

### プライバシー・マニフェスト

Brazeは、宣言されたトラッキングデータを自動的に専用の`-tracking` エンドポイントにリルートする新しい柔軟なAPIとともに、独自のプライバシーマニフェストをリリースしました。詳細については、[Brazeのプライバシー・マニフェストを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)ご覧ください。

### Google EUユーザー同意ポリシー

グーグルは、2024年3月6日に施行される[デジタル市場法（DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)）の変更に対応するため、[EUユーザー同意ポリシーを](https://www.google.com/about/company/user-consent-policy/)更新する。この新たな変更により、広告主はEEAおよび英国のエンドユーザーに対して特定の情報を開示し、彼らから必要な同意を得る必要がある。今度の変更の一環として、[Brazeで両方の同意シグナルをカスタム属性として収集]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)することができます。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期します。

### データの柔軟性

#### Google Firebase Cloud Messaging (FCM) API

{% multi_lang_include release_type.md release="General availability" %}

[Google の非推奨 Cloud Messaging API から、完全にサポートされた Firebase Cloud Messaging (FCM) API に移行]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)できるようになりました。 

#### Braze Cloud Data Ingestion（CDI）エンドポイント

{% multi_lang_include release_type.md release="General availability" %}

BrazeのCDIエンドポイントを使用してください：
[\- 既存の統合のリストを返します]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)。
\- 指定した積分の[過去の同期ステータスの一覧を返します]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)。
\- 指定した統合の[同期をトリガーする]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)。

#### Braze Cloud Data Ingestion (CDI)のDatabricksへの対応

カタログのBraze CDIサポートが[Databricksソースで]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data)利用可能になりました。

#### 手動によるSwift SDKの統合

パッケージマネージャを使用せずに手動で Swift SDK を統合する方法を説明するために、統合ガイドに[手動統合の]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration)記事を追加しました。

#### 非推奨

2024年1月11日、BrazeはWindowsアプリとBaiduアプリからのメッセージ配信とデータ収集を停止した。

### 創造性を解き放つ

#### SQLセグメント拡張の使用例

[SQL Segment Extensions の使用例]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases)ライブラリには、SQL Segment Extensions のテスト済みクエリが含まれており、独自の SQL クエリを作成する際のインスピレーションとして使用できます。

### 堅牢なチャンネル

#### カスタムコードブロック

{% multi_lang_include release_type.md release="General availability" %}

[カスタムコードブロックでは]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code)、アプリ内メッセージのHTML、CSS、JavaScriptを追加、編集、削除できます。

#### プッシュ通知のペイロードサイズを小さくする

新しいヘルプ記事「[通知ペイロードサイズ]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size)」では、プッシュペイロードサイズの制限のためにキャンペーンやキャンバスステップを開始できない場合に、プッシュ通知のペイロードサイズを小さくするためのヒントを提供しています。

#### キャンペーンまたはキャンバスにBCCアドレスを追加する

{% multi_lang_include release_type.md release="General availability" %}

Eメールメッセージに[BCCアドレスを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings)追加することができます。これにより、あなたのユーザーが受信したメッセージの同じコピーが、あなたのBCC受信トレイに送信されます。これにより、コンプライアンス要件やカスタマーサポートの問題のために、ユーザーに送信したメッセージのコピーを保持することができます。

#### ワンクリックでメール配信停止リンク

[list-unsubscribeヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe-header)使用すると、メール本文ではなく、メールボックスのUI内に**配信停止**ボタンを表示することで、受信者がマーケティングメールからワンクリックで配信停止できるようになります。

### 新しいブレイズ・パートナーシップ

#### Criteo - キャンバス・オーディエンス・シンク

[CriteoへのBraze Audience Syncを]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/)使用することで、ブランドは自社のBrazeインテグレーションからCriteoの顧客リストにユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信することができます。ユーザーデータに基づいてBraze Canvasでメッセージ（プッシュ、Eメール、SMS、ウェブフックなど）をトリガーするために通常使用する基準をすべて、Criteoの顧客リスト内のそのユーザーへの広告のトリガーに使用できるようになりました。

#### ムーバブル・インク - ダイナミック・コンテンツ

[Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink)Customer Data API統合により、マーケティング担当者は、Brazeに保存されている顧客イベントデータを有効化して、Movable Ink内でパーソナライズされたコンテンツを生成することができます。

#### スキューバ・アナリティクス - 分析

[Scuba Analyticsは]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics)、高速時系列データ用に設計された、フルスタックの機械学習によるデータコラボレーションプラットフォームです。Scubaでは、ユーザー（アクターとも呼ばれます）を選択的にエクスポートし、Brazeプラットフォームにロードすることができます。スクーバでは、カスタム・アクター・プロパティを使って行動傾向を分析し、さまざまなプラットフォームでデータを活性化し、機械学習を使って予測モデリングを行います。

### SDKアップデート
 
以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。
 
- [Expo プラグイン 2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - [Expo SDK 50の要件に従って](https://expo.dev/changelog/2024/01-18-sdk-50)、iOSの最小プラットフォームバージョンを`13.4` 。
    - このバージョンでは、Expo SDK 50を完全にサポートするために、Braze React Native SDKのバージョン[8.3.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0)以上が必要です。
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - アプリ内メッセージに使用される WebView が更新され、`WebViewAssetLoader` を使用するようになりました。
        - `WebSettings.allowFileAccess` `InAppMessageHtmlBaseView` と`BrazeWebViewActivity` では false に設定されている。
        - 独自の`InAppMessageWebViewClient` または`InAppMessageHtmlBaseView` を使用している場合は、元のクラスと比較して、実装が正しくアセットを読み込んでいることを確認してください。
        - カスタム・クラスを使用していない場合は、すべてが以前と同じように機能する。
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDKバージョン3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGet パッケージの名前は`AppboyPlatformXamariniOSBinding` から [`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/).
        - 更新されたパッケージを使用するには、using`AppboyPlatformXamariniOSBinding;` をusing Brazeに置き換えてください；
    - このバージョンでは、.NET 6+を使用する必要があり、Xamarinフレームワークを使用するプロジェクトのサポートは削除されました。Xamarinのサポート終了に関する[マイクロソフトの方針を](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)参照。
    - Androidバインディングを[Braze Android SDK 26.3.2から29.0.](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)1に更新しました。
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - このバージョンは、[Braze Swift SDKを](https://github.com/braze-inc/braze-swift-sdk/)使用するようにiOSバインディングを更新します。ほとんどのiOSのパブリックAPIは変更されています。使用する置き換えに関するガイダンスについては、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)（Swift）を参照してください。私たちは、古いパブリックAPIを使い続けるための互換バインディングを提供しています。
        - iOSバインディングは現在、複数のモジュールで構成されている：
            - **BrazeKit：**アナリティクスとプッシュ通知のサポートを提供する主なSDKライブラリ（nuget：[Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)）。
            - BrazeUI：Brazeが提供するアプリ内メッセージとコンテンツカード用のユーザーインターフェースライブラリ（nuget：[Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)）。
            - ブレイズロケーション位置分析とジオフェンス監視をサポートする位置情報ライブラリ（nuget：[Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)）。
            - BrazeKitCompat：4.0.0以前のAPIをサポートする互換ライブラリ（nuget：[Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)）。
            - BrazeUICompat：4.0.0以前のUI APIをサポートする互換ライブラリ（nuget：[Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)）。
        - 新しい統合についてはBrazeiOSMauiSampleAppを、互換モジュールの使用法についてはBrazeiOSMauiCompatSampleAppを参照してください。
    - iOSバインディングを[Braze Swift SDK 7.6.0に](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)更新しました。
    - iOSバインディングは、Xcode 15との互換性のために.NET 7を使用する必要があります。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024年1月9日リリース

### Shopifyとの統合に関するドキュメントの更新

BrazeとShopifyの統合ドキュメントの一部を更新しました：

- [Shopifyを始める]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [BrazeでShopifyを設定する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [ShopifyユーザーID管理]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### データの柔軟性

#### カタログの在庫切れ通知

{% multi_lang_include release_type.md release="Early access" %}

カタログとキャンバスを組み合わせて、[在庫]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)切れをお客様にお知らせすることができます。顧客が選択したカスタムイベントを実行するたびに、アイテムが補充されたときに通知されるように自動的に購読することができます。

#### カタログセグメント

{% multi_lang_include release_type.md release="Early access" %}

[カタログセグメントは]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/)、SQL Segment Extensionsのカタログデータに基づくユーザーのオーディエンスです。これらのSQL Segment Extensionsは、セグメントで参照し、キャンペーンやキャンバスでターゲットにすることができます。カタログセグメントはSQLを使用して、カタログのデータとカスタムイベントや購入のデータを結合します。そのためには、カタログとカスタムイベントまたは購入に共通の識別子フィールドを持つ必要があります。

#### Firebase Cloud Messaging API への移行

{% multi_lang_include release_type.md release="Early access" %}

Google の非推奨 Cloud Messaging API から、完全にサポートされた Firebase Cloud Messaging (FCM) API への[移行方法について]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)説明します。

### SDKアップデート

以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeKit` 、`BrazeLocation` 、Brazeのデータ収集ポリシーを説明するプライバシー・マニフェストを追加。詳細については、プライバシーマニフェストに関するAppleの[ドキュメントを](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)参照してください。データ収集方法を管理するためのより多くの設定は、将来のリリースで利用可能になる予定です。
    - 7.1.0で導入されたXCFrameworksのコード署名に関する問題を修正しました。
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOSブリッジをBraze Swift SDK 6.1.0から7.4.0に更新しました。
        - iOS リポジトリのリンクは、この[リポジトリから](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)ビルド済みの動的 XCFrameworks を指すようになりました。
    - ネイティブAndroidブリッジをBraze Android SDK 27.0.1から29.0.1に更新しました。
    - `AppboyBinding.GetFeatureFlag(string id)` はfeatureフラグが存在しない場合、`null` を返すようになった。
    - `FEATURE_FLAGS_UPDATED` は、リフレッシュ要求が成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがあった場合、最初のサブスクリプション時にのみトリガーされます。


## 2023年12月12日発売

### アンドロイド・プッシュ統合の更新

2023年6月20日、GoogleはAndroidアプリにプッシュ通知を送るためのCloud Messaging APIを廃止した。[標準Androidプッシュ統合では](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)、代わりにGoogleのFirebase Cloud Messaging APIを設定する方法が表示されるようになりました。

GoogleのCloud Messaging APIの減価償却の詳細については、[Firebase FAQを](https://firebase.google.com/support/faq#fcm-23-deprecation)参照してください。

### 堅牢なチャンネル

#### WhatsApp レスポンスメッセージ

{% multi_lang_include release_type.md release="General availability" %}

キャンペーンやキャンバスで[WhatsAppメッセージを作成]({{site.baseurl}}/whatsapp_response_messaging/)する際、24時間以内にユーザーのWhatsAppメッセージに返信するレスポンスメッセージを作成できます。レスポンスメッセージは、オプトインキャンペーンなど、ブランドとユーザーとのインタラクションを促進するキャンバスで特に役立ちます。

#### WhatsAppの周波数上限設定

{% multi_lang_include release_type.md release="General availability" %}

WhatsAppに[回数制限ルールを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)設定できるようになりました。フリークエンシー・キャッピングは、キャンペーンまたはキャンバス・コンポーネントの送信レベルで適用され、**「設定**」>「**フリークエンシー・キャッピング・ルール**」からワークスペースごとに設定できます。  

### データの柔軟性

#### コンバージョンダッシュボード

{% multi_lang_include release_type.md release="General availability" %}

[コンバージョンダッシュボードでは]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard/)、さまざまなアトリビューションメソッドを使用して、キャンペーン、キャンバス、チャンネルを横断してコンバージョンを分析できます。コンバージョンを測定する際、時間枠、コンバージョンイベント、コンバージョンウィンドウを指定することができます。

#### メールインサイトレポート

{% multi_lang_include release_type.md release="General availability" %}

[メールパフォーマンスダッシュボード]({{site.baseurl}}/email_engagement_dashboard/)内に、2つの新しいレポートを含む新しいタブ「メールインサイト」があります：

- **メールボックス・プロバイダーによる関与：**メールボックスプロバイダー別のクリック数と開封数を表示します。メールボックスプロバイダを選択し、特定の受信ドメインをドリルダウンすることができます。
- **曜日別エンゲージメント**ユーザーがいつメールに関与しているかを表示します。

#### サブスクリプション・グループの時系列グラフの更新

{% multi_lang_include release_type.md release="General availability" %}

**購読グループ**ページに表示される**購読グループタイムセリーグラフは**、メールや電話番号ごとではなく、ユーザーごとの購読カウントを表示するようになりました。これは、Brazeがダッシュボードの他の領域で統計を計算する方法と、よりよく一致しています。

### AIとMLの自動化

#### AIアイテムの推奨

{% multi_lang_include release_type.md release="General availability" %}

[AIアイテム・レコメンデーションは]({{site.baseurl}}/ai_item_recommendations)、ディープラーニング（深層学習）ベースの商品レコメンデーションエンジンで、ユーザーの購買行動の集合を利用して商品を推薦する。AIアイテム・レコメンデーションを使用して、最も人気のある商品を計算したり、特定のカタログ用にパーソナライズされたAIレコメンデーションを作成することができます。レコメンデーションの作成後、パーソナライゼーションを使用してそれらの製品をメッセージに挿入できます。

### 新しいブレイズ・パートナーシップ

#### ZapierによるFacebookリード広告 - リード獲得

[Zapier経由でFacebook Lead Adsを統合]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/facebook_via_zapier/)すると、FacebookからBrazeにリードをインポートし、リードが捕捉されたときにカスタムイベントを追跡することができます。

#### SmarterSends - メッセージテンプレート

Brazeと[SmarterSendsの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/smartersends/)パートナーシップにより、Brazeのパワーと分散したユーザーが所有するハイパーローカライズされたコンテンツを組み合わせることができ、マーケティングキャンペーンを向上させることができます。

#### Recurly - 支払い

[Recurlyと]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/recurly/)Brazeの統合により、Brazeとの購読データの共有プロセスが簡素化され、顧客との的を絞ったコミュニケーションが可能になります。

### SDKアップデート

以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [Flutter SDK 8.0.0-8.1.0](https://pub.dev/packages/braze_plugin/changelog)
  - ネイティブAndroidブリッジをBraze Android SDK 27.0.1から29.0.1に更新。
  - ネイティブiOSブリッジをBraze Swift SDK 6.6.1から7.2.0に更新。
  - Feature Flagsメソッドの動作を変更する。
    - `BrazePlugin.getFeatureFlagByID(String id)` はfeatureフラグが存在しない場合、`null` を返すようになった。
    - `BrazePlugin.subscribeToFeatureFlags(void Function(List<BrazeFeatureFlag>) onEvent))` は以下の場合にのみ発動する：
      - リフレッシュ要求が成功または失敗で完了したとき。
      - 現在のセッションから以前にキャッシュされたデータがある場合、最初のサブスクリプション時に。
  - Android SDKの最低サポートバージョンは21です。
- [React Native SDK 8.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.2.0/CHANGELOG.md)
- [Swift SDK 7.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Braze Segment Swift プラグイン 2.2.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
- [Braze Expo プラグイン 1.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.2.0/CHANGELOG.md)

## 2023年11月14日リリース

### Brazeを使い始める

エキサイティングなニュースだ！Brazeの[マーケティング担当]({{site.baseurl}}/user_guide/getting_started)者と[開発者]({{site.baseurl}}/developer_guide/platform_wide/getting_started)向けに特別に作られた2つの入門セクションをご紹介します。これらのセクションは、必要なツールやガイダンスを提供することで、Brazeを使い始められるように設計されています。飛び込んで探検を始めよう。

### 新しいBrazeダッシュボードのインスタンス

Brazeは、ダッシュボードとRESTエンドポイント用のさまざまなインスタンスを管理しています。新しいダッシュボードのインスタンス`US-07` を追加しました。詳細は[APIの]({{site.baseurl}}/api/basics/)概要を参照。

### 堅牢なチャンネル

#### アプリ内メッセージのカスタムテンプレートをドラッグ＆ドロップで作成可能

{% multi_lang_include release_type.md release="General availability" %}

[アプリ内メッセージ用のカスタムテンプレートをドラッグ＆ドロップで]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)使用し、ドラッグ＆ドロップエディターでアプリ内メッセージのデザインを開始できるようになりました。

#### SMSダブルオプトイン

{% multi_lang_include release_type.md release="General availability" %}

[SMSダブルオプトインは]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/)、ユーザーがSMSメッセージを受信する前に、オプトインの意思を明示的に確認することを要求することができます。これによって、SMSを利用する可能性の高いユーザーやSMSを利用しているユーザーに焦点を絞ることができます。

#### メールレポート用の推定実質開封率

{% multi_lang_include release_type.md release="General availability" %}

[推定実開封]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#estimated-real-open-rate)率は、Brazeが独自に作成した分析モデルを使用して、機械開封が存在しないかのようにキャンペーン独自の推定開封率を再構築します。Brazeは、各キャンペーンのクリックデータを使用して、実際の人間がメッセージを開封した割合を推測します。これは、アップルのMPPを含むさまざまなマシン・オープニング・メカニズムを補正するものである。 

#### キャンバス用パーソナライズド・パス

{% multi_lang_include release_type.md release="Beta" %}

[パーソナライズパスを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/)使用すると、キャンペーンにおけるパーソナライズバリアントと同様に、コンバージョンの可能性に基づいて個々のユーザーに対してキャンバスのジャーニー全体をパーソナライズすることができます。パーソナライズドパスとエクスペリメントパスステップを使用して、Brazeが残りのパスを互いにテストしている間、一部のユーザーを遅延グループに保持します。

### データの柔軟性

#### Brazeダッシュボードの検索

{% multi_lang_include release_type.md release="General availability" %}

[検索バーを使って]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/)、Brazeのダッシュボード内で自分の仕事やその他の情報を見つけることができます。検索バーはBrazeダッシュボードの上部にあります。 

#### カスタム属性とイベントのブロックリスト

{% multi_lang_include release_type.md release="General availability" %}

一度に最大10個のカスタム属性またはイベントをブロックリストに登録できるようになりました。詳細については、[カスタム・イベントと属性の]({{site.baseurl}}/user_guide/administrative/app_settings/custom_event_and_attribute_management/)管理を参照してください。

#### 新しいヘルプ記事ユニバーサルリンクとアプリリンク

アップルのユニバーサルリンクとアンドロイドのアプリリンクは、ウェブコンテンツとモバイルアプリ間のシームレスな移行を提供するために考案された仕組みです。ユニバーサルリンクがiOSに特有であるのに対し、AndroidアプリリンクはAndroidアプリに同じ目的を果たす。 

このトピックについて詳しくは、[ユニバーサルリンクとアプリリンクの]({{site.baseurl}}/help/help_articles/email/universal_links/)記事をご覧ください。

### 新しいブレイズ・パートナーシップ

#### Olo - チャンネル拡張

Brazeと[Oloの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/olo/)統合により、Brazeのユーザープロフィールを更新して、Oloのユーザープロフィールとの一貫性を保つことができます。また、Oloのイベントに基づいてBrazeから適切なメッセージを送信することもできます。

#### Typeform - 顧客データプラットフォーム

Brazeと[Typeformの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/typeform/)統合により、Typeformのレスポンスから収集したデータでBrazeのユーザープロフィールを更新したり、ユーザーのTypeformへのエンゲージメントに基づいてBrazeのメッセージングをトリガーしたり、ユーザーのTypeformのレスポンスに基づいてBrazeのメッセージングをパーソナライズしたりすることができます。

### SDKアップデート

以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [Web SDK v4.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Web SDK v5.0.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 29.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.1.0-7.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `Braze.Configuration.DeviceProperty.pushDisplayOptions` は非推奨となった。この値を与えても効果はない。
- [React Native SDK 8.0.0-8.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジをBraze Android SDK 27.0.1から29.0.0に更新。
    - ネイティブiOSブリッジをBraze Swift SDK 6.6.0から7.0.0に更新。
    - `Banner` コンテンツカードのタイプをImageOnlyに変更：
        - `BannerContentCard`から`ImageOnlyContentCard`
        - `ContentCardTypes.BANNER`から`ContentCardTypes.IMAGE_ONLY`
    - Androidでは、プロジェクト内のXMLファイルにコンテンツカードの`banner` という単語が含まれている場合、`image_only` に置き換える必要があります。
    - `Braze.getFeatureFlag(id)` はfeatureフラグが存在しない場合、`null` を返すようになった。
    - `Braze.Events.FEATURE_FLAGS_UPDATED` は、リフレッシュ要求が成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがあった場合、最初のサブスクリプション時にのみトリガーされます。

## 2023年10月17日リリース

### ワークスペースへのコピー

[ワークスペース間でキャンペーンをコピーすること]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/)で、別のワークスペースにあるキャンペーンのコピーから始めることで、メッセージの構成でスタートダッシュを切ることができます。このコピーは、編集してローンチするまで下書きとして残り、成功したメッセージング戦略を維持・発展させるのに役立ちます。

### 試験電流コネクタ

[テストカレントコネクターは]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/#test-currents-connectors)、既存のコネクターの無料バージョンで、さまざまな行き先をテストしたり試したりするために使用できます。テスト電流がある：

- テストカレントコネクターの数に制限はありません。
- 30日間の合計で最大10,000イベント。このイベントの合計は、ダッシュボード上で1時間ごとに更新される。

### 特徴的なフラグ

[機能フラグを]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/)使用すると、特定のユーザーまたはランダムに選択されたユーザーに対して、リモートで機能を有効または無効にすることができます。重要なのは、追加コードのデプロイやアプリストアのアップデートをすることなく、本番環境で機能をオン／オフできることだ。これにより、安心して新機能を展開することができる。

### 特集フラッグ実験

[機能フラグ実験では]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/)、コンバージョン率を最適化するためにアプリケーションの変更をA/Bテストできます。マーケティング担当者は、機能フラグを使用して、新機能がコンバージョン率にプラスの影響を与えるかマイナスの影響を与えるか、またはどの機能フラグのプロパティセットが最も最適かを判断することができます。

### ユーザープロファイルのマージ

**Search Users（ユーザ検索）**ページで検索した結果、複数のユーザ・プロファイルが返された場合、**Merge duplicates（重複をマージ**）ボタンをクリックして[ユーザ・プロファイルをマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#merge-profiles)することができます。どのユーザープロファイルを保持するかを選択できます。つまり、このプロファイルは保持され、マージされたプロファイルから属性を得ることになります。

### セグメント別業績データ

クエリビルダーのレポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのセグメント別に[パフォーマンスデータを分解]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)できるようになりました。

### ユーザープロファイルの更新

[`/users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)使用して、電話番号または電子メールでユーザープロファイルを更新できるようになりました。

## SDKアップデート
 
以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。
 
- [Braze Segment Swift プラグイン v2.1.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
- [Web SDK v4.10.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Web SDK v5.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - この [`subscribeToFeatureFlagsUpdates()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates)コールバックは、リフレッシュの成否にかかわらず、常に呼び出されるようになりました。更新の受信に失敗した場合、コールバックは現在キャッシュされている機能フラグで呼び出される。
    - この [`getFeatureFlag()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getfeatureflag)メソッドは、機能フラグが存在しない場合、または機能フラグが無効になっている場合はNULLを返すようになりました。
    - 4.0.4で非推奨とされていた`logContentCardsDisplayed()` メソッドを削除。
    - 非推奨の初期化オプション`enableHtmlInAppMessages` を削除。これは`allowUserSuppliedJavascript` オプションに置き換えるべきである。
    - 4.9.0で非推奨とされたBannerクラスを削除し、次のように変更しました。 [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html).
    - `Banner` クラス削除の一環として、`ab-banner` CSS クラス名を削除。CSSのカスタマイズは、代わりに`ab-image-only` 。
    - SDKがランタイムエラーを投げなくなった。初期化前にBrazeのメソッドが呼び出された場合、代わりに警告がコンソールに記録されます。
    - SDKは、カスタムHTMLアプリ内メッセージにデフォルトのBrazeアプリ内メッセージスタイルを追加しなくなりました。これらのスタイルは、以前はレガシーのアプリ内メッセージタイプで使用されていました。
- [Android SDK 29.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - `BannerImageCard`,`BannerImageCardView`,`BannerImageContentCardView` を`ImageOnlyCard`,`ImageOnlyCardView`,`ImageOnlyContentCardView` に改名。
    - バナーカードに使用されていたすべてのスタイルが画像のみのカードに更新されました。`banner` の文字があるキーはすべて`image_only` に置き換えてください。
    - デバイスのブランド情報が送信されるようになった。これをブロックしたい場合は、データ収集をブロックするを参照してください。
- [Flutter SDK 7.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブAndroidブリッジを[Braze Android SDK 26.1.1から27.0.](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701)1に更新。
    - Gradle 8 のサポートを追加しました。
- [Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `useUUIDAsDeviceId` コンフィギュレーションがデフォルトで有効になった。
        - 影響の詳細については、「[IDFVの収集-スウィフト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/swift_idfv/)」を参照のこと。
    - バナーコンテンツカードタイプと対応するUI要素は、`ImageOnly` に名前が変更されました。すべてのメンバー・メソッドとプロパティは変わらない。
        - `Braze.ContentCard.Banner` → `Braze.ContentCard.ImageOnly`
        - `BrazeContentCardUI.BannerCell` → `BrazeContentCardUI.ImageOnlyCell`
    - BrazeUIのテキストレイアウトロジックの一部をリファクタリングし、新しいBraze.ModalTextViewクラスを作成しました。
    - Feature Flagsメソッドの動作を更新。
        - `FeatureFlags.featureFlag(id:)` 存在しないIDに対してはnilを返すようになった。
        - `FeatureFlags.subscribeToUpdates(:)` は、リフレッシュ要求が成功または失敗で完了したときにコールバックをトリガします。
            - コールバックはまた、以前にキャッシュされたデータが存在する場合、最初のサブスクリプション時に即座にトリガーされます。
- [AppboyKit iOS SDK 4.6.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.6.0)
    - このリリースにはXcode`14.x` が必要です。
    - iOS 9とiOS 10のサポートを終了。
    - Carthage 経由でインポートする際、時代遅れの`.framework` アセットのサポートを削除し、最新の`.xcframework` アセットを使用するようにしました。
        - コマンド`carthage update --use-xcframeworks` を使用して、適切なBrazeアセットをインポートします。
        - `appboy_ios_sdk_full.json` 。 `appboy_ios_sdk.json`

## 2023年9月19日リリース

### クラウドデータ取り込みのためのBigQuery

サーバーレス・エンタープライズ・データウェアハウスである[BigQueryとの](https://cloud.google.com/bigquery)Cloud Data Ingestion統合を作成できるようになりました。詳細については、[Cloud Data Integestionの統合を]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=bigquery)参照してください。

### ブレイズデータ変換

[Brazeデータ変換では]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/)、外部プラットフォームからBrazeユーザープロファイルへのデータフローを自動化するためのWebhook統合を構築し、管理することができます。この新たに統合されたユーザーデータは、さらに洗練されたマーケティングのユースケースを可能にする。

### キャンバスでのコメント

[キャンバスのコメントは]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_comments/)、マーケティングチームがキャンバスの詳細を確認、議論、レビューするための素晴らしい共同スペースになります。キャンバスを作成する際、同僚からの追加フィードバックが必要な箇所を特定するために、コメントを作成・管理することができます。

### 配信センター

[配信可能性センターでは]({{site.baseurl}}/user_guide/data_and_analytics/analytics/deliverability_center)、Gmailポストマスターツールの使用をサポートすることで、送信されたメールのデータを追跡し、送信ドメインに関するデータを収集することで、メールのパフォーマンスに関するより詳細な洞察を提供します。 

メール配信はキャンペーン成功の中核です。BrazeダッシュボードのDeliverability Centerを使用すると、IPレピュテーションや配信エラーごとにドメインを表示し、メール配信に関する潜在的な問題を発見してトラブルシューティングすることができます。

### アプリ内メッセージのドラッグ＆ドロップ・エディター

これらの追加機能は、[アプリ内メッセージのドラッグ＆ドロップエディタに]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)追加されました：

- メッセージを削除しないテキストリンク
- プッシュプライマーを要求するボタンアクション
- カスタムコードエディタブロック

ドラッグ＆ドロップ・エディターで利用可能なすべての機能を利用するには、SDKを推奨SDKバージョンにアップデートしてください。

#### カスタムテンプレートの保存（早期アクセス）

アプリ内メッセージ用のドラッグ＆ドロップエディターでは、早期アクセス参加者は、エディターを終了した後に利用できる「**テンプレートとして保存**」ボタンを使って、カスタムアプリ内メッセージテンプレートを作成・保存できます。テンプレートとして保存する前に、まずキャンペーンを起動するか、下書きとして保存する必要があります。 

また、アプリ内メッセージテンプレートは、「**テンプレート**」>「**アプリ内メッセージテンプレート**」で作成・保存できます。

{% alert important %}
カスタム・テンプレートを保存する機能は、現在アーリーアクセス中です。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### アプリ内メッセージのダークモードを無効にする

開発者は、ユーザーのデバイスでダークモードがオンになっている場合、アプリ内メッセージにダークモードのスタイルが適用されないようにすることができます。この実装方法については、プラットフォーム別に以下のドキュメントを参照してください：

- [スウィフト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/#disabling-dark-mode)
- [Objective-C]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handling_in_app_display/#disabling-dark-mode)

### メッセージ・アーカイブ用の新しいフィールド

[メッセージアーカイブを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)使用すると、アーカイブまたはコンプライアンス目的でユーザーに送信されたメッセージのコピーをS3バケットに保存できます。メッセージが送信されるたびに、S3バケットに配信されるJSONペイロードに以下のフィールドが追加されました：

- `user_id`
- `campaign_name`
- `canvas_name`
- `canvas_step_name`

### 新リキッド名入れタグ

アプリ内メッセージでは、Liquid内で以下のアプリ属性を使用できます。値は、アプリがメッセージングを要求するために使用するSDK APIキーに基づいています：

- {% raw %}`{{app.${api_id}}}`{% endraw %}
- {% raw %}`{{app.${name}}}`{% endraw %}

詳しくは、[パーソナライズタグをサポート]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags#targeted-app-information)しましたをご覧ください。

### 新しいブレイズ・パートナーシップ

#### アンタボ・ロイヤリティ・クラウド - チャネル拡張

[Antavoと]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/antavo/)Brazeの統合により、ロイヤルティプログラム関連のデータを利用して、パーソナライズされたキャンペーンを構築し、顧客体験を向上させることができます。これはAntavoからBrazeへの一方向のデータ同期のみです。

#### Ketch - 顧客データ・プラットフォーム

Brazeと[Ketchの]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/ketch/)統合により、Ketchプリファレンスセンター内で顧客とのコミュニケーションプリファレンスをコントロールし、これらの変更を自動的にBrazeに反映させることができます。

#### レッドポイント - 顧客データ・プラットフォーム

Redpointは、完全に統合されたキャンペーン・オーケストレーション・プラットフォームをマーケティング担当者に提供するテクノロジー・プラットフォームである。Brazeと[Redpointの]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/redpoint/)統合により、RedpointのCDPデータに基づいてBrazeセグメントを作成できます。 

#### サイモンデータ - 顧客データプラットフォーム
 
Brazeと[Simon Dataの]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/simondata/)統合を使用して、洗練されたオーディエンスを作成し、Brazeに同期させることで、コードなしでリアルタイムにオーケストレーションを行うことができます。この統合により、Simonのキャンペーン優先順位付けやIDマッチング機能、複雑な集計サポートなどを最大限に活用し、Brazeのキャンペーンを下流に向上させることができます。

#### オファーフィット - ダイナミックコンテンツ

[OfferFitと]({{site.baseurl}}/partners/message_personalization/dynamic_content/offerfit/)Brazeの統合により、顧客データに基づいて、すべての顧客に適切なメッセージ、チャネル、タイミングを自動的に発見することができます。クロスセル、アップセル、再購入、リテンション、リニューアル、リファーラル、ウィンバックなどのビジネスゴールを設定し、特定された既存顧客に対してキャンペーンを最適化することができます。

### SDKアップデート

以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [Swift SDK 6.6.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#661)
- [Web SDK 4.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#490)
- [Android SDK 28.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2800)
    - SDK の最小バージョンを 21 (Lollipop) に更新しました。
    - Feature Flags関数が変更されました。
    - `Braze.getFeatureFlag(id)` は、機能フラグが存在しない場合はnullを返すようになった。
    - `Braze.subscribeToFeatureFlagsUpdates()` がコールバックされるのは、リフレッシュ要求が完了したときだけです。また、リフレッシュに失敗した場合は、キャッシュされた機能フラグとともに呼び出される。
        - アプリ起動時に即座にキャッシュ値が欲しい場合は、`Braze.getFeatureFlag(id)` 。
    - `DefaultInAppMessageViewWrapper.createButtonClickListener()` を`DefaultInAppMessageViewWrapper.createButtonClickListeners()` にリファクタリングした。
- [React Native SDK 7.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#700)
    - ネイティブAndroidブリッジを[Braze Android SDK 26.3.2から27.0.](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701)1に更新。
- [Cordova SDK 7.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2800)
    - ネイティブAndroidブリッジを[Braze Android SDK 26.3.2から27.0.](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701)1に更新。
- [Roku SDK 2.0.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md#200)
    - `getFeatureFlag` は、フラグが存在しない場合は無効を返す。
    - `BrazeTask` 機能フラグのリフレッシュが成功したとき、失敗したときを知るために、`BrazeFeatureFlagsUpdated` 。データ値は常に異なるとは限らない。

## 2023年8月22日リリース

## Shopifyカタログ 

Shopifyカタログでは、ShopifyストアからBrazeカタログに商品をインポートし、商品データを取り込むプロセスを自動化することで、メッセージのパーソナライゼーションを深めることができます。カート放棄、注文確認など、最新の商品詳細や情報を充実させることができます。

### 電子メールによるユーザーの統合

`/users/merge` エンドポイントを使用して、[ユーザーを電子メールでマージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merging-users-by-email)できるようになりました。 

{% alert important %}
電子メールによるユーザーのマージと、不一致の識別子による`/users/merge` の使用は、現在早期アクセス中である。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

## WhatsAppのベストプラクティス

WhatsAppメッセージを送信する前に、高い通話品質評価の維持、ブロックやレポートの回避、ユーザーのオプトイン/アウトなど、推奨される[ベストプラクティスを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/)ご参照ください。

### ドメインレピュテーション

配信可能性センターでは、迷惑メールフォルダに振り分けられるのを防ぐため、[ドメインのレピュテーションを]({{site.baseurl}}/user_guide/data_and_analytics/analytics/deliverability_center#domain-reputation)表示・監視できるようになりました。

### カスタマイズガイド 

開発者ポータルの再編成をご紹介できることを嬉しく思います。現在、[コンテンツ]({{site.baseurl}}/developer_guide/customization_guides/content_cards)カードをはじめとするSDKのカスタマイズオプションは、専用のカスタマイズガイドに集約されています。この変更により、詳細なインストラクションへのアクセスが効率化され、特定のニーズに合わせた体験がしやすくなります。

### キャンバスでのカード作成

Brazeが新しいコンテンツカードキャンペーンとキャンバスのステップについて、オーディエンスの適格性とパーソナライズを評価するタイミングは、カードが作成されるタイミングを指定することで選択できます。

{% alert important %}
キャンバスのステップでカードを作成するコントロールは、アーリーアクセスの段階にある。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### ワークスペースへのコピー

[ワークスペース間でキャンペーンをコピーすること]({{site.baseurl}}/copying_to_workspaces/)で、別のワークスペースにあるキャンペーンのコピーから始めることで、メッセージの構成でスタートダッシュを切ることができます。このコピーは、編集してローンチするまで下書きとして残り、成功したメッセージング戦略を維持・発展させるのに役立ちます。

{% alert important %}
ワークスペース間でのキャンペーンのコピーは、現在早期アクセス中です。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーまでお問い合わせください。
{% endalert %}

### 最大限にプッシュ通知

[Push Maxは]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/push_max/)、失敗したプッシュ通知を追跡し、ユーザーが受信する可能性が高いときにプッシュを再送信することで、Androidのプッシュ通知を増幅します。Push Maxと、この機能を使用して[中国OEMデバイスへの]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)Androidプッシュ通知の配信性を向上させる方法について説明します。

{% alert important %}
プッシュ・マックスは現在アーリーアクセス中。早期アクセスにご興味のある方は、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### SDKアップデート

以下のSDKアップデートがリリースされました。その他のアップデートは、対応するSDKの変更履歴をご確認ください。

- [Xamarin SDK 2.0.0-2.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Braze Android SDK 26.3.2を使用するためにAndroidバインディングを更新しました。
- [Flutter SDK 6.0.1](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブAndroidブリッジをBraze Android SDK 26.1.0から26.1.1に更新しました。
- [Android SDK 27.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 6.5.0-6.6.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - HTMLのアプリ内メッセージにおいて、カスタムイベントと購入のプロパティが常に`1` と`0` の値をそれぞれ`true` と`false` に変換してしまう問題を修正しました。これらのプロパティ値は、HTML内の元のフォームを尊重するようになります。
- [React Native SDK 6.0.0-6.0.2](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジをBraze Android SDK 26.3.1から26.3.2に更新しました。
- [Cordova SDK 6.0.0-6.0.1](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidバージョンをBraze Android SDK 26.3.1から26.3.2に更新しました。
- [Expo プラグイン 1.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/1.1.2/CHANGELOG.md)
- [ユニティ 4.3.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [セグメント Kotlin 1.4.1](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
- [セグメント-アンドロイド 15.0.1](https://github.com/Appboy/appboy-segment-android/blob/master/CHANGELOG.md)

<br><br>
