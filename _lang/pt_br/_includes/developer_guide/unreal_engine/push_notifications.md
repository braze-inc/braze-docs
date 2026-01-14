{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Configurando notificações por push

### Etapa 1: Configure seu projeto

{% tabs %}
{% tab Android %}
Primeiro, adicione o Firebase ao seu projeto Android. Para obter instruções passo a passo, consulte o [guia de configuração do Firebase](https://firebase.google.com/docs/android/setup) do Google.
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### Etapa 2: Ativar notificações por push

{% tabs %}
{% tab Android %}
Adicione as seguintes linhas ao arquivo `engine.ini` do seu projeto. Certifique-se de substituir `YOUR_SEND_ID` pelo [ID do remetente no seu projeto Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials).

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

Dentro do mesmo diretório que [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml), crie um novo diretório chamado `AndroidCopies` e adicione seu arquivo `google-services.json` a ele.
{% endtab %}

{% tab iOS %}
No seu projeto, acesse **Configurações** > **Configurações do Projeto** > **iOS** > **Online** e marque **Ativar Suporte a Notificações Remotas**. Quando terminar, verifique se sua provisão tem capacidades de push ativadas.

{% alert important %}
Para ativar capacidades de push para iOS, seu projeto deve ter sido construído a partir do código-fonte. Para saber mais, veja [Unreal Engine: Construindo a partir do código-fonte](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configurações opcionais

{% tabs %}
{% tab Android %}
#### Definindo ícones pequenos e grandes

Para definir os [ícones de notificação pequenos e grandes]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons):

1. Adicione ícones à pasta drawable apropriada (`drawable` por padrão) dentro da pasta `AndroidCopies/res`.
2. Adicione `braze.xml` à pasta `AndroidCopies/res/values` para definir os ícones. Um arquivo braze.xml muito básico:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
Os arquivos da pasta `AndroidCopies` serão copiados para a estrutura do projeto Android gerado, conforme definido no `BrazeUPLAndroid.xml`.
{% endalert %}
{% endtab %}

{% tab iOS %}
#### Notificações de lançamento remoto

A partir da versão 4.25.3 do Unreal Engine, o UE4 não possui suporte adequado para receber uma notificação remota que causa o lançamento inicial do aplicativo. Para suportar o recebimento dessa notificação, criamos dois patches git para aplicar - um para o UE4 e um para o plugin Braze SDK.

1. No diretório `Source` do seu Engine UE4, aplique o patch git `UE4_Engine-Cache-Launch-Remote-Notification.patch`.
2. No diretório do seu SDK Unreal Braze, aplique o patch git `Braze_SDK-Read-Cached-Remote-Launch-Notification.patch`.
{% endtab %}
{% endtabs %}
