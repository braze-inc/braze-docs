## Conditions préalables

Avant de commencer ce tutoriel, veuillez vérifier que votre SDK Braze répond aux exigences minimales en matière de version :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Affichage de bannières pour le SDK Swift

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

!étape
lignes-=14AppDelegate.swift

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-=20AppDelegate.swift

#### 2\. Veuillez actualiser vos placements.

Après avoir initialisé le SDK Braze,`call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`veuillez actualiser le contenu de la bannière au début de chaque session.

!étape
lignes-=19-37BannerViewController.swift

#### 3\. Veuillez initialiser la bannière et fournir un rappel.

Veuillez créer une`BrazeBannerUI.BannerUIView`instance avec votre objet Braze et votre ID de placement, puis fournissez un`processContentUpdates`rappel pour afficher la bannière et mettre à jour sa contrainte de hauteur en fonction de la hauteur du contenu fourni.

!étape
lignes-=38-40BannerViewController.swift

#### 4\. Activer les contraintes de disposition automatique

Veuillez masquer l'affichage de la bannière par défaut, puis désactiver la traduction du masque de redimensionnement automatique afin d'activer les contraintes de disposition automatique.

!étape
lignes-=43-58BannerViewController.swift

#### 5\. Ancrer le contenu et définir des contraintes de hauteur

Ancrez votre contenu principal en haut à l'aide de la disposition automatique et placez la vue Bannière directement en dessous. Épinglez les bords supérieur, inférieur et latéral de la bannière à la zone sécurisée, et définissez une contrainte de hauteur initiale`0` qui sera mise à jour lors du chargement du contenu.

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
lignes-=13AppDelegate.swift

#### 1\. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!étape
lignes-AppDelegate.swift=19

#### 2\. Veuillez actualiser vos placements.

Après avoir initialisé le SDK Braze, veuillez appeler`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`pour actualiser le contenu de la bannière au début de chaque session.

!étape
lignes-=1-46BannerSwiftUIView.swift

#### 3\. Créer un composant de vue

Veuillez créer un composant de vue SwiftUI réutilisable qui affiche les bannières disponibles et contient le contenu principal de votre application si nécessaire.

!étape
lignes-=36-43BannerSwiftUIView.swift

#### 4\. Afficher uniquement les bannières disponibles

Veuillez tenter d'afficher uniquement si le `BrazeBannerUI.BannerView`SDK est initialisé et si le contenu de la bannière existe pour cet utilisateur. Dans `.onAppear`, veuillez appeler`getBanner(for:placementID)`pour définir l'état de `hasBannerForPlacement`.

!étape
lignes-=17-32BannerSwiftUIView.swift

#### 5\. Afficher uniquement`BannerView` une fois le chargement terminé

Afin d'éviter les espaces vides dans votre interface utilisateur, veuillez n'afficher le `BrazeBannerUI.BannerView`contenu que si une bannière est présente et que le SDK est initialisé.

!étape
lignes-=23-32BannerSwiftUIView.swift

#### 6\. Mettre à jour de manière dynamique la hauteur de la bannière

Veuillez utiliser la`processContentUpdates`fonction de rappel pour récupérer la hauteur du contenu de la bannière dès qu'elle se charge. Veuillez mettre à jour votre état SwiftUI (`contentHeight`) et appliquer une`.frame(height:)`contrainte en utilisant la hauteur fournie.

!étape
lignes-BannerSwiftUIView.swift=34

#### 7\. Veuillez limiter la hauteur de la bannière.

Afin de garantir que votre bannière ne dépasse jamais la hauteur maximale, veuillez appliquer un`.frame(height: min(contentHeight, 80))`modificateur. Cela permettra de conserver l'équilibre visuel de votre interface utilisateur, quel que soit le contenu de la bannière.

{% endscrolly %}
{% endtab %}
{% endtabs %}
