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

> Brazeは、メジャー・プロダクト・リリースに合わせて、製品のアップデート情報を毎月リリースしているが、週ごとに雑多な改良が加えられている。
> <br>
> <br>
> このセクションに記載されているアップデートの詳細については、アカウント・マネージャーに問い合わせるか、[サポート・チケットを発行する]({{site.baseurl}}/help/support/)。また、[SDK Changelogsで]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/)、毎月のSDKのリリース、アップデート、改良に関する詳細情報を確認することができる。

## 2024年7月23日リリース

### Braze Docsのアップデート

#### ディアタクシーとブレイズ・ドックス

我々は、[Diátaxisと](https://diataxis.fr/)呼ばれるフレームワークを使ってドキュメンテーションの標準化を進めているところだ。ライターやコントリビューターがこの新しいフレームワークに合ったコンテンツを作成できるよう、[各コンテンツタイプのテンプレートを作成]({{site.baseurl}}/contributing/content_types)した。

#### Braze Docs用の新しいプル・リクエスト・テンプレート

私たちは、[Braze Docsに貢献する]({{site.baseurl}}/contributing/home/)のがより簡単で混乱しないように、プルリクエスト（PR）テンプレートを改善するために時間をかけた。それでもまだ改善の余地があると思うなら、PRを開設するか、[問題を提出する](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)こと。簡単なことなら何でもいい！
 
### データの柔軟性

#### カスタム・イベントと属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

を通じてエクスポートする。 [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes)と [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data)APIエンドポイントは早期アクセスではなくなった。

#### カレントの新しいユーザー権限

ユーザーに対する新しい権限設定が2つある：**百花繚乱の****積分を表示**し、**百花繚乱の積分を編集**する。ユーザー権限の詳細については[、こちらを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)参照のこと。 

#### Snowflakeデータ保持ポリシーの更新
 
8月27日より、2年以上前のすべてのスノーフレーク・セキュア・データ・シェアリング・イベントのデータから、個人を特定できる情報（PII）が削除される。Snowflakeを使用している場合、保持ポリシーが適用される前に、Snowflakeアカウントにコピーを保存することで、環境内の完全なイベントデータを保持することを選択することができる。詳しくは、[Snowflakeのデータ保持を]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)参照のこと。
 
### 創造性を解き放つ

#### 複数ページのアプリ内メッセージ

{% multi_lang_include release_type.md release="一般的な可用性" %}

アプリ内メッセージにページを追加することで、オンボーディングフローやウェルカムジャーニーのような連続したフローでユーザーを誘導することができる。詳しくは、[ドラッグ＆ドロップでアプリ内メッセージを作成するを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)参照のこと。

#### リンク短縮とリキッド

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Liquidを使ってURLをパーソナライズ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening)し、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルー率分析を収集する。試すには、[リンク・ショートニングを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)参照のこと。

#### カタログのAPI例

配列フィールドを使った`/catalogs` エンドポイントの例を追加した。例を見るには、以下をチェックしてほしい：

- [複数のカタログ項目を編集する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [複数のカタログ項目を作成する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [カタログ項目を更新する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [カタログ項目を編集する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [カタログ項目を作成する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [カタログ項目を更新する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [カタログを作成する]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### ロバスト・チャンネル

### 複数のWhatsAppビジネスアカウント

{% multi_lang_include release_type.md release="一般的な可用性" %}

各ワークスペースに複数のWhatsApp Businessアカウントとサブスクリプショングループ（および電話番号）を追加できるようになった。詳しくは[WhatsApp Businessアカウントを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups)ご覧下さい。 

#### SMSの地理的許可

SMS Geographic Permissionsは、SMSメッセージを送信できる国をコントロールすることで、セキュリティを強化し、不正なSMSトラフィックから保護する。SMSメッセージが承認された地域にのみ送信されるように、国の許可リストを指定する方法については、[SMS国の許可リストを設定するを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist)参照のこと。

#### LINEとブレイズ

{% multi_lang_include release_type.md release="ベータ" %}

[LINEは](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf)日本で最も人気のあるメッセージングアプリで、月間アクティブユーザー数は9500万人を超える。LINEアカウントとBrazeを統合することで、ゼロおよびファーストパーティの顧客データを活用し、顧客の嗜好、行動、クロスチャネルでのインタラクションに基づいて、適切な顧客に魅力的なLINEメッセージを送ることができる。まずは[LINEを]({{site.baseurl}}/line)ご覧いただきたい。

#### Shopifyである：値下げと再入荷

{% multi_lang_include release_type.md release="早期アクセス" %}

Shopifyでは、[値下げや]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) [再入荷商品の]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications)カスタム通知を作成できるようになった。

 
### AIとMLの自動化
 
#### 重複ユーザーのルールベースのマージ

以前は、Brazeで重複ユーザーを個別または一括で検索し、マージすることができた。重複の解決方法を制御するルールを作成し、最も関連性の高いユーザーを残すことができる。詳しくは、[ルールベースのマージを]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)参照のこと。

#### AI Liquidアシスタント

{% multi_lang_include release_type.md release="ベータ" %}

Sage AI Liquid AssistantはSage AIを搭載したチャットアシスタントで、メッセージ内容をパーソナライズするために必要なLiquidの生成をサポートする。テンプレートからリキッドを生成し、パーソナライズされたリキッドの提案を受け、セージAIのサポートで既存のリキッドを最適化することができる。AIリキッド・アシスタントは、使用されているリキッドを説明する注釈も提供するので、リキッドへの理解を深め、自分で書けるようになる。

まずは、[AIリキッド・アシスタントを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid)参照のこと。
 
### SDK
 
#### Android SDKのログ

[Braze Android SDKのロギングドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging)見直し、読みやすく、アプリで使いやすくした。また、各ログレベルの説明も追加した。

#### iOS SDKのフォアグラウンド・プッシュ通知

Braze iOS SDKの`subscribeToUpdates` メソッドが、フォアグラウンドプッシュ通知を受信したかどうかを検出できるようになった。詳しくは、[iOSプッシュ通知統合を]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)参照のこと。
 
#### Xamarinのドキュメントを更新する
 
[バージョン4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0)以降、Braze Xamarin SDKはSwift SDKバインディングを使用しているため、コードスニペットと参考資料を更新した。また、読みやすく、理解しやすいようにセクションを再構成した。確認するには、[Xamarinのドキュメントを]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup)参照のこと。

#### SDKのアップデート

以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。
 
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

[`/campaigns/trigger/send` エンド]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)ポイントが添付ファイルをサポートするようになった（ちょうど`/messages/send` エンドポイントが電子メールの添付ファイルをサポートするように）。 

