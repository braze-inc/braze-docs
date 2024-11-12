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

## 2024年7月23日リリース

### Braze Docsのアップデート

#### Diátaxis と Braze Docs

私たちは、[Diátaxis](https://diataxis.fr/)と呼ばれる枠組みを使ってドキュメントを標準化しています。ライターやコントリビューターがこの新しいフレームワークに合ったコンテンツを作成できるよう、[各コンテンツタイプのテンプレートを作成]({{site.baseurl}}/contributing/content_types)した。

#### Braze Docs の新しいプルリクエストテンプレート

私たちは、[Braze Docsに貢献する]({{site.baseurl}}/contributing/home/)のがより簡単で混乱しないように、プルリクエスト（PR）テンプレートを改善するために時間をかけた。まだ改善の余地があると思われる場合は、PR を開封するか、[問題を送信](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)してください。すべてが簡単になります。
 
### データの柔軟性

#### カスタム・イベントと属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

[`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) および[`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) API エンドポイントs によるエクスポートは、初期アクセスではなくなりました。

#### ユーザーの新しい Currents 権限

ユーザーには2つの新しい権限設定があります。\[**Currents 統合を表示する**] と \[**Currents 統合を編集する**] です。ユーザー権限の詳細については[、こちらを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)参照のこと。 

#### Snowflake データリテンションポリシーの更新
 
8月27日より、個人を特定できる情報 (PII) は、作成から2年を超えたすべての Snowflake Secure Data Sharing イベントデータから削除されます。Snowflake を使用する場合、完全なイベントデータを環境に保持するには、リテンションポリシーが適用される前に Snowflake アカウントにコピーを保存します。詳細については、[Snowflakeデータリテンション]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)を参照してください。
 
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

 
### AIとMLの自動化
 
#### 重複ユーザーのルールベースのマージ

以前は、Braze で重複するユーザーを個別または一括で検索してマージすることができました。これで、重複がどのように解決されるかをコントロールするためのルールを作成できるようになりました。そのため、最も関連性の高いユーザーが保持されます。詳細については、[ルールベースのマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)を参照してください。

#### AI Liquidアシスタント

{% multi_lang_include release_type.md release="ベータ" %}

Sage AI Liquid アシスタントは Sage AI を搭載したチャットアシスタントであり、メッセージコンテンツをパーソナライズするために必要な Liquid を生成する場合に役立ちます。テンプレートからの Liquid の生成、パーソナライズされた Liquid の提案の受け取り、および Sage AI のサポートを使用した既存の Liquid の最適化を実行できます。AI Liquid アシスタントには、使用されている Liquid を説明する注釈も用意されているため、Liquid の理解を深めたり、自作方法を学んだりできます。

開始するには、「[AI Liquid アシスタント]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid)」を参照してください。
 
### SDK
 
#### Android SDKのログ

Braze Android SDKの[ログ記録文書を見直したので、あなたのアプリで読みやすく、使いやすいです。また、各ログレベルの説明も追加した。

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

[WhatsAppおよびSMS Liquidプロパティーのサポートがキャンバスフロー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)に追加されました。アクションパスステップに \[SMS インバウンドメッセージを送信しました] または \[WhatsApp インバウンドメッセージを送信しました] トリガーが含まれている場合、後続のキャンバスステップに SMS または WhatsApp Liquid プロパティを含めることができるようになりました。これは、キャンバスフローでのイベントプロパティの動作を反映したものです。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。
 
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

#### Shopify`checkout.liquid` 非推奨

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

### AIとMLの自動化

#### AIコピーライティング・アシスタントのブランド・ガイドライン

{% multi_lang_include release_type.md release="一般的な可用性" %}

AIコピーライティングアシスタントが生成するコピーのスタイルを、ブランドの声に合わせてカスタマイズするための[ブランドガイドラインを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/)作成し、適用できるようになった。シナリオごとに複数のガイドラインを設定し、常に文脈に合ったトーンになるようにする。
 
### Braze の新しいパートナーシップ

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

## 2024年4月30日リリース

### プロモーション・コード・リストを作成または更新する権限

2024年4月以降、プロモーションコード一覧を作成・更新するには、「キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス」権限が必要となる。権限名とその説明のリストについては、[制限付きおよびチームロール権限の管理]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)を参照してください。

### データの柔軟性

