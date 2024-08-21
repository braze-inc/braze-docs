---
nav_title: ワークショップ
article_title: Amazon Personalize Workshop
alias: /partners/amazon_personalize_workshop/
description: "このリファレンス記事では、接続コンテンツを使用してAmazon Personalizeを設定し、それをBraze環境に統合する手順について説明します。"
page_type: partner
search_tag: Partner
---

# Amazon Personalize workshop

> このリファレンス記事では、Amazon Personalize を設定し、Connected Content を使用してBraze に統合する手順について説明します。これは、s をデプロイしてトレーニング Amazon Personalize ソリューションし、それらをBraze メール キャンペーンに統合するために必要なすべてのステップについて説明する実践的なワークショップを使用して行われます。

以下のサンプルは、Retail Demo Store と呼ばれる完全に機能するサンプルe コマースサイトにデプロイされます。このチュートリアルのリソースとコードは、[ AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) に公開されています。このリファレンスアーキテクチャインプリメンテーションをアウトラインとして使用して、独自の環境にAmazon Personalizeをインプリメントできます。

## 要件

[Retail Demo Store リポジトリ](https://github.com/aws-samples/retail-demo-store/) をクローンし、概要のステップに従ってワークショップ環境をAWS アカウントにデプロイする必要があります。ワークショップを完了し、インテグレーションコードを実行するには、AWS アカウントが必要です。

## 統合アーキテクチャ

ユーザー s にパーソナライズされたを送信するBrazeを設定するには、まず、例としてRetail Demo Store アーキテクチャを使用して、一般的なe コマース Web サイトに必要な関連コンポーネントを確認します。

![さまざまなコンポーネントが互いにどのように相互作用するかを示すBraze パーソナライゼーションアーキテクチャを分解する"画像。]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. リテールデモストアのWeb UI では、AWS Amplify JavaScript ライブラリーを使用して、トレーニングリングイベントをAmazon Personalize に送信します。
2. Braze キャンペーン ユーザーレコードは、グローバルストアユーザーから更新されます。
3. Braze キャンペーンの実行時に、接続コンテンツテンプレートを使用して、パーソナライズから推奨事項を取得し、対象ユーザーのメール テンプレートを入力します。
4. 推奨機種のトレーニングにも、商品カタログをご利用いただけます。

Braze は、ユーザープロファイルs の振る舞いまたは属性s に基づいてメールs をユーザーs に送信します。この情報は、ユーザーsを特定し、ユーザープロファイルsを構築するのに役立ち、いつメッセージまたはメールを送信するかを決定するのに役立ちます。

このイベントデータフローは、Amazon Personalize に送信される動作イベントデータと並行してh をアプリします。このワークショップでは、デモストアはAmplifyを使用してパーソナライズにイベントを送信します。このデータは、推奨モデルをトレーニングするために使用されます。このモデルは、Braze キャンペーンの実行時にコンテンツをパーソナライズしてユーザーにするためのBraze接続コンテンツ呼び出しで使用できます。

Braze接続コンテンツは、AWSで実行されているレコメンドサービスを介して、これらのレコメンドを取得できます。Retail Demo Store ワークショップには、推奨サービス展開の例が表示されます。独自のインフラのデプロイシナリオでは、同様のサービスをデプロイして、独自のカタログサービスから項目を取得する必要があります。

## リファレンスアーキテクチャワークショップのセットアップ

### ステップ1:AWS アカウントに小売デモストアをデプロイする

![使用可能なAWSリージョンの"画像。][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

次のテーブルでは、**AWS Region**を選択し、**Launch Stack**を選択します。このリストは、プロジェクトをデプロイできるすべての可能なリージョンを示すものではなく、Retail Demo Store でデプロイするために現在設定されているリージョンのみを表しています。

テンプレートのすべてのデフォルトパラメータを受け入れます。すべてのプロジェクトリソースのデプロイには、25 ～30 分かかります。

### ステップ2:ビルドAmazon Personalize キャンペーン

パーソナライズされたのプロダクト推奨事項を提供するには、まずマシンラーニングモデルをトレーニングし、Amazon Personalizeから推奨事項を得るための推論エンドポイントを提供する必要があります。ステップ 1 にデプロイされたCloudFormation テンプレートには、詳細なステップごとの手順を持つJupyter 以外のeBookを提供するAmazon SageMaker not eBook インスタンスが含まれています。

1. ステップ 1 でAWS CloudFormation テンプレートをデプロイしたAWS アカウントにサインインします。
2. Amazon SageMaker コンソールで、**Not eBook instances** を選択します。
3. **RetailDemoStore** not eBook インスタンスが表示されない場合は、ステップ 1 でプロジェクトをデプロイしたリージョンと同じリージョンにいることを確認します。
4. 非eBook インスタンスにアクセスするには、**Open Jupyter** または**Open JupyterLab** を選択します。
5. Jupyter ウェブインターフェイスにnot eBook インスタンスの読み込むed がある場合は、`workshop/1-Personalization/1.1-Personalize.ipynb` not eBookを選択します。eBookでないサブディレクトリを表示するには、`workshop` フォルダーを選択する必要があります。
6. `1.1-Personalize` がeBook 開封でない場合は、それぞれのセルを実行してワークショップをステップします。Jupyter ツールバーから**Run** を選択して、セル内のコードを順番に実行できます。未eBookの完了には、約2時間のアプリがかかります。

### ステップ3:Brazeからパーソナライズされた メールを送信

Amazon Personalize ソリューション s とキャンペーン s を使用すると、小売デモストアのインスタンスがメール キャンペーンに推奨事項を提供する準備が整います。ステップ 1 では、デモWeb アプリライセンスとすべての関連サービスをデプロイしました。これには、ステップ 2 でデプロイしたAmazon Personalize キャンペーンを使用するConnected Content を介してメール キャンペーン s をBraze と統合するために必要なレコメンドサービスが含まれます。

ステップ 2のパーソナライゼーションワークショップと同様に、次のBraze メッセージングワークショップでは、設定を使用してBrazeとAmazon Personalizeインテグレーションを設定します。

1. ステップ 1 でAWS CloudFormation テンプレートをデプロイしたAWS アカウントにサインインします。
2. Amazon SageMaker コンソールで、**Not eBook Instances**を選択します。
3. **RetailDemoStore** not eBook インスタンスが表示されない場合は、プロジェクトをデプロイしたのと同じAWS リージョンにいることを確認します。
4. 非eBook インスタンスにアクセスするには、**Open Jupyter** または**Open JupyterLab** を選択します。
5. Jupyter ウェブインターフェイスにnot eBook インスタンスの読み込むed がある場合は、`workshop/4-Messaging/4.2-Braze.ipynb` not eBookを選択します。eBookでないサブディレクトリを表示するには、`workshop` フォルダーを選択する必要があります。
6. `4.2-Braze` がeBook 開封でない場合は、それぞれのセルを実行してワークショップをステップします。Jupyter ツールバーから**Run** を選択して、セル内のコードを順番に実行できます。未eBookは、完了までに約1時間のアプリがかかります。

### ステップ4:リソースのクリーンアップ

将来の課金を回避するには、ステップ 1 で作成したAWS CloudFormation スタックを削除して作成したRetail Demo Store プロジェクトのAWS リソースを削除します。

[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}