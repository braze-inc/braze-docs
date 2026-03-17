---
nav_title: セキュリティイベントのS3エクスポート
article_title: S3 でのセキュリティ設定のエクスポート
page_order: 1
page_type: reference
description: "この参照記事では、UTC の午前0 時にセキュリティイベントを毎日Amazon S3 に自動的にエクスポートする方法について説明します。"
---

# Amazon S3 でのセキュリティイベントのエクスポート

> セキュリティイベントをクラウドストレージプロバイダーであるAmazon S3に自動的にエクスポートできる。UTCの深夜0時に実行される日次ジョブで処理される。設定後は、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はない。このジョブは、過去24時間のセキュリティイベントをCSV形式で、設定済みのS3ストレージにエクスポートする。CSVファイルは手動でエクスポートしたレポートと同じ構造を持っている。

{% alert note %}
10,000行の制限は、ダッシュボードからの手動CSVレポートダウンロードにのみ適用される。セキュリティイベントのS3へのエクスポートは、この行数制限の対象外である。
{% endalert %}

Braze は、Amazon S3 エクスポートを設定するための 2 つの異なる S3 認証および承認方法をサポートしています。

- AWS シークレットアクセスキー方式
- AWSロールARNメソッド

## AWS シークレットアクセスキー方式

この方法では、シークレットキーとアクセスキー ID を生成します。これにより、Braze は AWS アカウントでユーザーとして認証し、バケットにデータを書き込むことができます。

### ステップ 1: アイデンティティとアクセス管理（IAM）ユーザーを作成する

秘密のアクセスキーとアクセスキーIDを取得するには、[AWSアカウントの設定](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin)手順に従ってIAMユーザーを作成する必要がある。

### ステップ 2:認証情報を取得する

1. 新しいユーザーを作成した後、アクセスキーを生成し、アクセスキーID とシークレットアクセスキーをダウンロードします。

![「liyu-chen-test」という役割の概要ページだ。]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\.これらの認証情報は、後でBraze に入力する必要があるため、どこかにメモしておくか、認証情報ファイルをダウンロードしてください。

![アクセスキーとシークレットアクセスキーを含むフィールド。]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### ステップ 3:ポリシーの作成

1. **IAM**（Identity and Access Management）＞**ポリシー**＞**ポリシーの作成**に進み、ユーザーへの権限を追加する。 
2. **Create Your Own Policy**を選択します。これにより、Brazeは指定されたバケットにのみアクセスできるように制限された権限が与えられます。
3. 選択したポリシー名を指定します。
4. [**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。"INSERTBUCKETNAME"は必ずバケット名で置き換えてください。これらの権限がないと、インテグレーションは認証情報チェックに失敗し、作成されません。

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

### ステップ4:ポリシーのアタッチ

1. 新しいポリシーを作成した後、**Users**に移動し、特定のユーザーを選択します。 
2. [**権限**] タブで [**権限を追加**] を選択し、ポリシーを直接アタッチして、そのポリシーを選択します。 

これで、AWS 認証情報を Braze アカウントにリンクする準備ができました!

### ステップ 5: Brazeを AWS にリンクする

1. Braze で [**設定**] > [**会社の設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[**セキュリティイベントのダウンロード**] セクションにスクロールします。
2. [**クラウドストレージにエクスポート**] の下の [**AWS S3 にエクスポート**] をオンに切り替えて、[**AWS シークレットアクセスキー**] を選択します。これにより、S3 エクスポートが有効になります。 
3. 次の情報を入力します。
- AWS アクセスキー ID
- AWS シークレットアクセスキー
    - このキーを入力するときは、まず [**認証情報をテスト**] を選択して認証情報が機能することを確認します。
- AWS バケット名 

![「セキュリティイベントダウンロード」ページには、BrazeアカウントとBraze外部IDが入力済みである。]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\.[**変更内容を保存**] を選択します。 

![変更を保存するボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

AWS S3 を Braze アカウントに統合しました!

## AWSロールARNメソッド

AWS ロール ARN メソッドは、Braze Amazon アカウントがそのロールのメンバーとして認証できるようにするロール Amazon リソースネーム (ARN) を生成します。

### ステップ1:ポリシーの作成

1. アカウント管理者としてAWS マネジメントコンソールにサインインします。 
2. AWSコンソールで、**IAM**（Identity and Access Management）セクション＞**ポリシー**に移動し、次に「**ポリシーの作成」**を選択する。

![ポリシーの一覧と「ポリシーを作成」ボタンがあるページ。]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\.[**JSON**] タブを開き、[**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。`INSERTBUCKETNAME` は必ずバケット名に置き換えてください。 

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

{: start="4"}
4\.ポリシーを確認したら、[**次へ**] を選択します。

![ポリシーを確認し、必要に応じて権限を追加できるページだ。]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\.ポリシーの名前と説明を指定し、[**ポリシーの作成**] を選択します。

![ポリシーを確認し作成するページだ。]({% image_buster /assets/img/security_export/review_and_create.png %})

### ステップ 2:役割を作成する

1. Braze で [**設定**] > [**会社の設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[**セキュリティイベントのダウンロード**] セクションにスクロールします。 
2. [**AWS ロール ARN**] を選択します。 
3. ロールの作成に必要な識別子、Brase アカウント ID、および Braze external ID をメモします。

![「セキュリティイベントダウンロード」ページには、BrazeアカウントとBraze外部IDが入力済みである。]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. AWSコンソールで、**IAM**（Identity and Access Management）セクション＞**ロール**＞**ロールの作成**に進む。 
5. 信頼できるエンティティセレクターのタイプとして [**別の AWS アカウント**] を選択します。 
6. BrazeのアカウントID を入力し、[**外部 ID が必要**] をオンにして、Braze external ID を入力します。 
7. 完了したら [**次へ**] を選択します。

![信頼できるエンティティの種類を選択し、AWSアカウントに関する情報を提供するオプションがあるページ。]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### ステップ 3:ポリシーのアタッチ

1. 以前に検索バーで作成したポリシーを検索し、ポリシーの横にチェックマークを付けて添付します。 
2. [**次へ**] を選択します。

![ポリシーの一覧。タイプと説明の列がある。]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\.ロールに名前と説明を指定し、[**Create Role**] を選択します。

![ロールの詳細情報を提供するフィールド。例えば、名前、説明、信頼ポリシー、権限、タグなど。]({% image_buster /assets/img/security_export/name_review_create.png %})

新しく作成したロールがリストに表示されます。

### ステップ4:Braze AWS にリンクする

1. AWS コンソールで、新しく作成したロールを一覧で見つけます。名前を選択してそのロールの詳細を開き、**ARN**を書き留めます。

![「security-event-export-olaf」というロールの概要ページ。]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\.Braze で [**設定**] > [**会社の設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[**セキュリティイベントのダウンロード**] セクションにスクロールします。

![「セキュリティイベントのダウンロード」セクションで、「AWS S3へのエクスポート」のトグルがオンになっている状態。]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\.**AWSロールARN**が選択されていることを確認し、指定したフィールドにロールARNとAWS S3バケット名を入力します。
4\.**Test Credentials**を選択して、認証情報が正しく機能することを確認します。
5\.[**変更内容を保存**] を選択します。 

![変更を保存するボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

AWS S3 を Braze アカウントに統合しました!