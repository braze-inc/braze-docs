---
nav_title: ホーム
article_title: Brazeの新機能
description: "Brazeのリリースノートは毎月公開される。これにより、主要な製品リリース、継続的な製品改善、Brazeのパートナーシップ、SDKの変更点、機能の廃止について最新情報を入手できる。"
page_order: 0
search_rank: 1
page_type: reference

---

# Brazeの新機能

{% alert tip %}
このページに記載されている更新内容について、詳細を知りたい場合は、担当のアカウントマネージャーに連絡するか、[サポートチケットを開いてください]({{site.baseurl}}/user_guide/administrative/access_braze/support/)。月次SDKリリース、改善点、および互換性のない変更に関する詳細情報は、当社の[SDK変更履歴]({{site.baseurl}}/developer_guide/changelogs)を参照せよ。
{% endalert %}

{% details March 5, 2026 %}

## 2026年3月5日リリース

### データ&レポート

#### 新しいデータセンター

{% multi_lang_include release_type.md release="General availability" %}

Brazeは新しい[データセンター]({{site.baseurl}}/user_guide/data/data_centers/)を立ち上げた。JP-01。Braze アカウントを設定する際に、地域別のデータセンターに登録することができます。

#### コンテキスト変数

{% multi_lang_include release_type.md release="General availability" %}

[コンテキスト変数とは、]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables)特定のキャンバス内をユーザーが移動する過程で作成・使用できる一時的なデータである。ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。この手法により、各キャンバスエントリは独自の独立系コンテキストを維持できる。これにより、ユーザーは同一のジャーニー内で複数のアクティブ状態を保持しつつ、各状態固有のコンテキストを維持できる。

#### クラウドデータ取り込みソース

{% multi_lang_include release_type.md release="Early access" %}

[クラウドデータ取り込みには]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze)新しいUIが導入された。これによりデータソースと同期が分離され、単一のデータソースを任意の数の同期で再利用できるようになった。これにより、設定の重複が減り、複数の同期がある場合のセットアップが簡素化される。既存の同期設定がある場合、それらは自動的に新しいソースと同期の設定構造に移行される。ダウンタイムは発生しない。まず、**Cloud Data Ingestion** > **Sources** に移動してデータソースを表示、編集、または作成する。次に、同期を作成する際にドロップダウンからデータソースを選択する。

#### Currentsとデータ共有イベントの追加フィールド

{% multi_lang_include release_type.md release="General availability" %}

[CurrentsとData Shareのイベントには]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)、分析や下流システム向けのデータ深掘りを目的として、以下の新フィールドが追加された：

- `agentconsole.AgentExecuted`:追加された`error`(文字列) — 発生したエラーの説明。
- `agentconsole.ToolInvocation`:追加された`request_id`(文字列) — 全体的なLLMリクエストおよび完全な実行に対する一意のID。
- `users.messages.rcs.InboundReceive`:追加された`canvas_variation_name`(文字列) — ユーザーが受け取ったキャンバスバリエーションの名前。

#### Snowflake Data Share のキャンペーンおよびキャンバスフィールド

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Shareは]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3)、既存の66のテーブルにキャンペーンとキャンバスの情報を反映した追加フィールドを含めるようになった。具体的には以下の通りだ：

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV事前インポート検証とエラーレポート

{% multi_lang_include release_type.md release="General availability" %}

[CSVユーザーインポートは、]({{site.baseurl}}/user_guide/data/user_data_collection/user_import)事前インポート検証と詳細なエラーレポートをサポートするようになった。インポート前に、**ユーザー**インポートページで「**インポート前にファイルを検証する**」を選択せよ。Brazeはファイルをスキャンし、完全に失敗する行（エラー）と一部の値がスキップされて成功する行（警告）を識別子で識別し、レポートを生成する。レポートをダウンロードし、CSVを修正して再アップロードするか、そのまま進めることもできる。インポートが完了した後、失敗した行のダウンロード可能なレポートも利用可能だ。各問題の正確な理由が記載されている。

#### メッセージング診断ダッシュボード

{% multi_lang_include release_type.md release="Early access" %}

[メッセージング診断ダッシュボード]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard)は、メッセージ送信結果の概要を提示する。これにより、傾向を把握し、メッセージング設定における潜在的な問題を診断できる。このダッシュボードは、キャンペーンやキャンバスからのメッセージが期待通りに送信されなかった理由を理解するのに役立つ。

### BrazeAI<sup>TM</sup>

#### エージェントコンソール内のBrazeエージェント

{% multi_lang_include release_type.md release="General availability" %}

[Brazeエージェントは、]({{site.baseurl}}/user_guide/brazeai/agents/)Braze内で作成できるAI搭載のヘルパーだ。エージェントはコンテンツを生成し、知的な判断を下し、データを充実させることができる。これにより、よりパーソナライズされたカスタマーエクスペリエンスを提供できるのだ。エージェントを作成する際には、その目的を定義し、どのように振る舞うべきかの制限を設定する。公開後、エージェントはBrazeに[デプロイ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)され、パーソナライズされた文面を生成したり、リアルタイムで判断を下したり、カタログフィールドを更新したりできる。

### オーケストレーション

#### 細分化されたユーザー権限

{% multi_lang_include release_type.md release="Early access" %}

Brazeは、ユーザーアクセスをより柔軟に管理する手段として、[きめ細かい権限設定]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)を導入する。移行プロセスについては[「細粒度権限への移行」]({{site.baseurl}}/granular_permissions_migration/)を参照のこと。これにはレガシー権限が細粒度権限にどのように対応するかも含まれる。

#### チャネルベースのレート制限

{% multi_lang_include release_type.md release="General availability" %}

マルチチャネルキャンペーンやキャンバスのレート制限を設定する際、共有レート制限か[チャネルごとの]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases)レート[制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases)のいずれかを選択できる。マルチチャネルキャンペーンやキャンバスがチャネルベースのレート制限を使用する場合、そのレート制限は選択された各チャネルに適用される。例えば、キャンペーンやキャンバス全体で、1分間に最大5,000件のWebhookと2,500件のSMSメッセージを送信するように設定できる。

#### キャンバスコンテキストのステップ

{% multi_lang_include release_type.md release="General availability" %}

[Canvas Contextのステップでは、]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)ユーザーがキャンバス内を移動する際に、ユーザーに対して1つ以上の変数を作成したり更新したりできる。例えば季節割引を管理するキャンバスでは、コンテキスト変数を使用して、ユーザーがキャンバスにエントリするたびに異なる割引コードを保存できます。

### チャネル&　タッチポイント

#### コンテンツブロック内のロケールを翻訳する

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにロケールを追加した後、コンテンツブロック内で[異なる言語のユーザーを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)すべて[対象に]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)できる。

### 提携

#### アルゴリア - 検索レコメンデーション

[Algoliaは]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia)、開発者が高速で関連性が高く、スケーラブルな検索体験を構築するのを支援する検索・発見プラットフォームだ。強力なAPIファーストのアプローチにより、Algoliaは高度なランキングアルゴリズムとAI駆動のインサイトを組み合わせ、シームレスにサイト検索、ナビゲーション、パーソナライズされたコンテンツ発見を実現する。

#### Anthropic - AIモデル提供者

[Anthropicは]({{site.baseurl}}/partners/ai_model_providers/anthropic)AIの安全性と研究を専門とする企業だ。同社が開発中のClaudeは次世代AIアシスタントであり、幅広い言語タスクにおいて有用で誠実、かつ安全に設計されている。

#### Canva - メッセージのパーソナライゼーション - クリエイティブスタジオ

[Canvaは]({{site.baseurl}}/partners/canva)、Canva内の画像をBrazeメディアライブラリーに直接同期する。これによりクリエイティブワークフローが効率化され、すべてのメッセージングチャネルでビジュアルアセットが最新の状態に保たれる。

#### DOTS.ECO \- 報酬

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) ユーザーに追跡可能なデジタル証明書を通じて、現実世界の環境への影響を報酬として与えることができる。各証明書には、共有可能な証明書URLや画像URLといったメタデータを含めることができる。これにより、ユーザーは自身の影響力の証明を閲覧（および再確認）できる。

#### フィグマ - メッセージのパーソナライゼーション - クリエイティブスタジオ

[フィグマは]({{site.baseurl}}/partners/figma)共同設計プラットフォームであり、製品を構築し、設計し、試作することができる。この連携機能を使って、Figmaから画像やビジュアルアセットを直接Brazeのメディアライブラリーに送信できる。

#### Flybuy - メッセージのパーソナライゼーション - 位置情報

Radius Networksの[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy)は、AI技術を活用した業界をリードするオムニチャネル位置情報プラットフォームだ。ピックアップ、デリバリー、ドライブスルー、店内飲食といったサービス形態を横断し、サービス速度の最適化を実現する。Flybuyは統合型マーケティングスイートを通じて、ブランドが超ターゲティングされた瞬間ベースのメッセージを配信することを可能にする。これにより顧客エンゲージメントの促進、購入額の増加、そしてより広範なロイヤルティ施策の支援を実現する。

#### Google Gemini - AIモデル提供者

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini)は、GoogleのAIモデル群である。テキスト、コード、画像にわたる高度な推論を組み合わせ、ブランドがよりスマートでパーソナライズされた体験を提供することを支援する。

#### リムビック - メッセージパーソナライゼーション - パーソナライゼーションエンジン

[リムビックは]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik)AI共鳴レイヤーだ。市場に到達する前に、実際のオーディエンスがメッセージやコンセプト、AI出力をどう解釈し反応するかを予測する。60カ国以上、25言語以上を対象とした継続的な一次調査に基づき、Limbikは人間による検証を経た合成オーディエンスを提供する。これは機械の速度で、調査レベルの精度（信頼度95％、エラー範囲1.5％～3％）をもって実際のオーディエンス反応をシミュレートするデジタル人口である。リンビックは、メッセージングがオーディエンスの信念や感情に即座に共鳴することを保証する能力を提供する。

#### リンクランナー - メッセージオーケストレーション - アトリビューション

[Linkrunnerは]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner)モバイルアトリビューションおよび分析プラットフォームであり、ユーザー獲得キャンペーンのトラッキングと分析を支援する。

#### Mailizio - メッセージオーケストレーション - テンプレート

[Mailizioは]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio)メール作成・管理プラットフォームだ。直感的なビジュアルエディターを使って、再利用可能でブランドイメージを損なわないコンテンツを簡単にデザインできる。MailizioとBrazeの連携により、コンテンツブロックやメールテンプレートをエクスポートできる。その後、同じ素材からアプリ内メッセージを自動生成できるため、迅速かつ完全にコントロールされたキャンペーン展開が可能となる。

#### オープン・ロイヤルティ - データ＆分析 - ロイヤルティ

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty)はクラウドベースのロイヤルティプログラムプラットフォームであり、顧客ロイヤルティと報酬プログラムを構築・管理できる。BrazeとOpen Loyaltyの連携により、ポイント残高、会員ランクの変更、有効期限の警告といったロイヤルティデータが、リアルタイムで直接Brazeに同期される。これにより、ユーザーのロイヤルティステータスが変更された際に、パーソナライズされたメッセージ（メール、プッシュ通知、SMS）を送信できるようになる。

#### OpenAI - AIモデル提供者

[OpenAIは]({{site.baseurl}}/partners/ai_model_providers/openai)GPTのような高度なAIモデルを開発している。これらは自然言語の理解と生成をイネーブルメントし、ブランドが有意義な顧客とのやり取りを構築し拡大することを可能にする。

#### Shopgate - チャネル

[Shopgateは]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate)モバイルコマースとオムニチャネルプラットフォームであり、小売業者がショッピングアプリを作成し、フルフィルメントツールとクライアントリング（顧客データに基づくパーソナライズされた店舗内サポート）を通じて実店舗の効率を向上させるのを支援する。

#### Splio - データ＆分析 - コホートインポート

[スプリオは]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio)オーディエンス構築ツールであり、カスタマーエクスペリエンスを損なうことなくキャンペーン数と収益を増やすことができる。さらにオンラインとオフラインの両方でCRMキャンペーンのパフォーマンスをトラッキングし、追跡する分析機能を提供する。

### SDK

