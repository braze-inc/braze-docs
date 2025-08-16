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
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
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
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# 最新のBrazeリリースノート {#most-recent}

> Brazeは、主要な製品リリースに合わせて、月ごとに製品更新の情報を公開しています。ただし、製品は、週ごとにさまざまな改良が加えられて更新です。<br><br>このセクションに記載されているアップデートの詳細については、アカウント・マネージャーに問い合わせるか、[サポート・チケットを発行する]({{site.baseurl}}/user_guide/administrative/access_braze/support/)。また、[SDK Changelogsで]({{site.baseurl}}/developer_guide/changelogs)、毎月のSDKのリリース、アップデート、改良に関する詳細情報を確認することができる。

## 2025年6月24日リリース

### Braze による OfferFit

[OfferFit](https://www.offerfit.ai/) は、AB テストに代わって、あらゆるものをパーソナライズし、あらゆる指標を最大化する AI 意思決定を提供します。OfferFit を使えば、クリック数ではなく、売上を促進し、あらゆるビジネス KPI を最適化することができます。OfferFit のユースケースと主な機能については、当社が専用で用意した [OfferFit by Braze]({{site.baseurl}}/user_guide/offerfit) セクションをご覧ください。

### 新しいSDKチュートリアル

各 Braze SDK チュートリアルでは、完全なサンプルコードとともに、ステップバイステップの説明が提供されています。以下のチュートリアルを選んで使用を開始してください。

- [バナーの表示]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [アプリ内メッセージのスタイリングをカスタマイズする]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [条件付きでアプリ内メッセージを表示する]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [トリガーが設定されたアプリ内メッセージを延期する]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### データの柔軟性

#### SAMLジャストインタイムプロビジョニング

{% multi_lang_include release_type.md release="一般的な可用性" %}

[SAML ジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)を使用して、新規のダッシュボードユーザーが最初のサインイン時に Braze アカウントを作成できるようにします。これにより、管理者が新しいダッシュボード ユーザーのアカウントを手動で作成し、権限を選択してワークスペースに割り当て、アカウントの有効化を待機する必要がなくなります。

#### 選択ごとのフィルター

[選択項目]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections)ごとに最大10個のフィルターを追加できるようになりました。

#### カタログストレージ

無料版[カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage)のストレージサイズは最大100 MB です。100 MB 未満であれば、アイテム数に制限はありません。

#### クラウドデータ取り込みで同期された行数

クラウドデータ取り込みでは、デフォルトで、1回の実行で5億行まで同期できます。新しい行が5億行を超える同期は停止されます。

詳細については、[クラウドデータ取り込み製品の制限]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations)をご覧ください。

### 強力なチャネル

#### Inbox Vision のアクセシビリティテスト

{% multi_lang_include release_type.md release="一般的な可用性" %}

Inbox Vision の[アクセシビリティテスト]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing)を使用して、メールに存在する可能性のあるアクセシビリティの問題を浮き彫りにします。 

アクセシビリティテストでは、[Web コンテンツアクセシビリティガイドライン](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA 要件に照らしてメールコンテンツを分析します。これにより、どの要素がアクセシビリティ基準を満たしていないかについてのインサイトが得られます。

#### WhatsApp のクリック追跡

{% multi_lang_include release_type.md release="一般的な可用性" %}

レスポンスメッセージとテンプレートメッセージの両方で[クリックトラッキングを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking)有効にすると、WhatsAppパフォーマンスレポートでクリックデータを確認したり、誰が何をクリックしたかに基づいてユーザー群をセグメンテーションすることができる。

#### WhatsApp用動画

{% multi_lang_include release_type.md release="一般的な可用性" %}

送信する WhatsApp メッセージの本文に[動画を埋め込む]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features)ことができます。これらのファイルは URL または [Braze メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)でホストされていなければなりません。

### 新しいBrazeのパートナーシップ

#### Stripe - eコマース

