---
nav_title: クリエイティブの詳細
article_title: コンテンツカードのクリエイティブ詳細
page_order: 1
description: "この記事では、3 つの標準コンテンツ カード タイプにおける画像サイズの推奨事項や閉じる動作などのクリエイティブの詳細について説明します。"
channel:
  - content cards
tool: Media

---

# コンテンツカードのクリエイティブ詳細

> コンテンツ カードとそれが配置されているフィードは、キャンペーン作成プロセス中にはカスタマイズできません。エンジニアや開発者と協力してカードを作成し、カスタマイズする必要があります。技術的な詳細については、[開発者向けドキュメント][7]をご覧ください。

## コンテンツカードの種類

{% tabs %}
{% tab Classic %}

クラシック カードは、標準的なメッセージや通知、さらにはアイコンを使用してメッセージを視覚的に分類するのに最適です。画像はオプションですが、1:1 の比率にする必要があります。  

![Image of a classic card with recommended details and a classic card example]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> 1行のテキストが理想的です。<br> ここで Liquid を使用してメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的です。<br> ここで Liquid を使用してメッセージをパーソナライズできます。 |
| リンク テキスト | オプション。<br> 13ピクセル <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | オプション。<br> 1:1 の比率である必要があります。<br> 60 x 60 ピクセルの画質をお勧めします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Captioned Image %}

キャプション付き画像カードは、大規模なセールや新しいアプリ機能などの重要なコンテンツをアピールし、注目を集めるのに最適な方法です。

![Image of a Captioned Image card with recommended details and a Captioned Image card example]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px; 太字 <br> 1行のテキストが理想的です。<br> ここで Liquid を使用してメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px; 標準の太さ <br> 2行から4行のテキストが理想的です。<br> ここで Liquid を使用してメッセージをパーソナライズできます。 |
| リンク テキスト | オプション。<br> 13ピクセル <br> ウェブページへのリンク、またはアプリ内へのディープリンク。 |
| 画像 | 4:3 の比率を推奨します。<br> 最小幅は600ピクセルです。 <br> 高解像度の PNG、JPEG、GIF をサポートします。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Banner %}

派手なものがお望みなら、バナーカードがおすすめです。これはあなたの希望に応じて完全にカスタマイズされます。他の場所でコンテンツを作成してアップロードするだけで、自分だけの美しいカードが完成します。

![Image of a banner with recommended details and a banner example]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| リンクされたカード | オプション。<br> 13ピクセル <br> クリック時の行動は、Web ページへのリンク、またはアプリ内へのディープリンクです。 |
| 画像 | 任意のアスペクト比がサポートされます。<br> 最小幅は600ピクセルです。 <br> 高解像度の PNG、JPEG、GIF をサポートします。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## グローバルクリエイティブ詳細 {#general}

コンテンツ カードには、最初から優れた機能が備わっています。現時点では、Braze アカウントでカードのスタイル設定をネイティブに行うことはできませんが、統合中にコンテンツ カードのタイプとコンテンツ カード フィードごとにスタイル設定できます。詳細については、[コンテンツ カードのカスタマイズ][4]を参照してください。

### 解雇行為

ユーザーがカードを閉じるには、モバイルでスワイプするか、 `close X` 次のスクリーンショットに示すように、関数を実行します。の `x` Web SDK の場合のみ、ホバーすると表示されます。

![カードのスワイプまたは閉じる動作を示す画像][5]

ユーザーがすべてのカードを閉じた場合、または新しい更新をプッシュしていない場合、ユーザーのフィードは通常次のようになります。

![空のコンテンツ カード フィードの画像][6]{: style="max-width:45%"}

{% alert tip %}
ユーザーが関連するアクションを実行したときにコンテンツ カードを閉じるように設定することで、コンテンツ カードの関連性を維持します。たとえば、ユーザーが購入するとすぐにプロモーション コンテンツ カードが閉じられるように設定すると、すでに購入した商品のオファーが引き続き表示されないようになります。
{% endalert %}

### コンテンツ カードで GIF を使用する

| Android 用コンテンツ カード | iOS 用コンテンツ カード | Web 用コンテンツ カード |
| --- | --- |---|
| Android SDK は、デフォルトではアニメーション GIF のサポートを提供しません。GIF サポートを有効にする方法の詳細については、[GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/GIFs/)を参照してください。| Swift SDK は、デフォルトではアニメーション GIF サポートを提供しません。GIF サポートを有効にする方法の詳細については、[GIF サポート チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。| GIF サポートは、Web SDK 統合にデフォルトで含まれています。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

<br><br>

[1]: {% image_buster /assets/img/content_card_classic.png %}
[2]: {% image_buster /assets/img/content_card_captioned.png %}
[3]: {% image_buster /assets/img/content_card_banner.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
[7]: {{site.baseurl}}/developer_guide/customization_guides/customization_overview
