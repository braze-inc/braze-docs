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

> [Fivetran](https://fivetran.com/) は世界的に認知されたブランドであり、アナリストに焦点を当てた製品と完全に管理されたパイプラインにより、クエリ可能なデータをクラウドウェアハウスに配信してデータに基づく意思決定を可能にします。

Braze とFivetran の統合により、ユーザーはメンテナンス不要のパイプラインを作成できます。このパイプラインにより、すべてのアプリケーションとデータベースを中央のウェアハウスに接続することで、Braze データを収集、分析できます。中央ウェアハウスにデータが収集されると、データチームは好きなビジネスインテリジェンスツールを使って、Braze のデータを効率的に調査できます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Fivetranアカウント | このパートナーシップを利用するには、[Fivetran](https://fivetran.com/login?next=%2Fdashboard)アカウントが必要です。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー：<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL][1]によって異なります。 |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) は Amazon S3 または Google Cloud Storage のいずれかに接続する必要があります。 |
| Amazon S3 または Google Cloud Storage | この統合では、1つの Amazon S3または Google Cloud Storage にアクセスできる必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 統合

次のCurrents統合は、[Amazon S3](#setting-up-braze-currents-for-s3)および[Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage)の両方でサポートされています。

### S3 向けの Braze Currents の設定

#### ステップ1:external ID を確認する {#step-one}

次に、**Amazon S3**を選択します。ここに示されている external ID に注意してください。これは、Fivetran が S3 バケットにアクセスできるようにするために必要です。 

![Fivetran の Braze コネクター設定フォーム。このステップに必要なexternal IDフィールドは、ページの中央にある薄い灰色のボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### ステップ2:指定されたS3バケットへのアクセス権をFivetranに与える

##### IAMポリシーの作成

[Amazon IAM コンソール](https://console.aws.amazon.com/iam/home#home)を開封し、**ポリシー > ポリシーの作成**に移動します。



`{your-bucket-name}` を S3 バケットの名前に置き換えてください。

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

 



##### IAMロールを作成する {#step-two}

AWS で、**ロール** に移動し、**新しいロールを作成** を選択します。



[**Another AWS Account**] を選択し、FivetranアカウントID `834469178297` を入力します。必ず**Require external ID**チェックボックスを確認してください。ここでは、ステップ1で見つかったexternal IDを提供します。



権限**を選択して、作成したポリシーを選択します。





![ロールに記載されているAmazon S3 ARNです。]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Fivetran に指定するロール ARN の権限を指定できます。このロールに選択的な権限を付与すると、Fivetran は、参照する権限を持つもののみを同期できます。
{% endalert %}

#### ステップ3:Fivetran コネクターの設定を完了する

フォーム内で、指定されたフィールドに適切な値を入力してください:
- `Destination schema`:一意のスキーマ名。
- `API URL`:あなたのBraze REST APIエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `External ID`:Currentsセットアップ手順の[ステップ2](#step-two)で設定されたexternal ID。このIDは固定値です。
- `Bucket`:
- `Role ARN`:現在のセットアップ手順の[ステップ1](#step-one)にロールARNが見つかります。

{% alert important %}
**Amazon S3** が **クラウドストレージ** の選択肢として選ばれていることを確認してください。
{% endalert %}



### Google Cloud Storage 向けの Braze Currents の設定

#### ステップ1:Google Cloud Storage から Fivetran メールアドレスを取得する {#step-one2}

次に、**Google Cloud Storage**を選択します。表示されるメールアドレスに注意してください。

![Fivetran の Braze コネクター設定フォーム。このステップに必要なメールフィールドは、ページの中央にある薄い灰色のボックスにあります。]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### ステップ2:バケットアクセスを許可する



![Google Storage Console で利用可能なバケット。

次に、[ステップ1](#step-one2)のメールアドレスに `Storage Object Viewer` アクセス権を付与するため、メールアドレスをメンバーとして追加します。バケット名をメモしておいてください。次のステップで Fivetran を設定するときに必要となります。



#### ステップ3:Fivetran コネクターの設定を完了する

フォーム内で、指定されたフィールドに適切な値を入力してください:
- `Destination schema`:一意のスキーマ名。
- `API URL`:あなたのBraze REST APIエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `Bucket Name`:
- `Folder`:

{% alert important %}
**Google Cloud Storage** が **Cloud Storage** の選択肢として選択されていることを確認してください。
{% endalert %}



[1]: {{site.baseurl}}/api/basics/#api-definitions