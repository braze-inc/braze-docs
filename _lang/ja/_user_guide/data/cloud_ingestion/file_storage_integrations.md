---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このページでは、Braze Cloud Data の取り込みと、S3 から Braze への関連データの同期方法について説明します。"
page_order: 3
page_type: reference

---

# ファイルストレージの連携

> このページでは、クラウドデータ取り込みのサポートを設定し、S3 から Braze に関連データを同期する方法について説明します。

## 

S3 用のクラウドデータ取り込み (CDI) を使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze と直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。 



- 
- 
- 
- 

## 

連携には次のリソースが必要です。

 - データストレージ用の S3 バケット 
 - 新規ファイル通知用の SQS キュー 
 - Braze接続用のIAMロール  

### AWSの定義

まず、この作業で使われる用語をいくつか定義しておこう。

|  | 定義 |
| --- | --- |
| Amazon リソースネーム (ARN) | ARN は、AWS リソースの一意の識別子です。 |
| アイデンティティとアクセス管理 (IAM) | IAM は、AWS リソースへのアクセスを安全にコントロール可能にする Web サービスです。このチュートリアルでは、IAMポリシーを作成し、それをIAMロールに割り当てて、S3バケットをBrazeクラウドデータインジェストと統合します。 |
| Amazon Simple Queue Service (SQS) | SQS は、分散ソフトウェアシステムとコンポーネントを統合できるホストキューです。 |


## AWS でのクラウドデータ取り込みの設定

### ステップ 1:ソースバケットの作成

AWS アカウントでデフォルト設定の汎用 S3 バケットを作成します。

デフォルト設定は次のとおりです。

  - ACL 無効
  - すべてのパブリックアクセスをブロックする
  - バケットのバージョン管理を無効にする
  - SSE-S3 暗号化

次のステップで同じリージョンに SQS キューを作成するので、バケットを作成したリージョンをメモしておきます。

### ステップ2:SQS キューの作成

作成したバケットにオブジェクトが追加されたときに追跡するSQS キューを作成します。ここでは、デフォルト設定設定s を使用します。 



{% alert important %}
このSQS は、バケットを作成したリージョンと同じリージョンに必ず作成してください。
{% endalert %}

この設定では ARN とSQS のURL を頻繁に使用するため、それらを必ずメモしてください。



### ステップ 3:アクセスポリシーの設定

アクセスポリシーを設定するには、**詳細オプション** を選択します。 

次の文をキューのアクセスポリシーに追加します。注意して、`YOUR-BUCKET-NAME-HERE` をバケット名に、`YOUR-SQS-ARN` をSQS キューの ARN に、`YOUR-AWS-ACCOUNT-ID` をAWS アカウント ID に置き換えてください。 

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

1. ステップ 1 で作成したバケットで、[**プロパティ**] > [**イベント通知**] に移動します。
2. 設定に名前を付けます。オプションで、ファイルのサブセットのみを Braze で取り込む場合は、対象とするプレフィックスまたはサフィックスを指定します。
3. **Destination**で**SQSキュー**を選択し、ステップ 2で作成したSQSのARNを入力します。

{% alert note %}

{% endalert %}

### ステップ 5: IAM ポリシーの作成

ソースバケットの操作を Braze に許可する IAM ポリシーを作成します。まず、アカウント管理者として AWS 管理コンソールにサインインします。 

1. AWS コンソールの [IAM] セクションに移動し、ナビゲーションバーの [**ポリシー**] を選択してから [**ポリシーを作成**] を選択します。<br><br><br><br>

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
3\.入力が終わったら、[**ポリシーの確認**] を選択します。

4. ポリシーに名前と説明を付けて、[**ポリシーの作成**] を選択します。  





### ステップ 6: IAM ロールを作成する

AWS での設定を完了するには、IAM ロールを作成し、ステップ 4 の IAM ポリシーをそれにアタッチします。 

1. IAM ポリシーを作成したコンソールの同じ [IAM] セクションで、[**ロール**] > [**ロールの作成**] に移動します。 

<br><br><br><br>

2. Braze AWS アカウントID をBraze ダッシュボードからコピーします。

3. AWS で、信頼できるエンティティセレクターのタイプとして [**別の AWS アカウント**] を選択します。Braze のアカウント ID を入力し、[**外部 ID が必要**] チェックボックスをオンにして、Braze で使用する external ID を入力します。完了したら [**次へ**] を選択します。 

<br><br> ![S3 の [ロールの作成] ページ。<br><br>


ステップ 4 で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。

<br><br><br><br>



<br><br><br><br>

{: start="5"}
5. クラウドデータ取り込み連携の作成に使用するため、作成したロールの ARN と生成した external-id をメモしておきます。  

## Braze でのクラウドデータ取り込みの設定

1. 新しい連携を作成するには、[**データ設定**] > [**クラウドデータ取り込み**] を開き、[**新しいデータ同期を作成**] を選択して、[ファイルソース] セクションから [**S3 インポート**]を選択します。 
2. AWS の設定プロセスからの情報を入力して新しい同期を作成します。次の項目を指定します。

  - ロールの ARN
  - External ID
  - SQS URL (新しい連携ごとに一意である必要があります)
  - 
  - 
  - 地域



{: start="3"}
3\. 

<br><br><br><br>


アクセスや権限の問題で同期が切れた場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。 

<br><br> <br><br>

{: start="5"}
5. 最後に接続テストを行い、同期を保存します。 

<br><br>

## 必要なファイル形式

クラウドデータ取り込みは、JSON、CSV、および Parquet のファイルをサポートします。それぞれのファイルには、サポートされている 1 列以上の識別子列と、ペイロード列 1 列 (JSON 文字列) が必要です。



### 

ソースファイルには、1 つ以上のユーザー 識別子列またはキーを含めることができます。各行には1 つの識別子のみを含める必要がありますが、ソースファイルには複数の識別子型を含めることができます。

|  |  |
| --- | --- |
|  |  |
|  |  |
|  | これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。 |
|  | 同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。 |
|  | 同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 |
| |  |


{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` 列は必須ではなく、サポートもされていません。
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

  

## 

- S3 ソースバケットに追加するファイルが 512 MB を超えてはなりません。512MB以上のファイルはエラーとなり、Brazeに同期されない。
- 
- 
- 

## 

### 





### 




