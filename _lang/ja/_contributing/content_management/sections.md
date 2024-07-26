---
nav_title: セクション
article: Managing Sections
description: "Braze Docsでセクションを作成し、注文する方法を学習する。"
page_order: 2
noindex: true
---

# セクションのマネージャー

> Braze Docsでセクションを作成し、注文する方法を学習する。代わりに個々のページを作成、変更、削除するには、「[ページ]({{site.baseurl}}/contributing/content_management/pages/)」を参照のこと。セクションに関する一般的な情報については、[コンテンツ管理についてを]({{site.baseurl}}/contributing/content_management/#sections)参照のこと。

{% multi_lang_include contributing/prerequisites.md %}

## セクションを作成する

### ステップ 1:ディレクトリとMarkdownファイルを作成する

該当する主要セクションまたはサブセクションを開封し、新しいセクション用のディレクトリとMarkdownファイルを作成する。

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION 
        └── SUBSECTION 
            ├── NEW_DIRECTORY 
            └── NEW_FILE.md
```

次のように置き換えます。

| placeholder       | 説明                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIMARY_SECTION` | 新しいコンテンツが属する主セクションの名前。詳しくは、[プライマリーセクションを]({{site.baseurl}}/contributing/content_management/#primary-sections)参照のこと。                                                                              |
| `SUBSECTION`      | 該当する場合、新しいコンテンツが属するサブセクションの名前。詳細は[サブセクションを]({{site.baseurl}}/contributing/content_management/#subsections)参照のこと。                                                                              |
| `NEW_DIRECTORY`   | 新しいセクションの名前。[Braze Docsスタイルガイドに]({{site.baseurl}}/contributing/style_guide/)従うこと。すべて小文字を使用し、特殊文字を削除し、スペースをアンダースコア (`_`) に置き換える。この名前は`NEW_FILE` と一致しなければならない。       |
| `NEW_FILE`        | 新しいセクションの名前。[Braze Docsスタイルガイドに]({{site.baseurl}}/contributing/style_guide/)従うこと。すべて小文字を使用し、特殊文字を削除し、スペースをアンダースコア (`_`) に置き換える。この名前は`NEW_DIRECTORY` と一致しなければならない。 |
{: .reset-td-br-1 .reset-td-br-2}

ディレクトリ構造は以下のようになっているはずだ：

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            └── getting_started.md
```

### ステップ2:セクションを設定する

新しいセクションを作成する際、ランディングページの有無を設定することができる。

- **ランディングページがある：**この方法は、「はじめに」セクションのランディングページのように、前提条件やユーザー・ジャーニーの概要を列挙した専用の概要が必要な場合に使用する。
- **ランディングページはない：**セクションに専用の概要が必要ない場合は、この方法を使う。[Braze Docsのスタイルガイドに]({{site.baseurl}}/contributing/style_guide/)あるように、コンテンツは常に有用であるべきなので、有用なコンテンツがほとんどない場合はランディングページを追加しないこと。

{% tabs %}
{% tab ランディングページ付き %}
新しいMarkdownファイルを開封し、以下のテンプレートを追加する。その他のテンプレートについては、[テンプレートを]({{site.baseurl}}/contributing/templates/)参照のこと。

```markdown
---
nav_title: NAV_TITLE
article_title: LANDING_PAGE_TITLE
description: SHORT_DESCRIPTION
---

# LANDING_PAGE_TITLE 

> SHORT_DESCRIPTION

## HEADING

CONTENT
```

次のように置き換えます。

| placeholder          | 説明                                                                                                                                                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NAV_TITLE`          | 左側のナビゲーションバーに表示されるあなたのページのタイトル。ほとんどの場合、`nav_title` は、`article_title` と一致すべきであるが、スペースを節約するために、_短くても似たような_タイトルを使ってもよい。                                  |
| `LANDING_PAGE_TITLE` | ランディングページのタイトル。メタデータの`LANDING_PAGE_TITLE` の値は検索エンジンの検索結果に使われ、見出し1の`LANDING_PAGE_TITLE` の値はページに表示されるタイトルに使われる。                             |
| `SHORT_DESCRIPTION`  | あなたのページについての1-2文の短い説明文。YAMLのメタデータの`SHORT_DESCRIPTION` の値は検索エンジンの結果のために使われ、一方、見出し1の後の`SHORT_DESCRIPTION` の値はページでレンダリングされる説明のために使われる。 |
| `HEADING`            | 見出し2セクションのタイトル。                                                                                                                                                                                                        |
| `CONTENT`            | 見出し2セクションの本文段落。                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
必要に応じて[メタデータや]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)見出しを追加してほしい。
{% endalert %}
{% endtab %}

{% tab ランディングページなし %}
サブセクションのMarkdownファイルを開封し、以下のメタデータを追加して、ページのナビゲーションタイトルを設定し、ランディングページを無効にする。

```markdown
---
nav_title: NAV_TITLE
config_only: true
---
```

{% alert tip %}
必要に応じて[メタデータや]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)見出しを追加してほしい。
{% endalert %}

`NAV_TITLE` 、左側のナビゲーションバーに表示されるあなたのページのタイトルに置き換える。あなたのページは次のようなものであるべきだ：

```markdown
---
nav_title: Getting started
page_order: 2
noindex: true
config_only: true
---
```
{% endtab %}
{% endtabs %}

### ステップ 3:ページを追加する

新しいディレクトリに、各ページ用のMarkdownファイルを作成する。デフォルトのページレイアウトを使用するには、[ステップ]({{site.baseurl}}/contributing/content_management/sections/?tab=with%20landing%20page#step-2-configure-your-section)2のテンプレートを使用する。ディレクトリ構造は以下のようになっているはずだ：

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            │    ├── integrating_the_sdk.md 
            │    └── setting_up_push_notifications.md
            └── getting_started.md
```

各ページにコンテンツを追加し終わったら、[セクションの順序付けに](#ordering-a-section)進む。

{% alert tip %}
ページにコンテンツを追加するための完全なチュートリアルについては、[ページを]({{site.baseurl}}/contributing/content_management/pages/#writing-content)参照のこと。
{% endalert %}

## セクションを注文する

セクションを順番に並べるには、そのセクションのMarkdownファイルを開封し、そのYAMLフロントマター内の [`page_order`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-order)キーを検索する。

```markdown
---
page_order:
---
```

`page_order` キーは、左側のナビゲーションバー上のセクションにおけるページの相対的な順序を表し、負でない任意の数字（`0` 、`20` 、`5.5` など）を設定できる。`page_order` つまり、カレント・ディレクトリにある各MarkdownファイルのCurrentsを知る必要があるが、他のディレクトリ（サブディレクトリを含む）のCurrentsを知る必要はない。

現在のディレクトリにある各Markdownファイルの`page_order` キーを任意の非負の数に設定する。以下の例では、`page_order` を`2` に設定している。  

```markdown
---
nav_title: Subsection B
page_order: 2 
---

# Subsection B landing page
```

出力は以下のようになる：

![Braze Docsの左側ナビゲーション。「セクションB」のランディングページは3番目に表示されている。]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
