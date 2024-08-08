---
nav_title: プッシュ通知ストーリー
article_title: iOS 用プッシュストーリーの統合
platform: Swift
page_order: 27
description: "この記事では、Swift SDK に iOS プッシュストーリーを設定する方法を説明します。"
channel:
  - push

---

# プッシュ通知ストーリー

> [プッシュストーリー] [5] により、マーケティング担当者は写真カルーセル機能を使用してプッシュ通知内に一連のページを作成できます。これらのページは、画像、クリックアクション、タイトル、および説明で構成されています。 

iOS アプリにプッシュストーリーを設定するには、この記事で説明されている標準のプッシュ通知を統合する以外に、追加の手順が必要です。

## 前提条件

プッシュストーリーを受信するには、次の SDK バージョンが必要です。

{% sdk_min_versions swift:5.0.0 %}

[プッシュ通知統合のチュートリアルに従って][1]、アプリ内でプッシュを有効にしていることを確認してください。このタスクの一環として、`UNNotification`この機能に必要なフレームワークを実装しておく必要があります。

## ステップ 1:通知コンテンツ拡張ターゲットの追加 {#notification-content-extension}

アプリプロジェクトで、メニュー **[ファイル] > [新規] > [ターゲット...]** を選択し、新しい `Notification Content Extension` ターゲットを追加してアクティブ化します。

![][2]

Xcode によって新しいターゲットが生成され、次のようなファイルが自動的に作成されるはずです。

- `NotificationViewController.swift`
- `MainInterface.storyboard`

## ステップ 2: 機能を有効にする {#enable-capabilities}

Xcodeでは、**署名と機能ペインを使用してバックグラウンドモード機能をメインのアプリターゲットに追加します**。[**バックグラウンドフェッチ**] チェックボックスと [**リモート通知**] チェックボックスの両方を選択します。

![][3]

### アプリグループの追加

さらに、Xcodeの「**署名と機能**」ペインから、メインのアプリターゲットと通知コンテンツ拡張ターゲットにアプリグループ機能を追加します。次に、[**+**] ボタンをクリックします。アプリのバンドル ID を使用してアプリグループを作成します。たとえば、アプリのバンドル ID が `com.company.appname` の場合、アプリグループに `group.com.company.appname.xyz` という名前を付けることができます。

{% alert important %}
この場合のアプリグループとは、[Appleのアプリグループ利用資格を指し](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups)、Brazeワークスペース（以前のアプリグループ）IDではありません。
{% endalert %}

アプリをアプリグループに追加しないと、アプリがプッシュペイロードからの特定のフィールドの入力に失敗し、期待したとおりに完全に動作しない可能性があります。

## ステップ 3: プッシュストーリーフレームワークをアプリに追加する {#enable-capabilities}

{% tabs local %}
{% tab Swift Package Manager %}

[Swift Package Manager の統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)に従って、`BrazePushStory` を `Notification Content Extension` に追加します。

![In Xcode, under frameworks and libraries, select the "+" icon to add a framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![\]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

次の行を Podfile に追加します。

\`\`\`ruby
target 'YourAppTarget' do
ポッド「ブレイズキット」
ポッド「ブレイズII」
ポッド「ブレイズロケーション」
end

ターゲット '通知コンテンツ拡張ターゲット' は
ポッド「ブレイズプッシュストーリー」
end

# Rich Pushも統合したい場合のみ、以下を含めてください
ターゲット '通知サービス拡張ターゲット' が
pod「ブレイズ通知サービス」
end
\`\`\`
{% alert note %}
リッチプッシュの実装方法については、「[リッチ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager)」を参照してください。
{% endalert %}

Podfile を更新したら、ターミナル内で Xcode アプリプロジェクトのディレクトリーに移動し、`pod install`　を実行します。

{% endtab %}
{% tab Manual %}

[GitHub `BrazePushStory.zip` のリリースページから最新版をダウンロードし](https://github.com/braze-inc/braze-swift-sdk/releases)、`BrazePushStory.xcframework`抽出してプロジェクトに追加します。`Notification Content Extension`

({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
**BrazePushStory.xcFramework** **の [**埋め込み] 列で [埋め込みしない**] が選択されていることを確認します。**
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ 4: 通知ビューコントローラーを更新する{#enable-capabilities}

に`NotificationViewController.swift`、次の行を追加してヘッダーファイルをインポートします。

```swift
import BrazePushStory
```

次に、[`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/)デフォルトの実装を継承して置き換えます。

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### プッシュストーリーイベントのカスタム処理
プッシュストーリー通知イベントを処理する独自のカスタムロジックを実装したい場合は、`BrazePushStory.NotificationViewController`上記のように継承し、[`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:))以下のようにメソッドをオーバーライドしてください。

\`\`\`swift
ブレイズプッシュストーリーをインポート
ユーザー通知をインポートする
ユーザー通知のインポート UI

class NotificationViewController:BrazePushStory.NotificationViewController {
  override func didReceive(_ notification:UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  ()
  
  override func didReceive(_ response:UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) 
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  ()
}
\`\`\`

## ステップ 5: 通知コンテンツ拡張リストの設定 {#notification-content-extension}

`Info.plist`のファイルを開き`Notification Content Extension`、`NSExtension \ NSExtensionAttributes`以下のキーを追加して変更します。

| キー | タイプ | 値 |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | String  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Boolean | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Number  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Boolean | `YES`                  |

`Info.plist`ファイルは以下と一致する必要があります image:

![][12]

## ステップ 6:メインアプリでの　Braze 統合のアップデート{#update-braze}

Braze を初期化する前に、アプリグループの名前を Braze 設定のプロパティに割り当ててください。[`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup)

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
