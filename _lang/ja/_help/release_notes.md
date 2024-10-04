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

#### ディアタクシーとBraze・ドックス

私たちは、[Diátaxis](https://diataxis.fr/)と呼ばれる枠組みを使ってドキュメントを標準化しています。ライターやコントリビューターがこの新しいフレームワークに合ったコンテンツを作成できるよう、[各コンテンツタイプのテンプレートを作成]({{site.baseurl}}/contributing/content_types)した。

#### Braze文書の新しいプルリクエストテンプレート

私たちは、[Braze Docsに貢献する]({{site.baseurl}}/contributing/home/)のがより簡単で混乱しないように、プルリクエスト（PR）テンプレートを改善するために時間をかけた。まだ改善の余地があると思われる場合は、PR を開封するか、[問題をサブミットします](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=)。なんでも簡単!
 
### データの柔軟性

#### カスタム・イベントと属性をエクスポートする

{% multi_lang_include release_type.md release="一般的な可用性" %}

[`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) および[`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) API エンドポイントs によるエクスポートは、初期アクセスではなくなりました。

#### ユーザーの新しいCurrents権限

ユーザー s には2 つの新しい権限設定があります。**Currentsの統合**と**Currentsの統合を編集します**。ユーザー権限の詳細については[、こちらを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)参照のこと。 

#### Snowflake情報リテンションポリシーへのアップデート
 
8月27日から、個人識別情報(PII)は、2歳を超えるすべてのSnowflakeセキュアデータ共有イベントデータから削除されます。Snowflake を使用する場合は、リテンションポリシーがアプリされる前にSnowflake アカウントにコピーを保存することで、環境内のイベントデータ全体を保持することを選択できます。詳細については、[Snowflakeデータリテンション]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)を参照してください。
 
### クリエイティビティのアンロック

#### 複数ページのアプリ内メッセージ

{% multi_lang_include release_type.md release="一般的な可用性" %}

アプリ内メッセージにページを追加することで、オンボーディングフローやウェルカムジャーニーのような連続したフローでユーザーを誘導することができる。詳細については、[ドラッグアンドドロップによるアプリ内メッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)を参照してください。

#### リキッドとのリンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

[Liquidを使ってURLをパーソナライズ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening)し、SMSメッセージに含まれるURLを自動的に短縮し、クリックスルー率分析を収集する。試してみるには、[リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)を参照してください。

#### カタログのAPI例

配列フィールドを使った`/catalogs` エンドポイントの例を追加した。例を見るには、以下をチェックしてほしい：

- [カタログ項目を変更する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [カタログアイテムを複数作成する]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [カタログ項目のアップデート]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [カタログアイテムのエディット]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [カタログアイテムの作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [アップデートカタログアイテム]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [カタログの作成]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### 堅牢なチャネル

### 複数のWhatsAppビジネスアカウント

{% multi_lang_include release_type.md release="一般的な可用性" %}

各ワークスペースに複数のWhatsApp Businessアカウントとサブスクリプショングループ（および電話番号）を追加できるようになった。詳しくは、[複数のWhatsApp取引先]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups)を参照してください。 

#### SMSの地理的権限

SMS Geographic Permissionsは、SMSメッセージを送信できる国をコントロールすることで、セキュリティを強化し、不正なSMSトラフィックから保護する。SMSメッセージが承認された地域にのみ送信されるように、国の許可リストを指定する方法については、[SMS国の許可リストを設定するを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist)参照のこと。

#### 線とBraze

{% multi_lang_include release_type.md release="ベータ" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) は、月間アクティブユーザー数が9500万 を超える国内で最も人気のあるメッセージング アプリです。LINE アカウントをBraze と統合することで、ゼロパーティおよびファーストパーティの顧客データを活用して、好み、動作、およびクロスチャネルののインターアクションs に基づいて、説得力のあるLINE メッセージを適切な顧客s に送信できます。開始するには、[LINE]({{site.baseurl}}/line) を参照してください。

#### Shopify:株価下落、バックインストック

{% multi_lang_include release_type.md release="早期アクセス" %}

Shopifyでは、[値下げや]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) [再入荷商品の]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications)カスタム通知を作成できるようになった。

 
### AIとMLの自動化
 
#### 重複ユーザーのルールベースのマージ

重複したユーザーをBrazeで個別または一括で見つけて結合できます。これで、重複がどのように解決されるかをコントロールするためのルールを作成できるようになりました。そのため、最も関連性の高いユーザーが保持されます。詳細については、[ルールベースのマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)を参照してください。

#### AI Liquidアシスタント

{% multi_lang_include release_type.md release="ベータ" %}

