---
nav_title: ページレイアウト
article: Page layouts
description: "これらは、ページのYAMLフロントマターで`page_layout`キーに割り当てることができるページレイアウトです。"
page_order: 2
noindex: true
---

#  ページレイアウト

> これらは、ページのYAMLフロントマターで[`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout)キーに割り当てることができるページレイアウトです。一般的な情報については、[コンテンツ管理について]({{site.baseurl}}/contributing/content_management/#layouts)を参照してください。

## 前提条件

ページレイアウトを使用するには、YAMLフロントマターに[`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout)キーを追加する必要があります。

```markdown
---
nav_title: Getting started
article_title: Getting started with Braze Docs
page_layout: PAGE_LAYOUT_VALUE
---
```

次のセクションの値の1つと`PAGE_LAYOUT_VALUE`を置き換えます。

## ビジュアルレイアウト

### APIページ

`api_page` 値はAPIページ形式を適用するために使用されます。次の例では、この形式が[リスト統合]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)ページに適用されます:

{% tabs ローカル %}
{% tab 例の出力 %}
![「api_page」レイアウトを使用した例のページです。]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

### 開発者ガイド

`dev_guide` の値は開発者ガイド形式を適用するために使用されます。次の例では、この形式が[カタログエンドポイント]({{site.baseurl}}/api/endpoints/catalogs)ページに適用されます: 

{% tabs ローカル %}
{% tab 例の出力 %}
![「dev_guide」レイアウトを使用した例のページ。]({% image_buster /assets/img/contributing/styling_examples/layouts/dev_guide.png %})
{% endtab %}
{% endtabs %}

### 注目のページ

`featured` の値は、注目ページのフォーマットを適用するために使用されます。次の例では、この形式が[予測イベント]({{site.baseurl}}/user_guide/sage_ai/predictive_suite/predictive_events)ページに適用されます:

{% tabs ローカル %}
{% tab 例の出力 %}
![「注目」レイアウトを使用した例のページです。]({% image_buster /assets/img/contributing/styling_examples/layouts/featured.png %})
{% endtab %}
{% endtabs %}

### 用語集ページ

`glossary_page` 値は用語集ページ形式を適用するために使用されます。次の例では、この形式が[プッシュ通知の種類]({{site.baseurl}}/user_guide/message_building_by_channel/push/types)ページに適用されます:

{% tabs ローカル %}
{% tab 例の出力 %}
![「glossary_page」レイアウトを使用した例のページです。]({% image_buster /assets/img/contributing/styling_examples/layouts/glossary_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
特定のレイアウトでは、`"guide_top_text:"`のような値はMarkdown形式にすることで恩恵を受けるかもしれません。特定のYAML値にMarkdown形式を使用できます。そのためには、`>`をYAML値として追加し、その後のテキストをインデントします。
<br>
以下に例を示します。<br>
ガイドトップテキスト: ><br>
    \# これは例のMarkdownフォーマットです
{% endalert %}

## 他のレイアウト

### 空白の構成

`blank_config` の値は、Braze Docsでページを非表示にし、ユーザーを自動的に `www.braze.com/docs` にリダイレクトするために使用されます。詳細については、[URL のリダイレクト]({{site.baseurl}}/contributing/content_management/redirecting_urls/?tab=home%20page#redirecting-a-page)を参照してください。

### リダイレクト

`redirect` 値は、ページ内の見出しのURLをリダイレクトするために使用されます。詳細については、[URLのリダイレクト]({{site.baseurl}}/contributing/content_management/redirecting_urls/#redirecting-a-heading)を参照してください。
