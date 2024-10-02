---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "この参考記事では、Brazeと、非構造化データ用の大規模スケーラブルなオブジェクトストレージであるGoogle Cloud Storageとの提携について概説している。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storageは](https://cloud.google.com/storage/)、Googleがクラウドコンピューティング製品群の一部として提供する、非構造化データ用の大規模スケーラブルなオブジェクトストレージである。

BrazeとGoogle Cloud Storageの統合により、CurrentsのデータをGoogle Cloud Storageにストリーミングできる。後でETLプロセス（Extract、Transform、Load）を使って、Google BigQueryのような他の場所にデータを転送することができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| グーグル・クラウド・ストレージのアカウント | このパートナーシップを利用するには、グーグル・クラウド・ストレージのアカウントが必要だ。 |
| Currents | データをGoogle Cloud Storageにエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Google Cloud Storageと統合するには、Brazeが書き込み先のストレージバケット(`storage.buckets.get`)に関する情報を取得し、そのバケット(`storage.objects.create`)内にオブジェクトを作成できるように、適切な認証情報を設定する必要がある。 

これは、Currents統合で使用する秘密鍵を生成するロールとサービスアカウントを作成する手順を説明する、以下の手順を使用して行うことができる。

### ステップ1:役割を作成する

Google Cloud Platform Consoleで、**IAM & admin**>**Roles**>**\+ Create Roleと**進み、新しいロールを作成する。

![][2]

次に、ロールに名前を付け、**"+Add Permissions**"を選択し、以下を追加する：`storage.buckets.get` `storage.objects.create` と`storage.objects.get` を追加する。次に、**Createを**選択する。

オプションで、`storage.objects.delete` パーミッションを追加して、Brazeが不完全なファイルをクリーンアップできるようにする。まれに、Google Cloudが接続を早期に終了し、Brazeが不完全なファイルをGoogle Cloud Storageに書き込むことがある。通常の場合、Brazeは再試行し、正しいデータで新しいファイルを作成し、古いファイルはGoogle Cloud Storageに残す。

![][3]

### ステップ2:サービスアカウントを作成する

Google Cloud Platform Consoleで**IAM & admin**>**Service Accountsに**移動し、**Create Service Accountを**選択して新しいサービスアカウントを作成する。

![][4]

次に、サービスアカウントに名前を付け、新しく作成したカスタムロールへのアクセス権を付与する。

![Google Cloud Platformのcreate servicesページで、"Select a Role "フィールドにロールの名前を入力する。][5]

#### キーを作成する

ページ下部の「**Create Key**」ボタンで、Brazeで使用する**JSON**秘密鍵を作成する。キーが作成されると、あなたのマシンにダウンロードされる。

![][6]

### ステップ3:ブレイズで電流を設定する

Brazeで、**Currents**>**\+ Create Current**>**Google Cloud Storage Data Exportに**移動し、統合名と連絡先のEメールを入力する。

次に、**GCS JSON Credentialsに**JSON秘密鍵をアップロードし、CGSバケット名とGCSプレフィックス（オプション）を入力する。 

{% alert important %}
コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

![BrazeのGoogle Cloud Storage Currentsページ。このページには、インテグレーション名、コンタクトEメール、GCS JSONクレデンシャル、GCSバケット名、プレフィックスのフィールドがある。][7]

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージ・エンゲージメント・イベントまたは顧客行動イベントを選択する。完了したら、カレントを起動する。

### ステップ4:グーグル・クラウド・ストレージ（GCS）のエクスポートを設定する

Google Cloud Storage（GCS）エクスポートを設定するには、**Technology Partners**>**Google Cloud Storageに**進み、GCS認証情報を入力し、**Make this default data export destinationを**選択する。

{% alert tip %}
**GCS JSON クレデンシャルは**、[Google Cloud ドキュメントの](https://cloud.google.com/iam/docs/keys-create-delete)手順に従って生成される。必ず、生成されたJSON値全体を入力すること。
{% endalert %}

![BrazeダッシュボードのGoogle Cloud Storageページ。][8]{: style="max-width:70%;"}

対応するGoogle Cloud IAMサービスアカウントには、以下の権限が必要である（これは、Brazeの**Google Cloud Storage**ページで**Test Credentials**ボタンを選択することで確認できる）：
- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.get`
- `storage.objects.list`

エクスポートされたファイルの構成と内容は、AWS S3、Microsoft Azure、Google Cloud Storageの統合間で同一である。

## 輸出行動

クラウド・データ・ストレージ・ソリューションを統合し、API、ダッシュボード・レポート、またはCSVレポートをエクスポートしようとしているユーザーには、次のような問題が発生する：

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要がある。
- すべてのダッシュボード・レポートとCSVレポートは、ダウンロード用にユーザーのEメールに送信され（ストレージのパーミッションは不要）、データ・ストレージにバックアップされる。 

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
[8]: {% image_buster /assets/img/gcs7.png %}
