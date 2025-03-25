---
nav_title: リリースノート
article_title: リリースノート
page_order: 4
layout: dev_guide
guide_top_header: "リリースノート"
guide_top_text: "ここには、Brazeプラットフォームのすべてのアップデートが掲載されており、<a href='/docs/help/release_notes/#most-recent'>最新のプラットフォームアップデートは</a>以下の通り。"
page_type: landing
search_rank: 1
description: "このランディングページには、Brazeのリリースノートが掲載されている。ここでは、BrazeプラットフォームとSDKのすべてのアップデートと、非推奨機能のリストを見ることができる。"

guide_featured_title: "リリースノート"
guide_featured_list:
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 非推奨
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK 変更ログ
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# 最新のBrazeリリースノート {#most-recent}

> Brazeは、主要な製品リリースに合わせて、月ごとに製品更新の情報を公開しています。ただし、製品は、週ごとにさまざまな改良が加えられて更新です。
> <br>
> <br>
> このセクションに記載されているアップデートの詳細については、アカウント・マネージャーに問い合わせるか、[サポート・チケットを発行する]({{site.baseurl}}/help/support/)。また、[SDK Changelogsで]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/)、毎月のSDKのリリース、アップデート、改良に関する詳細情報を確認することができる。

## 2024年12月10日リリース

### IPアドレスによるSDKユーザーのロケーション

2024年11月26日現在、Braze は最初の SDK セッションの開始時から IP アドレスを使用して、位置情報に基づいて特定された国からユーザーのロケーションを検出します。Braze は IP アドレスを使用して、SDK を介して作成されたユーザープロファイルに国の値を設定します。その IP ベースの国の設定は、最初のセッション中とその後に使用できます。詳しくは[位置情報の追跡]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/)を参照してください。

### Elevated アクセス設定

[Elevated Accessは]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access)、Brazeダッシュボードで機密性の高いアクションを行う際のセキュリティをさらに強化する。アクティブユーザーである場合、ユーザーはセグメンテーションをエクスポートしたりAPIキーを表示したりする前に、アカウントを再確認する必要がある。Elevated アクセスを使用するには、[**設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[オン] に切り替えます。

### 個人を特定できる情報 (PII) の閲覧権限

管理者の場合は、Liquid 変数を使用してユーザープロパティにアクセスするメッセージプレビューで、[ユーザーがダッシュボードで会社によって定義された PII を表示できるようにする]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions)ことができます。 

ワークスペースでは、ダッシュボードであなたの会社が定義したPIIをユーザーが閲覧できるようにしたり、ユーザープロファイルは閲覧できるが、あなたの会社がPIIとして特定したフィールドを編集したりすることができる。

### データの柔軟性

#### データレイク・スキーマ

以下のスキーマが生のテーブルスキーマに追加された：
- `USERS_CANVASSTEP_PROGRESSION_SHARED`:キャンバス内のユーザーの進行イベント
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`:どのランダムバケット番号が現在および以前のグローバルコントロールグループにあるかを識別する
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`:ユーザーがフィーチャーフラグを閲覧した際のインプレッションイベント

#### アカウントベースのセグメンテーション

[企業間（B2B）のアカウントベースのセグメンテーションは]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/)、B2Bデータモデルの設定によって、2つの方法がある：

- ビジネス・オブジェクトにカタログを使う場合
- ビジネス・オブジェクトに接続ソースを使用する場合

#### セグメンテーションフィルター

セグメンテーションフィルターの全リストとその説明は、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)を参照してください。

##### で作成されたユーザープロファイル。

ユーザープロファイルの作成時期でユーザーをセグメンテーションする。ユーザーがCSVまたはAPIによって追加された場合、このフィルターは追加された日付を反映する。ユーザーがCSVまたはAPIによって追加されておらず、SDKによって最初のセッションがトラッキングされている場合、このフィルターはその最初のセッションの日付を反映する。

##### 電話番号を送信する

e.164 電話番号フィールドでユーザーをセグメンテーションする。このフィルターで正規表現を使えば、特定の国コードを持つ電話番号でセグメンテーションできる。

### 新しいBrazeのパートナーシップ

#### Narvar - e コマース

