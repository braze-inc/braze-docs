---
nav_title: クラウディナリ
article_title: クラウディナリ
description: "ここでは、Brazeとクラウディナリーの連携について概説した。"
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# クラウディナリ

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) は、"画像の管理、編集、最適化、および配信に使用される動画 プラットフォームで、s および動画をチャネルs およびカスタマージャーニーs のすべてのキャンペーンにスケールで提供します。統合され有効になっている場合、Cloudinaryのメディアマネジメントは、Braze キャンペーンおよびキャンバスのダイナミックな、文脈に応じた or 状況に即した、およびパーソナライズされたのアセット配信に役立ちます。 

## この統合について

クラウディナリをBrazeに接続すると、クラウディナリアセットに保存されているビジュアルメディアをブランドがBraze メッセージング チャネルで使用できるようになります。クラウディナリのダイナミックなリンクを使用すると、Braze ユーザー 属性s に基づいてリアルタイムで"画像s と動画s を選択およびカスタマイズできます。クラウディナリーとBrazeが一緒になって、それぞれの商品のストーリーを伝え、オンリーワンの体験をスケールでお届けする、視覚的に豊かなものづくりを支援するパーソナライズされた キャンペーンです。

このページでは、クラウディナリとBrazeの間で可能な、ただし網羅的ではない、4つの統合方法について概説します。これらの統合方法は、主にCloudinary のメディアライブラリから手動でコピーされたアセットリンクの変更に依存しています。 

