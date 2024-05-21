---
nav_title: カラープロファイルとCSS テンプレート
article_title: アプリ内メッセージのカラープロファイルとCSS テンプレート
page_order: 4
page_type: reference
description: "この記事では、アプリ内メッセージのカラープロファイルとCSS テンプレートの概要について説明します。"
channel:
  - in-app messages
---

# カラープロファイルとCSS テンプレート {#reusable-color-profiles}

> ダッシュボードにアプリ内メッセージとブラウザ内メッセージテンプレートを保存して、スタイルを使用して新しいキャンペーンやメッセージをすばやく作成できます。 

**テンプレート**> **アプリ内メッセージテンプレート**に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Templates & Media** の下にこのページがあります。
{% endalert %}

このページから、既存のテンプレートを編集するか、**\+ Create** をクリックし、**Color Profile** または**CSS Template** を選択して、アプリ内メッセージで使用する新しいテンプレートを作成できます。

## カラープロファイル

メッセージテンプレートのカラースキームをカスタマイズするには、16 進カラーコードを入力するか、カラーボックスをクリックしてカラーピッカーでカラーを選択します。

終了したら、**Save Color Profile**をクリックします。

### カラープロファイルの管理

また、[duplicate][6]および[archive][7]テンプレートを使用することもできます![Templates & Media][8] でテンプレートとクリエイティブコンテンツの作成と管理について詳しく説明します。

## CSS テンプレート{#in-app-message-templates}

[web modal in-app message](#web-modal-css)の完全なCSS テンプレートをカスタマイズできます。

CSS テンプレートに名前を付けてタグを付け、デフォルトテンプレートにするかどうかを選択します。提供されたスペースに独自のCSSを書き込むことができます。このスペースには、メッセージプレビューに表示されるCSS があらかじめ入力されています。必要に応じて、少し調整してください。

\`\`\`css
.ab-message-header, .ab-message-text {
color: #333333;
text-align: center;
}

.ab-message-header {
font-size: 20px;
font-weight: bold;
}

.abメッセージ・テキスト {
font-size: 14px;
font-weight: normal;
}

.ab-close-button svg {
fill: #9b9b9b;
}

.ab-messageボタン {
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

.abアイコン {
background-color: #0073d5;
color: white;
}

.abページ遮断薬 {
background-color: rgba(51, 51, 51, .75);
}
  \`\`\`

ご覧のように、背景色からフォントサイズ、重さ、そしてそれ以上のものまで、すべてを編集することができます。

### CSSテンプレートの管理

また、[duplicate][6]および[archive][7]テンプレートを使用することもできます![Templates & Media][8] でテンプレートとクリエイティブコンテンツの作成と管理について詳しく説明します。

## CSS 付きモダル(Web のみ) {#web-modal-css}

CSS メッセージでWeb 専用のWeb モダルを使用することを選択した場合は、独自のテンプレートを適用するか、提供されているスペースに独自のCSS を記述できます。このスペースには、メッセージプレビューに表示されるCSS があらかじめ入力されていますが、必要に応じて少し調整してください。

独自のテンプレートを適用する場合は、**Apply Template**をクリックし、アプリ内メッセージテンプレートギャラリーから選択します。オプションがない場合は、CSS Template Builder を使用して[CSS テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) をアップロードできます。


[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/
[7]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/
[8]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