#### SDKの互換性を損なう更新

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のバージョンを[37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[41.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
    - iOSバインディングを[Braze SWIFT SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[14.0.1に](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
    - Braze Android SDK に必要な新しい推移的 NuGet 依存関係を追加した：
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib バージョンが2.0.21.3から2.3.0.1に更新された。プロジェクトでこのパッケージを古いバージョンに明示的に固定している場合、復元エラーを避けるために更新が必要だ。
    - ニュースフィード機能を削除した。
        - この機能は、バージョン[38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0)でネイティブAndroid SDKから削除された。
        - この機能はバージョン[14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0)でネイティブSWIFT SDKから削除された。
    - enumのケースBRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeDataは に改名されたBRZInAppMessageDismissalReason.WipeData。
- [Expo プラグイン 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - このバージョンには、Braze React Native SDK 19.0.0 が必要だ。
    - (Android) データ永続化レイヤーにおけるメモリリークを修正した。
    - (Android) 終了状態からアプリが起動された際のプッシュ通知ディープリンク処理に対応するため、Braze.getInitialPushPayload() のサポートを追加した。この修正により、アプリをコールドスタートした際に、Android端末でプッシュ通知からのディープリンクが処理されない問題が解決された。
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - ネイティブSWIFT SDKのバージョンバインディングを、Braze SWIFT SDK 13.3.0から14.0.1に更新する。
    - ネイティブのAndroid SDKバージョンバインディングを、Braze Android SDK 40.0.2から41.0.0へ更新する。

{% enddetails %}

{% details February 5, 2026 %}

## 2026年2月5日リリース

### BrazeAI<sup>TM</sup>

#### コンテンツオプティマイザー

{% multi_lang_include release_type.md release="Beta" %}

[コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer)は、継続的で高バリアントのコンテンツテストを実行するキャンバスステップであり、オートメーションによるエンゲージメント最適化を提供する。メッセージステップと同様のドラッグ＆ドロップ可能なインターフェイスを使用し、テスト対象のコンポーネントを定義する。AIを用いてバリアントを生成する（または手動で入力する）。そしてLiquidタグを用いて、これらのコンポーネントをメッセージコンテンツにマッピングする。

非文脈に応じたマルチアームドバンディット最適化アルゴリズムを基盤とするコンテンツオプティマイザーは、ユーザーごとに単一のメッセージを送信する。予測に基づく推奨事項に基づき、どのコンポーネントバリアントの組み合わせを配信するかを決定する。ステップが時間の経過とともにデータを収集するにつれ、パフォーマンスの高いバリアントは送信割り当てが自然に増加し、パフォーマンスの低いバリアントは減少する。コンテンツオプティマイザーは、毎日一定数のユーザー（少なくとも1日あたり数千人）が繰り返し送信するキャンバスで最も効果を発揮する。これにより継続的な最適化がイネーブルされる。

### データ&レポート

#### eコマース推奨イベント

{% multi_lang_include release_type.md release="Early access" %}

e コマース推奨イベントを既存の購入イベントと一致させるため、[「注文を確定する」コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report)を追加した。これは「購入を行う」と類似している。

### チャネル&　タッチポイント

#### バナー内のローカライゼーションを行う

{% multi_lang_include release_type.md release="Early access" %}

ワークスペースにローカライゼーションを追加した後、単一のバナー内で[異なる言語のユーザーをターゲットにできる]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales)。

#### ドラッグ＆ドロップ可能なコンテンツブロックの幅を設定する

ナビゲーションメニューのボタンを選択して[、コンテンツブロックの幅を調整する]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block)。メールのグローバルスタイル設定で指定されていない場合、デフォルトの幅は100%だ。それ以外の場合は、グローバル設定が優先される。

![幅を編集するオプションを持つ両面矢印。]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### オートメーションによるIPウォームアップを使用する

{% multi_lang_include release_type.md release="Early access" %}

[オートメーションによるIPウォームアップ]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming)機能を使って、1日あたりの送信量を徐々に増やせ。そうすることで受信トレイのプロバイダーが送信パターンを学習し、信頼するようになる。Brazeは最もエンゲージメント度の高いサブスクライバーを優先的に送信する。これにより、日々の送信量がベストプラクティスに沿ったペースで増加する。

### 提携

#### LinkedIn – キャンバス オーディエンス同期

[Braze Audience Sync for LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/)を利用し、Braze連携から取得したユーザーデータをLinkedInの顧客リストに追加する。これにより、行動トリガーやセグメンテーションなどに基づいた広告配信が可能となる。ユーザーデータに基づいてBraze キャンバスでメッセージ（プッシュ通知、メール、SMS、Webhookなど）をトリガーする通常の基準は、LinkedInのカスタマーリストにおいて、そのユーザーへの広告をトリガーできるようになる。

#### Oracle Crowdtwist - データ&分析

[Oracle Crowdtwistは]({{site.baseurl}}/partners/crowdtwist)、ブランドがパーソナライズされたカスタマーエクスペリエンスを提供できるようにする、クラウドネイティブの顧客ロイヤルティソリューションのリーダーである。彼らのソリューションは100以上の既成のエンゲージメントパスを提供し、マーケターが顧客のより包括的な見解を構築するための迅速な価値実現を可能にする。

#### フルストーリー - ダイナミックなコンテンツ

[フルストーリーの]({{site.baseurl}}/partners/fullstory/)行動データプラットフォームは、テクノロジーリーダーがより良い、より情報に基づいた意思決定を行うのを助ける。Fullstoryの特許技術は、デジタル行動データを分析スタックに組み込むことで、質の高い行動データを大規模に活用する力を解き放つ。あらゆるデジタル訪問を実用的なインサイトへと変えるのだ。 

#### オープン・ロイヤルティ - データ&分析

[Open Loyalty]({{site.baseurl}}/partners/openloyalty)はクラウドベースのロイヤルティプログラムプラットフォームであり、顧客ロイヤルティと報酬プログラムを構築・管理できる。BrazeとOpen Loyaltyの連携により、ポイント残高、会員ランクの変更、有効期限の警告といったロイヤルティデータが、リアルタイムで直接Brazeに同期される。これにより、ユーザーのロイヤルティステータスが変更された際に、パーソナライズされたメッセージ（メール、プッシュ通知、SMS）を送信できるようになる。

#### DOTS.ECO \- 拡張機能

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) ユーザーに追跡可能なデジタル証明書を通じて、現実世界の環境への影響を報酬として与えることができる。各証明書には、共有可能な証明書URLや画像URLといったメタデータを含めることができる。これにより、ユーザーは自身の影響力の証明を閲覧（および再確認）できる。

#### Mailizio - メッセージオーケストレーション

[Mailizioは]({{site.baseurl}}/partners/mailizio/)メール作成・管理プラットフォームだ。直感的なビジュアルエディターを使って、再利用可能でブランドイメージを損なわないコンテンツを簡単にデザインできる。MailizioとBrazeの連携により、コンテンツブロックやメールテンプレートをエクスポートし、同じ素材からアプリ内メッセージを自動生成できる。これにより、迅速かつ完全にコントロールされたキャンペーン展開が可能となる。

### API

#### メディアライブラリの POST API

{% multi_lang_include release_type.md release="General availability" %}

メディアライブラリーのアセットはAPI経由で追加できるようになった。これにより顧客、パートナー、代理店はメッセージ作成ワークフローのオートメーションをさらに進められる。[API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create)を使ってアセットファイルを直接アップロードするか、既存のURLからファイルをコピーする。この機能は統合とオートメーションの機能を解放する。

### Currentsとデータ共有

#### ストレージ送信先とデータ共有のためのエージェントコンソールイベント

{% multi_lang_include release_type.md release="General availability" %}

ストレージ送信先（AWS S3、GCS、Azure Blob Storage）およびSnowflake Datashare向けに、新たに2つの[イベントが](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)利用可能になった：`agentconsole.AgentExecuted`と `agentconsole.ToolInvocation`である。これらのイベントにより、エージェントコンソールの使用状況や詳細をダウンストリームシステムで分析できる。これにより、エージェントの使用状況を理解し、最大限に活用できるようになる。エージェントを使えば、特定のタスクをBraze全体で実行できるインテリジェントエージェントを作成・展開できる。これには、キャンバスやカタログでのコンテンツ生成や、インテリジェントな意思決定に基づいてユーザーを異なるパスに誘導する機能が含まれる。詳細については、[Currentsの変更履歴](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照せよ。

#### 個々のチャネル向けの新しい「再試行」イベント

{% multi_lang_include release_type.md release="General availability" %}

メール、LINE、プッシュ通知、SMS、Webhook、WhatsAppの各チャネルで、新しい[再試行イベントが](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)利用可能になった。これらの事象は、フリークエンシーキャップによってスケジュールされたメッセージが中止されず遅延するタイミングを可視化する。メッセージの優先度が下げられたり配信頻度が制限された場合、設定された再試行期間内に再送信が可能となった。これにより、メッセージ配信パターンやフリークエンシーキャップの影響をより詳細に把握できるようになった。詳細については、[Currentsの変更履歴](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照せよ。

#### TokenStateChangeイベントに新しい'time_ms'フィールドを追加する

{% multi_lang_include release_type.md release="General availability" %}

イベント[`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)に新しい`time_ms`フィールドが追加された。これにより、プッシュトークンの状態変化をトラッキングする際にミリ秒単位の精度が得られる。この精度向上により、同一秒内に複数の変更が発生した場合でもプッシュトークンの最新ステータスを把握できる。これにより、下流システムにおいて正しいサブスクリプションステータスが維持されているという確信を得られる。詳細については、[Currentsの変更履歴](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)を参照せよ。

#### 匿名ユーザーをTealiumの送信先に送信する

{% multi_lang_include release_type.md release="General availability" %}

外部ユーザー IDが定義されていないイベントも[、Tealiumの]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents)送信先にストリーミングできるようになった。Currents 統合で「匿名ユーザーからのイベントを含める」チェックボックスを選択すると、外部ユーザー ID を持たないイベントは抑制されず、送信先に送信される。この機能は、識別子を持たない匿名ユーザーを扱う下流の分析やユースケースにおいて極めて重要である。

##### 匿名ユーザーをカスタムHTTP送信先に送信する

{% multi_lang_include release_type.md release="Beta" %}

外部ユーザー IDが定義されていないイベントは、カスタムHTTP送信先にストリーミングできるようになった。Currents 統合で「匿名ユーザーからのイベントを含める」チェックボックスを選択すると、外部ユーザー ID を持たないイベントは抑制されず、送信先に送信される。この機能は、識別子を持たない匿名ユーザーを扱う下流の分析やユースケースにおいて極めて重要である。

#### メール開封イベント — "machine_open"フィールド

[メール開封イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events)は[_、マシン開封_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens)メトリクスをレポートするために、フィールド"machine_open"値を生成するようになった。 

### SDK

以下のSDKアップデートがリリースされた。Swift SDK v14.0.1はユニバーサルリンクの処理に関する問題を修正した。Android SDK v40.2.0は、潜在的なメモリリークを修正し、透過アクティビティが存在する場合に複数のセッションが開かれる問題を解決する。Expo SDK v3.2.0では、ユニバーサルリンクのネイティブSWIFT SDK処理を設定するためのオプション`forwardUniversalLinks`が追加された（デフォルト値：false）。

#### SDKの互換性を損なう更新

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - `BrazeConfig.Builder.setIsLocationCollectionEnabled()` を`setIsAutomaticLocationCollectionEnabled()` に改名した。
    - `BrazeConfig.isLocationCollectionEnabled` を`isAutomaticLocationCollectionEnabled` に改名した。
    - `BrazeConfigurationProvider.isLocationCollectionEnabled` を`isAutomaticLocationCollectionEnabled` に改名した。
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expoプラグイン 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## 2026年1月8日リリース

### データ&レポート

#### Currentsイベントの更新

{% multi_lang_include release_type.md release="General availability" %}

バージョン4において、Currentsには以下の変更が加えられた：

* フィールドがイベントタイプに変更される`users.behaviors.pushnotification.TokenStateChange`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン
* フィールドがイベントタイプに変更される`users.messages.pushnotification.Bounce`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン
* フィールドがイベントタイプに変更される`users.messages.pushnotification.Send`：
    * 新しい`string`フィールド`push_token`を追加した：イベントのプッシュトークン
* フィールドがイベントタイプに変更される`users.messages.rcs.Click`：
    * 新しい`string`フィールド`canvas_variation_name`を追加した：このユーザーが受け取ったキャンバスのバリエーション名
    * フィールドは現在、*任意*`user_phone_number`*項目*となった。
* フィールドがイベントタイプに変更される`users.messages.rcs.InboundReceive`：
    * フィールドは現在、*任意*`user_id`*項目*となった。
* フィールドがイベントタイプに変更される`users.messages.rcs.Rejection`：
    * 新しい`string`フィールド`canvas_step_message_variation_id`を追加した：このユーザーが受け取ったキャンバスステップメッセージのバリエーションのAPI ID

各リリースのイベント変更については[、Currentsの変更履歴]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)を参照せよ。

#### 全行の同期ログをエクスポートする

{% multi_lang_include release_type.md release="Early access" %}

[クラウドデータ取り込み**同期ログ**ダッシュボード]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs)で、同期実行の行レベルログをエクスポートするには、次の方法を選択する：

* **エラーのある行：**エラーステータスの行のみを含むファイルをダウンロードする。
* **すべての行：**実行中に処理されたすべての行を含むファイルをダウンロードする。

### チャネル&　タッチポイント

#### 持ち込みの（BYO）WhatsAppコネクタ

[BYO（Bring Your Own）WhatsAppコネクタ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/)は、BrazeとInfobipの提携サービスである。このサービスでは、ユーザーがBrazeに自身のInfobip WhatsApp Business Manager（WABA）へのアクセス権を付与する。これにより、セグメンテーション、パーソナライゼーション、キャンペーンのオーケストレーションにはBrazeを利用しながら、メッセージング費用の管理と支払いをInfobipと直接行うことができる。 

#### キャンバスのバナー

{% multi_lang_include release_type.md release="Early access" %}

キャンバスの[メッセージステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)で、**バナーを**メッセージングチャネルとして選択する。ドラッグ＆ドロップエディターを使ってパーソナライズされたインラインメッセージを作成する。これにより、ユーザーセッションの開始時に自動的に更新される、邪魔にならず文脈に応じた体験を提供できる。 

#### ダイナミック BCC

{% multi_lang_include release_type.md release="General availability" %}

[ダイナミックなBCC]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc)では、BCCアドレスにLiquidを使用する。この機能は**メール設定**でのみ利用可能であり、キャンペーン自体では設定できないことに注意せよ。メールの受信者ごとに、BCCアドレスは1つだけ許可される。

#### チャネルベースのレート制限

マルチチャネルキャンペーン全体やキャンバスで共有されるレート制限の代わりに、チャネルごとに特定のレート制限を選択する。この場合、レート制限は選択した各チャネルに適用される。例えば、キャンペーンまたはキャンバス全体で、1分間に最大5,000件のWebhookと2,500件のSMSメッセージを送信するように設定する。詳細については、[レート制限とフリークエンシーキャップを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)参照のこと。

### 提携

#### LILT - ローカライゼーション

[LILTは、]({{site.baseurl}}/partners/lilt/)企業向け翻訳とコンテンツ作成のための完全なAIソリューションだ。LILTは、AIエージェントと完全オートメーションされたワークフローにより、グローバル企業がコンテンツ、製品、コミュニケーション、サポート業務を拡張・最適化することをイネーブルメントする。

### SDKの互換性を損なう更新

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - ニュースフィードを削除する。
        - ニュースフィードに関連する全てのUI要素、データモデル、およびアクションを完全に削除する。
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 2025年12月9日

### データ&レポート

#### ランディングページにGoogle Tag Managerを追加する

ランディングページにGoogle Tag Managerを追加するには、ドラッグ＆ドロップエディターでランディングページにカスタムコードブロックを追加し、そのブロックにGoogle[ Tag Managerのコードを挿入する]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page)。

### オーケストレーション

#### SMS Liquidのユースケース

[受信SMSキーワードに基づく異なるメッセージで返信する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response)ユースケースでは、ダイナミックなSMSキーワード処理を組み込み、特定の受信メッセージに対して異なるメッセージ文面で返信する。例えば、誰かが「START」と「JOIN」のどちらを送信したかによって、異なる返信を送ることができる。

#### コネクテッドコンテンツの許可リスト

特定のURLを許可リストに登録し[、コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)で使用できるようにできる。この機能を利用するには、顧客サクセスマネージャーに連絡せよ。

### チャネル&　タッチポイント

#### SMSの文字エンコーディング

[SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator)セグメント計算機に文字エンコーディング機能が追加された。**表示文字エンコーディング**を選択し、どの文字がGSM-7またはUCS-2でエンコードされているかを識別する。 

![SMSセグメント計算機。テキストボックスにサンプルSMSメッセージを入力し、文字エンコーディングを有効にした状態。]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### 最適化されたWhatsAppメッセージ

WhatsAppのMM APIは100%の配信保証を提供しないため、メッセージが届かなかったユーザーを他のチャネルでリターゲティングする方法を理解することが重要だ。 

ユーザーをリターゲティングするには、特定のメッセージを受け取らなかったユーザーセグメントを構築することを推奨する。これを行うには、エラーコードでフィルターをかける。このエラーコードは、WhatsAppのユーザーごとのマーケティングテンプレート`131049`送信制限の適用により、マーケティングテンプレートメッセージが送信されなかったことを示している。これを実現するには、[Braze Currents または SQL セグメントエクステンションを使用]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels)すればよい。

### 提携

#### その他のレベル - ダイナミックなコンテンツ

[OtherLevelsは]({{site.baseurl}}/partners/otherlevels/)、生成AIを活用する体験プラットフォームだ。スポーツブランド、出版社、運営事業者が顧客と関わる方法を変革する。従来のコンテンツを、ブランドに合ったパーソナライズされた動画やリッチメディア体験へと大規模に変換するのだ。

### SDK

#### SDKの互換性を損なう更新

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 2025年11月11日

### データの柔軟性

#### `Live Activities Push to Start Registered for App` セグメンテーションフィルター

この`Live Activities Push to Start Registered for App`フィルターは、ユーザーが特定のアプリ向けにiOSプッシュ通知を通じてライブアクティビティを開始するよう登録しているかどうかでユーザーをセグメントする。

#### RFM SQL セグメントエクステンション

[RFM（購入時期、購入頻度、購入金額）セグメントエクステンション]({{site.baseurl}}/rfm_segments/)を作成すれば、ユーザーの購買習慣を測定して優良顧客をターゲットにできる。

RFM分析とは、マーケティング手法の一つだ。ユーザーを「購入時期」「購入頻度」「購入金額」の3つのカテゴリーごとに0～3のスコアで評価し、最も良いユーザーを識別する。3が最高スコアで、0が最低スコアだ。最近性、頻度、および金額は、いずれもあなたが選択した特定の期間のデータに基づいている。

#### カスタム属性 — 値 

使用状況レポートを表示する際は、[**[値]**タブ]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab)を選択すると、約25万人のユーザーをサンプルとした、選択したカスタム属性の上位値を確認できる。

#### クラウドデータ取り込みのためのログ同期と監視

{% multi_lang_include release_type.md release="General availability" %}

クラウドデータ取り込み（CDI）[同期ログダッシュボード]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/)では、CDIが処理した全データを監視し、データの同期が正常に行われたかを確認できる。また「不正」または欠落したデータに関する問題を診断する。

#### 複数ルールによるフィーチャーフラグの段階的導入

[複数のルールを組み合わせたフィーチャーフラグの段階的導入]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts)を活用し、ユーザー評価のルールシーケンスを定義する。これにより、精密なセグメンテーションとコントロールされた機能リリースが可能となる。この方法は、同じ機能を多様なオーディエンスに展開するのに最適だ。

#### ドラッグ＆ドロップ製品ブロックのカタログフィールドへのマッピング

カタログ設定では、**商品ブロックの**切り替えを選択して、カタログ内の[特定のフィールド]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup)や情報[にマッピング]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup)できる。これにより、商品タイトル、商品URL、画像URLとして使用するフィールドを選択できる。

#### Currentsにおけるフリークエンシーキャップ中断イベント

Currentsを使用する際、チャネルのアボートイベント内で`abort_type`参照できるようになりました。これは、メッセージがフリークエンシーキャップにより中止されたことを識別し、どの中止原因となったフリークエンシーキャップルールを含んでいる。これは、フリークエンシーキャップルールを設定する方法を判断するのに役立つ。特定のCurrentsイベントの詳細については[、メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)を参照せよ。

### 強力なチャネル

#### バックグラウンド行の画像 

{% multi_lang_include release_type.md release="General availability" %}

アプリ内メッセージやランディングページには**、行のプロパティ**パネルで[背景行画像を追加]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image)できる。**バックグラウンド画像**の切り替えをオンにし、画像のURLを入力するか、[メディアライブラリー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)から画像を選択する。最後に、代替テキスト、サイズ、位置を設定し、画像が繰り返し表示されて行全体にパターンが形成されるかどうかを指定する。

![ピザのバックグラウンド画像で、横方向に繰り返しパターンがあるものだ。]({% image_buster /assets/img_archive/background_row.png %})

#### プレビューリンクをコピー

[バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional)や[メールのカスタムフッター]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer)、[メールの購読登録・配信停止ページ]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers)に**「プレビューリンクをコピー」**機能を使え。これでランダムなユーザーがコンテンツをどう見るかを確認できる共有リンクが生成される。

#### 配信を最適化した WhatsApp メッセージ

Metaの高度なAIシステムを活用し、マーケティングメッセージを最も関与する可能性が高いユーザーに届け、配信率とメッセージエンゲージメントを大幅に高める。

[最適化された配信機能を備えたWhatsAppメッセージは]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/)、Metaの新しい「[Marketing Messages Lite API」](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/)を使用して送信される。このAPIは従来のCloud APIと比較して優れたパフォーマンスを提供する。この新しい配信パイプラインは、あなたのメッセージを価値あるものと考え、受け取りたいと望むユーザーにより効果的にリーチするのに役立つ。

#### WhatsApp フロー

WhatsApp FlowメッセージをBraze キャンバスやキャンペーンに組み込む際、ユーザーがFlowを通じて送信する特定の情報を取得して活用したい場合がある。Brazeは、必要な階層化カスタム属性（NCA）スキーマを生成するために、ユーザー応答の構造に関する追加情報、特にJSON応答の期待される形状を受け取る必要がある。

[フローの応答をカスタム属性として保存し]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute)、テスト送信を完了することで、Brazeに応答構造に関する情報を提供できるようになった。

#### 編集可能なユーザープレビュー

[ランダムなユーザーまたは既存のユーザーから個々のフィールドを編集]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user)できる。これにより、メッセージ内のダイナミックなコンテンツをテストするのに役立つ。**編集**を選択すると、選択したユーザーを編集可能なカスタムユーザーに変換できる。

![「ユーザーとしてプレビュー」タブと「編集」ボタン。]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AI と ML のオートメーション

#### BrazeAI Decisioning Studio™ Go

以下の設定記事を参照することで、[BrazeAI Decisioning Studio™ ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go)Goとの連携を設定できるようになった：

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [クラヴィオ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [セールスフォース マーケティングクラウド]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Brazeエージェントの新機能

{% multi_lang_include release_type.md release="Beta" %}

[Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)をカスタマイズするには、以下の方法がある：

- エージェントが返信時に遵守すべき[ブランドガイドラインを]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines)適用する。 
- カタログを参照して、メッセージをさらにパーソナライズされた形で調整する。
- [出力形式]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)を指定することで、エージェントの出力を構造化する。
- エージェントの出力における偏差レベルに対する[温度]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature)調整。

### BrazeAI Operator™を搭載したChatGPTモデル

{% multi_lang_include release_type.md release="Beta" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)では、リクエストの種類に応じて以下のGPTモデルから選択して使用できる：

- GPT-5 ナノ
- GPT-5 mini（デフォルト）
- GPT-5

### 新しいBrazeのパートナーシップ

#### StackAdapt - 広告

[StackAdaptは]({{site.baseurl}}/partners/stackadapt/)AIを活用したマーケティングプラットフォームであり、ターゲットを絞ったパフォーマンス重視の広告を提供する。BrazeのユーザープロファイルデータをStackAdapt Data Hubに同期できる。二つのプラットフォームを連携させることで、顧客の統一的なビューを作成し、ファーストパーティデータを活用して広告のパフォーマンスを向上させることができる。

#### Cloudinary - ダイナミックなコンテンツ

[Cloudinaryは]({{site.baseurl}}/partners/cloudinary/)画像・動画プラットフォームであり、あらゆるキャンペーンにおいて、チャネルやカスタマージャーニーを横断して、大規模な画像・動画の管理、編集、最適化、配信を可能にする。Cloudinaryのメディア管理を統合してイネーブルメントすると、BrazeキャンペーンとCanvases向けにダイナミックで文脈に応じたパーソナライゼーションによるアセット配信を実現する。

#### カメレオン - AB テスト

[カメレオンは]({{site.baseurl}}/partners/kameleoon/)、実験、AIを活用したパーソナライゼーション、機能管理機能を単一の統合プラットフォームに備えた最適化ソリューションである。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - \`\`と\`\``subscribeToInAppMessage`のコールバック関数`addListener`に対するTypeScriptの型定義を修正する。`Braze.Events.IN_APP_MESSAGE_RECEIVED`
        - これらのリスナーは、新しい`InAppMessageEvent`型で適切にコールバックを返すようになった。以前は、メソッドは型`BrazeInAppMessage`を返すようにアノテーションされていたが、実際には型を返していた`String`。
         - いずれかのサブスクリプションAPIを使用している場合、このバージョンに更新した後もアプリ内メッセージの動作が変わらないことを確認せよ。サンプルコードは.`BrazeProject.tsx`を参照せよ。
    - APIの`logInAppMessageClicked`、およびは、既存の公開インター`logInAppMessageImpression`フェイス`logInAppMessageButtonClicked`に合わせるため、現在ではオブジェクト`BrazeInAppMessage`のみを受け付ける。
        - 以前は、オブジェクト`BrazeInAppMessage`と の両方を認`String`めていた。
    - `BrazeInAppMessage.toString()` 現在はJSON文字列表現ではなく、人間が読める文字列を返す。
        - アプリ内メッセージのJSON文字列表現を取得するには、. を使用する`BrazeInAppMessage.inAppMessageJsonString`。
    - iOSでは、`[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`はに移動された`[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`。
        - この新しいメソッドは、インスタンスメソッドではなくクラスメソッドになった。
    - メソッド`BrazeReactUtils`にヌル性アノテーションを追加する。
    - 以下の非推奨メソッドとプロパティをAPIから削除する：
        - `getInstallTrackingId(callback:)` 賛成して`getDeviceId`。
        - `registerAndroidPushToken(token:)` 賛成して`registerPushToken`。
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` 賛成して`setAdTrackingEnabled`。
        - `PushNotificationEvent.push_event_type` 賛成して`payload_type`。
        - `PushNotificationEvent.deeplink` 賛成して`url`。
        - `PushNotificationEvent.content_text` 賛成して`body`。
        - `PushNotificationEvent.raw_android_push_data` 賛成して`android`。
        - `PushNotificationEvent.kvp_data` 賛成して`braze_properties`。
    - ネイティブのAndroid SDKバージョンバインディングを[、Braze Android SDK 39.0.0から40.0.2へ](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新する。
- [.NET MAUI (Xamarin) SDK バージョン 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOSバインディングを[Braze SWIFT SDK 12.1.0から13.3.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。これにはXcode 26のサポートが含まれる。
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のネイティブAndroidブリッジを[39.0.0から40.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新する。
- [Braze SWIFT SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## 2025年10月14日リリース

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™は](https://www.braze.com/product/brazeai-decisioning-studio/)ABテストに代わり、あらゆる要素をパーソナライズするAI意思決定を実現する。あらゆる指標を最大化するのだ：クリック数ではなく、収益を追求する。BrazeAI Decisioning Studio™を使えば、あらゆるビジネスKPIを最適化できる。サンプルユースケースや主な機能については、専用セクション「[BrazeAI Decisioning Studio™」]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)を参照のこと。

### データの柔軟性

#### Currents の新しいイベント

これらの新しいイベントがCurr[ents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)用語集に追加された：

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

以下のCurrentsイベントに、これらの新しいフィールドが追加された：

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### 抑制リスト

{% multi_lang_include release_type.md release="General availability" %}

[抑制リストとは、]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)自動的にキャンペーンやキャンバスを受け取らないユーザーのグループである。抑制リストはセグメントフィルターによって定義される。ユーザーはフィルター条件を満たすことで抑制リストに入ったり出たりする。

#### ゼロコピーパーソナライゼーション

{% multi_lang_include release_type.md release="Early access" %}

クラウドデータ取り込み機能を使ってキャンバストリガーを同期し、[コピー不要のパーソナライゼーション]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)を実現する。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、それを送信先のキャンバスに渡す。Canvasステップには、Brazeユーザープロファイルに永続化されないパーソナライゼーションフィールドを任意で含めることができる。

#### オーディエンスパスおよび条件分岐ステップ用のキャンバスコンテキスト変数

{% multi_lang_include release_type.md release="Early access" %}

[オーディエンスパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)や[条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップでは、事前に宣言されたコンテキスト変数を使用する[コンテキスト変数フィルターを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters)できる。

### 創造性を引き出す

#### メール用のディールカード

メール本文の上部に直接、重要な取引情報を表示するために[ディールカード]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab)を使用する。これにより、受信者はオファーの詳細を素早く理解し、アクションを起こすことができる。

#### バナー用テンプレート

[バナーを作成]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create)する際、空白のテンプレートから始めるか、Brazeのテンプレートを使用するか、保存済みのバナーテンプレートを選択できるようになった。

### 強力なチャネル

#### 抑制リスト

{% multi_lang_include release_type.md release="General availability" %}
 
[除外リスト]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/)は、メッセージを受信しないユーザーグループを指定します。管理者は、セグメントフィルターを使用して除外リストを作成し、ユーザーグループをセグメンテーションと同じように絞り込むことができます。

#### LINE クリックトラッキング

{% multi_lang_include release_type.md release="General availability" %}

[LINEクリックトラッキングが]({{site.baseurl}}/line/click_tracking/)有効になっている場合、Brazeは自動的にURLを短縮し、トラッキング機能を追加し、クリックをリアルタイムで記録する。LINEが集計されたクリックデータを提供する一方で、Brazeはタイムリーで実用的な詳細なユーザー情報を提供する。このデータにより、クリック行動に基づくユーザーのセグメントや、クリックに応じたメッセージのトリガーなど、よりターゲットを絞ったセグメンテーションおよびリターゲティングストラテジを作成できます。

#### SMSとRCSボットのクリックフィルター

{% multi_lang_include release_type.md release="General availability" %}

[SMSおよびRCSボットクリックのフィルターは、]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/)疑わしいボットクリックを除外することで、キャンペーン分析とワークフローを強化する。「ボットクリック」とは、SMSやRCSメッセージ内の短縮リンクに対する自動クリックを指す。例えば、ウェブクローラー、AndroidやiOSのリンクプレビュー機能、あるいはCPaaSセキュリティソフトウェアによるクリックなどが該当する。この機能は正確なレポート作成、セグメンテーション、およびオーケストレーションを可能にし、実際のユーザーとのエンゲージメントを促進する。

#### WhatsAppの電話番号を移す

WhatsApp Businessアカウント（WABA）の電話番号と、それに関連付けられたサブスクリプショングループを[、]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/)Braze内の[別のワークスペース]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/)に移行する。

#### WhatsApp Flowsの応答メッセージとプレビュー

キャンバスでは、[返信メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses)とフローメッセージを使用するWhatsAppメッセージステップを作成できる。また、**プレビューフロー**を選択すれば、Braze内で直接フローをプレビューし、期待通りに動作するか確認できる。

#### WhatsAppの製品メッセージング

[製品メッセージは、]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/)Metaカタログから直接製品を紹介するインタラクティブなWhatsAppメッセージを送信できるようにする。

#### BrazeとWhatsAppを外部システムと統合する

WhatsAppチャネルで[AIチャットボットとライブエージェントへの引き継ぎを活用し、]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/)顧客サポート業務を効率化せよ。定型的な問い合わせをオートメーション化し、必要に応じて人間エージェントにシームレスに移行することで、応答時間を大幅に改善し、カスタマーエクスペリエンスを高めることができる。

### AI と ML のオートメーション

#### Braze エージェント

{% multi_lang_include release_type.md release="Beta" %}

[Brazeエージェントは、]({{site.baseurl}}/user_guide/brazeai/agents/)Braze内で作成できるAI搭載のヘルパーだ。エージェントはコンテンツを生成し、知的な判断を下し、データを充実させることができる。これにより、よりパーソナライズされたカスタマーエクスペリエンスを提供できるのだ。

### 新しいBrazeのパートナーシップ

#### ジャスパー - テンプレート

[Jasper]({{site.baseurl}}/partners/jasper/)とBrazeの連携により、コンテンツ作成とキャンペーン実行を効率化できる。ジャスパーを使えば、マーケティングチームは数分で高品質でブランドに合った文章を生成できる。Brazeはその後、これらのメッセージを最適なタイミングで適切なオーディエンスに届けることを可能にする。この統合はシームレスにワークフローを促進し、手作業を減らし、より強いエンゲージメント成果をもたらす。

#### Swym - ロイヤルティとリターゲティング

[Swymは]({{site.baseurl}}/partners/swym/)、ウィッシュリスト、後で保存、ギフト登録、再入荷通知を通じて、e コマースブランドが購買意欲を捉えるのを支援する。豊富な許可ベースのデータを活用すれば、超ターゲットを絞ったキャンペーンを構築し、パーソナライズされたショッピング体験を提供できる。これにより顧客のエンゲージメントを促進し、コンバージョンを向上させ、ロイヤルティを高めることができる。

### SDKのアップデート

以下のSDKアップデートがリリースされた。最新情報は以下に記載されている。その他の更新内容は、対応するSDKの変更履歴を確認することで確認できる。

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のネイティブAndroidブリッジを[37.0.0から39.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
        - GradlePluginKotlinVersionの最低必要バージョンは、現在2.1.0である。
    - [Braze SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のネイティブiOSブリッジを[12.0.0から13.2.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。これにはXcode 26のサポートが含まれる。
    - ニュースフィードのサポートを削除する。以下のAPIは削除された：
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - ネイティブ Android SDK のバージョンバインディングを[、Braze Android SDK 37.0.0 から 39.0.0 に](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新する。
    - ニュースフィードのサポートを削除する。以下のAPIは削除された：
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - [Braze SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のネイティブiOSブリッジを[12.0.0から13.2.0に](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。これにはXcode 26のサポートが含まれる。

{% enddetails %}
{% details September 16, 2025 %}

## 2025年9月16日リリース

### データの柔軟性

#### Braze データプラットフォーム

Brazeデータプラットフォームは、包括的で組み合わせ可能なデータ機能とパートナー連携の集合体だ。これにより、カスタマーライフサイクル全体にわたってパーソナライズされた効果的な体験を創出できる。データに関連する3つのタスクについて詳しく学習する： 

- [データ統合]({{site.baseurl}}/user_guide/data/unification)
- [データの有効化]({{site.baseurl}}/user_guide/data/activation)
- [データ配布]({{site.baseurl}}/user_guide/data/distribution)

#### カスタムバナーのプロパティ

{% multi_lang_include release_type.md release="Early access" %}

バナーキャンペーンのカスタムプロパティを使って、SDKを通じてキーと値のデータを取り出し、アプリの動作や外観を変更できる。詳細については、[カスタムバナーのプロパティを]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties)参照せよ。

#### トークン認証

{% multi_lang_include release_type.md release="General availability" %}

Braze コネクテッドコンテンツを使用する場合、特定の API では、ユーザー名とパスワードの代わりにトークンが必要になることがあります。Brazeは[トークン認証ヘッダー値を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication)保持する認証情報を保存できる。

#### プロモーションコード

プロモーションコードは、ユーザー更新ステップを通じてユーザープロファイルに保存できる。詳細については、[ユーザープロファイルへのプロモーションコードの保存]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile)を参照のこと。

### 創造性を引き出す

#### Brazeパイロット

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot)は、AndroidとiOS向けに公開されているアプリだ。このアプリを使えば、Brazeのダッシュボードから自分のスマートフォンにメッセージを送信できる。アプリをダウンロードし、Brazeダッシュボードへの接続を初期化し、設定を完了する手順については、[「Braze Pilotの始め方]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started)」を参照せよ。

### 新しいBrazeのパートナーシップ

#### ブリングス - 視覚的かつインタラクティブなコンテンツ

[ブリングスは]({{site.baseurl}}/partners/blings/)次世代のパーソナライズされた動画プラットフォームだ。リアルタイムでインタラクティブ、データドリブン型の動画体験を、大規模に複数のチャネルで提供することをイネーブルメントする。

#### Shopifyとサードパーティ製ツールの標準的な連携

Shopifyのオンラインストアでは、サイト上でBraze SDKをサポートするために、Brazeの標準的な統合方法を使用することを推奨する。

ただし、Google Tag Managerのようなサードパーティ製ツールの使用を好む場合もあると理解している。そこで、その方法についてのガイドを作成した。始めるには、Shopifyを[参照せよ。サードパーティによるタグ付け]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/)。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Braze Android SDK のネイティブ Android`36.0.0` ブリッジを更新する`39.0.0`。
    - Braze SWIFT SDK のネイティブ `12.0.0`iOS ブリッジを更新する`13.2.0`。これにはXcode 26のサポートが含まれる。

- [Braze SWIFT SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - `13.0.0+` SemVer 仕様のリリースを必要とするように Braze Swift SDK バインディングを更新します。これにより、Braze SDK の`13.0.0`から`14.0.0`までのあらゆるバージョンとの互換性が確保されます (11.0.0は含まれません)。

{% enddetails %}
{% details August 19, 2025 %}

## 2025年8月19日リリース

### タイムゾーンの一貫性に関する標準化をキャンバスコンテキストに適用する

{% multi_lang_include release_type.md release="Early access" %}

[Canvas Contextステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)の[早期アクセス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)に参加している場合、アクションベースのキャンバスにおけるトリガーイベントプロパティのdatetime型タイムスタンプは、常に[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)に正規化される。これについて詳しく学習したい場合は、[タイムゾーンの一貫性に関する標準化]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization)を参照せよ。

### データの柔軟性

#### セルフサービスのカスタムドメイン

{% multi_lang_include release_type.md release="General access" %}

[セルフサービスのカスタムドメイン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/)機能により、SMS、RCS、WhatsApp用の独自ドメインを、Brazeダッシュボードから直接設定・管理できる。最大10個のカスタムドメインを、一箇所で簡単に追加・監視・管理できる。

#### セグメントファネル統計

[ファネル統計の表示]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics)を選択して、そのフィルターグループの統計を表示し、追加されたフィルターがセグメント統計にどのように影響するかを確認します。その時点までの全てのフィルターに該当するユーザーの推定数と割合が表示される。フィルターグループの統計が表示されると、フィルターを変更するたびに自動的に更新されます。 

#### プッシュ通知のエンド`/campaigns/details`ポイント向けの新規応答フィールド

プッシュ`messages`通知の応答には、新たに2つのフィールドが含まれるようになった：

- `image_url`:Android通知画像、iOS通知画像、またはWeb プッシュアイコン画像の画像URL。
- `large_image_url`:Android ChromeおよびWindowsのWeb プッシュ通知用の通知画像URL。

#### 個人識別情報（PII）フィールドの定義

[特定のフィールドをPIIフィールドとして]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii)選択・[定義]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii)することは、Brazeダッシュボード上でユーザーが閲覧できる内容に影響を与えるだけであり、そのようなPIIフィールド内のユーザーデータの取り扱い方法には影響しない。

