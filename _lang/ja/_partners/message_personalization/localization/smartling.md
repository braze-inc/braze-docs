---
nav_title: Smartling
article_title: Smartling
description: "このリファレンス記事では、Brazeとローカライゼーション向けクラウドベースのソフト「スマートリング」の提携について概説します。このインテグレーションを使用すると、Brazeでメール テンプレートとコンテンツブロックを変換できます。"
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][2] は、Web サイト s、アプリライセンス、およびカスタマーエクスペリエンス s の翻訳を自動化することを目的とした顧客向けのエンドツーエンドの クラウド翻訳マネジメントソフトウェアです。

Brazeとスマートリングインテグレーションを使用すると、メール テンプレートとコンテンツブロックを変換できます。スマートリングは、翻訳中の視覚的な文脈の利点を言語学者に提供し、エラーを減らし、質を維持します。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| スマートリング・アカウント | この提携の前進タグeを取るには、[Smartlingアカウント][2]が必要です。 |
| スマートリング翻訳プロジェクト | Brazeをスマートリングに接続するには、まずサインアップし、[翻訳プロジェクト][3]を作成する必要があります。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロック権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [Your REST エンドポイント URL][1].エンドポイントは、インスタンスのBraze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

スマートリングBrazeインテグレーションでは、メール テンプレートとコンテンツブロックを翻訳できます。 

電子メールテンプレート: 
* HTMLエディタの電子メールのみがサポートされます。 
* それぞれの変換は、独自のメール テンプレートとして保存されます。 

コンテンツブロック: 
* すべてのコンテンツブロックがサポートされます。 
* コンテンツブロックには、元のバージョンと翻訳されたバージョンの両方が含まれます。
* リキッドスクリプトは、受信者の言語環境設定に基づいて、ディスプレイの正しい言語を決定します。

### ステップ1:スマートリングTMSでのBraze事業の設定

#### Brazeをスマートリングに接続する

1. [Smartling][2] で、スマートリングアカウントに[Braze Connector][6] プロジェクトタイプを作成します。 
  - 必要なすべてのターゲット言語がプロジェクトに追加されていることを確認します。
2. 本事業では、**Settings**> **Braze設定**> **Braze**に接続します。
3. Braze API のURL とBraze API キーを入力します。
4. \[**保存**] をクリックします。

#### 完全なBrazeコネクター構成

コネクタ構成については、スマートリング[ドキュメント][3]を参照してください。

以前の翻訳リクエストのオートメーション方法を選択します。

**Language Configuration**でソース言語とターゲット言語を設定します。これは、Smartling TMSにコンテンツを取り込み、翻訳をBrazeに送り返すためにコネクターによって使用されます。

![][8]

### ステップ2:Smartling にコンテンツを送信する

Brazeコネクターを接続して設定すると、スマートリングプロジェクトの**Braze**タブにBrazeの内容が表示されます。詳細については、スマートリング[ドキュメント][7]を参照してください。

Smartling は、以下の方法でコンテンツを検索および選択する高度な機能を提供します。
* キーワード検索
* Braze内容種別
* Braze タグギング

![][9]

### ステップ3:Brazeへの変換の追加

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