Braze と [Stripe]({{site.baseurl}}/partners/stripe) の連携により、トライアルの開始、購読の有効化、購読のキャンセルなどの Stripe イベントに基づいて、Braze でメッセージングをトリガーできます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - ネイティブAndroidブリッジを[Braze Android SDK 35.0.0から36.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブiOSブリッジを[Braze Swift SDK 11.6.1から12.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [セグメンテーション Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Braze Android SDK を[35.0.0から36.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。

## 2025年5月27日リリース

### データの柔軟性

#### ワークスペース間でキャンバスをコピーする

{% multi_lang_include release_type.md release="一般的な可用性" %}

キャンバスをワークスペース間でコピーできるようになりました。これによって、別のワークスペースにあるキャンバスのコピーから始めることで、メッセージの構成をジャンプスタートさせることができる。コピーされる内容については、[ワークスペース間でキャンペーンとキャンバスをコピーするを]({{site.baseurl}}/copying_to_workspaces/)参照のこと。

#### 承認ワークフローのメッセージングルール 

{% multi_lang_include release_type.md release="一般的な可用性" %}

承認ワークフローで[メッセージングルールを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules)使用し、追加承認が必要になる前に到達可能なユーザー数を制限することで、より多くのオーディエンスをターゲットにする前にキャンペーンやキャンバスを見直すことができる。

#### SnowflakeとBrazeの実体関係図

今年の初め、我々はSnowflakeとBrazeの間で共有されるデータのためにエンティティ関係テーブルを作成した。今月は、各テーブルの詳細をパンしたり、掴んだり、ズームしたりできる[新しいインタラクティブなダイアグラムを]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/)追加し、データがBrazeとどのように相互作用するのか、より良いアイデアを提供する。

### 創造性を引き出す

#### 推奨イベント

{% multi_lang_include release_type.md release="早期アクセス" %}

[推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events)は、最も一般的な e コマースのユースケースに対応しています。推奨イベントを使用することで、事前に作成されたキャンバステンプレート、カスタマーライフサイクルにマッピングされたレポートダッシュボードなどをアンロックすることができる。

### 強力なチャネル

#### バナーチャネル

{% multi_lang_include release_type.md release="一般的な可用性" %}

[バナーを]({{site.baseurl}}/user_guide/message_building_by_channel/banners)使えば、ユーザーにパーソナライズされたメッセージングを作成することができ、同時にメールやプッシュ通知など、他のチャネルのリーチを広げることができる。アプリやWebサイトに直接バナーを埋め込むことができるので、自然な感覚でユーザーとエンゲージメントできる。

#### リッチコミュニケーションサービス（RCS）チャネル

{% multi_lang_include release_type.md release="一般的な可用性" %}

[リッチ・コミュニケーション・サービス（RCS）は]({{site.baseurl}}/about_rcs/)、従来のSMSを強化するもので、ブランドは情報提供だけでなく、はるかにエンゲージメントの高いメッセージを配信することができる。現在、Android と iOS の両方でサポートされている RCS では、高品質のメディア、インタラクティブなボタン、ブランド化された送信者プロファイルなどの機能がユーザーのプリインストール済みメッセージングアプリで直接使用可能になるため、別のアプリをダウンロードする必要がなくなります。

#### プッシュ設定ページ

{% multi_lang_include release_type.md release="一般的な可用性" %}

[**プッシュ設定**ページを]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings)使用して、プッシュTTL（Time to Live）やAndroidキャンペーンのデフォルトFCM優先度など、プッシュ通知の主要設定を行う。これらの設定は、プッシュ通知の配信と効果を最適化し、ユーザーにとってより良いエクスペリエンスを保証するのに役立つ。

#### アプリ内メッセージキャンペーン用プロモーションコード

{% multi_lang_include release_type.md release="早期アクセス" %}

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

[Mention Me](https://www.mention-me.com/) と Braze を組み合わせることで、プレミアム顧客を獲得し、揺るぎないブランドロイヤリティを育むための入り口とすることができます。ファーストパーティの紹介データをシームレスに Braze に統合することで、ブランドのファンをターゲットにした、パーソナライズされたオムニチャネル体験を提供することができます。まずは、「[テクノロジーパートナー: Mention Me]({{site.baseurl}}/partners/mention_me)」をご覧ください。

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

{% multi_lang_include release_type.md release="早期アクセス" %}

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
        - 静的 XCFramework を手動で統合する場合、ターゲットの [*一般設定*] の [*Frameworks, Libraries, and Embedded Content*] セクションで、各 XCFramework の [*Embed & Sign*] オプションを選択する必要があります。
        - Swift パッケージマネージャーや CocoaPods の統合に対する変更は不要です。
- [Braze Segment Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - `12.0.0` 以上の SemVer のリリースを要求するように、Braze Swift SDK バインディングを更新しました。
        - これにより、Braze SDK の`12.0.0`から`13.0.0`までのあらゆるバージョンとの互換性が確保されます (11.0.0は含まれません)。
        - 変更内容の詳細については、[`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) の変更履歴エントリを参照してください。

## 2025年4月1日リリース

### Brazeナビゲーションの更新

更新された Braze のナビゲーションは、デバイスを問わず機能やコンテンツに効率的にアクセスできるように設計されています。ナビゲーションのバージョンを切り替えるオプションは使用できなくなりました。詳しくは、[Braze のナビゲーティング]({{site.baseurl}}/user_guide/administrative/access_braze/navigation)に関する記事をご覧ください。

### 開発者ガイドの単純化

以前は、多くのプラットフォームレベルのタスクが複数のページに分割されていました。例えば、Swift SDK の統合は6つのページに分割されていました。さらに、共有機能はプラットフォームごとに個別にドキュメント化されていた。つまり、「プッシュ通知の設定」といったトピックを検索すると、10種類のページがヒットすることになる。

**以前: **

![[プラットフォーム統合ガイド] セクションにある以前の Swift ドキュメント。]({% image_buster /assets/img/before_swift.png %})

今後は、プラットフォームレベルのタスクは1つのページに統合され、共有されている SDK 機能は (新しい SDK タブ機能により) 同じページに配置されます。例えば、Braze SDKを統合するためのページは1つだけになり、ページ上部のタブを選択することでプラットフォームを切り替えることができる。そうすると、ページ内の目次も更新され、現在選択されているタブが反映されます。

**今後: **

![[SDK の記事の統合] Swift タブにある更新された Swift ドキュメント。]({% image_buster /assets/img/after_swift.png %})

![[SDK の記事の統合] Android タブにある更新された Android ドキュメント。]({% image_buster /assets/img/after_android.png %})

### Braze ドキュメントへの貢献

ご存じないかもしれませんが、Braze のドキュメントは完全なオープンソースです。方法については、[貢献ガイド]({{site.baseurl}}/contributing/home)をご覧ください。今月は、[セクションを強制的に自動展開さ]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand)せたり、[APIで生成されたコンテンツをレンダリング]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server)したりといった、サイトの機能をドキュメント化した。

### データの柔軟性

#### キャンバスエントリのプロパティ更新

キャンバスエントリのプロパティが、[キャンバスのコンテキスト変数の]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)一部になりました。各コンテキスト変数には、名前、データ型、およびLiquid を含めることができる値が含まれます。詳しくは、[Context コンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)をご覧ください。

#### 電話番号フィルターのセグメンテーションフィルターの更新

セグメンテーションフィルターが更新され、2つの電話番号フィルターが変更されました。

- [書式なし電話番号]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (旧称: **電話番号**): フォーマットされていない電話番号でユーザーをセグメンテーションする。
- [電話番号]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (旧称: **発信電話番号**): E.164 形式の電話番号フィールドでユーザーをセグメンテーションします。

#### カスタムデータを削除する

ターゲットを絞ったキャンペーンやセグメントを構築していくうちに、カスタムイベントやカスタム属性が不要になるかもしれない。今後は、[このカスタムデータを削除]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data)し、アプリから参照を削除することができます。

#### メールアドレスと電話番号を持つユーザーをインポートする

[ユーザーのインポートに]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers)メールアドレスや電話番号を使用し、外部IDやユーザーエイリアスを省略できるようになった。

#### サービスプロバイダーによるログインのトラブルシューティング

サービスプロバイダー（SP）主導のログインに、SAMLとシングルサインオンの問題を解決するのに役立つ[トラブルシューティングセクションが]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting)追加された。

#### ユーザー・インポートのトラブルシューティング

[ユーザーインポートのトラブルシューティングセクションには]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting)、インポートしたCSVファイルの行が見つからない場合のトラブルシューティング方法など、新規および更新エントリがある。

#### セグメントエクステンションに関するよくある質問

複数のカスタムイベントを使用するセグメントエクステンションの作成方法など、セグメントエクステンションに関する[よくある質問を]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions)確認する。

#### パーソナライズされた遅延の延長

{% multi_lang_include release_type.md release="早期アクセス" %}

ユーザーに対して[パーソナライズされた遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays)を設定し、コンテキストステップで使用することで、遅延させるコンテキスト変数を選択することができます。

また、遅延ステップを最長2年まで延長できるようになりました。例えば、アプリの新規ユーザーをオンボーディングする場合、セッションを開始していないユーザーを後押しするために、メッセージステップを送信する前に2ヶ月間延長遅延を追加することができる。

#### Snowflakeのデフォルトユーザープロファイル属性

{% multi_lang_include release_type.md release="ベータ" %}

Snowflake の[デフォルトユーザープロファイル属性]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/)が3つになりました。各ビューは、独自のパフォーマンスを考慮した特定のユースケース向けに設計されています。例えば、ユーザープロファイルのデフォルト属性を定期的にスナップチャットで受け取ることができます。

### 強力なチャネル

#### メッセージングの基本

[メッセージング・ファンダメンタルズは]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals)、エンゲージメント・ツールの新しいセクションで、メッセージのアーカイブやローカライゼーションなど、キャンペーンやキャンバスで共有されるコンセプトや用語がまとめられている。

#### WhatsApp カスタムドメイン

[カスタムドメインを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/)1つまたは複数のWhatsAppサブスクリプショングループに割り当てられるようになった。

#### キャンバスのアプリ内メッセージのトリガー

セッションの開始時やカスタムイベントの発生時、購入時にトリガーされるよう、[アプリ内メッセージのトリガー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)のタイミングを選択できるようになりました。遅延期間が経過し、オーディエンスオプションがチェックされた後、ユーザーがメッセージステップに到達すると、アプリ内メッセージはライブに設定されます。ユーザーがセッションを開始し、アプリ内メッセージのトリガーイベントを実行した場合、ユーザーにはアプリ内メッセージが表示される。 

#### キャンバスの入場量制限

このキャンバスに入る可能性のある人の数を、選択した周期 (毎日、キャンバスの有効期間中、またはキャンバスがスケジュールされるたび) で制限することができます。例えば、キャンバスが1日に5,000人のユーザーにしか送信できないように[エントリコントロールを設定]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience)することができます。

#### 新しいユースケース: 予約リマインダーメールシステム

Brazeの機能を使って[予約リマインダーのメッセージングサービスを構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case)する方法を学習。このサービスでは、ユーザーが予約を入れることができ、今後の予約のリマインダーをメッセージングしてくれる。このユースケースではメールメッセージを使用しているが、ユーザープロファイルの1回の更新に基づいて、任意の、または複数のチャネルにメッセージを送信することができる。

#### 特定リンクのクリック追跡

HTMLエディターでメールメッセージにHTMLコードを追加するか、ドラッグ＆ドロップエディターでコンポーネントにHTMLコードを追加することで、特定のリンクの[クリックトラッキングをオフにする]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis)ことができる。

#### ダイナミックな Apple プッシュ通知サービスのゲートウェイ管理

[ダイナミックなAPNゲートウェイ管理は]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management)、適切なAPN環境を自動的に検出することで、iOSのプッシュ通知の信頼性と効率を高める。以前は、プッシュ通知用のAPN環境（開発環境または本番環境）を手動で選択していたため、ゲートウェイの設定が間違っていたり、配信に失敗したり、BadDeviceTokenエラーが発生したりすることがあった。

#### バナーの Flutter サポート

{% multi_lang_include release_type.md release="早期アクセス" %}

バナーが Flutter に対応しました。さらに、すべてのバナーのドキュメントが、より使いやすくなるように一新されました。以下の記事をご覧になり、使用を開始してください。

- [バナーについて]({{site.baseurl}}/developer_guide/banners/)
- [バナーキャンペーンを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [アプリにバナーを埋め込む]({{site.baseurl}}/developer_guide/banners/creating_placements/)

#### WhatsApp クリックトラッキング

{% multi_lang_include release_type.md release="早期アクセス" %}

[クリックトラッキング]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/)では、WhatsApp メッセージ内のリンクをタップされたタイミングを測定し、どのコンテンツがエンゲージメントを促進しているかを明確に把握することができます。BrazeはURLを短縮し、裏でトラッキング追跡を追加し、クリックイベントが発生するとログに記録する。

#### プッシュに関するよくある質問

プッシュキャンペーンを設定する際によくある質問をまとめた新しい[プッシュFAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq)の記事をチェックしよう。

#### プッシュに関するトラブルシューティング

[プッシュ通知のトラブルシューティングは]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting)、プッシュ通知の配信に関する課題を解決するための多くのステップを提供している。例えば、プッシュ通知の配信に問題がある場合に備えて、トラブルシューティングのためのステップをまとめています。

### 新しいBrazeのパートナーシップ

#### Movable Ink Da Vinci - ダイナミックなコンテンツ

Braze と Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) の統合により、ブランドは Da Vinci の AI ドリブン型コンテンツ決定エンジンを活用して、高度なパーソナライズメッセージングを配信できます。Da Vinci はユーザーごとに最も関連性の高いコンテンツをキュレートし、Braze を通じてメッセージをシームレスに展開します。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブAndroidブリッジを[Braze Android SDK 33.0.0から35.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - 最低限必要なAndroid SDKのバージョンは25である。詳細については、[こちら](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)をご覧ください。
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## 2025年3月4日リリース

### 延期

Braze は、ソフトバウンスの定義を更新し、2025年2月25日午前10時 (米国東部標準時) より、[延期]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)と呼ばれる新しいイベントを送信します。

SendGrid の顧客向けに、延期イベントとソフトバウンスイベントを分離する変更を行いました。延期されたイベントは、ソフトバウンスイベントとしてカウントします。SendGrid の顧客で、Currents、Query Builder、SQL Extension、Snowflake データ共有、またはトランザクションメール製品を使用している場合は、この影響を受けます。

#### 以前の動作

2025年2月25日以前は、キャンペーンまたはキャンバスのメールアドレスの延期イベントは、毎回ソフトバウンスイベントを記録していました。その結果、延期はソフトバウンスのデータに含まれていました。そのため、ユーザーやキャンペーンが想定以上にソフトバウンスイベントをレポートする可能性がありました。 

#### 新しい行動

2025年2月25日以降、延期されたイベントは毎回ソフトバウンスイベントを記録することはなくなります。その代わり、メールの再試行回数や延期回数を問わず、そのメールアドレスの送信ごとにソフトバウンスイベントを記録します。

#### これが意味すること

2025年2月25日からソフトバウンスイベントの量が大幅に減少し、その結果、以下のような変化が生じる可能性があります。

- Query Builder を使用して作成されたレポートのソフトバウンスが減少
- Y期間にX回ソフトバウンスしたユーザーをターゲットにする場合、SQLエクステンションを使用してセグメントサイズを小さくする。
- Currents および Snowflake を使用した当社の機能のいずれかを使用して配信されたソフトバウンスイベントの数が減少
- トランザクションメール製品のソフトバウンス数が減少

SparkPost の顧客の場合、ソフトバウンスイベントデータへの影響はありませんが、代わりに Currents と Snowflake で新しいメールイベント「延期」を受信するようになります。

### 開発者ガイドの単純化

複数の SDK で共有されている同一のコンテンツを、ドキュメントサイトの新しい SDK タブ機能で統合し始めています。今月は、[SDK 統合]({{site.baseurl}}/developer_guide/sdk_integration/)、[SDK 初期化]({{site.baseurl}}/developer_guide/sdk_initialization/)、[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)が統合されました。今後数ヶ月の更新にご期待ください。

### データの柔軟性
 
#### ユーザープロファイル用のBraze ID

ユーザープロファイルに [Braze ID]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles) が含まれるようになりました。ユーザープロファイルを検索する際にこれを使用できます。

#### 延期

Brazeは、ソフトバウンスの定義を更新し、メールがすぐに配信されなかった場合に、一時的な配信失敗の後、最大72時間までメールを再試行し、特定のキャンペーンの試行が停止される前に配信成功の可能性を最大化する、[延期という]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance)新しいイベントを送信している。

#### Snowflake エンティティのリレーションシップ
 
Snowflake と Braze のエンティティリレーションシップの[未加工のテーブルスキーマ](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt)を、新しい[ユーザーフレンドリーなドキュメントページ](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships)にマッピングしました。これには、各チャネルに属する `USER_MESSAGES` テーブルの内訳と、各テーブルの主キー、外部キー、ネイティブキーの説明が含まれます。

#### external ID の ID 管理

メールアドレスまたはハッシュ化されたメールアドレスをBraze外部IDとして使用すると、データソース全体のID管理を簡素化できますが、ユーザープライバシーとデータセキュリティに対する[潜在的な]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles)リスクを考慮することが重要です。
 
### 創造性を引き出す

#### Liquidチュートリアル

以下のシナリオにおけるオペレーターの使用方法に関する3つの [Liquid チュートリアル]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials)を追加しました。

<table border="1">
  <tr>
    <td>整数カスタム属性を持つメッセージを選択する。</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="整数のカスタム属性を持つメッセージを表示するBrazeの作成ステップ。" /></td>
  </tr>
  <tr>
    <td>文字列カスタム属性を持つメッセージを選択する。</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="文字列カスタム属性を持つメッセージを表示するBrazeの作成ステップ。" /></td>
  </tr>
  <tr>
    <td>場所に基づいてメッセージを中止する。</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="場所に基づいてメッセージが中止されている Braze の作成ステップ。" /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### キャンバスのコンテキストステップ
 
{% multi_lang_include release_type.md release="早期アクセス" %}
 
[Contextステップを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)使用して、キャンバス内を移動するユーザーのコンテキスト（またはユーザーの行動に関するインサイト）を表す変数のセットを作成または更新する。

#### パーソナライズされた遅延

{% multi_lang_include release_type.md release="早期アクセス" %}

遅延ステップで [**パーソナライズされた遅延**] トグルを選択して、ユーザーに[パーソナライズされた遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays)を設定することができます。これをコンテキストステップで使用すると、遅延させるコンテキスト変数を選択することができます。

キャンバスのユーザージャーニーで遅延ステップを設定する際、最長2年までの遅延を設定できるようになりました。

#### 自動同期の取り消し

[メールメッセージ作成]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email)画面では、プレーンテキストが同期されていない場合にのみ表示される「Regenerate from HTML」アイコンを選択することで、「Plaintext」タブで自動同期に戻すことができる。

![Braze の自動同期の取り消しボタン。]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### 強力なチャネル

#### Androidライブ更新

ライブ更新が正式に利用できるようになるのは
[Android 16では](https://android-developers.googleblog.com/2025/01/first-beta-android16.html)、[Android用のLive Updatesの]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local)ページで、その動作をエミュレートする方法を紹介しているので、[Swift Braze SDK用のLive Activitiesと]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)同様に、インタラクティブなロック画面通知を表示することができる。正式なライブ更新とは異なり、この機能は古いバージョンの Android にも実装できます。

#### ワークスペース間でフィーチャーフラグ付きキャンペーンをコピーする

[ワークスペース間でフィーチャーフラグ付きキャンペーンをコピー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags)できるようになった。これを行うには、送信先ワークスペースに、元のキャンペーンで参照されたフィーチャーフラグと一致する ID で設定されたフィーチャーフラグエクスペリメントがあることを確認します。

#### 新しい WhatsApp メッセージタイプに対応

WhatsAppメッセージが[動画、音声、ドキュメントの送信メッセージに]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages)対応した。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。

#### 右から左に読むメッセージ

[右から左に読むメッセージの作成]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)では、メッセージをできるだけ正確に表示できるように、右から左に読む言語でメッセージを作成するためのベストプラクティスを取り上げています。
 
### AI と ML のオートメーション
 
#### 項目の推奨事項

[メッセージングにおけるアイテムの推奨の使用は]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations)、`product_recommendation` Liquidオブジェクトをカバーし、その知識を実践に役立てるためのチュートリアルを含む。

### 新しいBrazeのパートナーシップ
 
#### Email Love - チャネルの拡張
 
Brazeと[Email Loveの]({{site.baseurl}}/partners/message_orchestration/)パートナーシップは、Email LoveのBrazeへのエクスポート機能とBraze APIを活用し、メールテンプレートをシームレスにBrazeにアップロードする。

#### VWO - AB テスト
 
Braze と [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) の統合により、VWO の実験データを活用してターゲットセグメントを作成し、パーソナライズされたキャンペーンを提供することができます。
 
### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - React Native の最小要件バージョンを[0.71.0](https://reactnative.dev/blog/2023/01/12/version-071)に引き上げます。詳細については、React Working Group の [Releases Support Policy](https://github.com/reactwg/react-native-releases#releases-support-policy) をご覧ください。
    - iOS の最小バージョンを12.0に引き上げます。
    - ネイティブの iOS バージョンバインディングを [Braze Swift SDK 7.5.0から8.1.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブAndroidバージョンバインディングを[Braze Android SDK 29.0.1から30.1.1に](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。

## 2025年2月4日リリース

### Braze ドキュメントの改善

#### 寄稿ガイド
[寄稿ガイド]({{site.baseurl}}/contributing/your_first_contribution)の最近の更新により、技術者でないユーザーも Braze ドキュメントに寄稿しやすくなりました。

#### データ＆分析の刷新
お探しの記事を見つけやすくするため、以前は「データ＆分析」の下にあった記事を「[データ]({{site.baseurl}}/user_guide/data)＆[分析]({{site.baseurl}}/user_guide/analytics)」に分離した。 

#### 開発者ガイド
[Braze 開発者ガイド]({{site.baseurl}}/developer_guide/home)の全ドキュメントをクリーンアップし、複数のページに散らばっていた「方法の説明」を1つのページにまとめました。

また、新しい [SDK リファレンスページ]({{site.baseurl}}/developer_guide/references)では、各 Braze SDK のすべてのリファレンスドキュメントとリポジトリをリストアップしています。

##### Unreal Engine Braze SDK
Unreal Engine Braze SDKのGitHubリポジトリのREADMEから、[Braze Docsの専用セクションに]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine)すべてのコンテンツを移行し、書き直した。

### データの柔軟性

#### API 使用状況ダッシュボード

{% multi_lang_include release_type.md release="一般的な可用性" %}

[API使用状況ダッシュボードを]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard)使用すると、Brazeに入力されるREST APIトラフィックを監視して、REST APIの使用状況の傾向を把握し、潜在的な問題をトラブルシューティングすることができる。

#### カスタム属性にタグを追加する

{% multi_lang_include release_type.md release="一般的な可用性" %}

イベント、アトリビューション、購入の管理」権限があれば、カスタム属性を作成した後に[タグを追加]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags)できます。その後、タグを使用して、属性のリストをフィルター処理できます。

#### カタログセレクションと非同期カタログフィールドエンドポイント 

{% multi_lang_include release_type.md release="一般的な可用性" %}

現在、以下のエンドポイントが一般提供されています。
* [POST: カタログフィールドの作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE: カタログフィールドの削除]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE: カタログ選択の削除]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: カタログ選択の作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### キャンペーンやキャンバスのトリガーとしてメールアドレスを使用する。

{% multi_lang_include release_type.md release="一般的な可用性" %}

[キャンペーンや]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) [キャンバスの]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience)トリガーとして、メールアドレスで受信者を指定できるようになった。

#### 電話番号を使ってAPI経由でユーザーを識別子する

{% multi_lang_include release_type.md release="一般的な可用性" %}

[`/users/identify` APIエンドポイントを通じて]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)ユーザーを識別するために、エイリアスとメール・アドレスに加えて電話番号を使用できるようになった。

#### SAML トレースを取得する
サポートで SAML SSO に関する問題をより効率的に解決できるように、[SAML トレースの取得方法に関するステップ]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace)を追加しました。
 
#### 地域別データセンター
Braze が成長して新しい地域にサービスを提供するのに伴い、[Braze のデータセンターに関する記事]({{site.baseurl}}/user_guide/data/data_centers)を追加し、運用アプローチを明確にしました。
 
### 創造性を引き出す
 
#### 値下げ通知と再入荷通知

{% multi_lang_include release_type.md release="一般的な可用性" %}

キャンバスやカタログで[入荷通知を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications)設定することで、顧客に商品の入荷を通知できるようになった。

また、カタログやキャンバスで値下げ通知を設定することで、商品の価格が下がったときに顧客に通知する[値下げ通知]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications)を作成することもできます。

#### セレクションプレビュー 

{% multi_lang_include release_type.md release="一般的な可用性" %}

セレクションを作成した後、ランダムなユーザーまたは特定のユーザーに対して、[セレクションが返す結果を見る]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview)ことができる。

#### リキッドを含むカタログアイテムのテンプレート化 

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Liquid を含むカタログ項目をテンプレート化]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid)できます。

#### キャンバステンプレート
[好みの調査でユーザーをオンボーディング]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey)し、[ダブルオプトインでメールでの登録を作成する]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup)ための新しいキャンバステンプレートを追加しました。

#### B2B 向け Salesforce Sales Cloud を使ってリードを管理する
B2B マーケターによる Braze の用途のひとつに、Salesforce Sales Cloudとの統合があります。この[ユースケース]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud)の実装方法に関する詳細をご覧ください。
 
### 強力なチャネル

#### 抑制リスト

{% multi_lang_include release_type.md release="ベータ" %}
 
[除外リスト]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)は、メッセージを受信しないユーザーグループを指定します。管理者は、セグメントフィルターを使用して除外リストを作成し、ユーザーグループをセグメンテーションと同じように絞り込むことができます。

### 新しいBrazeのパートナーシップ

#### Constructor - ダイナミックなコンテンツ
[Constructor]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/) は、AI と機械学習を利用してパーソナライズされた検索、レコメンデーション、ブラウジング体験を e コマースおよび小売 (店) の Web サイトに提供する、検索・商品発見プラットフォームです。
 
#### Trustpilot - ダイナミックなコンテンツ
[Trustpilot]({{site.baseurl}}/partners/trustpilot/) は、顧客がフィードバックを共有し、レビューの管理と返信を可能にするオンラインレビュープラットフォームです。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - SDK の最小バージョンを 21 (Lollipop) から 25 (Nougat) に更新した。

## 2025年1月7日リリース

### 創造性を引き出す

#### アプリ内メッセージテンプレート

アプリ内メッセージのドラッグ＆ドロップ用[テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/)を追加しました。

#### B2B Salesforce Sales Cloud でのリード管理

[Salesforce Sales Cloud でのリード管理]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/)では、Braze の Webhook を使用して、コミュニティから投稿された統合を通じて Salesforce Sales Cloud でリードを作成および更新する方法を示しています。

### 強力なチャネル

#### キャンバステンプレート

Braze キャンバスに、[ダブルオプトインによるメールでの登録]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/)と、[好みの調査によるオンボーディング]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/)のテンプレートを追加しました。

#### WhatsApp オプトインポリシーの変更

メタは最近、[オプトインポリシー](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)を更新しました。詳細については、[WhatsAppの製品更新を]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)参照のこと。

#### メールのドラッグ＆ドロップエディターにおけるコンテンツブロックの幅ツール

ドラッグ＆ドロップのメールエディターで、コンテンツブロックの[幅を調整]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block)できます。デフォルトの幅は100％である。

### データの柔軟性

#### ソフトバウンスのセグメントフィルター

Y日間にX回バウンスしたかどうかでユーザーをセグメントします。詳細については、[セグメンテーションフィルターの用語集]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)をご覧ください。

#### 匿名ユーザーの概要

[匿名ユーザーは]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)、匿名ユーザーとユーザーエイリアスの概要を説明し、その意義とメッセージングでどのように活用できるかを概説する。

#### グローバルコントロールグループのメンバーシップ

ユーザープロファイルの [**エンゲージメント**] タブを開き、[**その他**] セクションまでスクロールすると、[グローバルコントロールグループのメンバーシップを確認]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group)できます。

### 新しいBrazeのパートナーシップ

#### ジャストゥーノ - リード獲得

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/) では、ダイナミックなセグメンテーションにより、すべてのオーディエンスに対して完全に最適化されたビジター体験を作成することができ、サイトの速度に影響を及ぼしたり、開発作業を増加させることなく、最も高度なターゲティングを利用できます。

#### Odicci - 顧客データプラットフォーム

Braze は、ロイヤルティ主導のオムニチャネルエクスペリエンスを通じて顧客の獲得、エンゲージメント、維持を可能にするプラットフォームである [Odicci]({{site.baseurl}}/partners/odicci/) と連携します。

#### Optimizely - ABテスト

Braze と [Optimizely ]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/)の連携は双方向の連携であり、以下のことが可能になります。

- Brazeの顧客セグメントとイベントを毎晩Optimizelyデータプラットフォーム（ODP）に同期し、Optimizelyの顧客プロファイル、レポート、セグメンテーションを充実させる。
- Braze Currents のイベントを Braze から Optimizely のレポートツールに送信する。
- ODPの顧客データとイベントをBrazeに同期し、Brazeの顧客データを充実させ、ODPの顧客イベントに基づいてBrazeのメッセージングをトリガーする。

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

Braze と[ Zeotap](https://zeotap.com/) の統合により、Zeotap の顧客セグメントを Braze のユーザープロファイルに同期することで、キャンペーンの規模とリーチを拡大できます。[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) では、データを Zeotap に接続し、グローススタック全体で実用的なデータにすることもできます。

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
