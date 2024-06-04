---
nav_title: ライブ活動
article_title: iOS用ライブ・アクティビティ
platform: Swift
page_order: 1
description: "この記事では、Brazeを使用してSwift SDKのLive Activitiesトークンを管理する方法について説明します。"

---

# ライブ活動

> ライブ・アクティビティは、ロック画面に表示される持続的でインタラクティブな通知で、リアルタイムで物事を見守ることができます。ライブ・アクティビティはロック画面に表示されるため、通知を見逃すことはない。永続的であるため、ユーザーに携帯電話のロックを解除させることなく、最新のコンテンツを表示することができる。 

![A delivery tracker live activity on an iPhone lockscreen. A status bar with a car is almost half-way filled up. Text reads "2 min until pickup"]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

ライブ・アクティビティでは、静的な情報とあなたが更新する動的な情報を組み合わせて提示します。例えば、配送のステータストラッカーを提供するライブアクティビティを作成することができます。このライブ・アクティビティには、御社の名前が静的情報として表示され、また配達ドライバーが目的地に近づくと更新される動的な「配達までの時間」が表示されます。

開発者として、Brazeを使用してライブアクティビティのライフサイクルを管理し、Braze REST APIを呼び出してライブアクティビティのアップデートを行い、サブスクライブしているすべてのデバイスができるだけ早くアップデートを受信できるようにすることができます。また、BrazeでLive Activitiesを管理しているため、他のメッセージングチャネル（プッシュ通知、アプリ内メッセージ、コンテンツカード）と組み合わせて、採用を促進することができます。

## 前提条件 

{% sdk_min_versions swift:5.11.0 %}

その他の前提条件は以下の通り：

