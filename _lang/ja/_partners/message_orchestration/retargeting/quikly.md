---
nav_title: Quikly
article_title: Quikly
description: "このリファレンス記事では、BrazeとQuicklyのパートナーシップについて説明しています。Quicklyは緊急マーケティングプラットフォームであり、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速することができます。"
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly](https://www.quikly.com)、緊急性マーケティングプラットフォームは、心理学を活用して消費者を動機付け、ブランドが主要なマーケティングイニシアチブに対する反応を即座に高めることができます。

_この統合は Quikly によって管理されます。_

## 統合について

BrazeとQuiklyのパートナーシップにより、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速させることができます。Quiklyは、緊急性の心理学を利用して、消費者を楽しく、そして即座に動機付けることでこれを実現します。たとえば、ブランドが Quikly を使用して、新しいメールや SMS サブスクライバーを Braze にすぐに直接取り込んだり、モバイルアプリのダウンロードなどの他の重要なマーケティング目標達成を促進したりできます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Quikly アカウント | このパートナーシップを利用するには、[Quikly](https://www.quikly.com)ブランドパートナーアカウントが必要です。 |
| Braze REST API キー | `users.track`、`subscription.status.set`、`users.export.ids`、`subscription.status.get` の権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Quikly APIキー（オプション） | クライアントの成功マネージャーによって提供されたQuikly APIキー（Webhookのみ）。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

ブランドは Quikly を使用して、メールまたは SMS サブスクライバーの獲得を加速し、サブスクライバーが Braze 内で直接ファーストパーティデータを提供するように促すことができます。また Braze を使用して、Quikly アクティベーションで離脱した顧客をターゲットにすることもできます。これにより、そのオーディエンスが再アクティブ化され、維持されます。さらに、マーケティング担当者は、この統合を使用して、特定のカスタマージャーニーイベントに独自の報酬構造でインセンティブを与えることができます。 

以下に例を示します。
 - 消費者が [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype) でエキサイティングなリワードを獲得できるチャンスのためにオプトインすると、期待とエンゲージメントが日に日に高まります。ファーストパーティデータは自動的にBrazeにプッシュされます。
 - [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap) を使用して、消費者の反応の速さ、ランダムな他者との比較ランキングに基づく独自のリアルタイムオファーで、時間や数量がなくなる前に、新しいメールまたは SMS サブスクライバーの獲得を促進します。
 - Webhook を使用した独自のリワード構造で、カスタマージャーニーの特定のステップを促します。
 - Quiklyアクティベーションに参加すると、ユーザーのプロファイルにカスタム属性やイベントが適用されます。

## 統合

以下に示すのは、メール取得、SMS取得、カスタム属性、およびwebhookの4つの異なる統合です。選択する統合は、Quikly のアクティベーションとユースケースに応じて異なります。

{% tabs %}
{% tab メール獲得 %}

### メール取得

Quiklyのアクティベーションが顧客のメールアドレスやプロファイルデータを収集する場合、唯一必要なステップはQuiklyにREST APIキーとエンドポイントを提供することです。Quiklyは、ブランドアカウントを設定してこのデータをBrazeに渡します。追加のユーザー属性を含めたい場合は、API 認証情報を Quikly に提供するときにこのことに言及してください。

ここに、Quiklyがこのワークフローを実行する方法の概要を示します。
1. Quiklyのアクティベーションに参加すると、Quiklyは指定された`email_address`を持つユーザーが存在するかどうかを確認するために[エクスポートAPI]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してユーザー検索をスケジュールします。
2. ユーザーをログまたは更新します。
  - ユーザーが存在する場合:
    - 新しいプロファイルを作成しません。
    - 必要に応じて、Quiklyはユーザーがアクティベーションに参加したことを示すために、ユーザーのプロファイルにカスタム属性を記録できます。
  - ユーザーが存在しない場合:
    - Quikly は Braze の[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照します（ユーザーにはexternal IDがないため）。
    - 必要に応じて、Quikly はカスタムイベントをログに記録して、このプロファイルが Quikly アクティベーションに参加したことを示すことができます。

{% details /users/track request %}

#### リクエストヘッダー
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Request body
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab SMS 獲得 %}

### SMS サブスクリプション

Quikly アクティベーションは、顧客から直接携帯電話番号を収集して新しい SMS サブスクリプションを開始できます。この統合を有効にするには、Quikly クライアントのサクセスマネージャーに `subscription_group_id` を提供してください。サブスクリプショングループの`subscription_group_id`にアクセスするには、**サブスクリプショングループ**ページに移動します。

Quikly は顧客の電話番号を使用してサブスクリプション検索を実行し、SMS サブスクリプションが既に存在する場合はアクティベーションで自動的にクレジットを付与します。それ以外の場合は、新しいサブスクリプションが開始され、サブスクリプションのステータスが確認された後、顧客にクレジットが付与されます。

顧客が Quikly で携帯電話番号と同意を提供する際の全体的なワークフローは次のとおりです:
1. Quiklyは、[サブスクリプショングループステータス]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)を使用してサブスクリプション検索を実行し、指定された`phone`が`subscription_group_id`にサブスクライブされているかどうかを確認します。サブスクリプションが存在する場合、Quikly アクティベーションでユーザーにクレジットを付与します。さらなるアクションは必要ありません。
2. Quiklyは、[識別子エンドポイントによるユーザープロファイルのエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してユーザー検索を実行し、指定された`email_address`でユーザープロファイルが存在するかどうかを確認します。ユーザーが存在しない場合、Braze の[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照できるようにします（ユーザーには external ID がないため）。
3. [ユーザーのサブスクリプショングループステータスの更新エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)を使用してサブスクリプションのステータスを更新します。

既存のダブルオプトインSMSサブスクリプションワークフローをサポートするために、Quiklyは上記のワークフローの代わりにカスタムイベントをBrazeに送信できます。この場合、サブスクリプションステータスを直接更新するのではなく、[カスタムイベントによってダブルオプトインプロセスがトリガーされ]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)、サブスクリプションステータスが定期的に監視され、ユーザーが完全にオプトインしたことを確認してから Quikly アクティベーションが実行されます。

{% alert important %}
Braze は、`/users/track` エンドポイントを使用して新しいユーザーを作成する場合、Braze がユーザープロファイルを完全に作成できる時間を確保するために、関連するサブスクリプショングループにユーザーを追加するまでに約2分の遅延が必要であることをアドバイスしています。
{% endalert %}

{% details Detailed /subscription/status/set request %}
#### リクエストヘッダー
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Request body
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab カスタム属性 %}
### カスタム属性

Braze の実装によっては、Quikly アクティベーション内のイベントを Braze を通じてカスケードさせ、さらに処理することを検討する場合があります。たとえば、Quikly アクティベーションで達成したレベルやインセンティブに基づいてカスタムユーザー属性を適用し、アプリを開いたときや Web サイトにログインしたときに関連するコンテンツカードを表示することができます。これらの統合を実装するために Quikly がお客様と直接協力します。

{% endtab %}
{% tab webhook %}
### Webhook
Webhook を使用して、カスタマージャーニーの特定のイベントに対するインセンティブをトリガーします。たとえば、ユーザーがアプリにログインしたとき、プッシュ通知をオンにしたとき、またはストアロケーターを使用したときの Braze イベントがある場合、Webhook を使用して、特定のQuikly アクティベーションの設定に基づき、そのユーザーへのカスタムオファーをトリガーできます。たとえば、カスタムオファーでアクション (アプリへのログインなど) を実行するユーザーのうち、最初の X 人にリワードを与える、または即座の応答を促すために、時間の経過に伴い価値が減少するオファーを提供するなどの戦術があります。

### BrazeでQuiklyのWebhookを作成する

将来のキャンペーンやキャンバスのためにQuiklyのWebhookテンプレートを作成するには、Brazeプラットフォームの**テンプレート** > **Webhookテンプレート**に移動します。 

新しいキャンペーンを作成する際に、QuiklyのWebhookキャンペーンを一度だけ作成するか、既存のテンプレートを使用する場合は、Brazeで**Webhook**を選択してください。

**Blank テンプレート** を選択し、Webhook URL とリクエストボディに次の内容を入力します:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **リクエスト本文**:JSONキー/値のペア

#### リクエストヘッダと方法

Quikly では認証に `HTTP Header` が必要です。

- **HTTPメソッド**：POST
- **リクエストヘッダー**:
  - **Authorization**:ベアラー [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Request body

***JSONキー/値のペア***を選択し、次のペアを追加します:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### リクエストをプレビューする

**プレビュー** パネルでリクエストをプレビューするか、`Test` タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、Webhookをテストするために独自のユーザーをカスタマイズできます。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

{% endtab %}
{% endtabs %}

## サポート
ご質問がある場合は、Quiklyのクライアントサクセスマネージャーにお問い合わせください。


