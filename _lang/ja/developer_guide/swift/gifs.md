{% multi_lang_include developer_guide/prerequisites/swift.md %}

## カスタムイメージライブラリの統合

### ステップ 1: SDWebImageを統合する

[SDWebImageリポジトリを](https://github.com/SDWebImage/SDWebImage)Xcodeプロジェクトに統合する。

### ステップ 2: 新しいSWIFTファイルを作成する

Xcodeプロジェクトで、`SDWebImageGIFViewProvider.swift` という新しいファイルを作成し、以下をインポートする：

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### ステップ 3: `GIFViewProvider` を追加する

次に、サンプルの SDWebImage を追加する。 [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/).ファイルは以下のようなものであるべきだ：

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

### ステップ 4: を修正する。 `AppDelegate.swift`

プロジェクトの`AppDelegate.swift` で、`GIFViewProvider` を使って`BrazeUI` コンポーネントに GIF サポートを追加する。ファイルは以下のようなものであるべきだ：

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
