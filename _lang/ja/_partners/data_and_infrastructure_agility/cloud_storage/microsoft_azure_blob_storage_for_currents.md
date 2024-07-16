---
nav_title: Microsoft Azure Blobストレージ
article_title:Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description:"この参考記事では、Braze Currentsと、非構造化データ用の大規模スケーラブルなオブジェクトストレージであるMicrosoft Azure Blog Storageとのパートナーシップについて概説している。"
page_type: partner
tool:Currents
search_tag:Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storageは](https://azure.microsoft.com/en-us/services/storage/blobs/)、マイクロソフトがAzure製品群の一部として提供する、非構造化データ用の大規模スケーラブルなオブジェクトストレージである。

BrazeとMicrosoft Azure Blob Storageの統合により、データをAzureにエクスポートしてCurrentsデータをストリーミングできる。その後、ETLプロセス（Extract、Transform、Load）を使ってデータを他の場所に転送することができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Microsoft AzureおよびAzureストレージアカウント | このパートナーシップを利用するには、Microsoft AzureとAzureストレージのアカウントが必要だ。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Microsoft Azure Blob Storageと統合するには、BrazeがデータをAzureにエクスポートバックするか、Currentsデータをストリーミングできるように、ストレージアカウントと接続文字列が必要である。

### ステップ1:ストレージアカウントを作成する

Microsoft Azureで、サイドバーの**Storage Accountsに**移動し、**\+ Addを**クリックして新しいストレージアカウントを作成する。次に、ストレージアカウント名を指定する。その他のデフォルト設定は更新する必要はない。最後に、**レビュー＋**作成を選択する。 

すでにストレージアカウントをお持ちの場合でも、Brazeデータ専用に新規作成することをお勧めする。

![\]({% image_buster /assets/img/azure-currents-step-1.png %})

### ステップ2:接続文字列を取得する

ストレージアカウントがデプロイされたら、ストレージアカウントから**Access Keys**メニューに移動し、接続文字列をメモする。

マイクロソフトは2つのアクセスキーを提供し、一方のキーを使って接続を維持しながら、もう一方のキーを再生成する。必要なのはどちらか一方の接続文字列だけだ。

{% alert note %}
Brazeはキーではなく、このメニューの接続文字列を使用する。
{% endalert %}

![\]({% image_buster /assets/img/azure-currents-step-2.png %})

### ステップ3:ブロブ・サービス・コンテナを作成する

ストレージアカウントの**Blob Service**セクションにある**Blobs**メニューに移動する。先ほど作成したストレージアカウント内にBlobサービスコンテナを作成する。 

Blobサービスコンテナの名前を指定する。その他のデフォルト設定は更新する必要はない。

![\]({% image_buster /assets/img/azure-currents-step-3.png %})

### ステップ 4:カレントを設定する

Brazeで、**Currents > + Create Currents > Azure Blob Data Exportに**移動し、統合名と連絡先メールを入力する。

次に、接続文字列、コンテナ名、BlobStorage接頭辞（オプション）を指定する。

![The Microsoft Azure Blob storage Currents page in Braze. On this page exist fields for integration name, contact email, connection string, container name, and prefix.]({% image_buster /assets/img/maz.png %})

最後に、ページを一番下までスクロールし、エクスポートしたいメッセージエンゲージメントイベントまたはカスタマー行動イベントを選択する。完了したら、Currentsを起動する。

### ステップ 5: Azureデータエクスポートの設定

以下は、認証情報の設定である：
1. APIを通じたセグメンテーション・エクスポート
2. CSVエクスポート（ダッシュボード経由でのキャンペーン、セグメンテーション、ユーザーデータのエクスポート）
3. エンゲージメントレポート

Brazeで、**Partner Integrations**>**Technology Partners**>**Microsoft Azureに**移動し、接続文字列、Azureストレージコンテナ名、Azureストレージ接頭辞を入力する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

次に、**Make this the default data export destination**（**これをデフォルトのデータエクスポート先に**する）ボックスがチェックされていることを確認する。完了したら、統合を保存する。

![The Microsoft Azure data export page in Braze. On this page exist fields for connection string, container name, and prefix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
's important to keep your connection string up to date; if your connector'の認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

## 輸出行動

クラウドデータストレージソリューションを統合し、API、ダッシュボードレポート、またはCSVレポートをエクスポートしようとしているユーザーには、次のような問題が発生する：

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要がある。
- すべてのダッシュボード・レポートとCSVレポートは、ユーザーのメールに送信されてダウンロードされ（保存権限不要）、ユーザー・データ・ストレージにバックアップされる。 
