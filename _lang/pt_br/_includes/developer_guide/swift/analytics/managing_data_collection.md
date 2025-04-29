## Manifesto de privacidade da Apple {#privacy-manifest}

### O que são dados de rastreamento?

A Apple define "dados de rastreamento" como os dados coletados em seu app sobre um usuário final ou dispositivo que está vinculado a dados de terceiros (como publicidade direcionada) ou a um corretor de dados. Para obter uma definição completa com exemplos, consulte [Apple: Rastreamento](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Por padrão, o SDK da Braze não coleta dados de rastreamento. No entanto, dependendo da configuração do SDK da Braze, talvez seja necessário listar dados específicos da Braze no manifesto de privacidade do app.

### O que é um manifesto de privacidade?

Um manifesto de privacidade é um arquivo em seu projeto Xcode que descreve o motivo pelo qual seu app e SDKs de terceiros coletam dados, juntamente com seus métodos de coleta de dados. Cada um dos seus SDKs de terceiros que rastreiam dados exige seu próprio manifesto de privacidade. Quando você [cria o relatório de privacidade do seu app](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), esses arquivos de manifesto de privacidade são automaticamente agregados em um único relatório.

### Domínios de dados de rastreamento da API

A partir do iOS 17.2, a Apple bloqueará todos os pontos de extremidade de rastreamento declarados em seu app até que o usuário final aceite um [aviso de transparência de rastreamento de anúncios (ATT)](https://support.apple.com/en-us/HT212025). A Braze fornece endpoints de rastreamento para encaminhar seus dados de rastreamento e, ao mesmo tempo, permite que você encaminhe dados primários que não sejam de rastreamento para o endpoint original. 

## Declaração de dados de rastreamento do Braze

{% alert tip %}
Para obter um passo a passo completo, consulte o [tutorial de dados de rastreamento de privacidade](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Pré-requisitos

A seguinte versão do Braze SDK é necessária para implementar esse recurso:

{% sdk_min_versions swift:9.0.0 %}

### Etapa 1: Analise suas políticas atuais

Revise as políticas atuais de coleta de dados do SDK do Braze com sua equipe jurídica para determinar se o seu app coleta dados de rastreamento [conforme definido pela Apple](#what-is-tracking-data). Se não estiver coletando dados de rastreamento, não é necessário personalizar seu manifesto de privacidade para o SDK da Braze neste momento. Para saber mais sobre as políticas de coleta de dados do SDK da Braze, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

{% alert important %}
Se algum de seus SDKs que não sejam da Braze coletar dados de rastreamento, será necessário analisar essas políticas separadamente.
{% endalert %}

### Etapa 2: Criar um manifesto de privacidade

Primeiro, verifique se você já tem um manifesto de privacidade procurando um arquivo `PrivacyInfo.xcprivacy` em seu projeto Xcode. Se você já tiver esse arquivo, prossiga para a próxima etapa. Caso contrário, consulte [Apple: Crie um manifesto de privacidade](sdk-tracking.iad-01.braze.com).

### Etapa 3: Adicione seu endpoint ao manifesto de privacidade

Em seu projeto Xcode, abra o arquivo `PrivacyInfo.xcprivacy` do app, clique com o botão direito do mouse na tabela e verifique **Chaves e Valores Brutos**.

{% alert note %}

{% endalert %}

![Um projeto do Xcode com o menu de contexto aberto e "Raw Keys and Values" destacado.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Em **Configuração de privacidade do app**, escolha **NSPrivacyTracking** e defina seu valor como **SIM**.

![O arquivo 'PrivacyInfo.xcprivacy' aberto com "NSPrivacyTracking" definido como "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Em **Configuração de privacidade do app**, escolha **NSPrivacyTrackingDomains**. Na matriz de domínios, adicione um novo elemento e defina seu valor como o ponto de extremidade que você [adicionou anteriormente ao seu `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate), prefixado com `sdk-tracking`.

![O arquivo 'PrivacyInfo.xcprivacy' aberto com um endpoint de rastreamento da Braze listado em "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Etapa 4: Declare seus dados de rastreamento

Em seguida, abra o site `AppDelegate.swift` e liste cada [propriedade de rastreamento](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que deseja declarar, criando uma lista de rastreamento estática ou dinâmica. Lembre-se de que a Apple bloqueará essas propriedades até que o usuário final aceite o prompt de ATT, portanto, liste apenas as propriedades que você e sua equipe jurídica consideram rastreamento. Por exemplo:

{% tabs %}
{% tab exemplo estático %}
No exemplo a seguir, `dateOfBirth`, `customEvent` e `customAttribute` são declarados como dados de rastreamento em uma lista estática. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab exemplo dinâmico %}
No exemplo a seguir, a lista de rastreamento é atualizada automaticamente depois que o usuário final aceita o prompt ATT.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Etapa 5: Evitar loops de repetição infinitos

Para evitar que o SDK entre em um loop infinito de repetição, use o método `set(adTrackingEnabled: enableAdTracking)` para lidar com as permissões de ATT. A propriedade `adTrackingEnabled` em seu método deve ser tratada de forma semelhante à seguinte:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Desativar o rastreamento de dados

Para desativar a atividade de rastreamento de dados no Swift SDK, defina a propriedade [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) para `false` em sua instância do Braze. Quando `enabled` é definido como `false`, o SDK da Braze ignora qualquer chamada para a API pública. O SDK também cancela todas as ações em andamento, como solicitações de rede, processamento de eventos, etc. 

## Limpeza de dados armazenados anteriormente

Você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para limpar completamente os dados do SDK armazenados localmente no dispositivo de um usuário.

Para as versões 7.0.0 e posteriores do Braze Swift, o SDK e o método `wipeData()` geram aleatoriamente um UUID para o ID do dispositivo. No entanto, se o seu `useUUIDAsDeviceId` estiver definido como `false` _ou_ se estiver usando o Swift SDK versão 5.7.0 ou anterior, também será necessário fazer uma solicitação de postagem para [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) já que o seu Identificador para Fornecedores (IDFV) será automaticamente usado como o ID do dispositivo desse usuário.

## Retomada do rastreamento de dados

Para retomar a coleta de dados, defina [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) como `true`. Lembre-se de que isso não restaurará nenhum dado apagado anteriormente.

## Coleção IDFV

Nas versões anteriores do SDK da Braze para iOS, o campo IDFV (Identifier for Vendor, identificador do fornecedor) era coletado automaticamente como o ID do dispositivo do usuário. A partir do Swift SDK `v5.7.0`, o campo IDFV foi desativado opcionalmente e, em vez disso, o Braze definiu um UUID aleatório como o ID do dispositivo. A partir do Swift SDK `v7.0.0`, o campo IDFV não será coletado por padrão, e um UUID será definido como o ID do dispositivo.

O recurso `useUUIDAsDeviceId` configura o [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) para definir o ID do dispositivo como um UUID. Tradicionalmente, o SDK do iOS atribuía a ID do dispositivo igual ao valor IDFV gerado pela Apple. Com esse recurso ativado por padrão em seu app iOS, todos os novos usuários criados por meio do SDK receberiam um ID de dispositivo igual a um UUID.

Se você ainda quiser coletar o IDFV separadamente, poderá usar [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Considerações

#### Versão do SDK

No Swift SDK `v7.0.0+`, quando `useUUIDAsDeviceId` estiver ativado (padrão), todos os novos usuários criados serão atribuídos a um ID de dispositivo aleatório. Todos os usuários existentes anteriormente manterão o mesmo valor de ID do dispositivo, que pode ter sido IDFV.

Quando esse recurso não estiver ativado, os dispositivos continuarão a ser atribuídos ao IDFV após a criação.

#### Downstream 

**Parceiros tecnológicos**: Quando esse recurso for ativado, todos os parceiros de tecnologia que derivam o valor IDFV do ID do dispositivo Braze não terão mais acesso a esses dados. Se o valor IDFV derivado do dispositivo for necessário para a integração com parceiros, recomendamos que você defina esse recurso como `false`.

**Currents**: `useUUIDAsDeviceId` definido como true significa que o ID do dispositivo enviado em Currents não será mais igual ao valor IDFV.

### Perguntas frequentes

#### Essa mudança afetará meus usuários existentes no Braze?

Não. Quando ativado, esse recurso não substituirá nenhum dado de usuário no Braze. Novos IDs de dispositivo UUID serão criados apenas para novos dispositivos ou quando `wipedata()` for chamado.

#### Posso desativar esse recurso depois de ativá-lo?

Sim, esse recurso pode ser ativado e desativado a seu critério. Os IDs de dispositivos armazenados anteriormente nunca serão substituídos.

#### Ainda posso capturar o valor do IDFV via Braze em outro lugar?

Sim, você ainda pode coletar opcionalmente o IDFV por meio do Swift SDK (a coleta está desativada por padrão). 
