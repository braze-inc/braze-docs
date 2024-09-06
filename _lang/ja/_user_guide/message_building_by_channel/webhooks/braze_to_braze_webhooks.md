---
nav_title: ブレイズ・トゥ・ブレイズ・ウェブフック
article_title: ブレイズ・トゥ・ブレイズ・ウェブフック
page_order: 3
channel:
  - webhooks
description: "この記事では、Braze-to-Brazeウェブフックの作成方法について説明する。"

---

# Braze-to-Brazeウェブフック

> Webhookを使用して、Braze \[REST API][2]] と通信することができる。私たちはこれをBraze-to-Braze webhook-BrazeからBrazeへ通信するwebhookと呼んでいる。

## 前提条件

Braze-to-BrazeのWebhookを作成するには、到達したいエンドポイントのパーミッションを持つ\[APIキー][3] ]が必要だ。

## ユースケース

Braze-to-BrazeのWebhookでできることはたくさんあるが、ここでは一般的な使用例をいくつか紹介しよう：

- ユーザがメッセージを受信すると、カウンタのカスタム属性（整数）をインクリメントする。
- 最初のキャンバスから2番目のキャンバスをトリガーする。

{% alert tip %}
[ユーザー更新ステップを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)キャンバスに追加して、ユーザーの属性、イベント、購入をJSONコンポーザーで追跡する。こうすることで、BrazeがBraze-to-Braze webhookよりも効率的に更新を処理できるように、これらの更新はバッチ処理される。
{% endalert %}

このページの使用例は、\[Webhookがどのように機能するか][4] ]と\[BrazeでWebhookを作成する方法][5] ]をすでに知っていることを前提としている。

## Braze-to-Brazeウェブフックの作成手順

Webhookリクエストの詳細はユースケースによって異なるが、Braze-to-Braze Webhookを作成するための一般的なワークフローは変わらない。

1. \[キャンペーンまたはキャンバスのコンポーネントとしてウェブフック][5] を作成する。 
2. **空白のテンプレートを**選択する。
3. **Compose**タブで、**Webhook URLと** **Request Bodyを**ユースケースに応じて指定する。
4. **Settings "**タブで、**HTTPメソッドと** **リクエスト・ヘッダを**指定する。
5. 必要に応じて、Webhookの残りの部分を構築し続ける。ユースケースによっては、カスタムイベントからキャンペーンやキャンバスをトリガーするなど、特定の配信設定が必要なものもある。

### ユースケース:カウンターの整数カスタム属性をインクリメントする

この使用例では、カスタム属性を作成し、特定のアクションが発生した回数をカウントするためにLiquidを使用する。 

例えば、ユーザーがアクティブなアプリ内メッセージ・キャンペーンを何回見たかをカウントし、3回見たら二度とキャンペーンを受け取らないようにしたい場合がある。BrazeのLiquidロジックで何ができるか、より多くのアイデアについては、[Liquidユースケースライブラリを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)チェックしよう。

Braze-to-BrazeのWebhookを作成するための一般的な手順に従い、Webhookを設定する際には以下を参照すること：

- **Webhook URL:**あなたの\[RESTエンドポイントURL][7] の後に`/users/track`.例えば、US-06のインスタンスの場合、URLは`https://rest.iad-06.braze.com/users/track` となる。
- **要求本文:**Raw Text

#### リクエストヘッダと方法

Brazeは認証のために、APIキーと`content-type` を宣言するHTTPヘッダーを要求する。

- **要求ヘッダー:**
  - **認可する：**Bearer {YOUR_API_KEY}
  - **Content-Type:**application/json
- **HTTP メソッド:**POST

`YOUR_API_KEY` を、`users.track` 権限を持つ Braze API キーに置き換える。APIキーは、Brazeダッシュボードの**「設定」**>「**APIキー**」で作成できる。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**開発者コンソール**] > \[**API 設定**] から API キーを作成できます。
{% endalert %}

![][1]

#### Request body

リクエストボディにユーザートラックリクエストを追加し、リキッドにカウンタ変数を代入する。詳しくは\[ユーザートラック][8]]を参照のこと。

以下は、このエンドポイントに必要なリキッドとリクエストボディの例である。`your_attribute_count` は、ユーザーがメッセージを見た回数をカウントするために使用する属性である： {% raw %}

```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
カスタム属性カウンターが更新（インクリメントまたはデクリメント）されるたびに、[データポイントが]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)消費される。
{% endalert %}

### ユースケース:最初のキャンバスから2番目のキャンバスをトリガーする

この使用例では、2つのCanvasを作成し、最初のCanvasから2つ目のCanvasをトリガーするためにウェブフックを使用する。これは、ユーザーが別のキャンバスのあるポイントに到達したときのエントリートリガーのような役割を果たす。

1. 最初のキャンバスによってトリガーされるキャンバスである。 
2. キャンバスの**入力スケジュールで**、**API-Triggeredを**選択する。
3. **キャンバスIDを控えて**おくこと。これは後のステップで必要になる。
4. 2つ目のキャンバスのステップを作り続け、キャンバスを保存する。
5. 最後に、最初のキャンバスを作成する。2つ目のキャンバスをトリガーしたいステップを見つけ、ウェブフック付きの新しいステップを作成する。 

ウェブフックを設定する際は、以下を参照のこと：

- **Webhook URL:**あなたの\[RESTエンドポイントURL][7] の後に`canvas/trigger/send`.例えば、US-06のインスタンスの場合、URLは`https://rest.iad-06.braze.com/canvas/trigger/send` となる。
- **要求本文:**Raw Text

#### リクエストヘッダと方法

Brazeは認証のために、APIキーと`content-type` を宣言するHTTPヘッダーを要求する。

- **要求ヘッダー:**
  - **認可する：**ベアラー `YOUR_API_KEY`
  - **Content-Type:**application/json
- **HTTP メソッド:**POST

`YOUR_API_KEY` を、`canvas.trigger.send` 権限を持つ Braze API キーに置き換える。APIキーは、Brazeダッシュボードの**「設定」**>「**APIキー**」で作成できる。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**開発者コンソール**] > \[**API 設定**] から API キーを作成できます。
{% endalert %}

![][1]

#### Request body

テキストフィールドに`canvas/trigger/send` リクエストを追加する。詳細については、\[APIトリガー配信によるCanvasメッセージの送信][9] を参照のこと。以下は、このエンドポイントのリクエストボディの例である。`your_canvas_id` は、2番目のキャンバスのキャンバスIDである： 

{% raw %}
```json
{
      "canvas_id": "your_canvas_id",
      "recipients": [
        {
          "external_user_id": "{{${user_id}}}"
         }
      ]
}
```
{% endraw %}

## 知っておくべきこと

- Braze-to-BrazeのWebhookは、エンドポイントの[レート制限に]({{site.baseurl}}/api/api_limits/)従う。
- ユーザー・プロフィールの更新には追加の[データ・ポイントが]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count)発生するが、メッセージング・エンドポイントを通じて別のメッセージがトリガーされることはない。
- [匿名ユーザーを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)ターゲットにしたい場合は、Webhookのリクエスト本文で、`external_id` の代わりに`braze_id` を使うことができる。
- Braze-to-Brazeウェブフックを[テンプレートとして]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/)保存し、再利用することができる。
- [メッセージ・アクティビティ・ログを]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/)チェックして、ウェブフックの失敗を確認し、トラブルシューティングすることができる。


[1]: {% image_buster /assets/img_archive/webhook_settings.png %}
[2]: {{site.baseurl}}/api/basics/
[3]: {{site.baseurl}}/api/api_key/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/
[7]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
