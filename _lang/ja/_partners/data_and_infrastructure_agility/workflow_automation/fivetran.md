---
nav_title: Fivetran
article_title:Fivetran
alias: /partners/fivetran/
description:"この参考記事では、すぐに照会できるデータをクラウドウェアハウスに配信することで、データに裏打ちされた意思決定を支援できるワークフロー自動化ツールであるBrazeとFivetranのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner
tool:Currents

---

# Fivetran

> [Fivetranは](https://fivetran.com/)、アナリストに焦点を当てた製品と完全に管理されたパイプラインにより、すぐにクエリ可能なデータをクラウドウェアハウスに配信することで、データに裏打ちされた意思決定を可能にする、世界的に認知されたブランドである。

BrazeとFivetranの統合により、ユーザーは、すべてのアプリケーションとデータベースを中央ウェアハウスに接続することで、Brazeデータの収集と分析を可能にする、メンテナンス不要のパイプラインを作成することができる。データが中央ウェアハウスに収集された後、データチームは好みのビジネスインテリジェンスツールを使ってBrazeのデータを効率的に探索できる。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Fivetranアカウント | このパートナーシップを利用するには[Fivetran](https://fivetran.com/login?next=%2Fdashboard)アカウントが必要である。 |
| Braze REST API キー | 以下の権限を持つBraze REST APIキー：<br>\- users.export.ids<br>\- users.export.segment<br>\- email.unsubscribe<br>\- email.hard_bounces<br>\- messages.schedule_broadcasts<br>\- campaigns.list<br>\- campaigns.details<br>\- canvas.list<br>\- canvas.details<br>\- segments.list<br>\- segments.details<br>\- purchases.product_list<br>\- events.list<br>\- feed.list<br>\- feed.details<br>\- templates.email.info<br>\- templates.email.list<br>\- subscription.status.get<br>\- subscription.groups.get <br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは[インスタンスのBraze URLに][1]依存する。 |
| Braze Currents | [Braze Currentsは](https://www.braze.com/product/data-agility-management/currents/)、Amazon S3かGoogle Cloud Storageのいずれかに接続する必要がある。 |
| Amazon S3またはGoogle Cloud Storage | この統合には、Amazon S3かGoogle Cloud Storageにアクセスできることが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2} 

## 統合

以下のCurrents統合は、[Amazon S](#setting-up-braze-currents-for-s3)3と[Google Cloud Storageの](#setting-up-braze-currents-for-google-cloud-storage)両方でサポートされている。

### S3でBraze Currentsを設定する

#### ステップ1:外部IDを探す {#step-one}

[Fivetranダッシュボードで](https://fivetran.com/dashboard)、**\+ Connectorを**クリックし、**Braze**コネクタを選択してセットアップフォームを起動する。次に、**Amazon S**3を選択する。FivetranがあなたのS3バケットにアクセスできるようにするために必要だ。 

![The Fivetran set up Braze connector form. The external ID field needed for this step is located in the middle of the page in a light gray box.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### ステップ2:Fivetranに指定したS3バケットへのアクセス権を与える

##### IAMポリシーを作成する

[Amazon IAM Consoleを](https://console.aws.amazon.com/iam/home#home)開封し、**Policies > Create Policyに**移動する。

![\]({% image_buster /assets/img/fivetran_as3_iam.png %})

次に、**JSON**タブをクリックし、以下のポリシーを貼り付ける。`{your-bucket-name}` 」をS3バケット名に置き換えてほしい。

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

最後に、**Review Policy**をクリックし、ポリシーに固有の名前と説明を付ける。**Create Policyを**クリックしてポリシーを作成する。 

![\]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### IAMロールを作成する {#step-two}

AWSで「**Roles**」に移動し、「**Create New Role**」を選択する。

![\]({% image_buster /assets/img/fivetran_iam_new_role.png %})

**Another AWS Account**を選択し、Fivetran アカウント ID`834469178297` を入力する。**Require external ID**チェックボックスを必ずチェックすること。ここで、ステップ1で見つけた外部IDを入力する。

![\]({% image_buster /assets/img/fivetran_another_aws_account.png %})

次に、**Next: Permissionsを**クリックして、作成したばかりのポリシーを選択する。

![\]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

**Next: Reviewを**クリックし、新しいロールに名前を付け（Fivetranなど）、**Create Roleを**クリックする。ロールが作成されたら、それをクリックし、表示されたロールARNに注意する。

![The Amazon S3 ARN listed in the role.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Fivetranに指定したRole ARNの権限を指定することができる。このRoleに選択権限を与えることで、Fivetranは閲覧権限のあるものだけを同期できるようになる。
{% endalert %}

#### ステップ3:Fivetranコネクターを完成させる

Fivetranで、**\+ Connectorを**クリックし、**Braze**コネクタを選択してセットアップフォームを起動する。フォーム内で、指定されたフィールドに適切な値を記入する：
- `Destination schema`:一意なスキーマ名。
- `API URL`:Braze REST APIのエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `External ID`:Currents セットアップの[ステップ 2](#step-two)で設定した外部 ID。このIDは固定値である。
- `Bucket`:Brazeアカウントで**Integration > Currents > \[Your Current name] > Bucket Nameの**順にナビゲートして見つける。
- `Role ARN`:役割ARNは、Currentsセットアップの[ステップ](#step-one)1に記載されている。

{% alert important %}
**Amazon S3が** **クラウドストレージとして**選択されていることを確認する。
{% endalert %}

最後に「**Save & Test**」をクリックすれば、あとはFivetranがBrazeアカウントのデータと同期してくれる！

### Braze CurrentsをGoogle Cloud Storageに設定する

#### ステップ1:Google Cloud StorageからFivetranのメールを取り出す {#step-one2}

[Fivetranダッシュボードで](https://fivetran.com/dashboard)、**\+ Connectorを**クリックし、**Braze**コネクタを選択してセットアップフォームを起動する。次に**Google Cloud Storageを**選択する。表示されたメールアドレスをメモしておく。

![The Fivetran set up Braze connector form. The email field needed for this step is located in the middle of the page in a light gray box.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### ステップ2:バケツへのアクセスを許可する

[Google Storage Consoleに](https://console.cloud.google.com/storage/browser)移動し、Braze Currentsを設定したバケットを選択し、**バケット権限の編集を**クリックする。

![The Google Storage Console available buckets. Locate a bucket and click the vertical three dot symbol to open the drop down that allows you to edit bucket permissions.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

次に、[ステップ](#step-one2)1のメールをメンバーとして追加し、`Storage Object Viewer` 。Fivetranを設定する次のステップで必要になる。

![\]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### ステップ3:Fivetranコネクターを完成させる

Fivetranで、**\+ Connectorを**クリックし、**Braze**コネクタを選択してセットアップフォームを起動する。フォーム内で、指定されたフィールドに適切な値を記入する：
- `Destination schema`:一意なスキーマ名。
- `API URL`:Braze REST APIのエンドポイント。
- `API Key`:あなたのBraze REST APIキー。 
- `Bucket Name`:Brazeアカウントで**Integration > Currents > \[Your Current name] > Bucket Nameの**順にナビゲートして見つける。
- `Folder`:Brazeアカウントで**Integration > Currents > \[Your Current name] > Prefixの**順にナビゲートする。

{% alert important %}
**Google Cloud Storageが** **クラウドストレージとして**選択されていることを確認する。
{% endalert %}

最後に「**Save & Test**」をクリックすれば、あとはFivetranがBrazeアカウントのデータと同期してくれる！

[1]: {{site.baseurl}}/api/basics/#api-definitions