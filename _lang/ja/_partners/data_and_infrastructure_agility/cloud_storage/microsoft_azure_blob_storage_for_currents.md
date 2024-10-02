---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "この参考記事では、Braze Currentsと、非構造化データ用の大規模スケーラブルなオブジェクトストレージであるMicrosoft Azure Blog Storageとのパートナーシップについて概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storageは](https://azure.microsoft.com/en-us/services/storage/blobs/)、マイクロソフトがAzure製品群の一部として提供する、非構造化データ用の大規模スケーラブルなオブジェクトストレージである。

BrazeとMicrosoft Azure Blob Storageの統合により、データをAzureにエクスポートし、Currentsデータをストリーミングすることができる。その後、ETLプロセス（Extract、Transform、Load）を使ってデータを他の場所に転送することができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Microsoft AzureとAzureストレージアカウント | このパートナーシップを利用するには、Microsoft AzureとAzureストレージのアカウントが必要だ。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Microsoft Azure Blob Storageと統合するには、BrazeがデータをAzureにエクスポートバックするか、Currentsデータをストリーミングできるように、ストレージアカウントと接続文字列が必要である。

### ステップ1:ストレージアカウントを作成する

Microsoft Azureで、サイドバーの**Storage Accountsに**移動し、**\+ Addを**クリックして新しいストレージアカウントを作成する。次に、ストレージアカウント名を指定する。その他のデフォルト設定は更新する必要はない。最後に、**レビュー＋作成を**選択する。 

すでにストレージアカウントをお持ちの場合でも、Brazeのデータ専用に新規作成することをお勧めする。

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### ステップ2:接続文字列を取得する

ストレージアカウントがデプロイされたら、ストレージアカウントから**Access Keys**メニューに移動し、接続文字列をメモする。

マイクロソフトは2つのアクセスキーを提供し、一方のキーを使って接続を維持しながら、もう一方のキーを再生成する。必要なのはどちらか一方の接続文字列だけだ。

{% alert note %}
Brazeはキーではなく、このメニューの接続文字列を使用する。
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### ステップ 3:ブロブ・サービス・コンテナを作成する

ストレージアカウントの**Blob Service**セクションにある**Blobs**メニューに移動する。先ほど作成したストレージアカウント内にBlobサービスコンテナを作成する。 

Blobサービスコンテナの名前を指定する。その他のデフォルト設定は更新する必要はない。

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### ステップ 4:電流を設定する

Brazeで、**Currents > + Create Current > Azure Blob Data Exportに**移動し、統合名と連絡先のEメールを入力する。

次に、接続文字列、コンテナ名、BlobStorage接頭辞（オプション）を指定する。

![BrazeのMicrosoft Azure Blob storage Currentsページ。このページには、統合名、連絡先Eメール、接続文字列、コンテナ名、接頭辞のフィールドがある。]({% image_buster /assets/img/maz.png %})

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージ・エンゲージメント・イベントまたは顧客行動イベントを選択する。完了したら、カレントを起動する。

### ステップ 5: Azureデータエクスポートを設定する

以下は、クレデンシャルを設定するものである：
1. APIを通じてセグメントをエクスポートする
2. CSVエクスポート（キャンペーン、セグメント、キャンバスのユーザーデータをダッシュボード経由でエクスポートする）
3. エンゲージメントレポート

Brazeで、**Partner Integrations**>**Technology Partners**>**Microsoft Azureに**移動し、接続文字列、Azureストレージコンテナ名、Azureストレージ接頭辞を入力する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

次に、**Make this the default data export destination（これをデフォルトのデータ・エクスポート先にする**）ボックスがチェックされていることを確認する。完了したら、統合を保存する。

![BrazeのMicrosoft Azureデータエクスポートページ。このページには、接続文字列、コンテナ名、プレフィックスのフィールドがある。]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止する。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

## 輸出行動

クラウド・データ・ストレージ・ソリューションを統合し、API、ダッシュボード・レポート、またはCSVレポートをエクスポートしようとしているユーザーには、次のような問題が発生する：

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要がある。
- すべてのダッシュボード・レポートとCSVレポートは、ダウンロード用にユーザーのEメールに送信され（ストレージのパーミッションは不要）、データストレージにバックアップされる。 
