---
nav_title: Disparo Personalizado
article_title: Personalizando o acionamento de mensagem no app para iOS
platform: iOS
page_order: 7
description: "Este artigo de referência cobre o acionamento de envio de mensagens personalizadas no app para seu aplicativo iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Disparo de mensagem personalizada no app

Por padrão, mensagens no app são acionadas por tipos de eventos registrados pelo SDK. Se você quiser disparar mensagens no app por eventos enviados pelo servidor, também é possível.

Para ativar esse recurso, você enviaria um push silencioso para o dispositivo, o que permite que o dispositivo registre um evento baseado em SDK. Este evento do SDK, por sua vez, dispararia a mensagem no app voltada para o usuário.

## Etapa 1: Lidar com push silencioso e pares chave-valor

Adicione o seguinte código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Quando o push silencioso é recebido, um evento registrado pelo SDK "disparar mensagem no app" será registrado no perfil do usuário. Note que essas mensagens no app só serão disparadas se o push silencioso for recebido enquanto o aplicativo estiver em primeiro plano.

## Etapa 2: Criar uma campanha push

Crie uma campanha de push silenciosa que é acionada via o evento enviado pelo servidor. Para saber como criar uma campanha de push silenciosa, consulte [notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/).

![Uma mensagem no app de entrega baseada em ação que será enviada para usuários que realizam o evento personalizado "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

A campanha de push precisa incluir extras de pares chave-valor, que indicam que esta campanha de push é enviada para registrar um evento personalizado do SDK. Este evento será usado para disparar a mensagem no app:

![n entrega baseada em ação campanha de mensagem no app que tem dois pares chave-valor. "NOME_DA_CAMPANHA" definido como "mensagem no app exemplo", e "É_EVENTO_DE_SERVIDOR" definido como "verdadeiro".]({% image_buster /assets/img_archive/iOSServerPush.png %})

O código dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` verifica a chave `IS_SERVER_EVENT` e registra um evento personalizado do SDK se estiver presente.

Você pode alterar o nome do evento ou as propriedades do evento enviando o valor desejado dentro do par chave-valor extras da carga útil push. Ao registrar o evento personalizado, esses extras podem ser usados como parâmetro do nome do evento ou como uma propriedade do evento.

## Etapa 3: Crie uma campanha de mensagem no app

Crie sua campanha de mensagem no app visível para o usuário no dashboard da Braze. Esta campanha deve ter uma entrega baseada em ação e ser acionada a partir do evento personalizado registrado dentro do método `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

No exemplo a seguir, a mensagem no app específica a ser acionada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campanha de mensagem no app baseada em ação que será entregue aos usuários que realizarem o evento personalizado "disparar mensagem no app" onde "campaign_name" é igual a "exemplo de nome de mensagem no app".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

Devido a uma push message ser usada para registrar um evento personalizado registrado pelo SDK, a Braze precisará armazenar um token por push para cada usuário para ativar essa solução. Para iOS e Android, a Braze só armazenará um token a partir do momento em que um usuário tiver recebido o prompt de push do sistema operacional. Antes disso, o usuário não estará acessível usando push, e a solução anterior não será possível.

