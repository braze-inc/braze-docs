---
nav_title: Braze to Braze webhookを作成する
article_title: BrazeからBrazeへのWebhookを作成する
page_order: 3
channel:
  - webhooks
description: "この参考記事では、ユーザー更新とBraze to Braze webhookの使い分けについて説明している。また、Braze to Braze webhookの作成方法についても解説している。"

---

# Braze to Braze webhookを作成する

> Braze to Braze webhookは[、キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/)や[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/)内の[Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)を使用して、Braze内部から[Braze REST API]({{site.baseurl}}/api/basics/)を呼び出すことを可能にする。[APIトリガーのキャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を起動するといったオーケストレーションタスクにこれを使え。キャンバスから[ユーザー属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)、または[購入を]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)更新するには、代わりに[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)を使用する。ユーザープロファイルの変更に対応し、更新処理をより効率的に行うように設計されている。

この記事を最大限に活用するには、[webhookの仕組み]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)と、Brazeで[webhookを作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)する方法について理解しておく必要がある。

## ユーザーデータの変更にはユーザー更新を使用する

[カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)の変更、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)の記録、[購入の]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)記録を含む、キャンバス内からのユーザープロファイル更新には、Braze to Braze webhookではなく[User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)を使用する。 

ユーザー更新は複数の変更をまとめてバッチ処理で送信するため、Webhookよりも高速だ。Webhookよりも設定が簡単で、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer)を通じて複雑な更新をサポートする。例えば、ユーザーがメッセージを何回見たかを数えるには、Braze to Braze webhookではなく、User Updateの[インクリメントとデクリメント機能]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values)を使う。

{% alert tip %}
キャンバスに[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)を追加し、JSONコンポーザーを使ってユーザーの属性、イベント、購入履歴を更新する。
{% endalert %}

## Braze to Braze webhookの使用タイミング

ユーザー更新機能は、ユーザープロファイルを更新するためのBraze to Braze webhookとほぼ同じタスクを処理できる。単純なカスタム属性を超える複雑な更新には、[高度なJSONコンポーザー]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer)を使用できる。

Brazeのステップから直接ユーザーを更新する以外のシナリオで、Braze内部からBrazeの[REST API]({{site.baseurl}}/api/basics/)を呼び出す必要がある場合、Braze to Braze webhookを使用できる。一般的な例としては：

- 別のキャンバスから[APIトリガー型キャンバス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を起動する
- Braze内の1つのワークフローが、専用のキャンバスコンポーネントを持たないAPIを呼び出す必要があるオーケストレーションパターンにおいて、他の[メッセージングエンドポイントを]({{site.baseurl}}/api/endpoints/messaging/)呼び出すこと。

キャンバス内でのユーザー更新については、[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)を使用することを推奨する。

## 前提条件

BrazeからBrazeへのWebhookを作成するには、接続したいエンドポイントへの権限を持つ[API キー]({{site.baseurl}}/api/api_key/)が必要だ。例えば、APIトリガーのキャンバスを起動するには、その`canvas.trigger.send`権限を持つAPI キーが必要だ。

## Braze-to-Braze Webhook の設定

BrazeからBrazeへのWebhookを作成する一般的なワークフローは、以下のステップに従う：

1. キャンペーンまたはキャンバスのコンポーネントとして [ウェブフックを作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)します。 
2. [**空白のテンプレート**] を選択します。
3. **コンポーズ**タブで、APIのユースケースに合わせて**WebhookのURL**と**リクエストボディ**を指定する。
4. **設定**タブで、エンドポイントの要求に応じて**HTTPメソッド**と**リクエストヘッダー**を指定する。
5. 追加の配信設定（例：カスタムイベントからのトリガー）を構成し、キャンペーンまたはキャンバスの残りの部分を構築する。

## 最初のキャンバスから2番目のキャンバスをトリガーする

このユースケースでは、2つのキャンバスを作成し、BrazeからBrazeへのwebhookを使用して、最初のキャンバスから2番目のキャンバスをトリガーする。これは、ユーザーが別のキャンバス内の特定ポイントに到達したときのエントリトリガーのような役割を果たします。

1. まず、2 つ目のキャンバスを作成します。これは最初のキャンバスによってトリガーされるキャンバスです。
2. キャンバスの**エントリスケジュール**で、[**API トリガー**] を選択します。
3. **キャンバス ID** を書き留めます。後でこのステップが必要になる。
4. 続いて 2 つ目のキャンバスのステップを作成し、キャンバスを保存します。
5. 最後に、最初のキャンバスを作成する。2つ目のキャンバスをトリガーしたいステップを見つけ、ウェブフック付きの新しいステップを作成する。

ウェブフックを設定する際は、以下を参照のこと：

- **Webhook URL:**[REST エンドポイント URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) の後に `/canvas/trigger/send` を続けます。例えば `US-06` インスタンスの場合、URL は`https://rest.iad-06.braze.com/canvas/trigger/send` になります。
- **要求本文:**Raw Text

#### リクエストヘッダーと方法

Brazeは認証のためにHTTPヘッダーを必要とする。そのヘッダーにはAPI キーを含める必要がある。また、コンテンツタイプを宣言する別のヘッダーも必要だ。

- **リクエストヘッダー：**
  - **承認：** `Bearer YOUR_API_KEY`
  - **Content-Type:** `application/json`
- **HTTPメソッド：** `POST`

に、権限`canvas.trigger.send`を持つBraze API キーを`YOUR_API_KEY`置き換える。BrazeダッシュボードでAPI キーを作成するには、**設定**＞**API キー**に移動する。

![Brazeダッシュボードで、WebhookのリクエストヘッダーにAuthorizationとContent-Typeフィールドが表示される。]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Request body

テキストフィールドに`/canvas/trigger/send` リクエストを追加する。詳細は、[APIトリガーによる配信でCanvasメッセージを送信するを]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)参照のこと。以下はこのエンドポイントのリクエスト本文の例です。ここで `your_canvas_id` は、2 つ目のキャンバスのキャンバス ID です:

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

ユーザーが最初のキャンバスでこのWebhookステップに到達すると、BrazeはAPI経由でそのユーザーに対して2つ目のキャンバスをトリガーする。

## 考慮事項

- **ユーザー更新：**Canvasからのユーザープロファイル更新（属性、イベント、購入履歴）には、効率性と費用対効果を高めるため、Braze to Braze webhookではなく[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)機能を使用する。
- Braze to Braze webhookはエンドポイントの[レート制限]({{site.baseurl}}/api/api_limits/)の対象となる。
- ユーザープロファイルの更新は、全体の消費量にカウントされる[データポイントを]({{site.baseurl}}/user_guide/data/data_points/)生成する。一方、メッセージングエンドポイントを通じた別のメッセージの送信は、[データ]({{site.baseurl}}/user_guide/data/data_points/)ポイントを消費しない。
- [匿名ユーザー]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)を対象とするには、Webhookのリクエスト本文で  `external_id`の代わりに  `braze_id`を使用する。
- Braze to Braze webhookは、再利用可能な[Webhookテンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/)として保存できる。
- [メッセージアクティビティログを]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)チェックして、Webhook の失敗を確認し、トラブルシューティングすることができる。


