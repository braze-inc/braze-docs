---
nav_title: リマージ
article_title: リマージ
alias: /partners/remerge/
description: "この参考記事では、BrazeとRemergeのパートナーシップについて概説している。Remergeは、大規模なリターゲティングのための専用アプリで、アプリのオーディエンスを効率的にセグメントし、ユーザーをリターゲティングするためのツールを提供する。"
page_type: partner
search_tag: Partner

---

# リマージ

> [Remergeは](https://www.remerge.io/)、アプリのオーディエンスを効率的にセグメント化し、ユーザーをリターゲティングするためのツールを提供し、大規模なアプリのリターゲティングのために構築されている。

BrazeとRemergeの統合は、Webhookイベントを通じてRemergeにユーザーデータを送信し、モバイルデマンドサイドプラットフォームを通じてユーザーのリターゲティングを支援することで、強固でクロスチャネルのライフサイクルマーケティングキャンペーンの開発を支援する。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アカウントをリマージする | このパートナーシップを利用するには、リマージ・アカウントが必要である。 |
| ウェブフック・キーをリマージする | このキーはRemergeが提供する。 |
| AndroidアプリID | Android用Brazeアプリケーション固有の識別子（「com.example 」など）。 |
| iOSアプリID | iOS用のお客様固有のBrazeアプリケーション識別子（"012345678 "など）。 |
| Braze SDKでIDFAコレクションを有効にする | IDFAコレクションはBraze SDK内ではオプションであり、デフォルトでは無効になっている。 | 
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:BrazeのWebhookテンプレートを作成する

将来のキャンペーンやCanvas用にRemergeウェブフックテンプレートを作成するには、Brazeプラットフォームの**テンプレート**>**ウェブフックテンプレートに**移動する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Engagement（エンゲージメント）**」＞「**Templates & Media（テンプレート＆メディア**）」＞「**Webhook Templates（ウェブフック・テンプレート**）」と進む。
{% endalert %}

単発のRemergeウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**ウェブフックを**選択する。

新しいWebhookテンプレートで、以下のフィールドに記入する：
- **リクエスト・ボディ**Raw Text
- **ウェブフックのURL**：
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

ウェブフックのURLには、次のように記述する：
- `https://remerge.events/event` APIを使ってウェブフック・イベントを送信する。
- イベント名を設定する。この名前はダッシュボードに表示される。 [remerge.io][65]ダッシュボードに表示される。
- リマージには、Android用（"com.example"など）とiOS用（"012345678 "など）のアプリ固有のアプリケーション識別子を渡す。
- Remergeがこれを提供する。

![Brazeウェブフックビルダーに表示されるウェブフックURLとメッセージプレビュー。][67]

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないので、これらの値を自分で保存する必要がある。このデータを収集するには、ユーザーの同意が必要な場合があることに注意すること。
{% endalert %}

#### リクエストヘッダと方法

RemergeウェブフックはHTTPメソッドとリクエストヘッダを必要とする。

- **HTTPメソッド**：GET
- **ヘッダーを要求する**：
  - **Content-Type**: application/json

![リクエストヘッダ、HTTPメソッド、メッセージプレビューがBraze webhookビルダーに表示される。][68]

#### Request body

このウェブフックのリクエスト・ボディを定義する必要はない。

## ステップ2:リクエストをプレビューする

メッセージをプレビューして、リクエストがさまざまなユーザーに対して正しくレンダリングされていることを確認する。AndroidとiOSの両方のユーザーに対して、プレビューとテストリクエストの送信を推奨する。リクエストが成功すれば、APIは`HTTP 204` で応答する。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
