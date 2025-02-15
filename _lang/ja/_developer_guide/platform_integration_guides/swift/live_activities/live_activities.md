---
nav_title: ライブアクティビティ
article_title: iOSのライブアクティビティ
platform: Swift
page_order: 1
description: "この記事では、Braze を使用して、Swift SDK のライブアクティビティトークンを管理します。"

---

# ライブアクティビティ

> ライブアクティビティは、ロック画面に表示される永続的な対話型通知であり、リアルタイムで物事に注目することができます。ライブアクティビティはロック画面に表示されるため、通知が見逃されないようにすることができます。永続的であるため、ユーザーに電話機のロックを解除させなくても、最新の内容をユーザーに表示できます。 

![iPhone ロック画面の配信トラッカーのライブアクティビティ。車のついたステータス棒がほぼ半分に満ちている。「ピックアップまで2分」というテキストが表示されています]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

ライブアクティビティは、静的情報と、更新された動的情報を組み合わせて表示します。たとえば、配達のステータス追跡機能を提供するライブアクティビティを作成できます。このライブアクティビティには、あなたの会社の名前が静的情報として含まれ、さらに、配達ドライバーが目的地に近づくにつれて更新される「配達までの時間」が動的情報として含まれます。

開発者は Braze を使用して、ライブアクティビティのライフサイクルを管理し、Braze REST API を呼び出してライブアクティビティの更新を行い、登録済みのすべてのデバイスが可能な限り早く更新を受信できるようにすることができます。また、Braze でライブアクティビティを管理しているため、プッシュ通知、アプリ内メッセージ、コンテンツカードなど、その他のメッセージングチャネルとそれらを連携させて使用することで、採用を促進できます。

## 前提条件 

{% sdk_min_versions swift:5.11.0 %}

その他の前提条件は次のとおりです。

