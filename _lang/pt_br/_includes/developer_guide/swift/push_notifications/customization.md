{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Personalizando botões de ação {#push-action-buttons-integration}

O Braze Swift SDK fornece suporte ao manuseio de URL para botões de ação por push. Há quatro conjuntos de botões de ação por push padrão para as categorias de push padrão da Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, e `More`.

![Um GIF de uma mensagem push sendo puxada para baixo para exibir dois botões de ação personalizáveis.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Registrando botões de ação manualmente

{% alert important %}
Registrar botões de ação por push manualmente não é recomendado.
{% endalert %}

Se você [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) usando a opção de configuração `configuration.push.automation`, a Braze registra automaticamente os botões de ação para as categorias de push padrão e gerencia a análise de cliques dos botões de ação por push e o roteamento de URL.

No entanto, você pode optar por registrar botões de ação por push manualmente.

#### Etapa 1: Adição de categorias push padrão do Braze {#registering}

Use o seguinte código para se registrar nas categorias push padrão ao se [registrar no push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Clicar nos botões de ação por push com o modo de ativação em segundo plano apenas descartará a notificação e não abrirá o app. Na próxima vez que o usuário abrir o app, a análise de dados do clique do botão para essas ações será enviada para o servidor.
{% endalert %}

#### Etapa 2: Ativar o manuseio interativo de push {#enable-push-handling}

Para ativar a manipulação de nossos botões de ação por push, incluindo análise de dados de cliques e roteamento de URL, adicione o seguinte código ao método delegado `didReceive(_:completionHandler:)` do seu app:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Se você usar a estrutura `UNNotification` e tiver implementado os [métodos de notificação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) do Braze, já deverá ter esse método integrado. 

## Personalizando categorias de push {#customizing-push-categories}

Além de fornecer um conjunto de categorias de notificação por push padrão, o Braze oferece suporte a categorias e ações de notificação personalizadas. Depois de registrar as categorias no seu aplicativo, você pode usar o dashboard do Braze para enviar essas categorias de notificação personalizadas aos seus usuários.

Aqui está um exemplo que aproveita o endereço `LIKE_CATEGORY` exibido no dispositivo:

![Uma mensagem push exibindo dois botões de ação por push "unlike" e "like".]({% image_buster /assets/img_archive/push_example_category.png %})

### Etapa 1: Registre uma categoria

Para registrar uma categoria no seu app, use uma abordagem semelhante à seguinte:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Ao criar um `UNNotificationAction`, você pode especificar uma lista de opções de ação. Por exemplo, `.foreground` permite que seus usuários abram seu app após tocar no botão de ação. Isso é necessário para comportamentos de navegação ao clicar, como "Abrir app" e "Deep link com o app". Se você quiser um botão de ação que simplesmente descarte a notificação sem abrir o app, deixe `.foreground` fora do array `options` da ação. Para saber mais, consulte [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Etapa 2: Selecione suas categorias

Depois de registrar uma categoria, use o dashboard do Braze para enviar notificações desse tipo aos usuários.

{% alert tip %}
Você só precisa definir botões de ação no dashboard da Braze para comportamentos que não podem ser criados localmente no seu código Swift, como deep linking no seu app ou redirecionamento para uma URL da web. Essas ações precisam ser configuradas no dashboard para que possam definir qual URL ou deep link abrir. Para botões de ação que simplesmente descartam a notificação sem abrir o app, você não precisa configurá-los no dashboard—o comportamento de descarte é tratado automaticamente pelo iOS. Basta registrar sua categoria personalizada e suas ações no código do seu app, depois insira o nome da categoria correspondente no dashboard.
{% endalert %}

1. No dashboard do Braze, selecione **Envio de mensagens** > **Notificações por push** e, em seguida, escolha sua [campanha de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message) para iOS.
2. Em **Compose push notification (Notificação por push de composição**), ative **os botões de ação**.
3. No menu suspenso **Categoria de notificação do iOS**, selecione **Inserir categoria personalizada pré-registrada do iOS**.
4. Por fim, insira uma das categorias que você criou anteriormente. O exemplo a seguir usa a categoria personalizada: `LIKE_CATEGORY`.

![O dashboard da campanha de notificação por push com a configuração de categorias personalizadas.]({% image_buster /assets/img_archive/ios-notification-category.png %})

### Exemplo: Categoria de push personalizada {#example-custom-push-category}

Suponha que você queira criar uma notificação por push com dois botões de ação: **Gerenciar**, que faz deep link no seu app, e **Manter**, que simplesmente descarta a notificação.

No exemplo a seguir, a ação `MANAGE_IDENTIFIER` inclui a opção `.foreground`, que abre o app quando tocada—isso é necessário porque fará deep link em uma parte específica do app. A ação `KEEP_IDENTIFIER` usa um array de opções vazio, o que significa que descartará a notificação sem abrir o app.

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% endtabs %}

Como `MANAGE_IDENTIFIER` faz deep link no app, você deve configurar esse botão de ação no dashboard da Braze com a URL de deep link associada. No entanto, você não precisa definir um botão no dashboard para `KEEP_IDENTIFIER` porque ele apenas descarta a notificação. No dashboard, você só precisa inserir o nome da categoria (por exemplo, `YOUR_CATEGORY`) para corresponder ao que você registrou no código do seu app.

## Personalizando distintivos

Os emblemas são ícones pequenos, ideais para chamar a atenção do usuário. Você pode especificar uma contagem de distintivos na guia [**Configurações**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) quando compuser uma notificação por push usando o dashboard do Braze. Você também pode atualizar a contagem de emblemas manualmente por meio da propriedade [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) do aplicativo ou da [carga útil da notificação remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

O Braze limpará automaticamente a contagem de emblemas quando uma notificação do Braze for recebida enquanto o app estiver em primeiro plano. A configuração manual do número do crachá como 0 também limpará as notificações na central de notificações. 

Se você não tiver um plano para limpar os crachás como parte da operação normal do aplicativo ou enviando pushs que limpem o crachá, deverá limpar o crachá quando o aplicativo se tornar ativo, adicionando o seguinte código ao método delegado `applicationDidBecomeActive:` do seu aplicativo:

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Personalizando sons

### Etapa 1: Hospede o som no seu app

Os sons de notificação por push personalizados devem ser hospedados localmente no pacote principal de seu app. São aceitos os seguintes formatos de dados de áudio:

- PCM linear
- MA4
- µLaw
- aLaw

É possível empacotar os dados de áudio em um arquivo AIFF, WAV ou CAF. No Xcode, adicione o arquivo de som ao seu projeto como um recurso não localizado do pacote de aplicativos.

{% alert note %}
Os sons personalizados devem ter menos de 30 segundos quando reproduzidos. Se um som personalizado estiver acima desse limite, o som padrão do sistema será reproduzido.
{% endalert %}

#### Conversão de arquivos de som

Você pode usar a ferramenta afconvert para converter sons. Por exemplo, para converter o som do sistema PCM linear de 16 bits Submarine.aiff para áudio IMA4 em um arquivo CAF, use o seguinte comando no terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Você pode inspecionar um som para determinar seu formato de dados abrindo-o no QuickTime Player e escolhendo **Mostrar Inspetor de Filme** no menu **Filme**.
{% endalert %}

### Etapa 2: Forneça uma URL de protocolo para o som

Você deve especificar um URL de protocolo que direcione para o local do arquivo de som em seu app. Há dois métodos para fazer isso:

* Use o parâmetro `sound` do [objeto Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) para passar o URL para o Braze.
* Especifique o URL no dashboard. No [criador do push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), selecione **Configurações** e insira o URL do protocolo no campo **Som**. 

![O criador do push no dashboard da Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Se o arquivo de som especificado não existir ou se a palavra-chave “default” for inserida, a Braze usará o som de alerta padrão do dispositivo. Além do nosso dashboard, o som também pode ser configurado através da nossa [API de envio de mensagens][12].

Consulte a documentação para desenvolvedores da Apple sobre a [preparação de sons de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obter informações adicionais.

## Configurações

Ao criar uma campanha push por meio do dashboard, clique na guia **Settings (Configurações)** na etapa **Compose (Redigir** ) para visualizar as configurações avançadas disponíveis.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Pares de valores chave

A Braze permite que você envie pares de chave/valor de string personalizados, conhecidos como `extras`, juntamente com uma notificação por push para o seu app. Os extras podem ser definidos por meio do dashboard ou da API e estarão disponíveis como pares de valores-chave no dicionário `notification` passado para suas implementações de delegados push.

### Opções de alerta

Marque a caixa de seleção **Opções de alerta** para ver um menu suspenso de valores-chave disponíveis para ajustar como a notificação aparece nos dispositivos.

### Adição do sinalizador content-available

Marque a caixa de seleção **Adicionar sinalizador de conteúdo disponível** para instruir os dispositivos a baixar novos conteúdos em segundo plano. Geralmente, isso pode ser verificado se você estiver interessado em enviar [notificações silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Adição do sinalizador de conteúdo mutável

Marque a caixa de seleção **Add Mutable-Content Flag (Adicionar sinalizador de conteúdo mutável** ) para ativar a capacitação avançada do receptor. Esse sinalizador será enviado automaticamente ao criar uma [notificação Rich]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), independentemente do valor dessa caixa de seleção.

### ID de recolhimento

Especifique uma ID de recolhimento para agrupar notificações semelhantes. Se você enviar várias notificações com a mesma ID de colapso, o dispositivo mostrará apenas a notificação recebida mais recentemente. Consulte a documentação da Apple sobre [notificações agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Expiração

Ao marcar a caixa de seleção **Vencimento**, você poderá definir um tempo de expiração para sua mensagem. Se o dispositivo de um usuário perder a conectividade, o Braze continuará a tentar enviar a mensagem até o horário especificado. Se isso não for definido, a plataforma terá como padrão uma expiração de 30 dias. Observe que as notificações por push que expiram antes da entrega não são consideradas falhas e não serão registradas como bounce.
