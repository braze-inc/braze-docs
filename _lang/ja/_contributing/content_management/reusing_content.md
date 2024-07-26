---
nav_title: コンテンツの再利用
article: Reusing content
description: "Braze Docs全体でコンテンツを再利用する方法を学習することで、コンテンツの一貫性を高め、コンテンツ作成の時間を短縮することができる。"
page_order: 4
noindex: true
---

# コンテンツの再利用

> Braze Docs全体でコンテンツを再利用する方法を学習することで、コンテンツの一貫性を高め、コンテンツ作成の時間を短縮することができる。コンテンツの再利用に関する一般的な情報は、[コンテンツ・マネジメントについてを]({{site.baseurl}}/contributing/content_management/#content-reuse)参照のこと。

Jekyllのコンテンツの再利用は、インクルードを使用して達成される。インクルードは、通常のMarkdownファイルとして`_includes` ディレクトリに保存される。しかし、`_docs` ディレクトリのMarkdownファイルとは異なり、これらのファイルにはYAMLのフロントマターが必要ない。

{% multi_lang_include contributing/prerequisites.md %}

## インクルードを作成する

`_includes` ディレクトリに、`.md` の拡張子を持つ新しいMarkdownファイルを作成する。インクルードファイルはこのディレクトリのどこにでも格納できるが、サブディレクトリを使って関連するコンテンツをまとめておくのがベストだ。ファイルツリーは以下のようになっているはずだ：

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── site_generator.md
```

ページにコンテンツを追加し、[Braze Docsスタイルガイドに]({{site.baseurl}}/contributing/style_guide/)必ず従うこと。すでにYAMLのフロントマターを持っているページにインクルードを追加するつもりなら、インクルードにフロントマターを追加しないこと。内容は以下のようなものであるべきだ：

{% raw %}
```markdown
## Site generator 

Braze Docs is built using Jekyll, a popular static-site generator (SSG) that allows content files and design files to be stored in separate directories, such as `_docs` for content files and `assets` for design files. When the site is built, Jekyll intelligently merges each file and stores them as XML and HTML data in the `_site` directory. For more information, see [Jekyll Directory Structure](https://jekyllrb.com/docs/structure/).

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/braze_docs_github.png %})

As a contributor, you'll primarily work within the following directories.

| Directory                                                                     | Description                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)         | Contains all the written content for Braze Docs as text files written in Markdown. Text files are organized into directories and subdirectories mirroring the docs site, such as `_api` for the [API section]({{site.baseurl}}/api/home) and `user_guide` for the [User Guide section]({{site.baseurl}}/user_guide/introduction). |
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes) | Contains text files (called "includes") that can be reused in any file within the `_docs` directory. Typically, includes are short, modular pieces of content that don't use standard formatting. The files stored in this location are important for [content reuse](#content-reuse).                                            |
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)       | Contains all the images for Braze Docs. Any text file in the `_docs` or `_includes` directory can link to this directory to display an image on its page.                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}
```
{% endraw %}

{% alert tip %}
詳しい説明は、「[コンテンツを書く]({{site.baseurl}}/contributing/content_management/pages/#writing-content)」を参照のこと。
{% endalert %}

## インクルードを参照する

インクルードを参照するには、関連するMarkdownファイル内で以下の構文を使う：

{% raw %}
```plaintext
{% multi_lang_include PATH_TO_INCLUDE %}
```
{% endraw %}

`PATH_TO_INCLUDE` を`_includes` ディレクトリ内部からの相対パスに置き換える。例えば、次のようなファイルツリーがあるとする：

```bash
braze-docs
└── _includes
    ├── alerts
    ├── archive
    └── contributing
        └── prerequisites.md
```

参考文献は以下のようなものだ：

{% tabs ローカル %}
{% tab 入力例 %}
{% raw %}
```markdown
# Pages

> Learn how to create, modify, and remove pages on Braze Docs.

{% multi_lang_include contributing/prerequisites.md %}
```
{% endraw %}
{% endtab %}

{% tab 出力例 %}
![Braze Docsのコンテンツ再利用例]({% image_buster /assets/img/contributing/styling_examples/includes.png %}){: style="max-width:90%;"}
{% endtab %}
{% endtabs %}
