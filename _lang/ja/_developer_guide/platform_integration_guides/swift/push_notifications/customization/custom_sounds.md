---
nav_title: カスタムサウンド
article_title: iOS 用カスタムプッシュ通知サウンド
platform: Swift
page_order: 3
description: "この記事では、スウィフトSDKでのiOS カスタムサウンドの実装について説明します。"
channel:
  - push

---

# カスタムサウンド

## ステップ1:アプリでサウンドをホスティングする

カスタムプッシュ通知サウンドは、アプリのメインバンドル内でローカルにホストする必要があります。次のオーディオデータ形式が使用できます。

- リニア PCM
- MA4
- µLaw
- aLaw

オーディオデータは AIFF、WAV、または CAF ファイルにパッケージできます。Xcode で、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

{% alert note %}
カスタムサウンドを再生する場合は、30 秒未満にする必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。
{% endalert %}

### サウンドファイルを変換する

afconvert ツールを使用して、サウンドを変換できます。たとえば、16 ビットリニアPCM システムサウンドSubmarine.aiff をCAF ファイルのIMA4 オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Player でサウンドを開き、\[**ムービー**] メニューから \[**ムービーインスペクターを表示**] を選択するとサウンドのデータ形式を確認できます。
{% endalert %}

## ステップ2:サウンドのプロトコルURL を指定する

アプリ内のサウンドファイルの場所に送信するプロトコルURL を指定する必要があります。これには2 つの方法があります。

* [Appleプッシュオブジェクト][1]の`sound`パラメータを使用して、URLをBrazeに渡します。
* ダッシュボードで指定します。[push composer][2]で**Settings**を選択し、**Sound**フィールドにプロトコールURLを入力します。 

![Braze ダッシュボードのプッシュコンポーザー][8]

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合は、Braze では、デバイスのデフォルトのアラートサウンドが使用されます。ダッシュボードとは別に、\[メッセージング API][12] でサウンドを設定することもできます。

詳細については、\[カスタムアラートサウンドの準備][9]] に関するApple Developer のドキュメントを参照してください。

[1]: {{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android
[8]: {% image_buster /assets/img_archive/sound_push_ios.png %}
[9]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html