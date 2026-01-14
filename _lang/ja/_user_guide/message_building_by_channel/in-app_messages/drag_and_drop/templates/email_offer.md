---
nav_title: オファー付きメール登録
article_title: 特別オファーによる電子メールサインアップ
alias: "/email_offer/"
page_order: 5
description: "このページでは、アプリ内メッセージのドラッグアンドドロップエディタを使用して、サインアップ時に特別割引を提供することでメールリストを構築する方法について説明します。"
---

# 特別オファーを使用したメールによる登録

> アプリ内メッセージのドラッグアンドドロップエディタを使用して、サインアップ時に特別割引を提供することでメールリストを構築します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 特別なオファーを使用した電子メールサインアップフォームの作成

### ステップ1:テンプレートを選ぶ

ドラッグアンドドロップのアプリ内メッセージを作成する場合は、テンプレートに対して**特別なオファー**を使用した電子メールサインアップを選択し、**メッセージのビルド**を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![アプリ内メッセージエディターと特別オファー付きメール登録フォームのテンプレート。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_offer.png %})

### ステップ 2:メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3:メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、**メールサインアップ**ページを選択し、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![アプリ内メッセージエディターには、メールキャプチャエレメントをカスタマイズするためのサイドメニューが用意されている。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_offer.png %})

#### メール検証

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4: 免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、特別オファーの外観と感触をカスタマイズします。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



