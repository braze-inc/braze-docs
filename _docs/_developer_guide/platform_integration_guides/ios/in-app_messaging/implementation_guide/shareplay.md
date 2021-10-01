---
nav_title: Shareplay
article_title: Shareplay
platform: iOS
page_order: 1
description: ""
channel:
  - in-app messages

---

# Apple Shareplay and In-App Messages

Shareplay is a feature that enables iOS 15 users to have a shared media experiance together across their decivices when using facetime. This shared media experience will sync the audio and video playback controls across all compatible devices.

The new `GroupActivities` framework allows you to leverage SharePlay in our own applications. This framework encompasses more that just synced in-app media playback, but we will be looking at how to apply it to your Braze in-app messages. 

SharePlay as a Feature

A major selling point for integrating Shareplay is it can introduce new users to your app. If someone on a FaceTime call initiates the feature, an “Open” button will appear below the HUD on everyone’s screens. 

Users will either be launched into you app or directed to the App Store to download your app. 

In-App Messages as a Medium

What better way to showcase engaging content in your iOS application than with an in-app message! Fun fact, in-app messages can play videos natively with some lightweight developer work. In doing so, this can open Pandora’s box of `AVPlayerVideoController` features such as SharePlay. The in-app message used for this example is a subclassed `ABKInAppMessageModalViewController` that has a custom view to embed a native video player.

Shareplay Tips:
- The video itself cannot be attached as a media item to the in-app message and should be set in the key-value pairs with the value being a url. You can add url validity checking in `beforeInAppMesageDisplayed` as a guardrail pior to displaying the content.
- The in-app message should be eligible for all users with re-eligibility enabled. It would also need to have two triggers—your default trigger and another trigger for the SharePlay action. Users not on iOS 15 could still view the in-app message but would only be able to do so locally. 
- Be mindful of any other in-app messages that are triggered on session start that may or may not conflict with each other.

SharePlay With In-App Messages

The responsiveness of in-app messages is the main reason for them to be the channel of choice. In-app messages can also be launched from any screen which include but not limited to your home screen. For the Content Card loyalists, it’s very possible to achieve a similar user experience but will require more developer work. 

The `GroupActivities` API determines if there is a video present. If so, trigger the custom event to launch your SharePlay-able in-app message. The code snippet for this logic is detailed in the next section. 

It is expected to dynamically hide/show any SharePlay indicator. Utilize the `isEligibleForGroupSession` variable to observe if the user is currently on a FaceTime call or not. If you happen to be on a FaceTime call, a button will be visible to share the video across the compatible devices in the chat. The first time the user initiates SharePlay, a prompt will appear on the original device to select the options. A subsequent prompt will then appear on the shared users’ devices to engage in the content. 

Code Examples

Apple’s WWDC 2021 videos on Group Activities
Combine framework and its videos from previous WWDCs

The first thing to do would be to create an object that conforms to the GroupActivity protocol. The object is the metadata of the GroupSession shared throughout the SharePlay lifecycle. 

```swift
@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com.book-demo.GroupWatching"

  let mediaItem: MediaItem
  
  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata.type = .watchTogether
    metadata.title = mediaItem.title // “Big Buck Bunny”
    metadata.fallbackURL = mediaItem.url
    return metadata
  }
}
```

When you prepare to play the media item, each group activity has three states:
.activationDisabled - viewing individually
.activationPreferred - viewing together
.cancelled - ignore and handle gracefully

When the state comes back as activationPreferred, that is your cue to activate the rest of the group activity lifecycle. 

For triggering an in-app message from SharePlay, our trusty BrazeManager.swift helper file takes the liberty of checking if there is an enqueued media item from the GroupActivity. 

```swift
private var subscriptions = Set<AnyCancellable>()
private var selectedMediaItem: MediaItem? {
  didSet {
    guard let _ = selectedMediaItem else { return }
    
    // If the application has content to play, trigger the in-app message
    logCustomEvent("Launch SharePlay Video")
  }
}

@available(iOS 15, *)
private func launchVideoPlayerMessageIfNecessary() {
    // Assigns the `enqueuedMediaItem` value to the property `selectedMediaItem`
    CoordinationManager.shared.$enqueuedMediaItem
        .receive(on: DispatchQueue.main)
        .compactMap { $0 }
        .assign(to: \.selectedMediaItem, on: self)
        .store(in: &subscriptions)
}
```
The CoordinationManager is responsible for the state changes of SharePlay such as if the user(s) leaves and/or joins the call. 


## Code Snippets

### Launch IAM from SharePlay API

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

### Configure AVPlayer for IAM

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

### Leaving a Group Session on IAM Dismissal

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

### Overriding and Loading XIB

```swift
override var nibName: String {
  return "ModalVideoViewController"
}
   
/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the In-App Message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```

### Prepare To Play

```swift
@available(iOS 15, *)
func prepareToPlay() {
  if let mediaItem = mediaItem {
    CoordinationManager.shared.prepareToPlay(mediaItem)
  }
}
```

### Creating Group Watching Activity

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

### Configure SharePlay Button Visibility

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

[1]: {% image_buster /assets/img/shareplay/shareplay1.png %}
[2]: {% image_buster /assets/img/shareplay/shareplay2.png %}
[3]: {% image_buster /assets/img/shareplay/shareplay3.png %}
[4]: {% image_buster /assets/img/shareplay/shareplay4.png %}
[5]: {% image_buster /assets/img/shareplay/shareplay5.png %}
[6]: {% image_buster /assets/img/shareplay/shareplay6.jpg %}