- ライブ・アクティビティは、iOS 16.1以降のiPhoneとiPadでのみ利用可能です。この機能を使用するには、プロジェクトがこのiOSバージョンをターゲットにしていることを確認してください。
- `Push Notification` エンタイトルメントは、Xcode プロジェクトの**Signing & Capabilities**に追加する必要があります。
- Braze Swift SDKのバージョン8.2.0から、[Live Activityをリモートで登録](#step-2-start-the-activity)できるようになりました。この機能を使用するには、iOS 17.2以降が必要です。

{% alert note %}
ライブ・アクティビティとプッシュ通知は似ていますが、システム権限は別物です。デフォルトでは、すべてのライブ・アクティビティ機能が有効になっていますが、ユーザーはアプリごとにこの機能を無効にすることができます。
{% endalert %}

## ライブ活動の実施

### ステップ 1:アクティビティを作成する

まず、Appleのドキュメントにある[Displaying live data with Live][3]Activitiesに従って、iOSアプリケーションにライブ・アクティビティを設定してください。この作業の一環として、`Info.plist` に`YES` に設定した`NSSupportsLiveActivities` が含まれていることを確認してください。

ライブ・アクティビティの正確な性質はビジネスケースによって異なるため、[アクティビティ・オブジェクトを][4]設定し、初期化する必要があります。重要なのは、あなたが定義することだ：
* `ActivityAttributes`:このプロトコルは、ライブ・アクティビティに表示される静的（不変）コンテンツと動的（変化する）コンテンツを定義します。
* `ActivityAttributes.ContentState`:このタイプは、活動期間中に更新される動的データを定義します。

また、SwiftUIを使用して、サポートされているデバイスのロック画面とDynamic IslandのUIプレゼンテーションを作成します。 

Liveアクティビティに関するAppleの[前提条件や制限は][2]、Brazeとは独立しているため、よく理解しておいてください。

{% alert note %}
同じライブ・アクティビティに頻繁にプッシュを送信する場合は、`Info.plist` ファイルで`NSSupportsLiveActivitiesFrequentUpdates` を`YES` に設定することで、アップルの予算制限によるスロットルを回避できます。詳細については、ActivityKitドキュメントの [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency)セクションを参照してください。
{% endalert %}

#### 例

このショーでは、2つの野生動物保護団体が競い合い、保護されたフクロウにポイントが与えられます。この例では、`SportsActivityAttributes` という構造体を作成しましたが、`ActivityAttributes` の独自の実装を使用してもかまいません。

\`\`\`swift
\#if canImport(ActivityKit)
  インポート ActivityKit
\`endif\`

@available(iOS 16.1, \*)
struct SportsActivityAttributes：アクティビティ属性 {
public struct ContentState: Codable, Hashable {
var teamOneScore: Int
var teamTwoScore: Int
}

  var gameName：string
  var gameNumber：string
()
\`\`\`

### ステップ 2: 活動開始

まず、活動の登録方法を選択します：

- **リモートで：**メソッドを使用します。 [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>)メソッドを使い [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)エンドポイントを使用してアクティビティを開始します。
- **地元では**Live Activityのインスタンスを作成し、Brazeが管理するプッシュトークンを作成するために [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>)メソッドを使用して、Brazeが管理するプッシュトークンを作成します。

{% tabs local %}
{% tab remote %}
{% alert important %}
ライブ・アクティビティをリモート登録するには、iOS 17.2以降が必要です。
{% endalert %}

#### ステップ 2.1:ウィジェット拡張機能にBrazeKitを追加する

Xcodeプロジェクトで、アプリ名を選択し、次に**Generalを**選択します。**フレームワークとライブラリ**」の下に、`BrazeKit` が表示されていることを確認する。

![The BrazeKit framework under Frameworks and Libraries in a sample Xcode project.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### ステップ 2.2:BrazeLiveActivityAttributesプロトコルの追加

`ActivityAttributes` の実装で、`BrazeLiveActivityAttributes` プロトコルへの適合性を追加し、`brazeActivityId` 文字列を属性モデルに追加します。この文字列に値を割り当てる必要はない。

\`\`\`swift
import BrazeKit

\#if canImport(ActivityKit)
  インポート ActivityKit
\`endif\`

@available(iOS 16.1, \*)
struct SportsActivityAttributes：アクティビティ属性, BrazeLiveActivityAttributes {
public struct ContentState: Codable, Hashable {
var teamOneScore: Int
var teamTwoScore: Int
}

  var gameName：string
  var gameNumber：string
  var brazeActivityId：String?
()
\`\`\`

#### ステップ 2.3:プッシュ・トゥ・スタートの登録

次に、Live Activityタイプを登録し、Brazeがこのタイプに関連するすべてのプッシュ・トゥ・スタート・トークンとLive Activityインスタンスを追跡できるようにします。

{% alert warning %}
iOSオペレーティングシステムは、デバイスの再起動後の最初のアプリインストール時にのみ、push-to-startトークンを生成する。トークンを確実に登録するには、`didFinishLaunchingWithOptions` メソッドで`registerPushToStart` を呼び出します。
{% endalert %}

###### 例

以下の例では、`LiveActivityManager` クラスがライブ・アクティビティ・オブジェクトを扱っています。そして、`registerPushToStart` メソッドは、`SportActivityAttributes` を登録する：

\`\`\`swift
import BrazeKit

\#if canImport(ActivityKit)
  インポート ActivityKit
\`endif\`

class LiveActivityManager {

  @available(iOS 17.2, \*)
  func registerActivityType() {
    // This method returns a Swift background task.
// You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    pushToStartObserver：Task = Self.braze?.liveActivities.registerPushToStart()
    forType：活動<SportsActivityAttributes>.self、
      name: "スポーツアクティビティ属性"
      )
    ()

}
\`\`\`

#### ステップ 2.4:プッシュ・トゥ・スタート通知を送信する

エンドポイントを使用してリモートのプッシュ・トゥ・スタート通知を送信する。 [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)エンドポイントを使用して
{% endtab %}

{% tab local %}
[AppleのActivityKitフレーム](https://developer.apple.com/documentation/activitykit)ワークを使用してプッシュトークンを取得し、Braze SDKで管理することができます。これにより、BrazeがプッシュトークンをバックエンドのApple Push Notificationサービス（APNs）に送信するため、Braze APIを通じてLive Activitiesを更新することができます。

1. AppleのActivityKit APIを使用して、Live Activity実装のインスタンスを作成します。
2. `pushType` パラメータを`.token` とする。 
3. 定義したライブ活動`ActivitiesAttributes` 、`ContentState` 。 
4. アクティビティをBrazeインスタンスに登録するには、次のように渡します。 [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class).`pushTokenTag` パラメーターは、あなたが定義したカスタム文字列です。作成するライブ・アクティビティごとにユニークでなければなりません。

Live Activityを登録すると、Braze SDKはプッシュトークンの変化を抽出し、観察します。

#### 例

この例では、ライブ・アクティビティ・オブジェクトのインターフェースとして、`LiveActivityManager` というクラスを作成します。次に、`pushTokenTag` を`"sports-game-2024-03-15"` に設定する。

\`\`\`swift
import BrazeKit

\#if canImport(ActivityKit)
  インポート ActivityKit
\`endif\`

class LiveActivityManager {
  
  @available(iOS 15, \*)
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
    ()
  
}
\`\`\`

ライブ・アクティビティ・ウィジェットは、この初期コンテンツをユーザーに表示します。 

![A live activity on an iPhone lockscreen with two team's scores. Both the Wild Bird Fund and the Owl Rehab teams have scores of 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### ステップ 3: 活動履歴の追跡

アプリ起動時にBrazeがライブアクティビティを追跡するようにします：

1. `AppDelegate` ファイルを開いてください。
2. `ActivityKit` モジュールがあればそれをインポートする。
3. 呼び出し [`resumeActivities(ofType:)`][6]を`application(_:didFinishLaunchingWithOptions:)` 、アプリケーションに登録したすべての`ActivityAttributes` タイプについて呼び出す。

これにより、Brazeは、すべてのアクティブなライブアクティビティのプッシュトークン更新を追跡するタスクを再開することができます。ユーザーが自分のデバイスのライブアクティビティを明示的に解除した場合、そのアクティビティは削除されたとみなされ、Brazeはそのアクティビティを追跡しなくなります。

###### 例

\`\`\`swift
import UIKit
import BrazeKit

\#if canImport(ActivityKit)
  インポート ActivityKit
\`endif\`

@main
class AppDelegate:UIResponder, UIApplicationDelegate {

  static var braze:Braze? = nil

  func application(
    _ application:UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey:Any]?
  ) -> Bool {
    
    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  ()
}
\`\`\`

### ステップ 4: アクティビティの更新

![A live activity on an iPhone lock screen with two team's scores. Both the Wild Bird Fund has 2 points and the Owl Rehab has 4 points.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

エンドポイントは [`/messages/live_activity/update`][1]エンドポイントを使用すると、Braze REST APIを介して渡されるプッシュ通知でライブアクティビティを更新できます。このエンドポイントを使用して、ライブ・アクティビティの`ContentState` を更新してください。

`ContentState` を更新すると、ライブ・アクティビティ・ウィジェットに新しい情報が表示されます。前半戦が終わった時点で、スーパーフクロウのショーはこんな感じになっているかもしれない。

詳しくは[`/messages/live_activity/update` エンドポイントの][1]記事をご覧ください。

### ステップ 5: 活動終了

ライブ・アクティビティがアクティブになると、ユーザーのロック画面とダイナミック・アイランドの両方に表示されます。ライブ・アクティビティが終了し、ユーザーのUIから削除されるには、いくつかの方法があります。 

* **ユーザーの解雇**：ユーザーはライブ・アクティビティを手動で解除することができます。
* **タイムアウト**：デフォルトの8時間が経過すると、iOSはユーザーのダイナミックアイランドからライブアクティビティを削除します。デフォルトの12時間が経過すると、iOSはユーザーのロック画面からライブ・アクティビティを削除する。 
* **解散日**タイムアウト前にユーザーのUIから削除されるライブアクティビティの日付を指定できます。これは、アクティビティの`ActivityUIDismissalPolicy` で定義するか、`/messages/live_activity/update` エンドポイントへのリクエストで`dismissal_date` パラメータを使用します。
* **活動終了**：`/messages/live_activity/update` エンドポイントへのリクエストで、`end_activity` を`true` に設定することで、ライブ・アクティビティを即座に終了させることができます。

詳しくは[`/messages/live_activity/update` エンドポイントの][1]記事をご覧ください。

## トラブルシューティング

トラブルシューティングの詳細やよくある質問については、[FAQを][11]ご参照ください。

[1]: {{site.baseurl}}/api/endpoints/messaging/live_activity/update
[2]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints
[3]: https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities
[4]: https://developer.apple.com/documentation/activitykit/activityattributes
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/
