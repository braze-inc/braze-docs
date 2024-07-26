---
nav_title: GitとGitHub
article: Git and GitHub
description: "GitとGitHubの使い方を学び、Braze Docsに貢献できるようにしましょう。"
page_order: 6
noindex: true
---

# GitとGitHub

> GitとGitHubの使い方を学び、Braze Docsに貢献できるようにしましょう。

{% alert tip %}
Gitやコマンドラインに不慣れな場合は、代わりにチュートリアルから始めてください:[あなたの最初の貢献]({{site.baseurl}}/contributing/your_first_contribution/)。
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## ブランチを作成する

新しいGitブランチを作成するには、まず`develop`ブランチをチェックアウトしてローカル環境を更新します。

```bash
git checkout develop
git pull
```

Git の `checkout` コマンドを使用して新しい Git Branch を作成します。 

```bash
git checkout -b BRANCH_NAME
```

`BRANCH_NAME` を短く、スペースを含まない説明に置き換えてください。出力は次のようになります:

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

## プルリクエストの作成

プルリクエスト（PR）を作成するには、まずブランチをチェックアウトします。 

```bash
git checkout BRANCH_NAME
```

`BRANCH_NAME` を以前に作成した [Branch](#creating-a-branch) の名前に置き換えます。出力は次のようになります:

```bash
$ git checkout fixing-typo-in-metadata
Switched to branch 'fixing-typo-in-metadata'
```

変更を追加してコミットをステージします。

```bash
git add --all
git commit -m "COMMIT_MESSAGE"
```

変更内容を説明する短い文に`COMMIT_MESSAGE`を置き換えます。出力は次のようになります:

```bash
$ git commit -m "Fixing a typo in the recommended software doc
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
 1 file changed, 1 insertion(+), 1 deletion(-)
```

最後に、変更をBraze Docs GitHubリポジトリにプッシュします。

```bash
git push -u origin BRANCH_NAME
```

`BRANCH_NAME`をあなたのBranchの名前に置き換えてください。出力は次のようになります：

```bash
$ git push -u origin fixing-typo-in-recommended-software
Enumerating objects: 14, done.
...
To github.com:braze-inc/braze-docs.git
 * [new branch]      fixing-typo-in-recommended-software -> fixing-typo-in-recommended-software
branch 'fixing-typo-in-recommended-software' set up to track 'origin/fixing-typo-in-recommended-software'.
```

次に、[Braze Docs GitHubリポジトリ](https://github.com/braze-inc/braze-docs)に移動し、**Compare & pull request**を選択します。

![Braze Docs GitHubリポジトリに「開封プルリクエスト」が表示されています。]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

PRの説明には、次のようなMarkdownコメントが表示されます。これらのコメントを使用して、PRを記入してください。

```markdown
<!-- This is a Markdown comment. -->
```

完了したら、プルリクエストのドロップダウンを選択し、次に**下書きプルリクエスト**を選択します。

![Braze Docs GitHubリポジトリに「下書きプルリクエスト」が表示されています。]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

## レビューを依頼

Braze Docs チームのメンバーに PR レビューを依頼するには、[以前に作成した PR を開封](#creating-a-pull-request)し、**レビューの準備ができました**を選択します。

![「レビューの準備ができました」ボタンが強調表示されたプルリクエストの例です。]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

**レビュアー**とタイプ`braze-inc/docs-team`。チーム名を選択し、<kbd>Esc</kbd>を押すか、ドロップダウンの外をクリックして選択を確定します。

![「docs-team」がレビュアーとして追加されたプルリクエストの例です。]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

Braze Docsチームがレビュー後に追加の変更を要求した場合、[GitHub通知設定](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications)に従って通知されます。変更が必要ない場合、チームはあなたの変更を承認してマージします。

承認された貢献は、次の火曜日または木曜日に展開されます。必ずBrazeドキュメントをチェックして、あなたの努力を祝ってください。貢献してくれてありがとう！