- ライブアクティビティは、iOS 16.1 以降のiPhone およびiPad でのみ使用できます。この機能を使用するには、プロジェクトがこのiOS バージョンをターゲットとしていることを確認します。
- `Push Notification` 資格を、Xcode プロジェクトの [**署名 & 機能**] の下に追加する必要があります。
- ライブアクティビティでは、通知を送信するために `.p8` キーを使用する必要があります。`.p12` や`.pem` などの古いファイルはサポートされません。
- Braze Swift SDK のバージョン8.2.0以降は、[ライブアクティビティをリモートで登録](#step-2-start-the-activity)できます。この機能を使用するには、iOS 17.2 以降が必要です。

{% alert note %}
ライブアクティビティとプッシュ通知は似ていますが、システムパーミッションは別個のものです。デフォルトでは、すべてのライブアクティビティの機能が有効になっていますが、ユーザーはアプリごとにこの機能を無効にすることができます。
{% endalert %}

## ライブアクティビティの実装

### ステップ1:アクティビティを作成する

まず、Apple のドキュメントの[ライブアクティビティでライブデータを表示する](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities)手順に従い、iOS アプリケーションにライブアクティビティをセットアップします。このタスクの一部として、`YES` に設定した `NSSupportsLiveActivities` を `Info.plist` に含めます。

Live Activity の正確な性質はビジネスケースに固有であるため、[Activity](https://developer.apple.com/documentation/activitykit/activityattributes) オブジェクトを設定して初期化する必要があります。以下を定義することが重要です。
* `ActivityAttributes`:このプロトコルは、ライブアクティビティに表示される静的 (不変) コンテンツと動的 (可変) コンテンツを定義します。
* `ActivityAttributes.ContentState`:この型は、アクティビティの進行に伴って更新される動的データを定義します。

また、SwiftUI を使用して、サポートされているデバイスでロック画面とダイナミックアイランドの UI 表示を作成します。 

ライブアクティビティに関する Apple の[前提条件と制限](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints)をよく理解してください。これらの制約は、Braze の制約とは異なります。

{% alert note %}
同じライブアクティビティに頻繁にプッシュを送信する場合は、`Info.plist` ファイルで `NSSupportsLiveActivitiesFrequentUpdates` を `YES` に設定することで、Apple の予算制限で抑制されるのを回避できます。詳細については、ActivityKit ドキュメントの[`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency)のセクションを参照してください。
{% endalert %}

#### 例

競争している2つの野生動物救助チームに、居住地に生息するフクロウに対してポイントが与えられる Superb Owl ショーの更新をユーザーに提供するライブアクティビティを作成すると想定してみましょう。この例では、`SportsActivityAttributes` という構造体を作成しましたが、`ActivityAttributes` の独自の実装を使用できます。

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

- **リモート:**アプリケーションとユーザーのライフサイクルのできるだけ早い段階 (およびP ush to Start トークンが必要になる前) に、[`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) メソッドを使用します。次に、[`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) エンドポイントを使用してアクティビティを開始します。
- **ローカル:**Live Activity のインスタンスを作成し、[`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) メソッドを使用して、管理するBrazeのプッシュトークンs を作成します。

{% tabs local %}
{% tab remote %}
{% alert important %}
ライブアクティビティをリモートで登録するには、iOS 17.2以降が必要です。
{% endalert %}

#### ステップ 2.1:BrazeKit をウィジェット拡張に追加する

Xコードプロジェクトで、アプリの名前を選択し、**一般**を選択します。[**フレームワークとライブラリ**] の下に `BrazeKit` がリストされていることを確認します。

![Xcode サンプルプロジェクトの [フレームワークとライブラリ] の下にある BrazeKit フレームワーク。]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### ステップ2.2: BrazeLiveActivityAttributes プロトコルの追加

`ActivityAttributes` 実装で、`BrazeLiveActivityAttributes` プロトコルに適合性を追加してから、`brazeActivityId` 文字列を属性モデルに追加します。この文字列に値を割り当てる必要はありません。

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

#### ステップ 2.3:push-to-start の登録

次にライブアクティビティのタイプを登録し、そのタイプに関連付けられたすべての push-to-start トークンとライブアクティビティインスタンスを Braze が追跡できるようにします。

{% alert warning %}
iOS オペレーティングシステムは、デバイスが再起動した後、最初のアプリのインストール中にのみ push-to-start トークンを生成します。トークンが確実に登録されていることを確認するには、`registerPushToStart` を`didFinishLaunchingWithOptions` メソッドで呼び出します。
{% endalert %}

###### 例

次の例では、`LiveActivityManager` クラスがLive Activity オブジェクトを処理します。次に、`registerPushToStart` メソッドが `SportActivityAttributes` を登録します。

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
3. 定義したライブアクティビティの `ActivitiesAttributes` と `ContentState` を渡します。 
4. Brazeインスタンスにアクティビティを登録するには、[`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class) に渡します。`pushTokenTag` パラメータは、定義するカスタム文字列です。作成するLive Activity ごとに一意である必要があります。

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

ライブアクティビティウィジェットによって、この最初の内容がユーザーに表示されます。 

![2 つのチームのスコアを持つiPhone ロックスクリーンでのライブアクティビティ。Wild Bird Fund チームと Owl Rehab チームのスコアは両方とも0です。]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### ステップ3:アクティビティトラッキングを再開する

Braze がアプリ起動時にライブアクティビティを追跡できるようにするには、次のようにします。

1. `AppDelegate` ファイルを開きます。
2. 使用可能な場合は、`ActivityKit` モジュールをインポートします。
3. アプリケーションで登録したすべての `ActivityAttributes` タイプについて、`application(_:didFinishLaunchingWithOptions:)` で [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) を呼び出します。

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

### ステップ 4:アクティビティを更新する

![2チームのスコアを持つiPhoneロック画面でのライブアクティビティ。Wild Bird Fund チームは2ポイントで、Owl Rehab チームは4ポイントです。]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

[`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) エンドポイントを使用すると、Braze REST API を介して渡されたプッシュ通知を介してライブアクティビティを更新できます。このエンドポイントを使用して、Live Activity の`ContentState` を更新します。

`ContentState` を更新すると、ライブアクティビティのウィジェットに新しい情報が表示されます。前半終了時に、Superb Owl ショーがどのように見えるかを以下に示します。

詳細については、[`/messages/live_activity/update`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)の記事を参照してください。

### ステップ5:アクティビティを終了する

ライブアクティビティが有効な場合、ユーザーのロック画面とダイナミックアイランドの両方に表示されます。ライブアクティビティを終了し、ユーザーの UI から削除する方法はいくつかあります。 

* **ユーザーによる却下**:ユーザーは手動でライブアクティビティを削除できます。
* **タイムアウト**:デフォルトである8時間が経過すると、iOS はユーザーのダイナミックアイランドからライブアクティビティを削除します。デフォルトである12時間が経過すると、iOS はユーザーのロック画面からライブアクティビティを削除します。 
* **却下日**:タイムアウトする前に、ユーザーのユーザーインターフェイスからライブアクティビティを削除する日時を指定できます。これは、アクティビティの `ActivityUIDismissalPolicy` で定義するか、`/messages/live_activity/update` エンドポイントへのリクエストで `dismissal_date` パラメータを使用して定義します。
* **アクティビティの終了**:`/messages/live_activity/update` エンドポイントへのリクエストで `end_activity` を `true` に設定すると、すぐにライブアクティビティを終了できます。

詳細については、[`/messages/live_activity/update`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/live_activity/update)の記事を参照してください。

## トラブルシューティング

トラブルシューティングの詳細やよくある質問については、[FAQ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/)を参照してください。

