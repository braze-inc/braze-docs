---
nav_title: 翻訳
article_title: 翻訳エンドポイント
search_tag: エンドポイント
page_order: 9
layout: dev_guide

description: "このランディングページには、Braze変換エンドポイントs が一覧表示されます。"
page_type: landing

guide_top_header: "翻訳エンドポイント"
guide_top_text: "Brazeの翻訳エンドポイントを使って、キャンペーン、キャンバス、コンテンツブロック内の翻訳を管理し更新する。"

guide_featured_title: "キャンペーンエンドポイント"
guide_featured_list:
  - name: "取得:キャンペーンの翻訳を表示"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT:キャンペーン内の翻訳を更新"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:キャンペーンのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "取得:キャンバスの翻訳を表示"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT:キャンバス内の翻訳を更新"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:キャンバスのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "取得:メールテンプレートのデフォルトソース翻訳を表示する"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "取得:特定の翻訳とロケールを表示"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:すべての翻訳とロケールを表示"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT:メールテンプレートの翻訳を更新"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title3: "Content Block endpoints"
guide_menu_list3:
  - name: "取得:コンテンツブロックの全翻訳を表示する"
    link: /docs/api/endpoints/translations/content_blocks/get_translation_content_block/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT:コンテンツブロック内の翻訳を更新する"
    link: /docs/api/endpoints/translations/content_blocks/put_update_translation_content_block/
    image: /assets/img/braze_icons/target-04.svg

---

{% multi_lang_include early_access_beta_alert.md feature='Access to the Braze translation endpoints' %}

## 翻訳エンドポイントの仕組み

翻訳エンドポイントは[多言語構成]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/)で動作します。ここで、メッセージは、メッセージを受け取るユーザーに応じてレンダリング可能な異なるバージョンを持つことができます。

### 前提条件

これらのエンドポイントを使用する前に、[ロケールを追加]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale)する必要があります。

### 翻訳のテスト方法

翻訳サポートを検証するには、APIとBrazeダッシュボードを併用し、キャンペーン、キャンバス（個々のステップを含む）、コンテンツブロック、メールテンプレート全体で以下の2つの方法がある：

- 構成中 (開始前)
- 開始後 (開始後の下書きを使用)

翻訳の更新をテストする前に、以下を実行する必要があります。

1. [ロケールを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale)。
2. メッセージを作成し、必要に応じて翻訳タグを使用します。
3. メッセージを保存します。
4. 含めるロケールを選択します。
