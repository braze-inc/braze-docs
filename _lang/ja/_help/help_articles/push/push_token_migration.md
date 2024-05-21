---
nav_title: プッシュトークンの移行
article_title: プッシュトークンの移行
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeに切り替えた後も引き続きユーザーにプッシュメッセージを送信できるように、プッシュトークンを移行する方法について説明します。"
channel: push
---

# プッシュトークンの移行

[プッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/)は、アプリの通知の送信先を指定する一意の匿名識別子です。Brazeは、Android用のFirebase Cloud Messaging Service(FCM)やiOS用のApple Push Notification Service(APNs)などのプッシュサービスプロバイダーと接続し、これらのプロバイダーはアプリを識別する一意のデバイストークンを送信します。Brazeを統合する前に、自社または別のプロバイダーを通じてプッシュ通知を送信していた場合、プッシュトークンの移行により、登録済みのプッシュトークンを使用してユーザーにプッシュ通知を送信し続けることができます。

## SDKによる自動移行

Braze SDKは、以前にプッシュ通知にオプトインしたユーザーがBrazeに統合されたアプリまたはサイトに初めてサインインしたときに、プッシュトークンを自動的に移行します。Braze SDKを統合すると、APIを使用してプッシュトークンを移行する必要がなくなります。

ただし、プッシュトークンはユーザーがアプリに初めてログインしたときに移行されるため、SDK統合後にログインしていないユーザーには、Brazeはプッシュ通知を送信できないことに注意してください。Android と iOS のプッシュ トークンを手動で移行して、これらのユーザーに再度関与する方法を引き続きお勧めします。

{% alert note %}
Web プッシュ トークンの性質上、トークンは ~60 日ごとに期限切れになり、リセットされます。その期間内にセッションを持たないユーザーは、アクティブな Web プッシュ トークンを持ちません。Brazeは、期限切れのWebプッシュトークンを移行しません。これらのユーザーは、 [プッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を通じて再エンゲージする必要があります。
{% endalert %}

## APIによる手動移行

プッシュトークンの手動移行は、以前に作成したキーをAPIを介してBrazeプラットフォームにインポートするプロセスです。

エンドポイントを使用して[`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)、iOS (APNs) と Android (FCM) のトークンをプラットフォームにプログラムで移行します。識別されたユーザー (外部 ID が関連付けられているユーザー) と匿名ユーザー (外部 ID を持たないユーザー) の両方を移行できます。

プッシュトークンの移行中にアプリを指定し `app_id` て、適切なプッシュトークンを適切なアプリに関連付けます。各アプリ(iOS、Androidなど)には独自の`app_id`、API[キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの**[識別**]セクションにあります。必ず正しいプラットフォームの `app_id`.

{% alert important %}
API を使用して Web プッシュ トークンを移行することはできません。これは、Web プッシュ トークンが他のプラットフォームと同じスキーマに準拠していないためです。 

<br>プログラムで Web プッシュ トークンを移行しようとすると、次のようなエラーが表示されることがあります。 `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
API の移行の代わりに、SDK を統合し、トークン ベースが自然に再入力されるようにすることをお勧めします。
{% endalert %}

### 外部 ID が存在する場合の移行
識別されたユーザーの場合は、フラグを に`false`設定 `push_token_import` (またはパラメーターを省略) し、ユーザー `attributes` オブジェクトに 、`app_id`、および`token`値を指定します`external_id`。 

例えば：

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

### 外部 ID が存在しない場合の移行
他のシステムからプッシュトークンをインポートする場合、常に `external_id` 使用できるとは限りません。この状況では、フラグを`push_token_import`次のように`true`設定し、 と `token` の値を指定します`app_id`。Brazeは、トークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人にメッセージを送信し続けることができるようにします。トークンがBrazeにすでに存在する場合、リクエストは無視されます。

例えば：

'''json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header '承認:ベアラー YOUR-API-KEY-HERE' \
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
'''

インポート後、匿名ユーザーがBraze対応バージョンのアプリを起動すると、BrazeはインポートしたプッシュトークンをBrazeユーザープロファイルに自動的に移動し、一時プロファイルをクリーンアップします。

Brazeは月に一度、プッシュトークンを持たないフラグを持つ `push_token_import` 匿名のプロフィールを探します。匿名プロファイルにプッシュトークンがなくなった場合は、プロファイルを削除します。ただし、匿名プロファイルにプッシュトークンが残っていて、実際のユーザーがそのプッシュトークンを使用してデバイスにログインしていないことが示唆されている場合は、何もしません。

## Android プッシュトークンのインポート

{% alert important %}
iOSアプリにはプッシュを表示するためのフレームワークが1つしかなく、Brazeに必要なプッシュトークンと証明書がある限り、プッシュ通知はすぐにレンダリングされるため、iOSアプリではこれらの手順は必要ありません。
{% endalert %}

Braze SDKの統合が完了する前にAndroidのプッシュ通知をユーザーに送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証します。 

プッシュペイロードを処理および表示するレシーバーが必要です。プッシュペイロードを受信者に通知するには、必要なキーと値のペアをプッシュキャンペーンに追加します。これらのペアの値は、Brazeの前に使用していた特定のプッシュパートナーによって異なります。

{% alert note %}
一部のプッシュ通知プロバイダーでは、Brazeはキーと値のペアを平坦化して、適切に解釈できるようにする必要があります。特定の Android アプリのキーと値のペアをフラット化するには、カスタマー オンボーディング マネージャーまたはサクセス マネージャーにお問い合わせください。
{% endalert %}

_最終更新日:2022年12月5日_