{% alert important %}
[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) を使用してCloudinary の[Admin API](https://cloudinary.com/documentation/admin_api#banner) を呼び出すなど、より高度な統合方法を使用できますが、アプリの侵入は顧客s 間で異なります。クラウディナリおよびBraze 顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

| 要件     | 説明 |                        
|-----------------------|-----------------|
| クラウディナリーアカウント  | この提携の事前タグを行うには、[クラウディナリアカウント](https://cloudinary.com/users/register_free?utm_source=braze+docs+page)が必要です  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## 統合方法

{% alert tip %}
これらの統合方法の一部では、`f_auto` および`q_auto` Cloudinary Transformations を使用します。これにより、["画像](https://cloudinary.com/documentation/image_transformations#banner) および[動画](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) アセットのビヘイビアとアプリの稼働率をより詳細にカスタマイズできます。Transformations を含めるようにCloudinary アセットリンクを変更する方法の詳細については、[Transformation URL 構造](https://cloudinary.com/documentation/image_transformations#transformation_url_structure) を参照してください。
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## クラウドインダムを使用したキャンペーンアセットの選択

Braze キャンペーンおよびキャンバスでクラウディナリのDAM から"画像 s および動画 s を直接使用する最も直接的な方法は、クラウディナリメディアライブラリの**アセット** ページからURL をプルすることです。

![クラウディナリの"画像アセットライブラリのグリッドビューで、ハイライトされた"画像s の右上に"URL"ツールヒントが表示されます。]({% image_buster /assets/img/cloudinary/one.png %})

### 画像とGIFの設定

1. クラウディナリのDAM から、**Assets**> **Media Library**> **Assets**> **コピーURL**を選択して、"画像またはGIF URL をコピーします。
2. HTML で"画像 タグを作成し、コピーしたURL に`f_auto,q_auto` を追加して"画像またはGIF を最適化します。

#### サンプル"画像

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### 動画設定

1. Cloudinary のDAM から、**Assets**> **Media Library**> **Assets**> **Copy URL** に移動して、"画像またはGIF リンクをコピーします。
2. HTML で動画 タグを作成し、コピーしたURL に`f_auto,q_auto` を追加して、動画の形式と画質を自動的に最適化します。

#### サンプル動画

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

具体的なAndroidおよびiOSの考慮事項については、[ビデオ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/)を参照してください。 

{% endtab %}
{% tab Convert videoes into GIFs %}

## 動画es をメールs のGIF に変換する

動画アセットをGIF に自動的に変換するには、`f_auto:animated` [Cloudinary Transformation](https://cloudinary.com/documentation/image_transformations/) を使用します。これは、Braze メール チャネルを使用している場合に特に重要です。GIFは、メールの給与読み込むを削減するために最適化されており、高すぎると配信可能性の問題を引き起こす可能性があります。 

### 変換設定

1. クラウディナリDAM から動画 URL をコピーします。
2. "画像 タグを作成し、`f_auto:animated,fl_lossy` を追加してGIF サイズを縮小し、クライアントに最適なアニメーション形式を選択します。
3. `c_scale,w_nnn` を追加して、メールレイアウトの目的のGIF 幅に対応します。
4. `e_loop` を追加してアニメーションをループします。

#### GIF URL の例

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## ターゲット属性に基づいてキャンペーンアセットを動的に選択

この積分法は、属性s上のユーザー群dごとに最適なアセットをリアルタイムでインテリジェントに選択することにより、ダイナミックなの媒体パーソナライゼーションを可能にする。 

Liquid タグ s をBraze キャンペーン メッセージ内のクラウディナリリンクのパラメータとして含めると、メッセージの送信時に、関連するBraze 属性 s がLiquid タグ s とダイナミックな置き換えられます。これには、言語層や顧客層など、ユーザー固有のデータを使用できます。クラウディナリはこれらの属性を使用して、どのキャンペーンアセットがそのユーザーに最も適しているかを判断し、自動的に正しい"画像または動画を返します。これにより、受信者 s は文脈に応じた or 状況に即した関連性があり、ブランドアプリが確認されたアセットのみを受け取ります。

### 仕組み

クラウディナリは、[タグs](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) および[構造化メタデータ(SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) を使用してキャンペーンアセットを整理し、検索可能にします。 

それぞれのキャンペーンアセットは、キャンペーン タグ(`spring_launch` など) にグループ化され、`language=en` や`tier=gold` などのBraze 属性s に対応する構造化メタデータフィールドで拡張されます。Braze がCloudinary リンクを呼び出すと、[Custom Function](https://cloudinary.com/documentation/custom_functions#javascript_filters) は受信属性s を処理し、一致するタグs とメタデータを持つアセットを検索して、最適な一致を返します。 

完全に一致するものが見つからない場合は、すべてのエクスペリエンスで連続性を確保するために、フォールバックまたは「次善」の選択肢が自動的に選択されます。アセットが選択されると、Cloudinary のトランスフォーメーションレイヤー(`f_auto` または`q_auto` など) によって配信用のメディアが最適化されます。このようにタグの作成、メタデータ、およびカスタムファンクションを組み合わせることで、開発者 はパーソナライズされたアセットの配信を自動化する柔軟なAPI 駆動の方法を提供します。

{% alert tip %}
クラウディナリの[`braze-personalization` GitHub repo](https://github.com/cloudinary-devs/braze-personalization) にあるカスタム関数の作成とアプリ、および特定のキャンペーンのアセット選択とフォールバックオプションのカスタム関数のサンプルを参照してください。詳細なガイダンスについては、Cloudinary サポートチームにお問い合わせください。
{% endalert %}

### 前提条件

ダイナミックなアセットの選択を有効にするには、Cloudinary はタグとメタデータに基づいてアセットのセットを返すことができる必要があります。リスト配信タイプが制限されている場合、クラウディナリはBraze キャンペーン s でのパーソナライズされたアセット選択に必要なダイナミックな一覧を提供できません。
- リスト配信タイプを制限解除します。Cloudinaryコンソールでセキュリティ設定を開き、制限"画像タイプのリソースリストアイテムをクリアします。

### ダイナミックセレクト設定

1. Cloudinary でアセットのタグとメタデータを設定します。
2. カスタムファンクションをCloudinary DAM に読み込むします。
3. 目的のタグのクラウディナリURL を作成します。
4. タグ URL を基に、ダイナミックな "画像 リキッドタグ s を追加して、Braze 属性 s とカスタムファンクションを組み込みます。

#### URL の例

このサンプルでは、Cloudinary のアセットに、Braze 属性s に対応する期待値が入力された2 つの定義済みSMD フィールドs ("locale" および"オーディエンス") があることを前提としています。また、キャンペーンに必要なアセットには"samples" タグ が与えられ、カスタムファンクション`segmentedBanner.js` がCloudinary アカウントにアップロードされました。 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### 出力URL

- オーディエンス`internal`およびロケール`en`を持つユーザーsのアウトプットURL: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- オーディエンス`external`およびロケール`es`を持つユーザーsのアウトプットURL: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- フォールバック"画像: 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## パーソナライズ"画像の生成

Cloudinary の[テキストオーバーレイ変換](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) は、Cloudinary アセット内のBrazeからのユーザーデータを使用します。 

以下の例は、`l_text` トランスフォーメーションを使用してユーザーの名前をアセットに挿入する方法を示しています。キャンペーン s およびキャンバスを開発する際に、Liquid タグ s を活用して、`l_text` パラメータに入力するテキストを決定することで、さらにカスタマイズすることができます。

トランスフォーメーションパラメータを使用してアセットを設計する方法の詳細については、Cloudinary サポートチームにお問い合わせください。

### 例`l_text` 変換

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### 出力URL の例

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![海を見下ろす青い屋根のある白い教会は、"John Smith"という言葉の"画像の左上にあり、オパージュの暗い大きな長方形に課されています。]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