BrazeAI<sup>TM </sup>Liquid Assistant は、BrazeAI<sup>TM</sup> を搭載したチャットアシスタントで、メッセージコンテンツをパーソナライズするために必要なLiquid を生成するのに役立ちます。テンプレート s からLiquid を生成したり、パーソナライズされた Liquid の提案を受信したり、BrazeAI<sup>TM</sup> を使用して既存のLiquid を最適化したりできます。AI Liquid Assistant には、使用されているLiquid を説明するアノテーションも用意されているため、Liquid について理解を深め、自分で書くことを学ぶことができます。

開始するには、[AI Liquid assistant]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid)を参照してください。
 
### SDK
 
#### Android SDKのログ

Braze Android SDKの[ログ記録文書を見直したので、あなたのアプリで読みやすく、使いやすいです。また、各ログレベルの説明も追加した。

#### iOS SDKのフォアグラウンドプッシュ通知s

Braze iOS SDKの`subscribeToUpdates` メソッドは、フォアグラウンドプッシュ通知を受信したかどうかを検出できるようになりました。詳しくは、[iOS プッシュ通知統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)を参照してください。
 
#### Xamarinのドキュメントを更新する
 
[version 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0)であるため、Braze Xamarin SDKはSwift SDKバインディングを使用するため、コードの抜粋と参考資料を更新します。また、読みやすく、理解しやすいようにセクションを再構成した。確認するには、[Xamarin docs]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup)を参照してください。

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

[`/campaigns/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) はアタッチをサポートするようになりました(`/messages/send` エンドポイントはメールs のアタッチをサポートします)。 

#### データウェアハウスの追加サポート

{% multi_lang_include release_type.md release="早期アクセス" %}

Braze [クラウドデータ取り込み(CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources)は、BigQuery、Databricks、Redshift、およびSnowflakeをサポートするようになりました。

#### WhatsAppの電話番号移行

メタの埋め込みサインアップを使用して、WhatsAppの法人取引先間でWhatsAppの電話番号を移行します。[WhatsApp電話番号マイグレーション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration)について詳しくお読みください。
 
### クリエイティビティのアンロック

#### デバイス別エンゲージメント

{% multi_lang_include release_type.md release="一般的な可用性" %}

新レポート「**Engagement by Device**」は、ユーザーがどのデバイスを使ってメールに参加しているのかがわかる。このデータは、モバイル、デスクトップ、タブレット、および他のデバイスタイプのメール エンゲージメントを追跡します。[レポートと電子メールパフォーマンスダッシュボード]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard) について詳しく説明します。

#### キャンバスフローのWhatsAppとSMSリキッドプロパティ

{% multi_lang_include release_type.md release="一般的な可用性" %}

[WhatsAppおよびSMS Liquidプロパティーのサポートがキャンバスフロー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)に追加されました。これで、アクションパスステップに&quot が含まれている場合、SMS 受信メッセージ&quot が送信された場合、または&quot が送信された場合、後続のキャンバスステップにSMS またはWhatsApp リキッドプロパティがトリガー含まれるようになります。これは、イベントプロパティがキャンバスフローでどのように機能するかを反映します。こうすることで、メッセージを活用して、ユーザープロファイルや会話メッセージに関するファーストパーティデータを保存し、参照することができる。
 
#### 繰り返されるキャンバスのパーソナライズされたパス

{% multi_lang_include release_type.md release="早期アクセス" %}

キャンバスのパーソナライズドパスでは、コンバージョンの可能性に基づいて、個々のユーザーに対してキャンバスのジャーニーの任意のポイントをパーソナライズすることができる。これで、定期的なキャンバスでパーソナライズされたパスを使用できます。詳細については、[Personalized Variants]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths)を参照してください。

#### セグメントのトラブルシューティング

セグメントを使うか？以下は、[トラブルシューティングの手順と留意点]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting)である。

#### リキッドハイライト

アクセシビリティ・ガイドラインをより良くサポートするために、[Liquidが使用する色分けを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)改善した。

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### 堅牢なチャネル

#### SMSの地理的許可

{% multi_lang_include release_type.md release="早期アクセス" %}

SMSの地理的許可は、あなたがSMSメッセージを送信することができる国の制御を強制することにより、セキュリティを強化し、詐欺的なSMSトラフィックから保護する。管理者は、承認された地域にのみSMSメッセージが送信されるように、国の許可リストを指定できるようになった。詳細については、[SMS Geographic Permissions]({{site.baseurl}}/sms_geographic_permissions)を参照してください。 

![最も一般的な国が一番上に表示される "Country allowlist "ドロップダウン。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### SMS/MMSのベストプラクティス

オプトアウト監視やトラフィックポンプの推奨など、[Brazeを使ったSMS/MMSのベストプラクティスについて]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices)詳しく知る。 

#### プッシュ配信停止の追跡

プッシュ配信の停止を追跡するためのヒントについては、新しい[ヘルプ記事を]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)チェックしよう。

#### Shopify`checkout.liquid` 非推奨

Shopify `checkout.liquid` のサポートは、2024年8 月に非推奨になり、2025年8 月に終了することに注意してください。Braze がこの遷移 を処理する方法について詳しく説明します。[ 

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - 既存のFeature Flag API を非推奨にして、将来のバージョンで削除します。
        - `Braze.FeatureFlag.jsonStringProperty(key:)` は廃止されました。
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` は`Braze.FeatureFlag.jsonProperty(key:)` のために廃止されました。
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo プラグイン 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOSドキュメント

数か月前、[tvOS Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos)と[in-アプリ メッセージング]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos)の記事は間違って廃止された。これらのドキュメントは現在、Braze DocsのSwiftセクションで再公開されている。

