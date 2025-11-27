## 前提条件

このチュートリアルを始める前に、お使いのBraze SDKが最小バージョン要件を満たしていることを確認する：

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Swift SDKのバナーを表示する

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Swift" %}

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
lines-AppDelegate.swift=9-21

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=9-21

#### 2\.プレースメントをリフレッシュする

Braze SDKを初期化した後、`call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` 、各セッションの開始時にBannerコンテンツをリフレッシュする。

!!step
lines-BannerViewController.swift=9-21

#### 3\.バナーを初期化し、コールバックを提供する

Brazeオブジェクトと配置IDで`BrazeBannerUI.BannerUIView` インスタンスを作成し、`processContentUpdates` コールバックを提供してBannerを非表示にし、提供されたコンテンツの高さに基づいて高さ制約を更新する。

!!step
lines-BannerViewController.swift=9-21

#### 4\.自動レイアウト制約をイネーブルメントにする

デフォルトでバナービューを非表示にし、オートレイアウト制約を有効にするためにマスクの自動サイズ変換を無効にする。

!!step
lines-BannerViewController.swift=9-21

#### 5. コンテンツのアンカーと高さ制限の設定

オートレイアウトを使ってメインコンテンツをトップに固定し、バナー表示をその直下に配置する。バナーの前縁、後縁、下縁を安全な領域に固定し、`0` の初期高さ制約を設定する。この高さはコンテンツが読み込まれたときに更新される。

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
lines-AppDelegate.swift=9-21

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=19

#### 2\.プレースメントをリフレッシュする

Braze SDKを初期化した後、`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` を呼び出し、各セッションの開始時にバナーコンテンツをリフレッシュする。

!!step
lines-BannerSwiftUIView.swift=9-21

#### 3\.ビュー・コンポーネントを作成する

利用可能なバナーを表示し、必要に応じてアプリのメインコンテンツを含む、再利用可能なSwiftUIビューコンポーネントを作成する。

!!step
lines-BannerSwiftUIView.swift=9-21

#### 4\.利用可能なバナーのみを表示する

SDKが初期化され、そのユーザーのバナーコンテンツが存在する場合のみ、`BrazeBannerUI.BannerView` 。`.onAppear` 内で、`getBanner(for:placementID)` をコールし、`hasBannerForPlacement` の状態を設定する。

!!step
lines-BannerSwiftUIView.swift=9-21

#### 5. `BannerView` を読み込んだ後のみ表示する。

UIの空白を避けるため、バナーが存在し、SDKが初期化されている場合にのみ、`BrazeBannerUI.BannerView` 。

!!step
lines-BannerSwiftUIView.swift=9-21

#### 6. バナーの高さをダイナミックに更新する

`processContentUpdates` コールバックを使って、バナーが読み込まれたらすぐにコンテンツの高さを取得する。SwiftUIの状態(`contentHeight`)を更新し、提供された高さを使用して`.frame(height:)` 制約を適用する。

!!step
lines-BannerSwiftUIView.swift=34

#### 7. バナーの高さを制限する

バナーが最大高さを超えないようにするには、`.frame(height: min(contentHeight, 80))` の修正を適用する。こうすることで、バナーの内容にかかわらず、UIの視覚的なバランスを保つことができる。

{% endscrolly %}
{% endtab %}
{% endtabs %}