#### SAMLジャストインタイム・プロビジョニング

{% multi_lang_include release_type.md release="早期アクセス" %}

[ジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)は、SAML SSO と連携して、新しいダッシュボードユーザーが初回サインイン時に Braze アカウントを作成できるようにします。これにより、管理者が新しいダッシュボード ユーザーのアカウントを手動で作成し、権限を選択してワークスペースに割り当て、アカウントの有効化を待機する必要がなくなります。

#### 権限セットとロール

[パーミッション・セットを使って]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles)、特定のサブジェクト領域やアクションに関連するパーミッションを束ねる。これらの権限セットは、異なるワークスペースにわたって同じアクセス権を必要とするダッシュボードユーザーに適用できます。

#### クラウドデータ取り込みセグメント

Braze [クラウドデータ取り込みセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments)を使用すると、CDI 接続を介して利用可能なデータを使用して独自のデータウェアハウスを直接クエリする SQL を記述し、Braze 内でターゲットにできるユーザーグループを作成できます。

### 創造性を引き出す

### クエリビルダーのテンプレート

{% multi_lang_include release_type.md release="一般的な可用性" %}

クエリービルダーテンプレートを使用して、Snowflake から Braze データを使用してレポートを作成できます。[クエリービルダー]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/)テンプレートにアクセスするには、レポートの作成時に**クエリテンプレート**を選択します。すべてのテンプレートは過去60日までのデータを表示するが、エディターで直接その値や他の値を編集することができる。

### セグメント別パフォーマンスデータ

{% multi_lang_include release_type.md release="一般的な可用性" %}

クエリビルダーレポートテンプレートでは、キャンペーン、バリアント、キャンバス、キャンバスステップの[パフォーマンスデータをセグメント別に]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)分類できます。

### 強力なチャネル

#### SMSメッセージの自動リンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

[自動リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses)機能を使って、回答中の静的URLを自動的に短縮する。文字数カウンタが更新され、短縮URLの予想される長さが表示されるからだ。

### Braze の新しいパートナーシップ

#### Friendbuy - ロイヤルティ

Brazeと[Friendbuyの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/)統合を活用して、EメールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化しよう。Braze では、Friendbuy 経由で収集されたすべてのオプトイン電話番号の顧客プロファイルが生成されます。

### NiftyImages - ダイナミックコンテンツ

Braze と[NiftyImages]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/) のパートナーシップにより、既存の Braze パーソナライゼーションタグを NiftyImages URL にマッピングすることで、メールキャンペーンのダイナミックでパーソナライズされた画像を作成できます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブ iOS ブリッジを [Braze Swift SDK 7.7.0から8.4.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
        - iOSの最小デプロイメントターゲットは12.0に更新された。
    - ネイティブ Android ブリッジを [Braze Android SDK 29.0.1から30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新します。
    - サポートされるDartの最小バージョンは2.15.0である。
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - BrazeKitのプライバシーマニフェストからデフォルトのプライバシー追跡ドメインを削除する。
        - Braze [データトラッキング機能]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/)を使用している場合は、トラッキングエンドポイントをアプリレベルのプライバシーマニフェストに手動で追加する必要があります。
        - 統合の手引きについては、更新d [チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking)を参照してください。
    - 非推奨の`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)` を削除する。
        - このメソッドは、元は[release 5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0) で非推奨になりました。
        - 新しいデリゲートメソッドへの切り替えるに失敗しても、コンパイラエラーはトリガーされません。代わりに、定義した`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` メソッドは単に呼び出されません。
- [Xamarin SDKバージョン4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)

## 2024年4月2日リリース

### WhatsApp

#### 複数のビジネスアカウント

複数の WhatsApp Business アカウントと購読グループを各ワークスペースに追加できるようになりました。詳細な手順については、「[複数の WhatsApp ビジネスアカウントと電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)」を参照してください。

#### 料金を読む

WhatsApp では、企業のマーケティング会話により、価値の高い体験を創出し、エンゲージメントを最大にする新しい手法のテストが、インドの消費者を対象に開始されました。これには、ある特定の時期に、ある企業から受け取るマーケティングの会話の回数を制限することも含まれます。これは、読まれにくい少数の会話から始まります。詳細については、[メタリソース]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)を参照してください。

### データの柔軟性

