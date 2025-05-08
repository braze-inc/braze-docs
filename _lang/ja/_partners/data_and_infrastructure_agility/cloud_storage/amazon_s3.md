---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "このリファレンス記事では、Amazon Web Services が提供するスケーラブルなストレージシステムであるBraze とAmazon S3 の連携について説明します。"
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/)は、Amazon Web Servicesが提供する高度にスケーラブルなストレージシステムです。

Braze とAmazon S3 の統合には、次の2 つの統合戦略があります。

- [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)を利用して、他のプラットフォーム、ツール、場所に接続するまでデータを保存できます。
- ダッシュボードのデータエクスポート(CSV エクスポートやエンゲージメントレポートなど) を使用します。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amazon S3 アカウント | このパートナーシップを活用するには、Amazon S3アカウントが必要です。 |
| 専用 S3 バケット | Amazon S3 と統合するには、アプリ用の S3 バケットを作成する必要があります。<br><br>すでに S3バケットがある場合は、Braze 専用の新しいバケットを作成することをお勧めします。これにより、権限を制限できるようになります。新しいバケットを作成する方法については、次の手順を参照してください。 |
| Currents | データを Amazon S3 にエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 新しい S3 バケットの作成

アプリのバケットを作成するには、次の手順を実行します。

1. [Amazon S3コンソール](https://console.aws.amazon.com/s3/)を開き、**Sign in**または**AWS**でアカウントを作成する手順に従います。 
2. サインイン後、**Storage & Content Delivery**カテゴリから**S3**を選択します。 
3. 次の画面で**Create Bucket**を選択します。 
4. バケットを作成してリージョンを選択するように求められます。

{% alert note %}
現在は、[Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) が設定されたバケットをサポートしていません。
{% endalert %}

## 統合

Braze には、[Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) の Amazon S3-one と、すべてのダッシュボードデータエクスポート (CSV エクスポートやエンゲージメントレポートなど) の 2 つの異なる統合ストラテジがあります。どちらの統合も、2 つの異なる認証方法または許可方法をサポートしています。

- [AWS シークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロールARNメソッド](#aws-role-arn-auth-method)

## AWSシークレットキー認証方式

この認証メソッドは、シークレットキーとアクセスキー ID を生成し、Brazeがバケットにデータを書き込むためにAWSアカウントのユーザーとして認証できるようにします。

### ステップ1:ユーザーを作成する {#secret-key-1}

アクセスキー ID とシークレットアクセスキーを取得するには、[AWS で IAM ユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)する必要があります。

### ステップ2:認証情報を取得する {#secret-key-2}

新しいユーザーを作成した後、**Show User Security Credentials**を選択して、アクセスキーIDとシークレットアクセスキーを表示します。次に、これらの認証情報をどこかにメモするか、**Download Credentials** ボタンを選択します。後でBraze ダッシュボードに入力する必要があります。

![][11]

### ステップ3:ポリシーを作成する {#secret-key-3}

**Policies** > **Get Started** > **Create Policy** に移動して、ユーザーの権限を追加します。次に、**Create Your Own Policy**を選択します。これにより、制限された権限が付与されるため、Brazeは指定されたバケットにのみアクセスできます。 

![][12]

{% alert note %}
Currents およびDashboard Data Export には異なるポリシーが必要です。Braze バックエンドがエラー処理を実行できるようにするには、`s3:GetObject` が必要です。
{% endalert %}

任意のポリシー名を指定し、**Policy Document**に以下のコードスニペットを入力します。`INSERTBUCKETNAME` は必ずバケット名に置き換えてください。これらの権限がないと、インテグレーションは認証情報チェックに失敗し、作成されません。

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab ダッシュボードデータのエクスポート %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### ステップ4:ポリシーをアタッチする {#secret-key-4}

新しいポリシーを作成した後、**Users**に移動し、特定のユーザーを選択します。**Permissions**タブで、**Attach Policy**を選択し、作成した新しいポリシーを選択します。これで、AWS認証情報をBrazeアカウントにリンクする準備ができました。

![][13]

### ステップ 5: Brazeを AWS にリンクする {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。

次に、**Create Current**、**Amazon S3 Data Export**を選択します。

現在の名前を指定します。**Credentials** セクションで、**AWS Secret Access Key** が選択されていることを確認し、指定したフィールドにS3 アクセスID、AWS シークレットアクセスキー、およびAWS S3 バケット名を入力します。

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSのアクセスキーID とシークレットアクセスキーを最新の状態に保ちます。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を中止します。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

必要に応じて、次のカスタマイズを追加することもできます。

- **フォルダーのパス:**デフォルトは `currents` です。このフォルダーが存在しない場合、Braze によって自動的に作成されます。 
- **サーバ側の保管時のAES-256 暗号化:**デフォルトはオフで、`x-amz-server-side-encryption` ヘッダーが含まれます。

**Launch Current**を選択して続行します。

認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze Currents 用に設定されているはずです。

{% endtab %}
{% tab ダッシュボードデータのエクスポート %}

ブレーズで、**Partner Integrations**> **Technology Partners**に移動し、**Amazon S3**を選択します。

**AWS Credentials** ページで、**AWS Secret Access Key** が選択されていることを確認し、指定したフィールドにAWS アクセスID、AWS シークレットアクセスキー、およびAWS S3 バケット名を入力します。シークレットキーを入力するときは、まず**Test Credentials**を選択して認証情報が機能することを確認し、次に成功したときに**Save**を選択します。

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
ユーザーに移動し、AWS コンソールの **Security Credentials** タブで **Create Access Key** を選択することで、常に新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze アカウントに統合されているはずです。

{% endtab %}
{% endtabs %}

## AWS ロールARN 認証メソッド

この認証方法では、Braze Amazon アカウントがバケットにデータを書き込むために作成したロールのメンバーとして認証できるようにするロール Amazon リソースネーム (ARN) が生成されます。

### ステップ1:ポリシーを作成する {#role-arn-1}

まず、アカウント管理者として AWS 管理コンソールにサインインします。AWS コンソールの IAM セクションに移動し、ナビゲーションバーで **Policies** を選択し、**Create Policy** を選択します。

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Currents およびDashboard Data Export には異なるポリシーが必要です。Braze バックエンドがエラー処理を実行できるようにするには、`s3:GetObject` が必要です。
{% endalert %}

[**JSON**] タブを開き、[**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME` は必ずバケット名に置き換えてください。入力が終わったら、[**ポリシーの確認**] を選択します。

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab ダッシュボードデータのエクスポート %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

次に、ポリシーに名前と説明を指定し、**Create Policy**を選択します。

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:ロールを作成する {#role-arn-2}

コンソールの同じ IAM セクションで、**Roles** > **Create Role** を選択します。

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze アカウントから Braze アカウント ID と external ID を取得します。
- **Currents**:Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。次に、**Create Current**を選択し、**Amazon S3 Data Export**を選択します。ここには、ロールの作成に必要な識別子s があります。
- **ダッシュボードデータエクスポート**:ブレーズで、**Partner Integrations**> **Technology Partners**に移動し、**Amazon S3**を選択します。ここでは、ロールの作成に必要な識別子を確認します。

AWS Console に戻り、信頼できるエンティティセレクターのタイプとして [**Another AWS Account**] を選択します。BrazeのアカウントID を入力し、**外部ID を要求** をオンにして、Brazeの外部ID を入力します。完了したら [**次へ**] を選択します。

![S3 の [ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーをアタッチする {#role-arn-3}

次に、以前に作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にチェックマークを付けて添付します。完了したら [**次へ**] を選択します。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

ロールに名前と説明を指定し、**Create Role** を選択します。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

これで、新しく作成したロールがリストに表示されます。

### ステップ4:Braze AWS にリンクする {#role-arn-4}

AWS コンソールで、新しく作成したロールを一覧で見つけます。名前を選択して、そのロールの詳細を開きます。

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

ロール概要ページの上部にある**Role ARN**をメモします。

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze アカウントに戻り、提供されたフィールドにロールARN をコピーします。

{% tabs %}
{% tab Braze Currents %}

ブレーズで、**Currents** ページの**Integrations** に移動します。次に、**Create Current**を選択し、**Amazon S3 Data Export**を選択します。

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Current の名前を指定します。次に、**Credentials** セクションで、**AWS Role ARN** が選択されていることを確認し、指定したフィールドにロールARN とAWS S3 バケット名を入力します。

必要に応じて、次のカスタマイズを追加することもできます。

- フォルダーのパス (デフォルトは`currents`)
- サーバーサイド、保管時 AES-256 暗号化 (デフォルトはオフ) -`x-amz-server-side-encryption`ヘッダーを組み込みます。

**Launch Current**を選択して続行します。認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze Currents 用に設定されているはずです。

{% alert important %}
「S3の認証情報が無効です」というエラーが発生した場合、これは AWS でロールを作成した後に行われた統合が早すぎたことが原因である可能性があります。しばらくしてからもう一度やり直してください。
{% endalert %}

{% endtab %}
{% tab ダッシュボードデータのエクスポート %}

ブレーズで、**Technology Partners** ページの**Integrations** に移動し、**Amazon S3** を選択します。

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

[**認証情報**] ページで [**AWS ロール ARN**] ラジオボタンが選択されていることを確認し、ロール ARN と AWS S3バケット名を所定のフィールドに入力します。最初に**認証情報**を選択して認証情報が正しく機能することを確認し、成功したら**保存**を選択します。

{% alert tip %}
ユーザーに移動し、AWS コンソールの **Security Credentials** タブで **Create Access Key** を選択することで、常に新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze アカウントに統合されているはずです。

{% endtab %}
{% endtabs %}

## エクスポートの動作

クラウドデータストレージソリューションを統合しており、API、ダッシュボードレポート、または CSV レポートをエクスポートする場合、次のような状況が発生します。

- すべての API エクスポートでは、応答本文でダウンロード URL が返されないため、データストレージから取得する必要があります。
- すべてのダッシュボードレポートと CSV レポートは、ダウンロード用のメールでユーザーに送信され (保存権限は不要です)、Data Storage にバックアップされます。 

## 複数のコネクター

S3 バケットに送信する Currents コネクターを複数作成する場合は、同じ認証情報を使用できますが、それぞれに異なるパスを指定する必要があります。これらは、同じワークスペース内で作成することも、複数のワークスペース内で分割して作成することもできます。また、統合ごとに1つのポリシーを作成するか、両方の統合に対応する1つのポリシーを作成することもできます。 

Currentsとデータエクスポートの両方に同じ S3 バケットを使用する場合は、統合ごとに異なる権限が必要なため、2 つの個別のポリシーを作成する必要があります。


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
