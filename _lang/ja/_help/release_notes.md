---
nav_title: リリースノート
article_title: リリースノート
page_order: 4
layout: dev_guide
guide_top_header: "リリースノート"
guide_top_text: "ここでは、Brazeプラットフォームのすべての更新を見つけることができ、次の<a href='/docs/help/release_notes/#most-recent'>最新のプラットフォーム更新</a>があります。"
page_type: landing
search_rank: 1
description: "このランディングページはBrazeリリースノートのホームです。ここでは、BrazeプラットフォームおよびSDKのすべての更新情報、ならびに非推奨機能のリストを見つけることができます。"

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
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# 最新のBrazeリリースノート{#most-recent}

> Brazeは、主要な製品リリースに合わせて、毎月製品アップデートに関する情報を公開していますが、製品は週ごとにさまざまな改善が行われています。
> <br>
> <br>
> このセクションに記載されている更新に関する詳細については、アカウントマネージャーに連絡するか、[サポートチケットを開封する]({{site.baseurl}}/help/support/)。また、[SDKの変更履歴]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/)を確認して、毎月のSDKリリース、更新、および改善に関する詳細情報を確認することもできます。

## 2024年7月23日発売

### Braze Docs アップデート

#### DiátaxisとBraze Docs

私たちは、[Diátaxis](https://diataxis.fr/)というフレームワークを使用して、ドキュメントの標準化を進めています。私たちの作家や寄稿者がこの新しいフレームワークに適合するコンテンツを作成できるようにするために、各コンテンツタイプのためのテンプレートを[作成しました]({{site.baseurl}}/contributing/content_types)。

#### Braze Docsの新しいプルリクエストテンプレート

プルリクエスト（PR）テンプレートを改善し、[Braze Docsに貢献]({{site.baseurl}}/contributing/home/)しやすく、わかりやすくしました。改善の余地があると思われる場合は、PRを開封するか[問題を提出してください](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)。何でも簡単な方で！
 
### データの柔軟性

#### カスタムイベントと属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

エクスポートは[`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes)および[`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data)APIエンドポイントを通じて、もはや早期アクセスではありません。

#### 新しいCurrentsのユーザー権限

ユーザー向けに2つの新しい権限設定があります:**Currentsインテグレーションを表示**および**Currentsインテグレーションを編集**。ユーザー権限の詳細については[こちら]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)をご覧ください。 

#### Snowflakeデータリテンションポリシーの更新
 
8月27日から、個人を特定できる情報（PII）は、2年以上前のすべてのSnowflakeセキュアデータ共有イベントデータから削除されます。Snowflakeを使用する場合、リテンションポリシーが適用される前に、Snowflakeアカウントにコピーを保存することで、環境内の完全なイベントデータを保持することができます。詳細については、[Snowflakeデータリテンション]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)を参照してください。
 
### 創造性の解放

#### アプリ内の複数ページのメッセージ

{% multi_lang_include release_type.md release="一般的な可用性" %}

アプリ内メッセージにページを追加すると、オンボーディングフローやウェルカムジャーニーのように、ユーザーを順次のフローに案内できます。詳細については、[ドラッグアンドドロップを使用してアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)を参照してください。

#### Liquidを使用したリンクの短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

SMSメッセージに含まれるURLを自動的に短縮し、クリックスルーレート分析を収集するために[Liquidを使用]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening)します。試してみるには、[リンクの短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)を参照してください。

#### カタログのAPI例

配列フィールドを使用した`/catalogs`エンドポイントの例を追加しました。例を見るには、次を確認してください:

- [複数のカタログアイテムを編集]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [複数のカタログアイテムを作成する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [カタログ項目を更新する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [カタログ項目を編集]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [カタログアイテムを作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [カタログ項目を更新]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [カタログを作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### 堅牢なチャネル

### 複数のWhatsAppビジネスアカウント

{% multi_lang_include release_type.md release="一般的な可用性" %}

各ワークスペースに複数のWhatsAppビジネスアカウントとサブスクリプショングループ（および電話番号）を追加できるようになりました。詳細については、[複数のWhatsAppビジネスアカウント]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups)を参照してください。 

#### SMSの地理的許可

SMSの地理的許可は、SMSメッセージを送信できる国に対する制御を強化することにより、セキュリティを向上させ、不正なSMSトラフィックを防止します。SMSメッセージが承認された地域にのみ送信されるようにするために、国の許可リストを指定する方法については、[SMS国の許可リストの設定]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist)を参照してください。

#### LINEとBraze

{% multi_lang_include release_type.md release="ベータ" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf)は日本で最も人気のあるメッセージングアプリで、月間アクティブユーザー数は9500万人を超えています。LINEアカウントをBrazeと統合して、ゼロパーティおよびファーストパーティの顧客データを活用し、顧客の好み、行動、およびクロスチャネルのインタラクションに基づいて、適切な顧客に魅力的なLINEメッセージを送信できます。開始するには、[LINE]({{site.baseurl}}/line)を参照してください。

#### Shopify:価格の下落と再入荷

{% multi_lang_include release_type.md release="早期アクセス" %}

今、Shopifyを使用すると、[値下げ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications)や[再入荷商品]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications)のカスタム通知を作成できます。

 
### AIとMLオートメーション
 
#### 重複ユーザーのルールベースのマージ

以前は、Brazeで重複するユーザーを個別または一括で見つけてマージすることができました。これで、重複が解決される方法をコントロールするルールを作成できるようになり、最も関連性の高いユーザーが保持されます。詳細については、[ルールベースのマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)を参照してください。

#### AI Liquid アシスタント

{% multi_lang_include release_type.md release="ベータ" %}

Sage AI Liquid Assistantは、Sage AIによって提供されるチャットアシスタントで、メッセージ内容をパーソナライズするために必要なLiquidを生成するのに役立ちます。テンプレートからLiquidを生成し、パーソナライズされたLiquidの提案を受け取り、Sage AIのサポートで既存のLiquidを最適化できます。AI Liquidアシスタントは、使用されているLiquidを説明する注釈も提供するため、Liquidの理解を深め、自分で書くことを学ぶことができます。

開始するには、[AI Liquid assistant]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid)をご覧ください。
 