#### Amazon S3バケットをBrazeに同期する

{% multi_lang_include release_type.md release="早期アクセス" %}

S3 用のクラウドデータ取り込みを使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze と直接連携できるようになりました。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。詳細については、[ファイルストレージの統合]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/)を参照してください。

#### Shopify OAuth

{% multi_lang_include release_type.md release="一般的な可用性" %}

Shopifyは、あらゆる規模の小売ビジネスを開始し、成長させ、販売し、管理するための信頼できるツールを提供する、世界的なコマースのリーディングカンパニーである。Shopify for Brazeをセットアップすると、[ワークスペースのOAuthが有効になる]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)。

#### iOSのプッシュ通知にExpoを使う

React Nativeで Expo を使用して、リッチプッシュ通知とプッシュストーリーを iOS アプリに統合するための[手順を追加]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo)しました。

#### iOS ライブアクティビティのリモート起動

これで、[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/) エンドポイントを使用して、iOS でライブアクティビティをリモートで起動できます。詳細な手順については、「[ライブアクティビティ:アクティビティを開始する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity)」を参照してください。

### AIとMLの自動化

#### 項目の推奨事項

{% multi_lang_include release_type.md release="早期アクセス" %}

Braze による Sage AI を使用すると、最も人気のある製品を計算したり、特定のカタログのパーソナライズされた AI レコメンデーションを作成したりできます。詳細については、[項目の推奨事項について]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/)を参照してください。

#### アプリ内メッセージの内容をQAする

{% multi_lang_include release_type.md release="一般的な可用性" %}

以前は、Braze ダッシュボードで Sage AI を使用して SMS およびプッシュ通知コンテンツで品質保証を実行できました。[アプリ内メッセージの内容もQA]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/)できるようになった。

### Braze の新しいパートナーシップ

#### Census - コホートインポート

BrazeからCensusにコホートユーザーを[インポートできるようになりました]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/)。これは、SnowflakeやBigQueryのようなクラウドデータウェアハウスをBrazeに接続するデータアクティベーションプラットフォームです。マーケティングチームは、ファーストパーティデータの力を解き放ち、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、Braze 内の全てのデータを最新の状態に保つことができます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - React Nativeの最小バージョンを0.71.0に更新した。
  - iOSの最低バージョンを12.0に更新した。
  - Braze Swift SDK 8.1.0を使用するように iOS バインディングを更新しました。
  - Braze Android SDK 30.1.1を使用するように Android バインディングを更新しました。

## 2024年3月5日リリース

### Google EU ユーザー同意ポリシー

Googleは[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を[Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に応じて更新しています。これは2024年3月6日現在有効です。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。予定されているこの変更の一環として、[Braze で両方の同意シグナルをカスタム属性として収集]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)できるようになります。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### 重複ユーザーをマージする

{% multi_lang_include release_type.md release="早期アクセス" %}

Brazeのダッシュボードで、[重複ユーザーを検索してマージし]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)、キャンペーンとCanvasの効果を最大化できるようになった。ユーザープロファイルを個別にマージすることも、識別子が一致するすべてのプロファイルを最近更新されたユーザープロファイルにマージする一括マージを実行することもできます。

#### アーカイブされたコンテンツを検索する

Braze ダッシュボードで、[アーカイブされた内容を検索結果]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)に含めるには、**アーカイブされた内容を表示**を選択します。

#### AWS S3および Google Cloud Storage のメッセージアーカイブサポート

[メッセージのアーカイブ]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)を使用すると、アーカイブやコンプライアンスの目的で、ユーザーに送信したメッセージのコピーを AWS S3バケット、Azure Blob Storage コンテナー、または Google Cloud Storage バケットに保存できます。

#### SQL テーブルリファレンス

[SQLテーブル参照]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)にアクセスして、クエリビルダでクエリする、またはSQLセグメント拡張を生成するときに使用できるテーブルと列を確認します。

### 創造性を引き出す

#### AIコピーライティングのためのトーンコントロール

AIコピーライティングアシスタントで生成されるコピーのスタイルを決定するために、[メッセージトーンを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)選択できるようになった。

### 強力なチャネル

#### カード作成

カードが[作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)されるタイミングを指定することで、Braze が新しいコンテンツカードキャンペーンとキャンバスステップのオーディエンス適格性とパーソナライゼーションを評価するタイミングを選択できます。 

