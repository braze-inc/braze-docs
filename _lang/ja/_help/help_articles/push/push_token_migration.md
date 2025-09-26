---
nav_title: プッシュトークンを移行する
article_title: プッシュトークンを移行する
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeに切り替えた後もユーザーにプッシュメッセージを送信できるように、プッシュトークンを移行する方法について説明する。"
channel: push
---

# プッシュトークンを移行する

> [プッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) は、アプリの通知の送信先を指定する一意の匿名識別子です。Brazeは、AndroidのFirebase Cloud Messaging Service（FCM）やiOSのApple Push Notification Service（APN）のようなプッシュサービスプロバイダーと接続し、これらのプロバイダーは、あなたのアプリを識別するユニークなデバイストークンを送信する。Brazeを統合する前に、自社または他のプロバイダー経由でプッシュ通知を送信していた場合、プッシュトークンの移行により、プッシュトークンを登録したユーザーにプッシュ通知を送信し続けることができる。

## SDKによる自動移行

[Braze SDK を統合]({{site.baseurl}}/developer_guide/sdk_integration/)すると、オプトインしたユーザーのプッシュトークンは、ユーザーが次にアプリを開いたときに自動的に移行されます。それまでは、Braze を通じてそれらのユーザーにプッシュ通知を送ることはできません。

あるいは、[プッシュトークンを手動で移行する](#manual-migration-via-api)ことで、ユーザーへの再エンゲージをより迅速に行うことができます。

### Webトークンに関する考察

Web プッシュトークンの性質上、Web プッシュを実装する際には以下の点を考慮してください。

|検討|詳細|
|----------------------|------------|
| **サービスワーカー**  | デフォルトでは、Web SDK は `manageServiceWorkerExternally` や `serviceWorkerLocation` のような別のオプションが指定されない限り、`./service-worker` でサービスワーカーを探します。サービスワーカーの設定が適切でないと、ユーザーのプッシュトークンが期限切れになる可能性があります。 |
| **期限切れトークン**   | ユーザーが60日以内にWebセッションを開始しなかった場合、そのプッシュトークンは失効する。Braze は期限切れのプッシュトークンを移行できないので、再エンゲージするには[プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を送信する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API経由の手動移行

手動プッシュトークンマイグレーションは、これらの以前に作成されたキーを、APIを通じてBrazeプラットフォームにインポートするプロセスである。

[`users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を使用して、iOS (APN s) およびAndroid (FCM) トークンs をプラットフォームにプログラムで移行します。特定ユーザー（関連する外部IDを持つユーザー）と匿名ユーザー（外部IDを持たないユーザー）の両方を移行できる。

プッシュトークン移行時にアプリの`app_id` を指定し、適切なプッシュトークンを適切なアプリに関連付ける。各アプリ（iOS、Androidなど）にはそれぞれ`app_id` 、[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの**Identification**セクションで確認できる。必ず正しいプラットフォームの`app_id` を使用すること。

{% alert important %}
API を使用してウェブプッシュトークンを移行することはできません。これは、ウェブ・プッシュ・トークンが他のプラットフォームと同じスキーマに準拠していないためだ。 

<br>ウェブプッシュトークンをプログラムで移行しようとすると、次のようなエラーが表示されることがあります。 `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
APIマイグレーションの代わりに、SDKを統合し、トークン基盤が自然に再集積できるようにすることをお勧めします。
{% endalert %}

{% tabs local %}
{% tab external ID が存在する %}
識別されたユーザーの場合は、`push_token_import` フラグを`false` に設定 (またはパラメーターを省略) して、`external_id`、`app_id`、`token` の値をユーザー `attributes` オブジェクトで指定します。 

以下に例を示します。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab external ID が見つからない %}
他のシステムからプッシュトークンをインポートする場合、`external_id` が利用できるとは限らない。この状況では、`push_token_import` フラグを`true` に設定し、`app_id` と`token` の値を指定します。Braze は、トークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送信し続けられるようにします。トークンがすでにBrazeに存在する場合、リクエストは無視される。

以下に例を示します。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

インポート後、匿名ユーザーがBraze対応バージョンのアプリを起動すると、Brazeは自動的にインポートしたプッシュトークンをBrazeユーザープロファイルに移動し、一時的なプロファイルをクリーンアップする。

Braze は月に1回チェックを実行し、プッシュトークンがない `push_token_import` フラグが設定された匿名プロファイルを見つけます。匿名プロフィールにプッシュトークンがなくなった場合、プロフィールを削除する。しかし、匿名プロファイルがまだプッシュトークンを持っていて、実際のユーザーがまだそのプッシュトークンでデバイスにログインしていないことを示唆している場合は、何もしない。
{% endtab %}
{% endtabs %}

## Androidのプッシュトークンをインポートする

{% alert important %}
以下の考慮事項は Android アプリにのみ適用されます。iOS アプリでは、プッシュを表示するためのフレームワークがプラットフォームに1つしかないため、これらのステップは必要ありません。また、Braze に必要なプッシュトークンと証明書がある限り、プッシュ通知は即時にレンダリングされます。
{% endalert %}

Braze SDKの統合が完了する前にAndroidプッシュ通知をユーザーに送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証する。 

プッシュペイロードを処理し表示するレシーバーが必要である。プッシュペイロードをレシーバーに通知するには、必要なキーと値のペアをプッシュキャンペーンに追加する。これらのペアの値は、ブレイズの前に使用した特定のプッシュパートナーによって決まる。

{% alert note %}
プッシュ通知プロバイダーによっては、Brazeが適切に解釈できるように、キーと値のペアをフラットにする必要がある。特定のAndroidアプリのキーと値のペアをフラットにするには、カスタマー・オンボーディングまたはサクセス・マネージャーに連絡する。
{% endalert %}

_最終更新日：2022年12月5日_
