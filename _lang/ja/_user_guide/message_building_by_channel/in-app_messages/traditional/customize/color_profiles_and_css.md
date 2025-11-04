---
nav_title: カラープロファイルsとCSS テンプレートs
article_title: アプリ内メッセージのカラープロファイルとCSSテンプレート
page_order: 4
page_type: reference
description: "この記事では、アプリ内メッセージのカラープロファイルとCSSテンプレートの概要を説明します。"
channel:
  - in-app messages
---

# カラープロファイルとCSSテンプレート {#reusable-color-profiles}

> ダッシュボードにアプリ内メッセージおよびブラウザ内メッセージのテンプレートを保存して、あなたのスタイルを使用して新しいキャンペーンやメッセージを迅速に作成できます。 

**テンプレート** > **アプリ内メッセージテンプレート**。

このページから、既存のテンプレートを編集するか、**\+ 作成**をクリックして**カラープロファイル**または**CSSテンプレート**を選択し、アプリ内メッセージで使用する新しいテンプレートを作成できます。

## カラープロファイル

メッセージテンプレートのカラースキームは、HEXカラコードを入力するか、色付きのボックスをクリックしてカラーピッカーで色を選択することでカスタマイズできます。

終了したら**色のプロファイルを保存**をクリックします。

### カラープロファイルの管理

テンプレートを[複製]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)および[アーカイブ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)することもできます！[ テンプレート s & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) で、テンプレート s とクリエイティブコンテンツの作成と管理について詳しく説明します。

## CSS テンプレート{#in-app-message-templates}

[webモーダルアプリ内メッセージ](#web-modal-css)用の完全なCSSテンプレートをカスタマイズできます。

CSSテンプレートに名前を付けてタグを付け、デフォルトのテンプレートにするかどうかを選択します。提供されたスペースに自分のCSSを書くことができます。このスペースは、メッセージプレビューに表示されているCSSで既に埋められており、ニーズに合わせて少し調整しても構いません。

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

コードで示されたように、背景色からフォントのサイズや太さなど、さまざまなものを編集できます。

### CSSテンプレートの管理

テンプレートを[複製]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)および[アーカイブ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)することもできます！[ テンプレート s & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/) で、テンプレート s とクリエイティブコンテンツの作成と管理について詳しく説明します。

## モーダル with CSS (Web only) {#web-modal-css}

Web専用のWebモーダルをCSSメッセージで使用する場合は、独自のテンプレートを適用するか、指定されたスペースに独自のCSSを書くことができます。このスペースは、メッセージプレビューに表示されているCSSですでに事前入力されていますが、ニーズに合わせて少し調整しても構いません。

ご自身のテンプレートを適用する場合は、**テンプレートを適用**をクリックし、アプリ内メッセージテンプレートギャラリーから選択してください。オプションがない場合は、CSSテンプレートビルダーを使用して[CSSテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates)をアップロードできます。


