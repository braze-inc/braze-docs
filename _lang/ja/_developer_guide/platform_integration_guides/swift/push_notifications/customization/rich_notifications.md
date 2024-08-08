---
nav_title: リッチプッシュ通知
article_title: iOS のリッチプッシュ通知
platform: Swift
page_order: 5
description: "この記事では、Swift SDK の豊富なiOS プッシュ通知の実装について説明します。"
channel:
  - push

---

# リッチプッシュ通知

> 豊富な通知は、画像、GIF、およびビデオを含むプッシュ通知です。この機能を有効にするには、通知サービス拡張を作成する必要があります。これは、プッシュペイロードを表示する前に変更できる拡張の一種です。サポートされているファイルタイプとサイズのリストについては、Apple の[\`UNNotificationAttachment\`][28] を参照してください。

## ステップ 1:サービス拡張の作成

[通知サービス拡張][23]を作成するには、Xcodeの**File > New > Target**に移動し、**通知サービス拡張**を選択します。

![][26]{: style="max-width:90%"}

アプリケーションに拡張機能を埋め込むように [**アプリケーションに埋め込む**] が設定されていることを確認します。

## ステップ 2: 通知サービス拡張の設定

通知サービス拡張機能は、アプリにバンドルされている独自のバイナリです。[Apple Developer Portal][27] で、独自のアプリ ID とプロビジョニングプロファイルを使用して設定する必要があります。

通知サービス拡張のバンドルID は、メインアプリターゲットのバンドルID とは異なる必要があります。たとえば、アプリのバンドル ID が `com.company.appname` の場合、サービス拡張に `com.company.appname.AppNameServiceExtension` を使用できます。

## ステップ 3: リッチプッシュ通知の統合

`BrazeNotificationService`とリッチプッシュ通知を統合する手順については、[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)を参照してください。

サンプルを確認するには、サンプルアプリの[`NotificationService`][1] の使用法を参照してください。

### アプリにリッチプッシュフレームワークを追加する

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Manager 統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)の後、以下を実行して`BrazeNotificationService` を`Notification Service Extension` に追加します。

1. Xcode では、フレームワークとライブラリの下で、<i class="fas fa-plus"></i> 追加アイコンを選択してフレームワークを追加します。<br><br>![The plus icon is located under frameworks and libraries in Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. "BrazeNotificationService"フレームワークを選択します。<br><br>![The "BrazeNotificationService framework can be selected in the modal that opens.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

以下をPodfile に追加します。

\`\`\`ruby
target 'YourAppTarget' do
  ポッド『ブラゼキット』
  ポッド「BrazeUI」
  ポッド「BrazeLocation」
end

ターゲット'YourNotificationServiceExtensionTarget'は
  ポッド「BrazeNotificationService」
end

# プッシュストーリーを統合したい場合にのみ、以下を含める
ターゲット「YourNotificationContentExtensionTarget」は
  ポッド「BrazePushStory」
end
\`\`\`
{% alert note %}
プッシュストーリーを実装する手順については、[documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfile を更新したら、ターミナル内で Xcode アプリプロジェクトのディレクトリーに移動し、`pod install`　を実行します。

{% endtab %}

{% tab Manual %}

`BrazeNotificationService.xcframework` を`Notification Service Extension` に追加するには、[手動統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/) を参照してください。

({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### 独自のUNNotificationServiceExtensionの使用
独自のUNNotificationServiceExtension を使用する必要がある場合は、`didReceive` メソッドで[`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) を呼び出すことができます。

\`\`\`swift
BrazeNotificationServiceをインポートする
UserNotificationをインポートする

クラス通知サービス:UNNotificationServiceExtension {

  override func didReceive(
    _ リクエスト:未通知要求、
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ({
if brazeHandle(request: request, contentHandler: contentHandler) {
return
})

    // Custom handling here

    contentHandler(request.content)
  ()
}
\`\`\`

## ステップ 4: ダッシュボードでリッチプッシュ通知を作成する

マーケティングチームは、ダッシュボードから豊富な通知を作成することもできます。プッシュコンポーザーを介してプッシュ通知を作成し、イメージまたはGIF を添付するか、イメージ、GIF、またはビデオをホストするURL を指定します。アセットはプッシュ通知の受信時にダウンロードされるため、コンテンツをホスティングしている場合は、要求が大規模に同期的に急増することを想定する必要があります。

[1]: https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