#### データウェアハウスの追加サポート

{% multi_lang_include release_type.md release="早期アクセス" %}

Brazeの[Cloud Data Ingestion（CDI]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources)）は、BigQuery、Databricks、Redshift、Snowflakeをサポートするようになった。

#### WhatsAppの電話番号移行

WhatsAppビジネスアカウント間でWhatsApp電話番号を移行する。[WhatsAppの電話番号移行について]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration)もっと読む。
 
### 創造性を解き放つ

#### デバイス別エンゲージメント

{% multi_lang_include release_type.md release="一般的な可用性" %}

新レポート「**Engagement by Device**」は、ユーザーがどのデバイスを使ってメールに参加しているのかがわかる。このデータは、モバイル、デスクトップ、タブレット、その他のデバイスの種類を問わず、Eメールのエンゲージメントを追跡する。[レポートとEメールパフォーマンスダッシュボードの]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard)詳細はこちら。

#### キャンバスフローのWhatsAppとSMSリキッドプロパティ

{% multi_lang_include release_type.md release="一般的な可用性" %}

[キャンバスフローにWhatsAppとSMSリキッドプロパティの]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)サポートを追加した。アクションパスのステップが "Sent an SMS Inbound Message "または "Sent a WhatsApp Inbound Message "トリガーを含むとき、後続のキャンバスステップはSMSまたはWhatsApp Liquidプロパティを含むことができる。これは、Canvas Flowにおけるイベントプロパティの動作を反映している。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。
 
#### キャンバスに描かれたパーソナライズされた道

{% multi_lang_include release_type.md release="早期アクセス" %}

キャンバスのパーソナライズドパスでは、コンバージョンの可能性に基づいて、個々のユーザーに対してキャンバスのジャーニーの任意のポイントをパーソナライズすることができる。キャンバスにパーソナライズされたパスが追加された。[パーソナライズド・バリアントについて]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths)もっと知る。

#### セグメントのトラブルシューティング

セグメントを使うか？以下は、[トラブルシューティングの手順と留意点]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting)である。

#### リキッドハイライト

アクセシビリティ・ガイドラインをより良くサポートするために、[Liquidが使用する色分けを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)改善した。

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### ロバスト・チャンネル

#### SMSの地理的許可

{% multi_lang_include release_type.md release="早期アクセス" %}

SMSの地理的許可は、あなたがSMSメッセージを送信することができる国の制御を強制することにより、セキュリティを強化し、詐欺的なSMSトラフィックから保護する。管理者は、承認された地域にのみSMSメッセージが送信されるように、国の許可リストを指定できるようになった。詳細については、[SMS地理的許可を]({{site.baseurl}}/sms_geographic_permissions)参照のこと。 

![最も一般的な国が一番上に表示される "Country allowlist "ドロップダウン。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### SMS/MMSのベストプラクティス

オプトアウト監視やトラフィックポンプの推奨など、[Brazeを使ったSMS/MMSのベストプラクティスについて]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices)詳しく知る。 

#### プッシュ配信の停止を追跡する

