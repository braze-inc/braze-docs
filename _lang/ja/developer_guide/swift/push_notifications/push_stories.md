{% multi_lang_include developer_guide/prerequisites/swift.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)必要で、これには`UNNotification` フレームワークの実装も含まれる。

プッシュストーリーを受信するには、以下のSDKの最低バージョンが必要である：

{% sdk_min_versions swift:5.0.0 %}

## プッシュストーリーの設定

### ステップ 1: 通知コンテンツ拡張ターゲットを追加する{#notification-content-extension}

アプリ・プロジェクトで、メニュー「**ファイル」＞「新規作成」＞「ターゲット**」と進み、新しい`Notification Content Extension` ・ターゲットを追加してアクティブにする。

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode によって新しいターゲットが生成され、次のようなファイルが自動的に作成されるはずです。

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### ステップ2:機能を有効にする {#enable-capabilities}

Xcode で、[**署名 & 機能**] ペインを使ってメインアプリのターゲットにバックグラウンドモード機能を追加します。**バックグラウンドフェッチ**と**リモート通知**の両方のチェックボックスを選択します。

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### アプリグループの追加

さらに、Xcode の [**署名 & 機能**] ペインから、アプリグループ機能をメインアプリターゲットと通知コンテンツ拡張ターゲットに追加します。次に、**＋**ボタンをクリックする。アプリのバンドル ID を使用してアプリグループを作成します。たとえば、アプリのバンドル ID が `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。

{% alert important %}
ここでいうApp Groupsとは、Appleの[App Groups Entitlementの](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)ことであり、Brazeのワークスペース（旧App Group）IDのことではない。
{% endalert %}

アプリをアプリグループに追加しないと、アプリがプッシュペイロードからの特定のフィールドの入力に失敗し、期待したとおりに完全に動作しない可能性があります。

### ステップ3:アプリにPush Storyフレームワークを追加する {#enable-capabilities}

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Manager の統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/)に従って、`BrazePushStory` を `Notification Content Extension` に追加します。

![Xcodeのフレームワークとライブラリの下にある「+」アイコンを選択して、フレームワークを追加する。]({% image_buster /assets/img/swift/push_story/spm1.png %})()

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Podfile に次の行を追加します。

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
リッチプッシュの実装方法については、[リッチ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager)を参照してください。
{% endalert %}

Podfile を更新したら、ターミナル内で Xcode アプリプロジェクトのディレクトリーに移動し、`pod install`　を実行します。

{% endtab %}
{% tab Manual %}

[GitHub リリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)から最新の `BrazePushStory.zip` をダウンロードして展開し、`BrazePushStory.xcframework` をプロジェクトの `Notification Content Extension` に追加します。

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
[**埋め込み**] 列の下で、**BrazePushStory.xcframework** に対して [**埋め込まない**] が選択されていることを確認します。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ4: 通知ビューコントローラーを更新する{#enable-capabilities}

`NotificationViewController.swift` に以下の行を追加し、ヘッダーファイルをインポートする：

```swift
import BrazePushStory
```

次に、[`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/) を継承してデフォルトの実装を置き換えます。

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### プッシュストーリーイベントのカスタム処理

独自のカスタムロジックを実装してプッシュストーリー通知イベントを処理する場合は、上記のように `BrazePushStory.NotificationViewController` を継承し、以下のように [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) メソッドをオーバーライドします。

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

### ステップ5:通知コンテンツ拡張 plist を設定する{#notification-content-extension}

`Notification Content Extension` の`Info.plist` ファイルを開き、`NSExtension \ NSExtensionAttributes` の下に以下のキーを追加・変更する：

| キー                                              | タイプ    | 値                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | string  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | ブール値 | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | 数値  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | ブール値 | `YES`                  |

あなたの`Info.plist` ファイルは、以下の画像と一致するはずだ：

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### ステップ6: メインアプリでの Braze 統合の更新{#update-braze}

Brazeを初期化する前に、アプリグループの名前をBraze設定の [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup)プロパティに割り当てる。

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
