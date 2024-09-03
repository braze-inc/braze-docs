---
nav_title: Quikly
article_title: Quikly
description: "このリファレンス記事では、BrazeとQuicklyのパートナーシップについて説明しています。Quicklyは緊急マーケティングプラットフォームであり、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速することができます。"
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly][1]、緊急性マーケティングプラットフォームは、心理学を活用して消費者を動機付け、ブランドが主要なマーケティングイニシアチブに対する反応を即座に高めることができます。

BrazeとQuiklyのパートナーシップにより、Brazeのカスタマージャーニー内のイベントでコンバージョンを加速させることができます。Quiklyは、緊急性の心理学を利用して、消費者を楽しく、そして即座に動機付けることでこれを実現します。例えば、ブランドはQuiklyを使用して、新しいメールおよびSMSの購読者を直接Brazeに追加したり、モバイルアプリのダウンロードなどの他の重要なマーケティング目標を促進したりすることができます。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| クイックリーアカウント | このパートナーシップを利用するには、[Quikly][1]ブランドパートナーアカウントが必要です。 |
| Braze REST API キー | `users.track`の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][2].お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
| Quikly APIキー（オプション） | クライアントの成功マネージャーによって提供されたQuikly APIキー（Webhookのみ）。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

QuiklyはブランドがメールまたはSMSの取得を加速し、購読者がBraze内で直接ファーストパーティデータを提供するように動機付けることを可能にします。また、Brazeを使用して、休眠顧客を再活性化し、そのオーディエンスを保持するためのQuiklyアクティベーションをターゲットにすることもできます。さらに、マーケティング担当者は、この統合を使用して、特定のカスタマージャーニーイベントに独自の報酬構造でインセンティブを与えることができます。 

以下に例を示します。
 - 数日間にわたって期待感とエンゲージメントを高め、消費者が[Quikly Hype][3]でエキサイティングな報酬を獲得するチャンスにオプトインするようにします。ファーストパーティデータは自動的にBrazeにプッシュされます。
 - 新しいメールおよびSMS購読者の獲得を加速するために、消費者の反応速度、他者とのランク、ランダム、または時間や数量がなくなる前に基づいたユニークなリアルタイムオファーを使用して、[Quikly Swap][4]を使用します。
 - webhookを使用して、カスタマージャーニーの特定のステップをユニークな報酬構造で動機付けします。
 - Quiklyアクティベーションに参加すると、ユーザーのプロファイルにカスタム属性やイベントが適用されます。

## 統合

以下に示すのは、メール取得、SMS取得、カスタム属性、およびwebhookの4つの異なる統合です。選択する統合は、Quiklyのアクティベーションとユースケースに依存します。

{% tabs %}
{% tab メール Acquisition %}

### メール取得

Quiklyのアクティベーションが顧客のメールアドレスやプロファイルデータを収集する場合、唯一必要なステップはQuiklyにREST APIキーとエンドポイントを提供することです。Quiklyは、ブランドアカウントを設定してこのデータをBrazeに渡します。追加のユーザー属性を含めたい場合は、APIクレデンシャルをQuiklyに提供する際にこれを言及してください。

ここに、Quiklyがこのワークフローを実行する方法の概要を示します。
1. Quiklyのアクティベーションに参加すると、Quiklyは指定された`email_address`を持つユーザーが存在するかどうかを確認するために[エクスポートAPI]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してユーザー検索をスケジュールします。
2. ユーザーをログまたは更新します。
  - ユーザーが存在する場合:
    - 新しいプロファイルを作成しません。
    - 必要に応じて、Quiklyはユーザーがアクティベーションに参加したことを示すために、ユーザーのプロファイルにカスタム属性を記録できます。
  - ユーザーが存在しない場合:
    - QuiklyはBrazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照します（ユーザーにはexternal IDがないため）。
    - 必要に応じて、Quiklyはカスタムイベントをログに記録して、このプロファイルがQuiklyアクティベーションに参加したことを示すことができます。

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
{% tab SMS取得 %}

### SMS購読

Quiklyのアクティベーションは、顧客から直接携帯電話番号を収集し、新しいSMSサブスクリプションを開始することができます。この統合を有効にするには、Quiklyクライアント成功マネージャーに`subscription_group_id`を提供してください。サブスクリプショングループの`subscription_group_id`にアクセスするには、**サブスクリプショングループ**ページに移動します。

Quiklyは顧客の電話番号を使用してサブスクリプションの検索を行い、SMSサブスクリプションが既に存在する場合は自動的にアクティベーションでクレジットします。それ以外の場合は、新しいサブスクリプションが開始され、サブスクリプションのステータスが確認された後、顧客にクレジットが付与されます。

