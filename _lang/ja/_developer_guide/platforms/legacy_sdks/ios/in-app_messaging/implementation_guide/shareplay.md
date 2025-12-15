---
nav_title: シェアプレイ
article_title: SharePlay アプリ内メッセージ実装ガイド
platform: iOS
page_order: 1
description: "この高度な SharePlay 実装ガイドは、アプリ内メッセージの高度な実装ガイドで提供される動画のユースケースを詳しく説明しています。SharePlay は、iOS 15 FaceTime ユーザーがデバイス間でメディア体験を共有し、リアルタイムでオーディオと動画を同期することを可能とする新たにリリースされた機能です。"
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay アプリ内メッセージ実装ガイド

> SharePlay は、iOS 15 FaceTime ユーザーがデバイス間でメディア体験を共有し、リアルタイムでオーディオと動画を同期することを可能とする新たにリリースされた機能です。SharePlay は、ユーザーが友人や家族と一緒にコンテンツを体験できる優れた方法であり、Braze の顧客に動画コンテンツを利用する新たな手段を提供し、アプリケーションを新しいユーザーに紹介する機会を提供します。

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## 概要

iOS 15 更新の一部として Apple によってリリースされた新しい `GroupActivities` フレームワークを使用すると、Braze アプリ内メッセージを利用して SharePlay をアプリケーションに統合することで、FaceTime を活用できるようになります。
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

ユーザーが FaceTime 通話で SharePlay ビデオを開始すると、全員の画面の上部に [開く] ボタンが表示されます。開くと、オーディオとビデオがすべての互換性のあるデバイス間で同期され、ユーザーはリアルタイムで動画を一緒に視聴できるようになります。アプリをダウンロードしていない人は、App Store にリダイレクトされます。

**同期されたメディアの再生**<br>
同期されたメディア再生では、1人が SharePlay ビデオを一時停止すると、すべてのデバイスで一時停止されます。<br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## 統合

この統合で使用されるアプリ内メッセージは、サブクラス化されたモーダルアプリ内メッセージビューコントローラーです。セットアップのガイドは、iOS アプリ内メッセージの高度なユースケース[実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/)に記載されています。統合する前に、Xcode プロジェクトに `GroupActivities` 権限を追加してください。

{% alert important %}
統合を完了するには、このガイドとともに [Apple SharePlay ドキュメント](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback)を開くことをお勧めします。
{% endalert %}

### ステップ1:XIB のオーバーライドとロード

{% tabs %}
{% tab Swift %}
```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the in-app message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% endtabs %}

### ステップ2:アプリ内メッセージ用に AVPlayer を構成する

アプリ内メッセージでは、開発者の作業を軽く行うだけでビデオをネイティブに再生できます。こうすることで、SharePlay など、すべての `AVPlayerVideoController` 機能にアクセスできるようになります。この例で使用されるアプリ内メッセージは、ネイティブビデオプレーヤーを埋め込むためのカスタムビューを持つサブクラス化された `ABKInAppMessageModalViewController` です。

{% tabs %}
{% tab Swift %}
```swift
func configureVideoPlayer() {
  guard let urlString = inAppMessage.extras?["video_url"] as? String,
        let url = URL(string: urlString) else { return }
     
  let videoTitle = inAppMessage.extras?["video_title"] as? String
  mediaItem = MediaItem(title: videoTitle ?? "Video Content", url: url)
     
  let asset = AVAsset(url: url)
  let playerItem = AVPlayerItem(asset: asset)
  player.replaceCurrentItem(with: playerItem)
  playerViewController.player = player
   
  addChild(playerViewController)
  videoPlayerContainer.addSubview(playerViewController.view)
  playerViewController.didMove(toParent: self)
}
```
{% endtab %}
{% endtabs %}

#### ダッシュボードの構成

**キーと値のペア**:動画ファイルはアプリ内メッセージのキーと値のペアで設定する必要があり、メディア項目自体に添付することはできません。コンテンツを表示する前に、ガードレールとして `beforeInAppMesageDisplayed` に URL の有効性チェックを追加することもできます。

**トリガー**:アプリ内メッセージは、再適格性が有効になっているすべてのユーザーに対して有効にする必要があります。これは、メッセージを起動するデフォルトのトリガーと、SharePlay から開始されたときにメッセージを起動するもう1つのトリガーの2つのトリガーを設定することで実行できます。iOS 15 を使用していないユーザーは、メッセージをローカルでのみ表示できます。 

{% alert important %}
セッション開始時にトリガーされる他のアプリ内メッセージが互いに競合する可能性があることに注意してください。
{% endalert %}

### ステップ3:グループ視聴アクティビティを作成する

`GroupActivity` プロトコルに準拠したオブジェクトを作成します。オブジェクトは、SharePlay ライフサイクル全体で共有される `GroupSession` のメタデータになります。 

{% tabs %}
{% tab Swift %}
```swift
struct MediaItem: Hashable, Codable {
  let title: String
  let url: URL
}
 
