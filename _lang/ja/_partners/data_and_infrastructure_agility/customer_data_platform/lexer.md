---
nav_title: Lexer
article_title:レクサー
description:"この参考記事では、顧客データをマーケターの手に委ね、売上を促進するエクスペリエンスを喚起する顧客データプラットフォームであるBrazeとLexerの提携について概説している。"
alias: /partners/lexer/
page_type: partner
search_tag:Partner
---

# レクサー

> \[小売（店）向けに構築された顧客データプラットフォームである Lexer][6] は、堅牢なデータエンリッチメントと最も直感的なツールおよび専門家によるアドバイザリーを組み合わせ、カスタマーエクスペリエンスの向上を通じてブランドの売上増加を支援する。

BrazeとLexerの統合により、2つのプラットフォーム間でデータを同期することができる。Brazeのデータを使用して価値あるセグメンテーションを作成するか、既存のセグメンテーションをLexerにインポートしてインサイトを解き放つ。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| パートナーアカウント | このパートナーシップを利用するには、Lexerアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限（`user.delete` を除く）と`segment.list` 権限を持つ Braze REST API キー。Lexerがより多くのBrazeオブジェクトのサポートを追加するにつれて、権限設定は変更される可能性があるため、今より多くの権限を付与するか、将来的にこれらの権限を更新することを計画するとよい。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに依存する。 |
| Amazon AWS S3バケットと認証情報 | 統合を開始する前に、Lexerハブに接続されているAWS S3バケットの認証情報が必要である（これは、あなたが作成したバケットでも、Lexerがあなたのために作成して管理するバケットでもよい）。この要件に関するガイダンスについては、[Lexerを](https://learn.lexer.io/docs/amazon-s3)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Lexerで、**マネージャー＞統合と**進み、**Braze**タイルを選択し、**Brazeを統合を**クリックする。以下の情報を提供する：
- **Braze RESTエンドポイント**
- **Braze REST API キー**
- **AWS認証情報**
  - **AWS S3バケット名**
  - **AWS S3 \[バケットリージョン][4]**
  - **AWS S3バケットのパス**：このパスは、\[S3バケットをBraze][5] に接続する]際に指定したパスと一致する必要がある。Brazeに何も指定しなかった場合は空白にする。
  - **AWS S3のシークレットアクセスキー**：アクセスキーの作成]に関する情報はアマゾンを参照のこと][3] 。
- **BrazeエクスポートセグメントID**：Brazeで作成した、Lexerにエクスポートしたいすべてのユーザーを含むセグメントのID。Lexerにエクスポートしたくないユーザーがいる場合、Brazeで作成したセグメンテーションから除外することができる。セグメント識別子を見つけるには、Brazeで目的のセグメントをクリックし、**セグメントAPI識別子を**見つける。

![][1]

### AWS S3のオプションを選択する（Lexerマネージャーまたはセルフマネジメント）
BrazeをLexerハブに接続するには、Lexerがマネージャーするバケットを使用するのが望ましい。Brazeの設定に必要な一回限りの詳細をLexerが提供する。

すでにS3バケットをBrazeに接続し、他の目的で使用している場合は、前述のステップに従って、この自己管理バケットへのアクセスをLexerに提供する必要がある。

この統合は、既存のAPIトークンとシークレットをLexerに提供し、Lexerがあなたに代わってこれらのエクスポートを行うことで機能する。また、これらの認証情報とS3の設定を使用して、BrazeのデータをLexerにインポートし、両プラットフォームのデータを自動的に同期する。

## Brazeにセグメンテーションを送る

### ステップ1:アクティベーションを行う

Lexer ActivateはBrazeプロファイルを自動的に更新し、顧客のセグメンテーションへの出入りに応じてカスタム属性を追加または削除する。

1. Lexerの\[**Lexer Activations**]で\[**ACTIVATE NEW AUDIENCE**]をクリックする。
2. このキャンペーンに適切なBrazeアクティベーションを選択する。
3. セグメンテーションを追加する。
4. オーディエンス名を更新する。これがBrazeでの属性値となる。
5. これがBrazeで更新するカスタム属性だ。[Lexerのサポートに](support@lexer.io)連絡して更新する。
6. 適切なリストアクションにチェックを入れる。
7. 規約を確認し、**SEND AUDIENCEを**クリックする。

![][7]

### ステップ2:アクティベーションを確認する

Activateでアクティベーションが送信されたことが確認されると、Brazeで記録が更新され始める。Brazeでプロファイルが完全に更新されるのは、Lexerからの確認メールを受け取ってからである。

### ステップ3:セグメンテーションを作成する

Brazeでは、Lexerのオーディエンス名が、`lexer_audience` カスタム属性の値になっていることがわかる。Brazeには、1つの属性につき100個の値という制限がある。

セグメントを作成するには、「**セグメント > + セグメントの作成**」に移動し、フィルターとして**カスタム属性を**選択する。次に、属性として`lexer_audience` 、オーディエンス名としてLexerを選択する。完了したら、オーディエンスを**保存**する。

この新しく作成したセグメンテーションを、今後のBrazeキャンペーンやCanvasに追加して、これらのエンドユーザーをターゲットにすることができる。

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}