---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "ここでは、携帯顧客sの取得・リターゲティングに使用されるパフォーマンスマーケティング プラットフォームであるBrazeとJamppの提携について概説します。"
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/)は、携帯顧客sの取得およびリターゲティングに使用するパフォーマンスマーケティング プラットフォームです。Jamppは、行動データと予測テクノロジーおよびプログラムテクノロジーを組み合わせて、消費者が初めて購入するか、それよりも頻繁に購入するきっかけとなる個人的な関連性のある広告を表示することで、広告主の収益を生み出します。

Braze とJampp インテグレーションを使用すると、Braze ユーザー s がJampp にBraze Webhookを介してイベントを同期できます。そのため、顧客 s は、モバイル広告エコシステム内のリターゲティングイニシアチブに、より豊富なデータセットを追加できます。

広告でsをリターゲティングする 顧客したい場合の例:
- 顧客のメールまたはプッシュサブスクリプションのステートが変化したとき。
- 顧客とBraze メッセージング キャンペーンとの相互作用の仕方。
- 顧客がトリガー特定のジオフェンスを受け取った場合。

## 前提条件

この統合は、iOS とAndroid アプリ s をサポートします。

| 要件 | 説明 |
|---|---|
| Jampp勘定 | この提携の前倒しタグを行うには、[Jamppアカウント](https://www.jampp.com/)が必要です。 |
| Android アプリ番号 | Android用の一意のBraze アプリライケーション識別子("com.example"など)。 |
| iOS アプリ識別 | iOS 用の一意のBraze アプリライセンス識別子("012345678" など)。 |
| Braze SDKでのIDFA 収集の有効化 | IDFA 収集はBraze SDK内でオプションであり、デフォルトで無効になっています。 | 
| カスタム属性によるグーグル広告IDの収集 | Google 広告ID コレクションは顧客 s のオプションであり、\[カスタム属性][5] として収集できます。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:Braze でのWebhook テンプレートの作成

将来のキャンペーンs またはキャンバスで使用するJampp Webhook テンプレートを作成するには、Braze プラットフォームで**テンプレートs**>**Webhook テンプレートs** に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Engagement**> **Templates &Media**> **Webフックテンプレート** に移動します。
{% endalert %}

一度だけJampp Webhook キャンペーンしたい場合や、既設のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhook**を選択してください。

新しいWebフックテンプレートで、次のフィールドs を入力します。
- **リクエスト本文**:Raw Text
- **WebフックURL**:
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

Webhook では、次の操作を実行する必要があります。
- イベント名を設定します。この名前はあなたのJampp ダッシュボードの耳元をアプリします。
- Android("com.example"など)およびiOS("012345678"など)のアプリ固有のアプリライセンス識別子を渡します。
- グーグル広告IDとして"トラッキングしているアプリの適切なカスタム属性に[Liquid][1]を挿入します。この例では、Google の広告ID は`aaid` としてリストされていますが、開発者 s が設定したカスタム属性の名前に置き換える必要があります。

![Braze Webhook ビルダーに表示されるWebhookのURL およびメッセージプレビュー。][2]

{% alert important %}
Braze は自動的にIDFA/AAID を収集しないため、これらの値を自分で保存する必要があります。この情報を収集するには、ユーザーの同意を必要とする場合があることに注意してください。
{% endalert %}

#### リクエストヘッダーとメソッド

Jampp WebhookにはHTTP メソッドとリクエストヘッダーが必要です。

- **HTTP メソッド**:GET
- **リクエストヘッダー**:
  - **Content-Type**: application/json

![Braze Webhook ビルダに表示されるリクエストヘッダーs、HTTP メソッド、およびメッセージプレビュー。][3]

#### Request body

このWebhookのリクエストボディを定義する必要はありません。

### ステップ2:リクエストのプレビュー

リクエストがさまざまなユーザーに対して適切にレンダリングされていることを確認するために、メッセージをプレビューします。Android とiOS ユーザー s の両方のテストリクエストをプレビューして送信することをお勧めします。リクエストが成功した場合、API は`HTTP 204` で応答します。

{% alert important %}
テンプレートを保存してから退場してください！<br>更新されたWebhook テンプレートs は、新しい[Webhook キャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) を作成するときに**保存されたWebhook テンプレートs** 一覧にあります。
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
