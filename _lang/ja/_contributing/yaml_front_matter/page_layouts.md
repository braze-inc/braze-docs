---
nav_title: ページレイアウト
article: Page layouts
description: "これらは、ページのYAML フロントマターの`page_layout` キーに割り当てることができるページレイアウトです。"
page_order: 2
noindex: true
---

#  ページレイアウト

> これらは、ページのYAML フロントマターの[`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout) キーに割り当てることができるページレイアウトです。一般的な情報については、[Content Management]({{site.baseurl}}/contributing/content_management/#layouts)を参照してください。

## 前提条件

ページレイアウトを使用するには、[`page_layout`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-layout) キーをYAML の前面に追加する必要があります。

\`\`\`markdown
---
開始
article_title: Brazeドークスの使用開始
page_layout: PAGE\_LAYOUT\_VALUE
---
\`\`\`

`PAGE_LAYOUT_VALUE` を次のセクションのいずれかの値に置き換えます。

## ビジュアルレイアウト

### APIページ

`api_page` 値は、API ページ形式を適用するために使用されます。以下の例では、この形式が[リスト積分]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/) ページに適用されます。

{% tabs local %}
{% tab example output %}
![An example page using the 'api_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

### 開発者ガイド

`dev_guide` の値は、開発者ガイド形式を適用するために使用されます。次の例では、この形式が[Catalogs Endpoints]({{site.baseurl}}/api/endpoints/catalogs) ページに適用されます。 

{% tabs local %}
{% tab example output %}
![An example page using the 'dev_guide' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/dev_guide.png %})
{% endtab %}
{% endtabs %}

### 特集ページ

`featured` 値は、機能するページ形式を適用するために使用されます。次の例では、この形式が[Predictive Events]({{site.baseurl}}/user_guide/sage_ai/predictive_suite/predictive_events) ページに適用されます。

{% tabs local %}
{% tab example output %}
![An example page using the 'featured' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/featured.png %})
{% endtab %}
{% endtabs %}

### 用語集ページ

`glossary_page` 値は、用語集ページ形式を適用するために使用されます。次の例では、この形式が[プッシュ通知のタイプ]({{site.baseurl}}/user_guide/message_building_by_channel/push/types)ページに適用されます。

{% tabs local %}
{% tab example output %}
![An example page using the 'glossary_page' layout.]({% image_buster /assets/img/contributing/styling_examples/layouts/glossary_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
特定のレイアウトでは、`"guide_top_text:"` のような値は、Markdown フォーマットを使用すると便利な場合があります。特定のYAML値には、Markdownフォーマットを使用できます。そのためには、`>` をYAML 値として追加し、後でテキストをインデントします。
<br>
次に例を示します。<br>
guide\_top\_text: ><br>
    \# これは、マークダウン形式の例です
{% endalert %}

## その他のレイアウト

### 空白の設定

`blank_config` 値は、Braze Docs のページを非表示にし、ユーザを自動的に`www.braze.com/docs` にリダイレクトするために使用されます。詳細については、[リダイレクトURL]({{site.baseurl}}/contributing/content_management/redirecting_urls/?tab=home%20page#redirecting-a-page)を参照してください。

### リダイレクト

`redirect` 値は、ページ内ヘッダーのURL をリダイレクトするために使用されます。詳細については、[リダイレクトURL]({{site.baseurl}}/contributing/content_management/redirecting_urls/#redirecting-a-heading)を参照してください。