#### ユーザーパスをプレビューする

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザー用に作成したキャンバスジャーニーを体験しましょう。これには、受信するタイミングやメッセージのプレビューも含まれます。これらの[テスト実行]({{site.baseurl}}/preview_user_paths/)は、キャンバスを送信する前に、メッセージが適切なオーディエンスに送信されているかどうかの品質保証として機能します。

#### クイック・プッシュ・キャンペーン

{% multi_lang_include release_type.md release="一般的な可用性" %}

Braze でプッシュキャンペーンを作成する場合、[クイックプッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/) と呼ばれる単一の編集エクスペリエンスで、すべてのプラットフォームs に対して1 つのメッセージを作成する複数のプラットフォームs とデバイスを選択できます。この機能はキャンペーンでのみ利用できる。

#### カスタムの list-unsubscribe ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

[カスタムの list-unsubscribe ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)をメールメッセージングに追加すると、受信者がオプトアウトできるようになります。これにより、独自に設定したワンクリック配信停止 エンドポイントとオプションの「mailto:」を追加できます。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

#### アプリ内メッセージの複数ページ

{% multi_lang_include release_type.md release="早期アクセス" %}

[アプリ内メッセージにページを追加する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page)ことで、オンボーディングフローやウェルカムジャーニーのようなシーケンシャルなフローを通じてユーザーをガイドできます。**Build**タブの**Pages**セクションからページを管理できる。

#### 実験パスのランダム化

実験パスの[パス割り当てステップを常にランダム化]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)するには、ステップで \[**実験パスのランダムパス**] を選択します。このオプションは、勝者パスまたはパーソナライズされたパスを用いる場合は使用できません。

#### 電子メール・キャプチャ・フォーム

[ メールキャプチャメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) を使用すると、サイトのユーザーにメール住所を送信するように簡単に促すことができます。その後、すべてのメッセージング キャンペーンで使用できるように、ユーザープロファイルで使用できます。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - これは、2024年3月1日のサポート終了前の Objective-C SDK の最終リリースとなります ([Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) の使用を優先)。
    - SDWebImageの最小必要バージョンを5.8.2から5.18.7に更新した。このバージョンには、[プライバシーに影響を与えるSDK](https://developer.apple.com/support/third-party-SDK-requirements/)リストに表示されるSDWebImageのプライバシーマニフェストが含まれている。
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDKバージョン4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブ Android ブリッジを [Braze Android SDK 27.0.1から30.0.0に](https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
    - ネイティブ iOS ブリッジを [Braze Swift SDK 6.6.0から7.6.0に](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
    - `Banner` コンテンツ・カード・タイプの名前を`ImageOnly` に変更した：
        - `ContentCardTypes.BANNER` から `ContentCardTypes.IMAGE_ONLY`
        - Androidでは、プロジェクト内のXMLファイルにコンテンツカードのバナーという単語が含まれている場合、それを`image_only` に置き換える必要がある。
    - `BrazePlugin.getFeatureFlag(id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` は、更新リクエストが成功または失敗して完了したとき、および現在のセッションから過去にキャッシュされたデータがあった場合の初回のサブスクリプション時にのみトリガーされます。
    - 非推奨のメソッド`registerAppboyPushMessages` を削除しました。代わりに`setRegisteredPushToken` を使用します。

## 2024年2月6日リリース

### Brazeのプライバシーマニフェスト

Brazeは、宣言されたトラッキングデータを自動的に専用の`-tracking` エンドポイントにリルートする新しい柔軟なAPIとともに、独自のプライバシー・マニフェストをリリースした。詳細については、[Brazeプライバシーマニフェスト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)を参照してください。

### Google EU ユーザー同意ポリシー

Google は、2024年3月6日に発効した[デジタル市場法 (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) の変更に対応して、[EU ユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新します。この新しい変更により、広告主は EEA および英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。予定されているこの変更の一環として、[Braze で両方の同意シグナルをカスタム属性として収集]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)できるようになります。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### Google Firebase クラウドメッセージング(FCM) API

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Google の廃止予定の Cloud Messaging API から、完全にサポートされている Firebase Cloud Messaging (FCM) API への移行]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)が可能になります。 

#### Braze クラウドデータ取り込み (CDI) エンドポイント

{% multi_lang_include release_type.md release="一般的な可用性" %}

Braze CDI エンドポイントを使用して、以下を実行します。
- [既存の統合のリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)。
- 指定した統合の[過去の同期ステータスのリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)。
- 指定した統合の[同期をトリガーする]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)。

#### Braze クラウドデータ取り込み (CDI) での Databricks のサポート

Braze CDI で、[Databricks ソース]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data)がカタログのサポートの対象なりました。

