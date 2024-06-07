---
nav_title: Braze-to-Braze Webhook (ろう付け Webhook)
article_title: Braze-to-Braze Webhook (ろう付け Webhook)
page_order: 3
channel:
  - webhooks
description: "この記事では、主要なユースケースでBraze-to-Braze Webhookを作成する方法について説明します。"

---

# Braze-to-Braze Webhook (ろう付け Webhook)

> Webhookを使用してBraze [REST API][2]と通信し、基本的にAPIでできることはすべて行うことができます。これを Braze-to-Braze Webhook (Braze から Braze への通信を行う Webhook) と呼びます。

## 前提 条件

Braze-to-Braze Webhook を作成するには、アクセスするエンドポイントの権限を持つ [API キー][3] が必要です。

## ユースケース

Braze-to-Braze Webhook でできることはたくさんありますが、ここでは一般的なユースケースをいくつか紹介します。

- ユーザーがメッセージを受信したときにカウンターの整数カスタム属性をインクリメントします。
- 最初の Canvas から 2 つ目の Canvas をトリガーします。

{% alert tip %}
[ユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)をキャンバスに追加して、JSON コンポーザーでユーザーの属性、イベント、購入を追跡します。このようにして、これらの更新はバッチ処理されるため、BrazeはBraze-to-Braze Webhookよりも効率的に処理できます。
{% endalert %}

このページのユースケースは、Brazeの[Webhookの仕組み][4]と[Webhookの作成][5]の方法に精通していることを前提としています。

## Braze-to-Braze Webhook の作成手順

Webhook リクエストの詳細はユースケースごとに異なりますが、Braze-to-Braze Webhook を作成するための一般的なワークフローは同じです。

1. [Webhookを作成する][5] キャンペーンまたはキャンバスコンポーネントとして。 
2. **[Blank Template**] を選択します。
3. [ **作成** ] タブで、ユースケースのメモに従って **[Webhook URL** ] と **[要求本文** ] を指定します。
4. [ **設定** ] タブで、ユースケースのメモに従って **[HTTP メソッド** ] と **[要求ヘッダー** ] を指定します。
5. 必要に応じて、残りの Webhook の構築を続けます。一部のユースケースでは、カスタムイベントからキャンペーンやキャンバスをトリガーするなど、特定の配信設定が必要です。

### ユースケース：カウンターの整数カスタム属性をインクリメントする

このユースケースでは、カスタム属性を作成し、Liquidを使用して特定のアクションが発生した回数をカウントします。 

たとえば、ユーザーがアクティブなアプリ内メッセージキャンペーンを見た回数をカウントし、3回表示した後は再度キャンペーンを受け取らないようにすることができます。BrazeのLiquidロジックで何ができるかについては、 [Liquidのユースケースライブラリ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases)をご覧ください。

Braze-to-Braze Webhook を作成するための一般的な手順に従い、Webhook を設定する際に以下を参照してください。

- **Webhook URL:**[REST エンドポイント URL][7] の後に `/users/track`.たとえば、US-06 インスタンスの場合、URL は `https://rest.iad-06.braze.com/users/track`になります。
- **要求本文:**生のテキスト

#### 要求ヘッダーとメソッド

Brazeでは、認証のためにAPIキーを含むHTTPヘッダーと `content-type`、.

- **要求ヘッダー:**
  - **認可：**Bearer {YOUR\_API\_KEY}
  - **コンテンツタイプ:** application/json
- **HTTP メソッド:**ポスト:

`YOUR_API_KEY`権限のある`users.track`Braze APIキーに置き換えてください。APIキーは、Brazeダッシュボードの **[設定** ]> **[APIキー**]で作成できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**開発者コンソール**の **[API 設定**] > API キーを作成できます。
{% endalert %}

![][1]

#### リクエスト本文

リクエスト本文とLiquidにユーザートラックリクエストを追加して、カウンター変数を割り当てます。詳しくは[ユーザートラック][8]を参照してください。

以下は、このエンドポイントに必要な Liquid と要求本文の両方の例であり、 `your_attribute_count` はユーザーがメッセージを見た回数をカウントするために使用している属性です。 {% raw %}

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
カスタム属性カウンターが更新 (インクリメントまたはデクリメント) されるたびに、 [データ ポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/)が消費され、全体的な消費量にカウントされます。
{% endalert %}

### ユースケース：最初の Canvas から 2 つ目の Canvas をトリガーする

このユースケースでは、2 つの Canvas を作成し、Webhook を使用して最初の Canvas から 2 番目の Canvas をトリガーします。これは、ユーザーが別のキャンバスの特定のポイントに到達したときのエントリトリガーのように機能します。

1. まず、2 つ目の Canvas (最初の Canvas によってトリガーされる Canvas) を作成します。 
2. [Canvas **Entry Schedule (キャンバスエントリスケジュール**)] で [ **API トリガー]** を選択します。
3. **キャンバス ID** をメモします。これは後の手順で必要になります。
4. 2 つ目の Canvas のステップの作成を続行し、Canvas を保存します。
5. 最後に、最初のキャンバスを作成します。2 番目の Canvas をトリガーするステップを見つけ、Webhook を使用して新しいステップを作成します。 

Webhook を構成するときは、以下を参照してください。

- **Webhook URL:**[REST エンドポイント URL][7] の後に `canvas/trigger/send`.たとえば、US-06 インスタンスの場合、URL は `https://rest.iad-06.braze.com/canvas/trigger/send`になります。
- **要求本文:**生のテキスト

#### 要求ヘッダーとメソッド

Brazeでは、認証のためにAPIキーを含むHTTPヘッダーと `content-type`、.

- **要求ヘッダー:**
  - **認可：**持参人 `YOUR_API_KEY`
  - **コンテンツタイプ:** application/json
- **HTTP メソッド:**ポスト:

`YOUR_API_KEY`権限のある`canvas.trigger.send`Braze APIキーに置き換えてください。APIキーは、Brazeダッシュボードの **[設定** ]> **[APIキー**]で作成できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**開発者コンソール**の **[API 設定**] > API キーを作成できます。
{% endalert %}

![][1]

#### リクエスト本文

`canvas/trigger/send`テキストフィールドにリクエストを追加します。詳細は、[APIトリガー配信によるCanvasメッセージの送信][9]を参照してください。以下は、このエンドポイントの要求本文の例で、 `your_canvas_id` は 2 番目の Canvas の Canvas ID です。 

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

## 知っておきたいこと

- Braze-to-Braze Webhook には、エンドポイント [のレート制限]({{site.baseurl}}/api/api_limits/)が適用されます。
- ユーザー プロファイルを更新すると追加の [データ ポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count)が発生しますが、メッセージング エンドポイントを介して別のメッセージをトリガーすると発生しません。
- [匿名ユーザー]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles)をターゲットにする場合は、Webhook の要求本文ではなく、代わりに`external_id`使用できます`braze_id`。
- Braze-to-Braze Webhook を [テンプレート]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) として保存し、再利用することができます。
- [メッセージ アクティビティ ログ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/)を確認して、Webhook のエラーを表示およびトラブルシューティングできます。


[1]: {% image_buster /assets/img_archive/webhook_settings.png %}
[2]: {{site.baseurl}}/api/basics/
[3]: {{site.baseurl}}/api/api_key/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[6]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/
[7]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
