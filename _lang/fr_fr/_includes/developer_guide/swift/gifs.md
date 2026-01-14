{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Intégration d'une bibliothèque d'images personnalisée

### Étape 1 : Intégration de SDwebimage

Intégrez le [référentiel SDwebimage](https://github.com/SDWebImage/SDWebImage) dans votre projet Xcode.

### Étape 2 : Créer un nouveau fichier Swift

Dans votre projet Xcode, créez un nouveau fichier nommé `SDWebImageGIFViewProvider.swift` et importez ce qui suit :

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### Étape 3 : Ajouter `GIFViewProvider`

Ensuite, ajoutez notre SDwebimage d'exemple [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). Votre fichier devrait ressembler à ce qui suit :

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

### Étape 4 : Modifiez votre `AppDelegate.swift`

Dans votre projet `AppDelegate.swift`, ajoutez le support GIF à vos composants `BrazeUI` à l'aide de `GIFViewProvider`. Votre fichier devrait ressembler à ce qui suit :

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
