---
nav_title: カスタムサウンド
article_title: iOS 用カスタムプッシュ通知サウンド
platform: Swift
page_order: 3
description: "この記事では、Swift SDK で iOS カスタム サウンドを実装する方法について説明します。"
channel:
  - push

---

# カスタムサウンド

## ステップ1:アプリでサウンドをホスティングする

カスタム プッシュ通知サウンドは、アプリのメイン バンドル内でローカルにホストする必要があります。次のオーディオデータ形式が使用できます。

- リニア PCM
- MA4
- μLaw
- aLaw

オーディオデータは AIFF、WAV、または CAF ファイルにパッケージできます。Xcode で、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

{% alert note %}
カスタムサウンドを再生する場合は、30 秒未満にする必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。
{% endalert %}

### サウンドファイルの変換

afconvert ツールを使用してサウンドを変換できます。たとえば、16ビットリニア PCM システムサウンド Submarine.aiff をCAF ファイルの IMA4オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Player でサウンドを開き、[**ムービー**] メニューから [**ムービーインスペクターを表示**] を選択するとサウンドのデータ形式を確認できます。
{% endalert %}

## ステップ 2: サウンドのプロトコルURLを提供する

アプリ内のサウンド ファイルの場所を示すプロトコル URL を指定する必要があります。これを行うには 2 つの方法があります。

* 使用 `sound`[Apple プッシュ オブジェクト][1] のパラメータを使用して、URL を Braze に渡します。
* ダッシュボードで URL を指定します。[プッシュ コンポーザー][2]で、**[設定]** を選択し、**[サウンド]** フィールドにプロトコル URL を入力します。 

![Brazeダッシュボードのプッシュコンポーザー][8]

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合は、Braze では、デバイスのデフォルトのアラートサウンドが使用されます。ダッシュボードとは別に、[messaging API][12] でサウンドを設定することもできます。

詳細については、[カスタムアラートサウンドの準備][9] に関するApple 開発者のドキュメントを参照してください。

[1]: {{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android
[8]: {% image_buster /assets/img_archive/sound_push_ios.png %}
[9]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html