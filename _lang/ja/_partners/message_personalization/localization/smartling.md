---
nav_title: Smartling
article_title:スマートリング
description:「この参考記事では、BrazeとクラウドベースのローカライゼーションソフトウェアであるSmartlingのパートナーシップについて概説しています。この統合により、Braze のメールテンプレートとコンテンツブロックを翻訳できます。「
alias: /partners/smartling/
page_type: partner
search_tag:Partner
---

# スマートリング

> [Smartlingは][2]、ウェブサイト、アプリケーション、顧客エクスペリエンスの翻訳を自動化したいと考えているお客様向けの、エンドツーエンドのクラウド翻訳管理ソフトウェアです。

Braze と Smartling の統合により、メールテンプレートとコンテンツブロックを翻訳できます。Smartlingを使うと、翻訳中のコンテキストを視覚化できるという利点が言語学者に提供され、エラーが減り、品質が維持されます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| スマートリングアカウント | このパートナーシップを利用するには、[Smartlingアカウントが必要です][2]。 |
| スマートリング翻訳プロジェクト | Braze アカウントを Smartling に接続するには、[まずサインアップして翻訳プロジェクトを作成する必要があります][3]。 |
| Braze REST API キー | すべてのテンプレートとコンテンツブロック権限を持つBraze REST API キー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Smartling Brazeとの統合により、メールテンプレートとコンテンツブロックを翻訳できるようになります。 

メールテンプレート: 
* HTML エディタの電子メールのみがサポートされています。 
* 各翻訳は独自のメールテンプレートとして保存されます。 

コンテンツブロック: 
* すべてのコンテンツブロックがサポートされています。 
* コンテンツブロックには、元のバージョンと翻訳されたバージョンの両方が含まれています。
* Liquid スクリプトは、受信者の言語設定に基づいて表示に適した言語を決定します。

### ステップ1:スマートリング TMS で Braze プロジェクトをセットアップする

#### Braze をスマートリングに接続する

1. [スマートリングでは][2]、[スマートリングアカウントでBraze コネクタープロジェクトタイプを作成します][6]。 
  - 必要なすべてのターゲット言語がプロジェクトに追加されていることを確認します。
2. このプロジェクト内から、**設定 > Braze 設定** **> Braze** **に接続をクリックします**。
3. Braze API の URL と Braze API キーを入力します。
4. \[**保存**] をクリックします。

#### Braze コネクタの完全な構成

コネクタ構成の詳細については、Smartling [のドキュメント][3]。

以前の翻訳依頼をどのようにオートメーションしたいかを選択します。

**言語設定でソース言語とターゲット言語を設定します**。この情報は、コネクタが Smartling TMS にコンテンツを取り込み、翻訳を Braze に返送するために使用されます。

![][8]

### ステップ2:スマートリングにコンテンツを送信

Braze コネクターを接続してセットアップすると、Smartling プロジェクトの Braze タブに **Braze** コンテンツが表示されます。詳細については、Smartling [のドキュメントを参照してください][7]。

Smartlingは、次の方法でコンテンツを検索および選択するための高度な機能を提供します。
* キーワード検索
* Braze コンテンツタイプ
* Braze タギング

![][9]

### ステップ3:Braze に翻訳を追加する

Smartling プラットフォーム翻訳が完了すると、自動的に Braze に送信されます。Smartling と Braze の間でコンテンツを手動で同期する必要はありません。

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}