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



- 
- 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amazon S3 アカウント | このパートナーシップを活用するには、Amazon S3アカウントが必要です。 |
| 専用 S3 バケット | Amazon S3 と統合するには、アプリ用の S3 バケットを作成する必要があります。<br><br>すでに S3バケットがある場合は、Braze 専用の新しいバケットを作成することをお勧めします。これにより、権限を制限できるようになります。新しいバケットを作成する方法については、次の手順を参照してください。 |
| Currents | データを Amazon S3 にエクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 



1.  
2. サインイン後、**Storage & Content Delivery**カテゴリから**S3**を選択します。 
3. 次の画面で**Create Bucket**を選択します。 
4. バケットを作成してリージョンを選択するように求められます。

{% alert note %}

{% endalert %}

## 統合



- [AWS シークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロールARNメソッド](#aws-role-arn-auth-method)

## AWSシークレットキー認証方式

この認証メソッドは、シークレットキーとアクセスキー ID を生成し、Brazeがバケットにデータを書き込むためにAWSアカウントのユーザーとして認証できるようにします。

### ステップ1:ユーザーを作成する {#secret-key-1}

アクセスキー ID とシークレットアクセスキーを取得するには、[AWS で IAM ユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)する必要があります。

### ステップ2:認証情報を取得する {#secret-key-2}



![][11]

### ステップ3:ポリシーを作成する {#secret-key-3}

次に、**Create Your Own Policy**を選択します。これにより、制限された権限が付与されるため、Brazeは指定されたバケットにのみアクセスできます。 

![][12]

{% alert note %}

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



![][13]

### ステップ 5: Brazeを AWS にリンクする {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。





![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSのアクセスキーID とシークレットアクセスキーを最新の状態に保ちます。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を中止します。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

必要に応じて、次のカスタマイズを追加することもできます。

- **フォルダーのパス:**デフォルトは `currents` です。このフォルダーが存在しない場合、Braze によって自動的に作成されます。 
- **サーバ側の保管時のAES-256 暗号化:**デフォルトはオフで、`x-amz-server-side-encryption` ヘッダーが含まれます。



認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze Currents 用に設定されているはずです。

{% endtab %}
{% tab ダッシュボードデータのエクスポート %}





![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}

{% endalert %}

認証情報が正常に検証されたかどうかを示す通知が表示されます。これで、AWS S3が Braze アカウントに統合されているはずです。

{% endtab %}
{% endtabs %}

## AWS ロールARN 認証メソッド



### ステップ1:ポリシーを作成する {#role-arn-1}

まず、アカウント管理者として AWS 管理コンソールにサインインします。

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}

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



![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:ロールを作成する {#role-arn-2}



![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze アカウントから Braze アカウント ID と external ID を取得します。
- **Currents**:Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。ここには、ロールの作成に必要な識別子s があります。
- **ダッシュボードデータエクスポート**:

AWS Console に戻り、信頼できるエンティティセレクターのタイプとして [**Another AWS Account**] を選択します。BrazeのアカウントID を入力し、**外部ID を要求** をオンにして、Brazeの外部ID を入力します。完了したら [**次へ**] を選択します。

![S3 の [ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーをアタッチする {#role-arn-3}

次に、以前に作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にチェックマークを付けて添付します。完了したら [**次へ**] を選択します。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)



![ロールの ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

これで、新しく作成したロールがリストに表示されます。

### ステップ4:Braze AWS にリンクする {#role-arn-4}

AWS コンソールで、新しく作成したロールを一覧で見つけます。

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

ロール概要ページの上部にある**Role ARN**をメモします。

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze アカウントに戻り、提供されたフィールドにロールARN をコピーします。

{% tabs %}
{% tab Braze Currents %}



![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Current の名前を指定します。

必要に応じて、次のカスタマイズを追加することもできます。

- フォルダーのパス (デフォルトは`currents`)
- サーバーサイド、保管時 AES-256 暗号化 (デフォルトはオフ) -`x-amz-server-side-encryption`ヘッダーを組み込みます。

これで、AWS S3が Braze Currents 用に設定されているはずです。

{% alert important %}
「S3の認証情報が無効です」というエラーが発生した場合、これは AWS でロールを作成した後に行われた統合が早すぎたことが原因である可能性があります。しばらくしてからもう一度やり直してください。
{% endalert %}

{% endtab %}
{% tab ダッシュボードデータのエクスポート %}



![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

[**認証情報**] ページで [**AWS ロール ARN**] ラジオボタンが選択されていることを確認し、ロール ARN と AWS S3バケット名を所定のフィールドに入力します。

{% alert tip %}

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
