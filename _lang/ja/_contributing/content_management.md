---
nav_title: コンテンツのマネージャー
article: Managing Content
description: "Braze Docsのコンテンツ管理方法の概要を説明する。"
page_order: 2 
noindex: true
---

# コンテンツマネージャーについて

> これは、Braze Docsのコンテンツ管理方法の概要である。特定のトピックについて学習するには、ナビゲーションの専用トピックページを選択する。

## 方法論

Braze Docsは、docs-as-codeを使用して管理されている。docs-as-codeは、バージョンコントロールシステムを使用することで、ソフトウェア開発者のライフサイクルを反映したドキュメント管理方法である。Braze Docsは、Gitバージョンコントロールシステムを使用しているため、貢献者は、お互いの作業を上書きすることなく、同じドキュメントに取り組むことができる。詳しくは、[バージョンコントロールとGitについてを](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git)参照のこと。

![GitHub 上の Braze Docs リポジトリのホームページ。]({% image_buster /assets/img/contributing/github/home_page.png %})

## サイト・ジェネレーター 

Braze DocsはJekyllを使用して構築されている。Jekyllは人気のある静的サイトジェネレーターで、コンテンツファイルとデザインファイルを別々のディレクトリ（コンテンツファイルは`_docs` 、デザインファイルは`assets` ）に保存することができる。サイトが構築されると、Jekyllはインテリジェントに各ファイルをマージし、XMLとHTMLデータとして`_site` ディレクトリに格納される。詳細については、参照してください[Jekyllディレクトリ構造](https://jekyllrb.com/docs/structure/).

![Braze Docsのホームページ]({% image_buster /assets/img/contributing/styling_examples/home.png %})

コントリビューターとして、主に以下のディレクトリを担当する。

| ディレクトリ                                                                     | 説明                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)         | Braze DocsのすべてのコンテンツがMarkdownで書かれたテキストファイルとして格納されている。テキストファイルは、[APIセクションは]({{site.baseurl}}/api/home) `_api` 、[ユーザーガイドセクションは]({{site.baseurl}}/user_guide/introduction) `user_guide` のように、docsサイトを反映したディレクトリとサブディレクトリに整理されている。 |
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes) | `_docs` ディレクトリ内のどのファイルでも再利用できるテキストファイル（「インクルード」と呼ばれる）が含まれている。通常、インクルードとは、標準的な書式を使用しない、短くてモジュール化されたコンテンツのことである。この場所に保存されているファイルは、[コンテンツの再利用にとって](#content-reuse)重要である。                                            |
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)       | Braze Docsのすべての画像写真が含まれている。`_docs` または`_includes` ディレクトリにあるテキストファイルは、このディレクトリにリンクして、そのページに画像、写真を表示することができる。                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
完全なチュートリアルについては、[プレビューを生成するを]({{site.baseurl}}/contributing/generating_a_preview/)参照のこと。
{% endalert %}

## ページ

Braze Docsの各ページはMarkdown構文で記述され、`.md` ファイル拡張子を使用したMarkdownファイルとして保存される。各Markdownファイルの先頭には、各ページの隠されたメタデータを追加するためにYAMLフロントマターが使われる。

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# CONTENT
```

以下を交換する。

| placeholder      | 説明                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY`   | サポートされているメタデータ・タイプを表すキー。詳細は[メタデータを]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)参照のこと。 |
| `METADATA_VALUE` | メタデータ・タイプのキーに割り当てられた値。詳細は[メタデータを]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)参照のこと。  |
| `CONTENT`        | Markdown構文で書かれたページのコンテンツ。                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs ローカル %}
{% tab 入力例 %}
```markdown
---
nav_title: Contributing to Braze Docs
article: Contributing to Braze Docs
description: "Here's what you need to start contributing to Braze Docs!"
page_order: 0
search_tag: Contributing
---

# Contributing to Braze Docs

> Thanks for contributing to Braze Docs! Every Tuesday and Thursday, we merge community contributions and deploy them to Braze Docs. Use this guide to get your changes merged during our next deployment.
```
{% endtab %}

