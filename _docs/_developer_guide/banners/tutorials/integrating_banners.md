---
nav_title: Integrating Banners
guide_top_header: Integrating Banners
article_title: Integrating Banners
page_order: 1
layout: scrolly
description: "A tutorial on how to integrate and refresh banner placements"
---

# Displaying a Banner by its Placement ID

{% sdktabs %}
{% sdktab android %}
{% scrolly %}

```kotlin file=MainApplication.kt
import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger

public class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.logLevel = Log.VERBOSE

        // Configure Braze with your SDK key and endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        // Subscribe to Banner updates
        Braze.getInstance(this)
            .subscribeToBannersUpdates { update ->
                for (banner in update.banners) {
                    Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                    // And any custom banner logic you'd like
                }
            }
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Inflate the XML layout
        setContentView(R.layout.banners)
        
        // Refresh placements
        Braze.getInstance(this)
            .requestBannersRefresh(
                listOf("top-1")
            )
    }
}
```

```xml file=banners.xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal">

        <!-- Banner placement -->
        <com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:placementId="top-1" />

        <!-- ...the rest of your activity layout -->

    </LinearLayout>
</ScrollView>
```

!!step
lines-MainApplication.kt=12

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-MainApplication.kt=21-28

#### 2. Subscribe to banner updates

Use `subscribeToBannersUpdates()` to listen for and react to incoming banner refresh results from the server.

!!step
lines-MainApplication.kt=30-34

#### 3. Refresh placements

Invoke `requestBannersRefresh()` to fetch the latest banner content from Braze for the specified placement ID(s).

!!step
lines-banners.xml=15-19

#### 4. Define the BannerView in banners.xml

Specify a `<com.braze.ui.banners.BannerView>` element with `app:placementId="<placement-id>"` so that Braze knows where to render the banner content in your UI.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
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
  var bannerHeightConstraint: NSLayoutConstraint?

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
lines-AppDelegate.swift=15

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=21

#### 2. Trigger a banners refresh

Call `requestBannersRefresh` for your placement ID after initializing Braze.
This proactively fetches the latest banner data, ensuring your app can display new content quickly after launch.

!!step
lines-BannerViewController.swift=18-32

#### 3. Initialize the Braze banner view with a processContentUpdates callback

Create your `BrazeBannerUI.BannerUIView` with the correct placement ID and Braze instance.
The `processContentUpdates` callback will fire whenever the banner height changes.
Inside the callback, unhide the banner and update its height constraint using the provided content height (capped at 80pt for this example).

!!step
lines-BannerViewController.swift=34-36

#### 4. Hide banner by default, enable Auto Layout

Hide the banner view until content loads and disable autoresizing mask translation to use Auto Layout constraints.

!!step
lines-BannerViewController.swift=43-57

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
lines-AppDelegate.swift=15

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-AppDelegate.swift=21

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
{% endsdktab %}
{% sdktab web %}
{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

#### 1. Enable debugging (optional)

Enable debugging while developing to make troubleshooting easier!

!!step
lines-index.js=8-24

#### 2. Subscribe to banner updates

Use `subscribeToBannersUpdates(callback)` to register a handler that will run any time banners are refreshed.

Within the callback, get the banner for your placement using `braze.getBanner("global_banner")`.

!!step
lines-index.js=15-22

#### 3. Insert the banner and handle control groups

If a banner is returned, insert it into your page with `braze.insertBanner(banner, container)`.

If the returned banner is a control group (i.e. `isControl` is true), hide or collapse the banner's container so your layout stays clean.

!!step
lines-index.js=25

#### 4. Request banners refresh

Call `requestBannersRefresh(["global_banner", ...])` after initializing to ensure your banners are fetched from Braze.
Call this whenever you want to refresh the banners for any placement(s).

!!step
lines-main.html=3

#### 5. Add a container for your banner

Add a div in your HTML (e.g. `<div id="global-banner-container"></div>`) where Braze will insert the banner content.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}
