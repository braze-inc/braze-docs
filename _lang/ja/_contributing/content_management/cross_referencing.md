---
nav_title: 相互参照
article: Cross-referencing
description: "Braze Docsの他のページを相互参照する方法を学習する。"
page_order: 3
noindex: true
---

# 相互参照

> Braze Docsの他のページを相互参照する方法を学習する。Braze Docs以外のページを相互参照するには、[標準的なMarkdown構文を](https://www.markdownguide.org/basic-syntax/#links)使う。相互参照についての一般的な情報は、[コンテンツ管理についてを]({{site.baseurl}}/contributing/content_management/#cross-references)参照のこと。

{% multi_lang_include contributing/prerequisites.md %}

## クロスリファレンスを作成する

{% alert important %}
Liquidの{% raw %}`{% tab %}`{% endraw %} タグは参照スタイルのリンクをサポートしていないので、インラインリンクのみを以下にドキュメントする。既存の参照リンクは引き続き機能するが、もはや推奨されない。
{% endalert %}

{% tabs %}
{% tab マークダウン %}
該当するMarkdownファイルを開封し、インラインリンクを作成する。

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

次のように置き換えます。

| placeholder | 説明                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | ページタイトルまたは関連アクション。                  |
| `SHORT_URL` | `https://www.braze.com` を削除したページのURL。 |
{: .reset-td-br-1 .reset-td-br-2}

インラインリンクは以下のようなものであるべきだ：

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/docs/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}
{% endtab %}

{% tab HTML %}
該当するMarkdownファイルを開封し、インラインリンクを作成する。

{% raw %}
```markdown
<a href='[SHORT_URL]'>[LINK_TEXT]</a>
```
{% endraw %}

次のように置き換えます。

| placeholder | 説明                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | ページタイトルまたは関連アクション。                  |
| `SHORT_URL` | `https://www.braze.com` を削除したページのURL。 |
{: .reset-td-br-1 .reset-td-br-2}

インラインリンクは以下のようなものであるべきだ：

{% raw %}
```markdown
To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.
```
{% endraw %}
{% endtab %}
{% endtabs %}
