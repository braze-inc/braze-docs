---
nav_title: Integração
article_title: Integração push para FireOS
platform: FireOS
page_order: 0
page_type: solution
description: "Este artigo de referência explica como integrar as notificações por push da Braze em seu aplicativo FireOS."
channel: push
search_rank: 0.9
---

# Integração de push do FireOS

> Este artigo de referência explica como integrar as notificações por push da Braze em seu aplicativo FireOS.

Uma notificação por push é um alerta fora do aplicativo que aparece na tela do usuário quando ocorre uma atualização importante. As notificações por push são uma forma valiosa de fornecer aos usuários conteúdo relevante e oportuno para reengajá-los com seu app.

O ADM (envio de mensagens da Amazon para dispositivos) não é compatível com dispositivos que não sejam da Amazon. Para testar o push para Kindle, você precisa ter um [dispositivo FireOS](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Consulte nosso [artigo de ajuda]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) para obter práticas recomendadas adicionais.

O Braze envia notificações por push para dispositivos Amazon usando o [envio de mensagens para dispositivos Amazon (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Etapa 1: Ativar ADM

1. Crie uma conta no [Portal do desenvolvedor de apps e jogos da Amazon](https://developer.amazon.com/public), caso ainda não tenha feito isso.
2. Obtenha [as credenciais do OAuth (ID do cliente e segredo do cliente) e uma chave de API do ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Ative o **registro automático de ADM** na janela de configuração do Unity Braze. 
  - Como alternativa, é possível adicionar a seguinte linha ao arquivo `res/values/braze.xml` para ativar o registro do ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Etapa 2: Atualize AndroidManifest.xml

No site AndroidManifest.xml de seu app, adicione o namespace da Amazon à tag `<>manifest</>`:

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

Em seguida, declare as permissões necessárias para dar suporte ao ADM, adicionando os elementos `<>permission</>` e `<>uses-permission</>` após `<>manifest</> element`:

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

Em seguida, declare que seu app usa o recurso ADM do dispositivo e que foi projetado para permanecer funcional sem o ADM presente no dispositivo (`android:required="false"`) adicionando um elemento `amazon:enable-feature` ao elemento de aplicativo do manifesto. É seguro definir `android:required` como `"false"` porque o código do Braze ADM se degrada de forma graciosa quando o ADM não está presente no dispositivo:

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

Por fim, adicione filtros de intenção para lidar com as intenções `REGISTRATION` e `RECEIVE` do ADM em seu arquivo Braze `AndroidManifest.xml`. Imediatamente após `amazon:enable-feature`, adicione os seguintes elementos:

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## Etapa 3: Armazene sua chave de API do ADM

Primeiro, salve sua chave de API do ADM em um arquivo chamado `api_key.txt` e salve-o na pasta [`Assets/Plugins/Android/assets`][54] ] de seu projeto. Em seguida, [obtenha uma chave de API do ADM para seu app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).

A Amazon não reconhecerá sua chave se `api_key.txt` contiver caracteres de espaço em branco, como uma quebra de linha à direita.

## Etapa 4: Adicionar deep links

#### Ativando a abertura automática de deep linking

Para permitir que a Braze abra automaticamente seu app e quaisquer deep links quando uma notificação por push for clicada, defina `com_braze_handle_push_deep_links_automatically` como `true` em seu `braze.xml`:

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Se quiser personalizar o tratamento de deep linkings, você precisará criar um retorno de chamada de push que escute as intenções de push recebidas e abertas da Braze. Consulte [Manuseio personalizado de recibos e aberturas de push]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) na documentação do Android push para obter mais informações.

## Etapa 5: Adicionar o segredo do cliente e o ID do cliente ao dashboard da Braze

Por fim, você deve adicionar o segredo do cliente e o ID do cliente obtidos na [etapa 1](#step-1-enable-adm) à página de **Gerenciar configurações** do dashboard da Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## Registro push manual

A Braze não recomenda o uso do registro manual, mas, se você precisar lidar com o registro do ADM, adicione a seguinte opção ao seu arquivo [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm):

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
Em seguida, use [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) para passar o ADM do usuário `registration_id` para a Braze:

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## Extras da ADM

Os usuários podem enviar pares de valores-chave personalizados com uma mensagem push do Kindle como `extras` para [deep linking]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/), URLs de rastreamento, etc. Ao contrário do Android push, os usuários do Kindle push não podem usar as chaves reservadas do Braze como chaves ao definir os pares de valores-chave do `extra`.

As chaves reservadas incluem:

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Se uma tecla reservada do Kindle for detectada, o Braze retornará `Status Code 400: Kindle Push Reserved Key Used`.

