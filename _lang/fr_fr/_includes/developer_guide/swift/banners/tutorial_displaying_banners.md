## Conditions préalables

Avant de commencer ce tutoriel, vérifiez que votre SDK Braze répond aux exigences minimales en matière de version :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Affichage de bannières pour le SDK Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Afficher les bannières Swift" %}

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

!étape
lignes-AppDelegate.swift=14

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=20

#### 2\. Actualisez vos stages

Après avoir initialisé le SDK de Braze, `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` pour actualiser le contenu de la bannière au début de chaque session.

!étape
lignes-BannerViewController.swift=19-37

#### 3\. Initialiser la bannière et fournir un rappel

Créez une instance `BrazeBannerUI.BannerUIView` avec votre objet Braze et votre ID de placement, et fournissez un rappel `processContentUpdates` pour démasquer la bannière et mettre à jour sa contrainte de hauteur en fonction de la hauteur du contenu fournie.

!étape
lignes-BannerViewController.swift=38-40

#### 4\. Activer les contraintes de mise en page automatique

Masquez la vue de la bannière par défaut, puis désactivez la traduction du masque d'autodimensionnement pour activer les contraintes de mise en page automatique.

!étape
lignes-BannerViewController.swift=43-58

#### 5\. Ancrer le contenu et fixer des contraintes de hauteur

Ancrez votre contenu principal en haut à l'aide de la mise en page automatique et placez la vue de la bannière directement en dessous. Fixez les bords avant, arrière et inférieur de la bannière à la zone de sécurité et définissez une contrainte de hauteur initiale de `0` qui sera mise à jour lors du chargement du contenu.

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

!étape
lignes-AppDelegate.swift=13

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=19

#### 2\. Actualisez vos stages

Après avoir initialisé le SDK Braze, appelez `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` pour actualiser le contenu de la bannière au début de chaque session.

!étape
lignes-BannerSwiftUIView.swift=1-46

#### 3\. Créer un composant de vue

Créez un composant de vue SwiftUI réutilisable qui affiche les bannières disponibles et contient le contenu principal de votre application si nécessaire.

!étape
lignes-BannerSwiftUIView.swift=36-43

#### 4\. Afficher uniquement les bannières disponibles

Ne tentez d'afficher `BrazeBannerUI.BannerView` que si le SDK est initialisé et que le contenu de la bannière existe pour cet utilisateur. Dans `.onAppear`, appelez `getBanner(for:placementID)` pour définir l'état de `hasBannerForPlacement`.

!étape
lignes-BannerSwiftUIView.swift=17-32

#### 5\. N'affiche `BannerView` qu'après son chargement

Pour éviter les espaces vides dans votre interface utilisateur, n'affichez `BrazeBannerUI.BannerView` que si une bannière est présente et que le SDK est initialisé.

!étape
lignes-BannerSwiftUIView.swift=23-32

#### 6\. Mise à jour dynamique de la hauteur de la bannière

Utilisez le rappel `processContentUpdates` pour récupérer la hauteur du contenu de la bannière dès son chargement. Mettez à jour votre état SwiftUI (`contentHeight`) et appliquez une contrainte `.frame(height:)` en utilisant la hauteur fournie.

!étape
lignes-BannerSwiftUIView.swift=34

#### 7\. Limiter la hauteur de la bannière

Pour vous assurer que votre bannière ne dépasse jamais la hauteur maximale, appliquez le modificateur `.frame(height: min(contentHeight, 80))`. Ainsi, votre interface utilisateur restera visuellement équilibrée, quel que soit le contenu de la bannière.

{% endscrolly %}
{% endtab %}
{% endtabs %}
