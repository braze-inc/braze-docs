---
nav_title: 生活活動
article_title: iOSのライブアクティビティ
platform: Swift
page_order: 1
description: "この記事では、Braze を使用して、Swift SDKのLive Activities トークンを管理します。"

---

# 生活活動

> ライブアクティビティは、ロックスクリーンに表示される永続的な対話型通知であり、リアルタイムで物事に注目することができます。ロックスクリーンの耳元をアプリため、ライブアクティビティでは通知を見逃さないようにします。永続的なので、電話機のロックを解除することなく、最新の内容をユーザー s に表示できます。 

![iPhoneロックスクリーンでの配信トラッカーのライブアクティビティ。車のついたステータス棒がほぼ半分に満ちている。テキストは&quot を読み込みます。ピックアップ&クォートまで2 分。]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

ライブアクティビティは、更新した静止情報とダイナミックな情報を組み合わせて提供します。たとえば、配信のステータス追跡機能を提供するライブアクティビティを作成できます。このライブアクティビティには、ダイナミックな "配信"配信&quot のほかに、企業の名前が含まれます。配信ドライバーのアプリが送信先に到達すると、これは更新d になります。

開発者として、Braze を使用して、Live Activity ライフサイクルを管理し、Braze REST API を呼び出して、Live Activity 更新を作成し、すべての登録済みデバイスにできるだけ早く更新を受信させることができます。また、Braze でLive Activities を管理しているので、他のメッセージング チャネル s-プッシュ通知 s、アプリ内メッセージ s、Content Card と連動して使用できます。

## 前提条件 

{% sdk_min_versions swift:5.11.0 %}

その他の前提条件は次のとおりです。

- ライブアクティビティは、iOS 16.1 以降のiPhone およびiPad でのみ使用できます。この機能を使用するには、プロジェクトがこのiOS バージョンをターゲットとしていることを確認します。
- Xコードプロジェクトの**Signing & Capabilities**の下に、`Push Notification`資格を追加する必要があります。
- Braze Swift SDK 8.2.0 以降では、[リモートでLive Activity](#step-2-start-the-activity) を登録できます。この機能を使用するには、iOS 17.2 以降が必要です。

{% alert note %}
ライブアクティビティとプッシュ通知は似ていますが、システムパーミッションは別個のものです。デフォルトでは、すべてのライブアクティビティ機能が有効になっていますが、ユーザー s はアプリごとにこの機能を無効にすることができます。
{% endalert %}

## ライブアクティビティの実装

### ステップ1:アクティビティを作成する

まず、[ Live Activities ][3] を使用してライブデータをアプリ le のドキュメントに表示し、iOS アプリライケーションでLive Activities を設定したことを確認します。このタスクの一部として、`NSSupportsLiveActivities` set to `YES` in your `Info.plist` を必ず含めてください。

Live Activity の正確な性質はビジネスケースに固有であるため、[Activity][4] オブジェクトを設定して初期化する必要があります。重要なことは、以下を定義することです。
* `ActivityAttributes`:このプロトコールでは、ライブアクティビティでイヤーをアプリするスタティック(不変)とダイナミックな(変更)の内容を定義します。
* `ActivityAttributes.ContentState`:この型は、アクティビティーの進行中に更新d になるダイナミックなを定義します。

また、SwiftUI を使用して、サポートされているデバイスでロック画面とダイナミックアイランドのUI プレゼンテーションを作成します。 

Live Activities の[ 前提条件と制限][2] については、Braze とは独立系ため、Apple の[ に精通していることを確認してください。

{% alert note %}
同じLive Activity に頻繁にプッシュを送信する場合は、`NSSupportsLiveActivitiesFrequentUpdates` を`YES` に設定すると、`Info.plist` ファイルでアップルのバジェット制限によって調整されることを回避できます。詳しくは、ActivityKit ドキュメントの[`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) を参照してください。
{% endalert %}

#### 例

競合する2つの野生生物の救出物が、自分が住んでいるフクロウのための点を与えられる、スーパーブ・オール・ショーのためのユーザーs 更新sを与えるための生きた活動を作りたいと想像してみましょう。この例では、`SportsActivityAttributes` という構造体を作成しましたが、`ActivityAttributes` の独自の実装を使用できます。

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### ステップ2:アクティビティを開始する

まず、アクティビティの登録方法を選択します。

- **リモート:**[`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) メソッドを使用し、[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントを使用してアクティビティを起動します。
- **ローカル:**Live Activity のインスタンスを作成し、[`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) メソッドを使用して、管理するBrazeのプッシュトークンs を作成します。

{% tabs local %}
{% tab リモート %}
{% alert important %}
Live Activity をリモートで登録するには、iOS 17.2 以降が必要です。
{% endalert %}

#### ステップ 2.1:BrazeKit をウィジェット拡張に追加する

Xコードプロジェクトで、アプリの名前を選択し、**一般**を選択します。**Frameworks and Libraries**の下に、`BrazeKit`が表示されていることを確認します。

![サンプルXコード プロジェクトのFrameworks and Libraries にあるBrazeKit フレームワーク。]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### ステップ2.2: BrazeLiveActivityAttributes プロトコルの追加

`ActivityAttributes` インプリメンテーションで、`BrazeLiveActivityAttributes` プロトコルに適合性を追加し、`brazeActivityId` 文字列を属性 s モデルに追加します。この文字列に値を割り当てる必要はありません。

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
  var brazeActivityId: String?
}
```

#### ステップ 2.3:Push-to-startレジスタ

次に、Live Activity タイプを登録すると、Braze はこのタイプに関連付けられているすべてのプッシュ・ツー・スタート・トークンs およびLive Activity インスタンスを追跡できます。

{% alert warning %}
iOS オペレーティングシステムは、装置の再起動後の最初のアプリインストール中にのみ、プッシュ・ツー・スタートトークンs を生成します。トークンが確実に登録されていることを確認するには、`registerPushToStart` を`didFinishLaunchingWithOptions` メソッドで呼び出します。
{% endalert %}

###### 例

次の例では、`LiveActivityManager` クラスがLive Activity オブジェクトを処理します。次に、`registerPushToStart` メソッドは`SportActivityAttributes` を登録します。

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: "SportsActivityAttributes"
    )
  }

}
```

#### ステップ2.4: プッシュ・トゥ・スタート通知を送信する

[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントを使用してリモートのpush-to-start 通知を送信します。
{% endtab %}

{% tab local %}
[Apple のActivityKit フレームワーク](https://developer.apple.com/documentation/activitykit) を使用して、Braze SDKが管理できるプッシュトークンを取得できます。これにより、Braze がバックエンドのApple プッシュ通知サービス(APN) にプッシュトークンを送信するため、Braze API を使用してライブアクティビティを更新できます。

1. Apple のActivityKit API を使用して、Live Activity 実装のインスタンスを作成します。
2. `pushType` パラメータを`.token` として設定します。 
3. 定義したLive Activities `ActivitiesAttributes` および`ContentState` に合格します。 
4. Brazeインスタンスにアクティビティを登録するには、[`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class) に渡します。`pushTokenTag` パラメータは、ユーザが定義するカスタム文字列です。作成するLive Activity ごとに一意である必要があります。

