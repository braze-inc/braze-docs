---
nav_title: ユーザーの追跡
article_title: フォームを使用したユーザーの追跡
description: "メッセージにLiquidタグを追加して、ランディングページからフォームを送信するユーザーを識別する方法を学習します。"
page_order: 2
---

# フォームを使用したユーザーの追跡

> {% raw %}`{% landing_page_url %}`{% endraw %} Liquid タグをメッセージに追加して、ランディングページでフォームを送信したユーザーを追跡する方法について説明します。このリキッドタグは、メール、SMS、アプリ内メッセージなど、すべてのBraze メッセージングチャネルでサポートされています。トラッキングデータの詳細については、[ランディングページトラッキングデータについて]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data)を参照してください。

## CDI の仕組み

Braze では、ランディングページのLiquid タグを1 つまたは複数のチャンネルのメッセージに追加できます。ユーザがそのランディングページを訪問し、フォームを送信すると、Brazeはそのユーザの新しいプロファイルを作成するのではなく、そのデータを既存のプロファイルに自動的にリンクします。

{% alert tip %}
また、ページURL を外部チャネルに埋め込むことで、リード生成のランディングページを使用することもできます。ランディングページを作成したら、**ランディングページ詳細**に移動してランディングページの一意のURL を取得します。
{% endalert %}

## ランディングページのLiquid タグの使用

### 前提条件

開始する前に、[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)と[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)を作成する必要があります。

### ステップ1:ページURL の確認 {#page-url}

Braze はランディングページのURL を使用して、独自のLiquid タグを生成します。現在のページURL を変更する場合は、**Messaging**> **Landing Pages** に移動し、ランディングページを開きます。**ページURL**で、新しいページURLを入力できます。

{% alert warning %}
メッセージの送信後にページURL を変更すると、古いURL を使用してランディングページにアクセスしようとするユーザは、`404` ページに送信されます。
{% endalert %}

![Braze.] ({% image_buster /assets/img/landing_pages/url-handle-example.png %}) のランディングページの例のページURL{: style="max-width:80%;"}

### ステップ2: Liquid タグの生成

**Messaging**> **Campaigns**に移動し、キャンペーンを選択します。メッセージエディタで、**Personalization** を選択します。

![ドラッグアンドドロップエディタの'Add personalization' ボタン。]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze は、[ランディングページURL](#page-url) を使用して自動的にLiquid タグを生成します。タグを生成するには、次の表を参照してください。

\|**カスタマイズタイプ**| **ランディングページ**.|を選択します。
\|**ランディングページ**|ランディングページを選択[以前に作成した](#prerequisites).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

メッセージにLiquid タグを追加するには、**Insert** を選択するか、スニペットをクリップボードにコピーして手動で追加します。

![選択したランディングページの自動生成されたLiquid タグ。]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

スニペットは次のようになります。

{% raw %}
```ruby
{% landing_page_url my-custom-url-handle %}
```
{% endraw %}

### ステップ 3:メッセージを確定して送信する

Liquid スニペットをメッセージに埋め込み、残りのメッセージを確定します。準備ができたら、メッセージを送信してランディングページを通じてユーザーの追跡を開始できます。
