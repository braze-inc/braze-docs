---
nav_title: ユーザー属性CSVラムダプロセス
permalink: /user_csv_lambda/
description: "以下の記事では、Track users Brazeエンドポイントを通じてCSVファイルからユーザー属性データを直接BrazeにポストするLambdaプロセスを簡単にデプロイできるサーバーレスアプリケーションを紹介している。"
hidden: true
---

# ユーザー属性CSVをBrazeにインポートする

> 以下の記事では、CSVファイルからユーザー属性データを[Track usersエンドポイントを通じて]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)Brazeに直接ポストするLambdaプロセスを簡単にデプロイできるサーバーレスアプリケーションを紹介している。このアプリケーションの統合は、我々のAmperityパートナーとともにテストされ、[GitHubで](https://github.com/braze-inc/growth-shares-lambda-user-csv-import)見ることができる。

このプロセスは、設定されたAWS S3バケットにCSVファイルをアップロードすると即座に起動する。大きなファイルやアップロードを扱うことができるが、ラムダの時間制限により、関数は10分後に実行を停止する。このプロセスは、ファイルの残りの部分を処理するために、別のラムダ・インスタンスを起動する。ファンクションのタイミングについての詳細は、[推定実行](#estimated-execution-times)時間をチェックしてほしい。

{% alert important %}
このアプリケーションは、Brazeの成長部門によって構築され、維持されている。このアプリケーションの制作者に連絡を取りたい場合は、[GitHubのissueを](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues)作成し、フィードバックや問題が発生する可能性があることを伝えてほしい。


#### CSVユーザー属性

更新されるユーザー属性は、以下の`.csv` ：

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

最初の列は更新されるユーザーの外部IDを指定し、次の列は属性名と値を指定しなければならない。指定する属性の数は様々である。処理するCSVファイルがこのフォーマットに従っていない場合、この関数は失敗する。  

**CSVファイルの例：**

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### CSV処理

配列に含まれる値（例：`"['Value1', 'Value2']"` ）は自動的に構造化解除され、配列の文字列表現ではなく、配列でAPIに送信される。

## 要件

このラムダ関数を成功させるには、以下のものが必要だ：
- S3とLambdaサービスを利用するための**AWSアカウント**
- **Braze**サーバーに接続するための**Braze API URL**
- `/users/track` エンドポイントにリクエストを送信できるようにするための**Braze API キー**
- 更新するユーザーの外部IDと属性を含む**CSVファイル**

{% tabs %}
{% tab API URL %}

API URL、またはRESTエンドポイントは、Braze APIドキュメントやダッシュボードで確認できる。

- **APIドキュメント**<br>[APIドキュメントに従って]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)、BrazeインスタンスURLをRESTエンドポイントURLに一致させるだけでよい。例えば、ダッシュボードに`dashboard-01.braze.com/` URLが表示されている場合、RESTエンドポイントは`https://rest.iad-01.braze.com` 。<br><br>
- **ダッシュボード**<br>**Manage Settings**ページでSDKエンドポイントを探す。RESTエンドポイントを取得するには、`sdk` を`rest` に置き換える。例えば、`sdk.iad-01.braze.com` と表示された場合、APIのURLは次のようになる。 `rest.iad-01.braze.com`

{% endtab %}
{% tab APIキー %}

Brazeサーバーに接続するには、APIキーが必要である。この一意の識別子により、Brazeはあなたの身元を確認し、データをアップロードすることができる。 

APIキーを取得するには、**「設定」**>「**APIキー**」を選択する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを見つけることができる。


`/users/track` 、エンドポイントへの投稿を許可するAPIキーが必要となる。APIキーの1つがそのエンドポイントをサポートしていることが分かっていれば、そのキーを使うことができる。 

新しいものを作成するには、**Create New API Keyを**クリックする。次に、APIキーに名前を付け **users.track**を選択し、**\[Save API Key**]をクリックする。

{% endtab %}


## 使用上の注意

##### 概要
1. AWSサーバーレスアプリケーションリポジトリからBrazeの一般公開されているCSV処理Lambdaをデプロイする
2. 新しく作成したS3バケットに、ユーザー属性のCSVファイルをドロップする
3. ユーザーは自動的にBrazeにインポートされる

#### デプロイする

ユーザー属性CSVファイルの処理を開始するには、処理を代行するサーバーレス・アプリケーションをデプロイする必要がある。このアプリケーションは、デプロイを成功させるために以下のリソースを自動的に作成する：

- ラムダ関数
- Lambdaプロセスが読み込み可能なCSVファイル用のS3バケット_（注意：このLambda関数は、`.csv` 拡張子ファイルの通知のみを受け取る）_
- S3バケットの作成を許可する役割
- Lambdaが新しいバケットでS3のアップロードイベントを受け取ることを許可するポリシー

[アプリケーションへの](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import)直接リンクに従うか、[AWS Serverless Application Repositoryを](https://serverlessrepo.aws.amazon.com/applications)開き、"braze-user-attribute-import "を検索する。なお、このアプリケーションを見るには、`Show apps that create custom IAM roles and resource policies` のチェックボックスをチェックしなければならない。アプリケーションは、ラムダが新しく作成されたS3バケットから読み込むためのポリシーを作成する。

**Deployを**クリックし、AWSに必要なリソースをすべて作成させる。

デプロイを観察し、スタック（つまり必要なすべてのリソース）が[CloudFormationに](https://console.aws.amazon.com/cloudformation/)作成されていることを確認できる。serverlessrepo-braze-user-attribute-import」というスタックを見つける。**ステータスが** `CREATE_COMPLETE` に変わったら、その機能は使用可能である。スタックをクリックして**「リソース」を**開き、さまざまなリソースが作成されるのを見ることができる。

以下のリソースが作成された：

- [S3バケット](https://s3.console.aws.amazon.com/s3/)-`braze-user-csv-import-aaa123` という名前のバケット。`aaa123` はランダムに生成された文字列である。
- [ラムダ関数](https://console.aws.amazon.com/lambda/)\- 以下の名前のラムダ関数である。 `braze-user-attribute-import`
- [IAM Role](https://console.aws.amazon.com/iam/)-`braze-user-csv-import-BrazeUserCSVImportRole` という名前のポリシーで、ラムダがS3から読み込み、関数の出力をログに記録することを許可する。

#### 走る

この機能を実行するには、新しく作成したS3バケットにユーザー属性CSVファイルをドロップする。

## モニタリングとロギング

関数が正常に実行されていることを確認するには、関数の実行ログを読めばいい。BrazeユーザーCSVインポート機能を開き（コンソールのLambdaリストから選択）、**Monitorに**移動する。ここでは、その関数の実行履歴を見ることができる。出力を読むには、**View logs in CloudWatchを**クリックする。チェックしたいラムダ実行イベントを選択する。

## 推定実行時間
_2048 MB ラムダ関数_

| 行数 | 実行時間 |
| --------- | ---------- |
| 10k       | 3s         |
| 100k      | 30s        |
| 1M        | 5分      |
| 5M        | 30分     |

## 既存の関数を更新する

すでにアプリケーションをデプロイしていて、新しいバージョンがリポジトリにある場合は、初めてデプロイするのと同じように、機能を再デプロイすることでアップデートできる。つまり、Braze API KeyとBraze API URLを再度渡す必要がある。アップデートはファンクションコードを上書きするだけだ。S3バケットのような既存のリソースを変更したり削除したりすることはない。

## 致命的なエラー

予期せぬエラーによってファイルの処理が続行できなくなった場合、イベントが記録される（「[モニタリングとロギング](#monitoring-and-logging)」のCloudWatchからアクセス可能）。データ・ポイントを保存するために、同じデータを再インポートしないことが重要である。[GitHubリポジトリに](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)その手順がある。

{% alert important %}
[致命的なエラーや](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) [ラムダ設定の](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration)処理方法については、GitHubリポジトリを参照のこと。
