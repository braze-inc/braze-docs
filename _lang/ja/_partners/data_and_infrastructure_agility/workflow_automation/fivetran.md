---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "このリファレンス記事では、BrazeとFivetranのパートナーシップについて説明しています。Fivetranは、クラウドウェアハウスにクエリ可能なデータを提供することで、データに基づいた意思決定を支援するワークフローオートメーションツールです。"
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) は、アナリストに焦点を当てた製品と完全に管理されたパイプラインにより、クラウドウェアハウスにクエリ可能なデータを提供することで、データに基づいた意思決定を可能にする世界的に認知されたブランドです。

BrazeとFivetranの統合により、すべてのアプリケーションとデータベースを中央のウェアハウスに接続することで、Brazeデータを収集および分析するためのメンテナンス不要のパイプラインを作成できます。データが中央倉庫に収集された後、データチームは好みのビジネスインテリジェンスツールを使用してBrazeデータを効果的に探索できます。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Fivetranアカウント | このパートナーシップを利用するには、[Fivetran](https://fivetran.com/login?next=%2Fdashboard)アカウントが必要です。 |
| Braze REST API キー | 次の権限を持つBraze REST APIキー:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>email.ハードバウンス<br>messages.スケジュール放送<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>purchases.製品リスト<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント  | あなたのRESTエンドポイントURL。エンドポイントは、[BrazeインスタンスのURL][1]によって異なります。 |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) は Amazon S3 または Google Cloud Storage のいずれかに接続する必要があります。 |
| Amazon S3 または Google Cloud Storage | この統合には、Amazon S3 または Google Cloud Storage へのアクセスが必要です。 |
{: .reset-td-br-1 .reset-td-br-2} 

## 統合

次のCurrents統合は、[Amazon S3](#setting-up-braze-currents-for-s3)および[Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage)の両方でサポートされています。

### S3のためのBraze Currentsの設定

#### ステップ1:外部ID {#step-one} を見つけてください

[Fivetran ダッシュボード](https://fivetran.com/dashboard)で、**\+ Connector**をクリックし、**Braze**コネクタを選択してセットアップフォームを起動します。次に、**Amazon S3**を選択します。ここに提供されたexternal IDに注意してください。FivetranがあなたのS3バケットにアクセスできるようにするために必要です。 

![FivetranのセットアップBrazeコネクタフォーム。このステップに必要なexternal IDフィールドは、ページの中央にある薄い灰色のボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### ステップ2:指定されたS3バケットへのアクセス権をFivetranに与える

##### IAMポリシーの作成

[Amazon IAM コンソール](https://console.aws.amazon.com/iam/home#home)を開封し、**ポリシー > ポリシーの作成**に移動します。

![]({% image_buster /assets/img/fivetran_as3_iam.png %})

次に、**JSON**タブをクリックして、次のポリシーを貼り付けます。`{your-bucket-name}` を S3 バケットの名前に置き換えてください。

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

最後に、**ポリシーを確認**をクリックし、ポリシーに一意の名前と説明を付けます。「ポリシーの作成」をクリックしてポリシーを作成します。 

![]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### IAMロールを作成する {#step-two}

AWS で、**ロール** に移動し、**新しいロールを作成** を選択します。

![]({% image_buster /assets/img/fivetran_iam_new_role.png %})

**別のAWSアカウント**を選択し、FivetranアカウントID`834469178297`を提供します。必ず**Require external ID**チェックボックスを確認してください。ここでは、ステップ1で見つかったexternal IDを提供します。

![]({% image_buster /assets/img/fivetran_another_aws_account.png %})

次に、**次をクリックします。権限**を選択して、作成したポリシーを選択します。

![]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

クリック **次へ:レビュー**、新しい役割に名前を付けます（例えば、Fivetran）、そして**役割を作成**をクリックします。ロールが作成された後、それをクリックして表示されるロールARNをメモします。

![ロールに記載されているAmazon S3 ARNです。]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Fivetran用に指定するロールARNの権限を指定できます。このロールに選択的な権限を与えることで、Fivetranは権限を持つもののみを同期できるようになります。
{% endalert %}

#### ステップ3:Fivetranコネクタを完了する

Fivetranで、**\+ Connector**をクリックし、**Braze**コネクタを選択してセットアップフォームを起動します。フォーム内で、指定されたフィールドに適切な値を入力してください:
- `Destination schema`:ユニークなスキーマ名。
- `API URL`:あなたのBraze REST APIエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `External ID`:Currentsセットアップ手順の[ステップ2](#step-two)で設定されたexternal ID。このIDは固定値です。
- `Bucket`:Brazeアカウントで見つかりました。**統合 > Currents > \[あなたのCurrent名] > バケット名**に移動します。
- `Role ARN`:現在のセットアップ手順の[ステップ1](#step-one)にロールARNが見つかります。

{% alert important %}
**Amazon S3** が **クラウドストレージ** の選択肢として選ばれていることを確認してください。
{% endalert %}

最後に、**保存してテスト**をクリックすると、FivetranがBrazeアカウントのデータと同期して残りの作業を行います！

### Google Cloud StorageのBraze Currentsの設定

#### ステップ1:Google Cloud Storage {#step-one2} から Fivetran メールを取得する

[Fivetranダッシュボード](https://fivetran.com/dashboard)で、**\+ Connector**をクリックし、**Braze**コネクタを選択してセットアップフォームを起動します。次に、**Google Cloud Storage**を選択します。表示されるメールアドレスに注意してください。

![FivetranのセットアップBrazeコネクタフォーム。このステップに必要なメールフィールドは、ページの中央にある薄い灰色のボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### ステップ2:バケットアクセスを許可する

[Google Storage Console](https://console.cloud.google.com/storage/browser) に移動し、Braze Currents で設定したバケットを選択して、**バケットの権限を編集** をクリックします。

![Googleストレージコンソールで利用可能なバケット。バケットを見つけて、縦の3点シンボルをクリックして、バケットの権限を編集できるドロップダウンを開きます。]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

次に、`Storage Object Viewer`に[ステップ1](#step-one2)のメールへのアクセス権を付与し、メールをメンバーとして追加します。バケット名をメモしておいてください。次のステップでFivetranを設定する必要があります。

![]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### ステップ 3:Fivetranコネクタを完了する

Fivetranで、**\+ Connector**をクリックし、**Braze**コネクタを選択してセットアップフォームを起動します。フォーム内で、指定されたフィールドに適切な値を入力してください:
- `Destination schema`:ユニークなスキーマ名。
- `API URL`:あなたのBraze REST APIエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `Bucket Name`:Brazeアカウントで見つかりました。**統合 > Currents > \[あなたのCurrent名] > バケット名**に移動します。
- `Folder`:Brazeアカウントで、**Integration > Currents > \[Your Current name] > Prefix**に移動して見つけることができます。

{% alert important %}
**Google Cloud Storage** が **Cloud Storage** の選択肢として選択されていることを確認してください。
{% endalert %}

最後に、**保存してテスト**をクリックすると、FivetranがBrazeアカウントのデータと同期して残りの作業を行います！

[1]: {{site.baseurl}}/api/basics/#api-definitions