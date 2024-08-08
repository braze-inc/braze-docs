---
nav_title: メタデータ
article: Metadata
description: "これらは、ページのYAML フロントマターに追加できるメタデータキーです。"
page_order: 0
noindex: true
---

#  メタデータ

> これらは、ページのYAML フロントマターに追加できるメタデータキーです。詳細は、[Content Management]({{site.baseurl}}/contributing/content_management/#pages)を参照してください。

Markdown ファイルにメタデータを追加するには、Jekyll のフロントマター構文をファイルの先頭に追加する必要があります。

\`\`\`markdown
---
METADATA\_KEY:METADATA\_VALUE
---

# Brazeドークスの使用開始

Braze Docs またはdocs-as-code を初めて使用する場合は、チュートリアルから始めてください。
\`\`\`

以下を交換します。

| プレースホルダ| 説明                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY` | サポートされているメタデータ型を表すキー。次のセクションの[メタデータキー](#required-keys) で置き換えます。|
| `METADATA_VALUE` | メタデータキーに割り当てられた値。次のセクションで、メタデータキーのサポートされる値を確認します。|
{: .reset-td-br-1 .reset-td-br-2}

## 必須キー

### 記事タイトル

`article_title` キーは、オンライン検索結果のページタイトルとエンドユーザーのブラウザタブを設定するために使用されます。このキーは、任意の`string` 値を受け入れます。命名規則については、[ろう付けドックススタイルガイド]({{site.baseurl}}/contributing/style_guide/)を参照してください。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
article_title: Brazeドークスの使用開始
---
\`\`\`
{% endtab %}
{% endtabs %}

### 説明

`description` キーは、オンライン検索結果のページ記述を設定するために使用されます。このキーは、二重引用符で囲まれた150 文字未満の`string` 値を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
description: "Braze Docs を初めて使用する場合は、このステップバイステップのチュートリアルから始めてください。"
---
\`\`\`
{% endtab %}
{% endtabs %}

### ナビゲーションタイトル

`nav_title` キーは、Braze Docs の左側のナビゲーションバーのページタイトルを設定するために使用します。このキーでは、30 文字未満の`string` を使用できます。[`hidden`](#hide-page-from-navigation)キーが`true`に設定されている場合、`nav_title`は不要です。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
nav_title: はじめに
---
\`\`\`
{% endtab %}
{% endtabs %}

## オプションキー

### エンゲージメントツール

`tool` キーは、ページに関連するエンゲージメントツールを設定するために使用されます。このキーは、以下の`string` 値の1 つ以上をリストとして受け入れます。

- `dashboard`
- `docs`
- `canvas`
- `campaigns`
- `currents`
- `location`
- `media`
- `reports`
- `segments`
- `templates`

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
tool:
  \- 電流
  セグメント
---
\`\`\`
{% endtab %}
{% endtabs %}

### ナビゲーションからページを非表示にする

`hidden` キーは、Braze Docs の左側のナビゲーションからページを非表示にするために使用します。このキーはブール値`true` または`false` を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
hidden: 真
---
\`\`\`
{% endtab %}
{% endtabs %}

### 検索からページを隠す

`noindex` キーは、ページを内部および外部の検索結果(Braze Docs やGoogle Search など) から隠すために使用します。このキーはブール値`true` または`false` を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
noindex: true
---
\`\`\`
{% endtab %}
{% endtabs %}

### 目次を隠す

`hide_toc` キーは、ページ右側のページ内目次(TOC) を非表示にするために使用されます。このキーはブール値`true` または`false` を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
hide_toc: 真
---
\`\`\`
{% endtab %}
{% endtabs %}

### 目次から見出しを隠す

`toc_headers` キーは、ページ右側のページ内目次(TOC) から同じレベルのすべての見出しを非表示にするために使用されます。このキーでは、次の文字列値を使用できます。

- `h1`
- `h2`
- `h3`
- `h4`

`toc_headers` 割り当てられた値に一致するすべての見出しを非表示にします。特定の見出しを目次から非表示にするために使用することはできません。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
toc\_headers: h2
---
\`\`\`
{% endtab %}
{% endtabs %}

### メッセージングチャネル

`channel` キーは、ページの関連するメッセージングチャネルを設定するために使用されます。このキーは、以下の`string` 値の1 つ以上をリストとして受け入れます。

- `content cards`
- `email`
- `in-app messages`
- `news feed`
- `push`
- `sms`
- `webhooks`

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
チャネル:
  メール
  ニュースフィード
---
\`\`\`
{% endtab %}
{% endtabs %}

### ナビゲーションのみ

`config_only` キーは、ページのコンテンツを左側のナビゲーションバーで非表示にせずに非表示にするために使用します。[ランディングページのないセクションを作成する]({{site.baseurl}}/contributing/content_management/sections?tab=without%20landing%20page#step-2-configure-your-section)時に使用します。このキーは、ブール値`true` または`false` を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
config_only: true
---
\`\`\`
{% endtab %}
{% endtabs %}

### デフォルトURL を上書きする

`permalink` キーは、[`hidden`](#hide-page-from-navigation) キーと一緒に使用して、Braze Docs のページのデフォルトURL をオーバーライドします。`permalink` に割り当てられた値は、リダイレクトの前に`https://www.braze.com/docs` が付加されます。このキーは、以下の要件を満たす任意の`string` 値を受け入れます。

- 文字は小文字
- ワードはアンダースコアで区切られます(`_`)。
- "Directories"はスラッシュで区切られます(`/`)
- その他の特殊文字はすべて削除されます

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
hidden: 真
permalink: /support_contact/docs_team/
---
\`\`\`
{% endtab %}
{% endtabs %}

### ページレイアウト

`layout` キーは、ページのレイアウトを設定するために使用されます。`layout` が設定されていない場合、`default` レイアウトが使用されます。このキーは、次の`string` 値のいずれかを受け入れます。

- `api_page`
- `dev_guide`
- `featured_video`
- `featured`
- `glossary_page`
- `blank_config`
- `redirect`

各値の詳細については、[ページレイアウト]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/)を参照してください。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
page_layout: glossary\_page
---
\`\`\`
{% endtab %}
{% endtabs %}

### ページ順

`page_order` キーは、左側のナビゲーションバーの[ order sections]({{site.baseurl}}/contributing/content_management/sections/#ordering-a-section) に使用します。このキーは、負でない任意の数値(`0`、`20`、または`5.5` など) を受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
page_order: 35.6
---
\`\`\`
{% endtab %}
{% endtabs %}

### ページタイプ

`page_type` キーは、ページの書式を設定するために使用します。このキーは、次の`string` 値のいずれかを受け入れます。

- `glossary`
- `solution`
- `reference`
- `tutorial`
- `landing`
- `partner`
- `update`

各値の詳細については、[ページタイプ]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/)を参照してください。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
page_type: チュートリアル
---
\`\`\`
{% endtab %}
{% endtabs %}

### プラットフォーム

`platform` キーは、ページの関連プラットフォームを設定するために使用されます。このキーは、1 つ以上の[Braze SDKs]({{site.baseurl}}/developer_guide/home/) をリスト内の`string` 値として受け入れます。

{% tabs local %}
{% tab usage example %}
\`\`\`markdown
---
プラットフォーム: 
  iOS
  Web
  Android
---
\`\`\`
{% endtab %}
{% endtabs %}
