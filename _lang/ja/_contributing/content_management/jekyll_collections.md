---
nav_title: ジキル・コレクション
article_title: ジキルのコレクション
description: "Jekyllコレクションの作成方法を学習し、Braze Docsに新しい主要セクションを追加できるようにする。"
page_order: 6
---

# ジキルのコレクション

> Jekyllコレクションの作成方法を学習し、Braze Docsに新しい主要セクションを追加できるようにする。詳しくは、[Jekyll Collectionsを](https://jekyllrb.com/docs/collections/)参照のこと。

{% alert important %}
あなたのコンテンツのために新しいJekyllコレクションを作成する必要はほとんどないだろう。コンテンツをどこに保存すべきかわからない場合は、[GitHub issueを作成](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)しよう。
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## Jekyllコレクションを作成する

### ステップ 1:新しいコレクションを追加する

`config.yml` で、`collections` キーの下に新しいJekyllコレクションを追加する。

```yaml
collections:
  COLLECTION_KEY:
    title: COLLECTION_TITLE
    output: true
    default_nav_url: COLLECTION_URL/
```

次のように置き換えます。

| placeholder              | 説明                                       |
|-------------------|---------------------------------------------------|
| `COLLECTION_KEY`  | あなたのコレクションの名前を表すユニークな単語を1つ選ぶ。小文字のみを使用する。 |
| `COLLECTION_TITLE`| コレクション名をタイトル・ケースで記す。        |
| `COLLECTION_URL`  | コレクションのランディングページのデフォルトURL。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

新しいコレクションは以下のようなものになるはずだ：

```yaml
collections:
  partners:
    title: Technology Partners
    output: true
    default_nav_url: home/
```

### ステップ2:デフォルトのレイアウトを設定する

`config.yml` で、`defaults` キーの下にコレクションのデフォルトレイアウトを設定する。

```yaml
-  
  scope:
    path: ""
    type: "COLLECTION_KEY"
  values:
    nav_level: 1
```

`COLLECTION_KEY` を[前回](#step-1-add-a-new-collection)設定したキーに置き換える。以下に例を示します。

```yaml
defaults:
  -
    scope:
      path: ""
      type: "partners"
    values:
      nav_level: 1
```

### ステップ 3:ランディングページを作成する

`_docs` ディレクトリに新しいディレクトリを作成し、`home.md` という名前の新しいMarkdownファイルを追加する。

```plaintext
braze-docs
└── _docs
    └── _COLLECTION_NAME
        └── home.md
```

`_COLLECTION_NAME` 、コレクション名を小文字に置き換え、スペースをアンダースコアに置き換える。以下に例を示します。

```plaintext
braze-docs
└── _docs
    └── _technology_partners
        └── home.md
```

{% alert important %}
コレクションのディレクトリ名はアンダースコアで始まる必要がある。
{% endalert %}

### ステップ 4:追加コンテンツを追加する（オプション）

新しいコレクションのために、セクションとサブセクションを追加する。詳しい説明は[セクションの]({{site.baseurl}}/contributing/content_management/sections/#creating-a-section)作成を参照のこと。

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION
        └── SUBSECTION
            ├── NEW_DIRECTORY
            └── NEW_FILE.md
```

### ステップ 5: リダイレクトファイルを設定する

`braze-docs/_docs/_docs_pages` で、コレクション用の新しいMarkdownファイルを作成する。

```bash
COLLECTION_KEY.md
```

`COLLECTION_KEY` を[前回](#step-1-add-a-new-collection)設定したキーに置き換える。以下に例を示します。

```plaintext
braze-docs
└── _docs
    └── _docs_pages
        └── partners.md
```

Markdownファイルに、以下のYAMLフロント・マターを追加する：

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/COLLECTION_KEY/home
permalink: COLLECTION_KEY/
---
```

`COLLECTION_KEY` を[前回](#step-1-add-a-new-collection)設定したキーに置き換える。以下に例を示します。

```markdown
---
config_only: true
noindex: true
layout: redirect
redirect_to: /docs/partners/home
permalink: partners/
---
```
