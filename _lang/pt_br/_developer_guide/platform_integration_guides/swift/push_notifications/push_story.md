---
nav_title: Stories por push
article_title: Integrando push Stories para iOS
platform: Swift
page_order: 27
description: "Este artigo mostra como configurar Histórias Push do iOS para o SDK SWIFT."
channel:
  - push

---

# Stories por push

> As [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/) permitem que os profissionais de marketing usem a funcionalidade de carrossel de fotos para criar uma sequência de páginas em uma notificação por push. Estas páginas consistem em uma imagem, ação de clique, título e descrição. 

Configurar Push Stories para o seu app iOS requer etapas adicionais além de integrar notificações por push padrão, que estão descritas neste artigo.

## Pré-requisitos

As seguintes versões do SDK são necessárias para receber Push Stories:

{% sdk_min_versions swift:5.0.0 %}

Certifique-se de que você seguiu o [tutorial de integração de notificação por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) para ativar push no seu app. Como parte desta tarefa, você deve ter implementado a estrutura `UNNotification`, que é necessária para este recurso.

## Etapa 1: Adicionando o alvo de Extensão de Conteúdo de Notificação {#notification-content-extension}

No seu projeto de app, Acessar o menu **Arquivo > Novo > Alvo** e adicionar um novo `Notification Content Extension` alvo e ativá-lo.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

O Xcode deve gerar um novo alvo e criar arquivos automaticamente para você, incluindo:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

## Etapa 2: Ativar capacidades {#enable-capabilities}

No Xcode, adicione a capacidade de Modos de Fundo usando o painel **Assinatura e Capacidades** ao alvo principal do app. Selecione as caixas de seleção **Busca em segundo plano** e **Notificações remotas**.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

### Adicionando um grupo de app

Além disso, no painel **Assinatura e Capacidades** no Xcode, adicione a capacidade Grupos de app ao seu alvo principal do app, bem como aos alvos da Extensão de Conteúdo de Notificação. Em seguida, clique no botão **+**. Use o ID do pacote do seu app para criar o grupo de app. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você pode nomear seu grupo de app `group.com.company.appname.xyz`.

{% alert important %}
Grupos de app neste contexto referem-se à [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) da Apple e não ao seu ID de espaço de trabalho Braze (anteriormente grupo de app).
{% endalert %}

Se você não adicionar seu app a um grupo de app, seu app pode falhar em preencher certos campos da carga útil do push e não funcionará totalmente como esperado.

## Etapa 3: Adicionando o framework de story por push ao seu app {#enable-capabilities}

{% tabs localização %}
{% tab Swift Package Manager %}

Depois de seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/), adicione `BrazePushStory` a `Notification Content Extension`:

![No Xcode, em Framework e Library, selecione o ícone "+" para adicionar um framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Adicione a seguinte linha ao seu Podfile:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```
{% alert note %}
Para obter instruções sobre como implementar o Rich push, consulte [Notificações Rich]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

Depois de atualizar o Podfile, navegue até o diretório de seu projeto de app do Xcode em seu terminal e execute `pod install`.

{% endtab %}
{% tab Manual %}

Baixe o último `BrazePushStory.zip` da [página de lançamentos do GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), extraia-o e adicione o `BrazePushStory.xcframework` ao `Notification Content Extension` do seu projeto.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Certifique-se de que **Não Incorporar** esteja selecionado para **BrazePushStory.xcframework** na coluna **Incorporar**.
{% endalert %}

{% endtab %}
{% endtabs %}

## Etapa 4: Atualizando seu controlador de visualização de notificações {#enable-capabilities}

Em `NotificationViewController.swift`, adicione a seguinte linha para importar os arquivos de cabeçalho:

```swift
import BrazePushStory
```

Em seguida, substitua a implementação padrão herdando [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Eventos de story por push de manipulação personalizada
Se você quiser implementar sua própria lógica personalizada para lidar com eventos de notificação de story por push, herde `BrazePushStory.NotificationViewController` como acima e substitua os métodos [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) como abaixo.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

## Etapa 5: Definindo a extensão de conteúdo de notificação plist {#notification-content-extension}

Abra o `Info.plist` arquivo do `Notification Content Extension`, depois adicione e altere as seguintes chaves em `NSExtension \ NSExtensionAttributes`:

| Chave                                              | Tipo    | Valor                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | String  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Booleano | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Número  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Booleano | `YES`                  |

Seu `Info.plist` arquivo deve corresponder à seguinte imagem:

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

## Etapa 6: Atualizando a integração da Braze no seu app principal {#update-braze}

Antes de inicializar o Braze, atribua o nome do seu grupo de app à propriedade [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) da configuração do Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

