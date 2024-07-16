---
nav_title: Quikly
article_title:Quikly
description:"この参考記事では、Brazeと緊急マーケティングプラットフォームであるQuicklyのパートナーシップについて概説しており、Brazeカスタマージャーニー内のイベントにおけるコンバージョンを加速させることができる。"
alias: /partners/quikly/
page_type: partner
search_tag:Partner

---

# Quikly

> 緊急マーケティングプラットフォームである[Quiklyは][1]、心理学を活用して消費者のモチベーションを高めるため、ブランドは主要なマーケティング施策のレスポンスを即座に高めることができる。

BrazeとQuiklyのパートナーシップにより、Brazeカスタマージャーニー内のイベントでのコンバージョンを加速させることができる。Quiklyは、緊急性心理学を利用し、消費者を楽しい方法で、しかも即座にやる気にさせる。例えば、ブランドはQuiklyを使って、メールやSMSの新規購読者を即座に直接Brazeに獲得したり、モバイルアプリのダウンロードなど、他の主要なマーケティング目標の動機付けを行うことができる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| クイックリーのアカウント | このパートナーシップを利用するには、[Quikly][1]ブランド・パートナーのアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br>  |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][2]。エンドポイントはインスタンスのBraze URLに依存する。 |
| Quikly APIキー（オプション） | クライアントサクセスマネージャーから提供されたQuikly APIキー（Webhookのみ）。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Quiklyによって、ブランドはメールやSMSの獲得を加速することができ、サブスクライバーはBraze内で直接ファーストパーティデータを提供することができる。また、Brazeを使えば、失効した顧客をターゲットにQuiklyアクティベーションを行い、そのオーディエンスの再活性化と囲い込みを行うこともできる。さらに、マーケターはこの統合を利用して、独自の報酬体系で特定のカスタマージャーニーイベントにインセンティブを与えることができる。 

以下に例を示します。
 - 消費者が[Quikly Hypeで][3]エキサイティングな報酬を獲得するチャンスを求めてオプトインすることで、数日間にわたって期待感とエンゲージメントを高める。ファーストパーティーのデータは自動的にBrazeにプッシュされる。
 - [Quiklyスワップにより][4]、消費者の反応速度、他者との順位、ランダム性、または時間や数量が無くなる前に、ユニークなリアルタイムのオファーを使って、新規メールやSMSのサブスクライバーの獲得を加速させる。
 - Webhookを使用したユニークな報酬体系でカスタマージャーニーの特定のステップを動機付ける。
 - Quiklyのアクティベーションに参加したユーザーのプロファイルにカスタム属性やイベントを適用する。

## 統合

以下に、メール獲得、SMS獲得、カスタム属性、Webhooksの4つの異なる統合を紹介する。どの統合を選択するかは、Quiklyのアクティベーションとユースケースによって異なる。

{% tabs %}
{% tab Email Acquisition %}

### メール獲得

あなたのQuiklyアクティベーションが顧客のメールアドレスまたはプロファイルデータを収集する場合、必要なステップはQuiklyにREST APIキーとエンドポイントを提供することだけである。Quiklyは、このデータをBrazeに渡すようにブランドアカウントを設定する。追加で入れたいユーザー属性がある場合は、API認証情報をQuiklyに提供する際にその旨を伝える。

以下は、クィクリーがこのワークフローを実行する方法の概要である。
1. Quiklyのアクティベーションに参加すると、Quiklyは[エクスポートAPIを]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)使用してユーザー検索をスケジュールされ、指定された`email_address` でユーザーが存在するかどうかを確認する。
2. ユーザーをログインまたは更新する。
  - ユーザーが存在する場合：
    - 新しいプロファイルを作成しません。
    - 必要であれば、Quiklyはユーザープロファイルにカスタム属性を記録し、ユーザーがアクティベーションに参加したことを示すことができる。
  - ユーザーが存在しない場合：
    - Quiklyは、Brazeの[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由でエイリアスのみのプロファイルを作成し、ユーザー's email as the user alias to reference that user in the future (as the user won'tは外部IDを持つ）を設定する。
    - 必要であれば、QuiklyはこのプロファイルがQuiklyのアクティベーションに参加したことを示すカスタムイベントを記録することができる。

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
{% tab SMS Acquisition %}

### SMSサブスクリプション

クイックリーのアクティベーションは、顧客から直接携帯電話番号を収集し、新しいSMSサブスクリプションを開始することができる。この統合をイネーブルメントにするには、Quiklyクライアントサクセスマネージャーに`subscription_group_id`.サブスクリプショングループの`subscription_group_id` にアクセスするには、**サブスクリプショングループページに**移動する。

Quiklyは顧客の電話番号を使ってサブスクリプションの検索を行い、すでにSMSのサブスクリプションが存在する場合は、アクティベーションで自動的にクレジットされる。そうでない場合は、新しいサブスクリプションが開始され、サブスクリプションのステータスが確認された後、顧客にクレジットが加算される。

以下は、顧客がQuikly経由で携帯電話番号と同意を提供した場合の完全なワークフローである：
1. Quiklyは、[サブスクリプショングループのステータスを用いて]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)サブスクリプションのルックアップを行い、指定された`phone` が`subscription_group_id` にサブスクライブしているかどうかを確認する。サブスクリプションが存在する場合、Quiklyアクティベーションでユーザーにクレジットを入れる。これ以上のアクションは必要ない。
2. Quikly は、[Export user profile by identifier エンドポイントを]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)使用してユーザー検索を行い、指定された`email_address` を持つユーザープロファイルが存在するかどうかを確認する。ユーザーが存在しない場合は、Brazeの[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)経由でエイリアスのみのプロファイルを作成し、ユーザー's email as the user alias to reference that user in the future (as the user won't have an external ID)を設定する。
3. [ユーザーのサブスクリプショングループのステータスを更新するエンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)使用して、サブスクリプションのステータスを更新する。

