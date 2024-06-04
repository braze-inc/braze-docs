---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このリファレンス記事では、Braze クラウドデータ取り込みと S3 から Braze に関連データを同期する方法について説明します。"
page_order: 3
page_type: reference

---

# ファイルストレージの連携

> この記事では、クラウドデータ取り込みのサポートを設定し、S3 から Braze に関連データを同期する方法について説明します。

S3 用のクラウドデータ取り込みを使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze と直接連携できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。 

クラウドデータ取り込みは、JSON、CSV、Parquet のファイルと、属性、イベント、購入、およびユーザー削除のデータをサポートします。

連携には次のリソースが必要です。
 \- データストレージ用の S3 バケット
 \- 新規ファイル通知用の SQS キュー
 \- Braze アクセス用の IAM ロール  

{% alert note %}
Braze の S3 用のクラウドデータ取り込みサポートは現在、早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## AWS でのクラウドデータ取り込みの設定

AWS アカウントでクラウドデータ取り込みの連携を設定するには、次のステップに従います。

### ステップ 1: ソースバケットの作成

AWS アカウントでデフォルト設定の汎用 S3 バケットを作成します。 

デフォルト設定は次のとおりです。
  \- ACL 無効
  \- すべてのパブリックアクセスをブロックする
  \- バケットのバージョン管理を無効にする
  \- SSE-S3 暗号化

次のステップで同じリージョンに SQS キューを作成するので、バケットを作成したリージョンをメモしておきます。

### ステップ 2: SQS リソースの作成

S3 バケットを作成したリージョンに SQS キューを作成します。このキューは、作成したバケットにオブジェクトが追加された時点を追跡するために使用されます。

このキューは、アクセスポリシーステップに到達するまで、デフォルト設定で作成できます。アクセスポリシーを設定するときには、[詳細設定] オプションを選択します。次の文をキューのアクセスポリシーの最後に追加します。 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### ステップ 3: S3 バケットへのイベント通知の追加

1. ステップ 1 で作成したバケットで、[**プロパティ**] > [**イベント通知**] に移動します。

2. 設定に名前を付けます。オプションで、ファイルのサブセットのみを Braze で取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。

3. [**宛先**] で [**SQS キュー**] を選択し、ステップ 2 で作成した SQS の ARN を指定します。

### ステップ4: IAM ポリシーの作成

ソースバケットの操作を Braze に許可する IAM ポリシーを作成します。まず、アカウント管理者として AWS 管理コンソールにサインインします。 

1. AWS コンソールの [IAM] セクションに移動し、ナビゲーションバーの [**ポリシー**] を選択してから [**ポリシーを作成**] を選択します。<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. [**JSON**] タブを開き、[**ポリシードキュメント**] セクションに以下のコードスニペットを入力します。`YOUR-BUCKET-NAME-HERE` はバケット名に、`YOUR-SQS-ARN-HERE` は SQS キュー名に置き換えます。  

\`\`\`json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
"Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
},
    {
"Effect": "Allow",
"Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
"Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
},
    {
"Effect": "Allow",
"Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
"Resource": "YOUR-SQS-ARN-HERE"
}
        ]
            }

\`\`\`  

{: start="3"}
3. 入力が終わったら、[**ポリシーの確認**] を選択します。

4. ポリシーに名前と説明を付けて、[**ポリシーの作成**] を選択します。  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ 5: IAM ロール

AWS での設定を完了するには、IAM ロールを作成し、ステップ 4 の IAM ポリシーをそれにアタッチします。 

1. IAM ポリシーを作成したコンソールの同じ [IAM] セクションで、[**ロール**] > [**ロールの作成**] に移動します。<br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Braze ダッシュボードから Braze AWS のアカウント ID を取得します。[**パートナー連携**] > [**テクノロジーパートナー**] を選択し、[**Amazon S3**] を選択します。ここに、ロールの作成に必要なアカウント ID が表示されます。 

3. AWS で、信頼できるエンティティセレクターのタイプとして [**別の AWS アカウント**] を選択します。Braze のアカウント ID を入力し、[**外部 ID が必要**] チェックボックスをオンにして、Braze で使用する external ID を入力します。完了したら [**次へ**] を選択します。<br><br> ![S3 の [ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. ステップ 4 で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。完了したら [**次へ**] を選択します。<br><br>![ロールの ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>ロールに名前と説明を付け、[**ロールの作成**] をクリックします。<br><br>![ロールの ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5. CDI 連携の作成に使用するため、作成したロールの ARN と生成した external-id をメモしておきます。  

## Braze でのクラウドデータ取り込みの設定

1. 新しい連携を作成するには、[**データ設定**] > [**クラウドデータ取り込み**] を開き、[**新しいデータ同期を作成**] を選択して、[ファイルソース] セクションから [**S3 インポート**]を選択します。 

2. AWS の設定プロセスからの情報を入力して新しい同期を作成します。次の項目を指定します。
- ロールの ARN
- external ID
- SQS URL (新しい連携ごとに一意である必要があります)
- バケット名
- フォルダーのパス (オプション)
- 地域  

![\]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. 連携に名前を付け、この連携のデータ型を選択します。<br><br>![\]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. アクセスや権限の問題で同期が切れた場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。<br><br> ![\]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5. 最後に接続テストを行い、同期を保存します。<br><br>![\]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})