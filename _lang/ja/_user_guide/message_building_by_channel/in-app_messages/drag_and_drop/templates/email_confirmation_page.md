---
nav_title: 確認付きのメールによる登録
article_title: 確認ページ付きメールサインアップ
alias: "/email_confirmation_page/"
page_order: 6
description: "このページでは、アプリ内メッセージのドラッグアンドドロップエディタを使用して、確認ページを持つ電子メールサインアップフォームを作成する方法について説明します。"
---

# 確認ページを使用したメールによる登録

> in-app メッセージのドラッグアンドドロップエディタを使用して、確認ページ付きの電子メールサインアップフォームを作成します。

{% multi_lang_include drag_and_drop/templates.md section='SDKの要件' %}

## 確認ページ付きの電子メールサインアップフォームの作成

### ステップ1:テンプレートを選ぶ

ドラッグアンドドロップのアプリ内メッセージを作成する場合は、テンプレートの**確認ページ**のメールサインアップを選択し、**メッセージの作成**を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![確認ページが付いたメールサインアップフォームのテンプレートを含むアプリ内メッセージエディタ。][img1]

### ステップ2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューを持つアプリ内メッセージエディタ。][img2]

#### メール検証

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4:免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント][3]を使用して、メールサインアップフォームと確認ページのルックアンドフィールをカスタマイズします。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
