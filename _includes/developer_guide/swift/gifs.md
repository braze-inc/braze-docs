{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Integrating a custom image library

### Step 1: Integrate SDWebImage

Integrate the [SDWebImage repository](https://github.com/SDWebImage/SDWebImage) into your Xcode project.

### Step 2: Create a new Swift file

In your Xcode project, create a new file named `SDWebImageGIFViewProvider.swift` and import the following:

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### Step 3: Add `GIFViewProvider`

Next, add our sample SDWebImage [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). Your file should be similar to the following:

```swift
import UIKit
import BrazeUI
import SDWebImage


extension GIFViewProvider {


  /// A GIF view provider using [SDWebImage](https://github.com/SDWebImage/SDWebImage) as a
  /// rendering library.
  public static let sdWebImage = Self(
    view: { SDAnimatedImageView(image: image(for: $0)) },
    updateView: { ($0 as? SDAnimatedImageView)?.image = image(for: $1) }
  )


  private static func image(for url: URL?) -> UIImage? {
    guard let url else { return nil }
    return url.pathExtension == "gif"
      ? SDAnimatedImage(contentsOfFile: url.path)
      : UIImage(contentsOfFile: url.path)
  }


}
```

### Step 4: Modify your `AppDelegate.swift`

In your project's `AppDelegate.swift`, add GIF support to your `BrazeUI` components using `GIFViewProvider`. Your file should be similar to the following:

```swift
import UIKit
import BrazeKit
import BrazeUI


@main
class AppDelegate: UIResponder, UIApplicationDelegate {


  static var braze: Braze? = nil


  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    /* ... */


    GIFViewProvider.shared = .sdWebImage


    return true
  }
}
```
