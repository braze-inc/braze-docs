---
nav_title: ユーザー属性CSVラムダプロセス
permalink: /user_csv_lambda/
description: "以下の記事では、ユーザー追跡 Braze エンドポイントを通じて CSV ファイルからユーザー属性データを直接 Braze にポストする Lambda プロセスを簡単にデプロイできるサーバーレスアプリケーションを紹介しています。"
hidden: true
---

# ユーザー属性CSVをBrazeにインポートする

> 以下の記事では、[ユーザー追跡エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を通じて CSV ファイルからユーザー属性データを直接 Braze にポストする Lambda プロセスを簡単にデプロイできるサーバーレスアプリケーションを紹介しています。このアプリケーションの統合は、我々の Amperity パートナーによってテストされ、[GitHub](https://github.com/braze-inc/growth-shares-lambda-user-csv-import) で確認できます。

このプロセスは、設定された AWS S3 バケットに CSV ファイルをアップロードすると即座に起動します。大きなファイルやアップロードを扱うことができますが、Lambda の時間制限により、関数は10分後に実行を停止します。このプロセスは、ファイルの残りの部分を処理するために、別の Lambda インスタンスを起動します。ファンクションのタイミングについての詳細は、[推定実行](#estimated-execution-times)時間をチェックしてほしい。

{% alert important %}
このアプリケーションは Braze Growth 部門によって構築および保守されています。このアプリケーションの制作者に連絡を取りたい場合は、発生する可能性のあるフィードバックや問題について、[GitHub issue](https://github.com/braze-inc/growth-shares-lambda-user-csv-import/issues) を作成してください。
{% endalert %}

#### CSVユーザー属性

更新されるユーザー属性は、次の `.csv` 形式である必要があります。

```
external_id,attr_1,...,attr_n
userID,value_1,...,value_n
```

最初の列には更新するユーザーの外部 ID を指定し、次の列には属性名と値を指定する必要があります。指定する属性の数は異なる場合があります。処理するCSVファイルがこのフォーマットに従っていない場合、この関数は失敗する。  

**CSVファイルの例：**

```
external_id,Loyalty Points,Last Brand Purchased
abc123,1982,Solomon
def456,578,Hunter-Hayes
```

#### CSV処理

配列に含まれる値（例：`"['Value1', 'Value2']"` ）は自動的に構造化解除され、配列の文字列表現ではなく、配列でAPIに送信される。

## 要件

この Lambda 関数を正常に実行するには、次のものが必要です。
- S3とLambdaサービスを利用するための**AWSアカウント**
- Braze サーバーに接続するための **Braze API URL**
- `/users/track` エンドポイントにリクエストを送信できるようにするための**Braze API キー**
- 更新するユーザーの外部IDと属性を含む**CSVファイル**

{% tabs %}
{% tab API URL %}

API URL、または REST エンドポイントは、Braze API ドキュメントおよびダッシュボードにあります。

- **API ドキュメント**<br>[APIドキュメントに従って]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)、BrazeインスタンスURLをRESTエンドポイントURLに一致させるだけでよい。例えば、ダッシュボードに`dashboard-01.braze.com/` URLが表示されている場合、RESTエンドポイントは`https://rest.iad-01.braze.com` 。<br><br>
- **ダッシュボード**<br>\[**設定の管理**] ページに移動し SDK エンドポイントを見つけます。`sdk` を `rest` に置き換えて、REST エンドポイントを取得します。例えば、`sdk.iad-01.braze.com` と表示された場合、APIのURLは次のようになる。 `rest.iad-01.braze.com`

{% endtab %}
{% tab APIキー %}

Brazeサーバーに接続するには、APIキーが必要である。この一意の識別子により、Brazeはあなたの身元を確認し、データをアップロードすることができる。 

APIキーを取得するには、**「設定」**>「**APIキー**」を選択する。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、\[**開発者コンソール**] > \[**API 設定**] に API キーがあります。
{% endalert %}

`/users/track` エンドポイントに投稿する権限を持つ API キーが必要です。APIキーの1つがそのエンドポイントをサポートしていることが分かっていれば、そのキーを使うことができる。 

新しいものを作成する場合は、\[**新規 API キー作成**] をクリックします。次に、API キーに名前を付け、\[**ユーザーデータ**] エンドポイントグループの下の \[**users.track**] を選択し、\[**API キーの保存**] をクリックします。

{% endtab %}
{% endtabs %}

## 使用上の注意

##### 概要
1. AWSサーバーレスアプリケーションリポジトリからBrazeの一般公開されているCSV処理Lambdaをデプロイする
2. 新しく作成したS3バケットに、ユーザー属性のCSVファイルをドロップする
3. ユーザーは自動的にBrazeにインポートされる

#### デプロイする

ユーザー属性 CSV ファイルの処理を開始するには、処理を自動的に行うサーバーレスアプリケーションをデプロイする必要があります。このアプリケーションは、デプロイを成功させるために以下のリソースを自動的に作成する：

- ラムダ関数
- Lambdaプロセスが読み込み可能なCSVファイル用のS3バケット_（注意：このLambda関数は、`.csv` 拡張子ファイルの通知のみを受け取る）_
- S3 バケットの作成を許可するロール
- Lambdaが新しいバケットでS3のアップロードイベントを受け取ることを許可するポリシー

[アプリケーション](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:585170621372:applications/braze-user-attribute-import)への直接リンクをたどるか、[AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications) を開いて「braze-user-attribute-import」を検索します。なお、このアプリケーションを表示するには、`Show apps that create custom IAM roles and resource policies` のチェックボックスをオンにしなければなりません。アプリケーションは、ラムダが新しく作成されたS3バケットから読み込むためのポリシーを作成する。

\[**デプロイ**] をクリックし、AWS に必要なリソースをすべて作成させます。

デプロイを監視し、[CloudFormation](https://console.aws.amazon.com/cloudformation/) 内にスタック (つまり、必要なすべてのリソース) が作成されていることを確認できます。serverlessrepo-braze-user-attribute-import」というスタックを見つける。**ステータス**が `CREATE_COMPLETE` に変わったら、その機能は使用可能です。スタックをクリックして**「リソース」を**開き、さまざまなリソースが作成されるのを見ることができる。

以下のリソースが作成された：

- [S3バケット](https://s3.console.aws.amazon.com/s3/)-`braze-user-csv-import-aaa123` という名前のバケット。`aaa123` はランダムに生成された文字列である。
- [Lambda 関数](https://console.aws.amazon.com/lambda/)- `braze-user-attribute-import` という名前の Lambda 関数
- [IAM ロール](https://console.aws.amazon.com/iam/)\- Lambda が S3 から読み取りを行い、関数出力をログに記録することを許可する `braze-user-csv-import-BrazeUserCSVImportRole` という名前のポリシー

#### 実行

この機能を実行するには、新しく作成したS3バケットにユーザー属性CSVファイルをドロップする。

## モニタリングとロギング

関数が正常に実行されていることを確認するには、関数の実行ログを読めばいい。Braze ユーザー CSV インポート関数を開き (コンソールの Lambda リストから選択)、\[**Monitor**] に移動します。ここでは、その関数の実行履歴を見ることができる。出力を読み取るには、\[**CloudWatch でログを表示**] をクリックします。チェックしたいラムダ実行イベントを選択する。

## 推定実行時間
_2048 MB ラムダ関数_

| 行数 | 実行時間 |
| --------- | ---------- |
| 10k       | 3s         |
| 100k      | 30s        |
| 1M        | 5分      |
| 5M        | 30分     |

## 既存の関数を更新する

すでにアプリケーションをデプロイしていて、新しいバージョンがリポジトリにある場合は、初めてデプロイするのと同じように、機能を再デプロイすることでアップデートできる。つまり、Braze API キーと Braze API URL を再度渡す必要があります。アップデートはファンクションコードを上書きするだけだ。S3 バケットなどの他の既存のリソースを変更または削除することはありません。

## 致命的なエラー

ファイルのさらなる処理を妨げる予期しないエラーが発生した場合は、プログラムがファイルの処理を停止したポイントから Lambda を再起動するために使用できるイベントがログに記録されます (「[モニタリングとロギング](#monitoring-and-logging)」で説明されている CloudWatch からアクセス可能)。データ・ポイントを保存するために、同じデータを再インポートしないことが重要である。これを行う手順については、[GitHub リポジトリ](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)を参照してください。

{% alert important %}
[致命的なエラー](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#fatal-error)や [Lambda 設定](https://github.com/braze-inc/growth-shares-lambda-user-csv-import#lambda-configuration)の処理方法について詳しくは、GitHub リポジトリを参照してください。
{% endalert%}