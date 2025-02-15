---
nav_title: Android
article_title: notificações por push do Android para Unity
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "Este artigo de referência cobre a integração de notificação por push do Android para a plataforma Unity."

---

# Integração de notificação por push do Android

> Este artigo de referência cobre a integração de notificação por push do Android para a plataforma Unity.

Estas instruções são para integrar push com [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/).

Consulte nossa documentação do [Unity ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/) para obter instruções de integração do ADM.

## Etapa 1: ativar Firebase

Para começar, siga a documentação de configuração do [Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Integrar o Firebase Unity SDK pode fazer com que seu `AndroidManifest.xml` seja substituído. Se isso ocorrer, certifique-se de reverter para o original.
{% endalert %}

## Etapa 2: Defina suas credenciais do Firebase

Você precisa inserir sua chave de servidor do Firebase e o ID do remetente no dashboard da Braze. Para fazer isso, registre-se no [console de desenvolvedores do Firebase](https://console.firebase.google.com/) e selecione seu projeto Firebase. Em seguida, selecione **envio de mensagens na nuvem** em **Configurações** e copie a Chave do Servidor e o ID do Remetente:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

No Braze, selecione seu app Android na página de **Configurações do App** em **Gerenciar Configurações**. Em seguida, insira sua chave de servidor do Firebase no campo **Firebase Cloud Messaging Server Key** e o ID do remetente do Firebase no campo **Firebase Cloud Messaging Sender** ID.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## Etapa 3: Implementar integração automática de push

O SDK da Braze pode lidar automaticamente com o registro de push com os servidores do Firebase Cloud Messaging para que os dispositivos recebam notificações por push.

![O editor do Unity mostra as opções de configuração do Braze. Neste editor, a "Automate Unity Android Integration", "Push Notification Firebase Push", "Push Configuration Handle Push Deeplinks Automatically", "Push Configuration Push Notification HTML Rendering Enabled" e "Set Push Deleted/Opened/Received Listeners" estão configurados. Os campos "Firebase Sender ID", "Small/Large Icon Drawable", "Default Notification Accent Color" também são fornecidos.]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} "Android Push Settings")

- **Registro automático de envio de mensagens do Firebase ativado**<br> Instrui o Braze SDK a recuperar e enviar automaticamente um token por push FCM para um dispositivo. 
- **ID de remetente do Firebase Cloud Messaging**<br> O ID do remetente do seu console do Firebase.
- **Manipular deeplinks de push automaticamente**<br> Se o SDK deve lidar com a abertura de links profundos ou abrir o app quando notificações por push são clicadas.
- **Pequeno Ícone de Notificação Drawable**<br>O drawable deve ser exibido como o ícone pequeno sempre que uma notificação por push for recebida. A notificação usará o ícone do aplicativo como o ícone pequeno se nenhum ícone for fornecido.

## Etapa 4: Definir ouvintes de push

Se você deseja passar cargas úteis de notificação por push para o Unity ou tomar medidas adicionais quando um usuário recebe uma notificação por push, o Braze oferece a opção de configurar ouvintes de notificação por push.

No Braze, selecione seu app Android na página de **Configurações do App** em **Gerenciar Configurações**. Em seguida, insira sua chave de servidor do Firebase no campo **Configurações de notificação por push** e o ID do remetente do Firebase no campo de ID **Configurações de notificação por push**.

#### Ouvinte de push recebido

O ouvinte recebido de push é acionado quando um usuário recebe uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e envie o método de retorno de chamada do ouvinte recebido em **Set Push Received Listener**.

#### Ouvinte de push aberto

O ouvinte aberto de push é acionado quando um usuário lança o app clicando em uma notificação por push. Para enviar a carga útil push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push aberto em **Set Push Opened Listener**.

#### Push excluiu ouvinte (somente Android)

O ouvinte de exclusão de push é acionado quando um usuário desliza ou descarta uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push excluído em **Set Push Deleted Listener**.

#### Exemplo de implementação do ouvinte de push

O exemplo a seguir implementa o objeto de jogo `BrazeCallback` usando um método de retorno de chamada chamado `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` e `PushNotificationDeletedCallback` respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração do Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### Exemplo de implementação

O projeto de exemplo no [repositório do Braze Unity SDK](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples) contém um aplicativo de exemplo completo que inclui FCM.

## Deep linking para recursos in-app

Embora a Braze possa lidar com links profundos padrão (como URLs de sites, URIs do Android, etc.) por padrão, a criação de links profundos personalizados requer uma configuração adicional do Manifesto.

Para obter orientações de configuração, visite [Deep linking para recursos no aplicativo](https://developer.android.com/training/app-links/deep-linking).

## Adição de ícones de notificação por push do Braze

Para adicionar ícones push ao seu projeto, crie um plug-in do Android Archive (AAR) ou uma biblioteca do Android que contenha os arquivos de imagem do ícone. Para obter etapas e informações, consulte a documentação da Unity: [Projetos de biblioteca do Android e plug-ins do Android Archive](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).