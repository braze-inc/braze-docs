---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このリファレンス記事では、Braze クラウドデータ取り込みと S3 から Braze に関連データを同期する方法について説明します。"
page_order: 3
page_type: reference

---

# ファイルストレージの連携

> この記事では、クラウドデータ取り込みのサポートを設定し、S3 から Braze に関連データを同期する方法について説明します。

S3 のクラウドデータインジェスト(CDI) を使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze に直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。 

Cloud Data Ingestion supports JSON, CSV, and Parquet files, and attributes, event, purchase, and user delete data.

連携には次のリソースが必要です。
 - データストレージ用の S3 バケット 
 - 新しい通知のSQS キュー 
 - Braze接続用のIAMロール  

{% alert note %}
Braze Cloud Data Ingestion support for S3 is currently in early access.Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## AWSの定義

まず、このタスクで使用される用語のいくつかを定義します。

| ワード | 定義 |
| --- | --- |
| Amazonリソースネーム(ARN) | ARN は、AWS リソースの一意の識別子です。 |
| アイデンティティとアクセス管理(IAM) | IAM は、AWS リソースへの安全なコントロールアクセスを可能にするウェブサービスです。このチュートリアルでは、IAMポリシーを作成し、それをIAMロールに割り当てて、S3バケットをBrazeクラウドデータインジェストと統合します。 |
| Amazon Simple Queue Service (SQS) | SQS は、分散ソフトウェアシステムとコンポーネントを統合できるホストキューです。 |
{: .reset-td-br-1 .reset-td-br-2 }
 

## AWS でのクラウドデータ取り込みの設定

### ステップ 1:Create a source bucket

Create a general purpose S3 bucket with default settings in your AWS account. 

デフォルト設定は次のとおりです。
  - ACL 無効
  - すべてのパブリックアクセスをブロックする
  - バケットバージョニングの無効化
  - SSE-S3 暗号化

次のステップで同じリージョンに SQS キューを作成するので、バケットを作成したリージョンをメモしておきます。

### ステップ2:SQS キューの作成

作成したバケットにオブジェクトが追加されたときに追跡するSQS キューを作成します。ここでは、デフォルト設定設定s を使用します。

{% alert important %}
このSQS は、バケットを作成したリージョンと同じリージョンに必ず作成してください。
{% endalert %}

この設定では頻繁に使用するため、ARN とSQS のURL を必ずメモしてください。
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

### ステップ 3:アクセスポリシーの設定

アクセスポリシーを設定するには、**詳細オプション** を選択します。 

次の文をキューのアクセスポリシーに追加します。`YOUR-BUCKET-NAME-HERE` をバケット名に、`YOUR-SQS-ARN` をSQS キューARN に、`YOUR-AWS-ACCOUNT-ID` をAWSのアカウントID に置き換えるように注意してください。 

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

### ステップ 4:S3 バケットへのイベント通知の追加

1. ステップ 1 で作成したバケットで、**Properties**> **Event 通知 s** に移動します。

2. 設定に名前を付けます。オプションで、ファイルのサブセットのみを Braze で取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。

3. **Destination**で**SQSキュー**を選択し、ステップ 2で作成したSQSのARNを入力します。

### ステップ 5: IAM ポリシーの作成

Create an IAM policy to allow Braze to interact with your source bucket.To get started, sign in to the AWS management console as an account administrator. 

1. Go to the IAM section of the AWS Console, select **Policies** in the navigation bar, then select **Create Policy**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

2. **JSON** タブを開き、**Policy Document** セクションに以下のコード スニペットを入力します。`YOUR-BUCKET-NAME-HERE` をバケット名に、`YOUR-SQS-ARN-HERE` をSQS キュー名に置き換えるよう注意してください。 

```json
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

```  

{: start="3"}
3\.Select **Review Policy** when you're finished.

4. Give the policy a name and description and select **Create Policy**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### ステップ 6: IAM ロールを作成する

AWSの設定を完了するには、IAMロールを作成し、ステップ 4からIAMポリシーをアタッチします。 

1. IAM ポリシーを作成したコンソールの同じ \[IAM] セクションで、\[**ロール**] > \[**ロールの作成**] に移動します。<br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Retrieve the Braze AWS account ID from your Braze dashboard.\[**パートナー連携**] > \[**テクノロジーパートナー**] を選択し、\[**Amazon S3**] を選択します。ここには、ロールの作成に必要なアカウントID があります。<br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_find_account.png)<br><br>

3. AWS で、信頼できるエンティティセレクターのタイプとして \[**別の AWS アカウント**] を選択します。Provide your Braze account ID, select the **Require external ID** checkbox, and enter an external ID for Braze to use.Select **Next** when complete.<br><br> ![The S3 "Create Role" page.このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. ステップ 4 で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。Select **Next** when complete.<br><br>![Role ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Give the role a name and a description, and click **Create Role**.<br><br>![Role ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5. Cloud Data Ingestion 統合を作成するときに使用するために、作成したロールのARN と生成した外部ID をメモしておきます。  

## Braze でのクラウドデータインジェストの設定

1. 新しい連携を作成するには、\[**データ設定**] > \[**クラウドデータ取り込み**] を開き、\[**新しいデータ同期を作成**] を選択して、\[ファイルソース] セクションから \[**S3 インポート**]を選択します。 

2. Input the information from the AWS setup process to create a new sync.Specify the following:
- Role ARN
- External ID
- SQS URL (must be unique for each new integration)
- Bucket Name
- フォルダーのパス (オプション)
- 地域  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\.連携に名前を付け、この連携のデータ型を選択します。<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. アクセスや権限の問題で同期が切れた場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。<br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\.最後に接続テストを行い、同期を保存します。<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## 必要なファイル形式

クラウドデータ取り込みは、JSON、CSV、およびParquet ファイルをサポートします。それぞれのファイルには、サポートされている1 つ以上の識別子列と、JSON ストリングとしての給与読み込む列が含まれている必要があります。 

- ユーザ識別子ソースファイルには、1 つ以上のユーザー 識別子列またはキーを含めることができます。各行には1 つの識別子のみを含める必要がありますが、ソースファイルには複数の識別子型を含めることができます。 
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。This should match the `external_id` value used in Braze. 
    - `ALIAS_NAME` and `ALIAS_LABEL` \- These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias.Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier.This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion.To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address.If multiple profiles with the same email address exist, the most recently updated profile will be prioritized for updates.If you include both email and phone, we will use the email as the primary identifier.
    - `PHONE` - The user's email address.If multiple profiles with the same phone number exist, the most recently updated profile will be prioritized for updates. 
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列。

{% alert note %}
データウェアハウス ソースとは異なり、`UPDATED_AT` 列は必須でもサポートでもありません。
{% endalert %}

{% alert note %}
S3 ソースバケットに追加するファイルは、512MB を超えることはできません。512MBを超えるファイルはエラーになり、Brazeに同期されません。
{% endalert %}

{% tabs %}
{% tab JSON 属性 %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON カスタムイベント %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON 購入イベント %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}

{% endtab %}
{% tab CSV 属性 %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

サポートされているすべてのファイルタイプの例については、[braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)のサンプルファイルを参照してください。  
