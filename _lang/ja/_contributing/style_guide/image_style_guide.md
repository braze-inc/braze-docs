---
nav_title: 画像コピースタイルガイド
article_title: 画像コピースタイルガイド
description: "Braze Docs で画像を作成およびスタイリングするためのガイドラインです。"
page_order: 1
noindex: true
---

# 画像コピースタイルガイド

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## 配置とサイズの最適化

可能な限り、画像は関連するテキストの近くに配置し、画像スタイリング用の Markdown を使用して大きな画像のサイズを調整してください。コンテンツによっては、画像と利用可能なスペースに応じて、[テキストをページの左側または右側にアンカーする]({{site.baseurl}}/home/styling_test_page/#image-test)ことで対応します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="画像配置を正しく最適化した例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="画像配置の最適化が不適切な例。"></td></tr>
</tbody>
</table>
{:/}

## 画像のトリミング

関連するセクションを近くでトリミングしてください。必要でない限り、左側のナビゲーションバーは含めず、代わりに記事内にナビゲーションの指示を記載してください。これにより、UI の変更が発生した際に更新が必要な画像の数を抑えることができます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="適切にトリミングされた画像の例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="不適切にトリミングされた画像の例。"></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="適切にトリミングされた画像の例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="不適切にトリミングされた画像の例。"></td></tr>
</tbody>
</table>
{:/}

Braze Docs では各画像に既にボーダーが追加されているため、セクションのスクリーンショットではボーダーを省略してください。きれいなトリミングを目指します。ボーダーの外側または内側にコンポーネントがある場合は、ボーダーを残しても構いません。以下の画像を例として参照してください。

**推奨:**
![画像を正しくトリミングした例。]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**非推奨:**  
![画像のトリミングが不適切な例。]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**推奨:**  
![画像を正しくトリミングした例。]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## 機密情報のぼかし処理

名前、メールアドレス、API キーなどの個人を特定できる情報（PII）はぼかし処理を行ってください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="正しいぼかし処理の例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="不適切なぼかし処理の例。"></td></tr>
</tbody>
</table>
{:/}

## 重要なテキストを画像内に埋め込まない

すべてのユーザーが英語のテキストを読めるわけではなく、ページ翻訳ツールは画像内のテキストを翻訳しないため、画像内にテキストを埋め込むことは避けてください。テキストは記事内に記載するようにしてください。ユーザーのアクセシビリティを最大限に高めるため、画像には代替テキストを提供してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="画像内にテキストを埋め込まない正しい例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="画像内にテキストを埋め込んでしまった不適切な例。"></td></tr>
</tbody>
</table>
{:/}

## コンポーネントを強調しすぎない

必要でない限り、画像内のコンポーネントを強調しないでください。画像内の異なるコンポーネントをハイライトするには、青い四角形（最もアクセシブルなオプション）を細〜中程度の太さで使用してください。「ハイライトされたセクション」が通常の UI を遮らないようにしてください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="画像内のコンポーネントを正しく強調した例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="画像内のコンポーネントの強調が不適切な例。"></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="画像内のコンポーネントを正しく強調した例。"></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="画像内のコンポーネントの強調が不適切な例。"></td></tr>
</tbody>
</table>
{:/}