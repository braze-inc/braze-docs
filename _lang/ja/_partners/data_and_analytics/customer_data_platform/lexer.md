---
nav_title: Lexer
article_title: Lexer
description: "このリファレンス記事では、Braze と Lexer のパートナーシップについて説明します。Lexer はマーケターが顧客データを使用して、売上を伸ばすエクスペリエンスを生み出すことができる顧客データプラットフォームです。"
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/) は小売業向けに構築された顧客データプラットフォームであり、堅牢なデータ強化機能と最も直感的なツールおよび専門家によるアドバイスを組み合わせて、ブランドが改善されたカスタマーエクスペリエンスによりインクリメンタルセールスを伸ばすことができるようにします

_この統合は Lexer によって管理されます。_

## 統合について

Braze と Lexer の統合により、この2つのプラットフォーム間でデータを同期できます。Lexer のデータを使用して有益な Braze セグメントを作成するか、既存のセグメントを Lexer にインポートしてインサイトを引き出します。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| パートナーアカウント | このパートナーシップを活用するには、Lexer アカウントが必要です。 |
| Braze REST API キー | すべての `user` 権限 (`user.delete` を除く) と`segment.list` 権限を持つ Braze REST API キー。Lexer でサポートされる Braze オブジェクトの増加に伴い、権限セットが変わる可能性があります。このため、この時点でより多くの権限を付与するか、これらの権限を今後更新する計画を立てることができます。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Amazon AWS S3バケットと認証情報 | 統合を開始する前に、Lexer ハブに接続されている AWS S3 バケット (お客様が作成したバケットまたはLexer がお客様のために作成して管理しているバケット) のアクセス認証情報が必要です。この要件に関するガイダンスについては、[Lexerを](https://learn.lexer.io/docs/amazon-s3)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Lexerで **[Manage] > [Integration]** に移動し、[**Braze**] タイルを選択し、[**Integrate Braze**] をクリックします。次の情報を入力します。
- **Braze RESTエンドポイント**
- **Braze REST API キー**
- **AWS 認証情報**
  - **AWS S3 バケット名**
  - **AWS S3 [バケットリージョン](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3バケットのパス**：このパスは、[S3バケットを Braze に接続する]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/)ときに指定したパスと一致している必要があります。Brazeに何も指定しなかった場合は空白にする。
  - **AWS S3シークレットアクセスキー**:[アクセスキーの作成](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/)に関する情報はアマゾンを参照のこと。
- **Braze エクスポートセグメント ID**:Lexerにエクスポートしたいすべてのユーザーを含む、Brazeで作成したセグメントのID。Lexerにエクスポートしたくないユーザーがいる場合は、Brazeで作成したセグメントから除外することができる。セグメント識別子を確認するには、Braze で目的のセグメントをクリックし、[**セグメント API 識別子**] を見つけます。

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### AWS S3 オプションを選択する (Lexer マネージドまたはセルフマネージド)
Braze を Lexer ハブに接続する方法として、Lexer マネージド バケットを使用する方法が推奨されます。これにより、必要な設定作業が減ります。Lexer は、Braze の設定に必要な1回限りの詳細情報を提供します。

すでにS3バケットをBrazeに接続し、他の目的で使用している場合は、代わりに、前述の手順に従って、Lexerにこの自己管理バケットへのアクセスを提供する必要がある。

この統合は、既存のAPIトークンとシークレットをLexerに提供し、Lexerがあなたに代わってこれらのエクスポートを行うことで機能する。また、これらの認証情報と S3設定を使用して Braze データが Lexer にインポートされ、両方のプラットフォームのデータが自動的に同期されます。

## Braze にセグメントを送信する

### ステップ1:アクティベーションを行う

Lexer Activate により Braze プロファイルが自動的に更新され、セグメントへの顧客の出入りに応じて属性が追加または削除されます。

1. Lexer の [**Lexer Activations**] で [**ACTIVATE NEW AUDIENCE**] をクリックします。
2. このキャンペーンに適切なBrazeのアクティベーションを選択する。
3. セグメントを追加する。
4. オーディエンス名を更新します。これは Braze での属性値となります。
5. これがBrazeで更新するカスタム属性だ。更新のため [Lexer サポート](support@lexer.io)に連絡します。
6. 適切なリストアクションを確認します。ほとんどの場合、リストを維持します。
7. 規約を確認し、**「SEND AUDIENCE**」をクリックする。

![]({% image_buster /assets/img/lexer/lexer.png %})

### ステップ 2:アクティベーションを確認する

Activate でアクティベーションが送信されたことが確認されると、Braze でレコードの更新が開始されます。Lexer から確認メールが届くまで、Braze のプロファイルは完全には更新されません。

### ステップ 3:Braze セグメントを作成する

Brazeでは、Lexer のオーディエンス名が `lexer_audience` カスタム属性の値になっています。Braze では、属性あたりの値の数は100に制限されています。

セグメントを作成するには、「**セグメント > + セグメントの作成**」と進み、フィルターとして**「カスタム属性**」を選択する。次に、属性として `lexer_audience` を選択し、目的の Lexer オーディエンス名を選択します。完了したら、オーディエンスを**保存**します。

この新しく作成したセグメントを、今後のBrazeのキャンペーンやキャンバスに追加して、これらのエンドユーザーをターゲットにすることができる。


