---
nav_title: リッチプッシュ通知
article_title: iOS のリッチプッシュ通知
platform: Swift
page_order: 5
description: "この記事では、スイフトSDKのための豊富なiOS プッシュ通知の実装について説明します。"
channel:
  - push

---

# 豊かな通知

> リッチ通知 s は、"画像 s、GIF、および動画 を持つプッシュ通知 s です。この機能を有効にするには、通知サービス拡張を作成する必要があります。これは、プッシュペイ読み込むの変更を有効にする拡張の一種です。サポートされているファイルタイプとサイズのリストについては、Apple の\[`UNNotificationAttachment`][28] を参照してください。

## ステップ1:サービス拡張の作成

[ 通知 サービス拡張][23] を作成するには、Xコード で**File > New > Target** に移動し、** 通知 サービス拡張** を選択します。

![][26]{: style="max-width:90%"}

アプリケーションに拡張機能を埋め込むように \[**アプリケーションに埋め込む**] が設定されていることを確認します。

## ステップ2:通知 保守拡張機能のセットアップ

通知サービスエクステンションは、アプリにバンドルされている独自のバイナリーです。これは、\[アプリ le デベロッパポータル][27] で、独自のアプリ ID とプロビジョニングプロファイルを使用して設定する必要があります。

通知 サービスエクステンションのバンドルID は、メインアプリターゲットのバンドルID とは異なる必要があります。たとえば、アプリのバンドル ID が `com.company.appname` の場合、サービス拡張に `com.company.appname.AppNameServiceExtension` を使用できます。

## ステップ3:豊富なプッシュ通知の統合

リッチプッシュ通知s と`BrazeNotificationService` の統合に関するステップガイドについては、[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) を参照してください。

サンプルを確認するには、サンプルアプリの[`NotificationService`][1] の使用法を参照してください。

### アプリへのリッチプッシュフレームワークの追加

{% tabs local %}
{% tab スイフトパッケージマネージャ %}

[Swift Package Manager 統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)の後、以下を実行して`BrazeNotificationService` を`Notification Service Extension` に追加します。

1. Xコードでは、フレームワークとライブラリの下で、<i class="fas fa-plus"></i>追加アイコンを選択してフレームワークを追加します。<br><br>![プラスアイコンは、Xコード.]({% image_buster /assets/img_archive/rich_notification.png %})のフレームワークおよびライブラリの下にあります。<br><br>

2. "BrazeNotificationService"フレームワークを選択します。<br><br>!["BrazeNotificationServiceフレームワークは、開封s.]({% image_buster /assets/img_archive/rich_notification2.png %})のモーダルで選択できます。

{% endtab %}
{% tab ココアポッド %}

以下をPodfile に追加します。

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```
{% alert note %}
プッシュストーリーを実装する手順については、[ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfile を更新したら、ターミナル内で Xcode アプリプロジェクトのディレクトリーに移動し、`pod install`　を実行します。

{% endtab %}

{% tab マニュアル %}

`BrazeNotificationService.xcframework` を`Notification Service Extension` に追加するには、[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/) を参照してください。

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### 独自のUNNotificationServiceExtensionの使用
独自のUNNotificationServiceExtension を使用する必要がある場合は、`didReceive` メソッドで[`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) を呼び出すことができます。

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

## ステップ4: ダッシュボードでリッチプッシュ通知を作成する

マーケティングチームは、ダッシュボードからリッチプッシュ通知を作成することもできます。プッシュコンポーザーを介してプッシュ通知を作成し、単に"画像またはGIF を添付するか、"画像、GIF、または動画をホストするURL を指定します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツをホスティングしている場合は、要求が大規模に同期的に急増することを想定する必要があります。

[1]: https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
