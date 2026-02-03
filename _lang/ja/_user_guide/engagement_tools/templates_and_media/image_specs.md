---
nav_title: 画像の仕様
article_title: 画像の仕様
page_order: 4.1

page_type: reference
description: "この参考記事では、各チャネルタイプの推奨画像サイズと仕様について説明しています。"
tool:
  - Templates
  - Media

---

# 画像の仕様

> 一般的に、小さくて高品質な画像ほど読み込みが速くなるため、希望する出力を達成するために可能な限り小さなアセットを使用することをお勧めします。特定のチャネルで画像を最大限に使用するには、この記事の詳細を参照すること。

常にさまざまなデバイスで[メッセージをプレビューしてテストし]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)、画像とメッセージの最も重要な領域が期待どおりに表示されることを確認する必要があります。

{% alert tip %} 自信を持ってアセットを創造しましょう！アプリ内メッセージ "画像 テンプレート sとセーフゾーンオーバーレイは、すべてのサイズの機器でうまく動作するように設計されています。[Down 読み込む デザインテンプレート s ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %})。 {% endalert %}

{% multi_lang_include image_specs.md variable_name='payload size' %}

## アプリ内メッセージ

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

### Font Awesome

Braze では、モーダルアプリ内メッセージアイコンに [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) を使用できます。

## プッシュ通知

{% multi_lang_include image_specs.md variable_name='push notifications' %}

## メール

{% multi_lang_include image_specs.md variable_name='email' %}

## 画像行動

{% multi_lang_include image_specs.md variable_name='image behavior' %}
