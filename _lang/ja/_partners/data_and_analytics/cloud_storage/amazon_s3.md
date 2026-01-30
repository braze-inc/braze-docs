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

{% alert important %}
クラウドストレージプロバイダーを切り替える場合は、Brazeカスタマーサクセスマネージャーに連絡して、新しい統合の設定と検証についてさらにサポートを受けてください。
{% endalert %}

Braze と Amazon S3 の統合は、2 つの統合戦略を特徴としています。

- [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) を利用すると、他のプラットフォーム、ツール、ロケーションに接続するまでデータを保存できます。
- ダッシュボードのデータエクスポート (CSV エクスポートやエンゲージメントレポートなど) を使用します。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Amazon S3 アカウント | この提携を利用するには、Amazon S3アカウントが必要だ。 |
| 専用 S3 バケット | Amazon S3 と統合するには、アプリ用の S3 バケットを作成する必要があります。<br><br>すでに S3バケットがある場合は、Braze 専用の新しいバケットを作成することをお勧めします。これにより、権限を制限できるようになります。新しいバケットを作成する方法については、次の手順を参照してください。 |
| Currents | Amazon S3にデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。メッセージアーカイブの設定だけなら、Currentsは必要ない。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 新しい S3 バケットの作成

アプリのバケットを作成するには、以下の手順を実行します。