{% tab 出力例 %}
![Braze Docsのページ例]({% image_buster /assets/img/contributing/styling_examples/page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
完全なチュートリアルについては、[ページを作成するを]({{site.baseurl}}/contributing/content_management/pages/#creating-a-page)参照のこと。
{% endalert %}

## 画像、写真

画像, 写真はPNGファイルとして`assets/img` 内部に保存される。`img` ディレクトリの構造は、Braze Docsの構造と一致させる必要はないが、関連する画像写真をサブディレクトリにまとめるのがベスト。

各画像写真は、以下の構文を使って1つ以上のページにリンクすることができる。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

以下を交換する。

| placeholder | 説明                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | 画像, 写真のaltテキスト。これは、Braze Docsをスクリーンリーダーを使っている人たちにも同じようにアクセシブルにするために必要なことである。 |
| `IMAGE`     | `img` ディレクトリを起点とする画像, 写真への相対パス。                                                      |
{: .reset-td-br-1 .reset-td-br-2}

インライン画像は以下のようなものであるべきだ：

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert tip %}
詳しい説明は、[新しい画像を]({{site.baseurl}}/contributing/content_management/images/#adding-a-new-image)追加するを参照のこと。
{% endalert %}

## セクション

Braze Docsは、[主要なセクションと](#primary-sections) [サブセクションで](#subsections)構成されている。

### 主要セクション

Braze Docsの主なセクションは以下の通りである：

- [Brazeドックスホーム]({{site.baseurl}})
- [ユーザーガイド]({{site.baseurl}}/user_guide/introduction)
- [開発者ガイド]({{site.baseurl}}/developer_guide/home)
- [Braze API ガイド]({{site.baseurl}}/api/home)
- [テクノロジーパートナー]({{site.baseurl}}/partners/home)
- [Braze ヘルプ]({{site.baseurl}}/help/home)
- [Braze Docsに貢献する]({{site.baseurl}}/contributing/home/)

**Contributing to Braze Docs**以外の主なセクションは、Braze Docsのどのページからでもサイトヘッダーからアクセスできる。

![Braze Docsのサイトヘッダーに表示されている主要セクション]({% image_buster /assets/img/contributing/styling_examples/header.png %})

各主要セクションは[Jekyllコレクションを](https://jekyllrb.com/docs/collections/)使用して構築されており、関連するコンテンツをグループ化して簡単に管理できる。すべてのプライマリー・セクションがコレクションである一方で、すべてのコレクションがプライマリー・セクションであるわけではないことを覚えておいてほしい。Braze Docsコレクションの完全なリストは、Jekyllの設定ファイル`_config.yml` 。

```yaml
collections:
  home:
    title: Documentation
    output: true
    default_nav_url: ''
    page_order: 1
  user_guide:
    title: User Guide
    output: true
    default_nav_url: introduction/
    page_order: 2
  developer_guide:
    title: Developer Guide
    output: true
    default_nav_url: home/
    page_order: 3
  api:
    title: API
    output: true
    default_nav_url: home/
    page_order: 4
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
    page_order: 5
  help:
    title: Help
    output: true
    default_nav_url: home/
    page_order: 6
  contributing:
    output: true
    default_nav_url: contributing/
  hidden: # Hidden pages not directly linked via navigation
    title: Braze
    output: true
    hidden: true
  docs_pages: # Site specific pages. ie main redirects and search
    title: Braze
    output: true
    hidden: true
```

記載されている各コレクションは、`_docs` ディレクトリ内のディレクトリを表している。

```plaintext
braze-docs
└── _docs
    ├── _api
    ├── _contributing
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

各主要セクションのランディングページは、`page_order:` キーが`0` に設定された標準的なMarkdownファイルである。

{% tabs ローカル %}
{% tab 入力例 %}
```markdown
---
page_order: 0
nav_title: Home
article_title: Braze User Guide
layout: user_guide
user_top_header: "Braze User Guide"
---
```
{% endtab %}

{% tab 出力例 %}
![Braze Docsのランディングページの例]({% image_buster /assets/img/contributing/styling_examples/primary_section.png %})
{% endtab %}
{% endtabs %}

### サブセクション

Braze Docsのすべての主要セクションには、1つ以上のサブセクションがあり、それぞれが左側のナビゲーションで展開可能な項目を表している。

プライマリーセクションとは異なり、サブセクションはランディングページの有無にかかわらず設定できる。ランディングページのないサブセクションは、Braze Docsの有用でないページ数を最小限に抑えながら、関連するコンテンツをまとめて整理するのに役立つ。サブセクションがランディングページありで設定されていても、ランディングページなしで設定されていても、すべてのサブセクションはリポジトリ内のディレクトリとMarkdownファイルの両方を表す。例として、以下を参照のこと。

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% alert tip %}
詳しい説明は[セクションの]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section)作成を参照のこと。
{% endalert %}

`_primary_section` 、`subsection_a` にはランディングページが設定されていないが、`subsection_b` にはランディングページが設定されている。以下の例では、`subsection_a.md` は`config_only:` に`true` を設定し、このページがランディングページとしてレンダリングされるのを防いでいる。

{% tabs ローカル %}
{% tab 入力例 %}
```markdown
---
nav_title: Subsection A
page_order: 0
config_only: true
---
```
{% endtab %}

{% tab 出力例 %}
![Braze Docsの左側ナビゲーション。ランディングページのない拡張セクションの例を示す。]({% image_buster /assets/img/contributing/styling_examples/subsection_config_only.png %})
{% endtab %}
{% endtabs %}

しかし、`subsection_b.md` は`config_only:` キーを使わないので、このページはランディングページとしてレンダリングさ_れる_。

{% tabs ローカル %}
{% tab 入力例 %}
```markdown
---
nav_title: Subsection B
page_order: 0
---
```
{% endtab %}

{% tab 出力例 %}
![Braze Docsの左側ナビゲーション。ランディングページのある拡張セクションの例を示す。]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
`config_only:` 」を「`true` 」に設定したサブセクションは、ページとしてレンダリングされないが、サブセクションのディレクトリ名は、そのサブセクションのページのURLに使用される。詳しくは[URLを](#urls)参照のこと。
{% endalert %}

## クロスリファレンス

相互参照とは、Braze Docsのあるページが、Braze Docsの別のページにリンクしていることである。Braze Docsはサイトの要件により、相互参照リンクのための[標準的なMarkdown構文を](https://www.markdownguide.org/basic-syntax/)サポートしていないため、Liquidを使って作成した。

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

あなたの相互参照リンクは以下のようなものであるべきだ：

{% raw %}
```markdown
Before continuing, [create your SSH token]({{site.baseurl}}/docs/developer_guide/platform_wide/sdk_authentication).
```
{% endraw %}

{% alert tip %}
完全なウォークスルーは、[相互参照を]({{site.baseurl}}/contributing/content_management/cross_referencing/)参照のこと。
{% endalert %}

## コンテンツの再利用

Jekyllは、`include` タグを使用してドキュメント全体で書かれたコンテンツを再利用する機能を提供する。インクルードは`_includes` ディレクトリにあり、MarkdownまたはHTML構文で記述できる。

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

次のように置き換えます。

| placeholder     | 説明                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RELATIVE_PATH` | (オプション）`_includes` ディレクトリからのファイルへの相対パス。これは、`_includes/braze/upgrade_notice.md` のように、`_includes` ディレクトリ内部のファイルをインクルードする場合にのみ必要である。 |
| `FILE`          | 拡張子を含むファイル名。                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

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
![Braze Docsのコンテンツ再利用例]({% image_buster /assets/img/contributing/styling_examples/includes.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
完全なチュートリアルについては、[コンテンツの再利用を]({{site.baseurl}}/contributing/content_management/reusing_content)参照のこと。
{% endalert %}

## レイアウト

デフォルトでは、JekyllはBraze Docsの各ページを構築するために、`_layouts` ディレクトリの`default.html` レイアウトを使用する。しかしながら、YAMLフロントマターの`layout:` キーにレイアウトを割り当てることで、異なるレイアウトを使うことができる。

```markdown
---
layout: LAYOUT_VALUE
---
```

`LAYOUT_VALUE` をレイアウトファイル名に置き換え、ファイル拡張子を削除する。

{% tabs ローカル %}
{% tab 入力例 %}
**ファイルツリー**

```plaintext
braze-docs
└── _layouts
    └── api_page.html
```

**ページ内メタデータ**

```markdown
---
layout: api_page
---
```
{% endtab %}

{% tab 出力例 %}
![Braze DocsのAPI用語集のレイアウト例]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
詳しくは[ページレイアウトを]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts)参照のこと。
{% endalert %}

## URL

Braze DocsのURLは、常にdocsリポジトリ内のディレクトリ構造と一致する。以下のファイルツリーの例を考えると、`page_a.md` のURLは`https://www.braze.com/docs/primary_section/subsection_a/page_a` となる。

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

これには、`config_only:` を`true` に設定した[サブセクションに](#subsections)あるページの URL も含まれる。`config_only` 、サブセクションはページとしてレンダリングされないが、サブセクションのディレクトリ名は、そのディレクトリ内のページのURLを生成するために使用される。例として、以下を参照のこと。

```plaintext
braze-docs
└── _docs
    └── _primary_section
        ├── subsection_a
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_b
        │   ├── page_a.md
        │   └── page_b.md
        ├── subsection_a.md # not configured as a landing page
        └── subsection_b.md # configured as a landing page  
```

{% tabs ローカル %}
{% tab a款 %}

**ランディングページの例**

```markdown
---
nav_title: Subsection A
page_order: 1 
config_only: true
---
```

`subsection_a.md`はランディングページとして設定されているため、`page_a.md`と`page_b.md`のみが固有のURLを受け取ります。`subsection_b.md`はURLを受け取り**ません**。

**URLの例**

```plaintext
Subsection A URL: N/A
Page A URL: https://www.braze.com/docs/primary_section/subsection_a/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_a/page_b
```
{% endtab %}
{% tab b項 %}
**ランディングページの例**

```markdown
---
nav_title: Subsection B
page_order: 2 
---
```

`subsection_b.md` はランディングページとして設定されているので、`page_a.md` 、`page_b.md` 、`subsection_b.md` はユニークなURLを受け取る。

**URLの例**

```plaintext
Subesction B URL: https://www.braze.com/docs/primary_section/subsection_b
Page A URL: https://www.braze.com/docs/primary_section/subsection_b/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_b/page_b
```
{% endtab %}
{% endtabs %}
