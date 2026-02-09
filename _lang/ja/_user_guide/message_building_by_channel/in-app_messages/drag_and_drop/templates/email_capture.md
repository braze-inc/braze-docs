---
nav_title: メールサインアップフォーム
article_title: メールサインアップフォーム
alias: "/email_capture/"
page_order: 2
description: "このページでは、アプリ内メッセージのドラッグ＆ドロップエディターを使ってメール登録フォームを作成する方法を説明する。"
---

# メールサインアップフォーム

> ドラッグアンドドロップのメールサインアップアプリ内メッセージテンプレートを使用して、ユーザーのメールアドレスを収集し、サブスクリプショングループを成長させましょう。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## メールサインアップフォームの作成

### ステップ1:テンプレートを選ぶ

ドラッグ＆ドロップのアプリ内メッセージを作成するときには、テンプレートに [**メールで登録**] を選択し、[**メッセージを作成**] を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![メールキャプチャフォームのテンプレートを含むアプリ内メッセージエディタ。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### ステップ 2:メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニュー付きのアプリ内メッセージエディタ。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### メール検証

もしユーザーが受け付けられない特殊文字を含むメールアドレスを入力した場合、一般的なエラーインジケーターが表示され、フォームを送信することができない。このエラーメッセージはカスタマイズできない。エラーの挙動は、**プレビュー&テスト**タブとテストデバイスで確認できます。Braze が [メール アドレスの検証]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/) でメール アドレスをどのようにフォーマットするかの詳細をご覧ください。

### ステップ 4:免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、サインアップフォームの外観と感触をカスタマイズします。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