{% alert note %}
Braze Doc の[寄稿者]({{site.baseurl}}/contributing/home) は、サイトがRuby 3.3.0 で実行されるようになりました。必要に応じてRubyのバージョンをアップグレードしてほしい。
{% endalert %}

## 2024年5月28日リリース

### ドキュメントサイトの視覚的な更新

ドキュメンテーションのウェブサイトが新しくなったことにお気づきだろうか！新しく生き生きとしたBrazeブランドアイデンティティを反映するように改良しました。新ブランドの舞台裏については、[Unveiling Our New Brandをご覧いただきたい：BrazeクリエイティブディレクターGreg Erdelyi](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi)との会話。

### ポルトガル語とスペイン語をサポート

{% multi_lang_include release_type.md release="一般的な可用性" %}

Brazeは現在、ポルトガル語とスペイン語に対応している。Braze ダッシュボード アプリが認識する言語を変更するには、[言語設定s]({{site.baseurl}}/user_guide/administrative/access_braze/language/)を参照してください。

### 堅牢なチャネル

#### 多言語設定

{% multi_lang_include release_type.md release="一般的な可用性" %}

[多言語設定を]({{site.baseurl}}/multi_language_support/)調整することで、異なる言語や地域のユーザーをターゲットに、1通のメールメッセージの中で異なるメッセージを送ることができる。多言語対応を編集および管理するには、"Manage Multi-Language Settings" ユーザー権限が必要です。メッセージにロケールを追加するには、キャンペーンの編集権限が必要だ。

#### メッセージレベルのワンクリックリスト-配信停止 ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

list-配信停止 ヘッダー([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))のワンクリック配信停止は、受信者 sがメール sからオプトアウトするための簡単な方法を提供します。このヘッダー設定は、メールのメッセージレベルで適用されるように調整できる。この設定の詳細については、ワークスペース sの[電子メール配信停止 ヘッダーを参照してください。

#### 電子メールのサニタイズについて

Brazeがメールメッセージ内の特定の種類のJavaScriptを検出した場合に発生する処理については、新しい[サニタイズの]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization)記事を参照。その主な目的は、悪質業者が他のBrazeダッシュボードユーザーのセッションデータにアクセスするのを防ぐことである。

#### コンテンツブロックのインクルード数

アクティブなキャンペーンまたはキャンバスにコンテンツブロックを追加した後、コンテンツブロックライブラリから[ このコンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) をプレビューするには、コンテンツブロックにマウスを合わせて<i class="fa fa-eye preview-icon"></i>**プレビュー** アイコンを選択します。

#### キャンバスのステータス

Brazeのダッシュボードでは、キャンバスがステータスごとにグループ化されている。異なる[キャンバスのステータスと説明]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) を確認してください。

### AIとMLの自動化

#### AIコピーライティング・アシスタントのブランド・ガイドライン

{% multi_lang_include release_type.md release="一般的な可用性" %}

AIコピーライティングアシスタントが生成するコピーのスタイルを、ブランドの声に合わせてカスタマイズするための[ブランドガイドラインを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/)作成し、適用できるようになった。シナリオごとに複数のガイドラインを設定し、常に文脈に合ったトーンになるようにする。
 
### 新Braze提携

#### Adikteev - 分析

Brazeと[Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/)インテグレーションにより、Braze CRM キャンペーンs内のAdikteevのチャーン予測テクノロジーを活用してハイリスクユーザー Segmentsをプライオリティでターゲットにすることで、ユーザー リテンションを向上させることができます。
 
#### Celebrus - 分析
 
Brazeおよび[Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus)積分シームレスには、ウェブおよびモバイルアプリ チャネルのBraze SDKと統合され、チャネル活動データを持つアプリ チャネルの母集団を容易にします。これには、特定期間におけるデジタル資産全体のビジター・トラフィックに関する包括的な洞察も含まれる。
 
#### IAM Studio - メッセージテンプレート
 
Brazeと[IAM Studioの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/)統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeのアプリ内メッセージに簡単に挿入することができ、画像置換、テキスト変更、ディープリンク設定、カスタム属性、イベント設定を提供する。IAM Studio を使用すると、メッセージのプロダクション時間を短縮し、コンテンツプランニングにより多くの時間を割くことができます。
 
#### Regal - インスタントチャット

