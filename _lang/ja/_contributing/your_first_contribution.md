---
nav_title: 初めての寄付
article: Your first contribution
description: "docs-as-codeやBraze Docsを初めて使う人は、このステップバイステップのチュートリアルから始めよう。"
page_order: 1
noindex: true
---

# 最初の寄付

> docs-as-codeやBraze Docsを初めて使う人は、このステップバイステップのチュートリアルから始めよう。経験豊富な投稿者であれば、代わりに[コンテンツマネージャーについてを]({{site.baseurl}}/contributing/content_management/)参照してほしい。

このチュートリアルを終えると、次のことができるようになる：

- Braze DocsのGitHubリポジトリに移動する
- GitHubのWebサイトやローカルの環境を使って変更を加える
- プルリクエスト（PR）を作成する
- テストサイトで変更をプレビューする
- Braze Docsチームにレビューを依頼する

{% multi_lang_include contributing/prerequisites.md %}

## ステップ 1:GitHubリポジトリを探索する

[Braze DocsのGitHubリポジトリは](https://github.com/braze-inc/braze-docs)、Braze Docsのソースファイルをホストしている。まだすべてを理解していなくても、数分かけてリポジトリを探索してほしい。時間が経てば、もっと慣れるだろう。

![Braze Docs GitHub リポジトリのホームページ]({% image_buster /assets/img/contributing/github/home_page.png %})

## ステップ2:変化を起こす

docsリポジトリに少し慣れたところで、変更を始める準備ができた。まず、[Braze Docsを]({{site.baseurl}})開封し、簡単な変更を見つけ、どのように変更するかを決める：

- **GitHubを使う（シンプル）：**小規模の単一ドキュメントの変更であれば、GitHubのWebサイトから直接変更できる。
- **ローカル環境を使用する（詳細）：**複雑なドキュメントや複数のドキュメントを変更する場合は、ローカル環境から変更する必要がある。これが推奨される方法だ。

{% tabs %}
{% tab github %}
[Braze Docs GitHubリポジトリで](https://github.com/braze-inc/braze-docs)、`_docs` を選択する。

![Braze DocsのGitHubリポジトリのホームページで、ファイルツリーで'_docs'フォルダがハイライトされている。]({% image_buster /assets/img/contributing/github/select_docs_directory.png %})

Braze Docsの各ページのURLは、リポジトリのディレクトリ構造を反映している。ページのURLを使って、`_docs` ディレクトリにある対応するMarkdownファイルを探す。例えば、`braze.com/contributing/home` のMarkdownファイルは`_docs` >`_contributing` >`home.md` にある。

![Braze Docsの "Contributing "セクションのホームページ。]({% image_buster /assets/img/contributing/github/example_file_path.png %})

**このファイルを編集する**」を選択し、[Markdownフォーマットを使って](https://www.markdownguide.org/basic-syntax/)変更を加える。

![Braze Docsにある「このファイルを編集する」ページの例。]({% image_buster /assets/img/contributing/github/edit_from_directory.png %})

終了したら、**Commit changesを**選択する。

![Braze DocsのGitHubリポジトリで、ファイル編集後に「Commit changes」を表示する。]({% image_buster /assets/img/contributing/github/commit_changes.png %})

次のウィンドウで、「**変更を提案する**」を選択する。

![GitHubで「変更をコミット」を選択した後の「変更提案」ウィンドウ]({% image_buster /assets/img/contributing/github/propose_changes.png %}){: style="max-width:65%;"}
{% endtab %}

{% tab 地域環境 %}
{% alert important %}
続行する前に、すべての[前提](#prerequisites)条件が完了していることを確認する。
{% endalert %}

最近のテキストエディタ（[VS Codeや](https://code.visualstudio.com/Download) [Intellij IDEAなど](https://www.jetbrains.com/idea/download/)）のほとんどは、コマンドを実行したりプロジェクトファイルを操作したりするためのアプリ内ターミナルを提供している。テキストエディタを開封し、テキストエディタのアプリ内ターミナルを開く。

![アプリ内ターミナルを開封したIntellij IDEA]({% image_buster /assets/img/contributing/text_editor_with_terminal.png %})

{% alert tip %}
もし問題があれば、代わりにスタンドアロン・ターミナルを使うこともできる。
{% endalert %}

ターミナルで、`braze-docs` ディレクトリを開封する。

```bash
cd ~/PATH_TO_REPOSITORY
```

`PATH_TO_REPOSITORY` を、[環境]({{site.baseurl}}/contributing/home/#step-2-set-up-your-environment)設定時に`braze-docs` リポジトリを保存した場所に置き換える。コマンドは以下のようなものだ：

```bash
cd ~/braze/braze-docs
```

`braze-docs` 、Gitステータスをチェックする。

```bash
pwd
git status
```

{% alert tip %}
`git status` はGitディレクトリの現在のステータスを表示する。Gitを使い始めたばかりの人は、ステップごとにこのコマンドを実行すると、Gitのワークフローを視覚化しやすくなる。詳細については、[`git status`](https://git-scm.com/docs/git-status) を参照してください。
{% endalert %}

docsリポジトリでは、`develop` ブランチがBraze Docsの最新バージョンを反映している。`develop` Branchをチェックして、最新の更新をあなたの内部環境に取り込もう。

```bash
git checkout develop
git pull
```

ドキュメントに変更を加える場合は、常に新しいブランチを作成する。新しいブランチを作成するには、`git branch` と`-b` フラグを使用する。

```bash
git checkout -b BRANCH_NAME
```

`BRANCH_NAME` 、変更点をスペースで区切らない短い説明に置き換える。コマンドは以下のようなものだ：

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

テキストエディタで、変更したいドキュメントを開封し、[Markdownフォーマットを使って](https://www.markdownguide.org/basic-syntax/)変更を加える。

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

終了したら、変更を保存し、ターミナルを選択してGitのステータスをチェックする。出力は以下のようになる：

```bash
$ git status
On branch fixing-typo-in-metadata
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   _docs/_home/metadata.md

no changes added to commit (use "git add" and/or "git commit -a")
```

`git add` を使って、どの変更をコミットのステージに入れたいかをGitに伝える。次のコマンドは2つのオプションを示す：

- **パイプの左側：**`--all` を使って変更したファイルをすべて追加する。
- **パイプの右側：**`PATH_TO_FILE` を変更したファイルへの相対パスに置き換えて、個々のファイルを追加する。

```bash
git add {--all|PATH_TO_FILE}
```

短い説明（またはメッセージ）とともにコミットを作成するには、`git commit` に`-m` フラグを付ける。

```bash
git commit -m "COMMIT_MESSAGE"
```

`COMMIT_MESSAGE` を、変更点を説明する短い文章に置き換える。コマンドは以下のようなものだ：

```bash
$ git commit -m "Fixing a typo in the recommended software doc"
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the recommended software doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

最後に、変更をBraze DocsのGitHubリポジトリにプッシュする。

```bash
git push -u origin BRANCH_NAME
```

`BRANCH_NAME` 、あなたのBranchの名前に置き換える。出力は以下のようになる：

```bash
$ git push -u origin fixing-typo-in-recommended-software
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```
{% endtab %}
{% endtabs %}

## ステップ 3:プルリクエスト（PR）を作成する

まだそこにいない場合は、[リポジトリのホームページに](https://github.com/braze-inc/braze-docs)戻り、**比較＆プルリクエストを**選択する。

![Braze Docs GitHub リポジトリのトップページに "Open pull request "と表示されている。]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

PRの説明の中に、以下のようなMarkdownのコメントがある：

```markdown
<!-- This is a Markdown comment. -->
```

これらのコメントは、あなたのPR記述の指針となるだろう。完了したら、プルリクエストのドロップダウンを選択し、**プルリクエストの下書きを**選択する。

![]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}) "Draft pull request "を示すプルリクエストの例。{: style="max-width:65%;"}

## ステップ 4:自分の仕事を見直す

[Braze Docsスタイルガイドに従って]({{sitebase.url}}/contributing/style_guide/)コンテンツを作成し、サイトプレビューで作品を確認する。追加の変更が必要な場合は、[追加の変更を行う](#step-6-make-additional-changes-optional)を参照のこと。それ以外の場合は、Braze Docsチームに[レビューを依頼](#step-5-request-a-review)することができる。

{% tabs %}
{% tab github %}
PRコメントで、`@braze-inc/docs-team` タグを付けて、サイトプレビューをリクエストする。

![サイトプレビューを依頼するためにBraze Docsチームにタグ付けしたコメントの例。]({% image_buster /assets/img/contributing/github/tag_docs_team_in_comment.png %}){: style="max-width:83%;"}

サイトプレビューを開封するには、**配置を表示するを**選択する。

![Vercel botによって生成された "View deployment "ボタンを示すプルリクエストの例。]({% image_buster /assets/img/contributing/github/view_deployment.png %})

{% endtab %}

{% tab 地域環境 %}
ターミナルで、`rake` コマンドを使ってローカル・サーバーを起動する。

```bash
cd ~/braze-docs
rake
```

出力は以下のようになる：

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

デフォルトでは、サイトのプレビューはlocalhost上に生成される。 [`http://127.0.0.1:4000`](http://127.0.0.1:4000).サイトのプレビューを開封するには、Webブラウザでリンクを開く。

![ウェブブラウザで動作するサイトプレビューの例。]({% image_buster /assets/img/contributing/styling_examples/home.png %})

ローカルサーバーを停止するには、ターミナルを再び開き、<kbd>コントロール</kbd>＋<kbd>C</kbd>キーを押す。

{% alert tip %}
完全なチュートリアルについては、[プレビューを生成するを]({{site.baseurl}}/contributing/generating_a_preview/)参照のこと。
{% endalert %}
{% endtab %}
{% endtabs %}

## ステップ 5レビューを依頼する

Braze Docsチームのメンバーがあなたの作品をレビューする準備ができたら、**Ready for reviewを**選択する。

![]({% image_buster /assets/img/contributing/github/ready_for_review.png %}) "Ready for review "を示すプルリクエストの例。{: style="max-width:75%;"}

**レビュアーの**フィールドに、`braze-inc/docs-team` と入力する。チーム名を選択し、<kbd>Esc</kbd>キーを押すか、ドロップダウンの外をクリックして選択を確定する。

![レビュアーに "docs-team "を加えたプルリクエストの例。]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

docsチームがレビュー後に追加の変更を要求した場合は、[GitHubの通知設定に従って](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications)通知される。そうでなければ、docsチームがあなたの変更を承認し、マージする。

承認された献金は、翌週の火曜日か木曜日に配備される。ぜひBraze Docsをチェックして、あなたの頑張りを見てほしい。貢献してくれてありがとう！

## ステップ 6: 追加の変更を加える（オプション）

あなたまたはBraze Docsチームのメンバーがあなたの作品を確認した後、PRに追加の変更を加える必要があるかもしれない。ローカル環境かGitHubを使って行うことができる。

{% tabs %}
{% tab github %}
PRで、**Files changedを**選択し、更新したいファイルを探し、<i class="fa-solid fa-ellipsis"></i> **Show options**>**Edit fileを**選択する。

![プルリクエスト例の「変更されたファイル」セクションに「ファイルの編集」が表示されている。]({% image_buster /assets/img/contributing/github/edit_from_pr.png %})

終了したら、**Commit changesを**選択する。

![]({% image_buster /assets/img/contributing/github/commit_changes.png %}) 編集後の「変更をコミット」を示すプルリクエスト例のファイル。

**BRANCH_NAME ブランチに直接コミット**>**変更をコミット** を選択する。ここで、`BRANCH_NAME` はブランチの名前である。

![BRANCH_NAME ブランチに直接コミット」を選択した後に、「変更をコミット」オプションを選択する]({% image_buster /assets/img/contributing/github/confirm_committed_changes.png %}){: style="max-width:65%;"}

終わったら、[レビューをリクエスト](#step-5-request-a-review)する。
{% endtab %}

{% tab 地域環境 %}
PRの中で、Branch名の横にある<i class="fa-regular fa-clone"></i> **Copyを**選択する。

![ブランチ名の横に「コピー」アイコンが表示されているプルリクエストの例。]({% image_buster /assets/img/contributing/github/clone_the_fork.png %})

テキストエディタのターミナルで、自分のBranchをチェックアウトし、GitHubのリモートブランチから最新の更新をプルする。

```bash
git checkout BRANCH_NAME && git pull
```

`BRANCH_NAME` をクリップボードにコピーした Branch 名に置き換える。出力は以下のようになる：

```bash
$ git checkout fixing-typo-in-metadata  && git pull
Switched to branch 'fixing-typo-in-metadata'
Your branch is up to date with 'origin/fixing-typo-in-metadata'.
```

テキストエディタで、変更したいドキュメントを開封し、[ステップ2で完了したステップを繰り返す：変更を加える](#step-2-make-a-change).
{% endtab %}
{% endtabs %}
