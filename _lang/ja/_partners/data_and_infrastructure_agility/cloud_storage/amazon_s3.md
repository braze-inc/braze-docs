---
nav_title: Amazon S3
article_title:Amazon S3
alias: /partners/amazon_s3/
description:"この参考記事では、BrazeとAmazon Web Servicesが提供する拡張性の高いストレージシステムであるAmazon S3との提携について概説している。"
page_type: partner
search_tag:Partner

---

# Amazon S3

> [Amazon S3は](https://aws.amazon.com/s3/)、Amazon Web Servicesが提供する拡張性の高いストレージシステムだ。

BrazeとAmazon S3の統合は、[Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)活用してBrazeデータをS3インスタンスに送信し、他のプラットフォーム、ツール、場所に接続するまでデータをそこに保存することを可能にする。ダッシュボードのデータエクスポートで統合することもできる。このページの指示に従って、AWS S3統合を開始する。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amazon S3アカウント | このパートナーシップを利用するには、Amazon S3アカウントが必要である。 |
| 専用S3バケット | Amazon S3と統合する前に、アプリ用のS3バケットを作成する必要がある。<br><br>すでにS3バケットをお持ちの場合は、権限を制限できるように、Braze専用の新しいバケットを作成することをお勧めする。新しいバケツを作成する方法については、以下の説明を参照のこと。 |
| Currents | Amazon S3にデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

#### 新しいS3バケットを作成する

アプリ用のバケットを作成するには、[Amazon S3コンソールを](https://console.aws.amazon.com/s3/)開封し、**Sign in**or**Create an Account with AWSの**指示に従う。サインイン後、**Storage & Content Delivery**カテゴリーから**S**3を選択する。次の画面で**Create Bucketを**選択する。バケツを作成し、地域を選択するよう促される。

## 統合

1つは[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)用、もう1つはすべてのダッシュボードデータエクスポート用（CSVエクスポート、エンゲージメントレポートなど）。どちらの統合も、2つの異なる認証／認可方法をサポートしている：

- [AWSシークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロール ARNメソッド](#aws-role-arn-auth-method)

## AWSの秘密鍵認証方法

この認証方法は、秘密鍵とアクセスキーIDを生成し、イネーブルメントがAWSアカウントのユーザーとして認証し、バケットにデータを書き込むことを可能にする。

### ステップ1:ユーザーを作成する {#secret-key-1}

アクセスキーIDとシークレットアクセスキーを取得するには、[AWSでIAMユーザーと管理者グループを作成](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)する必要がある。

### ステップ2:認証情報を取得する {#secret-key-2}

新規ユーザーを作成した後、\[**Show User Security Credentials**]をクリックし、アクセスキーIDとシークレットアクセスキーを表示する。次に、これらの認証情報をどこかにメモしておくか、後でダッシュボードに入力する必要があるので、**認証情報のダウンロード**ボタンをクリックする。

![][11]

### ステップ3:ポリシーを作成する {#secret-key-3}

**Policies > Get Started > Create Policyに**移動し、ユーザーの権限を追加する。次に、**Create Your Own Policyを**選択する。これにより、Brazeは指定されたバケットにしかアクセスできなくなる。 

![][12]

{% alert note %}
カレント」と「ダッシュボードデータエクスポート」では異なるポリシーが必要である。
{% endalert %}

任意のポリシー名を指定し、次のコード・スニペットを**ポリシー・ドキュメント**・セクションに入力する。必ず`INSERTBUCKETNAME` をバケツ名に置き換えること。これらの権限がないと、認証情報のチェックに失敗し、統合は作成されない。

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
{% tab Dashboard Data Export %}
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

### ステップ 4:ポリシーを添付する {#secret-key-4}

新しいポリシーを作成した後、「**ユーザー**」に移動し、特定のユーザーをクリックする。**権限]**タブで\[**ポリシーの添付]**をクリックし、作成した新しいポリシーを選択する。これでAWS認証情報をBrazeアカウントにリンクする準備ができた。

![][13]

### ステップ 5: AWSにBrazeをリンクする {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

Brazeで、**Partner Integrations**>**Data Exportに**移動する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Integrationsの**下に**Currentsが**ある。
{% endalert %}

次に、**Create Currentを**クリックし、**Amazon S3 Data Exportを**選択する。

Currentに名前を付け、**Credentials**セクションで**AWS Secret Access Key**ラジオボタンが選択されていることを確認し、指定されたフィールドにS3アクセスID、AWSシークレットアクセスキー、AWS S3バケット名を入力する。

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSアクセスキーIDとシークレットアクセスキーを最新の状態に保つ。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態が**48時間**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

また、顧客のニーズに応じて以下のようなカスタマイズを加えることもできる：

- **フォルダパス：**デフォルトは`currents` である。このフォルダが存在しない場合は、Brazeが自動的に作成する。 
- **サーバーサイド、REST AES-256暗号化：**デフォルトはOFFで、`x-amz-server-side-encryption` のヘッダーを含む。

**Launch Currentsを**クリックして続行する。

認証情報が正常に認証されたかどうかが通知される。これでBraze Currents用にAWS S3が設定されたはずだ。

{% endtab %}
{% tab Dashboard Data Export %}

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Amazon S**3をクリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

AWS認証情報]ページで、\[**AWSシークレットアクセスキー**]ラジオボタンが選択されていることを確認し、指定のフィールドにAWSアクセスID、AWSシークレットアクセスキー、AWS S3バケット名を入力する。秘密鍵を入力する際、まず**認証情報の**テストをクリックして認証情報が機能することを確認し、成功したら**Saveを**クリックする。

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
ユーザーにナビゲートし、AWS Console内の**Security Credentials**タブで**Create Access Keyを**クリックすることで、常に新しい認証情報を取得することができる。
{% endalert %}

認証情報が正常に認証されたかどうかが通知される。これでAWS S3がBrazeアカウントに統合されたはずだ。

{% endtab %}
{% endtabs %}

## AWSロールARNの認証方法

この認証方法は、バケットにデータを書き込むために作成したロールのメンバーとして、イネーブルメントのAmazonアカウントが認証できるように、ロールAmazon Resource Name（ARN）を生成する。

### ステップ1:ポリシーを作成する {#role-arn-1}

まず、アカウント管理者として AWS 管理コンソールにサインインします。AWSコンソールのIAMセクションに移動し、ナビゲーションバーの**Policiesを**クリックし、**Create Policyを**クリックする。

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
カレント」と「ダッシュボードデータエクスポート」では異なるポリシーが必要である。
{% endalert %}

\[**JSON**] タブを開き、\[**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。必ず`INSERTBUCKETNAME` をバケツ名に置き換えること。終了したら「**ポリシーの見直し**」をクリックする。

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
{% tab Dashboard Data Export %}

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

次に、ポリシーに名前と説明をつけ、**Create Policyを**クリックする。

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:役割を作成する {#role-arn-2}

コンソールの同じIAMセクションで、**Roles > Create Roleを**クリックする。

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

BrazeアカウントからBrazeアカウントIDと外部IDを取得する：
- **Currents**:Brazeで、**Partner Integrations**>**Data Exportに**移動する。次に、**Create Currentを**クリックし、**Amazon S3 Data Exportを**選択する。ここに、ロールを作成するために必要な識別子がある。
- **ダッシュボードのデータをエクスポート**する：Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Amazon S**3をクリックする。ここに、ロールを作成するために必要な識別子がある。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>**\- Currentsは** **Integrations**> Currentsにある。<br>**\- テクノロジーパートナーは** **インテグレーションに属して**いる。
{% endalert %}

AWSコンソールに戻り、信頼されたエンティティセレクタのタイプとして、**別のAWS**アカウントを選択する。BrazeアカウントIDを入力し、**Require external ID**ボックスをチェックし、Braze外部IDを入力する。完了したら**Nextを**クリックする。

![S3 の \[ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーを添付する {#role-arn-3}

次に、先ほど作成したポリシーをロールにアタッチする。検索バーでポリシーを検索し、ポリシーの横にチェックマークを付けて添付する。完了したら**Nextを**クリックする。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

ロールに名前と説明を付け、\[**ロールの作成**] をクリックします。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

これで、新しく作成した「役割」がリストに表示されるはずだ。

### ステップ 4:AWSへのリンク {#role-arn-4}

AWSコンソールで、新しく作成したロールをリストで見つける。名前をクリックすると、そのロールの詳細が開封される。

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

役割概要ページの上部にある**役割ARNに**注意すること。

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Brazeアカウントに戻り、ロールARNをフィールドにコピーする。

{% tabs %}
{% tab Braze Currents %}

Brazeで、**Integrationsの** **Currents**ページに移動する。次に、「**Create Currents**」をクリックし、「**Amazon S3 Data Export**」を選択する。

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

カレントに名前をつける。次に、**Credentials**セクションで、**AWS Role ARN**ラジオボタンが選択されていることを確認し、指定されたフィールドにロールARNとAWS S3バケット名を入力する。

また、顧客のニーズに応じて以下のようなカスタマイズを加えることもできる：

- フォルダパス（デフォルトは`currents` ）。
- サーバーサイド、REST AES-256暗号化（デフォルトはOFF） -`x-amz-server-side-encryption` ヘッダーを含む。

**Launch Currentsを**クリックして続行する。

認証情報が正常に認証されたかどうかが通知される。これでBraze Currents用にAWS S3が設定されたはずだ。

{% alert important %}
もし "S3の認証情報が無効です "というエラーが表示された場合、これはAWSでロールを作成した後、統合が早すぎたことが原因かもしれない。待って、もう一度やってみる。
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Brazeで、**Integrationsの** **Technology Partners**ページに移動し、**Amazon S**3をクリックする。

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

**AWS認証情報**]ページで、\[**AWS Role ARN]**ラジオボタンが選択されていることを確認し、指定のフィールドにロールARNとAWS S3バケット名を入力する。最初に**Test Credentialsを**クリックして認証情報が正しく機能することを確認し、成功したら**Saveを**クリックする。

{% alert tip %}
ユーザーにナビゲートし、AWS Console内の**Security Credentials**タブで**Create Access Keyを**クリックすることで、常に新しい認証情報を取得することができる。
{% endalert %}

認証情報が正常に認証されたかどうかが通知される。これでAWS S3がBrazeアカウントに統合されたはずだ。

{% endtab %}
{% endtabs %}

## 輸出行動

クラウドデータストレージソリューションを統合し、API、ダッシュボードレポート、またはCSVレポートをエクスポートしようとしているユーザーには、次のような問題が発生する：

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要がある。
- すべてのダッシュボード・レポートとCSVレポートは、ダウンロード用にユーザーのメールに送信され（保存権限不要）、データストレージにバックアップされる。 

## マルチコネクター

S3バケットに送信するCurrentsコネクタを複数作成する場合は、同じ認証情報を使用できるが、それぞれに異なるフォルダパスを指定する必要がある。これらは、同じワークスペースで作成することもできるし、複数のワークスペースに分割して作成することもできる。また、統合ごとに1つのポリシーを作成するか、両方の統合をカバーする1つのポリシーを作成するかのオプションもある。 

Currentsとデータエクスポートの両方に同じS3バケットを使用する場合は、それぞれの統合に異なる権限が必要なため、2つの別々のポリシーを作成する必要がある。


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