Brazeと[Regalを]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/)統合することで、すべての顧客接点において、より一貫性のあるパーソナライズされた体験を生み出すことができる。

#### Treasure Data - コホートインポート
 
Braze および[Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/) インテグレーションを使用すると、Treasure Data からBraze にユーザー コホートs をインポートできるため、ウェアハウスにのみ存在するデータに基づいてターゲットキャンペーンs を送信できます。
 
#### Zapier - ワークフローの自動化
 
Braze および[Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) パートナーシップは、Braze API およびBraze webhookを活用してサードパーティのアプリライセンスに接続し、さまざまなアクションを自動化します。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Braze Swift SDKバインディングを更新し、9.2.0+ SemVer 名称からのリリースを要求します。
        - これにより、9.2.0 から10.0.0 までの任意のBraze SDKとの互換性が確保されます。
        - 破損の可能性のある変更の詳細については、[7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700)、[8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800)、および[9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900)の変更履歴を参照してください。
    - プッシュ通知のサポートでは、アプリのライケーションの`AppDelegate.application(_:didFinishLaunchingWithOptions:)` メソッドで、スタティックメソッド`BrazeDestination.prepareForDelayedInitialization()` をできるだけ早く呼び出す必要があります。
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - ネイティブiOS ブリッジ[ をBraze Swift SDK 7.7.0 から9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。
- [Expo プラグイン2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - ネイティブiOS ブリッジ[ をBraze Swift SDK 7.7.0 から9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。
    - Braze Android SDK 29.0.1から30.3.0に、ネイティブAndroidブリッジ[を更新しました。
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDKバージョン5.0.0
    - Braze Swift SDK 8.4.0 から9.0.0 へのiOS バインディング[ を更新しました。

## 2024年4月30日リリース

### プロモーション・コード・リストを作成または更新する権限

2024年4月以降、プロモーションコード一覧を作成・更新するには、「キャンペーン、キャンバス、カード、セグメント、メディアライブラリへのアクセス」権限が必要となる。権限名とその説明のリストについては、[制限付きおよびチームロール権限の管理]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)を参照してください。

### データの柔軟性

#### SAMLジャストインタイム・プロビジョニング

{% multi_lang_include release_type.md release="早期アクセス" %}

[ジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) は、SAML SSO と連携して、新しいダッシュボード ユーザーs が最初のサインイン時にBraze アカウントを作成できるようにします。これにより、管理者が新しいダッシュボード ユーザーのアカウントを手動で作成し、権限を選択してワークスペースに割り当て、アカウントの有効化を待機する必要がなくなります。

#### 権限セットとロール

[パーミッション・セットを使って]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles)、特定のサブジェクト領域やアクションに関連するパーミッションを束ねる。これらの権限セットは、異なるワークスペース間で同じアクセスを必要とするダッシュボード ユーザーにアプリ影響を与える可能性があります。

#### クラウドデータ取り込みセグメント

Braze [クラウドデータ取り込みSegment s]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) を使用すると、CDI 接続で利用可能なデータを使用して独自のデータウェアハウスを直接クエリーするSQL を記述し、Braze 内でターゲットにできるユーザーの集合を作成できます。

### クリエイティビティのアンロック

### クエリビルダーのテンプレート

{% multi_lang_include release_type.md release="一般的な可用性" %}

クエリービルダーのテンプレートsを使用して、SnowflakeからBrazeを使用してレポートsを作成できます。[Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) テンプレート s にアクセスするには、レポート作成時に**Query テンプレート** を選択します。すべてのテンプレートは過去60日までのデータを表示するが、エディターで直接その値や他の値を編集することができる。

### セグメント別パフォーマンスデータ

{% multi_lang_include release_type.md release="一般的な可用性" %}

[パフォーマンスデータは、Segment]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)ごとに、クエリービルダーのレポート テンプレートsで、キャンペーンs、バリアントs、キャンバスとキャンバスs、およびキャンバスステップsごとに分割できます。

### 堅牢なチャネル

#### SMSメッセージの自動リンク短縮

{% multi_lang_include release_type.md release="一般的な可用性" %}

[自動リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses)機能を使って、回答中の静的URLを自動的に短縮する。文字数カウンタが更新され、短縮URLの予想される長さが表示されるからだ。

### 新Braze提携

#### Friendbuy-ロイヤルティ

Brazeと[Friendbuyの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/)統合を活用して、EメールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化しよう。Brazeは、Friendbuyで収集されたすべてのオプトイン電話番号の顧客 プロファイルsを生成します。

### NiftyImages - ダイナミックコンテンツ

Braze と[Nifty "画像 s]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/) パートナーシップにより、Nifty s URL にダイナミックな とパーソナライズされた "画像 s をメール キャンペーンs x m アプリで作成できます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift プラグイン 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 本来のiOS ブリッジを[ Braze Swift SDK 7.7.0 から8.4.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) にアップデートします。
        - iOSの最小デプロイメントターゲットは12.0に更新された。
    - 本来のAndroidブリッジを[Braze Android SDK 29.0.1から30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)にアップデートします。
    - サポートされるDartの最小バージョンは2.15.0である。
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - BrazeKitのプライバシーマニフェストからデフォルトのプライバシー追跡ドメインを削除する。
        - Braze [データ"トラッキング機能]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/)を使用している場合は、"トラッキング エンドポイントをアプリレベルのプライバシーマニフェストに手動で追加する必要があります。
        - 統合の手引きについては、更新d [チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking)を参照してください。
    - 非推奨の`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)` を削除する。
        - このメソッドは、元は[release 5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0) で非推奨になりました。
        - 新しいデリゲートメソッドへの切り替えるに失敗しても、コンパイラエラーはトリガーされません。代わりに、定義した`BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` メソッドは単に呼び出されません。
- [Xamarin SDKバージョン4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)

## 2024年4月2日リリース

### WhatsApp

#### 複数のビジネスアカウント

これで、複数のWhatsApp 取引先およびサブスクリプショングループs をワークスペースごとに追加できます。完全なウォークスルーについては、[複数のWhatsApp取引先と電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)を参照してください。

#### 料金を読む

WhatsAppは、インドの消費者sから始まる新たなアプリ侵入をテストし、より価値ある体験を生み出し、企業のマーケティング対話とのエンゲージメントを最大化しています。これには、ある特定の時期に、ある企業から受け取るマーケティングの会話の回数を制限することも含まれます。これは、読まれにくい少数の会話から始まります。詳細については、[メタリソース]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)を参照してください。

### データの柔軟性

#### Amazon S3バケットをBrazeに同期する

{% multi_lang_include release_type.md release="早期アクセス" %}

S3 のクラウドデータインジェストを使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze に直接統合できるようになりました。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。詳細については、[ファイルストレージの統合]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/)を参照してください。

#### Shopify OAuth

{% multi_lang_include release_type.md release="一般的な可用性" %}

Shopifyは、あらゆる規模の小売ビジネスを開始し、成長させ、販売し、管理するための信頼できるツールを提供する、世界的なコマースのリーディングカンパニーである。Shopify for Brazeをセットアップすると、[ワークスペースのOAuthが有効になる]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)。