Brazeと[Narvar](https://corp.narvar.com/) の統合により、ブランドは Narvar の通知イベントを活用して Braze から直接メッセージをトリガーし、顧客にタイムリーな更新情報を提供することができます。

#### Zeotap for Currents - 顧客データプラットフォーム

Braze と[ Zeotap](https://zeotap.com/) の統合により、Zeotap の顧客セグメントを Braze のユーザープロファイルに同期することで、キャンペーンの規模とリーチを拡大できます。[Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) では、データを Zeotap に接続し、グローススタック全体で実用的なデータにすることもできます。

#### 通知 - ダイナミックなコンテンツ

Braze と[Notifyの](https://notifyai.io/)統合により、マーケターは様々なプラットフォームで効果的にエンゲージメントを促進できるようになります。従来のマーケティング手法に依存する代わりに、Braze API によってトリガーされたキャンペーンでは、Notify の機能を活用して、メール、SMS、プッシュ通知などを含む複数のチャネルを通じてパーソナライズされたメッセージングを配信できます。

#### Contentful - ダイナミックなコンテンツ

Braze と [Contentful](https://www.contentful.com/) の統合により、コネクテッドコンテンツを動的に使用して Contentful から Braze キャンペーンにコンテンツを取り込むことができます。

#### アウトグロウ - リード獲得 

Braze と[Outgrow](https://outgrow.co/) の統合により、ユーザーデータを Outgrow から Braze に自動的に転送することができ、高度にパーソナライズされたターゲットキャンペーンが可能になります。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Web SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - ネイティブ iOS ブリッジを [Braze Swift SDK 10.3.1から11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
    - ネイティブ Android ブリッジを [Braze Android SDK 32.1.0から 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)にアップデートします。
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## 2024年11月12日リリース
 
### データの柔軟性
 
#### `/users/track` の制限速度

[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)の制限速度が3,000/3秒に更新されました。
 
### 創造性を引き出す

#### キャンバスのユースケース

Braze キャンバスを活用するさまざまな方法を紹介するユースケースをまとめました。インスピレーションをお探しなら、以下からユースケースを選んで始めよう。

- [カート放棄]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [再入荷]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [機能採用]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [離脱ユーザー]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [オンボーディング]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [購入後のフィードバック]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### 強力なチャネル

#### LINE

{% multi_lang_include release_type.md release="一般的な可用性" %}

BrazeのLINE統合が一般的に利用可能になった！LINE は、月間アクティブユーザー数が9500万 を超える国内で最も人気のあるメッセージングアプリです。メッセージングに加え、LINEはソーシャルメディア、ゲーム、ショッピング、決済の「オールインワン」プラットフォームをユーザーに提供している。

まずは、[LINEのドキュメント]({{site.baseurl}}/user_guide/message_building_by_channel/line/)をご覧ください。
 
#### LinkedIn オーディエンス・シンク

{% multi_lang_include release_type.md release="ベータ" %}

LinkedInを[Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/) で利用できるようになりました。[Braze Audience Syncは]({{site.baseurl}}/partners/canvas_steps/)、トップクラスのソーシャルテクノロジーや広告テクノロジーの多くにキャンペーンのリーチを広げるのに役立つツールだ。ベータ版に参加するには、Brazeサクセスマネージャーに連絡すること。
 
### 開発者ガイドの改善
 
現在、[Braze 開発者ガイド]({{site.baseurl}}/developer_guide/home/)を大幅に改善しています。最初のステップとして、ナビゲーションを簡素化し、入れ子になっているセクションの数を減らした。 

|前|その後|
|------|-----|
|!["The old navigation for the Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["Braze開発者ガイドの新しいナビゲーション"]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### 新しいBrazeのパートナーシップ
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/) は世界有数のポストカードアプリで、ダイレクトメールのキャンペーンを簡単に実行でき、シームレスで収益性の高い方法で顧客とつながることができます。開始するには、[MyPostcard と Braze の統合]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/)を参照してください。
 
### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Expo プラグイン 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - このバージョンには、Braze React Native SDK の13.1.0 が必要です。
    - BrazeReactUtils.populateInitialUrl の iOS BrazeAppDelegate メソッド呼び出しを BrazeReactUtils.populateInitialPayload に置き換えます。
        - この更新により、アプリケーションが終了状態のときに通知をクリックしても、プッシュ通知開封イベントがトリガーされない問題が解決された。
        - この更新を完全に活用するには、JavaScriptコード内でBraze.getInitialURL の呼び出しをすべてBraze.getInitialPushPayload に置き換える。初期URLは、初期プッシュペイロードのurlプロパティからアクセスできるようになった。
- [Braze Segment Swift プラグイン 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - 11.1.1+ SemVer 仕様のリリースを必要とするように Braze Swift SDK バインディングを更新します。
    - これにより、Braze SDK の11.1.1から12.0.0までのあらゆるバージョンとの互換性が確保されます (12.0.0は含まれません)。
    - 破壊的な変更の可能性に関する詳細については、11.1.1の変更ログエントリを参照してください。

## 2024年10月15日リリース

### データの柔軟性

#### キャンペーンとキャンバス

キャンペーンとキャンバスの作成中に、デフォルトの推定値ではなく、ターゲットオーディエンスの到達可能なユーザーの正確な数を計算するには、[[正確な統計値を計算する]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size)] を選択します。

#### API Androidオブジェクト

[`android_priority` パラメーターは]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details)、FCM 送信者の優先順位を指定するために、「normal」または「high」のいずれかの値を受け入れます。デフォルトでは、通知メッセージは高い優先度で送信され、データメッセージは通常の優先度で送信される。

値の違いが配信に与える影響の詳細については、[Android メッセージの優先度](https://firebase.google.com/docs/cloud-messaging/android/message-priority/)を参照してください。

#### SDK

[Braze SDK の組み込みデバッガー]({{site.baseurl}}/developer_guide/platform_wide/debugging/)を使用すると、アプリで詳細ログを有効にすることなく、SDK を使用したチャネルの問題をトラブルシューティングできます。

#### ライブアクティビティ

Swift Live Activities の[よくある質問]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/)を更新し、いくつかの新しい質問と回答を追加しました。

#### カスタムイベント

配列またはオブジェクト値を含む[イベントプロパティオブジェクトは]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)、最大100KBのイベントプロパティペイロードを持つことができるようになった。

#### ランダムバケット番号

ABテストやキャンペーンで特定のユーザーグループをターゲットにするために、[ランダムなバケット番号を使用してランダムオーディエンスの再エントリーを]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers)使用する。

#### セグメントエクステンション

[セグメントエクステンションを定期的なスケジュールで更新する]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh)には、エクステンションを更新する頻度 (毎日、毎週または毎月) と、更新を実行する特定の時間を選択します。

