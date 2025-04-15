---
nav_title: iOS
article_title: Notificações por push para Unity
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "Este artigo de referência aborda a integração de notificações por push do iOS para a plataforma Unity."

---

# Integração de notificações por push do iOS

> Este artigo de referência aborda a integração de notificações por push do iOS para a plataforma Unity.

## Etapa 1: Escolha a integração push automática ou manual

A Braze fornece uma solução Unity nativa para automatizar as integrações push do iOS.

- Se preferir concluir a integração manualmente, modificando seu projeto Xcode construído, siga nossas [instruções nativas de push do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
- Se estiver fazendo a transição de uma integração manual para uma automatizada, siga as instruções em [Transição para uma integração automatizada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios).
- Nossa solução de notificação por push automática aproveita o recurso de autorização provisória do iOS 12 e não está disponível para uso com o pop-up nativo de prompt por push.

## Etapa 2: Implementar a integração automática de push

### Configurar notificações por push

Siga nossa [documentação de configuração de notificações por push do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) para configurar o Braze usando um arquivo `.p8`.

### Ativar a integração automática por push

Abra as definições de configuração da Braze no Unity Editor navegando até **Braze > Configurações**.

Marque **Integrar Push com o Braze** para registrar automaticamente os usuários para notificações por push, passar tokens por push para o Braze, rastrear análises de dados para aberturas de push e aproveitar nosso tratamento padrão de notificações por push.

### Ativar o push em segundo plano (opcional)

Marque **Ativar push em segundo plano** se quiser ativar o `background mode` para notificações por push. Isso permite que o sistema desperte seu aplicativo do estado `suspended` quando chegar uma notificação por push, ativando seu aplicativo para baixar conteúdo em resposta às notificações por push. É necessário marcar essa opção para nossa funcionalidade de rastreamento de desinstalação.

![O editor do Unity mostra as opções de configuração do Braze. Nesse editor, as opções "Automate Unity iOS integration", "Integrate push with braze" e "Enable background push" estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### Desativar o registro automático (opcional)

Os usuários que ainda não tiverem aceitado as notificações por push serão automaticamente autorizados a receber push ao abrir o aplicativo. Para desativar esse recurso e registrar manualmente os usuários para push, marque **Disable Automatic Push Registration (Desativar registro automático de push**).

- Se **a opção Disable Provisional Authorization (Desativar autorização provisória**) não estiver marcada no iOS 12 ou posterior, o usuário será autorizado provisoriamente (silenciosamente) a receber o quiet push. Se estiver marcada essa opção, o usuário verá o prompt push nativo.
- Se precisar configurar exatamente quando o prompt é mostrado em tempo de execução, desative o registro automático no editor de configuração do Braze e use `AppboyBinding.PromptUserForPushPermissions()`.

![O editor do Unity mostra as opções de configuração do Braze. Nesse editor, as capacitações "Automate Unity iOS integration", "integrate push with braze" e "disable automatic push registration" estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## Etapa 3: Definir ouvintes de push

Se quiser passar cargas úteis de notificação por push para o Unity ou realizar etapas adicionais quando um usuário receber uma notificação por push, o Braze oferece a opção de configurar ouvintes de notificação por push.

### Ouvinte de push recebido

O ouvinte de recebimento de push é acionado quando um usuário recebe uma notificação por push enquanto usa ativamente o aplicativo (por exemplo, quando o app está em primeiro plano). Defina o listener de recebimento de push no editor de configuração do Braze. Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_RECEIVED`.

![O editor do Unity mostra as opções de configuração do Braze. Nesse editor, a opção "Set Push Received Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationReceivedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### Ouvinte de push aberto

O listener aberto por push é acionado quando um usuário inicia o app clicando em uma notificação por push. Para enviar a carga útil push para o Unity, defina o nome de seu objeto de jogo e o método de retorno de chamada do ouvinte de abertura de push na opção **Set Push Opened Listener**:

![O editor do Unity mostra as opções de configuração do Braze. Nesse editor, a opção "Set Push Received Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationOpenedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_OPENED`.

### Exemplo de implementação do ouvinte push

O exemplo a seguir implementa o objeto de jogo `AppboyCallback` usando um nome de método de retorno de chamada `PushNotificationReceivedCallback` e `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração do Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```

## Recursos avançados

### Retorno de chamada do token por push

Para receber uma cópia dos tokens de dispositivos Braze do sistema operacional, defina um delegate usando `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.

### Outros recursos

Para implementar recursos avançados, como deep linking, contagem de ícones e sons personalizados, visite nossas [instruções de push nativo do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).

