## 필수 조건

이 튜토리얼을 시작하기 전에 Braze 소프트웨어 개발 키트가 최소 버전 요구 사항을 충족하는지 확인하세요:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Swift 소프트웨어 개발 키트 배너 표시하기

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md 튜토리얼="배너 신속하게 표시하기" %}

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

!!단계
lines-AppDelegate.swift=14

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-AppDelegate.swift=20

#### 2\. 게재 위치 새로고침하기

각 세션이 시작될 때마다 배너 콘텐츠를 새로고침하려면 Braze 소프트웨어 개발 키트( `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` )를 초기화하세요.

!!단계
라인-BannerViewController.swift=19-37

#### 3\. 배너 초기화 및 콜백 제공

Braze 객체와 배치 ID로 `BrazeBannerUI.BannerUIView` 인스턴스를 생성하고 `processContentUpdates` 콜백을 제공하여 제공된 콘텐츠 높이에 따라 배너의 숨김을 해제하고 높이 제약 조건을 업데이트합니다.

!!단계
라인-BannerViewController.swift=38-40

#### 4\. 자동 레이아웃 제약 조건 인에이블먼트

기본값으로 배너 보기를 숨긴 다음 자동 크기 조정 마스크 변환을 비활성화하여 자동 레이아웃 제약 조건을 인에이블먼트합니다.

!!단계
라인-BannerViewController.swift=43-58

#### 5\. 콘텐츠 앵커 및 높이 제약 조건 설정하기

자동 레이아웃을 사용하여 기본 콘텐츠를 상단에 고정하고 그 바로 아래에 배너 보기를 배치합니다. 배너의 선행, 후행 및 하단 가장자리를 안전 영역에 고정하고 콘텐츠가 로드될 때 업데이트되는 초기 높이 제약 조건을 `0` 으로 설정합니다.

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

!!단계
lines-AppDelegate.swift=13

#### 1\. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!단계
lines-AppDelegate.swift=19

#### 2\. 게재 위치 새로고침하기

Braze 소프트웨어 개발 키트를 초기화한 후 각 세션이 시작될 때마다 `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` 으로 전화하여 배너 콘텐츠를 새로고침합니다.

!!단계
라인-BannerSwiftUIView.swift=1-46

#### 3\. 뷰 구성 요소 만들기

사용 가능한 배너를 표시하고 필요한 경우 기본 앱 콘텐츠를 포함하는 재사용 가능한 SwiftUI 보기 컴포넌트를 만듭니다.

!!단계
라인-BannerSwiftUIView.swift=36-43

#### 4\. 사용 가능한 배너만 표시

소프트웨어 개발 키트가 초기화되어 있고 해당 사용자에 대한 배너 콘텐츠가 있는 경우에만 `BrazeBannerUI.BannerView` 표시를 시도합니다. `.onAppear` 에서 `getBanner(for:placementID)` 으로 호출하여 `hasBannerForPlacement` 의 상태를 설정합니다.

!!단계
라인-BannerSwiftUIView.swift=17-32

#### 5\. 로드된 후에만 `BannerView` 표시

UI의 공백을 방지하려면 배너가 있고 소프트웨어 개발 키트가 초기화된 경우에만 `BrazeBannerUI.BannerView` 을 표시하세요.

!!단계
lines-BannerSwiftUIView.swift=23-32

#### 6\. 배너 높이 동적 업데이트

`processContentUpdates` 콜백을 사용하여 배너가 로드되는 즉시 배너의 콘텐츠 높이를 가져옵니다. SwiftUI 상태(`contentHeight`)를 업데이트하고 제공된 높이를 사용하여 `.frame(height:)` 제약 조건을 적용합니다.

!!단계
lines-BannerSwiftUIView.swift=34

#### 7\. 배너 높이 제한

배너가 최대 높이를 초과하지 않도록 하려면 `.frame(height: min(contentHeight, 80))` 수정자를 적용하세요. 이렇게 하면 배너의 콘텐츠와 관계없이 UI가 시각적으로 균형 잡힌 상태를 유지합니다.

{% endscrolly %}
{% endtab %}
{% endtabs %}
