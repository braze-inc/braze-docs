---
nav_title: プッシュトークンを移行する
article_title: プッシュトークンを移行する
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeに切り替えた後もユーザーにプッシュメッセージを送信できるように、プッシュトークンを移行する方法について説明する。"
channel: push
---

# プッシュトークンを移行する

[プッシュトークンは]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/)、アプリの通知先を指定する一意の匿名識別子である。Brazeは、AndroidのFirebase Cloud Messaging Service（FCM）やiOSのApple Push Notification Service（APN）のようなプッシュサービスプロバイダーと接続し、これらのプロバイダーは、あなたのアプリを識別するユニークなデバイストークンを送信する。Brazeを統合する前に、自社または他のプロバイダー経由でプッシュ通知を送信していた場合、プッシュトークンの移行により、プッシュトークンを登録したユーザーにプッシュ通知を送信し続けることができる。

## SDKによる自動移行

Braze SDKは、過去にプッシュ通知をオプトインしたユーザーのプッシュトークンを、Brazeと統合されたアプリやサイトに初めてサインインした時に自動的に移行する。Braze SDKを統合すれば、APIを使用してプッシュトークンを移行する必要はない。

ただし、プッシュトークンはユーザーがアプリに最初にログインしたときに移行するため、SDK統合後にログインしていないユーザーにはBrazeからプッシュ通知を送信できないことに注意。これらのユーザーと再びエンゲージする方法として、AndroidとiOSのプッシュトークンを手動で移行することを望むかもしれない。

{% alert note %}
ウェブ・プッシュ・トークンの性質上、トークンは60日ごとに期限切れとなり、リセットされる。その期間内にセッションを持たない者は、アクティブなウェブ・プッシュ・トークンを持たないことになる。Brazeは期限切れのWebプッシュトークンを移行しない。このようなユーザーには、[プッシュ・プライマーを通じて]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)再参加してもらう必要がある。
{% endalert %}

## API経由の手動移行

手動プッシュトークンマイグレーションは、これらの以前に作成されたキーを、APIを通じてBrazeプラットフォームにインポートするプロセスである。

[`users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)使用して、iOS (APNs) および Android (FCM) トークンをお客様のプラットフォームにプログラム的に移行する。特定ユーザー（関連する外部IDを持つユーザー）と匿名ユーザー（外部IDを持たないユーザー）の両方を移行できる。

プッシュトークン移行時にアプリの`app_id` を指定し、適切なプッシュトークンを適切なアプリに関連付ける。各アプリ（iOS、Androidなど）にはそれぞれ`app_id` 、[API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/)ページの**Identification**セクションで確認できる。必ず正しいプラットフォームの`app_id` を使用すること。

{% alert important %}
APIを通じてウェブ・プッシュ・トークンを移行することはできない。これは、ウェブ・プッシュ・トークンが他のプラットフォームと同じスキーマに準拠していないためだ。 

<br>ウェブ・プッシュ・トークンをプログラムで移行しようとすると、次のようなエラーが表示されることがある： `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
APIマイグレーションの代替として、SDKを統合し、トークン・ベースが自然に再投入されるようにすることをお勧めする。
{% endalert %}

### 外部IDが存在する場合は移行する
特定されたユーザーの場合、`push_token_import` フラグを`false` に設定し（またはパラメータを省略し）、ユーザー`attributes` オブジェクトに`external_id` 、`app_id` 、`token` の値を指定する。 

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
他のシステムからプッシュトークンをインポートする場合、`external_id` が利用できるとは限らない。この場合、`push_token_import` フラグを`true` とし、`app_id` と`token` の値を指定する。Brazeは、各トークンについて一時的な匿名ユーザープロフィールを作成し、これらの個人とのメッセージのやり取りを継続できるようにする。トークンがすでにBrazeに存在する場合、リクエストは無視される。

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

Brazeは、プッシュトークンを持っていない`push_token_import` フラグの匿名プロフィールを見つけるために、月に1回チェックする。匿名プロフィールにプッシュトークンがなくなった場合、プロフィールを削除する。しかし、匿名プロファイルがまだプッシュトークンを持っていて、実際のユーザーがまだそのプッシュトークンでデバイスにログインしていないことを示唆している場合は、何もしない。

## Androidのプッシュトークンをインポートする

{% alert important %}
iOSアプリには、プッシュを表示するためのフレームワークが1つしかなく、Brazeが必要なプッシュトークンと証明書を持っている限り、プッシュ通知はすぐにレンダリングされるからだ。
{% endalert %}

Braze SDKの統合が完了する前にAndroidプッシュ通知をユーザーに送信する必要がある場合は、キーと値のペアを使用してプッシュ通知を検証する。 

プッシュペイロードを処理し表示するレシーバーが必要である。プッシュペイロードをレシーバーに通知するには、必要なキーと値のペアをプッシュキャンペーンに追加する。これらのペアの値は、ブレイズの前に使用した特定のプッシュパートナーによって決まる。

{% alert note %}
プッシュ通知プロバイダーによっては、Brazeが適切に解釈できるように、キーと値のペアをフラットにする必要がある。特定のAndroidアプリのキーと値のペアをフラットにするには、カスタマー・オンボーディングまたはサクセス・マネージャーに連絡する。
{% endalert %}

_最終更新日：2022年12月5日_