プッシュ配信の停止を追跡するためのヒントについては、新しい[ヘルプ記事を]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)チェックしよう。

#### Shopify`checkout.liquid` 非推奨

Shopify`checkout.liquid` のサポートは2024年8月に非推奨となり、2025年8月に終了する。Braze がこの遷移 を処理する方法について詳しく説明します。[ 

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - 既存のFeature Flag APIは廃止され、将来のバージョンで削除される：
        - `Braze.FeatureFlag.jsonStringProperty(key:)` は非推奨となった。
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` は非推奨となり、`Braze.FeatureFlag.jsonProperty(key:)` が採用された。
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo プラグイン 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOSドキュメント

数ヶ月前、[tvOSコンテンツカードと]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) [アプリ内メッセージングの]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos)記事が誤って非推奨となった。これらのドキュメントは現在、Braze DocsのSwiftセクションで再公開されている。

{% alert note %}
Braze Docsへの[投稿]({{site.baseurl}}/contributing/home)者は、このサイトが現在Ruby 3.3.0で動作していることに注意する必要がある。必要に応じてRubyのバージョンをアップグレードしてほしい。
{% endalert %}

## 2024年5月28日リリース

### ドキュメントサイトの視覚的な更新

ドキュメンテーションのウェブサイトが新しくなったことにお気づきだろうか！私たちは、新しい活気あるブレイズのブランド・アイデンティティを反映させるために、それを刷新した。新ブランドの舞台裏については、[Unveiling Our New Brandをご覧いただきたい：Braze エグゼクティブ・クリエイティブ・ディレクター グレッグ・エルデリとの対話](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### ポルトガル語とスペイン語をサポート

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeは現在、ポルトガル語とスペイン語に対応している。Brazeダッシュボードの表示言語を変更するには、[言語設定を]({{site.baseurl}}/user_guide/administrative/access_braze/language/)参照のこと。

### ロバスト・チャンネル

#### 多言語設定

{% multi_lang_include release_type.md release="一般的な可用性" %}

[多言語設定を]({{site.baseurl}}/multi_language_support/)調整することで、異なる言語や地域のユーザーをターゲットに、1通のメールメッセージの中で異なるメッセージを送ることができる。多言語サポートを編集・管理するには、「多言語設定の管理」ユーザー権限が必要である。メッセージにロケールを追加するには、キャンペーンの編集権限が必要だ。

#### メッセージレベルのワンクリックリスト配信停止ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

list-unsubscribeヘッダーのためのワンクリックunsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))は、受信者が電子メールからオプトアウトする簡単な方法を提供する。このヘッダー設定は、メールのメッセージレベルで適用されるように調整できる。この設定の詳細については、[ワークスペースのメール配信停止ヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces)参照のこと。

#### 電子メールのサニタイズについて

Brazeがメールメッセージ内の特定の種類のJavaScriptを検出した場合に発生する処理については、新しい[サニタイズの]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization)記事を参照。その主な目的は、悪質業者が他のBrazeダッシュボードユーザーのセッションデータにアクセスするのを防ぐことである。

#### コンテンツ・ブロックの包含数

アクティブなキャンペーンまたはキャンバスにコンテンツブロックを追加した後、コンテンツブロックにカーソルを合わせ、<i class="fa fa-eye preview-icon"></i> **プレビューアイコンを**選択すると、コンテンツブロックライブラリから[このコンテンツブロックをプレビューする]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)ことができる。

#### キャンバスのステータス

Brazeのダッシュボードでは、キャンバスがステータスごとにグループ化されている。異なる[キャンバスのステータスと説明]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) を確認してください。

### AIとMLの自動化

#### AIコピーライティング・アシスタントのブランド・ガイドライン

{% multi_lang_include release_type.md release="一般的な可用性" %}

AIコピーライティングアシスタントが生成するコピーのスタイルを、ブランドの声に合わせてカスタマイズするための[ブランドガイドラインを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/)作成し、適用できるようになった。シナリオごとに複数のガイドラインを設定し、常に文脈に合ったトーンになるようにする。
 
### 新しいブレイズ・パートナーシップ

#### アディクテフ - アナリティクス

Brazeと[Adikteevの]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/)統合により、Braze CRMキャンペーン内でAdikteevの解約予測技術を活用し、リスクの高いユーザーセグメントを優先的にターゲットにすることで、ユーザーリテンションを高めることができる。
 
#### セレブラス - 分析
 
Brazeと[Celebrusの]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus)統合は、WebとモバイルアプリのチャネルでBraze SDKとシームレスに統合され、チャネルの活動データをBrazeに取り込むことを容易にする。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的な洞察も含まれる。
 
#### IAM Studio - メッセージテンプレート
 
Brazeと[IAM Studioの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/)統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeのアプリ内メッセージに簡単に挿入することができ、画像置換、テキスト変更、ディープリンク設定、カスタム属性、イベント設定を提供する。IAM Studioを使えば、メッセージ作成時間を短縮し、コンテンツプランニングにより多くの時間を割くことができる。
 
#### リーガル - インスタント・チャット

Brazeと[Regalを]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/)統合することで、すべての顧客接点において、より一貫性のあるパーソナライズされた体験を生み出すことができる。

#### トレジャーデータ - コーホートインポート
 
Brazeと[Treasure Dataの]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/)統合により、Treasure DataからBrazeにユーザーコホートをインポートすることができる。
 
#### Zapier - ワークフローの自動化
 
Brazeと[Zapierの]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/)パートナーシップは、Braze APIとBraze webhooksを活用してサードパーティアプリケーションと接続し、さまざまなアクションを自動化する。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Braze Swift SDKバインディングを更新し、9.2.0+ SemVerのリリースを必要とするようにした。
        - これにより、Braze SDKの9.2.0から10.0.0までのどのバージョンとも互換性がある。
        - 潜在的な変更点の詳細については、[7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700)、[8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)、[9.0.](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900)0の変更履歴を参照のこと。
    - プッシュ通知のサポートには、アプリのライフサイクルのできるだけ早い段階で、アプリケーションの`AppDelegate.application(_:didFinishLaunchingWithOptions:)` メソッドでスタティック・メソッド`BrazeDestination.prepareForDelayedInitialization()` を呼び出す必要がある。
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOSブリッジを[Braze Swift SDK 7.7.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Expo プラグイン 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- ユニティ 6.0.0
    - ネイティブiOSブリッジを[Braze Swift SDK 7.7.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブAndroidブリッジを[Braze Android SDK 29.0.1から30.3.0に](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDKバージョン5.0.0
    - iOSバインディングを[Braze Swift SDK 8.4.0から9.0.0に](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。

## 2024年4月30日リリース

### プロモーション・コード・リストを作成または更新する権限

2024年4月以降、プロモーションコード一覧を作成・更新するには、「キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス」権限が必要となる。権限名とその説明の一覧については、「[限定されたチーム・ロールの権限を管理する]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)」を参照のこと。

### データの柔軟性

#### SAMLジャストインタイム・プロビジョニング

{% multi_lang_include release_type.md release="早期アクセス" %}

[ジャストインタイム・プロビジョニングは]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)SAML SSOと連動し、新規ダッシュボード・ユーザーが最初のサインイン時にBrazeアカウントを作成できるようにする。これにより、管理者は新しいダッシュボード・ユーザーのアカウントを手動で作成し、権限を選択し、ワークスペースに割り当て、アカウントを有効にするのを待つ必要がなくなる。

#### パーミッション・セットとロール

[パーミッション・セットを使って]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles)、特定のサブジェクト領域やアクションに関連するパーミッションを束ねる。これらの権限セットは、異なるワークスペース間で同じアクセスを必要とするダッシュボードユーザーに適用することができる。

#### クラウドデータ収集セグメント

Braze[Cloud Data Ingestionセグメントを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments)使用すると、CDI接続を介して利用可能になったデータを使用して、独自のデータウェアハウスに直接問い合わせるSQLを記述し、Braze内でターゲットとなるユーザーグループを作成することができる。

### 創造性を解き放つ

### クエリビルダーのテンプレート

{% multi_lang_include release_type.md release="一般的な可用性" %}

Query Builderのテンプレートを使って、SnowflakeのBrazeデータを使ったレポートを作成できる。[クエリ・ビルダー・テンプレートに]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/)アクセスするには、レポート作成時に**クエリ・テンプレートを**選択する。すべてのテンプレートは過去60日までのデータを表示するが、エディターで直接その値や他の値を編集することができる。

### セグメント別パフォーマンスデータ

{% multi_lang_include release_type.md release="一般的な可用性" %}

クエリビルダーのレポートテンプレートで、キャンペーン、バリアント、キャンバス、キャンバスステップの[パフォーマンスデータをセグメント別に]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)分解できる。

### ロバスト・チャンネル

#### SMSメッセージの自動リンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

[自動リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses)機能を使って、回答中の静的URLを自動的に短縮する。文字数カウンタが更新され、短縮URLの予想される長さが表示されるからだ。

### 新しいブレイズ・パートナーシップ

#### Friendbuy - ロイヤリティ

Brazeと[Friendbuyの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/)統合を活用して、EメールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化しよう。Brazeは、Friendbuyを通じて収集したオプトイン済みの電話番号の顧客プロファイルを作成する。

### NiftyImages - ダイナミックコンテンツ

Brazeと[NiftyImagesの]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/)パートナーシップにより、既存のBrazeパーソナライズタグをNiftyImagesのURLにマッピングすることで、メールキャンペーン用にダイナミックでパーソナライズされた画像を作成することができる。

### SDKのアップデート

以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブiOSブリッジを[Braze Swift SDK 7.7.0から8.4.0に](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
        - iOSの最小デプロイメントターゲットは12.0に更新された。
    - ネイティブAndroidブリッジを[Braze Android SDK 29.0.1から30.3.0に](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - サポートされるDartの最小バージョンは2.15.0である。
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - BrazeKitのプライバシーマニフェストからデフォルトのプライバシー追跡ドメインを削除する。
        - Brazeの[データトラッキング機能を]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/)使用している場合は、アプリレベルのプライバシーマニフェストにトラッキングエンドポイントを手動で追加する必要がある。
        - 統合ガイダンスについては、更新された[チュートリアルを](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking)参照のこと。
    - 非推奨の`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)` を削除する。
        - このメソッドは[リリース5.14.](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0)0で非推奨となった。
        - 新しいデリゲート・メソッドへの切り替えに失敗しても、コンパイラー・エラーは発生しない。代わりに、あなたが定義した`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` 。
- [Xamarin SDKバージョン4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)

## 2024年4月2日リリース

### WhatsApp

#### 複数のビジネスアカウント

各ワークスペースに複数のWhatsApp Businessアカウントとサブスクリプショングループを追加できる。詳しくは[WhatsApp Businessの複数アカウントと電話]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)番号をご覧下さい。

#### 料金を読む

WhatsAppは、より価値ある体験を創造し、企業のマーケティング会話とのエンゲージメントを最大化するために、インドの消費者を対象に新しいアプローチをテストしている。これには、ある人がある期間にどの企業からもらってくるマーケティングの会話の数を制限し、読まれる可能性の低い少数の会話から始めることも含まれる。詳しくは[メタ・リソースを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)参照のこと。

### データの柔軟性

#### Amazon S3バケットをBrazeに同期する

{% multi_lang_include release_type.md release="早期アクセス" %}

Cloud Data Ingestion for S3を使用して、AWSアカウント内の1つまたは複数のS3バケットをBrazeに直接統合できるようになった。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。詳細については、[ファイル・ストレージの統合を]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/)参照のこと。

#### Shopify OAuth

{% multi_lang_include release_type.md release="一般的な可用性" %}

Shopifyは、あらゆる規模の小売ビジネスを開始し、成長させ、販売し、管理するための信頼できるツールを提供する、世界的なコマースのリーディングカンパニーである。Shopify for Brazeをセットアップすると、[ワークスペースのOAuthが有効になる]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)。

#### iOSのプッシュ通知にExpoを使う

Expo with React Nativeを使ってリッチなプッシュ通知とプッシュストーリーをiOSアプリに統合する[手順を追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo)。

#### リモート・スタート iOSライブ・アクティビティ

これで、iOS上でライブ・アクティビティをリモート・スタートできるようになった。 [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/)エンドポイントを使う。完全なウォークスルーは、[ライブ・アクティビティを参照のこと：]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity) アクティビティを開始する。

### AIとMLの自動化

#### 推奨アイテム

{% multi_lang_include release_type.md release="早期アクセス" %}

Sage AI by Brazeを使えば、最も人気のある商品を計算したり、特定のカタログに対してパーソナライズされたAIレコメンデーションを作成したりすることができる。詳しくは、[アイテムの推奨についてを]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/)参照のこと。

#### アプリ内メッセージの内容をQAする

{% multi_lang_include release_type.md release="一般的な可用性" %}

以前は、BrazeのダッシュボードでSage AIを使ってSMSやプッシュ通知のコンテンツの品質保証を行うことができた。[アプリ内メッセージの内容もQA]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/)できるようになった。

### 新しいブレイズ・パートナーシップ

#### 国勢調査 - コーホート・インポート

BrazeからCensusにコホートユーザーを[インポートできるようになりました]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/)。これは、SnowflakeやBigQueryのようなクラウドデータウェアハウスをBrazeに接続するデータアクティベーションプラットフォームです。貴社のマーケティングチームは、ファーストパーティデータの力を引き出し、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、Braze内のすべてのデータを最新の状態に保つことができる。

### SDKのアップデート

以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。

- [リアクト・ネイティブ 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - React Nativeの最小バージョンを0.71.0に更新した。
  - iOSの最低バージョンを12.0に更新した。
  - iOSバインディングを更新し、Braze Swift SDK 8.1.0を使用するようにした。
  - Braze Android SDK 30.1.1を使用するようにAndroidバインディングを更新した。

## 2024年3月5日リリース

### Google EUユーザー同意ポリシー

グーグルは、2024年3月6日から施行される[デジタル市場法（DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)）の変更に対応するため、[EUユーザー同意ポリシーを](https://www.google.com/about/company/user-consent-policy/)更新している。この新たな変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、彼らから必要な同意を得る必要がある。今度の変更の一環として、[Brazeで両方の同意シグナルをカスタム属性として収集する]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)ことができる。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### 重複ユーザーをマージする

{% multi_lang_include release_type.md release="早期アクセス" %}

Brazeのダッシュボードで、[重複ユーザーを検索してマージし]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)、キャンペーンとCanvasの効果を最大化できるようになった。ユーザ・プロフィールを個別にマージすることも、識別子が一致するすべてのプロフィールを最近更新されたユーザ・プロフィールにマージするバルク・マージを実行することもできる。

#### アーカイブされたコンテンツを検索する

Brazeダッシュボードで、**アーカイブされたコンテンツを表示するを**選択することで、[検索結果にアーカイブされたコンテンツを]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)含めることができるようになった。

#### AWS S3とGoogle Cloud Storageのメッセージ・アーカイブをサポートする

[メッセージアーカイブを]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)使用すると、アーカイブやコンプライアンス目的でユーザーに送信したメッセージのコピーをAWS S3バケット、Azure Blob Storageコンテナ、Google Cloud Storageバケットに保存できる。

#### SQL テーブルリファレンス

クエリ・ビルダーやSQL Segment Extensionsの生成時にクエリ可能なテーブルとカラムを確認するには、[SQLテーブル・リファレンスを]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)参照する。

### 創造性を解き放つ

#### AIコピーライティングのためのトーンコントロール

AIコピーライティングアシスタントで生成されるコピーのスタイルを決定するために、[メッセージトーンを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)選択できるようになった。

### ロバスト・チャンネル

#### カード作成

Brazeが新しいコンテンツカードキャンペーンとキャンバスのステップでオーディエンスの適格性とパーソナライズを評価するタイミングは、カードが[作成さ]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)れるタイミングを指定することで選択できる。 

#### ユーザーパスをプレビューする

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザーが受け取るタイミングやメッセージをプレビューするなど、ユーザーのために作成したキャンバスの旅を体験しよう。これらの[テストは]({{site.baseurl}}/preview_user_paths/)、キャンバスを送信する前に、メッセージが適切なオーディエンスに送信されているかどうかの品質保証として機能する。

#### クイック・プッシュ・キャンペーン

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeでプッシュキャンペーンを作成する際、複数のプラットフォームやデバイスを選択し、[クイックプッシュと]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/)呼ばれる1回の編集で、すべてのプラットフォーム向けに1つのメッセージを作成することができる。この機能はキャンペーンでのみ利用できる。

#### カスタムリスト-配信停止ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

メールメッセージに[カスタムリスト・アンサブスクライブヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)追加することで、受信者がオプトアウトできるようになる。この方法で、あなた自身が設定したワンクリック配信停止エンドポイントと、オプションの "mailto: "を追加することができる。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

#### アプリ内メッセージ用の複数のページ

{% multi_lang_include release_type.md release="早期アクセス" %}

[アプリ内メッセージにページを追加する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page)ことで、オンボーディングフローやウェルカムジャーニーのような連続したフローでユーザーを誘導することができる。**Build**タブの**Pages**セクションからページを管理できる。

#### 実験パスのランダム化

常に実験パスステップのパス割り当てを[ランダム化する]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)には、ステップで**実験パスのランダム化されたパス**を選択します。このオプションは、勝者パスまたはパーソナライズされたパスを用いる場合は使用できません。

#### 電子メール・キャプチャ・フォーム

[Eメールキャプチャメッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/)使えば、サイトのユーザーに簡単にEメールアドレスの送信を促すことができる。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - これは、2024年3月1日にObjective-C SDKが終了する前の最後のリリースとなる（[Swift SDKの](https://github.com/braze-inc/braze-swift-sdk/)使用が優先されるため）。
    - SDWebImageの最小必要バージョンを5.8.2から5.18.7に更新した。このバージョンには、[プライバシーに影響を与えるSDK](https://developer.apple.com/support/third-party-SDK-requirements/)リストに表示されるSDWebImageのプライバシーマニフェストが含まれている。
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [ユニティ 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDKバージョン4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブAndroidブリッジを[Braze Android SDK 27.0.1から30.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - ネイティブiOSブリッジを[Braze Swift SDK 6.6.0から7.6.0に](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
    - `Banner` コンテンツ・カード・タイプの名前を`ImageOnly` に変更した：
        - `ContentCardTypes.BANNER` への `ContentCardTypes.IMAGE_ONLY`
        - Androidでは、プロジェクト内のXMLファイルにコンテンツカードのバナーという単語が含まれている場合、それを`image_only` に置き換える必要がある。
    - `BrazePlugin.getFeatureFlag(id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` は、リフレッシュリクエストが成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがあった場合は最初のサブスクリプションのときにのみトリガーする。
    - 非推奨のメソッド`registerAppboyPushMessages` を削除した。代わりに`setRegisteredPushToken` 。

## 2024年2月6日リリース

### プライバシー・マニフェスト

Brazeは、宣言されたトラッキングデータを自動的に専用の`-tracking` エンドポイントにリルートする新しい柔軟なAPIとともに、独自のプライバシー・マニフェストをリリースした。詳細については、[Brazeのプライバシー・マニフェストを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)参照のこと。

### Google EUユーザー同意ポリシー

グーグルは、2024年3月6日に施行される[デジタル市場法（DMA](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)）の変更に対応するため、[EUユーザー同意ポリシーを](https://www.google.com/about/company/user-consent-policy/)更新している。この新たな変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、彼らから必要な同意を得る必要がある。今度の変更の一環として、[Brazeで両方の同意シグナルをカスタム属性として収集する]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)ことができる。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### Google Firebase Cloud Messaging (FCM) API

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Googleの非推奨Cloud Messaging APIから、完全にサポートされたFirebase Cloud Messaging (FCM) APIに移行]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)できるようになった。 

#### Braze Cloud Data Ingestion（CDI）エンドポイント

{% multi_lang_include release_type.md release="一般的な可用性" %}

BrazeのCDIエンドポイントを使用する：
- [既存の統合のリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)。
- 指定した統合の[過去の同期ステータスのリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)。
- 指定した統合の[同期をトリガーする]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)。

#### Braze Cloud Data Ingestion (CDI)がDatabricksをサポートする。

カタログのBraze CDIサポートが[Databricksソースで]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data)利用可能になった。

#### 手動によるSwift SDKの統合

パッケージマネージャを使用せずに手動でSwift SDKを統合する方法を説明するために、統合ガイドに[手動統合の]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration)記事を追加した。

#### 非推奨

2024年1月11日、BrazeはWindowsアプリとBaiduアプリからのメッセージ配信とデータ収集を停止した。

### 創造性を解き放つ

#### SQLセグメント拡張の使用例

[SQL Segment Extensionsユースケースライブラリには]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases)、SQL Segment Extensionsのテスト済みクエリが含まれており、独自のSQLクエリを作成する際のインスピレーションとして利用できる。

### ロバスト・チャンネル

#### カスタム・コード・ブロック

{% multi_lang_include release_type.md release="一般的な可用性" %}

[カスタムコードブロックでは]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code)、アプリ内メッセージのHTML、CSS、JavaScriptを追加、編集、削除できる。

#### プッシュ通知のペイロードサイズを小さくする

新しいヘルプ記事「[Notification Payload Size（通知ペイロードサイズ]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size)）」は、プッシュペイロードサイズの制限のためにキャンペーンやキャンバスステップを開始できない場合に、プッシュ通知のペイロードサイズを小さくするためのヒントを提供する。

#### キャンペーンまたはキャンバスにBCCアドレスを追加する

{% multi_lang_include release_type.md release="一般的な可用性" %}

電子メールメッセージに[BCCアドレスを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings)付加することができる。これは、あなたのユーザーが受信したメッセージの同一コピーを、あなたのBCC受信トレイに送信する。これにより、コンプライアンス要件やカスタマーサポートの問題のために、ユーザーに送信したメッセージのコピーを保持することができる。

#### ワンクリックでメール配信を停止できるリンク

[list-unsubscribeヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe-header)使用すると、メール本文ではなく、メールボックスのUI内に**配信停止**ボタンを表示することで、受信者がマーケティングメールからワンクリックで配信停止できるようになる。

### 新しいブレイズ・パートナーシップ

#### Criteo - キャンバス・オーディエンス・シンク

[CriteoへのBraze Audience Syncを]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/)使用することで、ブランドは、自社のBrazeインテグレーションからCriteoの顧客リストにユーザーデータを追加し、行動トリガーやセグメンテーションなどに基づいて広告を配信することができる。ユーザーデータに基づいてBraze Canvasでメッセージ（プッシュ、Eメール、SMS、ウェブフックなど）をトリガーするために通常使用するあらゆる基準を、Criteoの顧客リストでそのユーザーに広告をトリガーするために使用できるようになった。

#### ムーバブル・インク - ダイナミック・コンテンツ

[Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink)Customer Data API統合により、マーケティング担当者はBrazeに保存されている顧客イベントデータを有効化して、Movable Ink内でパーソナライズされたコンテンツを生成することができる。

#### スキューバ・アナリティクス - 分析

[Scuba Analyticsは]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics)、高速時系列データ用に設計された、フルスタックの機械学習機能付きデータ・コラボレーション・プラットフォームである。Scubaでは、ユーザー（アクターとも呼ばれる）を選択的にエクスポートし、Brazeプラットフォームにロードすることができる。スクーバでは、カスタムのアクター・プロパティを使って行動傾向を分析し、さまざまなプラットフォームでデータを活性化し、機械学習を使って予測モデリングを行う。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。
 
- [Expo プラグイン 2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - [Expo SDK 50の要件に従い](https://expo.dev/changelog/2024/01-18-sdk-50)、iOSの最小プラットフォームバージョンを`13.4` 。
    - このバージョンでは、Expo SDK 50を完全にサポートするために、Braze React Native SDKのバージョン[8.3.0以上が](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0)必要である。
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - アプリ内メッセージに使用されるWebViewが更新され、`WebViewAssetLoader` を使用するようになった。
        - `WebSettings.allowFileAccess` `InAppMessageHtmlBaseView` と`BrazeWebViewActivity` では false に設定されている。
        - 独自の`InAppMessageWebViewClient` または`InAppMessageHtmlBaseView` を使用している場合は、オリジナルのクラスと比較して、実装が正しくアセットをロードしていることを確認してほしい。
        - カスタム・クラスを使用していない場合は、すべてが以前と同じように機能する。
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDKバージョン3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGetパッケージは、`AppboyPlatformXamariniOSBinding` から次のように名前が変更された。 [`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/).
        - 更新されたパッケージを使用するには、using`AppboyPlatformXamariniOSBinding;` をusing Brazeに置き換える；
    - このバージョンでは、.NET 6+を使用する必要があり、Xamarinフレームワークを使用するプロジェクトのサポートは削除された。Xamarinのサポート終了前後の[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。
    - Androidバインディングを[Braze Android SDK 26.3.2から29.0.1に](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新。
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - このバージョンは、[Braze Swift SDKを](https://github.com/braze-inc/braze-swift-sdk/)使用するためにiOSバインディングを更新する。ほとんどのiOSパブリックAPIが変更されたため、使用するAPIの変更については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)（Swift）を参照されたい。私たちは、古いパブリックAPIを使い続けるための互換バインディングを提供している。
        - iOSバインディングは現在、複数のモジュールで構成されている：
            - **BrazeKitだ：**アナリティクスとプッシュ通知のサポートを提供する主なSDKライブラリ（nuget： [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)).
            - BrazeUIである：Brazeが提供するアプリ内メッセージとコンテンツカード用のユーザーインターフェイスライブラリ（nuget： [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)).
            - ブレイズロケーション位置情報解析とジオフェンス監視をサポートする位置情報ライブラリ（nuget： [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)).
            - BrazeKitCompat：4.0.0以前のAPIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)).
            - BrazeUICompat：4.0.0以前のUI APIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)).
        - 新しい統合についてはBrazeiOSMauiSampleAppを、互換モジュールの使用法についてはBrazeiOSMauiCompatSampleAppを参照のこと。
    - iOSバインディングを[Braze Swift SDK 7.6.0に](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)更新。
    - iOSバインディングでは、Xcode 15との互換性のために.NET 7を使用する必要がある。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024年1月9日リリース

