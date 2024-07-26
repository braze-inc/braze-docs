---
nav_title: ホーム
article: Contributing to Braze Docs
description: "Braze Docsへの貢献を始めるために必要なものは以下の通り！"
page_order: 0
search_tag: Contributing
---

# Braze Docsに貢献する

> Braze Docsに貢献してくれてありがとう！毎週火曜日と木曜日に、コミュニティからの投稿をマージし、Braze Docsにデプロイする。このガイドを使って、次回のデプロイ時に変更をマージしてもらおう。

## 前提条件

Braze Docsに貢献するためには、Gitをある程度理解している必要がある。Gitを使うのが初めてで何から始めたらいいかわからない場合は、[Git Bookを参照：Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).復習が必要な場合は、[GitとGitHubを]({{site.baseurl}}/contributing/git_and_github/)参照のこと。

## ステップ 1:CLAに署名する

Braze Docsに貢献する人は全員、[貢献ライセンス契約（CLA](https://www.braze.com/docs/cla)）に署名しなければならない。CLAに署名しないと、GitHubの`@cla-bot` 、自動的にプルリクエストがブロックされる。

## ステップ 2:環境を設定する

Braze Docsに複雑な変更や複数ページの変更を加える前に、ローカライゼーション環境を設定する必要がある。しかし、小さな単一ドキュメントの変更は[GitHubで直接]({{site.baseurl}}/contributing/your_first_contribution/?tab=github#step-2-make-a-change)行うことができる。

### ステップ 2.1:必要なソフトウェアを入手する

最低限、ターミナル、テキストエディタ、そしてルビーのバージョンマネージャーが必要だ。何から始めたらいいかわからない場合は、以下を参照されたい。

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
        <td><a href="https://desktop.github.com/">GitHub Desktop</a></td>
        <td>ターミナルでコマンドを入力する代わりに、Gitコマンドを実行するために使うグラフィカル・ユーザー・インターフェース（GUI）。</td>
    </tr>    
    <tr>
        <td>ターミナル</td>
        <td><a href="https://wezfurlong.org/wezterm/index.html">Wezterm</a></td>
        <td>コマンドラインからコマンドを実行したり、Braze Docsリポジトリとやりとりしたりできるターミナルエミュレータ。Windowsオペレーティングシステムを使用している場合は、Windows Subsystem for Linux（WSL）もインストールする必要がある。</td>
    </tr>
    <tr>
        <td>ターミナル延長</td>
        <td><a href="https://learn.microsoft.com/en-us/windows/wsl/install">Linux用Windowsサブシステム（WSL）*。</a></td>
        <td>WSLを使えば、Linuxサブシステムをインストールし、Windowsオペレーティングシステム上でUnixライクなコマンドを実行できる。Windowsオペレーティングシステムから投稿する場合は、WSLをインストールすることをお勧めする。そうすることで、ドキュメントに記載されているUnixライクなコマンドが使えるようになる。<br><br><em>* Windows版のみ。</em></td>
    </tr>
    <tr>
        <td>パッケージマネージャー</td>
        <td><a href="https://brew.sh/">自作</a></td>
        <td>Braze Docsへの投稿に使用するさまざまなコマンドラインインターフェイス（CLI）ツールをインストールして管理できるパッケージマネージャー。</td>
    </tr>
    <tr>
        <td>Rubyバージョンマネージャー</td>
        <td><a href="https://github.com/rbenv/rbenv#using-package-managers">rbenv</a></td>
        <td>ローカライゼーション環境の設定時に、Braze Docsに必要なRubyバージョンのインストールと管理を可能にするRubyバージョンマネージャー。別のRubyバージョンマネージャーを使いたい場合は、<a href="https://www.ruby-lang.org/en/documentation/installation/#managers">Rubyがサポートしているバージョンマネージャーを</a>参照のこと。</td>
    </tr>
    <tr>
        <td>テキストエディタ</td>
        <td><a href="https://code.visualstudio.com/download">ビジュアル・スタジオ・コード（VSコード）</a></td>
        <td>BrazeDocsリポジトリ内のあらゆるファイルを編集できる、Microsoftによるフル機能のテキストエディタ。あなたの体験を向上させるために、以下のプラグインをインストールしてほしい：
            <ul>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=sissel.shopify-liquid">Liquid + Jekyll Linter</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint">マークダウン・リンター</a></li>
                <li><a href="https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker">スペルチェッカー</a></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>テキストエディタ</td>
        <td><a href="https://www.jetbrains.com/idea/download/">IntellijのIDEAコミュニティ版</a></td>
        <td>Intellij によるフル機能のテキストエディタで、Braze Docs リポジトリ内のあらゆるファイルを編集できる。あなたの体験を向上させるために、以下のプラグインをインストールしてほしい：
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
この記事を書いている時点では、すべてのソフトは無料だ。ある製品が無料でなくなったことを発見したら、[ぜひ](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)お知らせいただきたい。
{% endalert %}

### ステップ 2.2:GitHubアカウントを設定する

次に、[GitHubアカウントを作成](https://github.com/join)し、[SSHキーを設定](https://docs.github.com/en/enterprise-cloud@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)する。

{% alert note %}
[WSLを使って](https://learn.microsoft.com/en-us/windows/wsl/install)いる場合は、Linuxの指示に従ってSSHキーを設定する。
{% endalert %}

### ステップ 2.3:リポジトリをフォークする

[Braze Docs GitHubリポジトリを](https://github.com/braze-inc/braze-docs)開封し、**Forkを**選択する。

![Braze DocsのGitHubリポジトリに「Fork」と表示されている。]({% image_buster /assets/img/contributing/github/fork_the_repository.png %})

{% alert tip %}
詳細は[GitHubを参照のこと：フォークについて](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks).
{% endalert %}

デフォルト設定のまま、**フォークの作成を**選択する。

![Braze DocsのGitHubリポジトリに「Create fork」と表示されている。]({% image_buster /assets/img/contributing/github/create_a_new_fork.png %})

フォークしたリポジトリで、**コード**>**SSH**><i class="fa-regular fa-clone"></i> **コピーを**選択する。

![コード」ドロップダウンを開封し、「コピー」オプションを表示したフォークリポジトリの例。]({% image_buster /assets/img/contributing/github/clone_the_fork.png %}){: style="max-width:50%;"}

ターミナルでホームディレクトリを開封し、Braze Docsリポジトリを複製する。

```bash
cd ~
git clone git@github.com:braze-inc/braze-docs.git
```

### ステップ 2.4:Rubyをインストールする

[ローカル・サイトのプレビューを生成]({{site.baseurl}}/contributing/generating_a_preview/)するには、Rubyのバージョン`3.3.0` がインストールされている必要がある。ターミナルで`braze-docs` を開封し、Rubyのバージョン`3.3.0` をチェックする。

```bash
cd ~/braze-docs
ruby --version
```

このバージョンがインストールされていない場合は、[サポートされているバージョンマネージャーを使って](https://www.ruby-lang.org/en/documentation/installation/#managers)Rubyのバージョン`3.3.0` をインストールしてほしい。例えば、[rbenvを](https://github.com/rbenv/rbenv)使う：

```bash
rbenv install 3.3.0
```

### ステップ 2.5:依存関係をインストールする

次に、Braze Docsの依存関係をインストールする。これらは、ローカルのBraze Docsサイトを生成するための小さなプログラムである。

```bash
bundle install
```

## 次のステップ

Gitやdocs-as-codeが初めてなら、チュートリアルから始めよう：[あなたの最初の貢献]({{site.baseurl}}/contributing/your_first_contribution/)だ。そうでなければ、以下のいずれかをチェックしてほしい。

- [コンテンツ・マネージャー]({{site.baseurl}}/contributing/content_management/)
- [YAMLメタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)
- [プレビューを作成する]({{site.baseurl}}/contributing/generating_a_preview/)
- [スタイルガイド]({{site.baseurl}}/contributing/style_guide)