### SDK
 
#### Android SDK ログ

Braze Android SDK の [ ロギングドキュメント ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging) を全面的に見直し、アプリでの読みやすさと使いやすさを向上させました。また、各ログレベルの説明も追加しました。

#### iOS SDK フォアグラウンドプッシュ通知

Braze iOS SDKの`subscribeToUpdates`メソッドは、フォアグラウンドプッシュ通知が受信されたかどうかを検出できるようになりました。詳細については、[iOSプッシュ通知の統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)を参照してください。
 
#### Xamarin ドキュメントの更新
 
バージョン[4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0)以降、Braze Xamarin SDKはSWIFT SDKバインディングを使用しているため、コードスニペットと参考資料を更新しました。また、読みやすく理解しやすいようにセクションを再構成しました。確認するには、[Xamarin ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup)を参照してください。

#### SDKの更新

以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。
 
- [SWIFT SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [Web SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - 5.2.0で導入された回帰により、外部スクリプトが同期的にロードされると、HTMLインアプリメッセージが正しくレンダリングされない可能性がある問題を修正しました。
- [Web SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## 2024年6月25日発売

### 日本語のドキュメント

Braze Docsに日本語が対応しました！

![Brazeのドキュメントサイトに日本語のインターフェイスが表示される]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### データの柔軟性

#### APIトリガーキャンペーンの添付ファイル

{% multi_lang_include release_type.md release="一般的な可用性" %}

[`/campaigns/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) は現在添付ファイルをサポートしています（ちょうど `/messages/send` エンドポイント がメールの添付ファイルをサポートしているように）。 

#### 追加のデータウェアハウスサポート

{% multi_lang_include release_type.md release="早期アクセス" %}

Braze [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) は現在、BigQuery、Databricks、Redshift、および Snowflake をサポートしています。

#### WhatsApp電話番号の移行

Metaの埋め込みサインアップを使用して、WhatsAppビジネスアカウント間でWhatsAppの電話番号を移行します。WhatsApp電話番号の移行について[詳しく読む]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration)。
 
### 創造性の解放

#### デバイスによるエンゲージメント

{% multi_lang_include release_type.md release="一般的な可用性" %}

新しい**デバイス別エンゲージメント**レポートは、ユーザーがどのデバイスを使用してメールにエンゲージしているかの内訳を提供します。このデータは、モバイル、デスクトップ、タブレット、その他のデバイスタイプ全体でのメールエンゲージメントを追跡します。[レポートとメールパフォーマンスダッシュボード]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard)について詳しく学びましょう。

#### WhatsAppとSMS Liquidプロパティはキャンバスフローにあります

{% multi_lang_include release_type.md release="一般的な可用性" %}

キャンバスフローで[WhatsAppおよびSMS Liquidプロパティのサポートを追加しました]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)。今、アクションパスステップに「SMS受信メッセージを送信」または「WhatsApp受信メッセージを送信」トリガーが含まれている場合、後続のキャンバスステップにはSMSまたはWhatsApp Liquidプロパティを含めることができます。これは、キャンバスフローでイベントプロパティがどのように機能するかを反映しています。この方法を使用すると、メッセージを活用して、ユーザープロファイルおよび会話型メッセージングに関するファーストパーティデータを保存および参照できます。
 
#### パーソナライズされたパスが繰り返されるキャンバスに

{% multi_lang_include release_type.md release="早期アクセス" %}

キャンバス内のパーソナライズされたパスにより、コンバージョンの可能性に基づいて個々のユーザーのキャンバスジャーニーの任意のポイントをパーソナライズできます。現在、定期的なキャンバスに対してパーソナライズされたパスが利用可能です。[パーソナライズされた Variants]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths) について詳しく学びましょう。

#### セグメントのトラブルシューティング

セグメントを使用していますか？ここにいくつかの[トラブルシューティングの手順と考慮事項]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting)を示します。

#### Liquidハイライト

Liquidが使用する[色分け]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)を改善して、アクセシビリティガイドラインをよりよくサポートするようにしました。

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### 堅牢なチャネル

#### SMSの地理的許可

{% multi_lang_include release_type.md release="早期アクセス" %}

SMSの地理的許可は、SMSメッセージを送信できる国に対する制御を強化することにより、セキュリティを向上させ、不正なSMSトラフィックから保護します。管理者は、SMSメッセージが承認された地域にのみ送信されるように、国の許可リストを指定できるようになりました。詳細については、[SMSの地理的権限]({{site.baseurl}}/sms_geographic_permissions)を参照してください。 

![「国の許可リスト」ドロップダウンには、最も一般的な国が上部に表示されます。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### SMS/MMSのベストプラクティス

SMS/MMSに関する[Brazeのベストプラクティス<1>}、オプトアウト監視とトラフィックポンピングに関する推奨事項について詳しく学びましょう。 

#### トラッキングプッシュ購読解除

新しい[ヘルプ記事]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)をチェックして、プッシュ購読解除を追跡するためのヒントをいくつかご覧ください。

#### Shopify `checkout.liquid` 廃止

Shopify `checkout.liquid` のサポートは2024年8月に廃止が開始され、2025年8月に終了する予定です。Braze がこの移行をどのように処理するかについて[詳しく読む]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout)。 

### SDKの更新
 
以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。
 
- [SWIFT SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - 既存のフィーチャーフラグAPIを非推奨にし、将来のバージョンで削除されます:
        - `Braze.FeatureFlag.jsonStringProperty(key:)`は非推奨になりました。
        - `Braze.FeatureFlag.jsonObjectProperty(key:)`は`Braze.FeatureFlag.jsonProperty(key:)`に置き換えられました。
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo プラグイン 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOS ドキュメント

数ヶ月前、[tvOSコンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos)と[アプリ内メッセージング]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos)の記事が誤って廃止されました。これらのドキュメントは現在、Braze DocsのSWIFTセクションに再公開されています。

{% alert note %}
[寄稿者]({{site.baseurl}}/contributing/home)は、Braze Docsが現在Ruby 3.3.0で動作していることに注意する必要があります。必要に応じてRubyのバージョンをアップグレードしてください。
{% endalert %}

## 2024年5月28日発売

### ドキュメントサイトのビジュアル更新

ドキュメントWeb サイトが新しい外観になったことにお気づきかもしれません！私たちは、新しい活気に満ちたBrazeブランドのアイデンティティを反映するようにそれを刷新しました。舞台裏の様子については、[新しいブランドの発表をご覧ください。Brazeのエグゼクティブクリエイティブディレクター、Greg Erdelyi](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi)との対談。

### ポルトガル語とスペイン語のサポート

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeは現在、ポルトガル語とスペイン語の両方で利用可能です。Brazeダッシュボードの表示言語を変更するには、[言語設定]({{site.baseurl}}/user_guide/administrative/access_braze/language/)を参照してください。

### 堅牢なチャネル

#### 多言語設定

{% multi_lang_include release_type.md release="一般的な可用性" %}

マルチ言語設定を調整することにより、異なる言語や場所のユーザーに対して、すべて1つのメールメッセージ内で異なるメッセージをターゲットにすることができます。マルチ言語サポートを編集および管理するには、「マルチ言語設定の管理」ユーザー権限が必要です。メッセージにロケールを追加するには、キャンペーンを編集する権限が必要です。

#### メッセージレベルのワンクリックリスト配信停止ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

リスト配信停止ヘッダー（[RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)）のワンクリック配信停止は、受信者がメールの配信を停止する簡単な方法を提供します。このヘッダー設定を調整して、メールのメッセージレベルで適用できます。この設定の詳細については、[ワークスペースのメール配信停止ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces)を参照してください。

#### メールのサニタイズについて

Braze がメールメッセージ内の特定の種類の JavaScript を検出したときに発生するプロセスについて詳しく知るには、新しい [sanitization]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) 記事をご覧ください。その主な目的は、悪意のあるアクターが他のBrazeダッシュボードユーザーのセッションデータにアクセスするのを防ぐことです。

#### コンテンツブロックの包含数

アクティブなキャンペーンまたはキャンバスにコンテンツブロックを追加した後、コンテンツブロックライブラリーからコンテンツブロックにカーソルを合わせて[このコンテンツブロックをプレビュー]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)し、<i class="fa fa-eye preview-icon"></i> **プレビュー**アイコンを選択できます。

#### キャンバスのステータス

Brazeのダッシュボードでは、キャンバスはそのステータスによってグループ化されます。さまざまな[キャンバスのステータスと説明]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status)を確認して、それらの意味を確認してください。

### AIとMLオートメーション

#### AIコピーライティングアシスタントのブランドガイドライン

{% multi_lang_include release_type.md release="一般的な可用性" %}

AIコピーライティングアシスタントによって生成されたコピーのスタイルをカスタマイズして、ブランドの声に合わせるために、[ブランドガイドライン]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/)を作成および適用できるようになりました。異なるシナリオに対して複数のガイドラインを設定し、常に文脈に合ったトーンを確保しましょう。
 
### 新しいBrazeのパートナーシップ

#### Adikteev - 分析

Brazeと[Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/)の統合により、Adikteevのチャーン予測技術をBraze CRMキャンペーン内で活用して、優先的に高リスクのユーザーセグメントをターゲットにすることで、ユーザーリテンションを向上させることができます。
 
#### Celebrus - 分析
 
Brazeと[Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus)の統合は、Braze SDKとシームレスに統合され、Webおよびモバイルアプリチャネル全体でチャネルアクティビティデータをBrazeに提供します。これには、指定された期間にわたるデジタル資産全体の訪問者トラフィックに関する包括的な洞察が含まれます。
 
#### IAMスタジオ - メッセージテンプレート
 
Brazeと[IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/)の統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeのアプリ内メッセージに簡単に挿入でき、画像の置き換え、テキストの変更、ディープリンク設定、カスタム属性、およびイベント設定を提供します。IAM Studioを使用すると、メッセージの作成時間を短縮し、コンテンツの計画により多くの時間を割くことができます。
 
#### リーガル - インスタントチャット

Brazeと[Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/)を統合することで、すべての顧客接点でより一貫性があり、パーソナライズされた体験を提供できます。

#### トレジャーデータ - コホートインポート
 
Brazeと[トレジャーデータ]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/)の統合により、トレジャーデータからBrazeにユーザーコホートをインポートできるため、倉庫にしか存在しないデータに基づいてターゲットキャンペーンを送信できます。
 
#### Zapier - ワークフローオートメーション
 
Brazeと[Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/)のパートナーシップは、Braze APIとBraze webhookを活用して、サードパーティアプリケーションと接続し、さまざまなアクションを自動化します。

### SDKの更新
 
以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment SWIFT Plugin 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Braze Swift SDK バインディングを更新して、9.2.0+ SemVer デノミネーションからのリリースを要求します。
        - これにより、9.2.0から10.0.0未満の任意のバージョンのBraze SDKとの互換性が可能になります。
        - 潜在的な破壊的変更に関する詳細については、[7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700)、[8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)、および[9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900)の変更履歴エントリを参照してください。
    - プッシュ通知サポートは、アプリのライフサイクルの早い段階で、アプリケーションの`AppDelegate.application(_:didFinishLaunchingWithOptions:)`メソッド内で、できるだけ早く静的メソッド`BrazeDestination.prepareForDelayedInitialization()`を呼び出す必要があります。
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOSブリッジを[Braze SWIFT SDK 7.7.0から9.0.0に更新しました](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
- [エキスポプラグイン2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [SWIFT SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - ネイティブiOSブリッジを[Braze SWIFT SDK 7.7.0から9.0.0に更新しました](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
    - ネイティブAndroidブリッジを[Braze Android SDK 29.0.1から30.3.0に](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)更新しました。
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK バージョン 5.0.0
    - iOSバインディングを[Braze SWIFT SDK 8.4.0から9.0.0に更新しました](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。

## 2024年4月30日発売

### プロモーションコードリストを作成または更新する権限

2024年4月現在、ユーザーは「キャンペーン、キャンバス、カード、セグメント、メディアライブラリー」権限を持っている必要があります。プロモーションコードリストを作成または更新するために。[制限付きおよびチームロールの権限管理]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)を参照して、権限名とその説明のリストを確認してください。

### データの柔軟性

#### SAMLジャストインタイムプロビジョニング

{% multi_lang_include release_type.md release="早期アクセス" %}

[ジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)はSAML SSOと連携して、新しいダッシュボードユーザーが初回サインイン時にBrazeアカウントを作成できるようにします。これにより、管理者が新しいダッシュボードユーザーのアカウントを手動で作成し、権限を選択し、ワークスペースに割り当て、アカウントを有効化するのを待つ必要がなくなります。

#### 権限セットと役割

特定の主題領域やアクションに関連する権限をバンドルするには、[permission sets]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles)を使用します。これらの権限セットは、異なるワークスペースで同じアクセスが必要なダッシュボードユーザーに適用できます。

#### クラウドデータ取り込みセグメント

Braze [Cloud Data Ingestionセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments)を使用すると、CDI接続を介して利用可能なデータを使用して独自のデータウェアハウスを直接クエリするSQLを記述し、Braze内でターゲットにできるユーザーグループを作成できます。

### 創造性の解放

### クエリビルダーテンプレート

{% multi_lang_include release_type.md release="一般的な可用性" %}

クエリビルダーテンプレートを使用して、SnowflakeのBrazeデータを使用してレポートを作成できます。レポートを作成する際に[Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/)テンプレートにアクセスするには、**Query Template**を選択します。すべてのテンプレートは過去60日間のデータを表示しますが、エディターでその値や他の値を直接編集できます。

### セグメント別パフォーマンスデータ

{% multi_lang_include release_type.md release="一般的な可用性" %}

キャンペーン、バリアント、キャンバスおよびキャンバスステップのクエリビルダーレポートテンプレートで、[パフォーマンスデータをセグメント別に分解できます]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)。

### 堅牢なチャネル

#### SMSメッセージングの自動リンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

自動リンク短縮を使用して、応答内の静的URLを自動的に短縮します。これにより、文字カウンターが更新され、短縮されたURLの予想される長さが表示されるため、応答を調整するのに役立ちます。

### 新しいBrazeのパートナーシップ

#### Friendbuy - ロイヤルティ

Brazeと[Friendbuy]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/)の統合を活用して、メールおよびSMSの機能を拡張し、紹介およびロイヤルティプログラムのコミュニケーションを簡単に自動化しましょう。Brazeは、Friendbuyを介して収集されたオプトイン済みの電話番号のすべての顧客プロファイルを生成します。

### NiftyImages - ダイナミックなコンテンツ

Brazeと[NiftyImages]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/)のパートナーシップにより、既存のBrazeパーソナライゼーションタグをNiftyImagesのURLにマッピングすることで、メールキャンペーン用のダイナミックでパーソナライズされた画像を作成できます。

### SDKの更新

以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment SWIFT Plugin 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - ネイティブiOSブリッジを[Braze SWIFT SDK 7.7.0から8.4.0に更新します](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
        - iOSの最小デプロイメントターゲットが12.0に更新されました。
    - ネイティブのAndroidブリッジを[Braze Android SDK 29.0.1から30.3.0に更新します](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
    - サポートされている最小のDartバージョンは2.15.0です。
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SWIFT SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SWIFT SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - BrazeKitプライバシーマニフェストからデフォルトのプライバシートラッキングドメインを削除します。
        - Brazeの[データトラッキング機能<1>}を使用している場合は、トラッキングエンドポイントをアプリレベルのプライバシーマニフェストに手動で追加する必要があります。
        - 統合ガイダンスについては、更新された[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking)を参照してください。
    - 廃止された`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)`を削除します。
        - このメソッドは元々[リリース5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0)で非推奨になりました。
        - 新しいデリゲートメソッドに切り替えることに失敗すると、コンパイラエラーはトリガーされません。代わりに、定義した`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)`メソッドは単に呼び出されません。
- [Xamarin SDK バージョン 4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)

## 2024年4月2日発売

### WhatsApp

#### 複数のビジネスアカウント

今、複数のWhatsAppビジネスアカウントとサブスクリプショングループを各ワークスペースに追加できます。完全なウォークスルーについては、[複数のWhatsAppビジネスアカウントと電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)を参照してください。

#### レートを読む

WhatsAppは、インドの消費者から始めて、より価値のある体験を創造し、企業のマーケティング会話におけるエンゲージメントを最大化するための新しいアプローチをテストしています。これには、特定の期間内に任意の企業から受け取るマーケティング会話の数を制限することが含まれる場合があります。まず、読まれる可能性が低い少数の会話から始めます。詳細については、[Meta resources]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)を参照してください。

### データの柔軟性

#### Amazon S3バケットをBrazeに同期する

{% multi_lang_include release_type.md release="早期アクセス" %}

今では、Cloud Data Ingestion for S3 を使用して、AWS アカウント内の 1 つ以上の S3 バケットを Braze と直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。詳細については、[ファイルストレージの統合]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/)を参照してください。

#### Shopify OAuth

{% multi_lang_include release_type.md release="一般的な可用性" %}

Shopifyは、あらゆる規模の小売（店）ビジネスを開始、成長、マーケティング、および管理するための信頼できるツールを提供する、世界をリードするコマース企業です。今、BrazeのためにShopifyを設定すると、[ワークスペースのOAuthを有効にすることができます]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)。

#### iOSプッシュ通知にExpoを使用する

私たちは、Expoを使用してReact Nativeでリッチプッシュ通知とPush StoriesをiOSアプリに統合するための[手順を追加しました]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo)。

#### iOSライブアクティビティのリモートスタート

今、iOSでライブアクティビティをリモートで開始するには、[エンドポイント]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/)を使用できます。完全なウォークスルーについては、[ライブアクティビティを参照してください:アクティビティ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity)を開始します。

### AIとMLオートメーション

#### アイテムのおすすめ

{% multi_lang_include release_type.md release="早期アクセス" %}

BrazeのSage AIを使用すると、最も人気のある製品を計算したり、特定のカタログに対してパーソナライズされたAI推奨を作成したりできます。詳細については、[アイテムの推奨事項について]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/)を参照してください。

#### QA アプリ内メッセージ content

{% multi_lang_include release_type.md release="一般的な可用性" %}

以前は、BrazeダッシュボードでSage AIを使用してSMSおよびプッシュ通知コンテンツの品質保証を行うことができました。今、[QAアプリ内メッセージの内容]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/)もできます。

### 新しいBrazeのパートナーシップ

#### Census - コホートインポート

BrazeからCensusにコホートユーザーを[インポートできるようになりました]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/)。Censusは、SnowflakeやBigQueryなどのクラウドデータウェアハウスをBrazeに接続するデータアクティベーションプラットフォームです。あなたのマーケティングチームは、ファーストパーティデータの力を解き放ち、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、すべてのデータをBrazeで最新の状態に保つことができます。

### SDKの更新

以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。

- [React Native 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - React Native の最小バージョンを 0.71.0 に更新しました。
  - iOSの最小バージョンを12.0に更新しました。
  - iOSバインディングを更新して、Braze SWIFT SDK 8.1.0を使用するようにしました。
  - Androidバインディングを更新して、Braze Android SDK 30.1.1を使用するようにしました。

## 2024年3月5日発売

### Google EU ユーザー Consent Policy

Googleは、2024年3月6日から施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。この今後の変更の一環として、Brazeで両方の同意シグナルをカスタム属性として[収集できます]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)。Brazeは、これらのカスタム属性からのデータをGoogleの適切な同意フィールドに同期します。

### データの柔軟性

#### 重複するユーザーをマージする

{% multi_lang_include release_type.md release="早期アクセス" %}

Brazeのダッシュボードでは、キャンペーンやCanvasの効果を最大化するために、[重複するユーザーを検索して統合することができます]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)。ユーザープロファイルを個別にマージするか、一括マージを実行して、識別子が一致するすべてのプロファイルを最新のユーザープロファイルにマージすることができます。

#### アーカイブされたコンテンツを検索

Brazeのダッシュボードで、[検索結果にアーカイブされたコンテンツを含める]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)には、**アーカイブされたコンテンツを表示**を選択できます。

#### AWS S3およびGoogle Cloud Storageのメッセージアーカイブサポート

メッセージアーカイブ[を使用して]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)、ユーザーに送信されたメッセージのコピーを保存し、アーカイブまたはコンプライアンスの目的でAWS S3バケット、Azure Blob Storageコンテナ、またはGoogle Cloud Storageバケットに保存できます。

#### SQL テーブルリファレンス

[SQLテーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を訪問して、クエリビルダーまたはSQLセグメントエクステンションを生成する際にクエリ可能なテーブルと列を確認してください。

### 創造性の解放

#### AIコピーライティングのトーンコントロール

これで、AIコピーライティングアシスタントで生成されたコピーのスタイルを決定するための[メッセージトーン]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)を選択できるようになりました。

### 堅牢なチャネル

#### カード作成

Brazeが新しいコンテンツカードキャンペーンおよびキャンバスステップのオーディエンス適格性とパーソナライゼーションを評価するタイミングを、カードが[作成されたとき]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)に指定することで選択できます。 

#### ユーザー パスのプレビュー

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザーのために作成したキャンバスの旅を体験し、受け取るタイミングとメッセージをプレビューします。これらの[テスト実行]({{site.baseurl}}/preview_user_paths/)は、キャンバスを送信する前に、メッセージが正しいオーディエンスに送信されることを保証する品質保証として機能します。

#### クイックプッシュキャンペーン

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeでプッシュキャンペーンを作成する際に、複数のプラットフォームとデバイスを選択して、[クイックプッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/)と呼ばれる単一の編集体験で、すべてのプラットフォーム向けに1つのメッセージを作成できます。この機能はキャンペーンにのみ利用可能です。

#### カスタムリスト配信停止ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

メールメッセージングに[カスタムリスト配信停止ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)を追加すると、受信者はオプトアウトできます。この方法では、独自に設定したワンクリック配信停止エンドポイントとオプションの「mailto:」を追加できます。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

#### 複数のページのアプリ内メッセージ

{% multi_lang_include release_type.md release="早期アクセス" %}

[アプリ内メッセージにページを追加すること]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page) で、オンボーディングフローやウェルカムジャーニーのような順次フローでユーザーを案内できます。**ページ**セクションの**ビルド**タブからページを管理できます。

#### 実験パスのパスをランダム化する

常に実験パスステップの[パス割り当てをランダム化する]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)には、ステップで**実験パスのランダム化されたパス**を選択します。このオプションは、勝者パスまたはパーソナライズされたパスを用いる場合は使用できません。

#### メールキャプチャフォーム

[メールキャプチャメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/)により、サイトのユーザーにメールアドレスの送信を簡単に促すことができ、その後、すべてのメッセージングキャンペーンで使用するためにユーザープロファイルで利用可能になります。

### SDKの更新
 
以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - これは、2024年3月1日にサポート終了となる前のObjective-C SDKの最終リリースとなります（[Swift SDK](https://github.com/braze-inc/braze-swift-sdk/)の使用を推奨します）。
    - SDWebImageの最低必要バージョンを5.8.2から5.18.7に更新します。このバージョンには、[プライバシーに影響を与えるSDKのリスト](https://developer.apple.com/support/third-party-SDK-requirements/)に表示されるSDWebImageのプライバシーマニフェストが含まれています。
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDK バージョン 4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Braze Android SDK 27.0.1 から 30.0.0 へのネイティブ Android ブリッジを更新しました。
    - ネイティブiOSブリッジを[Braze SWIFT SDK 6.6.0から7.6.0に更新しました](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
    - `Banner` コンテンツカードタイプの名前を`ImageOnly`に変更しました:
        - `ContentCardTypes.BANNER`から`ContentCardTypes.IMAGE_ONLY`まで
        - Android では、プロジェクト内の XML ファイルに Content Cards のバナーという単語が含まれている場合は、`image_only` に置き換える必要があります。
    - `BrazePlugin.getFeatureFlag(id)` はフィーチャーフラグが存在しない場合、`null` を返します。
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` は、リフレッシュリクエストが成功または失敗で完了したとき、そして現在のセッションから以前にキャッシュされたデータがあった場合に初回サブスクリプション時にのみトリガーされます。
    - 非推奨のメソッド`registerAppboyPushMessages`を削除しました。代わりに`setRegisteredPushToken`を使用してください。

## 2024年2月6日発売

### Brazeプライバシーマニフェスト

Brazeは、宣言されたトラッキングデータを専用の`-tracking`エンドポイントに自動的にルーティングする新しい柔軟なAPIとともに、独自のプライバシーマニフェストをリリースしました。詳細については、[Brazeプライバシーマニフェスト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)を参照してください。

### Google EU ユーザー Consent Policy

Googleは、2024年3月6日に施行される[デジタル市場法（DMA）](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に対応して、[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新しています。この新しい変更により、広告主はEEAおよび英国のエンドユーザーに特定の情報を開示し、必要な同意を得る必要があります。この今後の変更の一環として、Brazeで両方の同意シグナルをカスタム属性として[収集できます]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)。Brazeは、これらのカスタム属性からのデータをGoogleの適切な同意フィールドに同期します。

### データの柔軟性

#### Google Firebase Cloud メッセージング (FCM) API

{% multi_lang_include release_type.md release="一般的な可用性" %}

今、Googleの廃止されたクラウドメッセージングAPIから、完全にサポートされているFirebase Cloud Messaging（FCM）APIに[移行することができます]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/)。 

#### Braze Cloud Data Ingestion (CDI) エンドポイント

{% multi_lang_include release_type.md release="一般的な可用性" %}

Braze CDIエンドポイントを使用して:
- [既存の統合のリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)。
- [指定された統合の過去の同期ステータスのリストを返します]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)
- [トリガー a sync]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/) for a given integration.

