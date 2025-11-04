---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "このリファレンス記事では、Braze と Jampp のパートナーシップについて説明します。Jampp は、モバイルの顧客の獲得とリターゲティングに利用されるパフォーマンスマーケティングプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) はモバイルの顧客の獲得とリターゲティングに利用されるパフォーマンスマーケティングプラットフォームです。Jampp は、行動データと予測技術やプログラム技術を組み合わせて、消費者に対して初めての購入やより頻繁な購入を促すパーソナルで関連性の高い広告を表示することで、広告主の収益を創出します。

_この統合は Jampp によって管理されます。_

## 統合について

Braze と Jampp の統合により、Braze ユーザーは Braze Webhook イベントを使用してイベントを Jampp に同期できます。その結果、お客様はモバイル広告エコシステム内で、より豊富なデータセットを各自のリターゲティングイニシアチブに追加できます。

広告で顧客をリターゲティングする状況の例を以下に示します。
- 顧客のメールまたはプッシュサブスクリプションのステートが変化したとき。
- 顧客とBraze メッセージング キャンペーンとの相互作用の仕方。
- 顧客が特定のジオフェンスをトリガーした場合。

## 前提条件

この統合はiOSとAndroidアプリをサポートしている。

| 要件 | 説明 |
|---|---|
| Jampp アカウント | このパートナーシップを活用するには、[Jampp アカウント](https://www.jampp.com/)が必要です。 |
| Android アプリ ID | Android用Brazeアプリケーション固有の識別子（「com.example 」など）。 |
| iOSアプリID | iOS用のお客様固有のBrazeアプリケーション識別子（"012345678 "など）。 |
| Braze SDKでIDFAコレクションを有効にする | IDFA 収集は Braze SDK 内ではオプションであり、デフォルトでは無効になっています。 | 
| カスタム属性によるグーグル広告IDの収集 | Google 広告 ID の収集は顧客向けのオプションであり、[[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types)]として収集できます。
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ1:Braze でのWebhook テンプレートの作成

将来のキャンペーンs またはキャンバスで使用するJampp Webhook テンプレートを作成するには、Braze プラットフォームで**テンプレートs**>**Webhook テンプレートs** に移動します。

一度だけJampp Webhook キャンペーンしたい場合や、既設のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhook**を選択してください。

新しい Webhook テンプレートで、次のフィールドに入力します。
- **リクエスト本文**:Raw Text
- **Webhook URL**:
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

Webhook URL で次の操作を行う必要があります。
- イベント名を設定します。この名前は Jampp ダッシュボードに表示されます。
- Android と iOS のアプリの一意のアプリケーション識別子 (Android:「com.example」、iOS:「012345678」など) を渡します。
- Google 広告 ID として追跡している適切なカスタム属性の [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) を挿入します。この例では、Google 広告 ID が `aaid` としてリストされていますが、これを開発者が設定したカスタム属性名に置き換える必要があります。

![Braze Webhook ビルダーに表示される Webhook URL とメッセージプレビュー。]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないので、これらの値を自分で保存する必要がある。このデータを収集するには、ユーザーの同意を必要とする場合があることに注意してください。
{% endalert %}

#### リクエストヘッダと方法

Jampp WebhookにはHTTP メソッドとリクエストヘッダーが必要です。

- **HTTPメソッド**：GET
- **リクエストヘッダー**:
  - **Content-Type**: application/json

![リクエストヘッダ、HTTPメソッド、メッセージプレビューがBraze webhookビルダーに表示される。]({% image_buster /assets/img/jampp_method.png %})

#### Request body

このウェブフックのリクエスト・ボディを定義する必要はない。

### ステップ2:リクエストをプレビューする

メッセージをプレビューして、リクエストがさまざまなユーザーに対して正しくレンダリングされていることを確認する。AndroidとiOSの両方のユーザーに対して、プレビューとテストリクエストの送信を推奨する。リクエストが成功すれば、APIは`HTTP 204` で応答する。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}