### 強力なチャネル

#### SMS

Googleアナリティクスなどのサードパーティーの分析ツールでキャンペーンのパフォーマンスを追跡できるように、SMSメッセージでUTMパラメータを使用する方法を示すために、[UTMパラメータの追加を]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening)追加した。

#### ランディングページ

ブランドのランディングページ URL をカスタマイズするには、[独自のドメインを Braze ワークスペースに接続します]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/)。

#### LINE と Braze

{% multi_lang_include release_type.md release="ベータ" %}

新しいドキュメントを追加した：

- [LINE メッセージタイプ]({{site.baseurl}}/line/create/message_types/)では、作成可能な LINE メッセージタイプについて説明します。これには、側面と制限事項が含まれ、LINE ベータコレクションの一部です。
- [ユーザーアカウント連携により]({{site.baseurl}}/line/line_setup/#user-account-linking)、ユーザーはLINEアカウントとアプリのユーザーアカウントを連携させることができる。その後、Braze で {% raw %}`{{line_id}}`{% endraw %} などの Liquid を使用して、ユーザーの LINE ID を Web サイトまたはアプリに渡すユーザーのためにパーソナライズされた URL を作成します。渡された LINE ID は、既知のユーザーに関連付けることができます。

#### WhatsAppとBraze

[WhatsAppビジネスアカウント(WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup)を複数のビジネスソリューションプロバイダーと共有できるようになった。

### 新しいBrazeのパートナーシップ

#### Future Anthem - ダイナミックコンテンツ

Braze と [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) のパートナーシップでは、Amplifier AI を活用して、コンテンツのパーソナライゼーション、リアルタイムエクスペリエンス、ダイナミックなオーディエンスを提供します。Amplifier AIは、スポーツ、カジノ、宝くじにまたがって機能し、好きなゲーム、エンゲージメントスコア、予想される次のベットなど、業界特有のプレイヤー属性でBrazeのプレイヤープロファイルを強化することができる。

### 設定

#### 識別子フィールドレベルの暗号化

{% multi_lang_include release_type.md release="一般的な可用性" %}

[識別子フィールドレベルの暗号化]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/)を使用すると、AWS Key Management Service (KMS) を使用してメールアドレスをシームレスに暗号化し、Braze で共有される個人を特定できる情報 (PII) を最小限に抑えることができます。暗号化は機密データを暗号文に置き換えます。これは読み取れない暗号化された情報です。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - [Swift 6 の厳密な並行性チェック](https://developer.apple.com/documentation/swift/adoptingswift6)のサポートを追加
        - 関連するパブリックBrazeクラスとデータ型は、`Sendable` プロトコルに準拠するようになり、同時実行コンテキストにまたがって安全に使用できるようになった。
        - メインスレッド専用 API が `@MainActor` 属性でマークされるようになりました。
        - コンパイラによって生成される警告の数を最小限に抑えながら、これらの機能を利用するには、Xcode 16.0 以降を使用することをお勧めします。以前のバージョンの Xcode も使用できますが、一部の機能では警告が発生する可能性があります。
    - プッシュ通知サポートを手動で統合する場合、警告を防ぐために`@preconcurrency` 属性を使用するように`UNUserNotificationCenterDelegate` 準拠を更新する必要があるかもしれない。
        - `@preconcurrency` 属性をプロトコル適合に適用することは、Xcode 16.0 以降でのみ可能です。サンプル・インテグレーション・コードは[こちら](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual)。
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - ネイティブ Android バージョンのバインディングを [Braze Android SDK 31.1.0から32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
    - ネイティブ iOS バージョンのバインディングを [Braze Swift SDK 10.3.0から11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Kotlin を1.8から Kotlin 2.0 に更新。
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## 2024年9月17日リリース

### データの柔軟性

#### Braze クラウドデータインジェスト for S3

[S3 用のクラウドデータ取り込み (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) を使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze と直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。

#### 1 か月あたりのアクティブユーザー数 CY 24-25

1 か月あたりのアクティブユーザー数-CY 24-25 を購入したお客様の場合、Braze は `/users/track` エンドポイントでさまざまなレート制限を管理します。詳細については、[POST を参照してください。ユーザー ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) を追跡します。 

### 創造性を引き出す

#### リキッドを含むカタログアイテムのテンプレート化

{% multi_lang_include release_type.md release="早期アクセス" %}

Liquid タグで `:rerender` フラグを使用して[カタログアイテムの Liquid コンテンツをレンダリングします]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid)。例えば、次のような Liquid コンテンツをレンダリングするとします。

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

次のように表示されます。

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### 強力なチャネル

#### WhatsApp レスポンスメッセージ

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザーからのインバウンド WhatsApp メッセージに返信するために、[応答メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages)を使うことができます。これらのメッセージは、作成中に Braze のアプリ内で作成され、いつでも編集できます。Liquid を使えば、応答メッセージの言語を適切なユーザーに合わせることができます。

#### キャンバステンプレート

{% multi_lang_include release_type.md release="一般的な可用性" %}

[キャンバステンプレート]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/)を作成し、キャンバス全体で特定の目標に合わせて簡単にカスタマイズできる一貫したフレームワークを作成することで、メッセージングを絞り込みます。

#### ランディングページ

{% multi_lang_include release_type.md release="ベータ" %}

Brazeの[ランディングページは]({{site.baseurl}}/user_guide/engagement_tools/landing_pages)、ユーザー獲得とエンゲージメント戦略を推進できる独立したウェブページである。

#### 前回閲覧時からの変更点

[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed)、キャンペーン、[セグメンテーションの]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed)更新回数は、各概要ページ（[メールキャンペーンの]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)概要ページなど）の「*Changes Since Last Viewed（最終閲覧からの変更*）」で確認できる。 

#### Webhookリクエストとコネクテッドコンテンツリクエストのトラブルシューティング 

[この記事では]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors)、Webhookとコネクテッドコンテンツのエラーコードのトラブルシューティング方法について、エラーの内容や解決ステップを紹介する。

