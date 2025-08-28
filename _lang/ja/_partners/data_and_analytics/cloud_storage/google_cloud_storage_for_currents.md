---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "このリファレンス記事では、Braze と Google Cloud Storage のパートナーシップについて説明します。Google Cloud Storage は、非構造化データのための大規模拡張可能オブジェクトストレージです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) は、Google が Cloud Computing 製品群の一部として提供する、非構造化データのための大規模拡張可能オブジェクトストレージソリューションです。

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Braze カスタマーサクセスマネージャーに連絡し、新しい統合の設定と検証について詳細なサポートをご依頼ください。
{% endalert %}

Braze と Google Cloud Storage の統合により、Currents データを Google Cloud Storage にストリーミングできます。その後、ETL プロセス (抽出、変換、読み込み) を使用して、データを Google BigQuery などの他の場所に転送できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Google Cloud Storage アカウント | このパートナーシップを活用するには、Google Cloud Storage アカウントが必要です。 |
| Currents | Google Cloud Storage にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Google Cloud Storage と統合するには、Braze が書き込み先のストレージバケット (`storage.buckets.get`) に関する情報を取得し、そのバケット (`storage.objects.create`) 内にオブジェクトを作成できるように、適切な認証情報を設定する必要があります。 

これを行うには次の手順に従います。この手順では、Currents 統合で使用する秘密キーを生成するロールとサービスアカウントを作成する手順を説明します。

### ステップ1:役割を作成する

[**IAM & admin**] > [**Roles**] > [**\+ Create Role**] に移動して、Google Cloud Platform Console に新しいロールを作成します。

![]({% image_buster /assets/img/gcs1.png %})

ロールに名前を付け、[**+Add Permissions**] を選択して、以下を選択します。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
`storage.objects.delete` 権限はオプションです。これにより Braze は不完全なファイルをクリーンアップすることができます。<br><br>まれに Google Cloud が接続を早期に終了し、Braze が Google Cloud Storage に不完全なファイルを書き込むことがあります。ほとんどの場合、Braze は再試行して、正しいデータで新しいファイルを作成し、古いファイルは Google Cloud Storage に残します。
{% endalert %}

完了したら、[**Create**] を選択します。

![]({% image_buster /assets/img/gcs2.png %})

### ステップ2: 新しいサービスアカウントを作成する

#### ステップ 2.1: サービスアカウントを作成する

[**IAM & admin**] > [**Service Accounts**] に移動し、[**Create Service Account**] を選択して、Google Cloud Platform Console で新しいサービスアカウントを作成します。

![]({% image_buster /assets/img/gcs3.png %})

次に、サービスアカウントに名前を付け、新しく作成したカスタムロールへのアクセス権を付与する。

![Google Cloud Platform のサービス作成ページで、「ロールを選択」するフィールドへのロール名の入力。]({% image_buster /assets/img/gcs4.png %})

#### ステップ 2.2: キーを作成する

ページ下部の「**Create Key**」ボタンで、Brazeで使用する**JSON**秘密鍵を作成する。キーが作成されると、あなたのマシンにダウンロードされる。

![]({% image_buster /assets/img/gcs5.png %})

### ステップ 3: Braze で Currents を設定する

Braze で [**Currents**] > [**\+ Current を作成**] > [**Google Cloud Storage データのエクスポート**] に移動し、統合名と連絡先メールを入力します。

次に [**GCS JSON 認証情報**] で JSON 秘密キーをアップロードし、GCS バケット名と GCS 接頭辞 (オプション) を指定します。 

{% alert important %}
認証情報ファイルを最新の状態に維持することが重要です。コネクターの認証情報の有効期限が切れると、コネクターはイベントの送信を停止します。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

![Braze の「Google Cloud Storage Currents」ページ。このページには、統合名、連絡先メール、GCS JSON 認証情報、GCS バケット名、接頭辞のフィールドがあります。]({% image_buster /assets/img/gcs6.png %})

最後に、ページの一番下までスクロールし、エクスポートしたいメッセージ・エンゲージメント・イベントまたは顧客行動イベントを選択する。完了したら、Current を起動します。

### ステップ 4: Google Cloud Storage のエクスポートの設定

Google Cloud Storage (GCS) エクスポートを設定するには、[**Technology Partners**] > [**Google Cloud Storage**] に移動し、GCS 認証情報を入力し、[**Make this the default data export destination**] を選択します。

エクスポートされたファイルの構成と内容は、AWS S3、Microsoft Azure、Google Cloud Storage の統合間で同一であることに留意します。

{% alert important %}
必ず、[Google Cloud で生成された](https://cloud.google.com/iam/docs/keys-create-delete) JSON の値をすべて入力してください。
{% endalert %}

![Braze ダッシュボードの Google Cloud Storage ページ。]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### ステップ 5: サービスアカウントの認証情報のテスト (オプション)

Google Cloud IAM サービスアカウントには必要な権限は以下のとおりです。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Braze ダッシュボードでこれらの権限を確認するには、[**Google Cloud Storage**] ページに移動して、[**認証情報のテスト**] を選択します。

![Braze ダッシュボードの Google Cloud Storage 認証情報セクション。]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## エクスポートの動作

クラウドデータストレージソリューションを統合しており、API、ダッシュボードレポート、または CSV レポートをエクスポートする場合、次のような状況が発生します。

- すべての API エクスポートでは、応答本文でダウンロード URL が返されないため、データストレージから取得する必要があります。
- すべてのダッシュボードレポートと CSV レポートは、ダウンロード用のメールでユーザーに送信され (保存権限は不要です)、Data Storage にバックアップされます。

## トラブルシューティング

### Google Cloud Storage の認証情報が無効である。

認証情報を入力しようとすると、以下のエラーが表示される

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Google Cloud IAM サービスアカウントに以下の権限があることを確認してください。

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

認証後に、[Braze ダッシュボードで認証情報をテスト](#step-5-test-your-service-account-credentials-optional)できます。
