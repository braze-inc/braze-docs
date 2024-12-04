---
nav_title: Notificações por push
article_title: Notificações por push para o Flutter
platform: Flutter
page_order: 2
description: "Este artigo aborda a implementação e o teste de notificações por push no Flutter."
channel: push

---

# Integração de notificações por push

> Este artigo de referência aborda como definir notificações por push para o Flutter. A integração de notificações por push requer a configuração de cada plataforma nativa separadamente. Siga os respectivos guias listados para concluir a instalação.

## Etapa 1: Concluir a configuração inicial

{% tabs %}
{% tab Android %}
### Etapa 1.1: Registro para push

Registre-se para push usando a API Firebase Cloud Messaging (FCM) do Google. Para obter um passo a passo completo, consulte as etapas a seguir do [guia de integração de push do Android nativo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/):

1. [Adicione o Firebase ao seu projeto]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Adicione o Cloud Messaging às suas dependências]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Crie uma conta de serviço]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Gerar credenciais JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Faça upload de suas credenciais JSON na Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### Etapa 1.2: Obtenha seu Sender ID (ID do remetente) do Google

Primeiro, acesse o Console Firebase, abra seu projeto e selecione <i class="fa-solid fa-gear"></i> **Settings** > **Project settings** (Configurações .> Configurações do projeto).

![O projeto Firebase com o menu "Settings" (Configurações) aberto.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Selecione **Envio de mensagens na nuvem** e, em seguida, em **Firebase Cloud Messaging API (V1)**, copie o **ID do remetente** para a área de transferência.

![A página "Cloud Messaging" do projeto Firebase com o "Sender ID" (ID do remetente) destacado.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

### Etapa 1.3: Atualize seu `braze.xml`

Adicione o seguinte ao seu arquivo `braze.xml`. Substitua `FIREBASE_SENDER_ID` pela ID do remetente que você copiou anteriormente.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
### Etapa 1.1: Faça upload de certificados APNs

Gere um certificado do serviço de Notificações por Push da Apple (APNs) e faça upload dele no dashboard do Braze. Veja um passo a passo completo em [Como fazer upload de seu certificado de APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

### Etapa 1.2: Adicione suporte a notificações por push ao app

Siga o [guia de integração nativa do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

## Etapa 2: Ouça os eventos de notificação por push (opcional)

Para ouvir os eventos de notificação por push que a Braze detectou e tratou, chame `subscribeToPushNotificationEvents()` e passe um argumento a ser executado.

{% alert note %}
Os eventos de notificação por push do Braze estão disponíveis tanto no Android quanto no iOS. Devido às diferenças de plataforma, o iOS só detectará eventos push do Braze quando um usuário interagir com uma notificação.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Campos de eventos de notificação por push

{% alert note %}
Devido às limitações da plataforma no iOS, o SDK da Braze só pode processar cargas úteis push enquanto o app estiver em primeiro plano. Os ouvintes (listeners) só serão disparados para o tipo de evento `push_opened` no iOS depois que um usuário interagir com um push.
{% endalert %}

Para obter uma lista completa dos campos de notificação por push, consulte a tabela abaixo:

| Nome do campo         | Tipo      | Descrição |
| ------------------ | --------- | ----------- |
| `payloadType`     | String    | Especifica o tipo de carga útil da notificação. Os dois valores enviados pelo Braze Flutter SDK são `push_opened` e `push_received`.  Somente os eventos `push_opened` são compatíveis com o iOS. |
| `url`              | String    | Especifica a URL que foi aberta pela notificação. |
| `useWebview`      | Booleano   | Se for `true`, a URL será aberta no app em uma visualização modal da Web. Se for `false`, a URL será aberta no navegador do dispositivo. |
| `title`            | String    | Representa o título da notificação. |
| `body`             | String    | Representa o corpo ou o texto do conteúdo da notificação. |
| `summaryText`     | String    | Representa o texto resumido da notificação. Isso é mapeado em `subtitle` no iOS. |
| `badgeCount`      | Número   | Representa a contagem de emblemas da notificação. |
| `timestamp`        | Número | Representa a hora em que a carga útil foi recebida pelo app. |
| `isSilent`        | Booleano   | Se for `true`, a carga útil é recebida silenciosamente. Para obter detalhes sobre o envio de notificações por push silenciosas no Android, consulte [Notificações por push silenciosas no Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications). Para obter detalhes sobre o envio de notificações por push silenciosas no iOS, consulte [Notificações por push silenciosas no iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/). |
| `isBrazeInternal`| Booleano   | Este será o endereço `true` se uma carga útil de notificação tiver sido enviada para um recurso interno do SDK, como sincronização de geofences, sincronização de Feature Flag ou rastreamento de desinstalação. A carga útil é recebida silenciosamente para o usuário. |
| `imageUrl`        | String    | Especifica o URL associado à imagem da notificação. |
| `brazeProperties` | Objeto    | Representa as propriedades do Braze associadas à campanha (pares chave-valor). |
| `ios`              | Objeto    | Representa campos específicos do iOS. |
| `android`          | Objeto    | Representa campos específicos do Android. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Teste a exibição de notificações por push

Para testar sua integração depois de configurar as notificações por push na camada nativa:

1. Defina um usuário ativo no aplicativo Flutter. Para fazer isso, inicialize seu plug-in chamando `braze.changeUser('your-user-id')`.
2. Vá para **Campaigns (Campanhas** ) e crie uma nova campanha de notificação por push. Escolha as plataformas que você gostaria de testar.
3. Crie sua notificação de teste e vá para a guia **Teste**. Adicione o mesmo `user-id` que o usuário teste e clique em **Send Test (Enviar teste**).
4. Você deverá receber a notificação em seu dispositivo em breve. Talvez seja necessário verificar a Central de Notificações ou atualizar as Configurações se ela não for exibida.

{% alert tip %}
A partir do Xcode 14, você pode testar notificações por push remotas em um simulador de iOS.
{% endalert %}