@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com.book-demo.GroupWatching"
 
  let mediaItem: MediaItem
   
  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata.type = .watchTogether
    metadata.title = mediaItem.title
    metadata.fallbackURL = mediaItem.url
    return metadata
  }
}
```
{% endtab %}
{% endtabs %}

#### 再生の準備をする

メディア項目の再生の準備をするとき、各グループアクティビティの `prepareForActivation()` の状態には以下の3つがあります。
- `.activationDisabled` - 個別閲覧
- `.activationPreferred` - 一緒に見る
- `.cancelled` - 無視して適切に処理する

状態が `activationPreferred` に戻ったら、残りのグループアクティビティのライフサイクルをアクティブにする合図です。 

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### ステップ 4:SharePlay API からアプリ内メッセージを起動する

`GroupActivities` API は動画が存在するかどうかを判別します。その場合は、カスタムイベントをトリガーして、SharePlay 対応のアプリ内メッセージを起動する必要があります。`CoordinationManager`は、ユーザーが通話から離れた場合や通話に参加した場合など、SharePlay の状態変更を行います。 

{% tabs %}
{% tab Swift %}
```swift
private var subscriptions = Set<AnyCancellable>()  
private var selectedMediaItem: MediaItem? {
  didSet {
    // Ensure the UI selection always represents the currently playing media.
    guard let _ = selectedMediaItem else { return }
 
    if !BrazeManager.shared.inAppMessageCurrentlyVisible {
      BrazeManager.shared.logCustomEvent("SharePlay Event")
    }
  }
}  
 
private func launchVideoPlayerIfNecessary() {
  CoordinationManager.shared.$enqueuedMediaItem
      .receive(on: DispatchQueue.main)
      .compactMap { $0 }
      .assign(to: \.selectedMediaItem, on: self)
      .store(in: &subscriptions)
}
```
{% endtab %}
{% endtabs %}

### ステップ5:アプリ内メッセージの終了時にグループセッションを終了する

アプリ内メッセージが閉じられたときが、SharePlay セッションを終了し、セッションオブジェクトを破棄する適切なタイミングです。

{% tabs %}
{% tab Swift %}
```swift
override func viewDidDisappear(_ animated: Bool) {
  super.viewDidDisappear(animated)
  groupSession?.leave()
  CoordinationManager.shared.leave()
}
 
class CoordinationManager() {
...
  // Published values that the player, and other UI items, observe.
  @Published var enqueuedMediaItem: MediaItem?
  @Published var groupSession: GroupSession<MediaItemActivity>?
 
  // Clear activity when the user leaves
  func leave() {
    groupSession = nil
    enqueuedMediaItem = nil
  }
...
}
```
{% endtab %}
{% endtabs %}

### SharePlay ボタンの可視性を構成する

SharePlay インジケーターを動的に非表示または表示することがベストプラクティスです。`isEligibleForGroupSession` 変数を使用して、ユーザーが現在 FaceTime 通話中かどうかを確認します。FaceTime 通話中の場合は、チャット内の互換性のあるデバイス間でビデオを共有するためのボタンが表示されるはずです。ユーザーが初めて SharePlay を開始すると、元のデバイスにオプションを選択するためのプロンプトが表示されます。その後、共有ユーザーのデバイスに、コンテンツに参加するためのプロンプトが表示されます。

{% tabs %}
{% tab Swift %}
```swift
private var isEligibleForSharePlay: Bool = false {
  didSet {
    sharePlayButton.isHidden = !isEligibleForSharePlay
  }
}
 
override func viewDidLoad() {
  super.viewDidLoad()
 
  // SharePlay button eligibility
  groupStateObserver.$isEligibleForGroupSession
    .receive(on: DispatchQueue.main)
    .assign(to: \.isEligibleForSharePlay, on: self)
    .store(in: &subscriptions)
}
``` 
{% endtab %}
{% endtabs %}

