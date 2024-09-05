---
nav_title: Push Stories
article_title: iOSのプッシュストーリーを統合する
platform: Swift
page_order: 27
description: "この記事では、Swift SDK向けにiOS Push Storiesをセットアップする方法を紹介する。"
channel:
  - push

---

# Push Stories

> \[プッシュストーリーズ][5] では、マーケティング担当者は写真のカルーセル機能を使って、プッシュ通知内に一連のページを作成することができる。これらのページは、画像、クリックアクション、タイトル、説明文で構成されている。 

iOSアプリにプッシュストーリーズを設定するには、標準的なプッシュ通知を統合する以外にも、この記事で説明する追加のステップが必要だ。

## 前提条件

プッシュストーリーを受信するには、以下のSDKバージョンが必要である：

{% sdk_min_versions swift:5.0.0 %}

[プッシュ通知統合のチュートリアルに従って][1]、アプリでプッシュを有効にしていることを確認する。このタスクの一環として、この機能に必要な`UNNotification` フレームワークを実装しておく必要がある。

## ステップ1:Notification Content Extensionターゲットを追加する {#notification-content-extension}

アプリ・プロジェクトで、メニュー「**ファイル」＞「新規作成」＞「ターゲット**」と進み、新しい`Notification Content Extension` ・ターゲットを追加してアクティブにする。

![][2]

Xcode によって新しいターゲットが生成され、次のようなファイルが自動的に作成されるはずです。

- `NotificationViewController.swift`
- `MainInterface.storyboard`

## ステップ2:機能を有効にする {#enable-capabilities}

Xcodeで、メインアプリのターゲットに**Signing & Capabilities**ペインを使ってBackground Modesケイパビリティを追加する。**バックグラウンド・フェッチと** **リモート通知の**両方のチェックボックスを選択する。

![][3]

### アプリグループの追加

さらに、Xcode の**Signing & Capabilities**ペインから、Notification Content Extension ターゲットと同様に、メインアプリターゲットに App Groups ケーパビリティを追加する。次に、**＋**ボタンをクリックする。アプリのバンドル ID を使用してアプリグループを作成します。たとえば、アプリのバンドル ID が `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。

{% alert important %}
ここでいうApp Groupsとは、Appleの[App Groups Entitlementの](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)ことであり、Brazeのワークスペース（旧App Group）IDのことではない。
{% endalert %}

アプリをアプリグループに追加しないと、アプリがプッシュペイロードからの特定のフィールドの入力に失敗し、期待したとおりに完全に動作しない可能性があります。

## ステップ3:アプリにPush Storyフレームワークを追加する {#enable-capabilities}

{% tabs local %}
{% tab スイフト・パッケージ・マネージャー %}

[Swift Package Manager の統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)に従って、`BrazePushStory` を `Notification Content Extension` に追加します。

![Xcodeのフレームワークとライブラリの下にある「+」アイコンを選択して、フレームワークを追加する。]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab ココアポッズ %}

次の行を Podfile に追加します。

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```
{% alert note %}
リッチ・プッシュの実装方法については、[リッチ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager)通知を参照のこと。
{% endalert %}

Podfile を更新したら、ターミナル内で Xcode アプリプロジェクトのディレクトリーに移動し、`pod install`　を実行します。

{% endtab %}
{% tab マニュアル %}

[GitHubのリリース](https://github.com/braze-inc/braze-swift-sdk/releases)ページから最新の`BrazePushStory.zip` をダウンロードし、それを解凍して、`BrazePushStory.xcframework` をあなたのプロジェクトの`Notification Content Extension` に追加する。

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
に**「埋め込まない**」が選択されていることを確認する。 **BrazePushStory.xcframework**が選択されていることを確認する。
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ4: 通知ビューコントローラを更新する {#enable-capabilities}

`NotificationViewController.swift` に以下の行を追加し、ヘッダーファイルをインポートする：

```swift
import BrazePushStory
```

次に、デフォルトの実装を置き換える。 [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### プッシュストーリーイベントのカスタム処理
プッシュ・ストーリー通知イベントを処理する独自のカスタム・ロジックを実装したい場合は、上記のように`BrazePushStory.NotificationViewController` 。 [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:))メソッドをオーバーライドする。

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

## ステップ5:Notification Content Extension plistを設定する {#notification-content-extension}

`Notification Content Extension` の`Info.plist` ファイルを開き、`NSExtension \ NSExtensionAttributes` の下に以下のキーを追加・変更する：

| キー                                              | タイプ    | 価値                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | string  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | ブール値 | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | 数値  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | ブール値 | `YES`                  |

あなたの`Info.plist` ファイルは、以下の画像と一致するはずだ：

![][12]

## ステップ 6:メインアプリのBrazeインテグレーションをアップデートする {#update-braze}

Brazeを初期化する前に、アプリグループの名前をBraze設定の [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup)プロパティに割り当てる。

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {% image_buster /assets/img/swift/push_story/add_content_extension.png %}
[3]: {% image_buster /assets/img/swift/push_story/enable_background_mode.png %}
[4]: {% image_buster /assets/img/swift/push_story/add_app_groups.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/
[12]: {% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %}
