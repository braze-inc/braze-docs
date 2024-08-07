---
nav_title: フィールドレベルの暗号化
article_title: フィールドレベルの暗号化
permalink: "/field_level_encryption/"
description: "この参考記事では、Brazeで共有される個人を特定できる情報（PII）を最小限に抑えるために、電子メールアドレスを暗号化する方法について説明する。"
page_type: reference
---

# フィールドレベルの暗号化

> フィールドレベルの暗号化を使用して、AWS Key Management Service（KMS）で電子メールアドレスをシームレスに暗号化し、Brazeで共有される個人を特定できる情報（PII）を最小限に抑えることができる。暗号化は、機密データを解読不可能な暗号化された情報である暗号文に置き換える。

{% alert important %}
フィールドレベルの暗号化は現在ベータ機能として提供されている。このベータ版への参加に興味がある場合は、Brazeのアカウントマネージャーに連絡すること。
{% endalert %}

## その仕組み

メールアドレスは、Brazeに追加される前にハッシュ化され、暗号化されていなければならない。メッセージが送信されると、AWS KMSに復号化されたメールアドレスがコールされる。次に、ハッシュ化された電子メールアドレスは、配信およびエンゲージメント・イベントのメタデータに挿入され、元のユーザーにリンクされる。こうしてBrazeはEメール分析を追跡することができる。Brazeは、プレーンテキストの電子メールアドレスが含まれる場合はすべて再編集し、ユーザーのプレーンテキストの電子メールアドレスを保存しない。

## 前提条件

フィールドレベルの暗号化を使用するには、Brazeに送信する**前に**メールアドレスを[暗号](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html)化して[ハッシュ化](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)するために、AWS KMSにアクセスする必要がある。 

以下の手順に従って、AWS秘密鍵認証方法を設定する。

1. アクセスキーIDとシークレットアクセスキーを取得するには、AWS Key Management Serviceの権限ポリシーを持つ[IAMユーザーと管理者グループを](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin)AWSに[作成する](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin)。IAMユーザーには、[kms:Decryptと](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) [kms:GenerateMacの](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html)パーミッションが必要である。詳細については、[AWS KMSの権限を](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html)参照のこと。
2. **Show User Security Credentialsを**選択し、アクセスキーIDとシークレットアクセスキーを表示する。これらの認証情報をどこかに控えておくか、「**Download Credentials**」ボタンを選択し、AWS KMSキーに接続する際に入力する必要がある。
3. 以下のAWSリージョンでKMSをセットアップする必要がある：
    - **米国のクラスターをブレイズする：** `us-east-1`
    - **EUクラスターをろう付けする：** `eu-central-1`
4. AWS Key Management Serviceで、2つのキーを作成し、キーの使用権限にIAMユーザーが追加されていることを確認する：
    - **[暗号化/復号化する](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk)：****Symmetric**key typeと**Encrypt and Decrypt**key usageを選択する。
    - **[ハッシュ](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html)だ：****Symmetric**key type」と「**Generate and Verify MAC**key usage」を選択する。鍵の仕様は**HMAC_256**でなければならない。キーを作成した後、Brazeで入力する必要があるので、HMACキーIDをどこかに控えておくこと。

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## ステップ 1:AWS KMSキーに接続する

AWS KMSの設定には、以下を入力する：

- アクセスキーID
- 秘密のアクセス・キー
- HMACキーID（保存後は更新できない）

## ステップ2:暗号化フィールドを選択する

次に、**Eメールアドレスを**選択してフィールドを暗号化する。 

あるフィールドで暗号化が有効になっている場合、そのフィールドを復号化したフィールドに戻すことはできない。つまり、暗号化は恒久的な設定なのだ。電子メールアドレスの暗号化を設定する場合、ワークスペースに電子メールアドレスを持つユーザーがいないことを確認する。これにより、ワークスペースの機能を有効にしたときに、Brazeにプレーンテキストのメールアドレスが保存されないようになる。

![]({% image_buster /assets/img/field_level_encryption.png %})

## ステップ 3:ユーザーのインポートと更新

フィールドレベルの暗号化が有効な場合、Brazeに追加する前にメールアドレスをハッシュ化して暗号化する必要がある。ハッシュ化する前に、必ず電子メールアドレスの大文字小文字を区別すること。詳細は[ユーザー属性オブジェクトを](#user-attributes-object)参照のこと。

BrazeでEメールアドレスを更新する場合、`email` が含まれる場所では、ハッシュ化されたEメールアドレス値を使用すること。これには以下が含まれる：

- RESTエンドポイント：
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- CSV経由でユーザーを追加または更新する

{% alert note %}
新規ユーザーを作成する際には、`email_encrypted` 、そのユーザーの暗号化されたEメール値を追加しなければならない。そうでなければ、ユーザーは作成されない。同様に、Eメールを持っていない既存のユーザーにEメールアドレスを追加する場合は、`email_encrypted` 。そうでなければ、ユーザーは更新されない。
{% endalert %}

## 考慮事項

これらの機能は、フィールドレベルの暗号化ではサポートされない：

- SDK経由でメールアドレスを特定し、取得する
- アプリ内メッセージメール取得フォーム
- Email Insightsメールボックスプロバイダチャートを含む受信者ドメインのレポート
- 正規表現によるメールアドレスフィルター
- 観客同期
- Shopifyとの統合

### ユーザー属性オブジェクト

`/users/track` エンドポイントでフィールド・レベルの暗号化を使用する場合、[ユーザー属性オブジェクトの]({{site.baseurl}}/api/objects_filters/user_attributes_object)フィールドの詳細に注意すること：

- `email` フィールドは、Eメールのハッシュ値でなければならない。
- `email_encrypted` フィールドは、電子メールの暗号化された値でなければならない。

## よくある質問

### 暗号化とハッシュ化の違いは何か？

暗号化は、データの暗号化と復号化が可能な双方向の機能である。同じ平文値を複数回暗号化すると、AWSの暗号化アルゴリズム（AES-256-GCM）は異なる暗号化値を生成する。ハッシュは一方向性関数で、平文を解読できないようにスクランブルする。ハッシュは毎回同じ値を返す。これにより、同じメールアドレスを共有する複数のユーザー間で購読状態を維持することが可能になる。

### テスト送信に使用するメールアドレスは？
テスト送信では、プレーンテキストのメールアドレスがサポートされている。特定のユーザーのEメールがどのように見えるかを見るには、次のようにする：

1. **ユーザーとしてメッセージをプレビューを**選択する。
2. **Test Sendで**、**Override recipients attributes with current preview user's attributesを**選択する。

{%raw%}
### このメールアドレスをBrazeのLiquid`{{${email_address}}}` 。

Brazeは、メール送信時に平文のメールアドレスをレンダリングする。プレビューでは、暗号化されたバージョンのメールを表示する。カスタム・ワンクリックURLでユーザーを参照する場合は、ユーザーの外部IDを使用することをお勧めする。

`{{${email_address}}}` は現在、プリファレンスセンターと配信停止ページではサポートされていない。
{%endraw%}

### カレントに掲載されるメールアドレスは？

ハッシュ化されたEメールアドレスは、Eメール配信やエンゲージメントイベントに含まれる。

### メッセージのアーカイブにはどのメールアドレスが表示されるのか？

平文の電子メールアドレスは、メッセージング・アーカイビングに含まれる。これらは顧客のクラウド・ストレージ・プロバイダーに直接送信され、メール本文には他の個人データが含まれている可能性がある。
