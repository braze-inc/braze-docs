---
nav_title: 初めての貢献
article: Your first contribution
description: "Docs-as-Code や Braze Docs を初めて使用する場合は、このステップバイステップのチュートリアルから始めてください。"
page_order: 1
noindex: true
---

# 初めての寄付

> Docs-as-Code や Braze Docs を初めて使用する場合は、このステップバイステップのチュートリアルから始めてください。経験豊富な寄稿者の場合は、代わりに「[コンテンツ管理]({{site.baseurl}}/contributing/content_management/)」を参照してください。

このチュートリアルを終了すると、次のことができるようになります。

- Braze Docs GitHub リポジトリをナビゲートする
- GitHub Web サイトまたはローカル環境を使用して変更を加える
- プルリクエスト (PR) の作成
- テストサイトでの変更のプレビュー
- Braze Docs チームにレビューをリクエストする

{% multi_lang_include contributing/prerequisites.md %}

## ステップ 1:GitHub リポジトリを調べる

[Braze Docs GitHub リポジトリは](https://github.com/braze-inc/braze-docs) Braze Docs のソースファイルをホストしています。まだすべてを理解していなくても、数分かけてリポジトリを探索してください。時間が経つにつれて、あなたはより親しみやすくなるでしょう。

![The Braze Docs GitHub repository homepage.]({% image_buster /assets/img/contributing/github/home_page.png %})

## ステップ 2:変更を加える

ドキュメントリポジトリに少し慣れてきたので、変更を開始する準備が整いました。まず、[Braze Docsを開いて]({{site.baseurl}})、行いたい簡単な変更を見つけて、どのように変更したいかを決めます。

- **GitHub を使用する (シンプル):**ドキュメントが 1 つしかない小さな変更の場合は、GitHub Web サイトから直接変更できます。
- **ローカル環境の使用 (上級者向け):**複雑な変更や複数の文書の変更を行う場合は、ローカル環境から変更する必要があります。これが推奨方法です。

{% tabs %}
{% tab github %}
[Braze Docs GitHub リポジトリで](https://github.com/braze-inc/braze-docs)、を選択します。`_docs`

![The Braze Docs GitHub repository homepage with the '_docs' folder highlighted in the file tree.]({% image_buster /assets/img/contributing/github/select_docs_directory.png %})

Braze Docsの各ページのURLは、リポジトリのディレクトリ構造を反映しています。ページのURLを使用して、`_docs`ディレクトリ内の対応するMarkdownファイルを見つけてください。たとえば、の Markdown ファイルは `_docs` > `_contributing` > `home.md` にあります。`braze.com/contributing/home`

![The home page for the "Contributing" section on Braze Docs.]({% image_buster /assets/img/contributing/github/example_file_path.png %})

[**このファイルを編集**] を選択し、[Markdownフォーマットを使用して変更を加えます](https://www.markdownguide.org/basic-syntax/)。

![An example page on Braze Docs showing "Edit this file".]({% image_buster /assets/img/contributing/github/edit_from_directory.png %})

終了したら、[**変更をコミット**] を選択します。

![The Braze Docs GitHub repository showing "Commit changes" after editing a file.]({% image_buster /assets/img/contributing/github/commit_changes.png %})

次のウィンドウで、[**変更の提案**] を選択します。

![The "Propose changes" window after selecting "Commit changes" in GitHub.]({% image_buster /assets/img/contributing/github/propose_changes.png %}){: style="max-width:65%;"}
{% endtab %}

{% tab local environment %}
{% alert important %}
続行する前に、[すべての前提条件を満たしていることを確認してください](#prerequisites)。
{% endalert %}

最近のほとんどのテキストエディター ([VS Code](https://code.visualstudio.com/Download) や [Intellij IDEA](https://www.jetbrains.com/idea/download/) など) には、コマンドを実行したりプロジェクトファイルを操作したりするためのアプリ内ターミナルが用意されています。テキストエディターを開き、テキストエディターのアプリ内ターミナルを開きます。

![Intellij IDEA with the in-app terminal open.]({% image_buster /assets/img/contributing/text_editor_with_terminal.png %})

{% alert tip %}
問題が発生した場合は、代わりにスタンドアロン端末を使用できます。
{% endalert %}

ターミナルで、`braze-docs`ディレクトリを開きます。

```bash
cd ~/PATH_TO_REPOSITORY
```

`PATH_TO_REPOSITORY``braze-docs`[環境を設定したときにリポジトリを保存した場所に置き換えてください]({{site.baseurl}}/contributing/home/#step-2-set-up-your-environment)。コマンドは次のようになるはずです。

```bash
cd ~/braze/braze-docs
```

`braze-docs`ディレクトリにいるかどうかを確認し、Git のステータスを確認します。

```bash
pwd
git status
```

{% alert tip %}
`git status` Git ディレクトリの現在の状態を表示します。Git を初めて使用する場合は、すべてのステップの後にこのコマンドを実行して Git ワークフローを視覚化できます。詳細については、を参照してください[`git status`](https://git-scm.com/docs/git-status)。
{% endalert %}

ドキュメントリポジトリでは、`develop`ブランチには最新バージョンの Braze Docs が反映されています。`develop`ブランチをチェックして、最新のアップデートをローカル環境に取り込んでください。

```bash
git checkout develop
git pull
```

ドキュメントに変更を加えるときは、必ず新しいブランチを作成します。`git branch``-b`フラグと一緒に使用して新しいブランチを作成します。

```bash
git checkout -b BRANCH_NAME
```

`BRANCH_NAME`スペースで区切らず、変更内容の短い説明に置き換えてください。コマンドは次のようになるはずです。

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

テキストエディターで、変更する文書を開き、[Markdownフォーマットを使用して変更を行います](https://www.markdownguide.org/basic-syntax/)。

{% multi_lang_include contributing/alerts/tip_locating_a_file.md %}

終了したら、変更を保存し、ターミナルを選択して Git のステータスを確認します。出力は以下のようになります。

\`\`\`bash
$ git status
ブランチでのメタデータのタイプミスの修正について
コミット用にステージングされていない変更:
  (「git add<file>...」を使用してください。「」でコミットされる内容を更新する)
  (「git restore」を使用してください<file>...「」を使用して作業ディレクトリの変更を破棄する)
        変更済み:\_docs/_home/metadata.md

コミットに変更は加えられません (「git add」または「git commit-a」を使用)
\`\`\`

`git add`どの変更をコミット用にステージングするかを Git に伝えるのに使います。次のコマンドは 2 つのオプションを表示します。

- **パイプの左側:**を使用して、`--all`変更したファイルをすべて追加します。
- **パイプの右側:**`PATH_TO_FILE`変更したファイルへの相対パスに置き換えて、個々のファイルを追加します。

```bash
git add {--all|PATH_TO_FILE}
```

`git commit``-m`フラグを付けて使用すると、短い説明 (またはメッセージ) とともにコミットを作成できます。

```bash
git commit -m "COMMIT_MESSAGE"
```

`COMMIT_MESSAGE`変更内容を説明する短い文に置き換えてください。コマンドは次のようになるはずです。

```bash
$ git commit -m "Fixing a typo in the recommended software doc"
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the recommended software doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

最後に、変更を Braze Docs GitHub リポジトリにプッシュしてください。

```bash
git push -u origin BRANCH_NAME
```

`BRANCH_NAME`あなたの支店の名前に置き換えてください。出力は以下のようになります。

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

## ステップ 3:プルリクエスト (PR) を作成する

まだ行っていない場合は、[リポジトリのホームページに戻り](https://github.com/braze-inc/braze-docs)、**Compare & pull request** を選択してください。

![The Braze Docs GitHub repository homepage showing "Open pull request".]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

PRの説明には、次のようなMarkdownのコメントが表示されます。

\`\`\`markdown
<!-- This is a Markdown comment. -->
```

これらのコメントは、PRの説明をガイドしてくれます。完了したら、プルリクエストのドロップダウンを選択し、[**ドラフトプルリクエスト**] を選択します。

![An example pull request showing "Draft pull request".]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

## ステップ 4: 作業内容を確認する

サイトプレビューで作業内容を確認して、コンテンツが [Braze Docs スタイルガイドに従っていることを確認してください]({{sitebase.url}}/contributing/style_guide/)。[さらに変更を加える必要がある場合は、「その他の変更を加える」を参照してください。](#step-6-make-additional-changes-optional)それ以外の場合は、Braze Docs [チームにレビューをリクエストできます](#step-5-request-a-review)。

{% tabs %}
{% tab github %}
PR コメントで、`@braze-inc/docs-team`タグを付けてサイトプレビューをリクエストします。

![An example comment tagging the Braze Docs team to request a site preview.]({% image_buster /assets/img/contributing/github/tag_docs_team_in_comment.png %}){: style="max-width:83%;"}

サイトプレビューを開くには、[**デプロイメントを表示**] を選択します。

![An example pull request showing the "View deployment" button generated by the Vercel bot.]({% image_buster /assets/img/contributing/github/view_deployment.png %})

{% endtab %}

{% tab local environment %}
ターミナルで、「ローカルサーバーを起動する」`rake` コマンドを使用します。

```bash
cd ~/braze-docs
rake
```

出力は以下のようになります。

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

デフォルトでは、[`http://127.0.0.1:4000`](http://127.0.0.1:4000)サイトプレビューはローカルホストで生成されます。サイトプレビューを開くには、Web ブラウザでリンクを開きます。

![An example site preview running in a web browser.]({% image_buster /assets/img/contributing/styling_examples/home.png %})

ローカルサーバーを停止するには、ターミナルを再度開き、<kbd><kbd>Control+C</kbd></kbd> を押します。

{% alert tip %}
詳細な手順については、「[プレビューの生成]({{site.baseurl}}/contributing/generating_a_preview/)」を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

## ステップ 5: レビューをリクエストする

Braze Docs **チームのメンバーに作業内容をレビューしてもらう準備ができたら、[レビュー準備完了**] を選択します。

![An example pull request showing "Ready for review".]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

**レビュアーとタイプ**`braze-inc/docs-team`。チーム名を選択して [<kbd>Esc</kbd>] を押すか、ドロップダウンをクリックして選択を確定します。

![An example pull request with "docs-team" added as the reviewer.]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

ドキュメントチームがレビュー後に追加の変更を要求した場合、[GitHubの通知設定に従って通知されます](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications)。それ以外の場合は、ドキュメントチームが変更を承認してマージします。

承認された寄付金は、次の火曜日または木曜日に配布されます。必ず Braze Docs をチェックして、あなたの頑張りを確認してください。貢献していただきありがとうございます！

## ステップ 6: その他の変更を加える (オプション)

あなたまたは Braze Docs チームのメンバーが作業内容を確認した後、PR に追加の変更を加える必要があるかもしれません。ローカル環境または GitHub を使用して行うことができます。

{% tabs %}
{% tab github %}
PRで、[**変更されたファイル**] を選択し、更新するファイルを見つけて、[<i class="fa-solid fa-ellipsis"></i>**オプションを表示**] > [**ファイルを編集**] を選択します。

![The "Files changed" section in an example pull request showing "Edit file".]({% image_buster /assets/img/contributing/github/edit_from_pr.png %})

終了したら、[**変更をコミット**] を選択します。

![A file from an example pull request showing "Commit changes" after editing.]({% image_buster /assets/img/contributing/github/commit_changes.png %})

[**BRANCH\_NAME ブランチに直接コミット**] > [**変更をコミット**] を選択します。ここで、`BRANCH_NAME`はブランチの名前です。

![The "Commit changes" option after choosing "Commit directly to BRANCH_NAME branch.]({% image_buster /assets/img/contributing/github/confirm_committed_changes.png %}){: style="max-width:65%;"}

終了したら、[レビューをリクエストしてください](#step-5-request-a-review)。
{% endtab %}

{% tab local environment %}
PRで、支店名の横にある [<i class="fa-regular fa-clone"></i>**コピー**] を選択します。

![An example pull request with the "Copy" icon shown next to the branch name.]({% image_buster /assets/img/contributing/github/clone_the_fork.png %})

テキストエディタのターミナルで、ブランチをチェックアウトし、GitHub のリモートブランチから最新の更新を取得します。

```bash
git checkout BRANCH_NAME && git pull
```

`BRANCH_NAME`クリップボードにコピーしたブランチ名に置き換えます。出力は以下のようになります。

```bash
$ git checkout fixing-typo-in-metadata  && git pull
Switched to branch 'fixing-typo-in-metadata'
Your branch is up to date with 'origin/fixing-typo-in-metadata'.
```

テキストエディターで、変更する文書を開き、[手順 2 で行った手順を繰り返します。変更を加えてください](#step-2-make-a-change)。
{% endtab %}
{% endtabs %}
