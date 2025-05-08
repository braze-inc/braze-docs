---
nav_title: Stories por push
article_title: Push Stories para iOS
platform: iOS
page_order: 27
description: "Este artigo de referência mostra como configurar o Push Stories para seu aplicativo iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuração do story por push

O recurso Push Story requer o framework `UNNotification` e o iOS 10. O recurso só está disponível a partir da versão 3.2.1 do SDK do iOS.

## Etapa 1: Ative o push em seu aplicativo

Siga a [integração de notificações por push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) para ativar o push em seu app.

## Etapa 2: Adição do direcionamento da extensão de conteúdo de notificação

Em seu projeto de app, acesse o menu **File > New > Target...** (Arquivo > Novo > Direcionamento...) e adicione um novo direcionamento `Notification Content Extension` e ative-o.

![]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

O Xcode deve gerar um novo alvo e criar arquivos automaticamente para você, incluindo:

{% tabs %}
{% tab OBJECTIVE C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Etapa 3: Ativar recursos

O recurso Push Story requer o modo em segundo plano na seção **Recursos** do direcionamento do aplicativo principal. Depois de ativar os modos em segundo plano, selecione **Background fetch** (Recuperação em segundo plano) e **Remote notifications** (Notificações remotas).

![]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Adicionando um grupo de app

Você também precisa adicionar `Capability App Groups`. Se você não tiver nenhum grupo de app em seu aplicativo, acesse o **recurso** do direcionamento do aplicativo principal, ative o `App Groups` e clique no botão **+**. Use o ID do pacote de seu aplicativo para criar o grupo de app. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá nomear o grupo do app como `group.com.company.appname.xyz`. Você precisa ativar o `App Groups` para os destinos do app principal e da extensão de conteúdo.

{% alert important %}
`App Groups` neste contexto, refere-se ao [direito de grupos de aplicativos](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) da Apple e não à sua ID do espaço de trabalho Braze (anteriormente grupo de app).
{% endalert %}

Se você não adicionar seu app a um grupo de apps, seu aplicativo poderá não preencher determinados campos da carga útil do push e não funcionará totalmente como esperado.

## Etapa 4: Adição do framework Push Story ao seu app

{% tabs local %}
{% tab Swift Package Manager %}

Depois de seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/), adicione `AppboyPushStory` a `Notification Content Extension`:

![No Xcode, em Framework e Library, selecione o ícone "+" para adicionar um framework.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Adicione a seguinte linha ao seu Podfile:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Depois de atualizar o Podfile, navegue até o diretório do seu projeto de app do Xcode no terminal e execute `pod install`.

{% endtab %}
{% tab Manual %}

Baixe a versão mais recente do `AppboyPushStory.zip` na [página de lançamento do GitHub](https://github.com/Appboy/appboy-ios-sdk/releases), extraia-a e adicione os seguintes arquivos ao `Notification Content Extension` do seu projeto:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Certifique-se de que **Não Incorporar** esteja selecionado para **AppboyPushStory.xcframework** na coluna **Incorporar**.
{% endalert %}

Adicione o sinalizador `-ObjC` ao `Notification Content Extension` do seu projeto em **Build Settings > Other Linker Flags **.

{% endtab %}
{% endtabs %}

## Etapa 5: Atualização do Notification View Controller

{% tabs %}
{% tab OBJECTIVO-C %}

Em seu site `NotificationViewController.h`, adicione as seguintes linhas para adicionar novas propriedades e importar os arquivos de cabeçalho:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

Em `NotificationViewController.m`, remova a implementação padrão e adicione o seguinte código:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

Em `NotificationViewController.swift`, adicione a seguinte linha para importar os arquivos de cabeçalho:

```swift
import AppboyPushStory
```

Em seguida, remova a implementação padrão e adicione o seguinte código:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?
    
  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }
    
  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }
    
  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Etapa 6: Definir o storyboard da extensão do conteúdo da notificação

Abra o storyboard `Notification Content Extension` e coloque um novo `UIView` no notification view controller. Renomeie a classe para `ABKStoriesView`. Faça com que a largura e a altura da exibição sejam redimensionáveis automaticamente, de acordo com o quadro de exibição principal do controlador de exibição de notificação.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

Em seguida, vincule o IBOutlet `storiesView` do notification view controller ao `ABKStoriesView` adicionado.

![]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Etapa 7: Definir o plist de extensão do conteúdo da notificação

Abra o arquivo `Info.plist` do `Notification Content Extension` e adicione e altere as seguintes chaves em `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` ( tipo`String` )
`UNNotificationExtensionDefaultContentHidden` = `YES` ( tipo`Boolean` )
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` ( tipo`Number` )

![]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Etapa 8: Atualização da integração do Braze em seu app principal

##### Opção 1: Tempo de execução

No dicionário `appboyOptions` usado para configurar sua instância da Braze, adicione uma entrada `ABKPushStoryAppGroupKey` e defina o valor como seu identificador de API do espaço de trabalho.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

##### Opção 2: Info.plist

Como alternativa, para configurar o espaço de trabalho do Story por push a partir do arquivo `Info.plist`, adicione um dicionário chamado `Braze` ao arquivo `Info.plist`. No dicionário `Braze`, adicione uma subentrada `PushStoryAppGroup` do tipo string e defina o valor como seu identificador de espaço de trabalho. Observe que antes do Braze iOS SDK v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.

## Próximas etapas

Em seguida, consulte as etapas para integrar [os botões de ação]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), o que é necessário para que os botões sejam exibidos em uma mensagem de story por push.


