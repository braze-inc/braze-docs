{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Displaying banners

{% tabs %}
{% tab UIKit %}
{% scrolly %}

```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=BannerViewController.swift
import UIKit
import BrazeKit
import BrazeUI

final class BannerViewController: UIViewController {

  static let bannerPlacementID = "top-1"
  var bannerHeightConstraints: NSLayoutConstraint?

  lazy var contentView: UILabel = {
    let contentView = UILabel()
    contentView.text = "Your Content Here"
    contentView.textAlignment = .center
    contentView.translatesAutoresizingMaskIntoConstraints = false
    return contentView
  }()

  lazy var bannerView: BrazeBannerUI.BannerUIView = {
    var bannerView = BrazeBannerUI.BannerUIView(
      placementId: BannerViewController.bannerPlacementID,
      braze: AppDelegate.braze!,
      processContentUpdates: { [weak self] result in
        // Update layout properties when banner content has finished loading.
        DispatchQueue.main.async {
          guard let self else { return }
          switch result {
          case .success(let updates):
            if let height = updates.height {
              self.bannerView.isHidden = false
              self.bannerHeightConstraint?.constant = min(height, 80)
            }
          case .failure(let error):
            return
          }
        }
      }
    )
    bannerView.translatesAutoresizingMaskIntoConstraints = false
    bannerView.isHidden = true
    return bannerView
  }()

  override func viewDidLoad() {
    super.viewDidLoad()
    self.view.addSubview(contentView)
    self.view.addSubview(bannerView)
    bannerHeightConstraint = bannerView.heightAnchor.constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
      contentView.topAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.topAnchor),
      contentView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      contentView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.topAnchor.constraint(equalTo: self.contentView.bottomAnchor),
      bannerView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      bannerView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.bottomAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.bottomAnchor),
      bannerHeightConstraint!,
    ])
  }
}
```

!!step
lines-AppDelegate.swift=14

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=20

#### 2. Trigger a banners refresh

Call `requestBannersRefresh` for your placement ID after initializing Braze.
This proactively fetches the latest banner data, ensuring your app can display new content quickly after launch.

!!step
lines-BannerViewController.swift=19-37

#### 3. Initialize the Braze banner view with a processContentUpdates callback

Create your `BrazeBannerUI.BannerUIView` with the correct placement ID and Braze instance.
The `processContentUpdates` callback will fire whenever the banner height changes.
Inside the callback, unhide the banner and update its height constraint using the provided content height (capped at 80pt for this example).

!!step
lines-BannerViewController.swift=38-40

#### 4. Hide banner by default, enable Auto Layout

Hide the banner view until content loads and disable autoresizing mask translation to use Auto Layout constraints.

!!step
lines-BannerViewController.swift=43-58

#### 5. Pin views with Auto Layout constraints and set up height constraint

Anchor your main content to the top. Place the banner view directly below, pinning its leading, trailing, and bottom to the safe area.
Set up a height constraint for the banner view (starting at 0), which will be updated when banner content loads.

{% endscrolly %}
{% endtab %}
{% tab SwiftUI %}
{% scrolly %}

```swift file=AppDelegate.swift
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            BannerSwiftUIView()
        }
    }
}
```

```swift file=BannerSwiftUIView.swift
import BrazeKit
import BrazeUI
import SwiftUI

@available(iOS 13.0, *)
struct BannerSwiftUIView: View {

  static let bannerPlacementID = "top-1"

  @State var hasBannerForPlacement: Bool = false
  @State var contentHeight: CGFloat = 0

  var body: some View {
    VStack {
      Text("Your Content Here")
        .frame(maxWidth: .infinity, maxHeight: .infinity)
      if let braze = AppDelegate.braze,
        hasBannerForPlacement
      {
        BrazeBannerUI.BannerView(
          placementId: BannerSwiftUIView.bannerPlacementID,
          braze: braze,
          processContentUpdates: { result in
            switch result {
            case .success(let updates):
              if let height = updates.height {
                self.contentHeight = height
              }
            case .failure:
              return
            }
          }
        )
        .frame(height: min(contentHeight, 80))
      }
    }.onAppear {
      AppDelegate.braze?.banners.getBanner(
        for: BannerSwiftUIView.bannerPlacementID,
        { banner in
          hasBannerForPlacement = banner != nil
        }
      )
    }
  }
}

```

!!step
lines-AppDelegate.swift=13

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=19

#### 2. Trigger a banners refresh

Call `requestBannersRefresh` for your placement ID after initializing Braze.
This proactively fetches the latest banner data, ensuring your app can display new content quickly after launch.

!!step
lines-BannerSwiftUIView.swift=1-46

#### 3. Build a SwiftUI banner view component

Create a reusable SwiftUI View that can display a Braze Banner if available, and contains your main app content as needed.

!!step
lines-BannerSwiftUIView.swift=36-43

#### 4. Check if a banner is available before rendering

Before attempting to show the banner, call `getBanner(for:placementID)` in `.onAppear`.
Set a state variable (`hasBannerForPlacement`) so your UI only tries to render the `BannerView` if content actually exists for the user.

!!step
lines-BannerSwiftUIView.swift=17-32

#### 5. Show BannerView only when ready

Conditionally render `BrazeBannerUI.BannerView` only if a banner is present and the SDK is initialized.
This prevents blank/white spaces in your UI when no banner is available.

!!step
lines-BannerSwiftUIView.swift=23-32

#### 6. Dynamically update banner height

Use the `processContentUpdates` callback to track banner content height as soon as it loads.
Update your SwiftUI state (`contentHeight`) and use `.frame(height:)` to control the banner’s visible height in your layout.

!!step
lines-BannerSwiftUIView.swift=34

#### 7. Limit banner height for a consistent look

Apply a `.frame(height: min(contentHeight, 80))` modifier to ensure your banner never exceeds a maximum height (e.g., 80 points), keeping the UI visually balanced regardless of content.

{% endscrolly %}
{% endtab %}
{% endtabs %}
