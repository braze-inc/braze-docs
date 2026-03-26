## Requisitos previos

Antes de comenzar este tutorial, comprueba que tu SDK de Braze cumple los requisitos mínimos de versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Mostrar banners para el SDK de SWIFT

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

!!paso
líneas-=14AppDelegate.swift

#### 1\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=20AppDelegate.swift

#### 2\. Actualiza tus ubicaciones

Después de inicializar el SDK de Braze,`call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`  para actualizar el contenido del banner al inicio de cada sesión.

!!paso
líneas-=19-37BannerViewController.swift

#### 3\. Inicializa el banner y proporciona una devolución de llamada.

Crea una`BrazeBannerUI.BannerUIView`instancia con tu objeto Braze y el ID de ubicación, y proporciona una`processContentUpdates`devolución de llamada para mostrar el banner y actualizar su restricción de altura en función de la altura del contenido proporcionado.

!!paso
líneas-=38-40BannerViewController.swift

#### 4\. Habilitar restricciones de diseño automático

Oculta la vista del banner de forma predeterminada y, a continuación, desactiva la traducción de la máscara de redimensionamiento automático para habilitar las restricciones de diseño automático.

!!paso
líneas-=43-58BannerViewController.swift

#### 5\. Anclar contenido y establecer restricciones de altura

Fija tu contenido principal en la parte superior utilizando el diseño automático y coloca la vista Banner directamente debajo. Fija los bordes superior, inferior y lateral del banner al área segura y establece una restricción de altura inicial`0` que se actualizará cuando se cargue el contenido.

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

!!paso
líneas-=13AppDelegate.swift

#### 1\. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera la posibilidad de habilitar la depuración.

!!paso
líneas-=19AppDelegate.swift

#### 2\. Actualiza tus ubicaciones

Después de inicializar el SDK de Braze, llama a`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`  para actualizar el contenido del banner al inicio de cada sesión.

!!paso
líneas-=1-46BannerSwiftUIView.swift

#### 3\. Crear un componente de vista

Crea un componente de vista SwiftUI reutilizable que muestre los banners disponibles y contenga el contenido principal de tu aplicación si es necesario.

!!paso
líneas-=36-43BannerSwiftUIView.swift

#### 4\. Mostrar solo los banners disponibles

Solo intenta mostrar`BrazeBannerUI.BannerView`  si el SDK está inicializado y existe contenido de banner para ese usuario. En `.onAppear`, llama a`getBanner(for:placementID)`  para establecer la configuración del estado`hasBannerForPlacement`.

!!paso
líneas-=17-32BannerSwiftUIView.swift

#### 5\. Mostrar solo  `BannerView`después de que se cargue

Para evitar espacios en blanco en la interfaz de usuario, solo muestra`BrazeBannerUI.BannerView`  si hay un banner presente y el SDK está inicializado.

!!paso
líneas-=23-32BannerSwiftUIView.swift

#### 6\. Actualizar de forma dinámica la altura del banner

Utiliza la`processContentUpdates`devolución de llamada para obtener la altura del contenido del banner tan pronto como se cargue. Actualiza tu estado SwiftUI (`contentHeight`) y aplica una`.frame(height:)`restricción utilizando la altura proporcionada.

!!paso
líneas-=34BannerSwiftUIView.swift

#### 7\. Limitar la altura del banner

Para asegurarte de que tu banner nunca supere la altura máxima, aplica un`.frame(height: min(contentHeight, 80))`modificador. Esto mantendrá tu interfaz de usuario visualmente equilibrada independientemente del contenido del banner.

{% endscrolly %}
{% endtab %}
{% endtabs %}
