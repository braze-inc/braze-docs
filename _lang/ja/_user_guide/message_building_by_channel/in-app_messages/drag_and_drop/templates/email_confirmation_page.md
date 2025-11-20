---
nav_title: 確認のメール登録
article_title: 確認ページ付きメールサインアップ
alias: "/email_confirmation_page/"
page_order: 6
description: "このページでは、アプリ内メッセージのドラッグアンドドロップエディタを使用して、確認ページを持つ電子メールサインアップフォームを作成する方法について説明します。"
---

# 確認ページを使用したメールによる登録

> in-app メッセージのドラッグアンドドロップエディタを使用して、確認ページ付きの電子メールサインアップフォームを作成します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 確認ページ付きの電子メールサインアップフォームの作成

### ステップ1:テンプレートを選ぶ

ドラッグ＆ドロップのアプリ内メッセージを作成するときには、テンプレートとして [**確認ページ付きメールサインアップ**] を選択し、その後 [**メッセージを作成**] を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![アプリ内メッセージエディターと確認ページ付きメール登録フォームのテンプレート。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### ステップ 2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3: メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![アプリ内メッセージエディターは、メールキャプチャエレメントをカスタマイズするためのサイドメニューを備えている。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### メール検証

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4: 免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、メールサインアップフォームと確認ページのルックアンドフィールをカスタマイズします。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


