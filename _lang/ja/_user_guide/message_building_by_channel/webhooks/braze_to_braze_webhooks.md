---
nav_title: Braze-to-Braze Webhook の作成
article_title: Braze-to-Braze Webhook の作成
page_order: 3
channel:
  - webhooks
description: "この記事では、主なユースケースのために Braze-to-Braze Webhook を作成する方法について説明します。"

---

# Braze-to-Braze Webhook の作成

> Webhook を使用して、Braze [REST API]({{site.baseurl}}/api/basics/) と通信できます。基本的には、Braze の API でできるすべての操作を実行できます。弊社では、このように Braze から Braze へ通信する Webhook のことを Braze-to-Braze Webhook と呼んでいます。このページのユースケースは、[Webhook の仕組み]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)と [Braze で Webhook を作成する方法]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)をすでに理解していることを前提としています。

## 前提条件

Braze-to-Braze Webhook を作成するには、目的のエンドポイントの権限を持つ [APIキー]({{site.baseurl}}/api/api_key/) が必要です。

## Braze-to-Braze Webhook の設定

Webhook リクエストの詳細はユースケースによって異なりますが、Braze-to-Braze Webhook を作成するための一般的なワークフローは変わりません。

1. キャンペーンまたはキャンバスのコンポーネントとして [ウェブフックを作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)します。 
2. [**空白のテンプレート**] を選択します。
3. [**Compose**] タブで、[**Webhook URL**] と [**リクエスト本文**] をユースケースに応じて指定します。
4. [**設定**] タブで、[**HTTP メソッド**] と [**リクエストヘッダー**] を指定します。
5. 必要に応じて、Webhook の残りの部分を引き続き作成します。ユースケースによっては、カスタムイベントからキャンペーンやキャンバスをトリガーするなど、特定の配信設定が必要なものもあります。

## ユースケース

Braze-to-Braze Webhook を使用すると多くのことができますが、使用を開始するには以下のユースケースがあります。

- ユーザがメッセージを受信すると、カウンタのカスタム属性（整数）をインクリメントする。
- 最初のキャンバスから2番目のキャンバスをトリガーする。

{% alert tip %}
[ユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)をキャンバスに追加して、ユーザーの属性、イベント、および購入を JSON 作成画面で追跡します。こうすると更新がバッチ処理され、Braze が Braze-to-Braze Webhook よりも効率的に更新を処理できます。
{% endalert %}

### ユースケース:カウンターの整数カスタム属性をインクリメントする

この使用例では、カスタム属性を作成し、特定のアクションが発生した回数をカウントするためにLiquidを使用する。 

例えば、ユーザーがアクティブなアプリ内メッセージ・キャンペーンを何回見たかをカウントし、3回見たら二度とキャンペーンを受け取らないようにしたい場合がある。Braze の Liquid ロジックでできることのアイデアについては、[Liquid ユースケースライブラリ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)を参照してください。

Braze-to-BrazeのWebhookを作成するための一般的な手順に従い、Webhookを設定する際には以下を参照すること：

- **Webhook URL:**[REST エンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) の後に `/users/track` を続けます。例えば `US-06` インスタンスの場合、URL は`https://rest.iad-06.braze.com/users/track` になります。
- **要求本文:**Raw Text

#### リクエストヘッダと方法

Braze には、API キーを含む認証用の HTTP ヘッダーと、`content-type` を宣言する別の HTTP ヘッダーが必要です。

- **要求ヘッダー:**
  - **認証:**ベアラー {YOUR_API_KEY}
  - **Content-Type:**application/json
- **HTTP メソッド:**POST

`YOUR_API_KEY` を、`users.track` 権限を持つ Braze API キーに置き換えます。APIキーは、Brazeダッシュボードの**「設定」**>「**APIキー**」で作成できる。

![Webhookのリクエストヘッダーs。]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

リクエスト本文にユーザー追跡リクエストと、カウンター変数を代入する Liquid を追加します。詳細については、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を参照してください。

以下は、このエンドポイントに必要なLiquid とリクエストボディの両方の例です。ここで、`your_attribute_count` は、ユーザーがメッセージを表示した回数を数えるために使用する属性です。

{% raw %}
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
カスタム属性カウンターが更新 (増加または減少) されるたびに、[データポイント]({{site.baseurl}}/user_guide/data/data_points/)が消費され、これは総消費量に加算されます。
{% endalert %}

### ユースケース:最初のキャンバスから2番目のキャンバスをトリガーする

この使用例では、2つのCanvasを作成し、最初のCanvasから2つ目のCanvasをトリガーするためにウェブフックを使用する。これは、ユーザーが別のキャンバス内の特定ポイントに到達したときのエントリトリガーのような役割を果たします。

1. まず、2 つ目のキャンバスを作成します。これは最初のキャンバスによってトリガーされるキャンバスです。 
2. キャンバスの**エントリスケジュール**で、[**API トリガー**] を選択します。
3. **キャンバス ID** を書き留めます。これは後のステップで必要になる。
4. 続いて 2 つ目のキャンバスのステップを作成し、キャンバスを保存します。
5. 最後に、最初のキャンバスを作成する。2つ目のキャンバスをトリガーしたいステップを見つけ、ウェブフック付きの新しいステップを作成する。 

ウェブフックを設定する際は、以下を参照のこと：

- **Webhook URL:**[REST エンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) の後に `canvas/trigger/send` を続けます。例えば、US-06 のインスタンスの場合、URL は `https://rest.iad-06.braze.com/canvas/trigger/send` となります。
- **要求本文:**Raw Text

#### リクエストヘッダと方法

Braze には、API キーを含む認証用の HTTP ヘッダーと、`content-type` を宣言する別の HTTP ヘッダーが必要です。

- **要求ヘッダー:**
  - **認証:**ベアラー `YOUR_API_KEY`
  - **Content-Type:**application/json
- **HTTP メソッド:**POST

`YOUR_API_KEY` を、`canvas.trigger.send` 権限を持つ Braze API キーに置き換えます。APIキーは、Brazeダッシュボードの**「設定」**>「**APIキー**」で作成できる。

![Webhookのリクエストヘッダーs。]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

テキストフィールドに`canvas/trigger/send` リクエストを追加する。詳細については、[API トリガー配信によるキャンバスメッセージの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を参照してください。以下はこのエンドポイントのリクエスト本文の例です。ここで `your_canvas_id` は、2 つ目のキャンバスのキャンバス ID です: 

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

- Braze-to-Braze Webhook は、エンドポイントの[レート制限]({{site.baseurl}}/api/api_limits/)の対象となります。
- ユーザー・プロフィールの更新には追加の[データ・ポイントが]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count)発生するが、メッセージング・エンドポイントを通じて別のメッセージがトリガーされることはない。
- [匿名ユーザー]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)をターゲットにしたい場合は、Webhook のリクエスト本文で、`external_id` の代わりに`braze_id` を使用できます。
- Braze-to-Braze Webhook を[template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) として保存し、再度使用することができます。
- [メッセージアクティビティログを]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)チェックして、Webhook の失敗を確認し、トラブルシューティングすることができる。


