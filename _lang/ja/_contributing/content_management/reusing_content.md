---
nav_title: コンテンツを再利用する
article: Reusing content
description: "コンテンツの一貫性を高め、コンテンツ作成にかかる時間を短縮できるように、Braze Docs全体でコンテンツを再利用する方法を学びましょう。"
page_order: 5
noindex: true
---

# コンテンツを再利用する

> コンテンツの一貫性を高め、コンテンツ作成にかかる時間を短縮できるように、Braze Docs全体でコンテンツを再利用する方法を学びましょう。コンテンツの再利用に関する一般的な情報については、「[コンテンツ管理]({{site.baseurl}}/contributing/content_management/#content-reuse)」を参照してください。

Jekyll でのコンテンツの再利用は、インクルードを使用して行われます。インクルードは通常の Markdown `_includes` ファイルとしてディレクトリに保存されます。ただし、`_docs`ディレクトリ内のMarkdownファイルとは異なり、これらのファイルにはYAMLフロントマターは必要ありません。

{% multi_lang_include contributing/prerequisites.md %}

## インクルードの作成

`.md``_includes`ディレクトリに拡張子を付けた新しい Markdown ファイルを作成します。インクルードファイルはこのディレクトリのどこにでも保存できますが、関連するコンテンツはサブディレクトリを使用してまとめておくのが一番です。ファイルツリーは次のようになっているはずです。

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── site_generator.md
```

ページにコンテンツを追加し、必ず [Braze Docs スタイルガイドに従ってください]({{site.baseurl}}/contributing/style_guide/)。すでに YAML フロントマターがあるページにインクルードを追加する予定がある場合は、インクルードにフロントマターを追加しないでください。コンテンツは次のようになっているはずです。

{% raw %}
\`\`\`markdown
## サイトジェネレーター 

Braze Docsは、人気の静的サイトジェネレーター（SSG）であるJekyllを使用して構築されています。これにより、コンテンツファイルとデザインファイルをコンテンツファイル用とデザインファイル用に別々のディレクトリに保存できます。`_docs` `assets`サイトを構築すると、Jekyllは各ファイルをインテリジェントにマージし、XMLおよびHTMLデータとしてディレクトリに保存します。`_site`詳細については、「[Jekyll ディレクトリ構造](https://jekyllrb.com/docs/structure/)」を参照してください。

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/braze_docs_github.png %})

寄稿者は、主に以下のディレクトリで作業することになります。

| ディレクトリ | 説明 |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)| Braze Docs用に書かれたすべてのコンテンツが、Markdownで記述されたテキストファイルとして含まれています。テキストファイルは、[[APIセクションやユーザーガイドセクションなど`_api`]({{site.baseurl}}/user_guide/introduction)]({{site.baseurl}}/api/home)、`user_guide`ドキュメントサイトを反映したディレクトリとサブディレクトリに整理されています。|
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes)| `_docs` ディレクトリ内のどのファイルでも再利用できるテキストファイル (「include」と呼ばれる) が含まれています。通常、インクルードは標準フォーマットを使用しない短いモジュール形式のコンテンツです。この場所に保存されているファイルは、[コンテンツを再利用する上で重要です](#content-reuse)。|
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)| ブレイズドキュメントのすべての画像が含まれています。`_docs``_includes`またはディレクトリ内の任意のテキストファイルをこのディレクトリにリンクして、そのページに画像を表示できます。|
{: .reset-td-br-1 .reset-td-br-2}
\`\`\`
{% endraw %}

{% alert tip %}
詳細なチュートリアルについては、「[コンテンツの作成]({{site.baseurl}}/contributing/content_management/pages/#writing-content)」を参照してください。
{% endalert %}

## インクルードを参照する

インクルードを参照するには、関連する Markdown ファイル内で以下の構文を使用してください。

{% raw %}
```plaintext
{% multi_lang_include PATH_TO_INCLUDE %}
```
{% endraw %}

`PATH_TO_INCLUDE``_includes`ディレクトリ内の相対パスに置き換えます。たとえば、次のファイルツリーがあるとします。

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── prerequisites.md
```

リファレンスは以下のようになります。

{% tabs local %}
{% tab example input %}
{% raw %}
\`\`\`markdown
# ページ

> Braze Docs でページを作成、変更、削除する方法をご覧ください。

{% multi_lang_include contributing/prerequisites.md %}
\`\`\`
{% endraw %}
{% endtab %}

{% tab example output %}
![Content reuse example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/includes.png %}){: style="max-width:90%;"}
{% endtab %}
{% endtabs %}
