---
nav_title: ユーザー属性 CSV Lambda プロセス
permalink: /user_csv_lambda/
description: "次の記事では、サーバーレスアプリケーションを参照しています。これにより、ユーザー属性データをCSV ファイルから追跡ユーザーBrazeエンドポイントを介して直接Brazeに投稿するLambda プロセスを簡単にデプロイできます。"
hidden: true
---

# Brazeインポートのユーザ属性CSV

> 次の記事では、[ Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を使用してCSV ファイルから直接Braze にユーザー属性データを送信するLambda プロセスを簡単にデプロイすることができるサーバーレスアプリケーションについて説明します。このアプリケーション統合は、Amperity パートナーでテストされ、[GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) にあります。

このプロセスは、設定されたAWS S3 バケットにCSV ファイルをアップロードするとすぐに起動します。大きなファイルやアップロードを処理できますが、Lambda の時間制限により、関数は10 分後に実行を停止します。このプロセスは、別の Lambda インスタンスを起動して、ファイルの残りの部分の処理を終了します。機能タイミングの詳細については、[推定実行時間](#estimated-execution-times)を確認してください。

{% alert important %}
このアプリケーションは、Braze Growth 部門によって構築され、管理されています。このアプリケーションの作成者に連絡する場合は、発生する可能性のあるフィードバックまたは問題について、[GitHub issue](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues) を作成します。
{% endalert %}

#### CSVユーザー属性

更新するユーザ属性は、次の`.csv` 形式で指定します。

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

最初の列には更新するユーザーの外部ID を指定し、次の列には属性名と値を指定する必要があります。指定できる属性の数は異なります。処理するCSV ファイルがこの形式に従わない場合、関数は失敗します。  

**CSV ファイルの例:**

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### CSV処理

配列内の値(例: `"['Value1', 'Value2']"`) は自動的に破棄され、配列の文字列表現ではなく、配列内のAPI に送信されます。

## 要件

この Lambda 関数を正常に実行するには、以下が必要です。
- **S3およびLambdaサービスを使用するためのAWSアカウント**
- **Brazeサーバに接続するためのBrazeAPI URL**
- **Braze API Key** `/users/track` エンドポイントにリクエストを送信できるようにする
- **CSV ファイル** ユーザの外部ID と更新する属性

{% tabs %}
{% tab API URL %}

API URL またはREST エンドポイントは、Braze API ドキュメントとダッシュボードで確認できます。

- **API ドキュメント**<br>[API documentation]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) に従って、Braze インスタンスのURL をREST エンドポイントのURL に単純に一致させます。たとえば、ダッシュボードに`dashboard-01.braze.com/` URL が表示されている場合、REST エンドポイントは`https://rest.iad-01.braze.com` になります。<br><br>
- **ダッシュボード**<br>**Manage Settings** ページに移動し、SDK エンドポイントを見つけます。REST エンドポイントを取得するには、`sdk` を`rest` に置き換えます。たとえば、`sdk.iad-01.braze.com` と表示された場合、API URL は次のようになります `rest.iad-01.braze.com`

{% endtab %}
{% tab API Key %}

Braze サーバに接続するには、API キーが必要です。この一意の識別子により、Braze はID を検証し、データをアップロードできます。 

API キーを取得するには、**Settings** > **API Keys** に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Developer Console** > **API Settings** にAPI キーがあります。
{% endalert %}

`/users/track` エンドポイントに投稿する権限を持つAPI キーが必要になります。エンドポイントがサポートされているAPI キーがある場合は、そのキーを使用できます。 

新しいAPI キーを作成するには、**Create New API Key**をクリックします。次に、API キーに名前を付け、**User Data** endpoints group の下で**users.track** を選択し、**Save API Key** をクリックします。

{% endtab %}
{% endtabs %}

## 使用方法

##### 概要
1. AWS Serverless Application Repository からBraze の公開されている CSV 処理 Lambda をデプロイする
2. 新しく作成した S3 バケットのユーザー属性を持つ CSV ファイルを削除する
3. ユーザーは自動的にBrazeにインポートされます

#### デプロイ

ユーザー属性CSV ファイルの処理を開始するには、処理を処理するサーバーレスアプリケーションをデプロイする必要があります。このアプリケーションは、正常にデプロイするために次のリソースを自動的に作成します。

- Lambda関数
- Lambda プロセスが読み取ることができる CSV ファイルの S3 バケット (_注意: この Lambda 関数は `.csv` 拡張ファイル _ の通知のみを受け取ります)
- S3 バケットの作成を許可するロール
- 新しいバケットで Lambda が S3 アップロードイベントを受信できるようにするポリシー

[application](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import)への直接リンクをたどるか、[AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications)を開き、"braze-user-attribute-import"を検索します。このアプリケーションを表示するには、`Show apps that create custom IAM roles and resource policies` チェックボックスをオンにする必要があります。アプリケーションは、新しく作成された S3 バケットから読み取る lambda のポリシーを作成します。

**Deploy**をクリックし、AWS に必要なすべてのリソースを作成させます。

デプロイを監視し、[CloudFormation](https://console.aws.amazon.com/cloudformation/) でスタック(つまり、必要なすべてのリソース) が作成されていることを確認できます。"serverlessrepo-braze-user-attribute-import"という名前のスタックを見つけます。**Status** が`CREATE_COMPLETE` に変わった後、関数を使用する準備が整いました。スタックをクリックして**Resources** を開き、作成されるさまざまなリソースを確認できます。

以下のリソースが作成されました。

- [S3 バケット](https://s3.console.aws.amazon.com/s3/) - `braze-user-csv-import-aaa123` という名前のバケット。`aaa123` はランダムに生成された文字列です
- [Lambda 関数](https://console.aws.amazon.com/lambda/) \- lambda 関数名 `braze-user-attribute-import`
- [IAM Role](https://console.aws.amazon.com/iam/) - `braze-user-csv-import-BrazeUserCSVImportRole` という名前のポリシーで、ラムダをS3 から読み取り、関数の出力をログに記録できます

#### 実行

この関数を実行するには、新しく作成したS3バケットにあるユーザー属性CSVファイルを削除します。

## 監視とロギング

関数が正常に実行されるように、関数の実行ログを読み取ることができます。Braze User CSV Import 機能を開き(コンソールのLambdas のリストから選択)、**Monitor** に移動します。ここでは、関数の実行履歴を確認できます。出力を読み取るには、**CloudWatch**でログを表示をクリックします。チェックするラムダ実行イベントを選択します。

## 推定実行時間
_2048MB Lambda関数_

| 行数| 実行時間|
| --------- | ---------- |
| 10k | 3s         |
| 100k | 30s |
| 1M | 5 分 |
| 5M | 30 min |

## 既存の関数の更新

すでにアプリケーションをデプロイしており、リポジトリで新しいバージョンが利用可能な場合は、関数を初めて実行したかのように再デプロイすることで更新できます。つまり、Braze API Key およびBraze API URL を再度渡す必要があります。更新は、機能コードのみを上書きします。S3 バケットなどの既存のリソースは変更または削除されません。

## 致命的エラー

予期しないエラーが発生した場合、ファイルのその後の処理を妨げるイベントがログに記録されます ([Monitoring and Logging](#monitoring-and-logging) で説明されている CloudWatch を介してアクセス可能)。このイベントは、プログラムがファイルの処理を停止した時点から Lambda を再起動するために使用できます。データポイントを保存するために同じデータを再インポートしないことが重要です。これを行う手順は、[GitHub リポジトリ](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error) にあります。

{% alert important %}
[fatal errors](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)または[Lambda configuration](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration)の処理方法の詳細については、GitHub リポジトリを参照してください。
{% endalert%}