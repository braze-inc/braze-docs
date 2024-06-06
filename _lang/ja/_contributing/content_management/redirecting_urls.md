---
nav_title: URL のリダイレクト
article: Redirecting URLs
description: "Braze Docsでページとページ見出しのURLをリダイレクトする方法を学びます。"
page_order: 6
noindex: true
---

# URL のリダイレクト

> Braze Docsでページとページ見出しのURLをリダイレクトする方法を学びます。

ページのURLは、Braze Docsリポジトリのディレクトリ構造と常に一致します。Markdown ファイルの名前を変更したり、別のディレクトリに移動したりすると、リダイレクトが設定されていない場合、元の URL で 404 エラーが発生します。

![Example of a 404 page on Braze Docs.]({% image_buster /assets/img/contributing/styling_examples/404.png %})

URL リダイレクトを設定することで、ユーザーのブックマークが壊れるのを防ぐことができます。

{% multi_lang_include contributing/prerequisites.md %}

## ページのリダイレクト

ページのURLをBraze Docsのホームページにリダイレクトするか、新しい場所にリダイレクトするかを選択できます。

{% tabs local %}
{% tab home page %}
関連する Markdown ファイルを開き、次のキーと値のペアを YAML フロントマターに追加します。既に `layout` キーがある場合は、既存のキーを新しいキーに置き換えます。

\`\`\`markdown
---
layout: blank\_config
---
\`\`\`

YAML のフロントマターは、次のようになります。

\`\`\`markdown
---
nav_title: カスタマイズガイド
config_only: true
layout: blank\_config
2.3.
---
\`\`\`
{% endtab %}

{% tab new location %}
関連する Markdown ファイルを移動または名前変更した後、ディレクトリ `assets/js/` に移動し、グローバル リダイレクト ファイルを開きます。

```bash
braze-docs
└── assets
    └── js
        └── broken_redirect_list.js
```

ファイルの で、次の構文を使用して新しい行にリダイレクトを作成します。

```javascript
validurls['REDIRECT_FROM'] = 'REDIRECT_TO';
```

以下を置き換えます。

|プレースホルダー |説明 |
|-----------------|------------------------------------------------------------------------------------------------|
| `REDIRECT_FROM` |リダイレクト _元の_ `https://www.braze.com/` URL を URL 文字列から削除します。 |
|`REDIRECT_TO` |リダイレクト_先_`https://www.braze.com/`の URL を URL 文字列から削除します。  |
{: .reset-td-br-1 .reset-td-br-2}

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

リダイレクトは次のようになります。

```javascript
validurls['/docs/user_guide/data_and_analytics/engagement_reports'] = '/docs/user_guide/data_and_analytics/your_reports/engagement_reports';
```
{% endtab %}
{% endtabs %}

## 見出しのリダイレクト

ページ内見出しのURLをリダイレクトするには、ページのYAMLフロントマター内のキーを使用します `local_redirect` 。まず、関連するMarkdownファイルを移動または名前変更し、ページのYAMLフロントマターで次の構文を使用します。

```
local_redirect:
  OLD_HEADING: 'NEW_HEADING_URL'
```

以下を置き換えます。

|プレースホルダー |説明 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `OLD_HEADING`     | [Markdown構文](https://www.markdownguide.org/basic-syntax/#an-example-putting-the-parts-together) の古い見出しと `#` 削除された。 |
|`NEW_HEADING_URL` |リダイレクト_先_`https://www.braze.com/`の新しい見出し URL が URL 文字列から削除されます。                                     |
{: .reset-td-br-1 .reset-td-br-2}

{% multi_lang_include contributing/alerts/warning_urls_must_be_lowercase.md %}

リダイレクトは次のようになります。

\`\`\`yaml
---
開始
article_title: Braze SDKを使い始める
description: 「Braze SDKを初めて使用する場合は、開始方法を学びます。」
local\_redirect:
  ソースから構築: '/docs/developer_guide/getting_started/#using-our-install-script'
\`\`\`
