---
nav_title: Notificações por push
article_title: Notificações por push para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "Este artigo aborda a integração de notificações por push para Android, FireOS e iOS na plataforma Xamarin."
channel: push
toc_headers: h2
---

# Integração de notificações por push

> Saiba como configurar notificações por push para Android, FireOS e iOS no Xamarin.

## Pré-requisitos

Para usar esse recurso, você precisará [integrar o SDK da Braze para a plataforma Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Integração de notificações por push

{% tabs %}
{% tab Android %}
{% alert tip %}
Para ver como os namespaces mudam entre Java e C#, dê uma olhada em nosso [app de amostra Xample no GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp).
{% endalert %}

Para integrar notificações por push no Xamarin, você precisará concluir as etapas das notificações por push nativas do Android. As etapas a seguir são apenas um resumo. Para obter um passo a passo completo, consulte o [guia de notificações por push nativas]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/).

### Etapa 1: Atualize seu projeto

1. Adicione o Firebase ao seu projeto Android.
2. Adicione a biblioteca de envio de mensagens da Cloud ao site `build.gradle` de seu projeto Android:
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### Etapa 2: Crie suas credenciais JSON

1. No Google Cloud, ative a [API de envio de mensagens do Firebase Cloud](https://console.cloud.google.com/apis/library/fcm.googleapis.com).
2. Selecione **Service Accounts (Contas de serviço** ) > your project (seu projeto) > **Create Service Account (criar conta de serviço**) e insira o nome, o ID e a descrição da conta de serviço. Quando terminar, selecione **Create (Criar) e continue**.
3. No campo **Função**, localize e selecione **Firebase Cloud Messaging API Admin** na lista de funções.
4. Em **Service Accounts (Contas de serviço)**, escolha seu projeto e selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Actions (Ações)** > **Manage Keys (Gerenciar chaves)** > **Add Key (Adicionar chave)** > **Create new key (Criar nova chave)**. Escolha **JSON** e, em seguida, selecione **Create (Criar)**.

### Etapa 3: Faça upload de suas credenciais JSON

1. Na Braze, selecione <i class="fa-solid fa-gear"></i> **Configurações** > **Configurações do app**. Nas **configurações de notificação por push** do seu app para Android, escolha **Firebase**, selecione **Upload JSON File** e faça upload das credenciais geradas anteriormente. Quando terminar, selecione **Salvar**.
2. Ative o registro automático do token FCM, acessando o Firebase Console. Abra seu projeto e selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings**. Selecione **Envio de mensagens na nuvem** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o número no campo **Sender ID (ID do remetente** ).
3. Em seu projeto do Android Studio, coloque o seguinte em `braze.xml`.

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
Para evitar que a Braze dispare solicitações de rede desnecessárias sempre que você enviar notificações por push silenciosas, remova todas as solicitações de rede automáticas configuradas no método `onCreate()` de sua classe `Application`. Para saber mais, consulte [Android Developer Reference: Aplicativo](https://developer.android.com/reference/android/app/Application).
{% endalert %}
{% endtab %}

{% tab ios %}
### Etapa 1: Concluir a configuração inicial

Consulte as [instruções de integração do Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration) para obter informações sobre como configurar seu aplicativo com push e armazenar suas credenciais em nosso servidor. Consulte o aplicativo de amostra [MAUI do iOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) para obter mais detalhes.

### Etapa 2: Solicitar permissão para notificações por push

Nosso Xamarin SDK agora oferece suporte à configuração automática de push. Configure a automação e as permissões do push adicionando o seguinte código à configuração da instância do Braze:

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

Consulte o aplicativo de amostra [MAUI do iOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp) para obter mais detalhes. Para saber mais, consulte a documentação da Xamarin sobre [Notificações aprimoradas do usuário em Xamarin.iOS](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos).
{% endtab %}
{% endtabs %}