#### iOSのプッシュ通知にExpoを使う

私たちは[豊富なプッシュ通知sとプッシュストーリーをReact Nativeでエキスポを使ってiOS アプリに統合するための命令]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo)を追加しました。

#### iOS ライブアクティビティのリモート起動

これで、[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/) エンドポイントを使用して、iOS でライブアクティビティをリモートで起動できます。フルウォークスルーについては、[ライブアクティビティを参照してください。Activity]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity) を開始します。

### AIとMLの自動化

#### 項目の推奨事項

{% multi_lang_include release_type.md release="早期アクセス" %}

BrazeAI<sup>TM</sup>を使用すると、最も人気のあるプロダクトを計算したり、特定のカタログのパーソナライズされた AI 推奨を作成したりできます。詳細については、[項目の推奨事項について]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/)を参照してください。

#### アプリ内メッセージの内容をQAする

{% multi_lang_include release_type.md release="一般的な可用性" %}

以前は、BrazeのダッシュボードでBrazeAI<sup>TM</sup>を使ってSMSやプッシュ通知のコンテンツの品質保証を行うことができた。[アプリ内メッセージの内容もQA]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/)できるようになった。

### 新Braze提携

#### Census - コホートインポート

BrazeからCensusにコホートユーザーを[インポートできるようになりました]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/)。これは、SnowflakeやBigQueryのようなクラウドデータウェアハウスをBrazeに接続するデータアクティベーションプラットフォームです。マーケティングチームは、ファーストパーティデータの力を解放してダイナミックな オーディエンス Segmentsを構築し、顧客 属性sを同期してキャンペーンsをパーソナライズし、すべてのデータをBrazeに最新の状態に保つことができます。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [React Native 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - React Nativeの最小バージョンを0.71.0に更新した。
  - iOSの最低バージョンを12.0に更新した。
  - Braze スウィフトSDK 8.1.0 を使用するようにiOS バインディングを更新しました。
  - Braze Android SDK 30.1.1 を使用するようにAndroidバインディングを更新しました。

## 2024年3月5日リリース

### Google EUユーザー同意ポリシー

Googleは[EUユーザー同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を[Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に応じて更新しています。これは2024年3月6日現在有効です。この新たな変更は、広告主に対し、一定の事項を自社及び英国のエンドユーザーに開示するとともに、その同意を得ることを要求するものである。この今後の変更の一部として、[ 両方の同意シグナルをBraze でカスタム属性 s]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users) として収集できます。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### 重複ユーザーをマージする

{% multi_lang_include release_type.md release="早期アクセス" %}

Brazeのダッシュボードで、[重複ユーザーを検索してマージし]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users)、キャンペーンとCanvasの効果を最大化できるようになった。ユーザープロファイルを個別にマージすることも、一括マージを実行することもできます。一括マージでは、一致する識別子s を持つすべてのプロファイルが、直近の更新d ユーザープロファイルにマージされます。

#### アーカイブされたコンテンツを検索する

Braze ダッシュボードで、[アーカイブされた内容を検索結果]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)に含めるには、**アーカイブされた内容を表示**を選択します。

