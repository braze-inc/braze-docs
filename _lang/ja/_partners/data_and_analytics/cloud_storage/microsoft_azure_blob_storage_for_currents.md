---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "このリファレンス記事では、Braze Currents と Microsoft Azure Blog Storage のパートナーシップについて説明します。Microsoft Azure Blog Storage は、非構造化データのための大規模拡張可能オブジェクトストレージです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) は、Microsoft が Azure 製品群の一部として提供する、非構造化データのための大規模拡張可能オブジェクトストレージです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Braze カスタマーサクセスマネージャーに連絡し、新しい統合の設定と検証について詳細なサポートをご依頼ください。
{% endalert %}

Braze と Microsoft Azure Blob Storage の統合により、データを Azure にエクスポートし、Currents データをストリーミングすることができます。その後、ETL プロセス (抽出、変換、読み込み) を使用してデータを他の場所に転送できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Microsoft AzureとAzureストレージアカウント | このパートナーシップを利用するには、Microsoft Azure と Azure ストレージアカウントが必要です。 |
| Currents | Currents にデータをエクスポートするには、アカウントに対して [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定しておく必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Microsoft Azure Blob Storage と統合するには、Braze がデータを Azure にエクスポートするか、Currents データをストリーミングするためのストレージアカウントと接続文字列を用意しておく必要があります。

### ステップ1:ストレージアカウントを作成する

Microsoft Azure で、サイドバーの [**Storage Accounts**] に移動し、[**\+ Add**] をクリックして新しいストレージアカウントを作成します。次に、ストレージアカウント名を指定する。その他のデフォルト設定は更新する必要はない。最後に [**Review + create**] を選択します。 

すでにストレージアカウントをお持ちの場合でも、Braze データ専用にストレージアカウントを新規作成することをお勧めします。

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### ステップ2:接続文字列を取得する

ストレージアカウントが準備できたら、ストレージアカウントから [**Access Keys**] メニューに移動し、接続文字列を書きとめておきます。

Microsoft は2つのアクセスキーを提供しています。1つのキーを再生成する際に、もう1つのキーを使用して接続を維持します。必要なのはどちらか一方の接続文字列だけだ。

{% alert note %}
Brazeはキーではなく、このメニューの接続文字列を使用する。
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### ステップ3:Blob サービスコンテナーを作成する

ストレージアカウントの**Blob Service**セクションにある**Blobs**メニューに移動する。先ほど作成したストレージアカウント内にBlobサービスコンテナを作成する。 

Blobサービスコンテナの名前を指定する。その他のデフォルト設定は更新する必要はない。

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### ステップ4:Currents を設定する

Brazeで **[Currents] > [+ Current を作成] > [Azure Blob データエクスポート]** に移動し、統合名と連絡先のメールを入力します。

次に、接続文字列、コンテナー名、BlobStorage 接頭辞 (オプション) を指定します。

![Braze の Microsoft Azure Blob ストレージ Currents のページ。このページには、統合名、連絡先メール、接続文字列、コンテナー名、接頭辞のフィールドがある。]({% image_buster /assets/img/maz.png %})

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージ・エンゲージメント・イベントまたは顧客行動イベントを選択する。完了したら、Current を起動します。

### ステップ 5: Azureデータエクスポートを設定する

次の目的で使用する認証情報を設定する手順を以下で説明します。
1. APIを通じてセグメントをエクスポートする
2. CSVエクスポート（キャンペーン、セグメント、キャンバスのユーザーデータをダッシュボード経由でエクスポートする）
3. エンゲージメントレポート

Braze で [**パートナー連携**] >[**テクノロジーパートナー**] > [**Microsoft Azure**] に移動し、接続文字列、Azure ストレージコンテナー名、Azure ストレージ接頭辞を入力します。

次に、[**これをデフォルトのデータエクスポート先にする**] ボックスがオンになっていることを確認します。これにより、エクスポートしたデータが確実に Azure に送信されます。完了したら、統合を保存する。

![BrazeのMicrosoft Azureデータエクスポートページ。このページには、接続文字列、コンテナー名、接頭辞のフィールドがある。]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
接続文字列を最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

## エクスポートの動作

クラウドデータストレージソリューションを統合しており、API、ダッシュボードレポート、または CSV レポートをエクスポートする場合、次のような状況が発生します。

- すべての API エクスポートでは、応答本文でダウンロード URL が返されないため、データストレージから取得する必要があります。
- すべてのダッシュボード・レポートとCSVレポートは、ダウンロード用にユーザーのEメールに送信され（ストレージのパーミッションは不要）、データストレージにバックアップされる。 