#### 手動によるSwift SDKの統合

[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration)記事を統合ガイドに追加し、パッケージマネージャーを使用せずにSwift SDKを手動で統合する方法について説明しました。

#### 非推奨

2024年1月11日、BrazeはWindowsアプリとBaiduアプリからのメッセージ配信とデータ収集を停止した。

### 創造性を引き出す

#### SQLセグメント拡張の使用例

[SQL セグメントエクステンションユースケース]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases)ライブラリに、独自の SQL クエリの作成時にヒントとして使用できる SQL セグメントエクステンション用のテスト済みクエリが含まれています。

### 強力なチャネル

#### カスタム・コード・ブロック

{% multi_lang_include release_type.md release="一般的な可用性" %}

[カスタムコードブロックでは]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code)、アプリ内メッセージのHTML、CSS、JavaScriptを追加、編集、削除できる。

#### プッシュ通知のペイロードサイズを小さくする

新しいヘルプ記事「[Notification Payload Size（通知ペイロードサイズ]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size)）」は、プッシュペイロードサイズの制限のためにキャンペーンやキャンバスステップを開始できない場合に、プッシュ通知のペイロードサイズを小さくするためのヒントを提供する。

#### キャンペーンまたはキャンバスにBCCアドレスを追加する

{% multi_lang_include release_type.md release="一般的な可用性" %}

電子メールメッセージに[BCCアドレスを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings)付加することができる。これにより、ユーザーが受信したメッセージの同じコピーがBCC 受信トレイに送信されます。これにより、コンプライアンス要件やカスタマーサポートの問題のために、ユーザーに送信したメッセージのコピーを保持することができる。

#### ワンクリックでメール配信を停止できるリンク

[list-unsubscribeヘッダーを]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe-header)使用すると、メール本文ではなく、メールボックスのUI内に**配信停止**ボタンを表示することで、受信者がマーケティングメールからワンクリックで配信停止できるようになる。

### Braze の新しいパートナーシップ

#### Criteo - キャンバスオーディエンス同期

[Braze Audience Sync to Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/) を使用すると、ブランドは独自の Braze 統合からのユーザーデータを Criteo の顧客リストに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze キャンバスでメッセージをトリガーするために通常使用する基準 (プッシュ、メール、SMS、Webhook など) を、Criteo 顧客リスト内の該当ユーザーに対して広告をトリガーするために使用できるようになりました。

#### Movable Ink - ダイナミックコンテンツ

[Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink) 顧客データ API の統合により、マーケターは Braze に保存されている顧客イベントデータをアクティブ化して、Movable Ink 内でパーソナライズされたコンテンツを生成できます。

#### Scuba Analytics - 分析

