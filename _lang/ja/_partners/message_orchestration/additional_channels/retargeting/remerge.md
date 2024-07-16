---
nav_title: Remerge
article_title:Remerge
alias: /partners/remerge/
description:"この参考記事では、BrazeとRemergeのパートナーシップについて概説している。Remergeは、大規模なリターゲティングのための専用アプリで、アプリのオーディエンスを効率的にセグメンテーションし、ユーザーをリターゲティングするためのツールを提供する。"
page_type: partner
search_tag:Partner

---

# Remerge

> [Remergeは](https://www.remerge.io/)、アプリオーディエンスを効率的にセグメンテーションし、ユーザーをリターゲティングするためのツールを備え、大規模なアプリリターゲティングのために構築されている。

BrazeとRemergeの統合は、Webhookイベントを通じてユーザーデータをRemergeに送信し、モバイルデマンドサイドプラットフォームを通じてユーザーをリターゲティングすることで、強固でクロスチャネルのライフサイクルマーケティングキャンペーンの開発を支援します。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アカウントをRemergeする | このパートナーシップを利用するにはRemergeアカウントが必要である。 |
| WebhookキーをRemergeする。 | この鍵はRemergeが提供する。 |
| AndroidアプリID | Android用のお客様固有のBrazeアプリケーション識別子（"com.example "など）。 |
| iOSアプリID | iOS用のお客様固有のBrazeアプリケーション識別子（"012345678 "など）。 |
| Braze SDKでIDFAコレクションをイネーブルメントする。 | IDFAコレクションはBraze SDK内ではオプションであり、デフォルトでは無効になっている。 | 
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:BrazeのWebhookテンプレートを作成する。

将来のキャンペーンやCanvas用にRemerge Webhookテンプレートを作成するには、Brazeプラットフォームの**テンプレート**>**Webhookテンプレートに**移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**エンゲージメント**>**テンプレートとメディア**>**Webhookテンプレートに**移動する。
{% endalert %}

単発のRemerge Webhookキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新規キャンペーン作成時にBrazeで**Webhookを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **リクエスト・ボディ**Raw Text
- **WebhookのURL**：
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Webhook URLには、次のように記述する：
- `https://remerge.events/event` APIを使用してWebhookイベントを送信する。
- イベント名を設定する。この名前は[remerge.ioの][65]ダッシュボードに表示される。
- Android用（"com.example "など）とiOS用（"012345678 "など）のアプリ固有の識別子をremergeに渡す。
- Remergeがこれを提供する。

![Braze to Braze Webhookビルダーに表示されるWebhook URLとメッセージプレビュー。][67]

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないので、これらの値を自分で保存する必要がある。このデータ収集にはユーザーの同意が必要な場合があることに注意すること。
{% endalert %}

#### リクエストヘッダーとメソッド

Remerge WebhookはHTTPメソッドとリクエストヘッダーを必要とする。

- **HTTPメソッド**：GET
- **リクエストヘッダー**：
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダー、HTTPメソッド、メッセージプレビュー。][68]

#### Request body

このWebhookのリクエスト・ボディを定義する必要はない。

## ステップ2:リクエストをプレビューする

メッセージをプレビューして、リクエストがさまざまなユーザーに対して適切にレンダリングされていることを確認する。AndroidとiOS両方のユーザーに対してプレビューとテストリクエストの送信を推奨する。リクエストが成功すると、APIは`HTTP 204` で応答する。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
