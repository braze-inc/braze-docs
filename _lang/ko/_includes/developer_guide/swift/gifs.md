{% multi_lang_include developer_guide/prerequisites/swift.md %}

## 사용자 지정 이미지 라이브러리 통합

### 1단계: SD웹이미지 통합

[SDWebImage 저장소를](https://github.com/SDWebImage/SDWebImage) Xcode 프로젝트에 통합합니다.

### 2단계: 새 Swift 파일 만들기

Xcode 프로젝트에서 `SDWebImageGIFViewProvider.swift` 이라는 새 파일을 만들고 다음을 임포트합니다:

```swift
import UIKit
import BrazeUI
import SDWebImage
```

### 3단계: 추가 `GIFViewProvider`

다음으로 샘플 SDWebImage [`GIFViewProvider`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/gifviewprovider/). 파일은 다음과 비슷해야 합니다:

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

### 4단계: 수정 `AppDelegate.swift`

프로젝트의 `AppDelegate.swift` 에서 `GIFViewProvider` 을 사용하여 `BrazeUI` 컴포넌트에 GIF 지원을 추가합니다. 파일은 다음과 비슷해야 합니다:

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
