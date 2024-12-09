---
nav_title: Integração da Huawei
article_title: Integração de push da Huawei para Android
platform: Android
page_order: 9
description: "Este artigo aborda como configurar uma integração Android da Huawei."
channel:
  - push

---

# Integração de push da Huawei

> Os telefones mais novos fabricados pela [Huawei](https://huaweimobileservices.com/) vêm equipados com o Huawei Mobile Services (HMS), um serviço usado para enviar push em vez do Firebase Cloud Messaging (FCM) do Google.<br><br>Este guia mostrará como configurar sua integração com o Android da Huawei para enviar push pela Braze e aproveitar todos os nossos recursos, como segmentação, análise de dados, canvas e muito mais!

## Etapa 1: Crie uma conta de desenvolvedor da Huawei

Antes de começar, você precisará criar uma [conta de desenvolvedor da Huawei](https://developer.huawei.com/consumer/en/console). Em sua conta da Huawei, acesse **My Projects > Project Settings > App Information** (Meus projetos > Configurações do projeto > Informações do app) e anote os endereços `App ID` e `App secret`.

![]({% image_buster /assets/img/huawei/huawei-credentials.png %})

## Etapa 2: Crie um novo app da Huawei no dashboard da Braze

No dashboard da Braze, acesse **Configurações** > **Configurações do app**.

Clique em **\+ Adicionar app**, forneça um nome (como My Huawei App) e selecione `Android` como a plataforma.

![]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Depois que seu novo app da Braze tiver sido criado, localize as configurações de notificação por push e selecione `Huawei` como o provedor de push. Em seguida, forneça seu `Huawei Client Secret` e `Huawei App ID`.

![]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

## Etapa 3: Integre o SDK de envio de mensagens da Huawei em seu app

A Huawei forneceu um [codelab de integração Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) detalhando a integração do Huawei Messaging Service em seu app. Siga essas etapas para começar.

Depois de concluir o codelab, você precisará criar um [Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) personalizado para obter tokens por push e encaminhar mensagens para o SDK da Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Depois de adicionar seu serviço push personalizado, adicione o seguinte em seu `AndroidManifest.xml`:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

## Etapa 4: Enviar um push da Huawei

Neste ponto, você criou um novo app Huawei para Android no dashboard da Braze, configurou-o com suas credenciais de desenvolvedor da Huawei e integrou os SDKs da Braze e da Huawei ao seu app.

Em seguida, podemos testar a integração testando uma nova campanha push na Braze.

### Criar uma nova campanha de notificação por push

Na página **Campanhas**, crie uma nova campanha e escolha **Notificação por push** como o tipo de mensagem.

Depois de dar um nome à sua campanha, escolha **Push para Android** como a plataforma de push.

![O criador da campanha exibe as plataformas de push disponíveis.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Em seguida, crie sua campanha de push com um título e uma mensagem.

### Enviar um push de teste

Na guia **Teste**, digite o ID do usuário, que foi definido no app usando o [método `changeUser(USER_ID_STRING)`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#assigning-a-user-id), e clique em **Enviar teste** para enviar um push de teste.

![A guia Teste no criador de mensagens de campanha mostra que você pode enviar uma mensagem de teste para si mesmo, fornecendo seu ID de usuário e inserindo-o no campo "Add Individual Users" (Adicionar usuários individuais).]({% image_buster /assets/img/huawei/huawei-test-send.png %})

Nesse momento, você deverá receber uma notificação por push de teste da Braze em seu dispositivo Huawei (HMS).

### Configuração da segmentação da Huawei (opcional)

Como o app da Huawei no dashboard da Braze foi criado com base na plataforma de push do Android, você tem a flexibilidade de enviar push para todos os usuários do Android (Firebase Cloud Messaging e Huawei Mobile Services) ou pode optar por segmentar o público da campanha para apps específicos.

Para enviar push apenas para apps da Huawei, [crie um novo segmento]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) e selecione seu app da Huawei na seção **Apps**.

![]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Claro, se quiser enviar o mesmo push para todos os provedores de push do Android, você pode optar por não especificar o app que enviará para todos os apps para Android configurados no espaço de trabalho atual.

## Análise de dados

Após o lançamento da campanha, você verá as análises de dados da campanha ou do canva agregadas para o push para Android. Consulte nosso [guia do usuário do push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) para saber mais sobre as análises e configurações de dados do push para Android.

