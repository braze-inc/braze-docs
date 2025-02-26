---
nav_title: Notificações Rich
article_title: Notificações por push avançadas para iOS
platform: Swift
page_order: 5
description: "Este artigo aborda a implementação de notificações por push avançadas do iOS para o Swift SDK."
channel:
  - push

---

# Notificações Rich

> As notificações Rich são notificações por push com imagens, GIFs e vídeos. Para habilitar essa funcionalidade, você deve criar uma extensão de serviço de notificação - um tipo de extensão que ativa a modificação de uma carga útil por push antes que ela seja exibida. Consulte o site da Apple [`UNNotificationAttachment`](https://developer.apple.com/reference/usernotifications/unnotificationattachment) da Apple para obter uma lista dos tipos e tamanhos de arquivos compatíveis.

## Etapa 1: Criação de uma extensão de serviço

Para criar uma [extensão de serviço de notificação](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), navegue até **File > New > Target** no Xcode e selecione **Notification Service Extension**.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Certifique-se de que **Embed In Application** esteja definido para incorporar a extensão em seu aplicativo.

## Etapa 2: Configuração da extensão do serviço de notificação

Uma extensão de serviço de notificação é seu próprio binário, que é empacotado com seu app. Ele deve ser configurado no [Portal Apple Developer](https://developer.apple.com) com seu próprio ID de app e perfil de provisionamento.

A ID do pacote da extensão do serviço de notificação deve ser diferente da ID do pacote do direcionamento do seu aplicativo principal. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá usar `com.company.appname.AppNameServiceExtension` para a extensão do serviço.

## Etapa 3: Integração de notificações por push avançadas

Para obter um guia passo a passo sobre a integração de notificações por push com `BrazeNotificationService`, consulte nosso [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver um exemplo, consulte o uso em [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) do nosso app Examples.

### Adição da estrutura rich push ao seu aplicativo

{% tabs localização %}
{% tab Swift Package Manager %}

Depois de seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/), adicione `BrazeNotificationService` ao seu site `Notification Service Extension` fazendo o seguinte:

1. No Xcode, em frameworks e bibliotecas, selecione o ícone <i class="fas fa-plus"></i> de adicionar para adicionar um framework. <br><br>![O ícone de adicionar está localizado em estruturas e bibliotecas no Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Selecione a estrutura "BrazeNotificationService". <br><br>![A estrutura "BrazeNotificationService" pode ser selecionada no modal que se abre.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Adicione o seguinte ao seu Podfile:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```
{% alert note %}
Para obter instruções sobre como implementar stories por push, consulte a [documentação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Depois de atualizar o Podfile, navegue até o diretório de seu projeto de app do Xcode em seu terminal e execute `pod install`.

{% endtab %}

{% tab Manual %}

Para adicionar `BrazeNotificationService.xcframework` ao seu `Notification Service Extension`, consulte [Integração manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/).

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Uso de sua própria extensão UNNotificationServiceExtension
Se você precisar usar seu próprio UNNotificationServiceExtension, poderá chamar [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) em seu método `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

## Etapa 4: Criação de uma notificação Rich em seu dashboard

Sua equipe de marketing também pode criar notificações Rich a partir do dashboard. Crie uma notificação por push por meio do criador de push e simplesmente anexe uma imagem ou GIF, ou forneça um URL que hospede uma imagem, GIF ou vídeo. Note que os ativos são baixados no recebimento de notificações por push, portanto, planeje-se para grandes picos síncronos de solicitações se estiver hospedando seu conteúdo.

