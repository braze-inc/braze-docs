---
nav_title: コンテンツ管理
article: Content Management
description: "これは Braze Docs でのコンテンツ管理方法の概要です。"
page_order: 2 
noindex: true
---

# コンテンツ管理について

> これは Braze Docs でのコンテンツ管理方法の概要です。特定のトピックについて詳しく知るには、ナビゲーションの専用トピックページを選択してください。

## 方法論

Braze Docsは、バージョン管理システムを使用してソフトウェア開発ライフサイクルを反映したドキュメントを管理する方法であるdocs-as-codeを使用して管理されます。Braze Docs は Git バージョン管理システムを使用しているため、寄稿者はお互いの作業を上書きすることなく、同じドキュメントを編集できます。詳細については、「[バージョン管理と Git について](https://docs.github.com/en/get-started/using-git/about-git#about-version-control-and-git)」を参照してください。

![The Braze Docs repository's home page on GitHub.]({% image_buster /assets/img/contributing/github/home_page.png %})

## サイトジェネレーター 

Braze Docsは、コンテンツファイルとデザインファイルを別々のディレクトリに保存できる、人気の静的サイトジェネレーターであるJekyllを使用して構築されています。これにより、`_docs`コンテンツファイル用とデザインファイル用など、コンテンツファイルとデザインファイルを別々のディレクトリに保存できます。`assets`サイトを構築すると、Jekyllは各ファイルをインテリジェントにマージし、XMLおよびHTMLデータとしてディレクトリに保存します。`_site`詳細については、「[Jekyll ディレクトリ構造](https://jekyllrb.com/docs/structure/)」を参照してください。

![The home page for Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

寄稿者は、主に以下のディレクトリで作業することになります。

| ディレクトリ | 説明 |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`_docs`](https://github.com/braze-inc/braze-docs/tree/develop/_docs)| Braze Docs用に書かれたすべてのコンテンツが、Markdownで記述されたテキストファイルとして含まれています。テキストファイルは、[[APIセクションやユーザーガイドセクションなど`_api`]({{site.baseurl}}/user_guide/introduction)]({{site.baseurl}}/api/home)、`user_guide`ドキュメントサイトを反映したディレクトリとサブディレクトリに整理されています。|
| [`_includes`](https://github.com/braze-inc/braze-docs/tree/develop/_includes)| `_docs` ディレクトリ内のどのファイルでも再利用できるテキストファイル (「include」と呼ばれる) が含まれています。通常、インクルードは標準フォーマットを使用しない短いモジュール形式のコンテンツです。この場所に保存されているファイルは、[コンテンツを再利用する上で重要です](#content-reuse)。|
| [`assets`](https://github.com/braze-inc/braze-docs/tree/develop/assets)| ブレイズドキュメントのすべての画像が含まれています。`_docs``_includes`またはディレクトリ内の任意のテキストファイルをこのディレクトリにリンクして、そのページに画像を表示できます。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
詳細な手順については、「[プレビューの生成」を参照してください。]({{site.baseurl}}/contributing/generating_a_preview/)
{% endalert %}

## ページ

Braze Docsの各ページはマークダウン構文で記述され、ファイル拡張子を使用してマークダウンファイルとして保存されます。`.md`各Markdownファイルの上部では、YAMLフロントマターを使用して各ページに非表示のメタデータを追加します。

\`\`\`markdown
---
METADATA\_KEY:METADATA\_VALUE
---

# CONTENT
\`\`\`

以下を置き換えてください。

| プレースホルダー | 説明 |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY` | サポートされているメタデータ型を表すキー。詳細については、「[メタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)」を参照してください。|
`METADATA_VALUE`| | メタデータ型のキーに割り当てられた値。詳細については、「[メタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)」を参照してください。|
| `CONTENT` | ページのコンテンツは Markdown 構文で記述されています。|
{: .reset-td-br-1 .reset-td-br-2}

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: Braze ドキュメントへの貢献
記事:Braze ドキュメントへの貢献
description: 「Braze Docs への貢献を始めるために必要なものは次のとおりです。」
page_order:0
search_tag: 寄稿
---

# Braze ドキュメントへの貢献

> Braze Docs に貢献していただきありがとうございます！毎週火曜日と木曜日には、コミュニティの投稿をまとめて Braze Docs にデプロイしています。このガイドを使用して、次回のデプロイ時に変更内容をマージしてください。
\`\`\`
{% endtab %}

{% tab example output %}
![Example page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
[詳細な手順については、「ページの作成」を参照してください。]({{site.baseurl}}/contributing/content_management/pages/#creating-a-page)
{% endalert %}

## 画像

`assets/img`画像は内部にPNGファイルとして保存されます。`img`ディレクトリの構造は Braze Docs の構造と一致する必要はありませんが、関連する画像をサブディレクトリにまとめるのがベストです。

各画像は、次の構文を使用して1つまたは複数のページにリンクできます。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

以下を置き換えてください。

| プレースホルダー | 説明 |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
`ALT_TEXT`| | 画像の代替テキスト。これは、スクリーンリーダーを使用するユーザーが Braze Docs に同等にアクセスできるようにするために必要です。|
| `IMAGE` | `img` ディレクトリから始まる画像への相対パス。| |
{: .reset-td-br-1 .reset-td-br-2}

インライン画像は次のようになるはずです。

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

{% alert tip %}
詳細な手順については、「[新しい画像の追加]({{site.baseurl}}/contributing/content_management/images/#adding-a-new-image)」を参照してください。
{% endalert %}

## セクション

[Braze Docs [は主要なセクションとサブセクションに分かれています](#primary-sections)。](#subsections)

### 主要セクション

Braze ドキュメントの主なセクションは以下のとおりです。

- [Brazeドックスホーム]({{site.baseurl}})
- [ユーザーガイド]({{site.baseurl}}/user_guide/introduction)
- 開発者ガイド
- [Braze API ガイド]({{site.baseurl}}/api/home)
- [テクノロジーパートナー]({{site.baseurl}}/partners/home)
- [Braze ヘルプ]({{site.baseurl}}/help/home)

これらの主要セクションには、Braze Docsのどのページからでもサイトヘッダーからアクセスできます。

![The primary sections as shown on the site header on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/header.png %})

[各主要セクションはJekyllコレクションを使用して構築されているため](https://jekyllrb.com/docs/collections/)、関連するコンテンツをグループ化して簡単に管理できます。すべてのプライマリセクションはコレクションですが、すべてのコレクションがプライマリセクションであるとは限らないことに注意してください。Braze Docs コレクションの全リストは Jekyll 設定ファイルにあります。`_config.yml`

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
  hidden: # Hidden pages not directly linked via navigation
    title: Braze
    output: true
    hidden: true
  docs_pages: # Site specific pages. ie main redirects and search
    title: Braze
    output: true
    hidden: true
```

リストされている各コレクションは、`_docs`ディレクトリ内のディレクトリを表します。

```plaintext
braze-docs
└── _docs
    ├── _api
    ├── _developer_guide
    ├── _docs_pages
    ├── _help
    ├── _hidden
    ├── _home
    ├── _partners
    └── _user_guide
```

各主要セクションのランディングページは、`page_order:``0`キーがに設定された標準のMarkdownファイルです。

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
page_order: 0
nav_title: ホーム
article_title: Braze ユーザーガイド
layout: user\_guide
user\_top\_header:「Braze ユーザーガイド」
---
\`\`\`
{% endtab %}

{% tab example output %}
![An example landing page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/primary_section.png %})
{% endtab %}
{% endtabs %}

### サブセクション

Braze Docsのすべての主要セクションには1つ以上のサブセクションがあり、それぞれが左側のナビゲーションの展開可能な項目を表しています。

プライマリセクションとは異なり、サブセクションはランディングページの有無にかかわらず設定できます。ランディングページのないサブセクションは、Braze Docsの役に立たないページの数を最小限に抑えながら、関連するコンテンツをまとめて整理するのに役立ちます。サブセクションがランディングページの有無にかかわらず、すべてのサブセクションはリポジトリ内のディレクトリと Markdown ファイルの両方を表します。例については、以下を参照してください。

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
[詳細な手順については、「セクションの作成]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section)」を参照してください。
{% endalert %}

`_primary_section`ディレクトリでは、`subsection_a`はランディングページで構成されていませんが`subsection_b`、にはランディングページが設定されています。次の例では、`subsection_a.md``config_only:`がに設定されています。これにより`true`、このページはランディングページとしてレンダリングされません。

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: サブセクション A
page_order: 0
config_only: true
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section without a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_config_only.png %})
{% endtab %}
{% endtabs %}

ただし、`subsection_b.md``config_only:`キーを使用しないため、_このページはランディングページとしてレンダリングされます_。

{% tabs local %}
{% tab example input %}
\`\`\`markdown
---
nav_title: サブセクション B
page_order: 0
---
\`\`\`
{% endtab %}

{% tab example output %}
![The left-side navigation on Braze Docs, showing an example of an expanded section with a landing page.]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
`config_only:``true`がに設定されているサブセクションはページとして表示されませんが、そのサブセクション内のページの URL にはサブセクションのディレクトリ名が引き続き使用されます。詳細については、「[URL](#urls)」を参照してください。
{% endalert %}

## コンテンツ再利用

Jekyllには、タグを使用して書かれたコンテンツをドキュメント全体で再利用する機能があります。`include``_includes`インクルードはディレクトリにあり、MarkdownまたはHTML構文で記述できます。

```markdown
{% raw %}{% multi_lang_include RELATIVE_PATH/FILE %}{% endraw %}
```

以下を置き換えてください。

| プレースホルダー | 説明 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RELATIVE_PATH` | (オプション) `_includes` ディレクトリからファイルへの相対パス。これは、`_includes`などのディレクトリ内のディレクトリからファイルをインクルードする場合にのみ必要です`_includes/braze/upgrade_notice.md`。|
`FILE`| | ファイル拡張子を含むファイルの名前。|
{: .reset-td-br-1 .reset-td-br-2}

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
![Content reuse example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/includes.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
詳細な手順については、「[コンテンツの再利用]({{site.baseurl}}/contributing/content_management/reusing_content)」を参照してください。
{% endalert %}

## レイアウト

デフォルトでは、`default.html` `_layouts` Jekyllはディレクトリ内のレイアウトを使用してBraze Docsの各ページを作成します。ただし、YAML `layout:` フロントマターのキーにレイアウトを割り当てることで、さまざまなレイアウトを使用できます。

\`\`\`markdown
---
layout: レイアウト値
---
\`\`\`

レイアウトファイルの名前とファイル拡張子を削除した名前に置き換えます`LAYOUT_VALUE`。

{% tabs local %}
{% tab example input %}
**ファイルツリー**

```plaintext
braze-docs
└── _layouts
    └── api_page.html
```

**ページ内メタデータ**

\`\`\`markdown
---
layout: page
---
\`\`\`
{% endtab %}

{% tab example output %}
![API glossary layout example on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/layouts/api_page.png %})
{% endtab %}
{% endtabs %}

{% alert tip %}
詳しくは、「[ページレイアウト]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts)」を参照してください。
{% endalert %}

## URL

Braze Docs の URL は、常にドキュメントリポジトリ内のディレクトリ構造と一致します。次のファイルツリーの例を考えると、の URL `page_a.md` はになります`https://www.braze.com/docs/primary_section/subsection_a/page_a`。

```plaintext
braze-docs
└── _docs
    └── _primary_section
        └── subsection_a
            └── page_a.md
```

これには、[`config_only:`がに設定されているサブセクションにあるページの](#subsections) URL が含まれます。`true``config_only`サブセクションはページとしてレンダリングされませんが、サブセクションのディレクトリ名は、そのディレクトリ内のページの URL を生成するために引き続き使用されます。例については、以下を参照してください。

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

{% tabs local %}
{% tab subsection a %}

**ランディングページの例**

\`\`\`markdown
---
nav_title: サブセクション A
page_order: 1
config_only: true
---
\`\`\`

`subsection_a.md`はランディングページとして設定されているため、固有の URL `page_a.md` `page_b.md` のみを受け取ります。`subsection_b.md`URL **は受信されません**。

**URL の例**

```plaintext
Subsection A URL: N/A
Page A URL: https://www.braze.com/docs/primary_section/subsection_a/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_a/page_b
```
{% endtab %}
{% tab subsection b %}
**ランディングページの例**

\`\`\`markdown
---
nav_title: サブセクション B
page_order: 2 
---
\`\`\`

`subsection_b.md`がランディングページ、、として設定されているので`page_a.md``page_b.md`、固有の URL `subsection_b.md` が割り当てられます。

**URL の例**

```plaintext
Subesction B URL: https://www.braze.com/docs/primary_section/subsection_b
Page A URL: https://www.braze.com/docs/primary_section/subsection_b/page_a
Page B URL: https://www.braze.com/docs/primary_section/subsection_b/page_b
```
{% endtab %}
{% endtabs %}