ライブアクティビティを登録すると、Braze SDKはプッシュトークンs の変化を抽出して観察します。

#### 例

たとえば、ライブアクティビティオブジェクトのインターフェイスとして`LiveActivityManager` というクラスを作成します。次に、`pushTokenTag` を`"sports-game-2024-03-15"` に設定します。

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {
  
  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }
  
}
```

ライブアクティビティウィジェットには、この最初の内容がユーザーs に表示されます。 

![2 つのチームのスコアを持つiPhone ロックスクリーンでのライブアクティビティ。ワイルドバード・ファンドとオール・リハブの両チームのスコアは0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### ステップ3:活動再開"トラッキング

Braze がアプリ起動時にライブアクティビティを追跡できるようにするには:

1. `AppDelegate` ファイルを開きます。
2. 使用可能な場合は、`ActivityKit` モジュールをインポートします。
3. アプリライケーションに登録したすべての`ActivityAttributes`タイプについて、[][6]`resumeActivities(ofType:)`を`application(_:didFinishLaunchingWithOptions:)`で呼び出します。

これにより、Brazeは、すべての有効なライブアクティビティのプッシュトークン 更新を追跡するタスクを再開できます。ユーザーがデバイス上のライブアクティビティを明示的に削除した場合、削除されたと見なされ、Brazeはそれを追跡できなくなることに注意してください。

###### 例

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### ステップ4: アクティビティを更新する

![2チームのスコアを持つiPhoneロック画面でのライブアクティビティ。野鳥ファンドは2点、オール・リハブは4点。]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

[`/messages/live_activity/update`][1] エンドポイントを使用すると、Braze REST API を通過するプッシュ通知s を介してライブアクティビティを更新できます。このエンドポイントを使用して、Live Activity の`ContentState` を更新します。

`ContentState` を更新すると、ライブアクティビティウィジェットに新しい情報が表示されます。上半期の終わりに、スーパーブ・オール・ショーがどのように見えるかを以下に示します。

詳細については、[`/messages/live_activity/update`エンドポイント][1]の記事を参照してください。

### ステップ5:活動を終了する

ライブアクティビティが有効な場合、ユーザーのロックスクリーンとダイナミックアイランドの両方に表示されます。ライブアクティビティを終了し、ユーザーのUI から削除するには、いくつかの方法があります。 

* **ユーザ解雇**:ユーザーは手動でライブアクティビティを削除できます。
* **タイムアウト**:デフォルト8時間後、iOSはユーザーのダイナミックアイランドからライブアクティビティを削除します。デフォルト12時間後、iOSはユーザーのロックスクリーンからライブアクティビティを削除します。 
* **解雇日**:タイムアウトする前に、ユーザーのユーザーインターフェイスからライブアクティビティを削除する日時を指定できます。これは、アクティビティの`ActivityUIDismissalPolicy` または`dismissal_date` パラメータを使用して、`/messages/live_activity/update` エンドポイントへのリクエストで定義されます。
* **アクティビティの終了**:`/messages/live_activity/update` エンドポイントへのリクエストで`end_activity` を`true` に設定すると、すぐにライブアクティビティを終了できます。

詳細については、[`/messages/live_activity/update`エンドポイント][1]の記事を参照してください。

## トラブルシューティング

トラブルシューティングの詳細やよくある質問については、[FAQ][11]を参照してください。

[1]: {{site.baseurl}}/api/endpoints/messaging/live_activity/update
[2]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints
[3]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
[4]: https://developer.apple.com/documentation/activitykit/activityattributes
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/