### Shopifyとの統合に関するドキュメントを更新

BrazeとShopifyの統合ドキュメントの一部を更新した：

- [Shopifyを使い始める]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [BrazeでShopifyを設定する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [ShopifyのユーザーID管理]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### データの柔軟性

#### カタログの在庫切れ通知

{% multi_lang_include release_type.md release="早期アクセス" %}

カタログを使った[在庫切れ通知と]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)キャンバスを組み合わせることで、顧客に商品の在庫切れを通知することができる。顧客が選択したカスタムイベントを実行するたびに、その商品が補充されたときに通知されるように自動的に購読することができる。

#### カタログセグメント

{% multi_lang_include release_type.md release="早期アクセス" %}

[カタログ・セグメントは]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/)、SQL Segment Extensionsのカタログ・データに基づくユーザーのオーディエンスである。これらのSQLセグメントエクステンションは、セグメントで参照され、キャンペーンやキャンバスでターゲットにすることができる。カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータとを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。

#### Firebase Cloud Messaging API への移行

{% multi_lang_include release_type.md release="早期アクセス" %}

Googleの非推奨Cloud Messaging APIから、完全にサポートされたFirebase Cloud Messaging (FCM) APIに[移行する方法を]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)学ぶ。

### SDKのアップデート

以下のSDKアップデートがリリースされた。その他のアップデートは、対応するSDKの変更履歴を確認することで見つけることができる。

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeKit` 、`BrazeLocation` 、Brazeのデータ収集ポリシーを説明するプライバシー・マニフェストを追加する。詳細については、プライバシー・マニフェストに関するAppleの[文書を](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)参照のこと。データ収集の慣行を管理するためのより多くの設定は、将来のリリースで利用可能になる予定である。
    - 7.1.0で導入されたXCFrameworksのコード署名に関する問題を修正した。
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOSブリッジをBraze Swift SDK 6.1.0から7.4.0に更新。
        - iOSリポジトリーのリンクは、この[リポジトリーから](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)ビルド済みのダイナミックXCFrameworksを指すようになった。
    - ネイティブAndroidブリッジをBraze Android SDK 27.0.1から29.0.1に更新。
    - `AppboyBinding.GetFeatureFlag(string id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `FEATURE_FLAGS_UPDATED` は、リフレッシュリクエストが成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがあった場合は最初のサブスクリプションのときにのみトリガーする。