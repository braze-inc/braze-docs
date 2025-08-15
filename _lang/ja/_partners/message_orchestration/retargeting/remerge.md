---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "このリファレンス記事では、Braze と Remerge のパートナーシップについて説明します。Remerge は、大規模なリターゲティングのための専用アプリであり、アプリのオーディエンスを効率的にセグメント化し、ユーザーをリターゲティングするツールを備えています。"
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) は、大規模なリターゲティングのための専用アプリであり、アプリのオーディエンスを効率的にセグメント化し、ユーザーをリターゲティングするツールを備えています。

_この統合は Remerge によって管理されます。_

## 統合について

Braze と Remerge の統合により、ユーザーデータを Webhook イベント経由で Remerge に送信し、モバイルデマンドサイドプラットフォームでユーザーのリターゲティングを支援することで、堅牢なクロスチャネルのライフサイクルマーケティングキャンペーンを開発できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Remerge アカウント | このパートナーシップを活用するには、Remerge アカウントが必要です。 |
| Remerge Webhook キー | このキーは Remerge から提供されます。 |
| AndroidアプリID | Android用Brazeアプリケーション固有の識別子（「com.example 」など）。 |
| iOSアプリID | iOS用のお客様固有のBrazeアプリケーション識別子（"012345678 "など）。 |
| Braze SDKでIDFAコレクションを有効にする | IDFAコレクションはBraze SDK内ではオプションであり、デフォルトでは無効になっている。 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:BrazeのWebhookテンプレートを作成する

今後のキャンペーンまたはキャンバス用の Remerge Ｗebhook テンプレートを作成するには、Braze プラットフォームの [**テンプレート**] > [**Webhook テンプレート**] に移動します。 

単発のRemergeウェブフックキャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeの**ウェブフックを**選択する。

新しいWebhookテンプレートに、次のフィールドに記入してください:
- **リクエスト本文**:Raw Text
- **Webhook URL**:
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

Webhook URL で次の操作を行う必要があります。
- `https://remerge.events/event` APIを使ってウェブフック・イベントを送信する。
- イベント名を設定する。この名前は [remerge.io](https://www.remerge.io/) ダッシュボードに表示されます。
- Android と iOS のアプリの一意のアプリケーション識別子 (Android:「com.example」、iOS:「012345678」など) を Remergeに渡します。
- キーを定義します。これは Remerge から提供されます。

![Braze Webhook ビルダーに表示される Webhook URL とメッセージプレビュー。]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
BrazeはデバイスのIDFA/AAIDを自動的に収集しないので、これらの値を自分で保存する必要がある。このデータを収集するには、ユーザーの同意を必要とする場合があることに注意してください。
{% endalert %}

#### リクエストヘッダと方法

RemergeウェブフックはHTTPメソッドとリクエストヘッダを必要とする。

- **HTTPメソッド**：GET
- **リクエストヘッダー**:
  - **Content-Type**: application/json

![Braze Webhook ビルダーに表示されるリクエストヘッダー、HTTP メソッド、メッセージプレビュー。]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Request body

このウェブフックのリクエスト・ボディを定義する必要はない。

## ステップ2:リクエストをプレビューする

メッセージをプレビューして、リクエストがさまざまなユーザーに対して正しくレンダリングされていることを確認する。AndroidとiOSの両方のユーザーに対して、プレビューとテストリクエストの送信を推奨する。リクエストが成功すれば、APIは`HTTP 204` で応答する。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}


