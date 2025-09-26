## Voraussetzungen

Bevor Sie mit diesem Tutorial beginnen, überprüfen Sie, ob Ihr Braze SDK die Mindestanforderungen erfüllt:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Anzeige von Bannern für das Swift SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md %}

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

!Schritt
Zeilen-AppDelegate.swift=14

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-AppDelegate.swift=20

#### 2\. Aktualisieren Sie Ihre Praktika

Nach der Initialisierung des Braze SDK, `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`, um die Bannerinhalte zu Beginn jeder Sitzung zu aktualisieren.

!Schritt
Zeilen-BannerViewController.swift=19-37

#### 3\. Initialisieren Sie das Banner und stellen Sie einen Callback bereit

Erstellen Sie eine Instanz `BrazeBannerUI.BannerUIView` mit Ihrem Braze-Objekt und Ihrer Platzierungs-ID und stellen Sie einen `processContentUpdates` Callback bereit, um das Banner einzublenden und seine Höhenbeschränkung auf der Grundlage der angegebenen Inhaltshöhe zu aktualisieren.

!Schritt
Zeilen-BannerViewController.swift=38-40

#### 4\. Enablement von Auto-Layout-Beschränkungen

Blenden Sie die Banner-Ansicht standardmäßig aus und deaktivieren Sie dann die automatische Übersetzung der Maske, um das Enablement von Auto-Layout-Einschränkungen zu aktivieren.

!Schritt
Zeilen-BannerViewController.swift=43-58

#### 5\. Inhalt verankern und Höhenbeschränkungen festlegen

Verankern Sie Ihren Hauptinhalt mit Auto-Layout ganz oben und platzieren Sie die Banneransicht direkt darunter. Legen Sie den vorderen, hinteren und unteren Rand des Banners im sicheren Bereich fest und setzen Sie eine anfängliche Höhenbeschränkung von `0`, die aktualisiert wird, wenn Inhalte geladen werden.

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

!Schritt
Zeilen-AppDelegate.swift=13

#### 1\. Enablement von Fehlersuchen (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!Schritt
Zeilen-AppDelegate.swift=19

#### 2\. Aktualisieren Sie Ihre Praktika

Rufen Sie nach der Initialisierung des Braze SDK `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` auf, um die Bannerinhalte zu Beginn jeder Sitzung zu aktualisieren.

!Schritt
Zeilen-BannerSwiftUIView.swift=1-46

#### 3\. Erstellen Sie eine Ansichtskomponente

Erstellen Sie eine wiederverwendbare SwiftUI-Ansichtskomponente, die verfügbare Banner anzeigt und bei Bedarf Ihren Hauptinhalt für die App enthält.

!Schritt
Zeilen-BannerSwiftUIView.swift=36-43

#### 4\. Nur verfügbare Banner anzeigen

Versuchen Sie nur dann, `BrazeBannerUI.BannerView` anzuzeigen, wenn das SDK initialisiert ist und Banner-Inhalte für diesen Nutzer:innen existieren. Rufen Sie in `.onAppear` `getBanner(for:placementID)` auf, um den Status von `hasBannerForPlacement` zu setzen.

!Schritt
Zeilen-BannerSwiftUIView.swift=17-32

#### 5\. Zeigen Sie `BannerView` erst an, nachdem es geladen wurde.

Um leeren Raum in Ihrem UI zu vermeiden, zeigen Sie `BrazeBannerUI.BannerView` nur an, wenn ein Banner vorhanden und das SDK initialisiert ist.

!Schritt
Zeilen-BannerSwiftUIView.swift=23-32

#### 6\. Bannerhöhe dynamisch aktualisieren

Verwenden Sie den `processContentUpdates` Callback, um die Höhe des Bannerinhalts abzurufen, sobald er geladen ist. Aktualisieren Sie Ihren SwiftUI-Status (`contentHeight`) und wenden Sie eine `.frame(height:)` -Beschränkung mit der angegebenen Höhe an.

!Schritt
Zeilen-BannerSwiftUIView.swift=34

#### 7\. Begrenzen Sie die Höhe des Banners

Um sicherzustellen, dass Ihr Banner niemals die maximale Höhe überschreitet, wenden Sie einen `.frame(height: min(contentHeight, 80))` Modifikator an. So bleibt Ihre UI unabhängig vom Inhalt des Banners visuell ausgewogen.

{% endscrolly %}
{% endtab %}
{% endtabs %}