#### DatabricksのBraze Cloud Data Ingestion（CDI）サポート

Brazeのカタログに対するCDIサポートが[Databricksソース]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data)で利用可能になりました。

#### 手動 SWIFT SDK 統合

統合ガイドに[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration)の記事を追加して、パッケージマネージャーを使用せずにSWIFT SDKを手動で統合する方法を説明しました。

#### 非推奨

2024年1月11日、BrazeはWindowsアプリおよびBaiduアプリからのメッセージ配信とデータ収集を停止しました。

### 創造性の解放

#### SQLセグメントエクステンションのユースケース

[SQLセグメントエクステンションのユースケース]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases)ライブラリーには、独自のSQLクエリを作成する際のインスピレーションとして使用できる、SQLセグメントエクステンションのテスト済みクエリが含まれています。

### 堅牢なチャネル

#### カスタムコードブロック

{% multi_lang_include release_type.md release="一般的な可用性" %}

[カスタムコードブロック]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code)を使用すると、アプリ内メッセージのHTML、CSS、およびJavaScriptを追加、編集、または削除できます。

#### プッシュ通知のペイロードサイズを減らす

新しいヘルプ記事[通知ペイロードサイズ]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size)は、プッシュ通知のペイロードサイズが制限を超えてキャンペーンやキャンバスステップを開始できない場合に、ペイロードサイズを削減するためのいくつかのヒントを提供します。