#### AWS S3 およびGoogle Cloud Storage のメッセージアーカイブサポート

[message archiving]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/)を使用して、アーカイブまたは準拠のためにユーザーに送信されたメッセージのコピーを、AWS S3バケット、Azure Blob Storageコンテナ、またはGoogle Cloud Storageバケットに保存できます。

#### SQL テーブルリファレンス

[SQLテーブル参照]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)にアクセスして、クエリビルダでクエリする、またはSQLセグメント拡張を生成するときに使用できるテーブルと列を確認します。

### クリエイティビティのアンロック

#### AIコピーライティングのためのトーンコントロール

AIコピーライティングアシスタントで生成されるコピーのスタイルを決定するために、[メッセージトーンを]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)選択できるようになった。

### 堅牢なチャネル

#### カード作成

カードが[created]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)のときに指定することで、Brazeが新しいコンテンツカード キャンペーンsとキャンバスステップsのオーディエンス適格性とパーソナライゼーションを評価するときを選択できます。 

#### ユーザーパスをプレビューする

{% multi_lang_include release_type.md release="一般的な可用性" %}

ユーザー用に作成したキャンバスジャーニーを体験しましょう。これには、受信するタイミングやメッセージのプレビューも含まれます。これらの[test runs]({{site.baseurl}}/preview_user_paths/)は、メッセージが正しいオーディエンスに送信されてからキャンバスに送信されることを保証します。

#### クイック・プッシュ・キャンペーン

{% multi_lang_include release_type.md release="一般的な可用性" %}

Braze でプッシュキャンペーンを作成する場合、[クイックプッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/) と呼ばれる単一の編集エクスペリエンスで、すべてのプラットフォームs に対して1 つのメッセージを作成する複数のプラットフォームs とデバイスを選択できます。この機能はキャンペーンでのみ利用できる。

#### カスタムリスト-配信停止 ヘッダー

{% multi_lang_include release_type.md release="一般的な可用性" %}

[custom list-配信停止 ヘッダー]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)をメール メッセージングに追加すると、受信者sがオプトアウトできます。これにより、独自に設定したワンクリック配信停止 エンドポイントとオプションの「mailto:」を追加できます。ワンクリック配信停止 HTTP が Yahoo および Gmail の一括送信者に対する要件であるため、Braze では、カスタムの list-unsubscribe ヘッダーをサポートするために URL を入力する必要があります。

#### アプリ内メッセージ s のマルチページ

{% multi_lang_include release_type.md release="早期アクセス" %}

[アプリ内メッセージにページを追加する]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page)では、オンボーディングの流れやウェルカムジャーニーのように、シーケンシャルな流れをユーザーに導くことができます。**Build**タブの**Pages**セクションからページを管理できる。

#### 実験パスのランダム化

実験パスの割付を実験パス ステップに必ず[ランダム化するには、ステップの実験パスs]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)で**ランダム化パスs を選択します。このオプションは、勝者パスまたはパーソナライズされたパスを用いる場合は使用できません。

#### 電子メール・キャプチャ・フォーム

[ メールキャプチャメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) を使用すると、サイトのユーザーにメール住所を送信するように簡単に促すことができます。その後、すべてのメッセージング キャンペーンで使用できるように、ユーザープロファイルで使用できます。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - これは、2024年3月1日の終末期以前のObjective-C SDKの最終版となる([Swift SDK](https://github.com/braze-inc/braze-swift-sdk/)を使用することに賛成)。
    - SDWebImageの最小必要バージョンを5.8.2から5.18.7に更新した。このバージョンには、[プライバシーに影響を与えるSDK](https://developer.apple.com/support/third-party-SDK-requirements/)リストに表示されるSDWebImageのプライバシーマニフェストが含まれている。
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDKバージョン4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Web SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Braze Android SDK 27.0.1 から30.0.0 に、ネイティブAndroid ブリッジ[ を更新しました。
    - Braze Swift SDK 6.6.0 から7.6.0 へのネイティブiOS ブリッジ[ を更新しました。
    - `Banner` コンテンツ・カード・タイプの名前を`ImageOnly` に変更した：
        - `ContentCardTypes.BANNER` to `ContentCardTypes.IMAGE_ONLY`
        - Androidでは、プロジェクト内のXMLファイルにコンテンツカードのバナーという単語が含まれている場合、それを`image_only` に置き換える必要がある。
    - `BrazePlugin.getFeatureFlag(id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)` 更新リクエストが成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがある場合に最初のサブスクリプション時にのみトリガーされます。
    - 非推奨のメソッド`registerAppboyPushMessages` を削除しました。代わりに`setRegisteredPushToken` を使用します。

## 2024年2月6日リリース

### Brazeのプライバシーマニフェスト

Brazeは、宣言されたトラッキングデータを自動的に専用の`-tracking` エンドポイントにリルートする新しい柔軟なAPIとともに、独自のプライバシー・マニフェストをリリースした。詳細については、[Brazeプライバシーマニフェスト]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)を参照してください。

### Google EUユーザー同意ポリシー

Googleは、2024年3月6日に施行される[Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)の変更に応じて、彼らの[EUユーザ同意ポリシー](https://www.google.com/about/company/user-consent-policy/)を更新している。この新たな変更は、広告主に対し、一定の事項を自社及び英国のエンドユーザーに開示するとともに、その同意を得ることを要求するものである。この今後の変更の一部として、[ 両方の同意シグナルをBraze でカスタム属性 s]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users) として収集できます。Brazeは、これらのカスタム属性のデータをGoogleの適切な同意フィールドに同期する。

### データの柔軟性

#### Google Firebase クラウドメッセージング(FCM) API

{% multi_lang_include release_type.md release="一般的な可用性" %}

これで、[ Google の廃止予定のCloud Messaging API から、完全にサポートされているFirebase Cloud Messaging (FCM) API]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/) に移行できます。 

#### Braze クラウドデータインジェスチョン(CDI) エンドポイント

{% multi_lang_include release_type.md release="一般的な可用性" %}

Braze CDI エンドポイント s を使用して:
- [既存の統合のリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)。
- 指定した統合の[過去の同期ステータスのリストを返す]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)。
- 指定した統合の[同期をトリガーする]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)。

#### データブリックのBraze クラウドデータ取り込み(CDI) 対応

カタログ s のBraze CDI サポートが[Databricks sources]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data) で使用できるようになりました。

#### 手動によるSwift SDKの統合

[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration)記事を統合ガイドに追加し、パッケージマネージャーを使用せずにSwift SDKを手動で統合する方法について説明しました。

#### 非推奨

2024年1月11日、BrazeはWindowsアプリとBaiduアプリからのメッセージ配信とデータ収集を停止した。

### クリエイティビティのアンロック

#### SQLセグメント拡張の使用例

[SQL Segment Extensions ユースケース s]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases) ライブラリーには、独自のSQL クエリの作成時にインスピレーションに使用できるSQL Segment Extensions のテスト済みクエリが含まれています。

### 堅牢なチャネル

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

### 新Braze提携

#### Criteo - キャンバスオーディエンス同期

[ Braze Audience Sync to Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/) を使用すると、ブランドは独自のBrazeインテグレーションからユーザーデータをCriteo 顧客一覧に追加して、行動トリガーs、セグメンテーションなどに基づく広告を配信できます。通常、メッセージをトリガーするために使用する基準(プッシュ、メール、SMS、Webhookなど)が、Brazeキャンバスでユーザーデータに基づいて、Criteo 顧客一覧のそのユーザーに広告をトリガーするために使用できるようになりました。

#### Movable Ink - ダイナミックコンテンツ

[Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink) 顧客 Data API インテグレーションでは、Movable Ink 内で顧客内容を生成するために、マーケター s がBraze に保存された顧客イベントデータを有効化できます。

#### Scuba Analytics - 分析

[Scuba Analyticsは]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics)、高速時系列データ用に設計された、フルスタックの機械学習機能付きデータ・コラボレーション・プラットフォームである。Scubaでは、ユーザー（アクターとも呼ばれる）を選択的にエクスポートし、Brazeプラットフォームにロードすることができる。Scuba では、カスタムアクタープロパティを使用して動作トレンドを分析し、さまざまなプラットフォーム間でデータを有効化し、マシンラーニングを使用して予測モデリングを実行します。

### SDKのアップデート
 
以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。
 
