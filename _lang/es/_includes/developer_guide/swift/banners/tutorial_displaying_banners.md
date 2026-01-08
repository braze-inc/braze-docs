## Requisitos previos

Antes de empezar este tutorial, comprueba que tu SDK de Braze cumple los requisitos mínimos de la versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Visualización de banners para el SDK de Swift

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Visualización de banners Swift" %}

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

Paso
líneas-AppDelegate.swift=14

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-AppDelegate.swift=20

#### 2\. Refresca tus colocaciones

Tras inicializar el SDK de Braze, `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para actualizar el contenido del Banner al inicio de cada sesión.

Paso
líneas-BannerViewController.swift=19-37

#### 3\. Inicializa el Banner y proporciona una devolución de llamada

Crea una instancia de `BrazeBannerUI.BannerUIView` con tu objeto Braze y tu ID de colocación, y proporciona una devolución de llamada a `processContentUpdates` para desocultar el Banner y actualizar su restricción de altura en función de la altura de contenido proporcionada.

Paso
líneas-BannerViewController.swift=38-40

#### 4\. Habilitar las restricciones del diseño automático

Oculta la vista de Banner de forma predeterminada y, a continuación, desactiva la traducción automática de máscaras para habilitar las restricciones del diseño automático.

Paso
líneas-BannerViewController.swift=43-58

#### 5\. Anclar contenido y establecer restricciones de altura

Ancla tu contenido principal a la parte superior utilizando el diseño automático, y coloca la vista de banner justo debajo. Fija los bordes inicial, final e inferior del Banner a la zona segura, y establece una restricción de altura inicial de `0` que se actualizará cuando se cargue el contenido.

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

Paso
líneas-AppDelegate.swift=13

#### 1\. Habilitar la depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

Paso
líneas-AppDelegate.swift=19

#### 2\. Refresca tus colocaciones

Tras inicializar el SDK de Braze, llama a `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para actualizar el contenido del Banner al inicio de cada sesión.

Paso
líneas-BannerSwiftUIView.swift=1-46

#### 3\. Crear un componente de vista

Crea un componente de vista SwiftUI reutilizable que muestre los Banners disponibles y contenga el contenido principal de tu aplicación si es necesario.

Paso
líneas-BannerSwiftUIView.swift=36-43

#### 4\. Mostrar sólo los banners disponibles

Sólo intenta mostrar `BrazeBannerUI.BannerView` si el SDK está inicializado y existe contenido de Banner para ese usuario. En `.onAppear`, llama a `getBanner(for:placementID)` para establecer el estado de `hasBannerForPlacement`.

Paso
líneas-BannerSwiftUIView.swift=17-32

#### 5\. Sólo muestra `BannerView` después de cargar

Para evitar espacios en blanco en tu IU, sólo muestra `BrazeBannerUI.BannerView` si hay un Banner y el SDK está inicializado.

Paso
líneas-BannerSwiftUIView.swift=23-32

#### 6\. Actualiza dinámicamente la altura del Banner

Utiliza la devolución de llamada `processContentUpdates` para obtener la altura del contenido del Banner en cuanto se cargue. Actualiza tu estado SwiftUI (`contentHeight`) y aplica una restricción `.frame(height:)` utilizando la altura proporcionada.

Paso
líneas-BannerSwiftUIView.swift=34

#### 7\. Limitar la altura del Banner

Para asegurarte de que tu Banner nunca supera la altura máxima, aplica un modificador `.frame(height: min(contentHeight, 80))`. Esto mantendrá tu IU visualmente equilibrada independientemente del contenido del Banner.

{% endscrolly %}
{% endtab %}
{% endtabs %}