#### キャンペーンまたはキャンバスにBCCアドレスを追加

{% multi_lang_include release_type.md release="一般的な可用性" %}

メールメッセージに[BCCアドレス]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings)を追加できます。これにより、ユーザーが受信したメッセージの同一コピーがBCC受信トレイに送信されます。これにより、コンプライアンス要件や顧客サポートの問題のために、ユーザーに送信したメッセージのコピーを保持できます。

#### ワンクリックでメールの配信停止リンク

リスト配信停止ヘッダーを使用すると、受信者はメールボックスのUI内に**配信停止**ボタンを表示することで、マーケティングメールからワンクリックで配信停止できます。

### 新しいBrazeのパートナーシップ

#### Criteo - キャンバス オーディエンス シンク

[BrazeオーディエンスSyncをCriteoに使用することで]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/)、ブランドは独自のBraze統合からのユーザーデータをCriteoの顧客リストに追加し、行動トリガー、セグメンテーションなどに基づいて広告を配信することができます。Braze キャンバスでユーザーデータに基づいてメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する任意の基準を、Criteo顧客リスト内のそのユーザーに広告をトリガーするために使用できるようになりました。

#### Movable Ink - ダイナミックなコンテンツ

[Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink)顧客データAPI統合により、マーケターはBrazeに保存された顧客イベントデータを活用して、Movable Ink内でパーソナライズされたコンテンツを生成できます。

