---
nav_title: S3 でのセキュリティイベントのエクスポート
article_title: S3 でのセキュリティ設定のエクスポート
page_order: 1
page_type: reference
description: "この参照記事では、UTC の午前0 時にセキュリティイベントを毎日Amazon S3 に自動的にエクスポートする方法について説明します。"
---

# Amazon S3 でのセキュリティイベントのエクスポート

> セキュリティイベントは、クラウドストレージプロバイダであるAmazon S3 に自動的にエクスポートできます。日次ジョブはUTC の午前0 時に実行されます。設定アップ後は、ダッシュボードからセキュリティイベントを手動でエクスポートする必要はありません。ジョブは、過去 24 時間のセキュリティイベントを CSV 形式で設定した S3 ストレージにエクスポートします。CSVファイルは、手動でエクスポートされたレポートと同じ構成になります。

Braze は、Amazon S3 エクスポートを設定するための 2 つの異なる S3 認証および承認方法をサポートしています。

- AWS シークレットアクセスキー方式
- AWSロールARNメソッド

## AWS シークレットアクセスキー方式

この方法では、シークレットキーとアクセスキー ID を生成します。これにより、Braze は AWS アカウントでユーザーとして認証し、バケットにデータを書き込むことができます。

### ステップ1:アプリ内メッセージユーザーの作成

シークレットアクセスキーとアクセスキーID を取得するには、[ AWS アカウント](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin) の手順に従って、アプリ内メッセージユーザーを作成する必要があります。

### ステップ2:認証情報を取得する

1. 新しいユーザーを作成した後、アクセスキーを生成し、アクセスキーID とシークレットアクセスキーをダウンロードします。

!["liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})() という名前のロールの概要ページ

{: start="2"}
2\.これらの認証情報は、後でBraze に入力する必要があるため、どこかにメモしておくか、認証情報ファイルをダウンロードしてください。

![アクセスキーとシークレットアクセスキーを含むフィールド。]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})()

### ステップ 3: ポリシーの作成

1. [**IAM**] > [**ポリシー**] > [**ポリシーを作成**] に移動し、ユーザーの権限を追加します。 
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

![Braze アカウントと Braze external ID が入力された [セキュリティイベントのダウンロード] ページ。]({% image_buster /assets/img/security_export/security_event_download1.png %})()

{: start="4"}
4\.[**変更内容を保存**] を選択します。 

![[変更内容を保存]ボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %})({: style="max-width:50%;"})

AWS S3 を Braze アカウントに統合しました!

## AWSロールARNメソッド

AWS ロール ARN メソッドは、Braze Amazon アカウントがそのロールのメンバーとして認証できるようにするロール Amazon リソースネーム (ARN) を生成します。

### ステップ1:ポリシーの作成

1. アカウント管理者としてAWS マネジメントコンソールにサインインします。 
2. AWS コンソールで、[**IAM**] セクション > [**ポリシー**] に移動し、[**ポリシーの作成**] を選択します。

![ポリシーのリストと [ポリシーの作成] ボタンがあるページ。]({% image_buster /assets/img/security_export/policies.png %})()

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

![ポリシーを確認し、オプションで権限を追加できるページ。]({% image_buster /assets/img/security_export/specify_permissions.png %})()

{: start="5"}
5\.ポリシーの名前と説明を指定し、[**ポリシーの作成**] を選択します。

![ポリシーを確認して作成するページ。]({% image_buster /assets/img/security_export/review_and_create.png %})()

### ステップ 2: 役割を作成する

1. Braze で [**設定**] > [**会社の設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[**セキュリティイベントのダウンロード**] セクションにスクロールします。 
2. [**AWS ロール ARN**] を選択します。 
3. ロールの作成に必要な識別子、Brase アカウント ID、および Braze external ID をメモします。

![Braze アカウントと Braze external ID が入力された [セキュリティイベントのダウンロード] ページ。]({% image_buster /assets/img/security_export/security_event_download2.png %})()

4. AWS コンソールで、[**IAM**] セクション> [**ロール**] > [**ロールの作成**] に移動します。 
5. 信頼できるエンティティセレクターのタイプとして [**別の AWS アカウント**] を選択します。 
6. BrazeのアカウントID を入力し、[**外部 ID が必要**] をオンにして、Braze external ID を入力します。 
7. 完了したら [**次へ**] を選択します。

![信頼されたエンティティタイプを選択し、AWS アカウントに関する情報を提供するオプションを含むページ。]({% image_buster /assets/img/security_export/select_trusted_entity.png %})()

### ステップ 3: ポリシーのアタッチ

1. 以前に検索バーで作成したポリシーを検索し、ポリシーの横にチェックマークを付けて添付します。 
2. [**次へ**] を選択します。

![タイプと説明の列を含むポリシーのリスト。]({% image_buster /assets/img/security_export/add_permissions.png %})()

{: start="3"}
3\.ロールに名前と説明を指定し、[**Create Role**] を選択します。

![名前、説明、信頼ポリシー、権限、タグなど、ロールの詳細を提供するフィールド。]({% image_buster /assets/img/security_export/name_review_create.png %})()

新しく作成したロールがリストに表示されます。

### ステップ4:Braze AWS にリンクする

1. AWS コンソールで、新しく作成したロールを一覧で見つけます。名前を選択してそのロールの詳細を開き、**ARN**を書き留めます。

!["security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})() という名前のロールの概要ページ

{: start="2"}
2\.Braze で [**設定**] > [**会社の設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[**セキュリティイベントのダウンロード**] セクションにスクロールします。

![[AWS S3 にエクスポート] のトグルがオンになっている [セキュリティイベントのダウンロード] セクション。]({% image_buster /assets/img/security_export/security_event_download3.png %})()

{: start="3"}
3\.**AWSロールARN**が選択されていることを確認し、指定したフィールドにロールARNとAWS S3バケット名を入力します。
4\.**Test Credentials**を選択して、認証情報が正しく機能することを確認します。
5\.[**変更内容を保存**] を選択します。 

![[変更内容を保存]ボタン。]({% image_buster /assets/img/security_export/save_changes_button.png %})({: style="max-width:40%;"})

AWS S3 を Braze アカウントに統合しました!