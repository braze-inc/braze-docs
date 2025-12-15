---
nav_title: リッチプッシュ通知
article_title: iOS のリッチプッシュ通知
platform: iOS
page_order: 3
description: "この参照記事では、iOS アプリケーションでリッチプッシュ通知を実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS 10リッチプッシュ通知

iOS 10では、画像、GIF、およびビデオでプッシュ通知を送信する機能が導入されています。この機能を有効にするには、クライアントは`Service Extension` を作成する必要があります。これは、プッシュペイロードが表示される前に変更できる新しいタイプの拡張機能です。

## サービス拡張の作成

[`Notification Service Extension`](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension) を作成するには、Xcode で **[ファイル] > [新規] > [ターゲット]** に移動し、[**通知サービス拡張**] を選択します。

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

アプリケーションに拡張機能を埋め込むように [**アプリケーションに埋め込む**] が設定されていることを確認します。

## サービス拡張の設定

`Notification Service Extension` は、アプリにバンドルされている独自のバイナリです。これは、[Apple Developer Portal](https://developer.apple.com)に独自のアプリIDとプロビジョニングプロファイルで設定する必要があります。

`Notification Service Extension` のバンドル ID は、メインアプリターゲットのバンドル ID とは異なる必要があります。たとえば、アプリのバンドル ID が `com.company.appname` の場合、サービス拡張に `com.company.appname.AppNameServiceExtension` を使用できます。

### Braze で動作するようにサービス拡張を設定する

Braze は、リッチコンテンツの設定、ダウンロード、および表示に使用する `ab` キーの下にある APNs ペイロードの添付ペイロードを送信します。以下に例を示します。

```json
{
  "ab" :
    {
    ...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

関連するペイロード値は次のとおりです。

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Braze ペイロードで手動でプッシュ通知を表示するには、`AppboyAPNSDictionaryAttachmentURLKey` の下の値からコンテンツをダウンロードし、`AppboyAPNSDictionaryAttachmentTypeKey` キーの下に格納されているファイルタイプのファイルとして保存し、通知添付ファイルに追加します。

### サンプルコード

サービス拡張は、Objective-C または Swift で記述できます。

Objective-C サンプルコードを使用するには、`Notification Service Extension` ターゲットの自動生成された `NotificationService.m` の内容をAppboy の [`NotificationService.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m) の内容に置き換えます。

Swift サンプルコードを使用するには、`Notification Service Extension` ターゲットの自動生成された`NotificationService.swift` の内容を Appboy の [`NotificationService.swift`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift) の内容に置き換えます。

## ダッシュボードでリッチプッシュ通知を作成する

Braze ダッシュボードでリッチプッシュ通知を作成するには、iOS プッシュを作成するか、イメージまたは GIF を添付するか、画像、GIF、または動画をホストするURL を指定します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツをホスティングしている場合は、要求が大規模に同期的に急増することを想定する必要があります。

サポートされているファイルタイプとサイズのリストについては、[`unnotificationattachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment)を参照してください。

