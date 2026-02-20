---
nav_title: ファイルストレージの連携
article_title: ファイルストレージの連携
description: "このページでは、Braze クラウドデータ取り込みと、S3 から Braze への関連データの同期方法について説明します。"
page_order: 3
page_type: reference

---

# ファイルストレージの連携

> このページでは、クラウドデータ取り込みのサポートを設定し、S3 から Braze に関連データを同期する方法について説明します。

## CDI の仕組み

S3 用のクラウドデータ取り込み (CDI) を使用して、AWS アカウントの 1 つ以上の S3 バケットを Braze と直接統合できます。新規ファイルが S3 にパブリッシュされると、メッセージが SQS に投稿され、Braze のクラウドデータ取り込みがそれらの新規ファイルを取り込みます。 

クラウドデータ取り込みは、以下をサポートしています。

- JSONファイル
- CSVファイル
- パーケットファイル
- 属性、カスタムイベント、購入イベント、ユーザー削除、カタログデータ

## 前提条件

連携には次のリソースが必要です。

 - データストレージ用の S3 バケット 
 - 新規ファイル通知用の SQS キュー 
 - Braze接続用のIAMロール  

### AWSの定義

まず、このタスクで使用される用語を定義します。

| 用語 | 定義 |
| --- | --- |
| Amazon リソースネーム (ARN) | ARN は、AWS リソースの一意の識別子です。 |
| アイデンティティとアクセス管理 (IAM) | IAM は、AWS リソースへのアクセスを安全にコントロール可能にする Web サービスです。このチュートリアルでは、IAMポリシーを作成し、それをIAMロールに割り当てて、S3バケットをBrazeクラウドデータインジェストと統合します。 |
| Amazon Simple Queue Service (SQS) | SQS は、分散ソフトウェアシステムとコンポーネントを統合できるホストキューです。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## AWS でのクラウドデータ取り込みの設定

### ステップ 1:ソースバケットの作成

AWS アカウントでデフォルト設定の汎用 S3 バケットを作成します。S3 バケットは、フォルダーが一意である限り、同期間で再利用できます。

デフォルト設定は次のとおりです。

- ACL 無効
- すべてのパブリックアクセスをブロックする
- バケットのバージョン管理を無効にする
- SSE-S3 暗号化
  - SSE-S3 は、サポートされている唯一のサーバー側暗号化タイプです。Amazon KMS暗号化はサポートされていません。

次回のステップで同じリージョンにSQS キューを作成する場合と同様に、バケットを作成したリージョンを書き留めておきます。

### ステップ2:SQS キューの作成

作成したバケットにオブジェクトが追加されたときに追跡するSQS キューを作成します。ここでは、デフォルト設定設定s を使用します。 

SQSキューはグローバルに一意でなければならない（例えば、CDI同期には1つしか使用できず、別のワークスペースで再利用することはできない）。

{% alert important %}
このSQS は、バケットを作成したリージョンと同じリージョンに必ず作成してください。
{% endalert %}

この設定では ARN とSQS のURL を頻繁に使用するため、それらを必ずメモしてください。

!["Advanced"を選択すると、キューにアクセスできるユーザーを定義するJSONオブジェクトの例が表示されます。]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

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
3. [**宛先**] で [**SQS キュー**] を選択し、ステップ2で作成した SQS の ARN を指定します。

{% alert note %}
S3バケットのルートフォルダにファイルをアップロードした後、一部のファイルをバケット内の特定のフォルダに移動すると、予期しないエラーが発生することがある。代わりにイベント通知をプレフィックス内のファイルについてのみ送信するように変更するか、プレフィックス外のファイルを S3 バケットに入れないようにするか、またはプレフィックスなしで連携を更新すること (すべてのファイルが取り込まれる) ができます。
{% endalert %}

### ステップ 5: IAM ポリシーの作成

ソースバケットの操作を Braze に許可する IAM ポリシーを作成します。まず、アカウント管理者として AWS 管理コンソールにサインインします。 

1. AWS コンソールの [IAM] セクションに移動し、ナビゲーションバーの [**ポリシー**] を選択してから [**ポリシーを作成**] を選択します。<br><br>![AWSコンソールの"Create policy"ボタン。]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

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

4. ポリシーの名前と説明を指定し、[**ポリシーの作成**] を選択します。  

!["new-policy-name."という名前のポリシーの例。]({% image_buster /assets/img/create_policy_3_name.png %})

![ポリシーの記述フィールド。]({% image_buster /assets/img/create_policy_4_created.png %})

### ステップ 6: IAM ロールを作成する

AWS での設定を完了するには、IAM ロールを作成し、ステップ 4 の IAM ポリシーをそれにアタッチします。 