自社のプライバシー規制やポリシー、[データリテンション]({{site.baseurl}}/api/data_retention/)に関する規定など、適用される規則にダッシュボードの設定を合わせるため、法務チームに相談せよ。

#### レポートビルダーのダウンロードリンクを共有する

レポートの[ダッシュボードリンクを共有]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report)するには、**[共有]**を選択し、[**リンクを共有**]または[**メールを送信**]**もしくは[スケジュールされたメールを送信**]を選択すればよい。

### 創造性を引き出す

#### ドラッグ＆ドロップメール用のカスタムヘッダータグ

メール本文にCSSやメタデータを追加するには、タグ`<head>`を使用する。例えば、これらのタグを使ってスタイルシートやファビコンを追加できる。Liquid は  タグ`<head>`でサポートされている。

### 強力なチャネル

#### ファジーなアウトアウトのベストプラクティス

ファジーオプトアウトメッセージを慎重に設定し、サブスクライバーにとって明確でコンプライアンスに適合した、かつ好ましい体験を創出するための[ベストプラクティスセクション]({{site.baseurl}})を追加した。

#### WhatsApp フロー

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flowsは]({{site.baseurl}}/whatsapp_flows/)既存のWhatsAppチャネルを強化する機能であり、インタラクティブでダイナミックなメッセージング体験を構築することを可能にする。 

