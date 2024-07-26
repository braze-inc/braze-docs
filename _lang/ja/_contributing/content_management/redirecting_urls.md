---
nav_title: URLをリダイレクトする
article: Redirecting URLs
description: "Braze Docsのページやページ見出しのURLをリダイレクトする方法を学習する。"
page_order: 5
noindex: true
---

# URLをリダイレクトする

> Braze Docsのページやページ見出しのURLをリダイレクトする方法を学習する。URLに関する一般的な情報は、[コンテンツ管理についてを]({{site.baseurl}}/contributing/content_management/#urls)参照のこと。

ページURLは常にBraze Docsリポジトリのディレクトリ構造と一致する。Markdownファイルがリネームされたり、別のディレクトリに移動された場合、リダイレクトが設定されていないと、元のURLは404エラーになる。

![Braze Docsの404ページの例]({% image_buster /assets/img/contributing/styling_examples/404.png %})

URLリダイレクトを設定することで、ユーザーのブックマークが壊れるのを防ぐことができる。

{% multi_lang_include contributing/prerequisites.md %}

## ページをリダイレクトする

ページのURLをBraze Docsのホームページまたは新しい場所にリダイレクトすることができる。

{% tabs ローカル %}
{% tab ホームページ %}
該当するMarkdownファイルを開封し、以下のキーと値のペアをYAMLのフロント・マターに追加する。すでに`layout` キーがある場合は、既存のキーを新しいキーに置き換える。

```markdown
---
layout: blank_config
---
```

あなたのYAMLフロント・マターは以下のようなものでなければならない：

```markdown
---
nav_title: Customization Guides
config_only: true
layout: blank_config
page_order: 3
---
```
{% endtab %}

{% tab 新天地 %}
関連するMarkdownファイルを移動またはリネームしたら、`assets/js/` ディレクトリに移動し、グローバル・リダイレクト・ファイルを開封する。

```bash
braze-docs
└── assets
    └── js
        └── broken_redirect_list.js
```

ファイルの先頭で、以下の構文を使って新しい行にリダイレクトを作成する：

```javascript
validurls['REDIRECT_FROM'] = 'REDIRECT_TO';
```

次のように置き換えます。

| placeholder     | 説明                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------|
| `REDIRECT_FROM` | URL文字列から`https://www.braze.com/` を削除したリダイレクト_先の_URL。 |
| `REDIRECT_TO`   | URL文字列から`https://www.braze.com/` を削除したリダイレクト_先の_URL。   |
{: .reset-td-br-1 .reset-td-br-2}

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

リダイレクトは以下のようなものであるべきだ：

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports';
```
{% endtab %}
{% endtabs %}

## 見出しをリダイレクトする

ページ内部の見出しのURLをリダイレクトするには、ページのYAMLフロントマターで`local_redirect` キーを使う。最初に、関連するMarkdownファイルを移動するか名前を変更し、ページのYAMLフロントマターで次の構文を使う：

```
local_redirect:
  OLD_HEADING: 'NEW_HEADING_URL'
```

次のように置き換えます。

| placeholder       | 説明                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `OLD_HEADING`     | `#` 、[Markdown構文の](https://www.markdownguide.org/basic-syntax/#an-example-putting-the-parts-together)古い見出しは削除された。 |
| `NEW_HEADING_URL` | URL文字列から`https://www.braze.com/` を削除した、リダイレクト_先の_新しい見出しURL。                                      |
{: .reset-td-br-1 .reset-td-br-2}

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

リダイレクトは以下のようなものであるべきだ：

```yaml
---
nav_title: Getting started
article_title: Getting started with the Braze SDK
description: "If you're new to the Braze SDK, learn how to get started."
local_redirect:
  building-from-source: '/docs/developer_guide/getting_started/#using-our-install-script'
```