1. IAM ポリシーを作成したコンソールの同じ [IAM] セクションで、[**ロール**] > [**ロールの作成**] に移動します。 

!["Create role"ボタン。]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2\.Braze AWS アカウントID をBraze ダッシュボードからコピーします。[**クラウドデータ取り込み**] に移動し、[**新しいデータ同期を作成**] を選択し、[**S3 インポート**] を選択します。
3\.AWS で、信頼できるエンティティセレクターのタイプとして [**別の AWS アカウント**] を選択します。Brazeの部門コードを入力します。**Require external ID**チェックボックスを選択します。
4\.Brazeで、**Data Settings** > **Cloud Data Ingestion**に移動し、**Create New Data Sync**を選択し、ファイルソースセクションから**S3 Import**を選択します。
5. 自動生成された**BrazeアカウントID**を複写します。 

![Braze アカウントID フィールドの認証情報セクション。]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
6. AWS で、アカウント ID を貼り付け、**Next** を選択します。

![S3 の [ロールの作成] ページ。このページには、ロール名、ロールの説明、信頼できるエンティティ、ポリシー、および権限境界のフィールドがあります。]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
7. ステップ 4 で作成したポリシーをロールにアタッチします。検索バーでポリシーを検索し、ポリシーの横のチェックマークを選択してアタッチします。完了したら [**次へ**] を選択します。

![new-policy-name を選択したロールARN。]({% image_buster /assets/img/create_role_3_attach.png %})

ロールに名前と説明を指定し、[**Create Role**] を選択します。

!["new-role-name"という名前のロールの例。]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
8. Cloud Data Ingestion 統合を作成するために必要なため、作成したロールのARN と生成した外部ID をメモしておきます。

## Braze でのクラウドデータ取り込みの設定

1. 新しい連携を作成するには、[**データ設定**] > [**クラウドデータ取り込み**] を開き、[**新しいデータ同期を作成**] を選択して、[ファイルソース] セクションから [**S3 インポート**]を選択します。 
2. AWS の設定プロセスからの情報を入力して新しい同期を作成します。次の項目を指定します。

  - ロールの ARN
  - External ID
  - SQS URL (新しい連携ごとに一意である必要があります)
  - バケット名
  - フォルダーパス (オプション、ワークスペース内の同期間で一意である必要があります)
  - 地域

![S3 に表示されるセキュリティー認証情報s を例にして、新しいインポートシンクを作成します。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\.統合に名前を付け、この統合のデータ型を選択する。 

![ユーザー 属性s をデータ型として、"cdi-s3-as-source-integration" の同期の詳細を設定します。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})

{: start="4"}
4\.アクセスや権限の問題で同期が切れた場合に通知を受け取る連絡先メールアドレスを追加します。オプションで、ユーザーレベルのエラーと同期の成功の通知をオンにします。 

