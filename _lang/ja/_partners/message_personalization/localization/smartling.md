---
nav_title: Smartling
article_title: Smartling
description: "このリファレンス記事では、Braze と Smartling のパートナーシップについて説明します。Smartling はクラウドベースのローカライゼーションソフトウェアです。この統合により、Braze でメールテンプレートとコンテンツブロックを翻訳できます。"
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][2] は、Web サイト s、アプリライセンス、およびカスタマーエクスペリエンス s の翻訳を自動化することを目的とした顧客向けのエンドツーエンドの クラウド翻訳マネジメントソフトウェアです。

Braze と Smartling の統合により、メールテンプレートとコンテンツブロックを翻訳できます。Smartling は、翻訳中に視覚的なコンテキストを利用できるようにすることで、エラーを減らし、品質を維持します。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Smartling アカウント | このパートナーシップを活用するには、[Smartling アカウント][2]が必要です。 |
| Smartling 翻訳プロジェクト | Braze アカウントを Smartling に接続するには、まずサインアップし、[翻訳プロジェクト][3]を作成する必要があります。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロック権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Braze と Smartling の統合により、メールテンプレートとコンテンツブロックを翻訳できます。 

電子メールテンプレート: 
* HTMLエディタの電子メールのみがサポートされます。 
* それぞれの変換は、独自のメール テンプレートとして保存されます。 

コンテンツブロック: 
* すべてのコンテンツブロックがサポートされます。 
* コンテンツブロックには、元のバージョンと翻訳されたバージョンの両方が含まれます。
* リキッドスクリプトは、受信者の言語環境設定に基づいて、ディスプレイの正しい言語を決定します。

### ステップ1:Smartling TMS で Braze プロジェクトを設定する

#### Braze を Smartling に接続する

1. [Smartling][2] で、Smartling アカウントに [Braze Connector][6] プロジェクトタイプを作成します。 
  - 必要なすべてのターゲット言語がプロジェクトに追加されていることを確認します。
2. このプロジェクト内から、[**Settings**] > [**Braze Settings**] > [**Connect to Braze**] をクリックします。
3. Braze API の URL とBraze API キーを入力します。
4. [**保存**] をクリックします。

#### Braze コネクター設定を完了する

コネクター設定の詳細については、Smartling の[ドキュメント][3]を参照してください。

以前の翻訳リクエストのオートメーション方法を選択します。

[**Language Configuration**] でソース言語とターゲット言語を設定します。これは、Smartling TMSにコンテンツを取り込み、翻訳をBrazeに送り返すためにコネクターによって使用されます。

![][8]

### ステップ2:Smartling にコンテンツを送信する

Brazeコネクターを接続して設定すると、スマートリングプロジェクトの**Braze**タブにBrazeの内容が表示されます。詳細については、Smartling の[ドキュメント][7]を参照してください。

Smartling は、以下の方法でコンテンツを検索および選択する高度な機能を提供します。
* キーワード検索
* Braze コンテンツタイプ
* Braze タグ付け

![][9]

### ステップ 3:Braze に翻訳を追加する

翻訳がスマートリングプラットフォームで完了すると、自動的にBrazeに送信されます。スマートリングとBraze間で手動でコンテンツを同期する必要はありません。

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}