---
nav_title: ホーム
article: Contributing to Braze Docs
description: "Braze Docsへの貢献を開始するために必要なものは以下の通りです！"
page_order: 0
search_tag: Contributing
---

# Braze Docsへの貢献

> Braze Docsへの貢献に感謝します！毎週火曜日と木曜日に、コミュニティからの投稿をマージし、Braze Docsにデプロイします。このガイドを使用して、次回のデプロイ時に変更をマージしてください。

## 前提条件

Braze Docsに貢献するためには、Gitをある程度理解していることが必要です。Gitを使うのが初めてで何から始めたらいいのかわからない場合は、[Git Bookをご覧ください：開始復習が必要な場合は、[GitとGitHubを]({{site.baseurl}}/contributing/git_and_github/)参照してください。

## ステップ 1:CLAに署名する

Braze Docsに貢献するすべての人は、[貢献ライセンス契約（CLA](https://www.braze.com/docs/cla)）に署名しなければなりません。CLAに署名しないと、GitHubの`@cla-bot` 、自動的にプルリクエストがブロックされます。

## ステップ 2:環境を整える

Braze Docsに複雑な変更や複数ページの変更を加える前に、ローカル環境をセットアップする必要があります。しかし、小さな単一ドキュメントの変更は、[GitHubで直接]({{site.baseurl}}/contributing/your_first_contribution/?tab=github#step-2-make-a-change)行うことができます。

### ステップ 2.1:必要なソフトウェアを入手する

最低限、ターミナル、テキストエディタ、ルビー・バージョン・マネージャが必要だ。何から始めたらいいかわからない場合は、以下を参照。

<style>
table td {
    word-break: break-word;
}
</style>
<table>
<thead>
    <tr>
        <th>タイプ</th>
        <th>製品</th>
        <th>説明</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Git GUI</td>
        <td><a href="https://desktop.github.com/">GitHubデスクトップ</a></td>
        <td>ターミナルでコマンドを入力する代わりに、Gitコマンドを実行するためのグラフィカル・ユーザー・インターフェース（GUI）。</td>
    </tr>    
    <tr>
        <td>ターミナル</td>
        <td><a href="https://wezfurlong.org/wezterm/index.html">ウェズターム</a></td>
        <td>コマンドラインからコマンドを実行し、Braze Docsリポジトリとやり取りできるターミナルエミュレータです。Windowsオペレーティング・システムを使用している場合は、Windows Subsystem for Linux（WSL）もインストールする必要があります。</td>
    </tr>
    <tr>
        <td>ターミナル延長</td>
        <td><a href="https://learn.microsoft.com/en-us/windows/wsl/install">Linux用Windowsサブシステム（WSL）*。</a></td>
        <td>WSLを使えば、Linuxサブシステムをインストールし、Windowsオペレーティング・システム上でUnixライクなコマンドを実行できる。Windowsオペレーティング・システムから投稿する場合は、WSLをインストールすることをお勧めします。<br><br><em>* Windows版のみ。</em></td>
    </tr>
    <tr>
        <td>パッケージマネージャー</td>
        <td><a href="https://brew.sh/">ホームブリュー</a></td>
        <td>Braze Docsへの投稿に使用するさまざまなコマンドラインインターフェイス（CLI）ツールをインストールして管理できるパッケージマネージャーです。</td>
    </tr>
    <tr>
        <td>Rubyバージョンマネージャ</td>
        <td><a href="https://github.com/rbenv/rbenv#using-package-managers">ルベンブ</a></td>
        <td>ローカル環境のセットアップ時に、Braze Docsに必要なRubyのバージョンをインストール・管理できるRubyバージョンマネージャです。別のRubyバージョン・マネージャーを使う場合は、<a href="https://www.ruby-lang.org/en/documentation/installation/#managers">Rubyのサポートされているバージョン・マネージャーを</a>参照してください。</td>
    </tr>
    <tr>
        <td>テキストエディタ</td>
        <td><a href="https://code.visualstudio.com/download">ビジュアルスタジオコード（VSコード）</a></td>
        <td>BrazeのDocsリポジトリにあるすべてのファイルを編集できる、Microsoftによるフル機能のテキストエディタです。より快適にご利用いただくために、以下のプラグインをインストールしてください：
            <ul>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=sissel.shopify-liquid">リキッド＋ジキル・リンター</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint">マークダウン・リンター</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker">スペルチェッカー</a></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>テキストエディタ</td>
        <td><a href="https://www.jetbrains.com/idea/download/">IntellijのIDEAコミュニティ・エディション</a></td>
        <td>Intellijによるフル機能のテキストエディタで、Braze Docsリポジトリのあらゆるファイルを編集できます。より快適にご利用いただくために、以下のプラグインをインストールしてください：
            <ul>
                <li><a href="https://plugins.jetbrains.com/plugin/7793-markdown">マークダウン・リンター</a></li>
                <li><a href="https://plugins.jetbrains.com/plugin/12175-grazie-lite">スペルチェッカー</a></li>
            </ul>
        </td>
    </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
この記事を書いている時点では、すべてのソフトウェアが無料である。製品が無料でなくなった場合は、お知らせ[ください](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)。
{% endalert %}

### ステップ 2.2:GitHubアカウントを設定する

次に、[GitHubアカウントを作成](https://github.com/join)し、[SSHキーを設定](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)します。

{% alert note %}
[WSLを使って](https://learn.microsoft.com/en-us/windows/wsl/install)いる場合は、Linuxの指示に従ってSSHキーを設定してください。
{% endalert %}

### ステップ 2.3:リポジトリをフォークする

[Braze Docs GitHubリポジトリを](https://github.com/braze-inc/braze-docs)開き、**Forkを**選択します。

![The Braze Docs GitHub repository showing "Fork".]({% image_buster /assets/img/contributing/github/fork_the_repository.png %})

{% alert tip %}
詳細は[GitHubを参照：フォークについて](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
{% endalert %}

デフォルトの設定のまま、**フォークの作成を**選択します。

![The Braze Docs GitHub repository showing "Create fork".]({% image_buster /assets/img/contributing/github/create_a_new_fork.png %})

フォークしたリポジトリで、**Code**>**SSH**><i class="fa-regular fa-clone"></i> **Copy** を選択します。

![An example forked repository with the "Code" dropdown open showing the "Copy" option.]({% image_buster /assets/img/contributing/github/clone_the_fork.png %}){: style="max-width:50%;"}

ターミナルでホームディレクトリを開き、Braze Docsリポジトリをクローンします。

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

### ステップ 2.4:Rubyのインストール

[ローカル・サイトのプレビューを生成]({{site.baseurl}}/contributing/generating_a_preview/)するには、Rubyのバージョン`3.2.2` 。ターミナルで`braze-docs` を開き、Rubyのバージョン`3.2.2` をチェックする。

```bash
cd ~/braze-docs
ruby --version
```

このバージョンがインストールされていない場合は、[サポートされているバージョン・マネージャーを使って](https://www.ruby-lang.org/en/documentation/installation/#managers)Rubyのバージョン`3.2.2` をインストールしてください。例えば、[rbenv](https://github.com/rbenv/rbenv).

```bash
rbenv install 3.2.2
```

### ステップ 2.5:依存関係をインストールする

次に、Braze Docsの依存関係をインストールします。これらは、ローカルのBraze Docsサイトを生成するための小さなプログラムです。

```bash
bundle install
```

## 次のステップ

Gitやdocs-as-codeが初めての方は、チュートリアルから始めましょう：[あなたの最初の貢献]({{site.baseurl}}/contributing/your_first_contribution/)そうでなければ、以下のいずれかをチェックしてほしい。

- [コンテンツ管理]({{site.baseurl}}/contributing/content_management/)
- [YAMLメタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)
- [プレビューの作成]({{site.baseurl}}/contributing/generating_a_preview/)
- [スタイルガイド]({{site.baseurl}}/contributing/style_guide)
