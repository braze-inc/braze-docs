---
nav_title: ワークショップ
article_title:Amazon Personalize Workshop
alias: /partners/amazon_personalize_workshop/
description:この記事では、Amazon Personalize を設定し、Connected Content を使用して Braze 環境に統合するプロセスについて説明します。
page_type: partner
search_tag:Partner
---

# Amazon Personalize workshop

> この記事では、Amazon Personalizeを設定し、Connected Contentを使用してBraze環境に統合するプロセスについて説明します。これは、Amazon Personalize ソリューションをデプロイおよびトレーニングし、それらを Braze のメールキャンペーンに統合するために必要なすべての手順を実行するハンズオンワークショップを使用して行われます。

次の例は、Retail Demo Store という完全に機能する例のeコマースサイトに展開されています。このチュートリアルのリソースとコードは[AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/)に公開されています。このリファレンスアーキテクチャの実装を使用して、Amazon Personalizeを独自の環境に実装するためのアウトラインとして使用できます。

## 要件

ワークショップ環境をAWSアカウントにデプロイするために、[Retail Demo Storeリポジトリ](https://github.com/aws-samples/retail-demo-store/)をクローンし、記載されている手順に従う必要があります。ワークショップを完了し、統合コードを実行するには、AWSアカウントが必要です。

## 統合アーキテクチャ

Brazeを設定してユーザーにパーソナライズされたメッセージを送信する前に、Retail Demo Storeのアーキテクチャを例として使用して、一般的なeコマースウェブサイトに必要な関連コンポーネントを確認してください。

![An image breaking down the Braze personalization architecture noting how the different components interact with one another.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. 小売デモストアのWeb UIは、AWS Amplify JavaScriptライブラリを使用してトレーニングイベントをAmazon Personalizeに送信します。
2. Brazeキャンペーンユーザーの記録は、グローバルストアユーザーサービスから更新されます。
3. Brazeキャンペーンが実行されると、Connected Contentテンプレートが使用され、Personalizeからの推奨事項が取得され、ターゲットユーザーのメールテンプレートに入力されます。
4. 製品カタログ情報は、レコメンデーションモデルのトレーニングにも使用できます。

Brazeは、ユーザーの行動やユーザープロファイルの属性に基づいて、ユーザーにメールを送信します。このデータはユーザーを特定し、メッセージやメールを送信するタイミングを決定するのに役立つユーザープロファイルを構築するのに役立ちます。

このイベントデータフローは、Amazon Personalizeに送信される行動イベントデータと並行して発生します。このワークショップでは、デモストアはAmplifyを使用してイベントをPersonalizeに送信します。このデータは、Brazeキャンペーンが実行されるときに、Braze Connected Contentコールでコンテンツをユーザーにパーソナライズするために使用できるレコメンデーションモデルをトレーニングするために使用されます。

Braze Connected Contentは、AWSで実行されているレコメンデーションサービスを介してこれらのレコメンデーションを取得できるようになります。小売デモストアワークショップは、例の推薦サービスの展開を示しています。独自のインフラストラクチャでのデプロイメントシナリオでは、独自のカタログサービスからアイテムを取得するために同様のサービスをデプロイする必要があります。

## リファレンスアーキテクチャワークショップの設定

### ステップ1:AWSアカウントにリテールデモストアをデプロイする

![利用可能なAWSリージョンの画像。][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

次の表で、**AWSリージョン**を選択し、**スタックの起動**を選択します。このリストは、プロジェクトを展開できるすべての可能な地域を表しているわけではなく、Retail Demo Storeで展開するために現在設定されている地域のみを示しています。

テンプレートのデフォルトパラメータ値をすべて受け入れます。すべてのプロジェクトリソースの展開には25〜30分かかります。

### ステップ2:Amazon Personalizeキャンペーンを構築する

パーソナライズされた製品の推奨を提供する前に、まず機械学習モデルをトレーニングし、Amazon Personalizeから推奨を取得できる推論エンドポイントを提供する必要があります。ステップ1でデプロイされたCloudFormationテンプレートには、詳細なステップバイステップの指示が記載されたJupyterノートブックを提供するAmazon SageMakerノートブックインスタンスが含まれています。

1. ステップ1でAWS CloudFormationテンプレートをデプロイしたAWSアカウントにサインインします。
2. Amazon SageMaker コンソールで、**ノートブックインスタンス** を選択します。
3. プロジェクトをステップ1でデプロイしたのと同じリージョンにいることを確認してください。**RetailDemoStore**ノートブックインスタンスが表示されない場合。
4. ノートブックインスタンスにアクセスするには、**Jupyterを開く**または**JupyterLabを開く**を選択します。
5. Jupyterウェブインターフェイスがノートブックインスタンスにロードされたら、`workshop/1-Personalization/1.1-Personalize.ipynb`ノートブックを選択します。ノートブックのサブディレクトリを表示するには、`workshop`フォルダを選択する必要があるかもしれません。
6. ノートブックを開いたら、各セルを実行してワークショップを進めてください。Jupyterツールバーから**実行**を選択して、セル内のコードを順次実行できます。ノートブックの完了には約2時間かかります。

### ステップ3:Brazeからパーソナライズされたメールを送信する

Amazon Personalizeのソリューションとキャンペーンが整った状態で、Retail Demo Storeのインスタンスはメールキャンペーンに推奨を提供する準備ができています。ステップ1では、デモのWebアプリケーションと、BrazeとConnected Contentを通じてメールキャンペーンを統合するために必要なレコメンデーションサービスを含むすべての関連サービスをデプロイしました。これには、ステップ2でデプロイしたAmazon Personalizeキャンペーンが使用されます。

ステップ2のパーソナライゼーションワークショップと同様に、次のBrazeメッセージングワークショップでは、BrazeとAmazon Personalizeの統合設定を段階的に説明します。

1. ステップ1でAWS CloudFormationテンプレートをデプロイしたAWSアカウントにサインインします。
2. Amazon SageMaker コンソールで、**Notebook Instances** を選択します。
3. プロジェクトをデプロイしたのと同じAWSリージョンにいることを確認してください。**RetailDemoStore**ノートブックインスタンスが表示されない場合。
4. ノートブックインスタンスにアクセスするには、**Jupyterを開く**または**JupyterLabを開く**を選択します。
5. Jupyterウェブインターフェイスがノートブックインスタンスにロードされたら、`workshop/4-Messaging/4.2-Braze.ipynb`ノートブックを選択します。ノートブックのサブディレクトリを表示するには、`workshop`フォルダを選択する必要があるかもしれません。
6. ノートブックを開いたら、各セルを実行してワークショップを進めてください。Jupyterツールバーから**実行**を選択して、セル内のコードを順次実行できます。ノートブックの完了には約1時間かかります。

### ステップ 4:リソースをクリーンアップする

将来の料金が発生しないようにするには、ステップ1で作成したAWS CloudFormationスタックを削除して、Retail Demo Storeプロジェクトが作成したAWSリソースを削除します。

[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}