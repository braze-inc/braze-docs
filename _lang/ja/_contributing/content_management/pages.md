---
nav_title: ページ
article: Pages
description: "Braze Docs でページを作成、変更、削除する方法をご覧ください。"
page_order: 0
noindex: true
---

# ページ

> Braze Docs でページを作成、変更、削除する方法をご覧ください。代わりにセクションを作成または並べ替えるには、「[セクション]({{site.baseurl}}/contributing/content_management/sections/)」を参照してください。ページに関する一般的な情報については、「[コンテンツ管理]({{site.baseurl}}/contributing/content_management/#pages)」を参照してください。

{% multi_lang_include contributing/prerequisites.md %}

## ページの作成

### ステップ 1:新しいファイルを作成

該当するディレクトリを開き、ページ用の新しい Markdown ファイルを作成します。

```bash
PAGE_TITLE.md
```

[Braze Docs `PAGE_TITLE` スタイルガイドに従ったページのタイトルに置き換えてください]({{site.baseurl}}/contributing/style_guide/)。すべて小文字を使用し、特殊文字を削除し、スペースをアンダースコア () に置き換えます。`_`ファイル名は次のようになっているはずです。

- **ページ:**C++ title: 用の開発環境のセットアップ
- **[ファイル] name:** `setting_up_your_development_environment_for_cpp.md`

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

### ステップ 2:テンプレートを追加

以下のテンプレートのいずれかをコピーして Markdown ファイルに貼り付けます。詳細については、「[テンプレート]({{site.baseurl}}/contributing/templates/)」を参照してください。

#### 基本テンプレート

{% multi_lang_include contributing/templates/basic.md %}

#### テクノロジーパートナーテンプレート

{% multi_lang_include contributing/templates/technology_partner.md %}

## コンテンツを書く

このセクションで説明するBraze固有の構文を除き、[すべてのコンテンツは標準のMarkdown構文を使用して記述してください](https://www.markdownguide.org/basic-syntax/)。

### クロスリファレンス

Braze Docs 以外でホストされているページを参照するには、標準の Markdown 構文を使用してください。

{% raw %}
```markdown
[LINK_TEXT](FULL_URL)
```
{% endraw %}

Braze Docs でホストされているページを相互参照するには、以下の Braze 固有の構文を使用してください。

{% raw %}
```markdown
[LINK_TEXT]({{site.baseurl}}/SHORT_URL)
```
{% endraw %}

{% alert note %}
[詳細な手順については、「クロスリファレンス」を参照してください。]({{site.baseurl}}/contributing/content_management/cross_referencing/)
{% endalert %}

### 画像を追加する

画像を追加するには、画像の PNG ファイルを内の該当する場所に配置し`assets/img`、次の構文を使用します。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

{% alert note %}
詳細な手順については、「[新しい画像の追加]({{site.baseurl}}/contributing/content_management/images/)」を参照してください。
{% endalert %}
