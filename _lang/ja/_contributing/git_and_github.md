---
nav_title: Git と GitHub
article: Git and GitHub
description: "Braze Docs に貢献できるように、Git と GitHub の使い方を学びましょう。"
page_order: 6
noindex: true
---

# Git と GitHub

> Braze Docs に貢献できるように、Git と GitHub の使い方を学びましょう。

{% alert tip %}
Git やコマンドラインを初めて使用する場合は、代わりにチュートリアルから始めてください。[あなたの最初の貢献]({{site.baseurl}}/contributing/your_first_contribution/)。
{% endalert %}

{% multi_lang_include contributing/prerequisites.md %}

## ブランチの作成

新しい Git ブランチを作成するには、`develop`まずブランチをチェックアウトしてローカル環境を更新します。

```bash
git checkout develop
git pull
```

Git `checkout` のコマンドを使用して新しい Git ブランチを作成します。 

```bash
git checkout -b BRANCH_NAME
```

`BRANCH_NAME`ブランチの変更点をスペースで区切らない短い説明に置き換えてください。出力は次のようになるはずです。

```bash
$ git checkout -b fixing-typo-in-metadata
Switched to a new branch 'fixing-typo-in-metadata'
```

## プルリクエストの作成

プルリクエスト (PR) を作成するには、まずブランチをチェックアウトします。 

```bash
git checkout BRANCH_NAME
```

`BRANCH_NAME`[前に作成したブランチの名前に置き換えてください](#creating-a-branch)。出力は次のようになるはずです。

```bash
$ git checkout fixing-typo-in-metadata
Switched to branch 'fixing-typo-in-metadata'
```

変更を追加し、コミットをステージングします。

```bash
git add --all
git commit -m "COMMIT_MESSAGE"
```

`COMMIT_MESSAGE`変更内容を説明する短い文に置き換えてください。出力は次のようになるはずです。

```bash
$ git commit -m "Fixing a typo in the recommended software doc
[fixing-typo-in-recommended-software 8b05e34] Fixing a typo in the metadata doc.
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

次に、[Braze Docs GitHub リポジトリに移動し](https://github.com/braze-inc/braze-docs)、「**比較とプルリクエスト**」を選択します。

![The Braze Docs GitHub repository showing "Open pull request".]({% image_buster /assets/img/contributing/github/compare_and_pull_request.png %})

PRの説明には、次のようなMarkdownのコメントが表示されます。これらのコメントを PR の記入に役立ててください。

\`\`\`markdown
<!-- This is a Markdown comment. -->
```

完了したら、プルリクエストのドロップダウンを選択し、[**ドラフトプルリクエスト**] を選択します。

![The Braze Docs GitHub repository showing "Draft pull request".]({% image_buster /assets/img/contributing/github/draft_pull_request.png %}){: style="max-width:65%;"}

## レビューをリクエストする

Braze Docs チームのメンバーに PR レビューをリクエストするには、[以前に作成した PR](#creating-a-pull-request) を開いて [**レビューの準備完了**] を選択します。

![An example pull request with the "Ready for review" button highlighted.]({% image_buster /assets/img/contributing/github/ready_for_review.png %}){: style="max-width:75%;"}

**レビュアーとタイプ**`braze-inc/docs-team`。チーム名を選択して [<kbd>Esc</kbd>] を押すか、ドロップダウンをクリックして選択を確定します。

![An example pull request with "docs-team" added as the reviewer.]({% image_buster /assets/img/contributing/github/add_docs_team_as_reviewers.png %}){: style="max-width:55%;"}

Braze Docs チームがレビュー後に追加の変更を要求した場合、[GitHub](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications) の通知設定に従って通知されます。変更が不要な場合は、チームが変更を承認してマージします。

承認された寄付金は、次の火曜日または木曜日に配布されます。必ず Braze Docs をチェックして、頑張ったことを祝いましょう。貢献していただきありがとうございます！
