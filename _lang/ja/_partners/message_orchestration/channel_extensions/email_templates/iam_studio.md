---
nav_title: IAMスタジオ
article_title: IAMスタジオ
description: "このリファレンス記事では、Braze とIAM Studio の連携について説明します。これは、メッセージパーソナライゼーション プラットフォームで、Braze を使用してパーソナライズされたを作成し、豊富なアプリ体験を提供することができます。"
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAMスタジオ

> [IAM Studio](https://www.inappmessage.com) はno-コード メッセージパーソナライゼーション プラットフォームで、豊富なアプリ体験を作成し、Brazeを通じて配信できます。

Braze とIAM Studio の統合により、カスタマイズ可能なアプリ内メッセージ テンプレートs をBraze アプリ内メッセージに簡単に挿入でき、"画像置換、テキストモディフィケーション、ディープリンク設定s、カスタム属性s、およびイベント設定s を提供できます。IAM Studio を使用すると、メッセージのプロダクション時間を短縮し、コンテンツプランニングにより多くの時間を割くことができます。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| IAM Studioアカウント | この提携の事前タグを行うには、[IAM Studioアカウント](https://www.inappmessage.com/register)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ユースケース

- 物品の購入促進
- ユーザー情報の収集
- 会員登録の拡大
- クーポン発行情報

## 統合

### ステップ1:テンプレートの選択

アプリ内メッセージ テンプレートギャラリーから使用するアプリ内メッセージ テンプレートを選択します

![IAM Studio テンプレートギャラリーには、"carousel slide モーダル", "simple icon モーダル", "モーダル full "画像"など、さまざまなテンプレートが表示されます。][1]

### ステップ2:テンプレートのカスタマイズ

まず、内容の"画像、文字、ボタンをカスタマイズします。"画像とボタンは必ず**Deeplink**を接続してください。

{% tabs ローカル %}
{% tab イメージ %}
!["画像をカスタマイズするためのオプションを示すIAM Studio UI。これらの選択肢には、"画像、半径、および"画像が含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab テキスト %}
![メッセージのタイトルと字幕をカスタマイズするオプションを示すIAM Studio UI。これらのオプションには、テキスト、書式設定、およびフォントが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab ボタン %}
![IAM Studio のUI には、メイン、左右のボタンをカスタマイズするオプションが表示されます。これらのオプションには、色、ディープリンク、テキスト、およびフォーマットが含まれます。]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

次に、カスタムフォントを追加し、リキッドタグs を使用してパーソナライズされた アプリ内メッセージを作成します。ログと"トラッキングを有効にするには、**ログデータを選択し、ユーザーの動作を追跡します**。

{% tabs ローカル %}
{% tab フォント %}
![IAM Studio のUI に、Liquid を追加するオプションが表示されます。これらの選択肢には、パーソナライズされた設定が含まれます。]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab 液体 %}
![IAM Studio のUI には、イベント/属性のログ記録をカスタマイズするためのオプションが表示されます。これらのオプションには、ユーザー動作ログが含まれます。]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab ロギングとトラッキング %}
![フォントをカスタマイズするオプションを示すIAM Studio UI。これらのオプションには、ユーザーがフォントスタイルをカスタマイズできることが含まれます。]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### ステップ3:テンプレートのエクスポート

すべての編集が完了したら、**エクスポート**をクリックしてテンプレートをエクスポートします。エクスポート後、アプリ内メッセージ HTML コードが生成されます。**コピーコード**をクリックして、このコードをコピーします。 

![][2]{: style="max-width:45%;"}

### ステップ4:Brazeでのコードの使用 

Braze に移動し、アプリ内メッセージで** HTML Input** ボックスにカスタムコードを貼り付けます。メッセージが正しく表示されていることを確認するために、メッセージをテストしてください。

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}
