---
nav_title: IAMスタジオ
article_title: IAMスタジオ
description: "このリファレンス記事では、Braze と IAM Studio のパートナーシップについて説明します。IAM Studio は、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Braze を通じてそのエクスペリエンスを提供できるメッセージパーソナライゼーションプラットフォームです。"
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAMスタジオ

> [IAM Studio](https://www.inappmessage.com) は、カスタマイズされたリッチなアプリ内エクスペリエンスを作成し、Braze を通じてそのエクスペリエンスを提供できる、ノーコードのメッセージパーソナライゼーションプラットフォームです。

_この統合は IAM Studio によって管理されます。\*s_

## 統合について

Braze と IAM Studio の統合により、カスタマイズ可能なアプリ内メッセージテンプレートを Braze アプリ内メッセージに簡単に挿入できます。これにより、画像の置き換え、テキストの変更、ディープリンク設定、カスタム属性、イベント設定が提供されます。IAM Studio を使用すると、メッセージの作成時間を短縮し、コンテンツ計画により多くの時間を費やすことができます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| IAM Studioアカウント | このパートナーシップを活用するには、[IAM Studio アカウント](https://www.inappmessage.com/register)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユースケース

- 物品の購入促進
- ユーザー情報の収集
- 会員登録の拡大
- クーポン発行情報

## 統合

### ステップ1:テンプレートの選択

アプリ内メッセージ テンプレートギャラリーから使用するアプリ内メッセージ テンプレートを選択します

![IAM Studio テンプレートギャラリーに「carousel slide modal」、「carousel slide modal」、「simple icon modal」、「modal full image」など、さまざまなテンプレートが表示されている。]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### ステップ2: テンプレートのカスタマイズ

まず、コンテンツの画像、テキスト、ボタンをカスタマイズします。"画像とボタンは必ず**Deeplink**を接続してください。

{% tabs ローカル %}
{% tab 画像 %}
![画像をカスタマイズするオプションが表示されている IAM Studio のUI。オプションには、画像、画像半径、淡色表示の画像がある。]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab テキスト %}
![メッセージのタイトルと字幕をカスタマイズするオプションを示すIAM Studio UI。これらのオプションには、テキスト、書式設定、およびフォントが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab ボタン %}
![メインの左および右ボタンをカスタマイズするオプションが表示されている IAM Studio の UI。これらのオプションには、色、ディープリンク、テキスト、およびフォーマットが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

次にカスタムフォントを追加し、Liquid タグを使用して、パーソナライズされたアプリ内メッセージを作成します。ログとトラッキングを有効にするには、[**Log data and track user behavior**] を選択します。

{% tabs ローカル %}
{% tab フォント %}
![Liquid を追加するオプションが表示されている IAM Studio のUI。これらのオプションには、パーソナライズされた文章の作成も含まれます。]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![イベント/属性のロギングをカスタマイズするオプションが表示されている IAM Studio のUI。これらのオプションには、ユーザー動作ログが含まれます。]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab ロギングとトラッキング %}
![フォントをカスタマイズするオプションを示すIAM Studio UI。これらのオプションには、ユーザーがフォントスタイルをカスタマイズできることが含まれます。]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png %})
{% endtab %}
{% endtabs %}

### ステップ3:テンプレートのエクスポート

すべての編集が完了したら、**エクスポート**をクリックしてテンプレートをエクスポートします。エクスポート後、アプリ内メッセージ HTML コードが生成されます。**コピーコード**をクリックして、このコードをコピーします。 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### ステップ 4: Brazeでのコードの使用 

Braze に移動し、アプリ内メッセージで** HTML Input** ボックスにカスタムコードを貼り付けます。メッセージが正しく表示されていることを確認するために、メッセージをテストしてください。

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


