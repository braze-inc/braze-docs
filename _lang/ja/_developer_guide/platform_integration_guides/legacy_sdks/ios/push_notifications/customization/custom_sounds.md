---
nav_title: カスタムサウンド
article_title: iOS 用カスタムプッシュ通知サウンド
platform: iOS
page_order: 3
description: "この参照記事では、iOS プッシュ通知にカスタムサウンドを実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムサウンド

## ステップ1:アプリでサウンドをホスティングする

カスタムプッシュ通知サウンドは、クライアントアプリケーション内のメインバンドル内でローカルにホストする必要があります。次のオーディオデータ形式が使用できます。

- リニア PCM
- MA4
- µLaw
- aLaw

オーディオデータは AIFF、WAV、または CAF ファイルにパッケージできます。Xcode で、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

afconvert ツールを使用して、サウンドを変換できます。たとえば、16ビットリニア PCM システムサウンド Submarine.aiff を CAF ファイルの IMA4オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

QuickTime Player でサウンドを開き、[**ムービー**] メニューから [**ムービーインスペクターを表示**] を選択するとサウンドのデータ形式を確認できます。

カスタムサウンドを再生する場合は、30 秒未満にする必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。

## ステップ2:ダッシュボードにサウンドのプロトコル URL を指定する

サウンドはアプリ内でローカルにホストする必要があります。プッシュコンポーザーの [**サウンド**] フィールドで、アプリ内のサウンドファイルにリダイレクトするプロトコル URL を指定する必要があります。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、以下のスクリーンショットに示すように、プッシュコンポーザーの [[messaging API]({{site.baseurl}}/api/endpoints/messaging/)] または [**設定**] にあるダッシュボードを使用して指定できます。

![]({% image_buster /assets/img_archive/sound_push_ios.png %})

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合は、Braze では、デバイスのデフォルトのアラートサウンドが使用されます。ダッシュボードとは別に、[[メッセージング API]({{site.baseurl}}/api/endpoints/messaging/)] でサウンドを設定することもできます。詳細については、[[カスタムアラートサウンドの準備](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html)] に関する Apple 開発者のドキュメントを参照してください。