顧客がQuiklyを介して携帯番号と同意を提供する際の完全なワークフローは次のとおりです:
1. Quiklyは、[サブスクリプショングループステータス]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)を使用してサブスクリプション検索を実行し、指定された`phone`が`subscription_group_id`にサブスクライブされているかどうかを確認します。サブスクリプションが存在する場合、Quiklyアクティベーションでユーザーにクレジットを付与します。さらなるアクションは必要ありません。
2. Quiklyは、[識別子エンドポイントによるユーザープロファイルのエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してユーザー検索を実行し、指定された`email_address`でユーザープロファイルが存在するかどうかを確認します。ユーザーが存在しない場合、Braze の [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を介してエイリアスのみのプロファイルを作成し、ユーザーのメールをユーザーエイリアスとして設定して、将来そのユーザーを参照できるようにします（ユーザーには external ID がないため）。
3. [ユーザーのサブスクリプショングループステータスエンドポイントを使用してサブスクリプションステータスを更新]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)。

既存のダブルオプトインSMSサブスクリプションワークフローをサポートするために、Quiklyは上記のワークフローの代わりにカスタムイベントをBrazeに送信できます。その場合、サブスクリプションステータスを直接更新するのではなく、[カスタムイベントがダブルオプトインプロセスをトリガーし]({{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/double_opt_in/)、サブスクリプションステータスが定期的に監視され、ユーザーが完全にオプトインしたことを確認してからQuiklyアクティベーションでクレジットされます。

{% alert important %}
Brazeは、新しいユーザーを`/users/track`エンドポイント経由で作成する際に、ユーザーを関連するサブスクリプショングループに追加する前に、ユーザープロファイルを完全に作成するための時間を確保するために約2分の遅延を設けることを推奨します。
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

Braze の実装によっては、Quikly アクティベーション内のイベントを Braze を通じてカスケードさせ、さらに処理することを検討する場合があります。例えば、Quiklyアクティベーションで達成されたレベルやインセンティブに基づいてカスタム属性をユーザーに適用し、アプリを開封したりWebサイトにログインしたときに関連するコンテンツカードを表示することができます。Quiklyは、これらの統合を実装するために直接協力します。

{% endtab %}
{% tab webhook %}
### Webhook
特定のイベントに対するインセンティブをトリガーするためにwebhookを使用してカスタマージャーニーを進めます。例えば、ユーザーがアプリにログインしたとき、プッシュ通知をオンにしたとき、またはストアロケーターを使用したときにBrazeイベントがある場合、特定のQuiklyアクティベーションの設定に基づいて、そのユーザーにカスタムオファーをトリガーするWebhookを使用できます。例として、アクション（例えば、アプリにログインする）を行った最初のX人のユーザーにカスタムオファーを提供する、または時間が経過するにつれて価値が減少するオファーを提供して即時の反応を促す戦術が含まれます。

### BrazeでQuiklyのWebhookを作成する

将来のキャンペーンやキャンバスのためにQuiklyのWebhookテンプレートを作成するには、Brazeプラットフォームの**テンプレート** > **Webhookテンプレート**に移動します。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**エンゲージメント** > **テンプレートとメディア** > **Webhookテンプレート**に移動します。
{% endalert %}

新しいキャンペーンを作成する際に、QuiklyのWebhookキャンペーンを一度だけ作成するか、既存のテンプレートを使用する場合は、Brazeで**Webhook**を選択してください。

**Blank テンプレート** を選択し、Webhook URL とリクエストボディに次の内容を入力します:
- **Webhook URL**: https://api.quikly.com/webhook/braze
- **リクエスト本文**:JSONキー/値のペア

#### リクエストヘッダーとメソッド

Quiklyには認証のための`HTTP Header`が必要です。

- **HTTPメソッド**:POST
- **リクエストヘッダー**:
  - **認可**:ベアラー \[PARTNER_AUTHORIZATION_HEADER]
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

### プレビューあなたのリクエスト

**プレビュー** パネルでリクエストをプレビューするか、`Test` タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、Webhookをテストするために独自のユーザーをカスタマイズできます。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を作成する際に、更新されたWebhookテンプレートは**保存されたWebhookテンプレート**リストにあります。
{% endalert %}

{% endtab %}
{% endtabs %}

## サポート
ご質問がある場合は、Quiklyのクライアントサクセスマネージャーにお問い合わせください。

[1]: https://www.quikly.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.quikly.com/urgency-marketing/platform/product-overview/hype
[4]: https://www.quikly.com/urgency-marketing/platform/product-overview/swap
