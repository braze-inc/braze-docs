{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Integração de uma biblioteca de imagens personalizada

### Etapa 1: Integrar SDWebImage

Integre o [repositório SDWebImage](https://github.com/SDWebImage/SDWebImage) em seu projeto Xcode.

### Etapa 2: Criar um novo arquivo Swift

Em seu projeto Xcode, crie um novo arquivo chamado `SDWebImageGIFViewProvider.swift` e importe o seguinte:

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### Etapa 3: Adicionar `GIFViewProvider`

Em seguida, adicione nossa amostra de SDWebImage [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). Seu arquivo deve ser semelhante ao seguinte:

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

### Etapa 4: Modifique seu `AppDelegate.swift`

No site `AppDelegate.swift` de seu projeto, adicione suporte a GIF aos componentes `BrazeUI` usando `GIFViewProvider`. Seu arquivo deve ser semelhante ao seguinte:

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