#### スキューバ分析 - 分析

[Scuba 分析]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics) は、高速時系列データ用に設計されたフルスタックの機械学習対応データコラボレーション プラットフォームです。Scubaを使用すると、ユーザー（アクターとも呼ばれます）を選択的にエクスポートし、それらをBrazeプラットフォームに読み込むことができます。Scubaでは、カスタムアクターのプロパティを使用して、行動の傾向を分析し、さまざまなプラットフォームでデータを活用し、機械学習を使用して予測モデリングを実施します。

### SDKの更新
 
以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。
 
- [エキスポプラグイン2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - iOSの最小プラットフォームバージョンを`13.4`に引き上げ、[Expo SDK 50の要件](https://expo.dev/changelog/2024/01-18-sdk-50)に従います。
    - このバージョンでは、Expo SDK 50 を完全にサポートするために、Braze React Native SDK のバージョン [8.3.0+](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0) が必要です。
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - アプリ内メッセージに使用されるWebViewは`WebViewAssetLoader`を使用するように更新されました。
        - `WebSettings.allowFileAccess` は `InAppMessageHtmlBaseView` と `BrazeWebViewActivity` で false に設定されました。
        - ご自身の`InAppMessageWebViewClient`または`InAppMessageHtmlBaseView`を使用している場合は、オリジナルのクラスと比較して、実装が正しくアセットを読み込んでいることを確認してください。
        - カスタムクラスを使用していない場合、すべてが以前のように機能します。
- [Braze SWIFT SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze SWIFT SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDK バージョン 3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGetパッケージの名前が`AppboyPlatformXamariniOSBinding`から[`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/)に変更されました。
        - 更新されたパッケージを使用するには、`AppboyPlatformXamariniOSBinding;`の使用を次のように置き換えます: using Braze;
    - このバージョンでは.NET 6+の使用が必要で、Xamarinフレームワークを使用するプロジェクトのサポートが削除されます。Microsoft の Xamarin サポート終了に関するポリシーをご覧ください。
    - Androidバインディングを[Braze Android SDK 26.3.2から29.0.1に更新しました](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)。
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - このバージョンでは、iOSバインディングが[Braze SWIFT SDK](https://github.com/braze-inc/braze-swift-sdk/)を使用するように更新されます。ほとんどのiOSパブリックAPIが変更されました。使用する代替品については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)（SWIFT）を参照してください。私たちは、古い公開APIを引き続き利用するための互換性バインディングを提供します。
        - iOSバインディングは現在、複数のモジュールで構成されています:
            - **ブラゼキット:**メインSDKライブラリーは、分析およびプッシュ通知をサポートします（nuget: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)）。
            - ブラゼUI:Braze提供のアプリ内メッセージとコンテンツカードのためのユーザーインターフェイスライブラリー (nuget: [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI))。
            - ブラゼロケーション:ロケーションライブラリーは、ロケーション分析とジオフェンスモニタリングをサポートします（nuget: [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)）。
            - BrazeKitCompat:互換性ライブラリーは、4.0.0以前のAPIをサポートしています（nuget: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)）。
            - ブラゼUI互換:互換性ライブラリーは、4.0.0以前のUI APIをサポートします（nuget: [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)）。
        - 新しい統合についてはBrazeiOSMauiSampleAppを参照し、互換性モジュールの使用についてはBrazeiOSMauiCompatSampleAppを参照してください。
    - iOSバインディングを[Braze SWIFT SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)に更新しました。
    - iOSバインディングは、Xcode 15との互換性のために.NET 7を使用する必要があります。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024年1月9日発売

### 更新された Shopify 統合ドキュメント

BrazeおよびShopifyの統合ドキュメントのセクションを更新しました。更新内容は以下の通りです。

- [Shopifyの使い方を始める]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [BrazeでShopifyを設定する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [Shopify ユーザー identity management]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### データの柔軟性

#### カタログの在庫補充通知

{% multi_lang_include release_type.md release="早期アクセス" %}

カタログを通じて[再入荷通知]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)とキャンバスを組み合わせて使用することで、商品が再入荷した際に顧客に通知することができます。顧客が選択したカスタムイベントを実行するたびに、アイテムが補充されたときに通知されるように自動的に購読されます。

#### カタログセグメント

{% multi_lang_include release_type.md release="早期アクセス" %}

[カタログセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/) は、SQLセグメントエクステンションのカタログデータに基づくオーディエンスです。これらのSQLセグメントエクステンションは、Segment内で参照され、その後キャンペーンやキャンバスによってターゲットにされることができます。カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータとを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。

#### Firebase Cloud Messaging API への移行

{% multi_lang_include release_type.md release="早期アクセス" %}

Google の非推奨 Cloud メッセージング API から完全にサポートされている Firebase Cloud メッセージング (FCM) API への移行方法を学びます。

### SDKの更新

以下のSDKアップデートがリリースされました。以下に重大な更新が記載されています。その他の更新については、対応するSDKの変更ログを確認してください。

- [SWIFT SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeKit`と`BrazeLocation`のプライバシーマニフェストを追加して、Brazeのデータ収集ポリシーを説明します。詳細については、Appleのプライバシーマニフェストに関する[ドキュメント](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)を参照してください。将来のリリースで、データ収集の実践を管理するためのより多くの構成が利用可能になります。
    - 7.1.0で導入されたXCFrameworkのコード署名の問題を修正します。
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Braze Swift SDK 6.1.0 から 7.4.0 へのネイティブ iOS ブリッジを更新しました。
        - iOSリポジトリリンクは、現在この[リポジトリ](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)からの事前構築されたダイナミックなXCFrameworksを指しています。
    - ネイティブのAndroidブリッジをBraze Android SDK 27.0.1から29.0.1に更新しました。
    - `AppboyBinding.GetFeatureFlag(string id)` は、フィーチャーフラグが存在しない場合、`null` を返します。
    - `FEATURE_FLAGS_UPDATED` は、リフレッシュリクエストが成功または失敗で完了したとき、そして現在のセッションから以前にキャッシュされたデータがあった場合に初回サブスクリプション時にのみトリガーされます。