1. [Amazon S3](https://console.aws.amazon.com/s3/) コンソールを開き、指示に従って AWS に**サインイン**または**アカウントを作成**します。 
2. サインイン後、**Storage& Content Delivery**カテゴリーから**S3を**選択する。 
3. 次の画面で**Create Bucket**を選択します。 
4. バケツを作成し、地域を選択するよう促される。

{% alert note %}
Currents は、[Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) が設定されたバケットには対応できません。
{% endalert %}

## 統合

Braze には、Amazon S3 に関する統合戦略が 2 種類あります。その 1 つは[Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) に関するもので、もう 1 つはすべてのダッシュボードデータエクスポート (CSV エクスポート、エンゲージメント レポートなど) に関するものです。どちらの統合も、2 種類の認証/許可方法をサポートしています。

- [AWS シークレットアクセスキー方式](#aws-secret-key-auth-method)
- [AWSロールARNメソッド](#aws-role-arn-auth-method)

## AWSシークレットキー認証方式

この認証メソッドは、シークレットキーとアクセスキー ID を生成し、Brazeがバケットにデータを書き込むためにAWSアカウントのユーザーとして認証できるようにします。

### ステップ1:ユーザーを作成する {#secret-key-1}

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、「**ダッシュボードデータエクスポート**」タブのステップに従う。
{% endalert %}

アクセスキーIDとシークレットアクセスキーを取得するには、[AWSでIAMユーザーと管理者グループを作成する](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)。

### ステップ2:認証情報を取得する {#secret-key-2}

新しいユーザーの作成後に、**Show User Security Credentials** を選択して、アクセスキー ID とシークレットアクセスキーを表示します。次に、これらの認証情報をどこかにメモしておくか、後でダッシュボードに入力する必要があるので、**認証情報のダウンロード**ボタンを選択する。

![]({% image_buster /assets/img_archive/S3_Credentials.png %})

### ステップ 3:ポリシーを作成する {#secret-key-3}

[**Policies**] > [**Get Started**] > [**Create Policy**] に移動して、ユーザーの権限を追加します。次に、**Create Your Own Policy**を選択します。これは限定的な権限を与えるもので、Brazeは指定されたバケットにしかアクセスできない。 

![]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Currents と Dashboard Data Export には異なるポリシーが必要です。Braze バックエンドがエラー処理を実行できるようにするには、`s3:GetObject` が必要です。
{% endalert %}

任意のポリシー名を指定し、**Policy Document**に以下のコードスニペットを入力します。`INSERTBUCKETNAME` は必ずバケット名に置き換えてください。これらの権限がないと、認証情報のチェックに失敗し、統合は作成されない。

{% alert note %}
メッセージのアーカイブ設定のみを行う場合は、**ダッシュボードデータエクスポートタブの**コードスニペットを使用する。
{% endalert %}

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

### ステップ4:ポリシーをアタッチする {#secret-key-4}

新しいポリシーの作成後に、**Users** に移動し、特定のユーザーを選択します。[**権限**] タブで、[**ポリシーの添付**] をクリックし、作成した新しいポリシーを選択します。これで、AWS 認証情報を Braze アカウントにリンクする準備ができています。

![]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### ステップ 5: Brazeを AWS にリンクする {#secret-key-5}

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、「**ダッシュボードデータエクスポート**」タブのステップに従う。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。

次に、[**Current を作成**] をクリックし、[**Amazon S3 データエクスポート**] を選択します。

Current に名前を付けます。**Credentials** セクションで、**AWS Secret Access Key** が選択されていることを確認し、指定されたフィールドに S3 アクセス ID、AWS シークレットアクセスキー、および AWS S3 バケット名を入力します。

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
AWSのアクセスキーID とシークレットアクセスキーを最新の状態に保ちます。コネクタの認証情報が期限切れになると、コネクタはイベントの送信を停止する。この状態が**5日**以上続くと、コネクタのイベントは削除され、データは永久に失われる。
{% endalert %}

必要に応じて、次のカスタマイズを追加することもできます。

- **フォルダーのパス:**デフォルトは `currents` です。このフォルダが存在しない場合は、Brazeが自動的に作成する。 
- **サーバ側の保管時のAES-256 暗号化:**デフォルトはオフで、`x-amz-server-side-encryption` ヘッダーが含まれます。

[**Current を開始**] を選択して続行します。

認証情報が正常に検証されたかどうかが通知される。AWS S3がBraze Currents用に設定された。

{% endtab %}
{% tab Dashboard Data Export %}

Braze で、[**パートナー連携**] > [**テクノロジーパートナー**] を選択し、[**Amazon S3**] を選択します。

**AWS Credentials** ページで、**AWS Secret Access Key** が選択されていることを確認し、指定したフィールドに AWS アクセス ID、AWS シークレットアクセスキー、および AWS S3 バケット名を入力します。シークレットキーを入力する際は、まず [**認証情報のテスト**] を選択して認証情報が機能することを確認し、成功したら [**保存**] を選択します。

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
ユーザーに移動し、AWS コンソールの **Security Credentials** タブで **Create Access Key** を選択することで、常に新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかが通知される。AWS S3がBrazeアカウントに統合された。

{% endtab %}
{% endtabs %}

## AWS ロールARN 認証メソッド

この認証メソッドによって、Braze の Amazon アカウントがバケットにデータを書き込むために作成したロールのメンバーとして認証できるようにするロール Amazon リソースネーム (ARN) が生成されます。

### ステップ 1: ポリシーを作成する {#role-arn-1}

まず、アカウント管理者として AWS 管理コンソールにサインインします。AWS コンソールの IAM セクションに移動し、ナビゲーションバーで [**Policies**] を選択してから、[**Create Policy**] を選択します。

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Currents と Dashboard Data Export には異なるポリシーが必要です。Braze バックエンドがエラー処理を実行できるようにするには、`s3:GetObject` が必要です。
{% endalert %}

[**JSON**] タブを開き、[**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME` は必ずバケット名に置き換えてください。入力が終わったら、[**ポリシーの確認**] を選択します。

{% alert note %}
メッセージのアーカイブ設定のみを行う場合は、**ダッシュボードデータエクスポートタブの**コードスニペットを使用する。
{% endalert %}

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

次に、ポリシーに名前と説明を指定し、[**Create Policy**] を選択します。

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ2:ロールを作成する {#role-arn-2}

コンソールと同じ IAM セクションで、[**Roles**] > [**Create Role**] を選択します。

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Braze アカウントから Braze アカウント ID と external ID を取得します。
- **Currents**:Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。次に、[**Current を作成**] をクリックし、[**Amazon S3 データエクスポート**] を選択します。ここで、ロールの作成に必要な識別子を確認します。
- **ダッシュボードデータエクスポート**:Braze で、[**パートナー連携**] > [**テクノロジーパートナー**] を選択し、[**Amazon S3**] を選択します。ここで、ロールの作成に必要な識別子を確認します。(メッセージアーカイブの設定のみを行う場合は、ここでロールを作成する)。

AWS Console に戻り、信頼できるエンティティセレクターのタイプとして [**Another AWS Account**] を選択します。BrazeのアカウントID を入力し、**外部ID を要求** をオンにして、Brazeの外部ID を入力します。完了したら [**次へ**] を選択します。

![S3 の [ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

### ステップ3:ポリシーをアタッチする {#role-arn-3}

次に、以前に作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横にチェックマークを付けて添付します。完了したら [**次へ**] を選択します。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

ロールに名前と説明を指定し、[**Create Role**] を選択します。

![ロールの ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

新しく作成した「役割」がリストに表示される。

### ステップ4:Braze AWS にリンクする {#role-arn-4}

AWS コンソールで、新しく作成したロールを一覧で見つけます。名前を選択して、そのロールの詳細を開きます。

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

ロール概要ページの上部にある**Role ARN**をメモします。

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Braze アカウントに戻り、提供されたフィールドにロールARN をコピーします。

{% alert note %}
メッセージアーカイブの設定のみを行う場合は、「**ダッシュボードデータエクスポート**」タブのステップに従う。
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

Braze で、[**Currents**] ページの [**統合**] に移動します。次に、[**Current を作成**] を選択し、[**Amazon S3 データエクスポート**] を選択します。

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Current の名前を指定します。次に、[**認証情報**] セクションで [**AWS ロール ARN**] が選択されていることを確認し、ロール ARN と AWS S3 バケット名を所定のフィールドに入力します。

必要に応じて、次のカスタマイズを追加することもできます。

- フォルダーのパス (デフォルトは`currents`)
- サーバーサイド、保管時 AES-256 暗号化 (デフォルトはオフ) -`x-amz-server-side-encryption`ヘッダーを組み込みます。

[**Current を開始**] を選択して続行します。認証情報が正常に検証されると通知が表示される。AWS S3がBraze Currents用に設定された。

{% alert important %}
「S3の認証情報が無効です」というエラーが発生した場合、これは AWS でロールを作成した後に行われた統合が早すぎたことが原因である可能性があります。しばらくしてからもう一度やり直してください。
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

Braze で、[**テクノロジーパートナー**] ページの [**統合**] に移動し、[**Amazon S3**] をクリックします。

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

[**認証情報**] ページで [**AWS ロール ARN**] ラジオボタンが選択されていることを確認し、ロール ARN と AWS S3バケット名を所定のフィールドに入力します。最初に [**認証情報のテスト**] をクリックして、認証情報が正しく動作することを確認し、成功したら [**保存**] をクリックします。

{% alert tip %}
ユーザーに移動し、AWS コンソールの [**セキュリティ認証情報**] タブで [**アクセスキーの作成**] を選択すると、いつでも新しい認証情報を取得できます。
{% endalert %}

認証情報が正常に検証されたかどうかが通知される。AWS S3がBrazeアカウントに統合された。

{% endtab %}
{% endtabs %}

## エクスポートの動作

クラウド・データ・ストレージ・ソリューションを統合し、API、ダッシュボード・レポート、CSVレポートをエクスポートしているユーザーは、次のような経験をしている：

- すべてのAPIエクスポートは、レスポンスボディにダウンロードURLを返さず、データストレージを通じて取得する必要がある。
- すべてのダッシュボード・レポートとCSVレポートは、ユーザーのメールに送信されてダウンロードされ（保存権限不要）、データ・ストレージにバックアップされる。

{% alert important %}
**JSONフォーマットの要件**：JSONエクスポートでは、BrazeはJSONL（改行区切りのJSON）フォーマットを使用し、各行に個別のJSONオブジェクトが含まれる。このフォーマットは、単一のJSON配列またはオブジェクトである標準的なJSONとは異なる。エクスポートされたファイルの各行は有効なJSONオブジェクトだが、ファイル全体としては1つの有効なJSONドキュメントではない。これらのファイルを処理するときは、ファイル全体を1つのJSONドキュメントとしてパースするのではなく、各行を個別のJSONオブジェクトとしてパースする。

カレントのエクスポートは、JSONではなく、Apache Avroフォーマット（`.avro` ファイル）を使用する。このJSONフォーマットの要件は、ダッシュボードデータのエクスポートとAPIエクスポートに適用される。
{% endalert %}

## 複数のコネクター

S3バケットに送信するCurrentsコネクタを複数作成する場合は、同じ認証情報を使用できるが、それぞれに異なるフォルダパスを指定する必要がある。同じワークスペースで作成することもできるし、複数のワークスペースに分割して作成することもできる。また、統合ごとに1つのポリシーを作成するか、両方の統合をカバーする1つのポリシーを作成するかのオプションもある。 

Currentsとデータエクスポートの両方に同じS3バケットを使用する場合は、それぞれの統合に異なる権限が必要なため、2つの別々のポリシーを作成する必要がある。