既存のダブルオプトインSMSサブスクリプションワークフローをサポートするために、Quiklyは上記のワークフローではなく、カスタムイベントをBrazeに送信することができる。その場合、サブスクリプションのステータスを直接更新するのではなく、[カスタムイベントがダブルオプトインプロセスをトリガー]({{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/double_opt_in/)し、サブスクリプションのステータスが定期的に監視され、ユーザーが完全にオプトインしたことを確認してから、Quiklyのアクティベーションでクレジットが付与される。

{% alert important %}
Brazeは、`/users/track` エンドポイント経由で新規ユーザーを作成する場合、関連するサブスクリプショングループにユーザーを追加する前に、Brazeがユーザープロファイルを完全に作成する時間を確保するために、2分程度遅延させる必要があることをアドバイスしている。
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
{% tab Custom Attributes %}
### カスタム属性

Brazeの実装によっては、Quiklyのアクティベーション内のイベントをBrazeにカスケードしてさらに処理させたい場合がある。例えば、Quiklyアクティベーションで達成したレベルやインセンティブに基づいてカスタムユーザー属性を適用し、アプリ開封時やWebサイトログイン時に関連するコンテンツカードを表示できるようにしたい場合がある。Quiklyは、これらの統合を実装するためにあなたと直接協力する。

{% endtab %}
{% tab Webhooks %}
### Webhook
Webhookを使ってカスタマージャーニーの特定のイベントに対してインセンティブをトリガーする。例えば、ユーザーがアプリにログインした時、プッシュ通知をオンにした時、店舗ロケーターを使用した時のBrazeイベントがある場合、Webhookを使用して、特定のQuiklyアクティベーションの設定に基づいて、そのユーザーにカスタムオファーをトリガーすることができる。戦術の例としては、アクション（アプリへのログインなど）を行ったユーザーのうち、最初のX人にカスタムオファーで報酬を与えたり、時間が経過するほど価値が下がるオファーを提供したりして、即座のレスポンスを動機付ける。

### BrazeでQuikly Webhookを作成する。

将来のキャンペーンやCanvases用にQuikly Webhookテンプレートを作成するには、Brazeプラットフォームの「**テンプレート**」>「**Webhookテンプレート**」に移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**エンゲージメント**>**テンプレートとメディア**>**Webhookテンプレートに**移動する。
{% endalert %}

単発のQuikly Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。

**Blank Templateを**選択し、Webhook URLとリクエストボディに以下を入力する：
- **WebhookのURL**： https://api.quikly.com/webhook/braze
- **リクエスト本文**：JSONキーと値のペア

#### リクエストヘッダーとメソッド

Quiklyは認可のために`HTTP Header` 。

- **HTTPメソッド**：ポスト
- **リクエストヘッダー**：
  - **認可する**：Bearer \[PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Request body

選択する ***JSONキーと値のペア***を選択し、以下のペアを追加する：
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### リクエストをプレビューする

**プレビュー**パネルでリクエストをプレビューするか、`Test` タブに移動する。ここでは、ランダムユーザー、既存ユーザー、またはカスタマイズしたユーザーを選択して、Webhook をテストすることができる。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

{% endtab %}
{% endtabs %}

## サポート
ご質問はクイックリーのクライアント・サクセス・マネージャーまで。

[1]: https://www.quikly.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.quikly.com/urgency-marketing/platform/product-overview/hype
[4]: https://www.quikly.com/urgency-marketing/platform/product-overview/swap
