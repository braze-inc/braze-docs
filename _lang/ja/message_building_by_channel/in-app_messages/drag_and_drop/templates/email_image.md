---
nav_title: イメージを使用した電子メールのサインアップ
article_title: バックグラウンドイメージを使用した電子メールサインアップ
alias: "/email_image/"
page_order: 4
description: "このページでは、アプリ内メッセージドラッグアンドドロップエディタを使用して、1つのシンプルなメッセージでブランドスタイルを表示し、メールリストを構築する方法について説明します。"
---

# 背景画像を使用したメールによる登録

> アプリ内メッセージドラッグアンドドロップエディタを使用して、1つのシンプルなメッセージでブランドスタイルを表示し、メールリストを構築します。

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## バックグラウンドイメージを使用した電子メールサインアップフォームの作成

### ステップ1:テンプレートを選ぶ

ドラッグ＆ドロップのアプリ内メッセージを作成するときには、テンプレートとして [**背景画像付きのメールサインアップ**] を選択し、その後 [**メッセージを作成**] を選択します。このテンプレートは、モバイルアプリとWebブラウザの両方でサポートされています。

![メールサインアップフォームのテンプレートがあり、背景イメージがあるアプリ内メッセージエディター。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})()

### ステップ 2: メッセージスタイルを設定する

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### ステップ 3: メール登録コンポーネントのカスタマイズ

メールサインアップフォームの作成を開始するには、エディタでメールキャプチャ要素を選択します。デフォルトでは、収集されたメールアドレスはグローバルサブスクリプショングループ**Subscribed**を持ちます。特定のサブスクリプショングループにユーザーをオプトインするには、[メールサブスクリプションの状態を更新する]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)を参照してください。

メールキャプチャ要素のプレースホルダーテキストとラベルテキストをカスタマイズできます。

![メールキャプチャ要素をカスタマイズするためのサイドメニューを持つアプリ内メッセージエディタ。]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})()

#### メール検証

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### ステップ 4: 免責事項の言語を追加（オプション）

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### ステップ 5: メッセージにスタイルを設定する

ドラッグアンドドロップ[アプリ内メッセージコンポーネント]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)を使用して、サインアップフォームの外観と感触をカスタマイズします。**メッセージコンテナー**メニューでデフォルトの背景画像 URL を置き換えて独自の背景画像を追加するか、URL を削除して[メディアライブラリ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)から画像を選択します。

## 結果の分析

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## ベストプラクティス

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}




