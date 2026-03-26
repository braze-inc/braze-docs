---
nav_title: データをRedshiftに転送する
article_title: Redshift へのデータ転送
page_order: 8
page_type: tutorial
description: "このハウツー記事では、ETL（Extract, Transform, Load）プロセスを通じてAmazon S3からRedshiftにデータを転送する方法を説明する。"
tool: Currents

---

# データをRedshiftに転送する

> [Amazon Redshift](https://aws.amazon.com/redshift/) は、Amazon S3 と並んでAmazon Web Services 上で動作する、評判の良いデータウェアハウスです。CurrentsのBrazeデータは、Redshiftへの直接転送用に構造化されている。

以下は、Amazon S3からRedshiftへデータを転送する方法を説明する。このプロセスは抽出、変換、読み込み（ETL）を通じて行われる。完全なコードについては、Currentsのサンプル[GitHubリポジトリ](https://github.com/Appboy/currents-examples)を参照せよ。

{% alert important %}
これは、最も有利な場所にデータを転送するという観点で、選択できる多くのオプションの単なる 1 つに過ぎません。
{% endalert %}

## S3からRedshiftへのローダーの概要

この[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader)スクリプトは、同じRedshiftデータベース内の別のマニフェストテーブルを使用して、既にコピーされたファイルのトラッキングを行う。全体的な構造は以下の通りだ：

1. S3内の全ファイルをリストアップし、前回実行時から追加された新規ファイルを`s3loader.py`識別子で識別する。その際、リストとマニフェストテーブルの内容を比較する。
2. 新しいファイルを含む[マニフェスト](http://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html)ファイルを作成する。
3. マニフェストファイルを使用して、S3からRedshiftへ新しいファイルをコピーするクエリ`COPY`を実行する。
4. Redshiftの別々のマニフェストテーブルにコピーされたファイルの名前を挿入する。
5. コミットする。

## 依存関係

ローダーを実行するには、AWS Python SDKとPsycopgをインストールする必要がある。

```bash
pip install boto3
pip install psycopg2
```

## 権限

### S3への読み取りアクセス権を持つRedshiftロール

まだ行っていない場合は、[AWS](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html)の[ドキュメント](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html)に従って、S3上のファイルに対してコマンド`COPY`を実行できるロールを作成せよ。

### Redshift VPC の受信ルール

RedshiftクラスターがVPC内にある場合、S3ローダーを実行しているサーバーからの接続を許可するようVPCを設定しなければならない。Redshiftクラスターに入り、ローダーが接続するVPCセキュリティグループのエントリを選択する。次に、新しい受信ルールを追加する：**タイプ** = Redshift、**プロトコル** = TCP、**ポート** = クラスターのポート、**送信元** = ローダーを実行しているサーバーのIP（テスト時は「どこでも」）。

### S3への完全なアクセス権を持つアイデンティティとアクセス管理（IAM）ユーザー

S3ローダーは、Currentsデータを含むファイルへの読み取りアクセス権と、Redshift`COPY`コマンド用に生成するマニフェストファイルの保存場所への完全なアクセス権を必要とする。[IAMコンソール](https://console.aws.amazon.com/iam/home#/users)から、新しいIdentity and Access Management（IAM）ユーザーを作成し、権限`AmazonS3FullAccess`を付与する。認証情報を保存しておけ。ローダーに渡す必要があるからな。

アクセス認証情報は、環境変数、共有認証情報ファイル（`~/.aws/credentials`）、またはAWS設定ファイルを通じてローダーに渡すことができる。代わりに、それらを  オブジェクト`S3LoadJob`内の  フィールド`aws_access_key_id`と`aws_secret_access_key`  フィールドに割り当てることで、ローダーに直接含めることもできる。ただし、ソースコード内に認証情報をハードコーディングすることは推奨しない。

## 使用

### 使用例

以下のサンプルプログラムは、S3からRedshiftのテーブル`content_card_impression`にイベント`users.messages.contentcard.Impression`のデータを読み込む。

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### 認証情報

ローダーを実行するには、まずRedshiftクラスターのホスト名`host`、`port`ユーザー`database`名、パスワードを提供する必要がある。さらに、`user`SQLクエリを実行`COPY`できるRedshiftユーザーの`password`ユーザー名とパスワードも必要だ。さらに、前のセクションで作成したS3読み取りアクセス権を持つRedshiftロールのARNを提供しなければならない。

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### ジョブ設定

イベントファイルのS3バケットとプレフィックス、および`COPY`データを取り込みたいRedshiftテーブル名を指定する必要がある。

さらに、ローダーが要求する「auto」オプション付きの`COPY`Avroファイルに加え、Redshiftテーブルのカラム定義はサンプルプログラムに示す通り、Avroスキーマのフィールド名と一致させる必要がある。適切な型のマッピング（例：`string`\`int\`から`int``text`\`int\`へ、\`string\`から`integer``string`へ）も行うこと。

すべてのファイルを一度にコピーするのに時間がかかりすぎる場合は、ローダーにオプション`batch_size`を渡すこともできる。\`-b\`オプションを渡すことで、ローダーは一度にすべてをコピーする必要`batch_size`がなく、1バッチずつ段階的にコピーとコミットを行えるようになる。1バッチを読み込むのにかかる時間は、ファイルのサイズ`batch_size`とRedshiftクラスターのサイズに依存する。

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```