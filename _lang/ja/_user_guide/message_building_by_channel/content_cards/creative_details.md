---
nav_title: クリエイティブの詳細
article_title: コンテンツ・カードのクリエイティブな詳細
page_order: 1
description: "この記事では、3つの標準的なコンテンツ・カード・タイプにおける画像サイズの推奨や解雇の動作など、クリエイティブな詳細について説明する。"
channel:
  - content cards
tool: Media

---

# コンテンツ・カードのクリエイティブ詳細

> キャンペーンの作成プロセス中に、コンテンツカードとそれらが配置されるフィードをカスタマイズすることはできません。カードの作成とカスタマイズを行うには、エンジニアおよび開発者との共同作業が必要です。技術的な詳細については、[開発者向けドキュメント][7] を参照してください。

## コンテンツカードのタイプ

{% tabs %}
{% tab クラシック %}

クラシックカードは、標準的なメッセージングや通知、あるいはアイコンを使ってメッセージを視覚的に分類するのに適しています。画像は任意だが、1:1の比率でなければならない。

![推奨されるディテールとクラシックカードのサンプルを持つ、クラシックなカードの画像]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | オプション。<br> 1 対 1 の比率でなければなりません。<br> 画質は60×60pxを推奨する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab キャプション付き画像 %}

キャプション付き画像カードは、ビッグセールやアプリの新機能など、重要なコンテンツをアピールし、注目を集めるのに最適な方法だ。

![推奨されるディテールとキャプション付き画像カードのサンプルを持つ、キャプション付き画像カードの画像]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | 4:3 の比率を推奨。<br> 最小幅 600 px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab バナー %}

趣向を凝らした演出にはバナーカードが向いています。これは必要に応じて完全にカスタマイズすることができます。別の場所でコンテンツを作成し、それをアップロードするだけで、あなただけの美しいカードが完成する。

![推奨される詳細とバナーのサンプルを持つ、バナーの画像]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| リンク付きカード | オプション。<br> 13 px <br> Web ページまたはアプリ内のディープリンクへの、クリック時動作リンク。 |
| 画像 | あらゆるアスペクト比に対応しています。<br> 最小幅 600 px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## グローバル・クリエイティブの詳細 {#general}

コンテンツカードは、最初から素晴らしい機能を備えています。現時点では、カードのスタイリングを Braze アカウントでネイティブに行うことはできませんが、統合時にタイプやコンテンツカードフィードによってコンテンツカードをスタイリングすることができます。詳しくは、[コンテンツカードのカスタマイズ][4]] を参照してください。

### 破棄の動作

ユーザーがカードを破棄するには、次のスクリーンショットのようにモバイルでスワイプするか、`close X` 機能を使用します。Web SDK のみ、カーソルを合わせると `x` が表示されます。

![カードのスワイプまたはクローズ解除の動作を示す画像][5]

もしユーザーがすべてのカードを退会していたり、新しいアップデートをプッシュしていない場合、そのユーザーのフィードは通常このようになる：

![空のコンテンツ・カード・フィードのイメージ][6]{: style="max-width:45%"}

{% alert tip %}
コンテンツカードの関連性を維持できるよう、ユーザーが関連するアクションを起こしたときに破棄されるように設定します。例えば、プロモーション用のコンテンツカードは、ユーザーが購入するとすぐに破棄されるように設定し、すでに購入した商品のオファーが表示され続けないようにします。
{% endalert %}

### コンテンツ・カードでGIFを使う

| Android用コンテンツカード | iOS用コンテンツカード | ウェブ用コンテンツカード |
| --- | --- |---|
| Android SDK は、デフォルトではアニメーション GIF をサポートしていません。GIF サポートの有効化の詳細については、[GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/) を参照してください。 | Swift SDK では、アニメーション GIF がデフォルトではサポートされていません。GIF サポートの有効化の詳細については、[GIF サポートのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。 | GIF のサポートは、Web SDK 統合にデフォルトで含まれています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

[1]: {% image_buster /assets/img/content_card_classic.png %}
[2]: {% image_buster /assets/img/content_card_captioned.png %}
[3]: {% image_buster /assets/img/content_card_banner.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
[7]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview