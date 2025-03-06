---
nav_title: Botões de ação
article_title: Botões de ação por push para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência aborda como implementar botões de ação em suas notificações por push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Botões de ação {#push-action-buttons-integration}

O Braze iOS SDK aceita categorias de push padrão, incluindo suporte de manuseio de URL para cada botão de ação por push. Atualmente, as categorias padrão têm quatro conjuntos de botões de ação por push: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel` e `More`. 

![Um GIF de uma mensagem push sendo puxada para baixo para exibir dois botões de ação personalizáveis.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Para registrar nossas categorias de push padrão, siga as instruções de integração:

## Etapa 1: Adicionando categorias de push padrão do Braze

Use o código a seguir para se registrar em nossas categorias push padrão ao se [registrar no push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab swift %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Clicar nos botões de ação por push com o modo de ativação em segundo plano apenas descartará a notificação e não abrirá o app. Na próxima vez que o usuário abrir o app, a análise de dados do clique do botão para essas ações será enviada para o servidor.

Se você quiser criar suas próprias categorias de notificação personalizadas, consulte [personalização do botão de ação]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization).

## Etapa 2: Ativar o manuseio interativo de push

Se você usa a estrutura `UNNotification` e implementou [delegados]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) do Braze, já deve ter esse método integrado. 

Para ativar a manipulação de nossos botões de ação por push, incluindo análise de dados de cliques e roteamento de URL, adicione o seguinte código ao método delegado `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` do seu app:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Se você não estiver usando o UNNotification Framework, precisará adicionar o seguinte código ao `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` do seu app para ativar o manuseio do nosso botão de ação por push:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Recomendamos fortemente que as pessoas que usam `handleActionWithIdentifier` comecem a usar o framework `UNNotification`. Recomendamos isso devido à descontinuação de [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Personalização da categoria push

Além de fornecer um conjunto de [categorias de notificação por push padrão]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), o Braze oferece suporte a categorias e ações de notificação personalizadas. Depois de registrar categorias em seu aplicativo, você pode usar o dashboard da Braze para enviar categorias de notificação aos seus usuários.

Se não estiver usando a estrutura `UserNotifications`, consulte a documentação sobre [categorias alternativas](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Essas categorias podem ser atribuídas a notificações por push por meio de nosso dashboard para disparar as configurações do botão de ação de seu design. Aqui está um exemplo que aproveita o endereço `LIKE_CATEGORY` exibido no dispositivo:

![Uma mensagem push exibindo dois botões de ação por push "unlike" e "like".]({% image_buster /assets/img_archive/push_example_category.png %})


