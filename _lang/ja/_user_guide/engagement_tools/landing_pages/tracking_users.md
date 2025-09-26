---
nav_title: ユーザーの追跡
article_title: フォームを使用したユーザーの追跡
description: "メッセージにLiquidタグを追加して、ランディングページからフォームを送信するユーザーを識別する方法を学習します。"
page_order: 2
---

# フォームを使用したユーザーの追跡

> ランディングページでフォームを送信したユーザーを追跡するには、ランディングページ Liquid タグをメッセージに追加します。このリキッドタグは、メール、SMS、アプリ内メッセージなど、すべてのBraze メッセージングチャネルでサポートされています。トラッキングデータの詳細については、[ランディングページトラッキングデータについて]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data)を参照してください。

## CDI の仕組み

Braze では、{% raw %}`{% landing_page_url %}`{% endraw %} Liquid タグを任意の単一またはマルチチャネルメッセージに追加できます。ユーザがそのランディングページを訪問し、フォームを送信すると、Brazeはそのユーザの新しいプロファイルを作成するのではなく、そのデータを既存のプロファイルに自動的にリンクします。次の例では、ランディングページ Liquid タグを使用して、顧客を調査にリンクします。

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
また、ページURL を外部チャネルに埋め込むことで、リード生成のランディングページを使用することもできます。ランディングページを作成したら、**ランディングページ詳細**に移動してランディングページの一意のURL を取得します。
{% endalert %}

## ランディングページのLiquid タグの使用

### 前提条件

開始する前に、[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)と[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)を作成する必要があります。

### ステップ1:ページ URL を確認する {#page-url}

Braze はランディングページのURL を使用して、独自のLiquid タグを生成します。現在のページ URL を変更する場合は、[**メッセージング**] > [**ランディングページ**] に移動し、ランディングページを開きます。**ページURL**で、新しいページURLを入力できます。

{% alert warning %}
メッセージ送信後にページ URL を変更すると、古い URL を使用してランディングページにアクセスしようとするユーザーは `404` ページに送信されます。
{% endalert %}

![Braze でのランディングページのページ URL の例。]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### ステップ2: Liquid タグの生成

**Messaging**> **Campaigns**に移動し、キャンペーンを選択します。メッセージエディタで、**Personalization** を選択します。

![ドラッグ＆ドロップエディターの [パーソナライズを追加する] ボタン。]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze は、[ランディングページURL](#page-url) を使用して自動的にLiquid タグを生成します。タグを生成するには、次の表を参照してください。

\|**パーソナライゼーションタイプ**| [**ランディングページ**] を選択します。|
\|**ランディングページ**| [以前に作成した](#prerequisites)ランディングページを選択します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

メッセージにLiquid タグを追加するには、**Insert** を選択するか、スニペットをクリップボードにコピーして手動で追加します。

![選択したランディングページの自動生成されたLiquid タグ。]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

スニペットは次のようになります。

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### ステップ 3:メッセージを確定して送信する

Liquid スニペットをメッセージに埋め込み、残りのメッセージを確定します。以下に例を示します。

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

準備ができたら、メッセージを送信してランディングページを通じてユーザーの追跡を開始できます。
