---
nav_title: Botões de ação
article_title: Botões de ação por push para iOS
platform: Swift
page_order: 1
description: "Este artigo aborda como implementar botões de ação em suas notificações por push do iOS para o Swift SDK."
channel:
  - push

---

# Botões de ação {#push-action-buttons-integration}

> O Braze Swift SDK fornece suporte ao manuseio de URL para botões de ação por push. 

Há quatro conjuntos de botões de ação por push padrão para as categorias de push padrão da Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, e `More`. 

![Um GIF de uma mensagem push sendo puxada para baixo para exibir dois botões de ação personalizáveis.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

Se você quiser criar suas próprias categorias de notificação personalizadas, consulte [personalização do botão de ação](#push-category-customization).

## Integração automática (recomendado)

Ao integrar o push usando a opção de configuração `configuration.push.automation`, o Braze registra automaticamente os botões de ação por push para as categorias de push padrão e lida com a análise de dados de cliques dos botões de ação por push e com o roteamento de URL.

## Integração manual

Para ativar manualmente esses botões de ação por push, primeiro registre-se para as categorias push padrão. Em seguida, use o método delegado `didReceive(_:completionHandler:)` para ativar os botões de ação por push.

### Etapa 1: Adição de categorias push padrão do Braze {#registering}

Use o seguinte código para se registrar nas categorias push padrão ao se [registrar no push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Clicar nos botões de ação por push com o modo de ativação em segundo plano apenas descartará a notificação e não abrirá o app. Na próxima vez que o usuário abrir o app, a análise de dados do clique do botão para essas ações será enviada para o servidor.
{% endalert %}

### Etapa 2: Ativar o manuseio interativo de push {#enable-push-handling}

Para ativar a manipulação de nossos botões de ação por push, incluindo análise de dados de cliques e roteamento de URL, adicione o seguinte código ao método delegado `didReceive(_:completionHandler:)` do seu app:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Se você usar a estrutura `UNNotification` e tiver implementado os [métodos de notificação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) do Braze, já deverá ter esse método integrado. 

## Personalização da categoria push

Além de fornecer um conjunto de categorias de notificação por push padrão, o Braze oferece suporte a categorias e ações de notificação personalizadas. Depois de registrar as categorias no seu aplicativo, você pode usar o dashboard do Braze para enviar essas categorias de notificação personalizadas aos seus usuários.

Essas categorias podem ser atribuídas a notificações por push por meio de nosso dashboard para disparar as configurações do botão de ação de seu design. 

### Exemplo de categoria de push personalizado

Aqui está um exemplo que aproveita o endereço `LIKE_CATEGORY` exibido no dispositivo:

![Uma mensagem push exibindo dois botões de ação por push "unlike" e "like".]({% image_buster /assets/img_archive/push_example_category.png %})

#### Etapa 1: Registre uma categoria

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
{% tab OBJECTIVE C %}

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
Ao criar um `UNNotificationAction`, você pode especificar uma lista de opções de ação. Por exemplo, `UNNotificationActionOptions.foreground` permite que os usuários abram o app depois de tocar no botão de ação. Isso é necessário para comportamentos de navegação ao clicar, como "Abrir app" e "Deep link com o app". Para saber mais, consulte [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

#### Etapa 2: Selecione suas categorias

Depois de registrar uma categoria, use o dashboard do Braze para enviar notificações desse tipo aos usuários.

{% alert tip %}
Só é necessário definir categorias de notificação personalizadas para botões de ação com _ações especiais_, como deep links em seu app ou abertura de URL. Não é necessário defini-las para botões de ação que apenas descartam uma notificação.
{% endalert %}

1. No dashboard do Braze, selecione **Envio de mensagens** > **Notificações por push** e, em seguida, escolha sua [campanha de push]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message) para iOS.
2. Em **Compose push notification (Notificação por push de composição**), ative **os botões de ação**.
3. No menu suspenso **Categoria de notificação do iOS**, selecione **Inserir categoria personalizada pré-registrada do iOS**.
4. Por fim, insira uma das categorias que você criou anteriormente. O exemplo a seguir usa a categoria personalizada: `LIKE_CATEGORY`.

![O dashboard da campanha de notificação por push com a configuração de categorias personalizadas.]({% image_buster /assets/img_archive/ios-notification-category.png %})

