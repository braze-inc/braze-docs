## 前提条件

このチュートリアルを始める前に、Braze SDKが最低バージョン要件を満たしていることを確認せよ：

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
lines-=14AppDelegate.swift

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
行AppDelegate.swift数-=20

#### 2\.配置を更新する

Braze SDKを初期化した後、各セッションの開始時に`call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`バナーコンテンツを更新する。

!!step
行BannerViewController.swift番号19-37

#### 3\.バナーを初期化し、コールバックを提供する

Brazeオブジェクトと配置IDでインスタンス`BrazeBannerUI.BannerUIView`を作成し、提供されたコンテンツの高さに基づいてバナーを表示し、その高さ制約を更新する`processContentUpdates`コールバックを提供する。

!!step
行BannerViewController.swift-=38-40

#### 4. オートレイアウトの制約のイネーブルメント

デフォルトでバナービューを非表示にし、自動レイアウトのイネーブルメントを有効にするために自動リサイズマスクの変換を無効にする。

!!step
行BannerViewController.swift番号43-58

#### 5. アンカーコンテンツを設定し、高さの制約を適用する

メインコンテンツをオートレイアウトで最上部に固定し、バナービューをその直下に配置する。バナーの上端、下端、および両端を安全領域に固定する。初期の高さ制約を設定し、コンテンツを読み込む際に更新される`0`ようにする。

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
行AppDelegate.swift数-=13

#### 1\.デバッグを有効にする(オプション)

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=19

#### 2\.配置を更新する

Braze SDKを初期化した後、各セッションの開始時にバナーコンテンツを更新するために\``requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`refresh`を呼び出す。

!!step
行BannerSwiftUIView.swift番号-=1-46

#### 3\.ビューコンポーネントを作成する

利用可能なバナーを表示し、必要に応じてメインアプリコンテンツを含む、再利用可能なSwiftUIビューコンポーネントを作成する。

!!step
行BannerSwiftUIView.swift番号36-43

#### 4. 利用可能なバナーのみを表示する

SDKが初期化され、かつそのユーザー向けのバナーコンテンツが存在する場合にのみ`BrazeBannerUI.BannerView`表示を試みる。において`.onAppear`、を呼び出して`getBanner(for:placementID)`の状態`hasBannerForPlacement`を設定する。

!!step
行BannerSwiftUIView.swift番号-=17-32

#### 5. 読み込みが終わってから`BannerView`表示する

UIに空白部分が生じないように、バナーが存在し、かつSDKが初期化されている場合にのみ`BrazeBannerUI.BannerView`表示する。

!!step
行BannerSwiftUIView.swift番号23-32

#### 6. バナーの高さをダイナミックに更新する

コール`processContentUpdates`バックを使って、バナーのコンテンツの高さを読み込みが完了次第取得する。SwiftUIのステートを更新し、指定された高さを使って`contentHeight`制約`.frame(height:)`を適用する。

!!step
lines-BannerSwiftUIView.swift=34

#### 7. バナーの高さを制限する

バナーが最大の高さを超えないようにするには、修飾`.frame(height: min(contentHeight, 80))`子を使う。これにより、バナーの内容に関わらず、UIの視覚的なバランスが保たれる。

{% endscrolly %}
{% endtab %}
{% endtabs %}
