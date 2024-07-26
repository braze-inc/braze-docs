---
nav_title: プレビューの生成
article: Generating a preview
description: "ローカルサイトのプレビューを生成する方法を学び、Braze Docsでの作業の見え方を確認しましょう。"
page_order: 5 
noindex: true
---

# プレビューを生成中

> ローカルサイトのプレビューを生成する方法を学び、Braze Docsでの作業の見え方を確認しましょう。

{% multi_lang_include contributing/prerequisites.md %}

## プレビューの生成

### ステップ 1:ブランチをチェックアウトする

ターミナルで、サイトプレビューに使用するブランチをチェックアウトします。

```bash
git checkout BRANCH_NAME
```

`BRANCH_NAME`をあなたのBranchまたは他の人のBranchの名前に置き換えてください。あなたのコマンドは次のようになります:

```bash
git checkout BD-2346-fixing-typo-swift
```

### ステップ2:ローカルサーバーを開始する

ローカルサーバーを開始すると、[現在のBranch](#step-1-checkout-a-branch)のファイルが使用され、Braze Docsのローカルプレビューが作成されます。現在のBranchを使用してローカルサーバーを開始するには、`braze-docs`ディレクトリで次のコマンドを実行します。

```bash
rake
```

出力は次のようになります:

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

### ステップ 3:開封 your site プレビュー

デフォルトでは、サイトのプレビューはlocalhost [`http://127.0.0.1:4000`](http://127.0.0.1:4000)で生成されます。サイトのプレビューを開封するには、リンクをWebブラウザーで開封してください。

![Webブラウザで実行されている例サイトのプレビュー]({% image_buster /assets/img/contributing/styling_examples/home.png %})

### ステップ 4:ローカルサーバーを停止する

ローカルサーバーを停止するには、ターミナルを再度開き、<kbd>コントロール</kbd> + <kbd>C</kbd>を押します。

## プレビューの更新

ほとんどの場合、`braze-docs`のファイルに変更を加えると、サイトのプレビューが自動的に更新されます。このような場合、ターミナルは次のようなメッセージを出力します:

```bash
Asset Pipeline: Processing 'javascript_asset_tag' manifest 'global'
Asset Pipeline: Saved 'global-128fd02b54e35ea79fcb21ea460fac06.js' to '/Users/alex-lee/braze-docs/_site/assets'
                    ...done in 1.940883 seconds.
```

ブラウザでこれらの更新を表示するには、ページを更新してください。

{% alert tip %}
ブラウザでページを更新するには、macOSでは<kbd>Command</kbd> + <kbd>R</kbd>、Windowsでは<kbd>コントロール</kbd> + <kbd>R</kbd>を押します。
{% endalert %}

しかし、サイトのプレビューが自動的に更新され**ない**場合があります。例えば、次のような場合です。

- ファイルまたはディレクトリ名が変更されました
- 新しいファイルまたはディレクトリが追加されました
- ファイルの内容は`_includes`ディレクトリで編集されます 

これらの更新を確認するには、[ローカルサーバーを停止して](#step-4-stop-your-local-server)、[再起動する必要があります](#step-2-start-a-local-server)。
