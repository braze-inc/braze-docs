---
nav_title: 相互参照
article: Cross-referencing
description: "他のページを相互参照する方法については、Brazeドックスを参照してください。"
page_order: 4
noindex: true
---

# 相互参照

> 他のページを相互参照する方法については、Brazeドックスを参照してください。Braze Docs 以外のページを相互参照するには、[標準のMarkdown 構文](https://www.markdownguide.org/basic-syntax/#links) を使用します。

{% multi_lang_include contributing/prerequisites.md %}

## クロスリファレンスの作成

相互参照を作成する場合、インラインメソッドまたは参照スタイルメソッドのいずれかを使用できます。インライン方式は明瞭性を優先し、リファレンス方式は可読性を優先した。

{% tabs %}
{% tab in-line %}
関連するMarkdown ファイルを開き、インラインリンクを作成します。

{% subtabs %}
{% subtab Markdown %}

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

以下を交換します。

| プレースホルダ| 説明                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | ページタイトルまたは関連アクション|
| `SHORT_URL` | `https://www.braze.com` が削除されたページURL。|
{: .reset-td-br-1 .reset-td-br-2}

インラインリンクは、次のようになります。

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/docs/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}
{% endsubtab %}

{% subtab HTML %}

{% raw %}
```markdown
<a href='[SHORT_URL]'>[LINK_TEXT]</a>
```
{% endraw %}

以下を交換します。

| プレースホルダ| 説明                                        |
|-------------|----------------------------------------------------|
| `LINK_TEXT` | ページタイトルまたは関連アクション|
| `SHORT_URL` | `https://www.braze.com` が削除されたページURL。|
{: .reset-td-br-1 .reset-td-br-2}

インラインリンクは、次のようになります。

{% raw %}
```markdown
To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}

{% endtab %}

{% tab reference-style %}
関連するMarkdown ファイルを開き、リファレンススタイルのリンクを作成します。

```markdown
[LINK_TEXT][REFERENCE_NUMBER]
```

以下を交換します。

| プレースホルダ| 説明|
|--------------------|--------------------------------------------------------------------------|
| `LINK_TEXT` | ページタイトルまたは関連アクション|
| `REFERENCE_NUMBER` | このページの別の参照形式のリンクにまだ割り当てられていない正の整数を割り当てます。|
{: .reset-td-br-1 .reset-td-br-2}

参考文献は以下のようになります。

```markdown
Before continuing, [create your SSH token][2]. When you're finished, see [Step 2: Uploading your token][5].
```

ページの下部で、関連するリンクを追加します。

{% raw %}
```markdown
[REFERENCE_NUMBER]: {{site.baseurl}}SHORT_URL
```
{% endraw %}

以下を交換します。

| プレースホルダ| 説明|
|--------------------|---------------------------------------------------------|
| `REFERENCE_NUMBER` | リンク先の参照番号|
| `SHORT_URL` | `https://www.braze.com/docs` が削除されたページURL。|
{: .reset-td-br-1 .reset-td-br-2}

リンクは次のようになります。

{% raw %}
```markdown
[2]: {{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/
[5]: {{site.baseurl}}/developer_guide/platform_wide/swift#step-2-uploading-your-token
```
{% endraw %}
{% endtab %}
{% endtabs %}
