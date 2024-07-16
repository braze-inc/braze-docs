---
nav_title: Jampp
article_title:Jampp
alias: /partners/jampp/
description:"この参考記事では、モバイル顧客の獲得とリターゲティングに利用されるパフォーマンスマーケティングプラットフォームであるJamppとBrazeの提携について概説している。"
page_type: partner
search_tag:Partner

---

# Jampp

> [Jamppは](https://www.jampp.com/)、モバイル顧客を獲得しリターゲティングするためのパフォーマンスマーケティングプラットフォームである。Jamppは、行動データと予測テクノロジー、プログラマティックテクノロジーを組み合わせ、消費者にパーソナライゼーションされた広告を表示することで、広告主に収益をもたらす。

BrazeとJamppの統合により、BrazeユーザーはBrazeのWebhookイベントを介してJamppにイベントを同期できる。その結果、顧客はモバイル広告エコシステム内のリターゲティング・イニシアチブに、より豊富なデータセットを追加することができる。

広告で顧客をリターゲティングしたい場合の例をいくつか挙げる：
- 顧客のメールまたはプッシュサブスクリプションの状態が変化したとき。
- 顧客がBrazeのメッセージングキャンペーンとどのように関わったか。
- 顧客が特定のジオフェンスをトリガーした場合。

## 前提条件

この統合はiOSとAndroidアプリをサポートしている。

| 必要条件 | 説明 |
|---|---|
| Jamppアカウント | このパートナーシップを利用するには[Jamppアカウントが](https://www.jampp.com/)必要だ。 |
| AndroidアプリID | Android用のお客様固有のBrazeアプリケーション識別子（"com.example "など）。 |
| iOSアプリID | iOS用のお客様固有のBrazeアプリケーション識別子（"012345678 "など）。 |
| Braze SDKでIDFAコレクションをイネーブルメントする。 | IDFAコレクションはBraze SDK内ではオプションであり、デフォルトでは無効になっている。 | 
| カスタム属性によるGoogle広告IDの収集 | Google広告IDの収集は顧客の任意であり、\[カスタム属性][5] 。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:BrazeでWebhookテンプレートを作成する。

今後のキャンペーンやCanvasで使用するJampp Webhookテンプレートを作成するには、Brazeプラットフォームの「**テンプレート**>**Webhookテンプレート**」に移動する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**エンゲージメント**>**テンプレートとメディア**>**Webhookテンプレートに**移動する。
{% endalert %}

Jampp Webhookキャンペーンを単発で作成する場合や、既存のテンプレートを使用する場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **リクエスト・ボディ**Raw Text
- **WebhookのURL**：
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Webhook URLには、次のように記述する：
- イベント名を設定する。この名前はJamppダッシュボードに表示される。
- Android用（"com.example "など）、iOS用（"012345678 "など）のアプリ固有の識別子を渡す。
- トラッキングしているカスタム属性の[Liquidを][1]Google広告IDとして挿入する。なお、この例ではGoogleの広告IDが`aaid` と記載されているが、開発者が設定したカスタム属性名に置き換える必要がある。

![Braze to Braze Webhookビルダーに表示されるWebhook URLとメッセージプレビュー。][2]

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないので、これらの値を自分で保存する必要がある。このデータ収集にはユーザーの同意が必要な場合があることに注意すること。
{% endalert %}

#### リクエストヘッダーとメソッド

Jampp WebhookはHTTPメソッドとリクエストヘッダーを必要とする。

- **HTTPメソッド**：GET
- **リクエストヘッダー**：
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダー、HTTPメソッド、メッセージプレビュー。][3]

#### Request body

このWebhookのリクエスト・ボディを定義する必要はない。

### ステップ2:リクエストをプレビューする

メッセージをプレビューして、リクエストがさまざまなユーザーに対して適切にレンダリングされていることを確認する。AndroidとiOS両方のユーザーに対してプレビューとテストリクエストの送信を推奨する。リクエストが成功すると、APIは`HTTP 204` で応答する。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