### 新しいBrazeのパートナーシップ

#### Inbox Monster - 分析

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) は、企業ブランドがすべての送信を成功させるためのインボックスシグナルプラットフォームです。これは、最新の顧客関係管理 (CRM) チームを強化し、送信の不安を解消する、配信可能性、クリエイティブなレンダリング、SMS 監視のための統合ソリューションスイートです。

#### SessionM - ロイヤルティ

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) は、キャンペーン管理機能とロイヤルティ管理ソリューションを提供するカスタマーエンゲージメントとロイヤリティプラットフォームで、マーケターがターゲットを絞ったアウトリーチを推進してエンゲージメントと収益性を向上させるのを支援します。

### AI と ML のオートメーション

#### トレンドアイテムのおすすめ

「AI でパーソナライズ」されたモデルに加えて、[AI によるアイテムのおすすめ]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending)機能には、最近のユーザーインタラクションで最もポジティブな勢いのあったアイテムを勧める「トレンド」のレコメンデーションモデルも含まれています。

### 設定

#### 役割

{% multi_lang_include release_type.md release="一般的な可用性" %}

[ロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)を使用すると、ワークスペースのアクセスコントロールと個別のカスタムアクセス許可をバンドルすることで、より多くの構成が可能になります。これは、1 つのダッシュボードに多数のブランドまたは地域ワークスペースがある場合に特に便利です。ロールを使用して、適切なワークスペースにダッシュボード ユーザーを追加し、関連付けられた権限を直接付与することができます。 

#### セキュリティ・イベント・レポート

ダウンロードしたセキュリティ・レポート・イベントに表示される可能性のある[セキュリティ・イベントの]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report)完全なリストを追加した。

#### メッセージング利用レポート

{% multi_lang_include release_type.md release="早期アクセス" %}

[メッセージ使用状況ダッシュボードでは]({{site.baseurl}}/message_usage/)、SMSやWhatsAppのクレジット使用状況をセルフサービスでインサイトでき、契約割当てと比較した過去と現在の使用状況を総合的に確認できる。これらのインサイトは、混乱を減らし、超過料金のリスクを防ぐための調整に役立つ。

### SDK

#### Braze Swift SDKの初期化の遅延

