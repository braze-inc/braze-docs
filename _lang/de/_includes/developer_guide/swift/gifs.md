{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Eigene Bilderbibliotheken einbinden

### Schritt 1: SDWebImage integrieren

Integrieren Sie das [SDWebImage Repository](https://github.com/SDWebImage/SDWebImage) in Ihr Xcode Projekt.

### Schritt 2: Erstellen Sie eine neue Swift-Datei

Erstellen Sie in Ihrem Xcode-Projekt eine neue Datei mit dem Namen `SDWebImageGIFViewProvider.swift` und importieren Sie Folgendes:

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### Schritt 3: hinzufügen `GIFViewProvider`

Als nächstes fügen Sie unser SDWebImage-Beispiel hinzu [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). Ihre Datei sollte in etwa so aussehen wie die folgende:

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

### Schritt 4: Ändern Sie Ihr `AppDelegate.swift`

Fügen Sie in Ihrem Projekt `AppDelegate.swift` mit `GIFViewProvider` die GIF-Unterstützung zu Ihren `BrazeUI` Komponenten hinzu. Ihre Datei sollte in etwa so aussehen wie die folgende:

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
