---
nav_title: IAM スタジオ
article_title:IAM スタジオ
description:「この参考記事では、BrazeとIAM Studioのパートナーシップについて概説しています。IAM Studioは、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Brazeを通じて配信できるメッセージパーソナライゼーションプラットフォームです。「
alias: /partners/iam_studio/
page_type: partner
search_tag:Partner

---

# IAM スタジオ

> [IAM Studio](https://www.inappmessage.com) はコード不要のメッセージパーソナライゼーションプラットフォームで、パーソナライズされたリッチなアプリ内体験を作成し、Braze を通じて配信できます。

BrazeとIAM Studioの統合により、カスタマイズ可能なアプリ内メッセージテンプレートをBrazeアプリ内メッセージに簡単に挿入して、画像, 写真置換、テキストの変更、ディープリンク設定、カスタム属性、イベント設定を行うことができます。IAM Studio を使用すると、メッセージ作成時間を短縮し、より多くの時間をコンテンツ計画に充てることができます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| IAM スタジオアカウント | このパートナーシップを利用するには [IAM Studio アカウントが必要です](https://www.inappmessage.com/register)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ユースケース

- 商品の購入を促す
- ユーザー情報収集
- 会員登録数の増加
- クーポン発行情報

## 統合

### ステップ1:テンプレートを選択する

アプリ内メッセージテンプレートギャラリーから、使用したいアプリ内メッセージテンプレートを選択します

![IAM Studio テンプレートギャラリーには、「カルーセルスライドモーダル」、「シンプルアイコンモーダル」、「モーダルフル画像, 写真」などのさまざまなテンプレートが表示されます。][1]

### ステップ2:テンプレートをカスタマイズ

まず、コンテンツの画像, 写真、テキスト、ボタンをカスタマイズします。画像, 写真**ボタンには必ずディープリンクを接続してください**。

{% tabs local %}
{% tab Image %}
![The IAM Studio UI showing the options to customize the image. These options include the image, image radius, and image dimmed.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Text %}
![The IAM Studio UI showing the options to customize the title and subtitle of your message. These options include text, formatting, and font.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Button %}
![The IAM Studio UI showing the options to customize the main, left and right button. These options include color, deep link, text, and formatting.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

次に、カスタムフォントを追加し、Liquidタグを使用して、パーソナライズされたアプリ内メッセージを作成します。ロギングとトラッキング, 追跡を有効にするには、「**データをログに記録してユーザー行動を追跡する**」を選択します。

{% tabs local %}
{% tab Fonts %}
![The IAM Studio UI showing the options to add Liquid. These options include making personalized setence.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![The IAM Studio UI showing the options to customize event/attribute logging. These options include that user behavior log.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Logging and Tracking %}
![The IAM Studio UI showing the options to customize font. These options include that user can customize font style.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### ステップ3:テンプレートをエクスポートする

すべての編集が完了したら、\[エクスポート] **をクリックしてテンプレートをエクスポートします**。エクスポート後、アプリ内メッセージの HTML コードが生成されます。\[コードコピー] ボタンをクリックして、**このコードコピーします**。 

![][2]{: style="max-width:45%;"}

### ステップ 4:Braze でコードを使う 

Braze に移動し、**アプリ内メッセージの HTML 入力ボックスにカスタムコード**貼り付けます。メッセージをテストして、正しく表示されていることを確認してください。

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}
