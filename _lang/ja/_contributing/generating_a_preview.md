---
nav_title: プレビューの生成
article: Generating a preview
description: "ローカルサイトプレビューを生成する方法を学習します。これにより、Braze Docs で作業がどのように見えるかを確認できます。"
page_order: 5 
noindex: true
---

# プレビューの生成

> ローカルサイトプレビューを生成する方法を学習します。これにより、Braze Docs で作業がどのように見えるかを確認できます。

{% multi_lang_include contributing/prerequisites.md %}

## プレビューの生成

### ステップ 1:ブランチのチェックアウト

端末で、サイトプレビューに使用するブランチをチェックアウトします。

```bash
git checkout BRANCH_NAME
```

`BRANCH_NAME` を、あるブランチまたは別の人のブランチの名前に置き換えます。コマンドは次のようになります。

```bash
git checkout BD-2346-fixing-typo-swift
```

### ステップ 2:ローカルサーバーを起動する

ローカルサーバを起動すると、[現在のブランチ](#step-1-checkout-a-branch) 内のファイルが、Braze Docs のローカルプレビューを構築するために使用されます。現在のブランチを使用してローカルサーバを起動するには、`braze-docs` ディレクトリで次のコマンドを実行します。

```bash
rake
```

出力は次のようになります。

```bash
== Sinatra (v3.0.4) has taken the stage on 4000 for development with backup from Puma
Puma starting in single mode...
* Puma version: 6.3.1 (ruby 3.2.2-p225) ("Mugi No Toki Itaru")
*  Min threads: 8
*  Max threads: 32
*  Environment: development
*          PID: 16158
* Listening on http://127.0.0.1:4000
...
```

### ステップ 3:サイトプレビューを開く

デフォルトでは、サイトプレビューはlocalhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000) に生成されます。サイトプレビューを開くには、Web ブラウザでリンクを開きます。

![An example site preview running in a web browser.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

### ステップ 4: ローカルサーバーを停止する

ローカルサーバーを停止するには、ターミナルを再度開き、<kbd>Control</kbd> + <kbd>C</kbd> を押します。

## プレビューの更新

ほとんどの場合、`braze-docs` のファイルを変更すると、サイトプレビューが自動的に更新されます。この場合、ターミナルは次のようなメッセージを出力します。

```bash
Asset Pipeline: Processing 'javascript_asset_tag' manifest 'global'
Asset Pipeline: Saved 'global-128fd02b54e35ea79fcb21ea460fac06.js' to '/Users/alex-lee/braze-docs/_site/assets'
                    ...done in 1.940883 seconds.
```

ブラウザでこれらの更新を表示するには、ページを更新します。

{% alert tip %}
ブラウザでページを更新するには、macOS で<kbd>Command</kbd> + <kbd>R</kbd> を押すか、Windows で<kbd>Control</kbd> + <kbd>R</kbd> を押します。
{% endalert %}

ただし、次の場合など、サイトプレビューが**not** を自動的に更新する場合があります。

- ファイル名またはディレクトリ名が変更された場合
- 新しいファイルまたはディレクトリが追加された
- `_includes` ディレクトリ内のファイルの内容が編集されます 

これらの更新を確認するには、[ローカルサーバーを停止し、[再起動する必要があります](#step-2-start-a-local-server)。
