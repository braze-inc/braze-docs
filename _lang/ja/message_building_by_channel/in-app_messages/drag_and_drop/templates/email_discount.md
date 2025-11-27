---
nav_title: 割引を使用したメールによる登録
article_title: 割引付きメール登録
alias: "/email_discount/"
page_order: 3
description: "このリファレンスページでは、アプリ内メッセージのドラッグアンドドロップエディタを使用して、新しいサブスクライバの割引を提供する電子メールサインアップフォームを構築する方法について説明します。"
---

# 割引を使用したメールによる登録

> アプリ内メッセージのドラッグアンドドロップエディタを使用して、新しいサブスクライバの割引を提供するメールサインアップフォームを作成します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 割引で電子メールのサインアップフォームを作成する

### ステップ1:テンプレートを選ぶ

ドラッグアンドドロップのアプリ内メッセージを作成する場合は、テンプレートの** welcome discount** を使用したメールサインアップを選択し、**Build message** を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![割引を含むメールサインアップフォームのテンプレートが表示されているアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})()

### ステップ 2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3: メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューを持つアプリ内メッセージエディタ。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})()

#### メール検証

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4: 免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、サインアップフォームと割引の外観と感触をカスタマイズします。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