[遅延初期化]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/)を設定して、プッシュ通知の処理が確実に保持されるようにしながら、Braze Swift SDK を非同期的に初期化します。これは、サーバーから構成データを取得したり、ユーザーの同意を待ったりするなど、SDK を初期化する前に他のサービスを設定する必要がある場合に役立ちます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - このバージョンでは、Cordova Android 13.0.0 が必要になりました。
    - プロジェクトの依存要件の完全なリストについては、[Cordova のリリース発表](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html)を参照してください。-ネイティブ Android ブリッジを[Braze Android SDK 30.3.0から32.1.0 ](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。
    - ネイティブ iOS ブリッジを [Braze Swift SDK 9.2.0から10.1.0に](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - ネイティブ Android ブリッジを [Braze Android SDK 30.3.0から32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。
    - ネイティブ iOS ブリッジを [Braze Swift SDK 9.0.0 から10.1.0に](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
- [Braze Segment Swift プラグイン 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - `10.2.0+` SemVer 仕様のリリースを必要とするように Braze Swift SDK バインディングを更新します。
        - これにより、Braze SDK の`10.2.0`から`11.0.0`までのあらゆるバージョンとの互換性が確保されます (11.0.0は含まれません)。
        - 破壊的な変更の可能性に関する詳細については、[`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000)の変更ログエントリを参照してください。
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - ネイティブ Android ブリッジを [Braze Android SDK 30.4.0から32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)にアップデートします。
        - 呼び出された後に外部サブスクリプション (`subscribeToContentCards()` など) を保持するように、Android の `wipeData()` の動作を変更します。
    - ネイティブ iOS ブリッジを [Braze Swift SDK9.0.0から10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## 2024年8月20日リリース

### 新しいユースケース

#### カタログ

カタログには、任意のタイプのデータを取り込むことができます。通常、データは製品、割引、プロモーション、イベントなど、提供するアイテムに関するメタデータです。[ユースケース]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)を読んで、このデータを使用して、関連性の高いメッセージングでユーザーをターゲットにする方法を学んでください。

#### Intelligence Suite

Intelligence Suite は、ユーザー履歴やキャンペーン、キャンバスのパフォーマンスを分析し、エンゲージメント、視聴率、コンバージョンを高めるための自動調整を行う強力な機能を備えています。これらの機能がさまざまな業界にどのようなメリットをもたらすかについては、[ユースケースを]({{site.baseurl}}/user_guide/brazeai/intelligence)ご覧いただきたい。

### ホームダッシュボード更新

Brazeダッシュボードでは、最近編集したり作成したファイルに簡単にアクセスでき、[中断したところから再開]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off)できる。このセクションは、Braze ダッシュボードの [**ホーム**] ページの上部に表示されます。

### データの柔軟性

#### データ変換テンプレートと新しい送信先

{% multi_lang_include release_type.md release="一般的な可用性" %}

デフォルトのコードではなく、特定の外部プラットフォームで作業を開始できるように、専用の[テンプレートライブラリ]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation)を使用してデータ変換を構築します。**POST を選択できるようになりました。ソースプラットフォームから Webhook を変換してユーザーに即時メッセージを送信するには、宛先として API のみ**を使用してメッセージを送信します。

#### ユーザーを一括マージする

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザープロファイルの重複が発生した場合、これらのユーザーを[一括マージする]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)ことで、ユーザーデータの効率化を図ることができる。

#### カスタム属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

[カスタム属性のリストを CSV ファイルとしてエクスポートする]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data)には、**カスタム属性**ページで [**すべてエクスポート**] を選択します。CSVファイルが生成され、ダウンロードリンクがEメールで送信される。

#### Currents の IP 許可リスト

Braze は、リストされた IP から Currents データを送信します。これは、[許可リスト]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents)にオプトインされているすべての API キーにダイナミックに自動で追加されます。

### 強力なチャネル

#### 新しいセグメンテーション・ビルダー体験

{% multi_lang_include release_type.md release="一般的な可用性" %}

[最新のエクスペリエンス]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)を使用してセグメントを構築します。セグメントは、データの変更に応じてリアルタイムで更新されます。また、ターゲットおよびメッセージングの目的で必要な数のセグメントを作成できます。

#### セグメント別指標

[クエリビルダーの]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/)レポートテンプレートを使用して、キャンペーン、キャンバス、バリアント、ステップのパフォーマンス指標をセグメント別に分類する。

#### 電話番号の取得

WhatsApp メッセージングチャネルを使用するには、[Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) または [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) の要件を満たす電話番号が必要です。 

電話番号は自分で取得する必要があります。Brazeは番号を提供しません。ビジネス電話プロバイダーを通じて物理的な電話をSIMカード付きで購入するか、当社のパートナーの1つを使用することができます。Twilio または Infoblip。**Twilio または Infobip のアカウントを持っていなければなりません。これは Braze を通じて行うことはできません。**

### 新しいBrazeのパートナーシップ

#### Zendesk Chat - インスタントチャット

Braze と [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) の統合では、各プラットフォームの Webhook を使用して双方向の SMS 会話を設定します。ユーザーがサポートを要請すると、Zendeskにチケットが作成される。エージェントのレスポンシブは、APIトリガーのSMSキャンペーンを通じてBrazeに転送され、ユーザーの返信はZendeskに送り返される。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Braze でプッシュイベントをサブスクライブするときに、次の変更が行われました。[`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - `update` の終了は、デフォルトで「プッシュ開封」イベントと「プッシュ受信」イベントの両方によってトリガーされるようになりました。これまでは、「プッシュ開封」イベントによってのみトリガーされていました。
            - 引き続き「プッシュ開封」イベントのみをサブスクライブするには、パラメーター `payloadTypes` に `[.opened]` を渡します。もしくは、`Braze.Notifications.Payload` からの `type` が .`.opened` であることを確認するように、`update` クロージャを実装してください。
        - `content-available: true` を含むプッシュ通知を受信した場合、[`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) は `.opened` の代わりに `.received` になります。
    - 次の非推奨 API を使用不可としてマークします。
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - 非推奨のAPIを削除する：
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - 非推奨の`BrazeLocation` クラスを削除し、`BrazeLocationProvider` を採用した。
- [Xamarin SDKバージョン6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOS および Android のバインディングに対して、.NET 8.0 のサポートが追加されました。これは、.NET 7.0がサポート終了となったためです。
        - これにより、.NET 7.0のサポートはなくなった。
    - Android バインドを [Braze Android 30.4.0 から32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。
    - iOSバインディングを [Braze Swift SDK 9.0.0から10.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
        - プッシュ通知イベントをサブスクライブすると、「プッシュ開封」イベントに対してのみではなく、「プッシュ受信」と「プッシュ開封」の両方に対して iOS でサブスクリプションがトリガーされます。
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - ネイティブ iOS バージョンのバインディングを [Braze Swift SDK 9.0.0から10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
        - プッシュ通知イベントをサブスクライブすると、「`push_opened`」イベントに対してのみではなく、「`push_received`」と「`push_opened`」の両方に対して iOS でサブスクリプションがトリガーされます。

## 2024年7月23日リリース

### Braze Docsのアップデート

#### Diátaxis と Braze Docs

私たちは、[Diátaxis](https://diataxis.fr/)と呼ばれる枠組みを使ってドキュメントを標準化しています。ライターやコントリビューターがこの新しいフレームワークに適合するコンテンツを作成できるよう、[各コンテンツタイプのテンプレートを]({{site.baseurl}}/contributing/content_types)作成した。

#### Braze Docs の新しいプルリクエストテンプレート

私たちは、[Braze Docsに貢献する]({{site.baseurl}}/contributing/home/)のがより簡単で混乱しないように、プルリクエスト（PR）テンプレートを改善するために時間をかけた。まだ改善の余地があると思われる場合は、PR を開封するか、[問題を送信](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)してください。すべてが簡単になります。
 
### データの柔軟性

#### カスタム・イベントと属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

カスタムイベントやカスタム属性をエクスポートする際に [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes)と [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data)エンドポイントを使う。

#### ユーザーの新しい Currents 権限

ユーザーには2つの新しい権限設定があります。[**Currents 統合を表示する**] と [**Currents 統合を編集する**] です。[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)の詳細については、こちらを参照してください。。 

#### Snowflake データリテンションポリシーの更新
 
2024年8月27日より、個人を特定できる情報 (PII) は、作成から2年を超えたすべての Snowflake Secure Data Sharing イベントデータから削除されます。Snowflake を使用する場合、完全なイベントデータを環境に保持するには、リテンションポリシーが適用される前に Snowflake アカウントにコピーを保存します。[Snowflakeデータリテンション]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)についての詳細をご覧ください。
 
### 創造性を引き出す

#### 複数ページのアプリ内メッセージ

{% multi_lang_include release_type.md release="一般的な可用性" %}

アプリ内メッセージにページを追加することで、オンボーディングフローやウェルカムジャーニーのような連続したフローでユーザーを誘導することができる。詳細については、[ドラッグアンドドロップによるアプリ内メッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)を参照してください。

#### Liquid でのリンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Liquidを使ってURLをパーソナライズ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening)し、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルー率分析を収集する。試してみるには、[リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)を参照してください。

#### カタログのAPI例

配列フィールドを使った`/catalogs` エンドポイントの例を追加した。例を見るには、以下をチェックしてほしい：

- [複数のカタログ項目を編集]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [複数のカタログ項目を作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [カタログアイテムを更新]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [カタログアイテムを編集]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [カタログアイテムを作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [カタログアイテムを更新]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [カタログを作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### 強力なチャネル

### 複数のWhatsAppビジネスアカウント

{% multi_lang_include release_type.md release="一般的な可用性" %}

各ワークスペースに複数のWhatsApp Businessアカウントとサブスクリプショングループ（および電話番号）を追加できるようになった。詳しくは、[複数のWhatsApp取引先]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups)を参照してください。 

#### SMSの地理的権限

SMS Geographic Permissionsは、SMSメッセージを送信できる国をコントロールすることで、セキュリティを強化し、不正なSMSトラフィックから保護する。SMSメッセージが承認された地域にのみ送信されるように、国の許可リストを指定する方法については、[SMS国の許可リストを設定するを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist)参照のこと。

#### LINE と Braze

{% multi_lang_include release_type.md release="ベータ" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) は、月間アクティブユーザー数が9500万 を超える国内で最も人気のあるメッセージング アプリです。LINE アカウントを Braze と統合することで、ゼロパーティおよびファーストパーティの顧客データを活用し、顧客の嗜好、行動、クロスチャネルのインタラクションに基づいて、適切な顧客に魅力的な LINE メッセージを送信できます。開始するには、[LINE]({{site.baseurl}}/line) を参照してください。

#### Shopify:値下げ、再入荷商品

{% multi_lang_include release_type.md release="早期アクセス" %}

Shopifyでは、[値下げや]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) [再入荷商品の]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications)カスタム通知を作成できるようになった。
 
### AI と ML のオートメーション
 
#### 重複ユーザーのルールベースのマージ

以前は、Braze で重複するユーザーを個別または一括で検索してマージすることができました。これで、重複がどのように解決されるかをコントロールするためのルールを作成できるようになりました。そのため、最も関連性の高いユーザーが保持されます。詳細については、[ルールベースのマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)を参照してください。

#### AI Liquidアシスタント

{% multi_lang_include release_type.md release="ベータ" %}

AI Liquid アシスタントは BrazeAI <sup>TM</sup> を搭載したチャットアシスタントであり、メッセージコンテンツをパーソナライズするために必要な Liquid を生成する場合に役立ちます。テンプレートからの Liquid の生成、パーソナライズされた Liquid の提案の受け取り、および BrazeAI<sup>TM</sup> のサポートを使用した既存の Liquid の最適化を実行できます。AI Liquid アシスタントには、使用されている Liquid を説明する注釈も用意されているため、Liquid の理解を深めたり、自作方法を学んだりできます。

開始するには、「[AI Liquid アシスタント]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid)」を参照してください。
 
### SDK
 
#### Android SDKのログ

[Braze Android SDKのログ記録文書]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging)を見直したので、あなたのアプリで読みやすく、使いやすいです。また、各ログレベルの説明も追加した。

#### iOS SDKのフォアグラウンドプッシュ通知s

Braze iOS SDKの `subscribeToUpdates` メソッドで、フォアグラウンドプッシュ通知を受信したかどうかを検出できるようになりました。詳しくは、[iOS プッシュ通知統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)を参照してください。
 
#### Xamarinのドキュメントを更新する
 
[バージョン4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0)以降、Braze Xamarin SDK で Swift SDK バインディングが使用されるため、コードスニペットと参考資料が更新されました。また、読みやすく、理解しやすいようにセクションを再構成した。確認するには、[Xamarin ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup)を参照してください。

#### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Swift SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [Web SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - 5.2.0で導入されたリグレッションにより、外部スクリプトが同期的に読み込まれた場合にHTMLアプリ内メッセージが正しくレンダリングされないことがあった問題を修正した。
- [Web SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## 2024年6月25日リリース

### 日本語ドキュメント

Braze Docsが日本語に対応した！

![日本語インターフェースを表示するBraze Docsサイト]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### データの柔軟性

#### APIトリガーキャンペーンの添付ファイル

{% multi_lang_include release_type.md release="一般的な可用性" %}

[`/campaigns/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)で添付ファイルがサポートされるようになりました (`/messages/send` エンドポイントでメールの添付ファイルがサポートされるのと同様)。 

#### データウェアハウスの追加サポート

{% multi_lang_include release_type.md release="早期アクセス" %}

Braze [クラウドデータ取り込み (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) で、BigQuery、Databricks、Redshift、Snowflake がサポートされるようになりました。

#### WhatsAppの電話番号移行

Meta の埋め込みサインアップを使用して、WhatsApp Business アカウント間で WhatsApp の電話番号を移行します。[WhatsApp電話番号マイグレーション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration)について詳しくお読みください。
 
### 創造性を引き出す

#### デバイス別エンゲージメント

{% multi_lang_include release_type.md release="一般的な可用性" %}

新レポート「**Engagement by Device**」は、ユーザーがどのデバイスを使ってメールに参加しているのかがわかる。このデータは、モバイル、デスクトップ、タブレット、および他のデバイスタイプのメールエンゲージメントを追跡します。[レポートと電子メールパフォーマンスダッシュボード]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard) について詳しく説明します。

#### キャンバスフローのWhatsAppとSMSリキッドプロパティ

{% multi_lang_include release_type.md release="一般的な可用性" %}

[WhatsAppおよびSMS Liquidプロパティーのサポートがキャンバスフロー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)に追加されました。アクションパスステップに [SMS インバウンドメッセージを送信しました] または [WhatsApp インバウンドメッセージを送信しました] トリガーが含まれている場合、後続のキャンバスステップに SMS または WhatsApp Liquid プロパティを含めることができるようになりました。これは、キャンバスフローでのイベントプロパティの動作を反映したものです。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。
 
#### 繰り返されるキャンバスのパーソナライズされたパス

{% multi_lang_include release_type.md release="早期アクセス" %}

キャンバスのパーソナライズドパスでは、コンバージョンの可能性に基づいて、個々のユーザーに対してキャンバスのジャーニーの任意のポイントをパーソナライズすることができる。定期的なキャンバスでパーソナライズされたパスを使用できるようになりました。詳細については、[Personalized Variants]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths)を参照してください。

#### セグメントのトラブルシューティング

セグメントを使うか？以下は、[トラブルシューティングの手順と留意点]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting)である。

#### リキッドハイライト

アクセシビリティ・ガイドラインをより良くサポートするために、[Liquidが使用する色分けを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)改善した。

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### 強力なチャネル

#### SMS 地理的許可

{% multi_lang_include release_type.md release="早期アクセス" %}

SMSの地理的許可は、あなたがSMSメッセージを送信することができる国の制御を強制することにより、セキュリティを強化し、詐欺的なSMSトラフィックから保護する。管理者は、承認された地域にのみSMSメッセージが送信されるように、国の許可リストを指定できるようになった。詳細については、[SMS Geographic Permissions]({{site.baseurl}}/sms_geographic_permissions)を参照してください。 

![最も一般的な国が一番上に表示される "Country allowlist "ドロップダウン。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### SMS/MMSのベストプラクティス

オプトアウト監視やトラフィックポンプの推奨など、[Brazeを使ったSMS/MMSのベストプラクティスについて]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices)詳しく知る。 

#### プッシュの配信停止をトラッキングする

プッシュ配信の停止を追跡するためのヒントについては、新しい[ヘルプ記事を]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)チェックしよう。

#### Shopify `checkout.liquid` 廃止

Shopify `checkout.liquid` は、2024年8月に非推奨になり、2025年8月に終了することにご注意ください。この変化に対する Braze の対応については、[こちら]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout)をご覧ください。 

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - 将来のバージョンで削除される既存のフィーチャーフラグ API を非推奨にします。
        - `Braze.FeatureFlag.jsonStringProperty(key:)` は非推奨になりました。
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` は非推奨になり、`Braze.FeatureFlag.jsonProperty(key:)` に置き換えられした。
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo プラグイン 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOSドキュメント

数か月前、[tvOS コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos)と[アプリ内メッセージング]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos)の記事は誤って非推奨になりました。これらのドキュメントは現在、Braze DocsのSwiftセクションで再公開されている。

{% alert note %}
Braze Docs の[貢献者]({{site.baseurl}}/contributing/home)は、サイトが Ruby 3.3.0で実行されるようになったことを確認する必要があります。必要に応じてRubyのバージョンをアップグレードしてほしい。
{% endalert %}

## 2024年5月28日リリース

### ドキュメントサイトの視覚的な更新

ドキュメンテーションのウェブサイトが新しくなったことにお気づきだろうか！新しく生き生きとしたBrazeブランドアイデンティティを反映するように改良しました。新ブランドの舞台裏については、[Unveiling Our New Brandをご覧いただきたい：Braze クリエイティブディレクター Greg Erdelyi との会話](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi)。

### ポルトガル語とスペイン語をサポート

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeは現在、ポルトガル語とスペイン語に対応している。Braze ダッシュボード アプリが認識する言語を変更するには、[言語設定s]({{site.baseurl}}/user_guide/administrative/access_braze/language/)を参照してください。

### 強力なチャネル

#### 多言語設定

{% multi_lang_include release_type.md release="一般的な可用性" %}

[多言語設定を]({{site.baseurl}}/multi_language_support/)調整することで、異なる言語や地域のユーザーをターゲットに、1通のメールメッセージの中で異なるメッセージを送ることができる。多言語サポートを編集および管理するには、「多言語設定を管理」ユーザー権限が必要です。メッセージにロケールを追加するには、キャンペーンの編集権限が必要だ。

#### メッセージレベルのワンクリックリスト-配信停止 ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

list-unsubscribe ヘッダーのワンクリック配信停止 ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) により、受信者がメールから簡単にオプトアウトできます。このヘッダー設定は、メールのメッセージレベルで適用されるように調整できる。この設定の詳細については、「[ワークスペースのメール配信停止ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces)」を参照してください。

#### 電子メールのサニタイズについて

Brazeがメールメッセージ内の特定の種類のJavaScriptを検出した場合に発生する処理については、新しい[サニタイズの]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization)記事を参照。その主な目的は、悪質業者が他のBrazeダッシュボードユーザーのセッションデータにアクセスするのを防ぐことである。

#### コンテンツブロックの包含カウント

アクティブなキャンペーンまたはキャンバスにコンテンツブロックを追加した後、コンテンツブロックライブラリから[ このコンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) をプレビューするには、コンテンツブロックにマウスを合わせて<i class="fa fa-eye preview-icon"></i>**プレビュー** アイコンを選択します。

#### キャンバスのステータス

Brazeのダッシュボードでは、キャンバスがステータスごとにグループ化されている。異なる[キャンバスのステータスと説明]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) を確認してください。

### AI と ML のオートメーション

#### AIコピーライティング・アシスタントのブランド・ガイドライン

{% multi_lang_include release_type.md release="一般的な可用性" %}

AIコピーライティングアシスタントが生成するコピーのスタイルを、ブランドの声に合わせてカスタマイズするための[ブランドガイドラインを]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/)作成し、適用できるようになった。シナリオごとに複数のガイドラインを設定し、常に文脈に合ったトーンになるようにする。
 
### 新しいBrazeのパートナーシップ

#### Adikteev - 分析

Braze と [Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) の統合により、Braze CRM キャンペーン内で Adikteev の解約予測技術を活用し、リスクの高いユーザーセグメントを優先的にターゲットにすることで、ユーザーリテンションを高めることができます。
 
#### Celebrus - 分析
 
Braze と [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) の統合により、Web アプリチャネルとモバイルアプリチャネルで Braze SDK とシームレスに統合され、チャネルアクティビティデータを Braze に取り込みやすくなります。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的な洞察も含まれる。
 
#### IAM Studio - メッセージテンプレート
 
Brazeと[IAM Studioの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/)統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeのアプリ内メッセージに簡単に挿入することができ、画像置換、テキスト変更、ディープリンク設定、カスタム属性、イベント設定を提供する。IAM Studio を使用すると、メッセージの作成時間を短縮し、コンテンツ計画により多くの時間を費やすことができます。
 
#### Regal - インスタントチャット

Brazeと[Regalを]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/)統合することで、すべての顧客接点において、より一貫性のあるパーソナライズされた体験を生み出すことができる。

#### トレジャーデータ - コホートインポート
 
Braze と[トレジャーデータ]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/)の統合により、トレジャーデータから Braze にユーザーコホートをインポートし、ウェアハウス内にのみ存在する可能性のあるデータに基づいてターゲットを絞ったキャンペーンを送信できるようになります。
 
#### Zapier - ワークフローの自動化
 
Braze と [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) のパートナーシップでは、Braze API と Braze Webhook を活用してサードパーティアプリケーションに接続し、さまざまなアクションを自動化します。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Braze Swift SDK バインディングを更新して、9.2.0+ SemVer 仕様のリリースを必要とするようにします。
        - これにより、Braze SDK の9.2.0から10.0.0までのあらゆるバージョンとの互換性が確保されます (10.0.0は含まれません)。
        - 破壊的な変更の可能性に関する詳細については、[7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700)、[8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)、および[9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900)の変更ログエントリを参照してください。
    - プッシュ通知のサポートでは、アプリケーションの `AppDelegate.application(_:didFinishLaunchingWithOptions:)` メソッドにおいて、アプリのライフサイクルのできるだけ早い段階で静的メソッド `BrazeDestination.prepareForDelayedInitialization()` を呼び出すことが必要になりました。
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブ iOS ブリッジを [Braze Swift SDK 7.7.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
- [Expo プラグイン2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - ネイティブ iOS ブリッジを [Braze Swift SDK 7.7.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
    - ネイティブ Android ブリッジを [Braze Android SDK 29.0.1から30.3.0に](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDKバージョン5.0.0
    - iOSバインディングを [Braze Swift SDK 8.4.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
