---
nav_title: ワークショップ
article_title: Amazon Personalize Workshop
alias: /partners/amazon_personalize_workshop/
description: "このリファレンス記事では、接続コンテンツを使用してAmazon Personalizeを設定し、それをBraze環境に統合する手順について説明します。"
page_type: partner
search_tag: Partner
---

# Amazon Personalize workshop

> このリファレンス記事では、コネクテッドコンテンツを使用して Amazon Personalize を設定し、Braze 環境に統合するプロセスについて説明します。これは、s をデプロイしてトレーニング Amazon Personalize ソリューションし、それらをBraze メール キャンペーンに統合するために必要なすべてのステップについて説明する実践的なワークショップを使用して行われます。

_この統合は Amazon Personalize によって管理されます。_

## 統合について

以下の例は、リテールデモストアという名前の、機能を完備したサンプル e コマースサイトに展開されています。このチュートリアルのリソースとコードは、[ AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) に公開されています。このリファレンスアーキテクチャインプリメンテーションをアウトラインとして使用して、独自の環境にAmazon Personalizeをインプリメントできます。

## 要件

[Retail Demo Store リポジトリ](https://github.com/aws-samples/retail-demo-store/) をクローンし、概要のステップに従ってワークショップ環境をAWS アカウントにデプロイする必要があります。ワークショップを完了し、インテグレーションコードを実行するには、AWS アカウントが必要です。

## 統合アーキテクチャ

Braze でユーザーにパーソナライズされたメッセージの送信を設定する前に、リテールデモストアのアーキテクチャを例にして、一般的な e コマース Web サイトに必要な関連コンポーネントを確認します。

![さまざまなコンポーネントの相互作用を示すBraze パーソナライゼーションアーキテクチャの分解図。]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. リテールデモストアのWeb UI では、AWS Amplify JavaScript ライブラリーを使用して、トレーニングリングイベントをAmazon Personalize に送信します。
2. Braze キャンペーンユーザーレコードは、Global Store User サービスから更新されます。
3. Braze キャンペーンの実行時に、コネクテッドコンテンツテンプレートを使用して、Personalize からレコメンデーションを取得し、ターゲットユーザーのメールテンプレートを入力します。
4. 推奨機種のトレーニングにも、商品カタログをご利用いただけます。

Braze は、ユーザープロファイルの行動または属性に基づいてユーザーにメールを送信します。このデータは、ユーザーを識別し、ユーザープロファイルを作成して、メッセージまたはメールを送信するタイミングかを決定するのに役立ちます。

このイベントデータフローは、Amazon Personalize に送信される行動イベントデータと並行して発生します。このワークショップでは、デモストアで Amplify を使用して Personalize にイベントを送信します。このデータは、レコメンデーションモデルのトレーニングに使用されます。その後レコメンデーションモデルは、Braze キャンペーンの実行時にユーザーに対してコンテンツをパーソナライズするための Braze コネクテッドコンテンツ呼び出しで使用できます。

Braze コネクテッドコンテンツは、AWS で実行されているレコメンデーションサービスからこれらのレコメンドを取得できます。Retail Demo Store ワークショップでは、レコメンデーションサービスの導入の例が示されます。独自のインフラのデプロイシナリオでは、同様のサービスをデプロイして、独自のカタログサービスから項目を取得する必要があります。

## リファレンスアーキテクチャワークショップのセットアップ

### ステップ1:AWS アカウントに Retail Demo Store をデプロイする

![使用可能な AWS リージョンの画像。]({% image_buster /assets/img/amazon_personalize/region.png %}){: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

次の表で [**AWS Region**] を選択し、[**Launch Stack**] を選択します。このリストは、プロジェクトをデプロイできるすべてのリージョンを示すものではなく、Retail Demo Store のデプロイのために現在設定されているリージョンのみを示しています。

テンプレートのすべてのデフォルトパラメータを受け入れます。すべてのプロジェクトリソースのデプロイには25～30分かかります。

### ステップ2:ビルドAmazon Personalize キャンペーン

パーソナライズされたのプロダクト推奨事項を提供するには、まずマシンラーニングモデルをトレーニングし、Amazon Personalizeから推奨事項を得るための推論エンドポイントを提供する必要があります。ステップ1でデプロイされた CloudFormation テンプレートには、詳細な手順を含む Jupyter ノートブックを提供する Amazon SageMaker ノートブックインスタンスが含まれています。

1. ステップ 1 でAWS CloudFormation テンプレートをデプロイしたAWS アカウントにサインインします。
2. Amazon SageMaker コンソールで [**Notebook instances**] を選択します。
3. **RetailDemoStore** ノートブックインスタンスが表示されない場合は、ステップ1でプロジェクトをデプロイしたリージョンと同じリージョンにいることを確認してください。
4. ノートブックインスタンスにアクセスするには、[**Open Jupyter**] または [**Open JupyterLab**] を選択します。
5. Jupyter Web インターフェイスがノートブックインスタンスに読み込まれたら、`workshop/1-Personalization/1.1-Personalize.ipynb` ノートブックを選択します。ノートブックのサブディレクトリを表示するには、`workshop` フォルダーを選択する必要があります。
6. `1.1-Personalize` ノートブックが開いている場合は、各セルを実行してワークショップを順に実行します。Jupyter ツールバーから**Run** を選択して、セル内のコードを順番に実行できます。ノートブックが完了するまでには約2時間かかります。

### ステップ3:Braze からパーソナライズされたメールを送信する

Amazon Personalize ソリューションとキャンペーンを導入することで、Retail Demo Store のインスタンスがメールキャンペーンにレコメンデーションを提供できるようになります。ステップ1では、デモ Web アプリケーションとすべての関連サービスをデプロイしました。これには、コネクテッドコンテンツを介して Braze とメールキャンペーンを統合するために必要なレコメンデーションサービスが含まれています。これは、ステップ2でデプロイした Amazon Personalize キャンペーンを使用します。

ステップ 2のパーソナライゼーションワークショップと同様に、次のBraze メッセージングワークショップでは、設定を使用してBrazeとAmazon Personalizeインテグレーションを設定します。

1. ステップ 1 でAWS CloudFormation テンプレートをデプロイしたAWS アカウントにサインインします。
2. Amazon SageMaker コンソールで [**Notebook instances**] を選択します。
3. **RetailDemoStore** ノートブックインスタンスが表示されない場合は、ステップ1でプロジェクトをデプロイした AWS リージョンと同じリージョンにいることを確認してください。
4. ノートブックインスタンスにアクセスするには、[**Open Jupyter**] または [**Open JupyterLab**] を選択します。
5. Jupyter Web インターフェイスがノートブックインスタンスに読み込まれたら、`workshop/4-Messaging/4.2-Braze.ipynb` ノートブックを選択します。ノートブックのサブディレクトリを表示するには、`workshop` フォルダーを選択する必要があります。
6. `4.2-Braze` ノートブックが開いている場合は、各セルを実行してワークショップを順に実行します。Jupyter ツールバーから**Run** を選択して、セル内のコードを順番に実行できます。ノートブックが完了するまでには約1時間かかります。

### ステップ4:リソースのクリーンアップ

今後料金が発生しないようにするため、作成した Retail Demo Store プロジェクトの AWS リソースを削除します。このためには、ステップ1で作成した AWS CloudFormation スタックを削除します。


