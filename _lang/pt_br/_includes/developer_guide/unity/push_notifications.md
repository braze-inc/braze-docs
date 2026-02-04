{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuração da notificação por push

### Etapa 1: Configurar a plataforma

{% tabs %}
{% tab Android %}
#### Etapa 1.1: ativar Firebase

Para começar, siga a documentação de configuração do [Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Integrar o Firebase Unity SDK pode fazer com que seu `AndroidManifest.xml` seja substituído. Se isso ocorrer, certifique-se de reverter para o original.
{% endalert %}

#### Etapa 1.2: Defina suas credenciais do Firebase

Você precisa inserir sua chave de servidor do Firebase e o ID do remetente no dashboard da Braze. Para fazer isso, registre-se no [console de desenvolvedores do Firebase](https://console.firebase.google.com/) e selecione seu projeto Firebase. Em seguida, selecione **envio de mensagens na nuvem** em **Configurações** e copie a Chave do Servidor e o ID do Remetente:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

No Braze, selecione seu app Android na página de **Configurações do App** em **Gerenciar Configurações**. Em seguida, insira sua chave de servidor do Firebase no campo **Firebase Cloud Messaging Server Key** e o ID do remetente do Firebase no campo **Firebase Cloud Messaging Sender** ID.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Etapa 1.1: Verificar o método de integração

A Braze fornece uma solução Unity nativa para automatizar as integrações push do iOS. Se, em vez disso, você quiser configurar e gerenciar sua integração manualmente, consulte [Swift: Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Caso contrário, continue para a próxima etapa.

{% alert note %}
Nossa solução de notificação por push automática aproveita o recurso de autorização provisória do iOS 12 e não está disponível para uso com o pop-up nativo de prompt por push.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Etapa 1.1: Ativar ADM

1. Crie uma conta no [Amazon Apps & Portal do desenvolvedor de jogos](https://developer.amazon.com/public), caso ainda não tenha feito isso.
2. Obtenha [as credenciais do OAuth (ID do cliente e segredo do cliente) e uma chave de API do ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Ative o **registro automático de ADM** na janela de configuração do Unity Braze. 
  - Como alternativa, é possível adicionar a seguinte linha ao arquivo `res/values/braze.xml` para ativar o registro do ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Etapa 2: Configurar notificações por push

{% tabs %}
{% tab Android %}
#### Etapa 2.1: Configurar as definições de push

O SDK da Braze pode lidar automaticamente com o registro de push com os servidores do Firebase Cloud Messaging para que os dispositivos recebam notificações por push. No Unity, ative **a Automate Unity Android Integration** e, em seguida, defina as seguintes configurações **de notificação por push**.

| Configuração                                | Descrição                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Registro automático de envio de mensagens do Firebase ativado | Instrui o Braze SDK a recuperar e enviar automaticamente um token por push FCM para um dispositivo.                                                                |
| ID de remetente do Firebase Cloud Messaging     | O ID do remetente do seu console do Firebase.                                                                                                                |
| Manipular deeplinks de push automaticamente    | Se o SDK deve lidar com a abertura de links profundos ou abrir o app quando notificações por push são clicadas.                                                  |
| Pequeno Ícone de Notificação Drawable       | O drawable deve ser exibido como o ícone pequeno sempre que uma notificação por push for recebida. A notificação usará o ícone do aplicativo como o ícone pequeno se nenhum ícone for fornecido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### Etapa 2.1: Faça upload de seu token de APNs

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Etapa 2.2: Ativar o push automático

Abra as definições de configuração da Braze no Unity Editor navegando até **Braze > Configurações**.

Marque **Integrar Push com o Braze** para registrar automaticamente os usuários para notificações por push, passar tokens por push para o Braze, rastrear análises de dados para aberturas de push e aproveitar nosso tratamento padrão de notificações por push.

#### Etapa 2.3: Ativar o push em segundo plano (opcional)

Marque **Ativar push em segundo plano** se quiser ativar o `background mode` para notificações por push. Isso permite que o sistema desperte seu aplicativo do estado `suspended` quando chegar uma notificação por push, ativando seu aplicativo para baixar conteúdo em resposta às notificações por push. É necessário marcar essa opção para nossa funcionalidade de rastreamento de desinstalação.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, as opções "Automate Unity iOS integration" (Automatizar integração do Unity com iOS), "Integrate push with Braze" (Integrar push com Braze) e "Enable background push" (Ativar capacitação em segundo plano) estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Etapa 2.4: Desativar o registro automático (opcional)

Os usuários que ainda não tiverem aceitado as notificações por push serão automaticamente autorizados a receber push ao abrir o aplicativo. Para desativar esse recurso e registrar manualmente os usuários para push, marque **Disable Automatic Push Registration (Desativar registro automático de push**).

- Se **a opção Disable Provisional Authorization (Desativar autorização provisória**) não estiver marcada no iOS 12 ou posterior, o usuário será autorizado provisoriamente (silenciosamente) a receber o quiet push. Se estiver marcada essa opção, o usuário verá o prompt push nativo.
- Se precisar configurar exatamente quando o prompt é mostrado em tempo de execução, desative o registro automático no editor de configuração do Braze e use `AppboyBinding.PromptUserForPushPermissions()`.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, as opções "Automate Unity iOS integration", "integrate push with Braze" e "disable automatic push registration" estão ativadas.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Etapa 2.1: Atualize `AndroidManifest.xml`

Se o seu app não tiver um `AndroidManifest.xml`, você poderá usar o seguinte modelo. Caso contrário, se você já tiver um `AndroidManifest.xml`, confira se falta alguma das seções a seguir e adicione-as ao seu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Etapa 2.2: Armazene sua chave de API do ADM

Em nome do seu [aplicativo, gere uma chave de API do ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), salve a chave em um arquivo chamado `api_key.txt` e adicione-o ao diretório [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) do projeto.

{% alert important %}
A Amazon não reconhecerá sua chave se `api_key.txt` contiver caracteres de espaço em branco, como uma quebra de linha à direita.
{% endalert %}

Em seguida, em seu arquivo `mainTemplate.gradle`, adicione o seguinte:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Etapa 2.3: Adicionar um arquivo .jar de ADM

O arquivo Jar do ADM necessário pode ser colocado em qualquer lugar do seu projeto, de acordo com a [documentação do JAR do Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Etapa 2.4: Adicionar o segredo do cliente e o ID do cliente ao dashboard da Braze

Por fim, você deve adicionar o segredo do cliente e o ID do cliente obtidos na [etapa 1](#unity_step-1-enable-adm) à página de **Gerenciar configurações** do dashboard da Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Etapa 3: Definir ouvintes de push

{% tabs %}
{% tab Android %}
#### Etapa 3.1: Ativar o ouvinte de push recebido

O ouvinte recebido de push é acionado quando um usuário recebe uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e envie o método de retorno de chamada do ouvinte recebido em **Set Push Received Listener**.

#### Etapa 3.2: Ativar o ouvinte de push aberto

O ouvinte aberto de push é acionado quando um usuário lança o app clicando em uma notificação por push. Para enviar a carga útil push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push aberto em **Set Push Opened Listener**.

#### Etapa 3.3: Ativar o ouvinte push excluído

O ouvinte de exclusão de push é acionado quando um usuário desliza ou descarta uma notificação por push. Para enviar a carga útil do push para o Unity, defina o nome do seu objeto de jogo e o método de retorno de chamada do ouvinte de push excluído em **Set Push Deleted Listener**.

#### Exemplo de ouvinte push

O exemplo a seguir implementa o objeto de jogo `BrazeCallback` usando um método de retorno de chamada chamado `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` e `PushNotificationDeletedCallback` respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração da Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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
{% endtab %}

{% tab Swift %}
#### Etapa 3.1: Ativar o ouvinte de push recebido

O ouvinte de recebimento de push é acionado quando um usuário recebe uma notificação por push enquanto usa ativamente o aplicativo (por exemplo, quando o app está em primeiro plano). Defina o listener de recebimento de push no editor de configuração do Braze. Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_RECEIVED`.

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, a opção "Set Push Received Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationReceivedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Etapa 3.2: Ativar o ouvinte de push aberto

O ouvinte aberto de push é acionado quando um usuário lança o app clicando em uma notificação por push. Para enviar a carga útil push para o Unity, defina o nome de seu objeto de jogo e o método de retorno de chamada do ouvinte de abertura de push na opção **Set Push Opened Listener**:

![O editor Unity mostra as opções de configuração da Braze. Nesse editor, a opção "Set Push Received Listener" é expandida, e o "Game Object Name" (AppBoyCallback) e o "Callback Method Name" (PushNotificationOpenedCallback) são fornecidos.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.PUSH_OPENED`.

#### Exemplo de ouvinte push

O exemplo a seguir implementa o objeto de jogo `AppboyCallback` usando um nome de método de retorno de chamada `PushNotificationReceivedCallback` e `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de exemplo de implementação mostra as opções de configuração da Braze mencionadas nas seções anteriores e um trecho de código C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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
{% endtab %}

{% tab Amazon Device Messaging %}
Ao atualizar o site `AndroidManifest.xml` na [etapa anterior](#unity_step-21-update-androidmanifestxml), os push listeners foram configurados automaticamente quando você adicionou as seguintes linhas. Portanto, não é necessária nenhuma configuração adicional.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Para saber mais sobre os ouvintes push da ADM, consulte [Amazon: Integrar o envio de mensagens da Amazon para dispositivos](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurações opcionais

{% tabs %}
{% tab Android %}
#### Deep linking para recursos in-app

Embora a Braze possa lidar com links profundos padrão (como URLs de sites, URIs do Android, etc.) por padrão, a criação de links profundos personalizados requer uma configuração adicional do Manifesto.

Para obter orientações de configuração, visite [Deep linking para recursos no aplicativo](https://developer.android.com/training/app-links/deep-linking).

#### Adição de ícones de notificação por push do Braze

Para adicionar ícones push ao seu projeto, crie um plug-in do Android Archive (AAR) ou uma biblioteca do Android que contenha os arquivos de imagem do ícone. Para obter etapas e informações, consulte a documentação da Unity: [Projetos de biblioteca do Android e plug-ins do Android Archive](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).
{% endtab %}

{% tab Swift %}
#### Retorno de chamada do token por push

Para receber uma cópia dos tokens de dispositivos Braze do sistema operacional, defina um delegate usando `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
No momento, não há configurações opcionais para o ADM.
{% endtab %}
{% endtabs %}
