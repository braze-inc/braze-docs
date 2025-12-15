## 前提条件

このチュートリアルを開始する前に、Braze SDKが最低バージョン要件を満たしていることを確認してください。

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## スウィフトSDKのバナーの表示

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
lines-AppDelegate.swift=14

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=20

#### 2\.配置を更新する

Braze SDKを初期化した後、`call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` を実行して、それぞれのセッションの先頭でバナーの内容を更新します。

!!step
lines-BannerViewController.swift=19-37

#### 3\.バナーを初期化し、コールバックを提供する

BrazeオブジェクトとプレイスメントID で`BrazeBannerUI.BannerUIView` インスタンスを作成し、`processContentUpdates` コールバックを指定してバナーを非表示にし、提供されたコンテンツの高さに基づいてその高さのトレーニングt を更新します。

!!step
lines-BannerViewController.swift=38-40

#### 4. 自動レイアウト設定を有効にするtsトレーニング

デフォルトでバナービューを非表示にしてから、マスク変換の自動サイズ変更を無効にして、自動レイアウト設定のトレーニングts を有効にします。

!!step
lines-BannerViewController.swift=43-58

#### 5. アンカーの内容と高さの設定トレーニングts

Auto Layout を使用してメインコンテンツを上に固定し、その下にバナービューを配置します。バナーの先頭、末尾、および底辺を安全領域に固定し、内容がs 読み込むのときに更新d になる`0` の最初の高さcons トレーニングt を設定します。

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
lines-AppDelegate.swift=13

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=19

#### 2\.配置を更新する

Braze SDKを初期化した後、`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` を呼び出して、それぞれのセッションの先頭でバナーの内容を更新します。

!!step
lines-BannerSwiftUIView.swift=1-46

#### 3\.ビューコンポーネントの作成

使用可能なバナーを表示し、必要に応じて主なアプリ内容を含む再利用可能なSwiftUI ビューコンポーネントを作成します。

!!step
lines-BannerSwiftUIView.swift=36-43

#### 4. 利用可能なバナーのみ表示

SDKが初期化され、バナーコンテンツがそのユーザーに存在する場合にのみ、`BrazeBannerUI.BannerView` を表示しようとします。`.onAppear`では、`getBanner(for:placementID)`を呼び出して`hasBannerForPlacement`の状態を設定します。

!!step
lines-BannerSwiftUIView.swift=17-32

#### 5. sを読み込むした後、`BannerView`のみを表示する

UI の空白を回避するには、バナーが存在し、SDKが初期化されている場合にのみ`BrazeBannerUI.BannerView` を表示します。

!!step
lines-BannerSwiftUIView.swift=23-32

#### 6. バナーの高さをダイナミックに更新

`processContentUpdates` コールバックを使用して、s を読み込むするとすぐにバナーの内容の高さを取得します。SwiftUI ステート(`contentHeight`) をアップデートし、指定された高さを使用してly a `.frame(height:)` cons トレーニングt をアプリします。

!!step
lines-BannerSwiftUIView.swift=34

#### 7. バナーの高さを制限する

バナーの高さが上限を超えないようにするには、`.frame(height: min(contentHeight, 80))` 修飾子をアプリします。これにより、バナーのコンテンツに関係なくUI の視覚的なバランスが維持されます。

{% endscrolly %}
{% endtab %}
{% endtabs %}