[Scuba Analyticsは]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics)、高速時系列データ用に設計された、フルスタックの機械学習機能付きデータ・コラボレーション・プラットフォームである。Scubaでは、ユーザー（アクターとも呼ばれる）を選択的にエクスポートし、Brazeプラットフォームにロードすることができる。Scuba では、カスタムアクタープロパティを使用して動作トレンドを分析し、さまざまなプラットフォーム間でデータを有効化し、マシンラーニングを使用して予測モデリングを実行します。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Expo プラグイン2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - [Expo SDK 50の要件](https://expo.dev/changelog/2024/01-18-sdk-50)に従って、iOSの最低プラットフォームバージョンを`13.4`に上げます。
    - このバージョンでは、Expo SDK 50を完全にサポートするために、Braze React Native SDK のバージョン[8.3.0以上](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0)が必要です。
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - アプリ内メッセージに使用される WebView が、`WebViewAssetLoader`を使用するために更新されました。
        - `InAppMessageHtmlBaseView` と `BrazeWebViewActivity` で、`WebSettings.allowFileAccess` が False に設定されました。
        - 独自の`InAppMessageWebViewClient` または`InAppMessageHtmlBaseView` を使用している場合は、オリジナルのクラスと比較して、実装が正しくアセットをロードしていることを確認してほしい。
        - カスタム・クラスを使用していない場合は、すべてが以前と同じように機能する。
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDKバージョン3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGet パッケージの名前が`AppboyPlatformXamariniOSBinding` から[`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/) に変更されました。
        - 更新されたパッケージを使用するには、`AppboyPlatformXamariniOSBinding;` を使用するすべてのインスタンスを Braze を使用ように置き換えます。
    - このバージョンでは、NET 6以降を使用する必要があり、Xamarin フレームワークを使用するプロジェクトのサポートが削除されます。Xamarinのサポート終了前後の[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。
    - Android バインドを [Braze Android SDK 26.3.2から29.0.1](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)に更新しました。
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - このバージョンは、[ Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) を使用するためにiOS バインドを更新します。ほとんどのiOSパブリックAPIが変更されたため、使用するAPIの変更については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)（Swift）を参照されたい。私たちは、古いパブリックAPIを使い続けるための互換バインディングを提供している。
        - iOSバインディングは現在、複数のモジュールで構成されている：
            - **BrazeKit:**アナリティクスとプッシュ通知のサポートを提供する主なSDKライブラリ（nuget： [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)).
            - BrazeUI:Brazeが提供するアプリ内メッセージとコンテンツカード用のユーザーインターフェイスライブラリ（nuget： [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)).
            - BrazeLocation:位置情報解析とジオフェンス監視をサポートする位置情報ライブラリ（nuget： [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)).
            - BrazeKitCompat：4.0.0以前のAPIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)).
            - BrazeUICompat：4.0.0以前のUI APIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)).
        - 新しい統合についてはBrazeiOSMauiSampleAppを、互換モジュールの使用法についてはBrazeiOSMauiCompatSampleAppを参照のこと。
    - iOS バインドを[Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0) に更新しました。
    - iOS バインドでは、Xcode 15との互換性を確保するために、NET 7を使用する必要があります。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024年1月9日リリース

### Shopifyとの統合に関するドキュメントを更新

以下のようなBrazeとShopifyインテグレーションドキュメントのセクションを更新します。

- [Shopify を使い始める]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [BrazeでShopifyを設定する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [ShopifyのユーザーID管理]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### データの柔軟性

#### カタログの在庫切れ通知

{% multi_lang_include release_type.md release="早期アクセス" %}

カタログとキャンバスによる[再入荷通知]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)を組み合わせて使用​​することで、商品の再入荷時に顧客に通知できます。選択されたカスタムイベントを実行した顧客が、商品の補充時に通知を受け取れるよう自動的に配信登録できます。

#### カタログセグメント

{% multi_lang_include release_type.md release="早期アクセス" %}

[カタログセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/)は、SQL セグメントエクステンションのカタログデータに基づくユーザーのオーディエンスです。これらのSQLセグメントエクステンションは、セグメントで参照され、キャンペーンやキャンバスでターゲットにすることができる。カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータとを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。

#### Firebase Cloud Messaging API への移行

{% multi_lang_include release_type.md release="早期アクセス" %}

Google の廃止予定の Cloud Messaging API から、完全にサポートされている Firebase Cloud Messaging (FCM) API への[移行方法]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)について説明します。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeKit`および`BrazeLocation`のプライバシーマニフェストを追加して、Brazeのデータ収集ポリシーを説明します。詳細については、プライバシー・マニフェストに関するAppleの[文書を](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)参照のこと。データ収集プラクティスを管理するためのその他の設定は、今後のリリースで利用できるようになります。
    - 7.1.0で導入されたXCFrameworksのコード署名に関する問題を修正した。
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - ネイティブ iOS ブリッジを Braze Swift SDK 6.1.0から7.4.0に更新しました。
        - iOS リポジトリリンクが、この[リポジトリ](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)から事前構築済みのダイナミック XCFramework を指すようになりました。
    - ネイティブ Android ブリッジを Braze Android SDK 27.0.1から29.0.1に更新しました。
    - `AppboyBinding.GetFeatureFlag(string id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `FEATURE_FLAGS_UPDATED` は、更新リクエストが成功または失敗して完了したとき、および現在のセッションから過去にキャッシュされたデータがあった場合の初回のサブスクリプション時にのみトリガーされます。