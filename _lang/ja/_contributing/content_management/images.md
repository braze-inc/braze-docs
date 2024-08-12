---
nav_title: 画像
article: Images
description: "Braze Docsで画像を追加、変更、削除する方法を学びます。"
page_order: 2
noindex: true
---

# 画像

> Braze Docsで画像を追加、変更、削除する方法を学びます。画像に関する一般的な情報については、「 [コンテンツ管理]({{site.baseurl}}/contributing/content_management/#images)」を参照してください。

{% multi_lang_include contributing/prerequisites.md %}

## 新しい画像を追加する

### ステップ 1:画像ファイルを追加する

テキストエディタで、>`img`を開きます`assets`。通常、新しい画像は、ページ上の他の画像と同じディレクトリに追加する必要があります。ただし、最善の判断を下すことができます。新しい画像が [Braze Docsスタイルガイド]({{site.baseurl}}/contributing/style_guide/)に従っていることを確認し、PNGファイルを関連するサブディレクトリに追加します。

```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

以下を置き換えます。

|プレースホルダー |説明 |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` |関連するディレクトリの名前。関連するディレクトリがない場合は、作成できます。|
| `FILE`      |ファイル拡張子を含むファイルの名前。                                       |
{: .reset-td-br-1 .reset-td-br-2}

画像ファイルは次のようになります。

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

### ステップ 2:画像へのリンク

新しい画像にリンクする場合は、インライン構文または参照スタイルの構文を使用できます。インライン構文は明瞭さを優先し、参照スタイルの構文は読みやすさを優先します。

{% tabs local %}
{% tab in-line %}
Markdown ファイルで、インライン構文を使用して新しい画像にリンクします。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

以下を置き換えます。

|プレースホルダー |説明 |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  |画像の代替テキスト。これは、ブラッドリーダーを使用しているユーザーがBraze Docsに等しくアクセスできるようにするために必要です。|
| `IMAGE`     |ディレクトリから `img` 始まるイメージへの相対パス。                                                     |
{: .reset-td-br-1 .reset-td-br-2}

インライン画像は次のようになります。

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}
{% endtab %}

{% tab reference-style %}
Markdown ファイルで、参照スタイルの構文を使用して新しい画像にリンクします。

{% raw %}
```markdown
![ALT_TEXT.][REFERENCE_NUMBER]
```
{% endraw %}

以下を置き換えます。

|プレースホルダー |説明 |
|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`         |画像の代替テキスト。これは、ブラッドリーダーを使用しているユーザーがBraze Docsに等しくアクセスできるようにするために必要です。|
| `REFERENCE_NUMBER` |このページの別の参照スタイルのリンクにまだ割り当てられていない正の整数を割り当てます。                  |
{: .reset-td-br-1 .reset-td-br-2}

インライン画像は次のようになります。

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.][10]
```
{% endraw %}

ページの下部に、参照を追加します。

{% raw %}
```markdown
[REFERENCE_NUMBER]: {{site.baseurl}}SHORT_URL
```
{% endraw %}

以下を置き換えます。

|プレースホルダー |説明 |
|--------------------|---------------------------------------------------------|
| `REFERENCE_NUMBER` |リンク先の参照の番号。     |
| `IMAGE` |ディレクトリから `img` 始まるイメージへの相対パス。 |
{: .reset-td-br-1 .reset-td-br-2}

リンクは次のようになります。

{% raw %}
```markdown
[10]: {% image_buster /assets/img/contributing/getting_started/github_pull_request.png %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## イメージの更新

### ステップ 1:元の参照を検索する

関連するMarkdownファイルを開き、次のような古い [インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) または [参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) 画像リンクを探します。

{% raw %}
```markdown
{% image_buster /assets/img/DIRECTORY/IMAGE.png %}
```
{% endraw %}

### ステップ 2:イメージを更新する

既存のイメージを更新する場合は、新しいイメージ ファイルを追加するか、既存のイメージ ファイルを置き換えることができます。新しい画像は、 [Braze Docsスタイルガイド]({{site.baseurl}}/contributing/style_guide/)に従っていることを確認してください。

- **既存のファイルを上書きする(推奨):**この方法は、元の画像が正確なコンテンツを表しているが、古いブランドを描写した画像など、視覚的に古くなっている場合に使用します。この方法により、Braze Docsリポジトリに保存される画像の総数が減ります。
- **新しいファイルを追加:**この方法は、廃止された機能やワークフローを描いた画像など、元の画像に完全に古いコンテンツが描かれている場合に使用します。

{% tabs local %}
{% tab overwrite existing file %}
元の画像の名前と一致するように新しい画像の名前を変更します。次の例では、イメージ ファイル名がどのように同一であるかを確認します。

- **元のファイル name:** `getting_started_with_github_select_start3.png`
- **新規ファイル name:** `getting_started_with_github_select_start3.png`

次に、元のイメージと同じディレクトリに新しいイメージを追加します。確認を求められたら、画像を上書きすることを確認します。画像ファイルは次のようになります。

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── getting_started_with_github_select_start3.png
```
{% endtab %}

{% tab add new file%}
通常、新しい画像はこのページの他の画像と同じディレクトリに追加する必要がありますが、最善の判断を下すことができます。準備ができたら、PNG ファイルを の `assets/img/`適切な場所に追加します。

{% alert warning %}
新しい画像ファイルを追加するときに、古い画像ファイルを削除しないでください。
{% endalert %}

```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

以下を置き換えます。

|プレースホルダー |説明 |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` |関連するディレクトリの名前。関連するディレクトリがない場合は、作成できます。|
| `FILE`      |ファイル拡張子を含むファイルの名前。                                       |
{: .reset-td-br-1 .reset-td-br-2}

画像ファイルは次のようになります。

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

イメージが関連するディレクトリに追加されたら、 [インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) または [参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) 構文を使用してこのイメージにリンクできます。
{% endtab %}
{% endtabs %}

## イメージの削除

画像を削除するには、関連する Markdown ファイルを開き、 [インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image) または [参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image) 画像リンクを削除します。リポジトリからイメージ ファイルを削除しないでください。

{% alert warning %}
画像ファイルを削除すると、その画像は他のBraze Docs言語の翻訳では壊れます。
{% endalert %}
