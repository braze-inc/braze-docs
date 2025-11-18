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

> キャンペーンの作成プロセス中に、コンテンツカードとそれらが配置されるフィードをカスタマイズすることはできません。カードの作成とカスタマイズを行うには、エンジニアおよび開発者との共同作業が必要です。技術的な詳細については、[開発者向けドキュメント]({{site.baseurl}}/developer_guide/getting_started/customization_overview)を参照してください。

## コンテンツカードのタイプ

{% tabs %}
{% tab Classic %}

クラシックカードは、標準的なメッセージングや通知、あるいはアイコンを使ってメッセージを視覚的に分類するのに適しています。画像は任意だが、1:1の比率でなければならない。

<<<<<<< HEAD
![おすすめのディテールと古典的なカード事例を掲載した古典的なカードのイメージ]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}
=======
\![おすすめのディテールと古典的なカード事例を掲載した古典的なカードのイメージ]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}
>>>>>>> main

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | オプション。<br> 1 対 1 の比率でなければなりません。<br> 画質は60×60pxを推奨する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

キャプション付き画像カードは、ビッグセールやアプリの新機能など、重要なコンテンツをアピールし、注目を集めるのに最適な方法だ。

<<<<<<< HEAD
![推奨内容のキャプション付き画像カードの画像とキャプション付き画像カードの例]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}
=======
\![推奨内容のキャプション付き画像カードの画像とキャプション付き画像カードの例]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}
>>>>>>> main

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的だ。<br> ここで Liquid を使ってメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | 4:3 の比率を推奨。<br> 最小幅 600 px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

よりクリエイティブなコントロールが必要な場合は、画像のみのカードを使用します。任意のツールを使用して画像を作成し、このカードタイプに画像をアップロードします。

<<<<<<< HEAD
![おすすめ内容の"画像専用コンテンツカードと"画像専用サンプルの"画像]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}
=======
\![おすすめ内容の"画像専用コンテンツカードと"画像専用サンプルの"画像]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}
>>>>>>> main

| カード機能 | 詳細 |
| --- | ---|
| リンク付きカード | オプション。<br> 13 px <br> Web ページまたはアプリ内のディープリンクへの、クリック時動作リンク。 |
| 画像 | あらゆるアスペクト比に対応しています。<br> 最小幅 600 px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## グローバル・クリエイティブの詳細 {#general}

コンテンツカードは、最初から素晴らしい機能を備えています。現時点では、カードのスタイリングを Braze アカウントでネイティブに行うことはできませんが、統合時にタイプやコンテンツカードフィードによってコンテンツカードをスタイリングすることができます。詳細については、[コンテンツカードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/)を参照してください。

### 破棄の動作

ユーザーがカードを破棄するには、次のスクリーンショットのようにモバイルでスワイプするか、`close X` 機能を使用します。Web SDK のみ、カーソルを合わせると `x` が表示されます。

<<<<<<< HEAD
![カードのスワイプ/クローズ動作を示すイメージ]({% image_buster /assets/img/dismissal-cc.png %})

もしユーザーがすべてのカードを退会していたり、新しいアップデートをプッシュしていない場合、そのユーザーのフィードは通常このようになる：

![空のコンテンツカードフィードのイメージ]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}
=======
\![カードのスワイプ/クローズ動作を示すイメージ]({% image_buster /assets/img/dismissal-cc.png %})

もしユーザーがすべてのカードを退会していたり、新しいアップデートをプッシュしていない場合、そのユーザーのフィードは通常このようになる：

\![空のコンテンツカードフィードのイメージ]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}
>>>>>>> main

{% alert tip %}
コンテンツカードの関連性を維持できるよう、ユーザーが関連するアクションを起こしたときに破棄されるように設定します。例えば、プロモーション用のコンテンツカードは、ユーザーが購入するとすぐに破棄されるように設定し、すでに購入した商品のオファーが表示され続けないようにします。
{% endalert %}

### コンテンツ・カードでGIFを使う

| Android用コンテンツカード | iOS用コンテンツカード | ウェブ用コンテンツカード |
| --- | --- |---|
| Android SDK は、デフォルトではアニメーション GIF をサポートしていません。GIF サポートの有効化の詳細については、[GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android) を参照してください。 | Swift SDK では、アニメーション GIF がデフォルトではサポートされていません。GIF サポートの有効化の詳細については、[GIF サポートのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。 | GIF のサポートは、Web SDK 統合にデフォルトで含まれています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

