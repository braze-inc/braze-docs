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

> コンテンツカードとそのフィードのカスタマイズは、キャンペーン作成中に行うことはできない。技術的な詳細については、\[開発者向けドキュメント]][7] を参照のこと。

## コンテンツ・カードの種類

{% tabs %}
{% tab クラシック %}

クラシックカードは、標準的なメッセージや通知、あるいはアイコンでメッセージを視覚的に分類するのに最適だ。画像は任意だが、1:1の比率でなければならない。  

![おすすめ詳細とクラシックカードのイメージ例]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここでリキッドを使ってメッセージをパーソナライズすることもできる。 |
| メッセージ | 13px; レギュラーウェイト <br> 2行から4行のテキストが理想的だ。<br> ここでリキッドを使ってメッセージをパーソナライズすることもできる。 |
| リンクテキスト | オプションだ。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| イメージ | オプションだ。<br> 1対1の比率でなければならない。<br> 画質は60×60pxを推奨する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab キャプション付き画像 %}

キャプション付き画像カードは、ビッグセールやアプリの新機能など、重要なコンテンツをアピールし、注目を集めるのに最適な方法だ。

![推奨詳細とキャプション付きイメージカードの例]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> テキストは1行が理想的だ。<br> ここでリキッドを使ってメッセージをパーソナライズすることもできる。 |
| メッセージ | 13px; レギュラーウェイト <br> 2行から4行のテキストが理想的だ。<br> ここでリキッドを使ってメッセージをパーソナライズすることもできる。 |
| リンクテキスト | オプションだ。<br> 13 px <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| イメージ | 4：3の比率を推奨する。<br> 最小幅600px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab バナー %}

派手さを求めるなら、バナーカードが向いている。これはあなたが望むものに完全にカスタマイズされる。別の場所でコンテンツを作成し、それをアップロードするだけで、あなただけの美しいカードが完成する。

![推奨詳細とバナー例の画像]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| カード機能 | 詳細 |
| --- | ---|
| リンクカード | オプションだ。<br> 13 px <br> オンクリックビヘイビアは、ウェブページまたはアプリ内へのディープリンクにリンクする。 |
| イメージ | あらゆるアスペクト比に対応する。<br> 最小幅600px。 <br> 高解像度のPNG、JPEG、GIFをサポートする。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## グローバル・クリエイティブの詳細 {#general}

コンテンツ・カードは最初から優れた機能を備えている。現時点では、カードのスタイリングはBrazeアカウントでネイティブに行うことはできないが、統合時にタイプやコンテンツカードフィードによってコンテンツカードをスタイリングすることができる。詳しくは\[コンテンツカードのカスタマイズ][4] ]を参照のこと。

### 解雇行動

ユーザーがカードを退会するには、モバイルでスワイプするか、次のスクリーンショットのように`close X` 。Web SDKのみ、カーソルを合わせると`x` が表示される。

![カードのスワイプまたはクローズ解除の動作を示す画像][5]

もしユーザーがすべてのカードを退会していたり、新しいアップデートをプッシュしていない場合、そのユーザーのフィードは通常このようになる：

![空のコンテンツ・カード・フィードのイメージ][6]{: style="max-width:45%"}

{% alert tip %}
コンテンツカードは、ユーザーが関連するアクションを起こしたときに解除されるように設定することで、関連性を保つことができる。例えば、プロモーション用のコンテンツカードは、ユーザーが購入するとすぐに破棄されるように設定し、すでに購入した商品のオファーが表示され続けないようにする。
{% endalert %}

### コンテンツ・カードでGIFを使う

| Android用コンテンツカード | iOS用コンテンツカード | ウェブ用コンテンツカード |
| --- | --- |---|
| Android SDKは、デフォルトではアニメーションGIFをサポートしていない。GIFサポートの有効化の詳細については、[GIFを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/)参照のこと。 | Swift SDK では、アニメーション GIF がデフォルトではサポートされていません。GIFサポートの有効化の詳細については、[GIFサポートチュートリアルを](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)参照のこと。 | GIFのサポートは、Web SDK統合にデフォルトで含まれている。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

<br><br>

[1]: {% image_buster /assets/img/content_card_classic.png %}
[2]: {% image_buster /assets/img/content_card_captioned.png %}
[3]: {% image_buster /assets/img/content_card_banner.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
[7]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview
