---
nav_title: 画像、写真
article: Managing Images
description: "Braze Docsで画像写真を追加、修正、削除する方法を学習する。"
page_order: 1
noindex: true
---

# 画像、写真をマネージャーする

> Braze Docsで画像写真を追加、修正、削除する方法を学習する。画像, 写真に関する一般的な情報は、[コンテンツ管理についてを]({{site.baseurl}}/contributing/content_management/#images)参照のこと。

{% multi_lang_include contributing/prerequisites.md %}

## 新しい画像、写真を追加する

### ステップ 1:画像ファイルを追加する

テキストエディタで`assets` >`img` を開封する。一般的に、新しい画像はページの他の画像と同じディレクトリに追加する。ただし、最善の判断を下すことはできる。新しい画像写真が[Braze Docsスタイルガイドに従って]({{site.baseurl}}/contributing/style_guide/)いることを確認し、関連するサブディレクトリにPNGファイルを追加する。

```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

次のように置き換えます。

| placeholder | 説明                                                                               |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` | 関連するディレクトリの名前。関連するディレクトリがない場合は、作成してもよい。 |
| `FILE`      | 拡張子を含むファイル名。                                        |
{: .reset-td-br-1 .reset-td-br-2}

画像ファイルは以下のようなものであるべきだ：

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

### ステップ2:画像、写真へのリンク

{% alert important %}
Liquidの{% raw %}`{% tab %}`{% endraw %} タグは参照スタイルのリンクをサポートしていないので、インラインリンクのみを以下にドキュメントする。既存の参照リンクは引き続き機能するが、もはや推奨されない。
{% endalert %}

Markdownファイルで、インライン構文を使って新しい画像写真にリンクする。

{% raw %}
```markdown
![ALT_TEXT.]({% image_buster /assets/img/DIRECTORY/IMAGE.png %})
```
{% endraw %}

次のように置き換えます。

| placeholder | 説明                                                                                                             |
|-------------|-------------------------------------------------------------------------------------------------------------------------|
| `ALT_TEXT`  | 画像, 写真のaltテキスト。これは、Braze Docsをスクリーンリーダーを使っている人たちにも同じようにアクセシブルにするために必要なことである。 |
| `IMAGE`     | `img` ディレクトリを起点とする画像, 写真への相対パス。                                                      |
{: .reset-td-br-1 .reset-td-br-2}

インライン画像は以下のようなものであるべきだ：

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %})
```
{% endraw %}

### ステップ 3:画像, 写真の最大幅を設定する(オプション)

画像リンクに以下のLiquidコードを追加することで、画像の最大幅を設定できる：

{% raw %}
```markdown
{: style="max-width:NUMBER%;"}
```
{% endraw %}

`NUMBER` 、パーセンテージで設定したい最大幅に置き換える。画像, 写真のリンクは以下のようにする：

{% raw %}
```markdown
![The form for creating a new pull request on GitHub.]({% image_buster /assets/img/contributing/getting_started/github_pull_request.png %}){: style="max-width:65%;"}
```
{% endraw %}

## 画像, 写真の更新

### ステップ 1:オリジナルのリファレンスを探す

該当するMarkdownファイルを開封し、古い[インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image)または[参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image)画像リンクを探す。

{% raw %}
```markdown
{% image_buster /assets/img/DIRECTORY/IMAGE.png %}
```
{% endraw %}

### ステップ 2:画像、写真を更新する

既存の画像を更新する場合、新しい画像ファイルを追加するか、既存の画像ファイルを置き換えることができる。新しい画像, 写真が[Braze Docs Style Guideに従って]({{site.baseurl}}/contributing/style_guide/)いることを確認する。

- **既存のファイルを上書きする（推奨）：**オリジナルの画像写真が正確な内容を描写しているが、古いブランディングを描いた画像など、視覚的に古くなっている場合にこの方法を使う。この方法により、Braze Docsリポジトリに保存される画像の総数が減る。
- **新しいファイルを追加する：**この方法は、非推奨の機能やワークフローを描いた画像など、元の画像が完全に古いコンテンツを描いている場合に使用する。

{% tabs ローカル %}
{% tab 既存のファイルを上書きする %}
新しい画像の名前を元の画像の名前と同じにする。次の例では、画像ファイル名が同じであることを確認してほしい。

- **元のファイル名** `getting_started_with_github_select_start3.png`
- **新しいファイル名だ：** `getting_started_with_github_select_start3.png`

次に、新しい画像を元の画像と同じディレクトリに追加する。聞かれたら、画像, 写真を上書きすることを確認する。画像ファイルは以下のようなものであるべきだ：

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── getting_started_with_github_select_start3.png
```
{% endtab %}

{% tab 新しいファイルを追加する%}。
一般的に、新しい画像は、このページの他の画像と同じディレクトリに追加されるべきであるが、あなたの最善の判断で追加してもよい。準備ができたら、`assets/img/` の該当する場所にPNGファイルを追加する。

{% alert warning %}
新しい画像ファイルを追加する際、古い画像ファイルは削除しないこと。
{% endalert %}

```bash
braze-docs
└── assets
    └── img
        └── DIRECTORY
            └── FILE.png
```

次のように置き換えます。

| placeholder | 説明                                                                               |
|-------------|-------------------------------------------------------------------------------------------|
| `DIRECTORY` | 関連するディレクトリの名前。関連するディレクトリがない場合は、作成してもよい。 |
| `FILE`      | 拡張子を含むファイル名。                                        |
{: .reset-td-br-1 .reset-td-br-2}

画像ファイルは以下のようなものであるべきだ：

```bash
braze-docs
└── assets
    └── img
        └── contributing 
            └── github_home_page.png
```

画像, 写真が関連するディレクトリに追加された後、[インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image)または[参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image)構文を使用して、この画像にリンクすることができる。
{% endtab %}
{% endtabs %}

## 画像、写真を削除する

画像を削除するには、該当するMarkdownファイルを開封し、[インライン]({{site.baseurl}}/contributing/content_management/images/?tab=in-line#step-2-link-to-the-image)または[参照スタイルの]({{site.baseurl}}/contributing/content_management/images/?tab=reference-style#step-2-link-to-the-image)画像リンクを削除する。リポジトリから画像ファイルを削除しない。

{% alert warning %}
画像ファイルが削除されると、その画像は他のBraze Docs言語翻訳のために壊れる。
{% endalert %}
