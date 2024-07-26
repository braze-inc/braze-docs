---
nav_title: メタデータ
article: Metadata
description: "これらはページのYAMLフロントマターに追加できるメタデータキーである。"
page_order: 0
noindex: true
---

#  メタデータ

> これらはページのYAMLフロントマターに追加できるメタデータキーである。より一般的な情報については、[コンテンツマネージャーについてを]({{site.baseurl}}/contributing/content_management/#pages)参照のこと。

Markdownファイルにメタデータを追加するには、ファイルの先頭にJekyllのフロントマター構文を追加する必要がある。

```markdown
---
METADATA_KEY: METADATA_VALUE
---

# Getting started with Braze Docs

If you're new to Braze Docs or docs-as-code, start with our tutorial.
```

次のように置き換えます。

| placeholder      | 説明                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| `METADATA_KEY`   | サポートされているメタデータ・タイプを表すキー。次のセクションの[メタデータ・キーで](#required-keys)置き換える。 |
| `METADATA_VALUE` | メタデータのキーに割り当てられた値。次のセクションで、メタデータ・キーがサポートしている値を確認する。                 |
{: .reset-td-br-1 .reset-td-br-2}

## 必須キー

### 記事タイトル

`article_title` キーは、オンライン検索結果やエンドユーザーのブラウザタブのページタイトルの設定に使用される。このキーは`string` 。命名規則については、[Braze Docs Style Guideを]({{site.baseurl}}/contributing/style_guide/)参照のこと。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
article_title: Getting started with Braze Docs
---
```
{% endtab %}
{% endtabs %}

### 説明

`description` キーは、オンライン検索結果でページの説明を設定するために使用される。このキーは、二重引用符で囲まれた150文字以下の`string` 。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
description: "If you're new to Braze Docs, start with this step-by-step tutorial."
---
```
{% endtab %}
{% endtabs %}

### ナビゲーションタイトル

`nav_title` キーは、Braze Docsの左側のナビゲーションバーにページタイトルを設定するために使用する。このキーは、`string` 30文字未満の任意の文字を受け付ける。もし [`hidden`](#hide-page-from-navigation)キーが`true` に設定されている場合、`nav_title` は必要ない。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
nav_title: Getting started
---
```
{% endtab %}
{% endtabs %}

## オプションキー

### エンゲージメント・ツール

`tool` キーは、ページの関連エンゲージメントツールの設定に使われる。このキーは、以下の`string` 、1つ以上の値をリストとして受け付ける。

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

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
tool:
  - currents
  - segments
---
```
{% endtab %}
{% endtabs %}

### ナビゲーションからページを隠す

`hidden` キーは、Braze Docsの左側ナビゲーションからページを隠すために使用する。このキーは、`true` または`false` というブーリアン値を受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
hidden: true
---
```
{% endtab %}
{% endtabs %}

### 検索からページを隠す

`noindex` キーは、内部および外部の検索結果（Braze DocsやGoogle検索など）からページを隠すために使用する。このキーは、`true` または`false` というブーリアン値を受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
noindex: true
---
```
{% endtab %}
{% endtabs %}

### 目次を隠す

`hide_toc` キーは、ページの右側にあるページ内目次（TOC）を隠すために使われる。このキーは、`true` または`false` というブーリアン値を受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
hide_toc: true
---
```
{% endtab %}
{% endtabs %}

### 目次から見出しを隠す

デフォルトでは、目次（TOC）はすべての見出しレベルを表示する。特定の見出しレベルのみを表示するには、`toc_headers` キーで必要なレベルを明示的にリストアップする。リストにない見出しレベルは、TOCから隠される。

このキーは以下の文字列値を受け付ける：

- `h1`
- `h2`
- `h3`
- `h4`

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
toc_headers: h2
---
```
{% endtab %}
{% endtabs %}

### メッセージングチャネル

`channel` 、ページに関連するメッセージングチャネルを設定する。このキーは、以下の`string` 、1つ以上の値をリストとして受け付ける。

- `content cards`
- `email`
- `in-app messages`
- `news feed`
- `push`
- `sms`
- `webhooks`

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
channel:
  - email
  - news feed
---
```
{% endtab %}
{% endtabs %}

### ナビゲーションのみ

`config_only` 、左側のナビゲーション・バーに非表示にすることなく、ページのコンテンツを隠すことができる。このキーは、[ランディングページのないセクションを作る]({{site.baseurl}}/contributing/content_management/sections?tab=without%20landing%20page#step-2-configure-your-section)ときに使う。このキーは、`true` または`false` というブーリアン値を受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
config_only: true
---
```
{% endtab %}
{% endtabs %}

### デフォルトのURLを上書きする

`permalink` 。 [`hidden`](#hide-page-from-navigation)キーを使って、Braze DocsのページのデフォルトURLを上書きする。`permalink` に割り当てられた値は、リダイレクトされる前に`https://www.braze.com/docs` でプリペンドされる。このキーは、以下の条件を満たす`string` 値を受け付ける。

- 文字は小文字
- 単語はアンダースコア (`_`) で区切る。
- "ディレクトリ "はフォワード・スラッシュ(`/`)で区切られる。
- その他の特殊文字はすべて削除される

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
hidden: true
permalink: /support_contact/docs_team/
---
```
{% endtab %}
{% endtabs %}

### ページレイアウト

`layout` キーでページのレイアウトを設定する。`layout` が設定されていない場合は、`default` のレイアウトが使用される。このキーは、以下の`string` 。

- `api_page`
- `dev_guide`
- `featured_video`
- `featured`
- `glossary_page`
- `blank_config`
- `redirect`

各値の詳細については、[ページレイアウトを]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/)参照のこと。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
page_layout: glossary_page
---
```
{% endtab %}
{% endtabs %}

### ページ順

`page_order` キーは、左側のナビゲーションバーで[セクションを順番に並べる]({{site.baseurl}}/contributing/content_management/sections/#ordering-a-section)ときに使う。このキーは、負でない任意の数字（`0` 、`20` 、`5.5` など）を受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
page_order: 35.6
---
```
{% endtab %}
{% endtabs %}

### ページタイプ

`page_type` 、ページの書式設定を行う。このキーは、以下の`string` 。

- `glossary`
- `solution`
- `reference`
- `tutorial`
- `landing`
- `partner`
- `update`

各値の詳細については、[ページの種類を]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/)参照のこと。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
page_type: tutorial
---
```
{% endtab %}
{% endtabs %}

### プラットフォーム

`platform` キーは、ページの関連プラットフォームの設定に使われる。このキーは、1つ以上の[Braze SDKを]({{site.baseurl}}/developer_guide/home/)リスト内の`string` 値として受け付ける。

{% tabs ローカル %}
{% tab 使用例 %}
```markdown
---
platform:
  - iOS
  - Web
  - Android
---
```
{% endtab %}
{% endtabs %}