![同期エラー 通知s の通知環境設定のセットアップ。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. 最後に、**Test connection** を選択して、Braze がバケットにアクセスできることを確認し、取り込み可能なファイルを一覧表示します(これらのファイル内のデータではありません)。次に同期を保存します。 

![データプレビューとの接続をテストするための選択肢です。]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## 必要なファイル形式

クラウドデータ取り込みは、JSON、CSV、および Parquet のファイルをサポートします。それぞれのファイルには、サポートされている 1 列以上の識別子列と、ペイロード列1列 (JSON 文字列) が必要です。

Brazeは、AWSによって強制される以上の追加のファイル名要件を強制しない。ファイル名は一意でなければなりません。一意性のためにタイムスタンプを付加することを推奨する。

### ユーザー識別子

ソースファイルには、1 つ以上のユーザー 識別子列またはキーを含めることができます。各行には1 つの識別子のみを含める必要がありますが、ソースファイルには複数の識別子型を含めることができます。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | これは更新したいユーザーの識別子である。これは Braze で使用されている `external_id` 値と一致しなければなりません。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | これら2つの列は、ユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。 |
| `BRAZE_ID` | Brazeのユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。 |
| `EMAIL` | ユーザーのEメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。 |
| `PHONE` | ユーザーの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 |
|`PAYLOAD` | Brazeでユーザーに同期させたいフィールドのJSON文字列。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
データウェアハウスソースとは異なり、`UPDATED_AT` 列は必須ではなく、サポートもされていません。
{% endalert %}

{% tabs %}
{% tab JSON Attributes %}
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
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
ソースファイルのすべての行に有効なJSONが含まれている必要があります。含まれていない場合、ファイルはスキップされます。
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
オプションの**DELETED** 列を含めます。`DELETED` が`true` の場合、そのカタログアイテムはBrazeのカタログから削除されます。[カタログ項目の削除](#deleting-catalog-items)を参照してください。
{% endtab %}

{% endtabs %}  

サポートされているすべてのファイルタイプの例については、[Braze-examplesの](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage)サンプルファイルを参照のこと。  

## データの削除

S3 のクラウドデータインジェストでは、ファイルアップロードs を使用したユーザー およびカタログアイテムの削除がサポートされています。それぞれに別々の同期とファイル形式を使用します。

- **[ユーザーの削除s](#deleting-users)** \- データタイプ**Delete ユーザー** と、ユーザー 識別子s のみを含むアップロード files (給与なし読み込む) で同期を作成します。
- **[カタログアイテムの削除](#deleting-catalog-items)** \- 既存のカタログ同期を使用し、`deleted` (または`DELETED`) 列を追加してアイテムを削除します。

### ユーザーの削除

S3 のファイルを使用してBraze のユーザープロファイル s を削除するには:

1. 新しいクラウドデータ取り込み同期を作成します(他の同期と同じ[AWSおよびBrazeセットアップ](#setting-up-cloud-data-ingestion-in-aws))。
2. Brazeで同期を設定する場合は、**データタイプ**を**ユーザの削除**に設定します。
3. ユーザー 識別子列のみを含むS3バケットに読み込むします。`PAYLOAD` 列を含めないでください。ペイ読み込むが存在すると同期が失敗し、誤って削除されないようにします。

ファイル内の各行は、以下のいずれかを使用して1 つのユーザーを識別する必要があります。

| 識別子 | 説明 |
| --- | --- |
| `EXTERNAL_ID` | Brazeで使用される`external_id` に一致します。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | 両方の列が一緒になって、別名でユーザーを識別します。 |
| `BRAZE_ID` | Braze生成ユーザー ID(現存ユーザーのみ)。 |

{% alert important %}
ユーザー の削除は永続的で、元に戻すことはできません。削除する予定のユーザーのみを含めます。詳しくは、[クラウドデータ取り込みによるユーザーの削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/)を参照してください。
{% endalert %}

**例- JSON (ユーザー削除):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**例- CSV (ユーザー削除):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

同期が実行されると、Braze はバケット内の新しいファイルを処理し、対応するユーザープロファイルを削除します。

### カタログ項目の削除

ファイルストレージを使用してカタログから項目を削除するには:

1. [同期カタログデータ]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)(データタイプ**カタログs**)と同じS3同期を使用します。
2. CSV またはJSON ファイルで、オプションの**`deleted`** (または**`DELETED`**) 列を追加します。
3. Braze のカタログから削除するすべてのアイテムについて、`deleted` を`true` に設定します。

各行には、`ID` と`PAYLOAD` が必要です。削除対象としてマークされた行の場合、給与読み込むは最小限にすることができます。Braze は`ID` によってアイテムを削除します。

**例- JSON (カタログアイテムの削除):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**例- CSV (カタログアイテムの削除):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

同期が実行されると、`deleted: true` の行によって、一致するカタログアイテムがBrazeで削除されます。完全なカタログの同期と削除の動作については、[カタログデータの同期と削除]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)を参照してください。

## 知っておくべきこと

- S3 ソースバケットに追加するファイルが512 MBを超えてはなりません。512 MBを超えるファイルはエラーになり、Braze に同期されません。
- 1ファイルあたりの行数に制限はありませんが、同期の速度を向上させるために、小さなファイルを使用することをお勧めします。例えば500 MB のファイルの取り込みは、100 MBのファイルを5つに分けて取り込む場合よりもかなり時間がかかります。
- 一度にアップロードできるファイルの数に制限はありません。
- ファイル内やファイル間の順序付けはサポートされていません。競合が予想される状況を監視している場合には、定期的に更新をバッチ処理することをお勧めします。

## トラブルシューティング

### ファイルのアップロードと処理

CDIは、同期が作成された後に追加されたファイルのみを処理する。このプロセスで、Braze は追加される新しいファイルを探します。これにより、SQS への新しいメッセージがトリガーされます。これにより、新しいファイルを処理するために新しい同期が開始される。

既存のファイルを使用して、Brazeがバケットにアクセスでき、取り込むファイルを検出できることを検証できますが、Brazeと同期されません。CDI がそれらを処理するには、同期する既存のファイルをS3 に再アップロードする必要があります。 

### 予期せぬファイルエラーを処理する

エラーや失敗ファイルが多い場合は、CDI のターゲットフォルダー以外のフォルダーにある S3 バケットに、別のプロセスがファイルを追加している可能性があります。

ファイルがソースバケットにアップロードされたが、ソースフォルダーには含まれていない場合、CDI は SQS 通知を処理しますが、ファイルに対してアクションを実行しないため、エラーとして表示されることがあります。
