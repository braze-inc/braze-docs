## Pré-requisitos

Antes de iniciar este tutorial, verifique se o SDK do Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibição de banners para o Swift SDK

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Exibindo Banners Swift" %}

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

!!! etapa
linhas-AppDelegate.swift=14

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
linhas-AppDelegate.swift=20

#### 2\. Atualize suas colocações

Após inicializar o SDK do Braze, acesse `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para atualizar o conteúdo do banner no início de cada sessão.

!!! etapa
Linhas -BannerViewController.swift=19-37

#### 3\. Inicialize o Banner e forneça um retorno de chamada

Crie uma instância `BrazeBannerUI.BannerUIView` com seu objeto Braze e ID de posicionamento e forneça um retorno de chamada `processContentUpdates` para exibir o Banner e atualizar sua restrição de altura com base na altura do conteúdo fornecido.

!!! etapa
Linhas -BannerViewController.swift=38-40

#### 4\. Ativar restrições de Auto Layout

Oculte a visualização de banner por padrão e, em seguida, desative a tradução da máscara de redimensionamento automático para ativar as restrições do Auto Layout.

!!! etapa
Linhas -BannerViewController.swift=43-58

#### 5\. Ancorar conteúdo e definir restrições de altura

Ancore seu conteúdo principal na parte superior usando o Auto Layout e coloque a visualização do banner diretamente abaixo dele. Fixe as bordas principal, final e inferior do banner na área segura e defina uma restrição de altura inicial de `0` que será atualizada quando o conteúdo for carregado.

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

!!! etapa
linhas-AppDelegate.swift=13

#### 1\. Ativar a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere a possibilidade de ativar a depuração.

!!! etapa
linhas-AppDelegate.swift=19

#### 2\. Atualize suas colocações

Após inicializar o SDK do Braze, chame `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para atualizar o conteúdo do banner no início de cada sessão.

!!! etapa
linhas-BannerSwiftUIView.swift=1-46

#### 3\. Criar um componente de visualização

Crie um componente de visualização SwiftUI reutilizável que exiba os Banners disponíveis e contenha o conteúdo principal do app, se necessário.

!!! etapa
Linhas -BannerSwiftUIView.swift=36-43

#### 4\. Exibir apenas os Banners disponíveis

Só tente mostrar `BrazeBannerUI.BannerView` se o SDK for inicializado e o conteúdo do Banner existir para esse usuário. Em `.onAppear`, chame `getBanner(for:placementID)` para definir o estado de `hasBannerForPlacement`.

!!! etapa
Linhas -BannerSwiftUIView.swift=17-32

#### 5\. Mostrar apenas `BannerView` após o carregamento

Para evitar espaços em branco em sua interface do usuário, mostre o site `BrazeBannerUI.BannerView` somente se um banner estiver presente e o SDK for inicializado.

!!! etapa
Linhas -BannerSwiftUIView.swift=23-32

#### 6\. Atualizar dinamicamente a altura do banner

Use o retorno de chamada `processContentUpdates` para obter a altura do conteúdo do banner assim que ele for carregado. Atualize o estado do SwiftUI (`contentHeight`) e aplique uma restrição `.frame(height:)` usando a altura fornecida.

!!! etapa
linhas-BannerSwiftUIView.swift=34

#### 7\. Limitar a altura do banner

Para garantir que seu banner nunca ultrapasse a altura máxima, aplique um modificador `.frame(height: min(contentHeight, 80))`. Isso manterá sua interface do usuário visualmente equilibrada, independentemente do conteúdo do banner.

{% endscrolly %}
{% endtab %}
{% endtabs %}