#### WhatsAppでの製品に関する問い合わせ

ユーザーは商品やカタログのメッセージに対して[、商品に関する質問]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions)で返信できる。これらは受信メッセージとして到着し、その後アクションパスで分類できる。

さらに、Brazeはこれらの質問から製品IDとカタログIDを抽出する。したがって、オートメーションを設定したり、別のチーム（例えばカスタマーサポート）に質問を転送したりする場合、これらの詳細を含めることができる。

### AI と ML のオートメーション

#### 新しいBrazeAI™のユースケース記事

BrazeAI™を最大限に活用するための新しいユースケース記事を追加した。これらのガイドは、AIをエンゲージメント戦略に適用する実践的な方法を強調している。具体的には：

- [解約予測]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case)：顧客の離反リスクを早期に識別し、迅速にアクションを取る。
- [予測イベント]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case)：主要なユーザーアクションを予測し、リアルタイムで体験を形作る。
- [レコメンデーション]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ):顧客行動に基づいて、より関連性の高いコンテンツや商品を提供する。

#### MCPサーバー

{% multi_lang_include release_type.md release="Beta" %}

[Braze MCPサーバー]({{site.baseurl}}/user_guide/brazeai/mcp_server/)は、安全で読み取り専用の接続を提供する。これにより、ClaudeやCursorといったAIツールが、個人を特定できないBrazeデータにアクセスできるようになる。これらのツールは、データを変更することなく質問に答え、傾向を分析し、インサイトを提供できる。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - 「オプション」認証エラーに対してトリガーされる`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`ように、の機能を拡張する。
        - 「必須」認証エラーと「任意」認証エラーの両方に対して、デリゲートメソッドのトリガーが`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`呼び出されるようになる。
        - 「必須」のSDK認証エラーのみを処理したい場合、このデリゲートメソッドの実装内で、`BrazeSDKAuthError.optional`がfalseであることを確認するチェックを追加せよ。
    - イネーブルメント時に発効する`Braze.Configuration.sdkAuthentication`よう、の使用方法を修正する。
        - 以前、この設定の値はSDKによって消費されず、トークンが存在する場合、常にリクエストに添付されていた。
        - このイネーブルメントが有効な場合のみ、SDKは送信ネットワークリクエストにSDK認証トークンを添付する。
    - の全プロパティ`Braze.FeatureFlag`とのプロパティの全設定は、すべて`Braze.Banner`に設定された`private`。これらのクラスのプロパティは読み取り専用になった。
    - バージョン で非推奨となった`11.4.0`プロパティ`Braze.Banner.id`を削除する。
        - 代わりに、バナーのキャンペーントラッキングIDを読み取るには`Braze.Banner.trackingId`を使用する。
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - ネイティブのAndroid SDKバージョンバインディングを[、Braze Android SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[37.0.0へ](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新する。
    - ネイティブSWIFT SDKのバージョンバインディングを[、Braze SWIFT SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[13.0.0へ](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新する。
        - この`sdkAuthenticationError`イベントのトリガーは、認証エラーが「必須」と「任意」の両方の場合に発生するようになる。
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - iOSおよびAndroidバインディング向けに.NET 9.0のサポートを追加した。
        - これにより、.NET 8.0 のサポートが削除される。
        - これには[iOS 12.2以降のバージョン](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0)が必要だ。
    - [Braze ](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)Androidのバインディングを[32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[37.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
    - iOSバインディングを[Braze SWIFT SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)から[12.1.0に](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
    - このリリースにはバナー機能のAPIが含まれているが、現在このSDKでは完全にはサポートされていない。.NET MAUI アプリでバナーを使用したい場合は、アプリに統合する前に顧客サポートマネージャーに連絡すること。
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - iOS内部実装の`enableSdk`メソッドを更新した。SWIFT SDKで非推奨となった``_requestEnableSDKOnNextAppRun`\`の代わりに\``setEnabled`:`を使用するように変更した。
    - このメソッドを呼び出す際、アプリを再起動する必要はなくなった。このメソッドが実行されると、SDKのイネーブルメントは直ちに開始される。
    - [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)からネイティブの[`36.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)Androidブリッジを更新した[`37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。

{% enddetails %}
{% details July 22, 2025 %}

## 2025年7月22日リリース

### Amazon S3 でのセキュリティイベントのエクスポート

[セキュリティイベントを]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/)クラウドストレージプロバイダーである[Amazon S3に]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/)自動的に[エクスポート]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/)できる。UTCの深夜0時に実行される日次ジョブで処理される。設定が完了すれば、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はない。

### データの柔軟性

#### CSV インポート

{% multi_lang_include release_type.md release="General availability" %}

CSVインポートを使って、Braze内のユーザー属性やカスタムイベント（`last_destination_searched``first_name`例：、など`trip_booked`）を記録・更新できる。開始するには、「[CSV インポート]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import)」を参照してください。

#### API使用アラート

{% multi_lang_include release_type.md release="General availability" %}

API使用状況アラートは、APIの使用状況を可視化する重要な手段であり、予期せぬトラフィックを事前に検知することを可能にする。これらのアラートを設定して主要なAPIリクエスト量をトラッキングすれば、リアルタイムで通知を受け取ることができ、問題がマーケティングキャンペーンに影響を与える前に解決できる。

#### ワークスペース API のレート制限

ワークスペースのAPIレート制限では、特定の取り込みエンドポイント（`/users/track`例：SDKデータ）に対してワークスペースが行えるAPIリクエストの最大数を設定できる。ワークスペースのグループ全体にレート制限を適用することもできる。つまり、そのグループ内の全ワークスペースで制限が共有される。

#### Currents の新しいイベント

これらの新しいイベントがCurrents用語集に追加された：

- [バナー中止イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [バナークリックイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [バナーインプレッションイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [バナーが表示されたイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook 失敗イベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### キャンペーン分析のデフォルトの時間範囲

[**キャンペーン分析**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/)の期間設定は、デフォルトで現在時刻から過去90日間を表示する。これは、キャンペーンが90日以上前に開始された場合、指定した期間の分析データは「0」と表示されることを意味する。古いキャンペーンの全分析データを見るには、レポートの時間範囲を調整する。

#### Canvas実験パスステップの更新された動作

もしキャンバスにアクティブな[実験]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)または進行中の[実験]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)がある場合、アクティブなキャンバスを更新すると（実験パスステップに更新しなくても）、進行中の実験は終了する。実験を再開するには、既存の実験パスをを解除して新しい実験パスを開始するか、キャンバスを複製して新しいキャンバスを起動します。 

詳細については、「[開始後のキャンバスの編集]({{site.baseurl}}/post-launch_edits/)」を参照してください。

#### エンド`/users/export/ids`ポイントに対してより高速なレート制限が利用可能だ

以下の要件を満たすことで、[/users/export/ids エンドポイントのレート制限]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit)を秒間40リクエストに増やすこともできる：

- ワークスペースにはデフォルトのレート制限（1分あたり250リクエスト）がイネーブルドされている。既存のレート制限を解除するサポートが必要な場合は、担当のBrazeアカウントマネージャーに連絡すること。
- リクエストには、受け取りたい全フィールドを列挙するfields_to_exportパラメータが含まれている。

#### メールテンプレートのエンドポイントの新しい翻訳

{% multi_lang_include release_type.md release="Early access" %}

これらのエンドポイントを使って、メールテンプレートの翻訳とロケールを表示し、更新する。

- [GET: ソース翻訳を表示する]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: メールテンプレートエンドポイントの特定の翻訳とローカライゼーションを表示する]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: メールテンプレートの全翻訳とローカライゼーションを表示する]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: メールテンプレートの翻訳を更新する]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### 創造性を引き出す

#### ランディングページ

ランディングページは、小さい画面では列を縦に積み重ねることで[、ユーザーの端末サイズに応じてレスポンシブ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page)に対応できる。これをイネーブルメントするには、レスポンシブにしたい行に列を追加し、**列のカスタマイズ**セクションで「**小さい画面では縦に積み重ねる**」をオンにする。

### 強力なチャネル

#### メールのボットフィルタリング

{% multi_lang_include release_type.md release="General availability" %}

[[メール設定]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings)] でボットフィルタリングを設定して、すべての疑わしいマシンまたはボットクリックを除外します。メールの「ボットクリック」とは、自動プログラムにより生成されたメール内のハイパーリンのクリックを指します。これらのボットクリックをフィルタリングすることで、メッセージを意図的にトリガーし、参加している受信者に配信できます。

#### 製品ブロックのドラッグ&ドロップ

{% multi_lang_include release_type.md release="Early access" %}

[ドラッグ＆ドロップエディター]({{site.baseurl}}/dnd_product_blocks/)を使えば、カスタムLiquidコードを作成する必要なく、メッセージに製品ブロックを素早く追加・設定できる。これによりシームレスに製品紹介が可能となる。ドラッグ＆ドロップによる商品ブロック機能は、現在メールでのみ利用可能だ。

#### ランディングページやアプリ内メッセージのテキスト

スパンテキストを使えば、[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page)や[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks)において、カスタムコードなしでテキストブロックに特定のスタイルを適用できる。そうするには、スタイルを適用したいテキストを選択し、**スタイルとして「spanで囲む**」を選択する。 

#### 広告をクリックしてWhatsAppへ

[WhatsAppにクリックする広告は、]({{site.baseurl}}/whatsapp_use_cases/)FacebookやInstagramなどのMeta広告から新規顧客と既存顧客の両方を効率的に誘導する方法だ。これらの広告を使って自社製品やサービスを宣伝し、同時にユーザーにWhatsAppでの存在を知らせるのだ。 

### 新しいBrazeのパートナーシップ

#### Shopify Visitory API — e コマース

Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報は Shopify に送信されます。このデータは、加盟店が来店者を把握し、よりパーソナライズされたショッピング体験を提供するための手がかりとなります。

#### オケンド — e コマース

Brazeと[Okendo]({{site.baseurl}}/partners/okendo/)の連携は、Okendoプラットフォーム内の複数の製品で機能する。これにはレビュー、ロイヤルティ、紹介、アンケート、クイズが含まれる。Okendoはカスタムイベントとユーザー属性をBrazeに送信する。これらはメッセージのパーソナライゼーションやトリガーに使用できる。

#### Lemnisk — 顧客データプラットフォーム

Brazeと[Lemnisk]({{site.baseurl}}/partners/lemnisk/)の連携により、ブランドや企業はBrazeの真の力を解き放つことができる。これはCDP主導のインテリジェンス層として機能し、プラットフォームを横断したユーザーデータをリアルタイムで統合し、収集したユーザー情報と行動をBrazeへリアルタイムで送信する。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Web SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - プロパティ、`logBannerClick`メソッド`logBannerImpressions``Banner.html`を削除した。代わりに、インプレッションとクリックのトラッキング, 追跡を自動的に処理する[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)を使用する。
    - 旧式のニュースフィード機能のサポートを終了した。これにはフィードクラスの削除と、それに伴う関連メソッドの削除が含まれる。
    - レガシーのニュースフィードカードで使用されていた作成者とカテゴリのフィールドは、サブ[`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)クラスから削除された。
    - linkTextフィールドは、[`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)カードサブクラスとそのコンストラクタからも削除された。
    - SDKが初期化されていない場合、特定のSDKメソッドが明示的にundefinedを返すことを明記するため、定義を明確化し型を更新した。これにより型指定を実際のランタイム動作に整合させた。これは、以前の（不完全な）型定義に依存していたプロジェクトに新たなTypeScriptエラーを引き起こす可能性がある。
    - アプリ内メッセージの画像（`cropType`デフォルトでは`CENTER_CROP`）は、`FullScreenMessage`アクセシビリティ向上のため、従来の`<span>`\`<IMG>\`タグではなく`<img>``<A>`タグでレンダリングされるようになった。これにより、クラスまたはその`.ab-center-cropped-img`子要素に対する既存のCSSカスタマイズが壊れる可能性がある。
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - iOS内部実装を更新した。SWIFT SDKで非推奨となった\``enableSdk`setEnabled:`_requestEnableSDKOnNextAppRun`\`の代わりに\`setEnabled:\`を使用するように変更した。
        - このメソッドを呼び出す際、アプリを再起動する必要はなくなった。このメソッドが実行されると、SDKのイネーブルメントは直ちに開始される。
    - [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)のネイティブAndroidブリッジを[36.0.0から37.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新した。
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
