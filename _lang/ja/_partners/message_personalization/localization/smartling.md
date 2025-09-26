---
nav_title: Smartling
article_title: Smartling
description: "このリファレンス記事では、Braze と Smartling のパートナーシップについて説明します。Smartling はクラウドベースのローカライゼーションソフトウェアです。Braze Connectorは、HTMLメールテンプレート、コンテンツブロック、キャンバス、キャンペーンメールメッセージの翻訳をサポート。"
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) は、Web サイト s、アプリライセンス、およびカスタマーエクスペリエンス s の翻訳を自動化することを目的とした顧客向けのエンドツーエンドの クラウド翻訳マネジメントソフトウェアです。

_この統合は Smartling によって管理されます。_

## 統合について

Braze Connectorは、HTMLメールテンプレート、コンテンツブロック、キャンバス、キャンペーンメールメッセージの翻訳をサポート。翻訳はSmartlingに依頼され、翻訳されたコンテンツは自動的にBrazeに送られる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Smartling アカウント | このパートナーシップを活用するには、[Smartling アカウント](https://dashboard.smartling.com/)が必要です。 |
| Smartling 翻訳プロジェクト | Braze アカウントを Smartling に接続するには、まずサインインし、[翻訳プロジェクトを作成する](https://help.smartling.com/hc/en-us/articles/115003074093)必要があります。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロック権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Smartling と Braze の統合により、HTML メールテンプレート、コンテンツブロック、キャンバスおよびキャンペーンメールメッセージを翻訳できます。翻訳する内容によって、以下の詳細に注意すること：

**メールテンプレート**
* HTMLメールテンプレートのみがサポートされている。
* 翻訳されたメールがコネクターを通じて Braze に配信される方法を決定する必要があります。
  * **すべての言語に1つのメール：**コネクターは、すべての言語をソースと同じメールで配信します。
  * **1言語につき1メール：**コネクターは Braze の各言語に新しいメールを作成します。

**コンテンツブロック**
* すべてのコンテンツブロックがサポートされます。
* コンテンツブロックには、元のバージョンと翻訳されたバージョンの両方が含まれます。
* リキッドスクリプトは、受信者の言語環境設定に基づいて、ディスプレイの正しい言語を決定します。

**キャンペーンとキャンバス**
* Brazeの**Multi-Language Support**設定に対象言語が追加されていることを確認する。
* コネクター設定の詳細については、[Smartling のドキュメント](https://help.smartling.com/hc/en-us/articles/13248549217435)を参照してください。

## 統合

### ステップ1:Smartling TMS で Braze プロジェクトを設定する

#### Braze を Smartling に接続する

1. [Smartling](https://dashboard.smartling.com/) で、Smartling アカウントに [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093) プロジェクトタイプを作成します。
  - 必要なターゲット言語がすべてプロジェクトに追加されていることを確認する。
2. このプロジェクトで、[**設定**] > [**Braze 設定**] > [**Braze に接続する**] の順にクリックします。
3. Braze API の URL とBraze API キーを入力します。
4. [**保存**] を選択します。

#### Braze コネクター設定を完了する

コネクター設定の詳細については、Smartling の[ドキュメント](https://help.smartling.com/hc/en-us/articles/13248549217435)を参照してください。

1. 以前の翻訳リクエストのオートメーション方法を選択します。
2. [**Language Configuration**] でソース言語とターゲット言語を設定します。このコネクターは、Smartling TMSにコンテンツを取り込み、Brazeに翻訳を送り返すために使用される。

![コネクターの言語設定。]({% image_buster /assets/img/smartling/smartling-braze-settings.png %})

### ステップ2:Smartling にコンテンツを送信する

Brazeコネクターを接続して設定すると、スマートリングプロジェクトの**Braze**タブにBrazeの内容が表示されます。詳細については、Smartling の[ドキュメント](https://help.smartling.com/hc/en-us/articles/13248577069979)を参照してください。

Smartling は、以下の方法でコンテンツを検索および選択する高度な機能を提供します。

* キーワード検索
* Braze コンテンツタイプ
* Braze タグ付け

![コンテンツブロックリスト。]({% image_buster /assets/img/smartling/smartling-content-blocks-list.png %})

### ステップ 3:Braze に翻訳を追加する

翻訳がスマートリングプラットフォームで完了すると、自動的にBrazeに送信されます。スマートリングとBraze間で手動でコンテンツを同期する必要はありません。


