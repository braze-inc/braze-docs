---
nav_title: ユーザー 属性 CSV Lambda プロセス
permalink: /user_csv_lambda/
description: "次の記事では、サーバーレスアプリケーションについて説明します。このアプリケーションを使用すると、CSVファイルからユーザー属性データを直接BrazeのTrack users Brazeエンドポイントに投稿するLambdaプロセスを簡単にデプロイできます。"
hidden: true
---

# ユーザー属性CSVをBrazeにインポート

> 次の記事では、サーバーレスアプリケーションについて説明します。このアプリケーションを使用すると、CSVファイルからユーザー属性データを直接Brazeに投稿するLambdaプロセスを簡単にデプロイできます。これを[ユーザーを追跡するエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を通じて行います。このアプリケーション統合は、当社のAmperityパートナーと共にテストされ、[GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import)で見つけることができます。

このプロセスは、CSVファイルを設定されたAWS S3バケットにアップロードするとすぐに開始されます。大きなファイルやアップロードを処理できますが、Lambdaの時間制限のため、関数は10分後に実行を停止します。このプロセスは、ファイルの残りの部分を処理するために別のLambdaインスタンスを起動します。関数のタイミングの詳細については、[推定実行時間](#estimated-execution-times)を確認してください。

{% alert important %}
このアプリケーションは、Braze成長部門によって構築および維持されています。このアプリケーションの作成者に連絡したい場合は、フィードバックや発生する可能性のある問題について[GitHub issue](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues)を作成してください。
{% endalert %}

#### CSVユーザー属性

更新されるユーザー属性は、次の`.csv`形式であることが期待されます:

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

最初の列には更新するユーザーのexternal IDを指定し、次の列には属性名と値を指定する必要があります。指定する属性の数は異なる場合があります。CSVファイルを処理する際に、この形式に従わない場合、関数は失敗します。  

**CSVファイルの例:**

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### CSV処理

配列内の任意の値（例：`"['Value1', 'Value2']"`）は自動的に分解され、配列の文字列表現ではなく配列としてAPIに送信されます。

## 要件

このLambda関数を正常に実行するには、次のものが必要です:
- **AWS アカウント** を使用して S3 および Lambda サービスを利用する
- **Braze API URL** を使用して Braze サーバーに接続する
- **Braze API キー** を使用して `/users/track` エンドポイントにリクエストを送信することができます
- **CSVファイル** にユーザーの外部IDと更新する属性

{% tabs %}
{% tab API URL %}

API URL、またはRESTエンドポイントは、Braze APIドキュメントおよびダッシュボードで確認できます。

- **APIドキュメント**<br>[APIドキュメント]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)によると、BrazeインスタンスURLをRESTエンドポイントURLに単純に一致させます。例えば、ダッシュボードに`dashboard-01.braze.com/` URLが表示されている場合、RESTエンドポイントは`https://rest.iad-01.braze.com`になります。<br><br>
- **ダッシュボード**<br>**設定の管理**ページに移動して、SDKエンドポイントを見つけてください。`sdk` を `rest` に置き換えて、REST エンドポイントを取得します。例えば、`sdk.iad-01.braze.com`が表示された場合、API URLは`rest.iad-01.braze.com`になります。

{% endtab %}
{% tab API キー %}

Brazeサーバーに接続するには、APIキーが必要です。このユニークな識別子により、Brazeはあなたの身元を確認し、データをアップロードすることができます。 

API キーを取得するには、**設定** > **API キー**に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは**開発者コンソール** > **API 設定**で見つけることができます。
{% endalert %}

`/users/track` エンドポイントに投稿する権限を持つAPIキーが必要です。APIキーの1つがそのエンドポイントをサポートしていることがわかっている場合、そのキーを使用できます。 

新しいものを作成するには、**新しいAPIキーを作成**をクリックします。次に、API キーに名前を付け、**users.track**の下の**ユーザーデータ**エンドポイントグループを選択し、**API キーを保存**をクリックします。

{% endtab %}
{% endtabs %}

## 使用説明書

##### 概要
1. AWS サーバーレスアプリケーションリポジトリから Braze の公開されている CSV 処理 Lambda をデプロイする
2. 新しく作成されたS3バケットにユーザー属性を含むCSVファイルをドロップします
3. ユーザーは自動的にBrazeにインポートされます

#### 展開する

ユーザー属性CSVファイルの処理を開始するには、処理を担当するサーバーレスアプリケーションをデプロイする必要があります。このアプリケーションは、正常にデプロイするために次のリソースを自動的に作成します:

- ラムダ関数
- CSVファイル用のS3バケットで、Lambdaプロセスが読み取ることができます（_注: このLambda関数は`.csv`拡張子のファイルに対してのみ通知を受け取ります_）
- S3バケットの作成を許可する役割
- 新しいバケットでLambdaがS3アップロードイベントを受信できるようにするポリシー

直接リンクをたどって[アプリケーション](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import)にアクセスするか、[AWSサーバーレスアプリケーションリポジトリ](https://serverlessrepo.aws.amazon.com/applications)を開いて「Braze-ユーザー-属性-インポート」を検索してください。このアプリケーションを表示するには、`Show apps that create custom IAM roles and resource policies`チェックボックスをオンにする必要があることに注意してください。このアプリケーションは、新しく作成されたS3バケットから読み取るためのポリシーをラムダに作成します。

**デプロイ**をクリックして、AWSに必要なリソースをすべて作成させます。

CloudFormation でスタック (つまり、必要なすべてのリソース) が作成されていることを確認できます。"serverlessrepo-Braze-ユーザー-属性-インポート"という名前のスタックを見つけてください。**ステータス**が`CREATE_COMPLETE`に変わった後、機能が使用可能になります。スタックをクリックして**Resources**を開封し、さまざまなリソースが作成されるのを見ることができます。

次のリソースが作成されました:

- [S3バケット](https://s3.console.aws.amazon.com/s3/) - `braze-user-csv-import-aaa123`という名前のバケットで、`aaa123`はランダムに生成された文字列です
- [ラムダ関数](https://console.aws.amazon.com/lambda/) - `braze-user-attribute-import`という名前のラムダ関数
- [IAM Role](https://console.aws.amazon.com/iam/) \- ポリシー名 `braze-user-csv-import-BrazeUserCSVImportRole` により、Lambda が S3 から読み取り、関数の出力をログに記録できるようにする

#### 走る

関数を実行するには、新しく作成されたS3バケットにユーザー属性CSVファイルをドロップします。

## 監視とログ

関数が正常に実行されることを確認するために、関数の実行ログを読むことができます。BrazeユーザーCSVインポート機能を開封（コンソールのLambdaリストから選択）し、**Monitor**に移動します。ここでは、関数の実行履歴を見ることができます。出力を読むには、**CloudWatch でログを表示**をクリックします。チェックしたいラムダ実行イベントを選択します。

## 推定実行時間
_2048 MB ラムダ関数_

| 行数 | 実行時間 |
| --------- | ---------- |
| 1万       | 3秒         |
| 10万      | 30秒        |
| 100万        | 5分      |
| 500万        | 30分     |

## 既存の関数を更新する

アプリケーションを既にデプロイしていて、リポジトリに新しいバージョンがある場合は、最初に行ったかのように関数を再デプロイすることで更新できます。つまり、Braze API キーとBraze API URLを再度渡す必要があります。更新は関数コードのみを上書きします。それは、S3バケットのような他の既存のリソースを変更または削除しません。

## 致命的なエラー

予期しないエラーが発生してファイルの処理が進まない場合、（[モニタリングとログ記録](#monitoring-and-logging)で説明されているCloudWatchを通じてアクセス可能な）イベントが記録され、プログラムがファイルの処理を停止したポイントからLambdaを再起動するために使用できます。同じデータを再インポートしないことが重要です。データポイントを節約するために。これを行う手順は、私たちの[GitHubリポジトリ](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)にあります。

{% alert important %}
GitHubリポジトリを訪れて、[致命的なエラー](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)や[Lambda構成](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration)の処理方法について詳しく学んでください。
{% endalert%}