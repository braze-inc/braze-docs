{% multi_lang_include developer_guide/prerequisites/swift.md %}

## カスタムイメージライブラリの統合

### ステップ1:SDWebImageの統合

[SDWebImageリポジトリ](https://github.com/SDWebImage/SDWebImage)をXcodeプロジェクトに統合します。

### ステップ2: 新しいSwift ファイルを作成する

Xcode プロジェクトで、`SDWebImageGIFViewProvider.swift` という名前の新しいファイルを作成し、以下をインポートします。

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### ステップ 3:`GIFViewProvider` を追加する

次に、サンプルSDWebImage [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/) を追加します。ファイルは次のようになります。

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

### ステップ4:変更する `AppDelegate.swift`

プロジェクトの`AppDelegate.swift` で、`BrazeUI` コンポーネントに`GIFViewProvider` を使用してGIF サポートを追加します。ファイルは次のようになります。

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