- [Expoプラグイン2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - iOSの最低プラットフォーム版を`13.4`に、[Expo SDK 50の要求事項](https://expo.dev/changelog/2024/01-18-sdk-50)に従って押し込みます。
    - このバージョンでは、Expo SDK 50 に完全に対応するために、Braze 対応ネイティブSDKのバージョン[8.3.0+](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0) が必要です。
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - アプリ内メッセージに使用されるOBView は、`WebViewAssetLoader` を使用するために更新d になっています。
        - `WebSettings.allowFileAccess` `InAppMessageHtmlBaseView` および`BrazeWebViewActivity` でfalse に設定されました。
        - 独自の`InAppMessageWebViewClient` または`InAppMessageHtmlBaseView` を使用している場合は、オリジナルのクラスと比較して、実装が正しくアセットをロードしていることを確認してほしい。
        - カスタム・クラスを使用していない場合は、すべてが以前と同じように機能する。
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDKバージョン3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGet パッケージの名前が`AppboyPlatformXamariniOSBinding` から[`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/) に変更されました。
        - 更新 d パッケージを使用するには、`AppboyPlatformXamariniOSBinding;` を使用するすべてのインスタンスをBraze を使用する: に置き換えます。
    - このバージョンでは、。NET 6+ を使用する必要があり、Xamarin フレームワークを使用するプロジェクトのサポートが削除されます。Xamarinのサポート終了前後の[Microsoftのポリシー](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)を参照してください。
    - Androidバインドを[Braze Android SDK 26.3.2 から29.0.1](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) に更新しました。
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - このバージョンは、[ Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) を使用するためにiOS バインドを更新します。ほとんどのiOSパブリックAPIが変更されたため、使用するAPIの変更については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)（Swift）を参照されたい。私たちは、古いパブリックAPIを使い続けるための互換バインディングを提供している。
        - iOSバインディングは現在、複数のモジュールで構成されている：
            - **BrazeKit:**アナリティクスとプッシュ通知のサポートを提供する主なSDKライブラリ（nuget： [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)).
            - BrazeUI:Brazeが提供するアプリ内メッセージとコンテンツカード用のユーザーインターフェイスライブラリ（nuget： [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)).
            - BrazeL 配置:位置情報解析とジオフェンス監視をサポートする位置情報ライブラリ（nuget： [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)).
            - BrazeKitCompat：4.0.0以前のAPIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)).
            - BrazeUICompat：4.0.0以前のUI APIをサポートする互換ライブラリ（nuget： [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)).
        - 新しい統合についてはBrazeiOSMauiSampleAppを、互換モジュールの使用法についてはBrazeiOSMauiCompatSampleAppを参照のこと。
    - iOS バインドを[Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0) に更新しました。
    - iOS バインディングでは、Xコード 15 との互換性のために。NET 7 を使用する必要があります。
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024年1月9日リリース

### Shopifyとの統合に関するドキュメントを更新

以下のようなBrazeとShopifyインテグレーションドキュメントのセクションを更新します。

- [Shopify の使用開始]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [BrazeでShopifyを設定する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [ShopifyのユーザーID管理]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### データの柔軟性

#### カタログの在庫切れ通知

{% multi_lang_include release_type.md release="早期アクセス" %}

[バックインストック通知s]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)とカタログsとキャンバスの組合せを使用して、アイテムがバックインストックのときに顧客sに通知することができます。顧客は、選択したカスタムイベントを実行するたびに、自動的にサブスクライブして、アイテムの補充時に通知を受け取ることができます。

#### カタログセグメント

{% multi_lang_include release_type.md release="早期アクセス" %}

[カタログ Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/)は、SQL Segment拡張のカタログ情報に基づくユーザーsのオーディエンスです。これらのSQLセグメントエクステンションは、セグメントで参照され、キャンペーンやキャンバスでターゲットにすることができる。カタログセグメントは、SQL を使用して、カタログのデータとカスタムイベントまたは購入のデータとを結合します。これを行うには、カタログとカスタムイベントまたは購入に共通の識別子フィールドが必要です。

#### Firebase Cloud Messaging API への移行

{% multi_lang_include release_type.md release="早期アクセス" %}

[ Google の廃止予定のCloud Messaging API から、完全にサポートされているFirebase Cloud Messaging (FCM) API に]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/) を移行する方法について説明します。

### SDKのアップデート

以下のSDKアップデートがリリースされた。破壊的な更新は下記のとおりです。その他すべての更新は、対応する SDK の変更履歴をご確認ください。

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - `BrazeKit`および`BrazeLocation`のプライバシーマニフェストを追加して、Brazeのデータ収集ポリシーを説明します。詳細については、プライバシー・マニフェストに関するAppleの[文書を](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)参照のこと。データ収集プラクティスを管理するためのその他の設定は、今後のリリースで利用できるようになります。
    - 7.1.0で導入されたXCFrameworksのコード署名に関する問題を修正した。
- [Web SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Braze Swift SDK 6.1.0 から7.4.0 にネイティブiOS ブリッジを更新しました。
        - iOS リポジトリリンクは、この[リポジトリ](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic) からビルド済みのダイナミックな XCF ワークを指し示します。
    - Braze Android SDK 27.0.1から29.0.1にネイティブAndroidブリッジを更新しました。
    - `AppboyBinding.GetFeatureFlag(string id)` は、featureフラグが存在しない場合、`null` を返すようになった。
    - `FEATURE_FLAGS_UPDATED` 更新リクエストが成功または失敗で完了したとき、および現在のセッションから以前にキャッシュされたデータがある場合に最初のサブスクリプション時にのみトリガーされます。