---
nav_title: プッシュトークンの移行
article_title: プッシュトークンの移行
page_order: 0

page_type: solution
description: "このヘルプ記事では、プッシュトークンの移行方法について説明しているため、Brazeに切り替えた後もユーザーにプッシュメッセージを送信し続けることができる。"
channel: push
---

# プッシュトークンを移行する

[プッシュトークンは]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/)、アプリの通知をどこに送るかを指定する一意の匿名識別子である。Brazeは、AndroidのFirebase Cloud Messaging Service（FCM）やiOSのApple Push Notification Service（APN）のようなプッシュサービスプロバイダーと接続し、これらのプロバイダーは、アプリを識別するユニークなデバイストークンを送信する。Brazeを統合する前に、独自または他のプロバイダーを通じてプッシュ通知を送信していた場合、プッシュトークンの移行により、登録したプッシュトークンを持つユーザーにプッシュ通知を送信し続けることができる。

## SDKによる自動移行

Braze SDKは、過去にプッシュ通知をオプトインしたユーザーのプッシュトークンを、Brazeと統合されたアプリやサイトに初めてサインインした時に自動的に移行する。Braze SDKを統合すれば、APIを使ってプッシュトークンを移行する必要はない。

ただし、プッシュトークンはユーザーがアプリに初めてログインしたときに移行するため、SDK統合後にログインしていないユーザーにはプッシュ通知を送信できないことに注意。これらのユーザーと再度エンゲージメントする方法として、AndroidとiOSのプッシュトークンを手動で移行することもできる。

{% alert note %}
Webプッシュトークンの性質上、トークンは〜60日ごとに期限切れとなり、リセットされる。その期間内にセッションがない人は、アクティブなWebプッシュトークンを持っていないことになる。Brazeは期限切れのWebプッシュトークンを移行しない。このようなユーザーには、[プッシュ・プライマーを通じて]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)再エンゲージメントを図る必要がある。
{% endalert %}

## API経由の手動移行

手動のプッシュトークンマイグレーションは、これらの以前に作成したキーをAPIを通じてお客様のBrazeプラットフォームにインポートするプロセスである。

[`users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)使用して、iOS (APN) および Android (FCM) トークンをプラットフォームへプログラム的に移行する。識別子ユーザー（関連する外部IDを持つユーザー）と匿名ユーザー（外部IDを持たないユーザー）の両方を移行できる。

プッシュトークン移行時にアプリの`app_id` を指定し、適切なプッシュトークンを適切なアプリに関連付ける。各アプリ（iOS、Androidなど）にはそれぞれ`app_id` 、[APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの**Identification**セクションで確認できる。必ず正しいプラットフォームの`app_id` を使用すること。

{% alert important %}
APIを通じてWebプッシュトークンを移行することはできない。これは、Webプッシュトークンが他のプラットフォームと同じスキーマに準拠していないためだ。 

<br>Webプッシュトークンをプログラムで移行しようとすると、次のようなエラーが表示されることがある： `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
APIマイグレーションの代替として、SDKを統合し、トークン・ベースが自然に再投入されるようにすることをお勧めする。
{% endalert %}

### 外部IDが存在する場合は移行する
識別子ユーザーの場合は、`push_token_import` フラグを`false` に設定し（またはパラメータを省略し）、ユーザー`attributes` オブジェクトに`external_id` 、`app_id` 、`token` の値を指定する。 

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

### 外部IDが存在しない場合の移行
他のシステムからプッシュトークンをインポートする場合、`external_id` が利用できるとは限らない。この場合、`push_token_import` のフラグを`true` と設定し、`app_id` と`token` の値を指定する。Brazeは、トークンごとに一時的な匿名ユーザープロファイルを作成し、これらの個人へのメッセージを継続できるようにする。トークンがすでにBrazeに存在する場合、リクエストは無視される。

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

インポート後、匿名ユーザーがアプリのBraze対応バージョンを起動すると、Brazeは自動的にインポートしたプッシュトークンをユーザープロファイルに移動し、一時的なプロファイルをクリーンアップする。

Brazeは月に一度、`push_token_import` フラグを持つ匿名プロファイルで、プッシュトークンを持っていないものをチェックする。匿名プロファイルにプッシュトークンがなくなった場合、プロファイルを削除する。しかし、匿名プロファイルにまだプッシュトークンが残っていて、実際のユーザーがまだそのプッシュトークンを使ってデバイスにログインしていないことを示唆している場合は、何もしない。

## Androidプッシュトークンをインポートする

{% alert important %}
iOSアプリには、プッシュを表示するためのフレームワークが1つしかなく、プッシュ通知に必要なプッシュトークンと証明書があれば、プッシュ通知はすぐにレンダリングされるため、これらのステップは必要ない。
{% endalert %}

Braze SDKの統合が完了する前にユーザーにAndroidプッシュ通知を送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証する。 

プッシュペイロードを処理し表示するレシーバーが必要である。プッシュペイロードを受信者に通知するには、必要なキーと値のペアをプッシュキャンペーンに追加する。これらのペアの値は、Brazeの前に使用した特定のプッシュ・パートナーによって決まる。

{% alert note %}
プッシュ通知プロバイダーによっては、Brazeがキーと値のペアをフラットにし、適切に解釈できるようにする必要がある。特定のAndroidアプリのキーと値のペアをフラットにするには、顧客オンボーディングまたはサクセスマネージャーに連絡する。
{% endalert %}

_最終更新日：2022年12月5日_
