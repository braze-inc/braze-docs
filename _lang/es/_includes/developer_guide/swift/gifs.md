{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Integración de una biblioteca de imágenes personalizada

### Paso 1: Integrar SDWebImage

Integra el [repositorio SDWebImage](https://github.com/SDWebImage/SDWebImage) en tu proyecto Xcode.

### Paso 2: Crear un nuevo archivo Swift

En tu proyecto Xcode, crea un nuevo archivo llamado `SDWebImageGIFViewProvider.swift` e importa lo siguiente:

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### Paso 3: Añade `GIFViewProvider`

A continuación, añade nuestra SDWebImage de muestra [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). Tu archivo debe ser similar al siguiente

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

### Paso 4: Modifica tu `AppDelegate.swift`

En la página `AppDelegate.swift` de tu proyecto, añade soporte GIF a tus componentes `BrazeUI` utilizando `GIFViewProvider`. Tu archivo debe ser similar al siguiente

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
