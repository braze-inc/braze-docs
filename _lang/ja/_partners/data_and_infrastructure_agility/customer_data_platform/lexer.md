---
nav_title: レクサー
article_title: レクサー
description: "この参考記事では、BrazeとLexerの提携について概説している。Lexerは、顧客データをマーケティング担当者の手に委ね、売上を促進する体験を喚起する顧客データ・プラットフォームである。"
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# レクサー

> \[小売業向けに構築された顧客データプラットフォームであるLexer][6] は、堅牢なデータエンリッチメントと最も直感的なツールおよび専門家の助言を組み合わせることで、ブランドが顧客体験を向上させ、売上の増加を促進するのを支援する。

BrazeとLexerの統合により、2つのプラットフォーム間でデータを同期することができる。Lexerのデータを使用して価値あるBrazeセグメントを作成するか、既存のセグメントをLexerにインポートしてインサイトを引き出す。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| パートナーアカウント | このパートナーシップを利用するには、Lexerアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限（`user.delete` を除く）と`segment.list` 権限を持つ Braze REST API キー。Lexerがより多くのBrazeオブジェクトをサポートするようになると、パーミッション・セットは変更される可能性がある。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Amazon AWS S3バケットと認証情報 | 統合を開始する前に、Lexerハブに接続されているAWS S3バケットのアクセス認証情報が必要である（これは、あなたが作成したバケットでも、Lexerがあなたのために作成し管理するバケットでもよい）。この要件に関するガイダンスについては、[Lexerを](https://learn.lexer.io/docs/amazon-s3)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Lexerで、**Manage > Integrationに**移動し、**Braze**タイルを選択し、**Integrate Brazeを**クリックする。以下の情報を提供する：
- **Braze RESTエンドポイント**
- **Braze REST API キー**
- **AWSクレデンシャル**
  - **AWS S3バケット名**
  - **AWS S3 \[バケットリージョン][4]**
  - **AWS S3バケットのパス**：このパスは、\[S3バケットをBraze][5] に接続する]際に指定したパスと一致する必要がある。Brazeに何も指定しなかった場合は空白にする。
  - **AWS S3のシークレットアクセスキー**：アクセスキーの作成]に関する情報はアマゾンを参照のこと][3] 。
- **ブレイズの輸出セグメントID**：Lexerにエクスポートしたいすべてのユーザーを含む、Brazeで作成したセグメントのID。Lexerにエクスポートしたくないユーザーがいる場合は、Brazeで作成したセグメントから除外することができる。セグメント識別子を見つけるには、Brazeで目的のセグメントをクリックし、**セグメントAPI識別子を**見つける。

![][1]

### AWS S3のオプションを選択する（Lexer管理または自己管理）
BrazeをLexerハブに接続するには、Lexerが管理するバケットを使用するのが望ましい。Lexerは、Brazeの設定に必要な1回限りの詳細を提供する。

すでにS3バケットをBrazeに接続し、他の目的で使用している場合は、代わりに、前述の手順に従って、Lexerにこの自己管理バケットへのアクセスを提供する必要がある。

この統合は、既存のAPIトークンとシークレットをLexerに提供し、Lexerがあなたに代わってこれらのエクスポートを行うことで機能する。また、これらの認証情報とS3の設定を使用して、BrazeのデータをLexerにインポートし、両プラットフォームのデータを自動的に同期する。

## セグメントをブレイズに送る

### ステップ1:アクティベーションを行う

Lexer ActivateはBrazeプロファイルを自動的に更新し、顧客のセグメントへの出入りに応じて属性を追加または削除する。

1. Lexerの\[**Lexer Activations**]で**\[ACTIVATE NEW AUDIENCE]**をクリックする。
2. このキャンペーンに適切なBrazeのアクティベーションを選択する。
3. セグメントを追加する。
4. オーディエンス名を更新する。これがBrazeでの属性値となる。
5. これがBrazeで更新するカスタム属性だ。[Lexerサポートに](support@lexer.io)連絡してアップデートする。
6. 適切なリストアクションをチェックする。
7. 規約を確認し、**「SEND AUDIENCE**」をクリックする。

![][7]

### ステップ2:アクティベーションを確認する

Activateでアクティベーションが送信されたことが確認されると、Brazeで記録が更新され始める。Lexerから確認メールが届くまで、Brazeのプロフィールは完全に更新されない。

### ステップ3:ブレイズ・セグメントを作成する

Brazeでは、Lexerのオーディエンス名が`lexer_audience` カスタム属性の値になっていることがわかる。Brazeには、1つの属性につき100個の値という制限がある。

セグメントを作成するには、「**セグメント > + セグメントの作成**」と進み、フィルターとして**「カスタム属性**」を選択する。次に、属性として`lexer_audience` 、オーディエンス名としてLexerを選択する。完了したら、オーディエンスを**保存する**。

この新しく作成したセグメントを、今後のBrazeのキャンペーンやキャンバスに追加して、これらのエンドユーザーをターゲットにすることができる。

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}