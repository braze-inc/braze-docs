---
nav_title: Disparo Personalizado
article_title: Personalizando o acionamento de mensagem no app para iOS
platform: Swift
page_order: 6
description: "Este artigo de referência cobre o acionamento de envio de mensagens no app iOS personalizado para o SDK SWIFT."
channel:
  - in-app messages
---

# Disparo personalizado

> Por padrão, mensagens no app são acionadas por eventos registrados pelo SDK. Como alternativa, você pode disparar mensagens no app por eventos enviados pelo servidor.

Para disparar mensagens no app usando eventos do lado do servidor, envie um push silencioso para o dispositivo para permitir que ele registre um evento baseado no SDK. Este evento do SDK pode, posteriormente, disparar a mensagem no app voltada para o usuário.

## Etapa 1: Lidar com push silencioso e pares chave-valor

Implemente a seguinte função e chame-a dentro do [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: método](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Quando o push silencioso é recebido, um evento registrado pelo SDK "disparar mensagem no app" será registrado no perfil do usuário. 

{% alert important %}
Devido a uma mensagem por push ser usada para registrar um evento personalizado registrado pelo SDK, a Braze precisará armazenar um token por push para cada usuário para ativar essa solução. Para usuários de iOS, a Braze só armazenará um token a partir do momento em que o usuário receber o prompt de push do sistema operacional. Antes disso, o usuário não estará acessível usando push, e a solução anterior não será possível.
{% endalert %}

## Etapa 2: Crie uma campanha de push silenciosa

Crie uma [campanha de push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/), que é disparada pelo evento enviado pelo servidor. 

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários cujos perfis de usuário tenham o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que esta campanha de push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app.

![Uma campanha de mensagem no app de entrega baseada em ação que possui dois pares chave-valor. "CAMPAIGN_NAME" definido como "Exemplo de nome de mensagem no app" e "IS_SERVER_EVENT" definido como "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro do par chave-valor extras da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

## Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagens no app com entrega baseada em ação que será entregue aos usuários que executarem o evento personalizado "Disparo de mensagem no app", em que "campaign_name" é igual a "Exemplo de nome de campanha do IAM".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.
{% endalert %}

