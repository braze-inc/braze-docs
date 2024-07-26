---
nav_title: ページ
article: Managing Pages
description: "Braze Docsでページを作成、変更、削除する方法を学習する。"
page_order: 0
noindex: true
---

# ページのマネージャー

> Braze Docsでページを作成、変更、削除する方法を学習する。代わりにセクションを作成したり並べ替えたりするには、[セクションを]({{site.baseurl}}/contributing/content_management/sections/)参照のこと。ページに関する一般的な情報は、[コンテンツ・マネージャーについてを]({{site.baseurl}}/contributing/content_management/#pages)参照のこと。

{% multi_lang_include contributing/prerequisites.md %}

## ページを作成する

### ステップ 1:新しいファイルを作成する

該当するディレクトリを開封し、ページ用の新しいMarkdownファイルを作成する。

```bash
PAGE_TITLE.md
```

`PAGE_TITLE` 、[Braze Docs Style Guideに]({{site.baseurl}}/contributing/style_guide/)従ったページタイトルに置き換える。すべて小文字を使用し、特殊文字を削除し、スペースをアンダースコア (`_`) に置き換える。ファイル名は以下のようなものであるべきだ：

- **ページのタイトル**C++の開発環境を設定する
- **ファイル名：** `setting_up_your_development_environment_for_cpp.md`

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

### ステップ2:テンプレートを追加する

以下のテンプレートのいずれかをコピーし、Markdownファイルに貼り付ける。詳しくは[テンプレートを]({{site.baseurl}}/contributing/templates/)参照のこと。

#### 基本テンプレート

{% multi_lang_include contributing/templates/basic.md %}

#### テクノロジーパートナーテンプレート

{% multi_lang_include contributing/templates/technology_partner.md %}

## コンテンツを書く

このセクションで取り上げるBraze特有の構文以外は、すべてのコンテンツは[標準的なMarkdown構文を使って](https://www.markdownguide.org/basic-syntax/)記述する。

### 相互参照

Braze Docsの外でホストされているページを参照するには、標準的なMarkdown構文を使う。

{% raw %}
```markdown
[LINK_TEXT](FULL_URL)
```
{% endraw %}

Braze Docsでホストされているページを相互参照するには、以下のBraze固有の構文を使用する。

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

{% alert note %}
完全なウォークスルーは、[相互参照を]({{site.baseurl}}/contributing/content_management/cross_referencing/)参照のこと。
{% endalert %}

### 画像、写真を追加する

画像を追加するには、画像のPNGファイルを`assets/img` 内の関連する場所に置き、次の構文を使う。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

{% alert note %}
詳しい説明は、[新しい画像を]({{site.baseurl}}/contributing/content_management/images/)追加するを参照のこと。
{% endalert %}
