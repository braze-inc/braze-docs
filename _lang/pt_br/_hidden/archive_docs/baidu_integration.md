---
nav_title: Integração com o Baidu
article_title: Integração de notificações por push do Baidu para Android
platform: Android
permalink: /baidu_integration/
description: "Este artigo mostra como configurar uma integração do Baidu com o Android."
hidden: true
---
# Integração com o Baidu
{% multi_lang_include archive/baidu_deprecation.md %}

O Braze pode enviar notificações por push para dispositivos Android usando o [Baidu Cloud Push][14]. Note que o uso do Baidu Cloud Push **não** exige que você distribua seus apps por meio da Baidu App Store.

## Etapa 1: Criar uma conta no Baidu

Para criar uma conta no Baidu, visite o [Portal do Baidu][7] e clique em **登录** (Entrar) para abrir uma caixa de diálogo que permitirá o registro ou a criação de uma nova conta.

![][33]

Para criar uma nova conta, na parte inferior da caixa de diálogo de login, clique em **立即注册** (nova conta).

![][38]{: style="max-width:70%;"}

Digite seu nome de usuário, número de telefone e senha na página de criação de conta. Em seguida, clique no botão Receber código de verificação. Agora você receberá uma mensagem SMS do Baidu com um código de verificação. Por fim, aceite o contrato de licença e clique em **注册** (criar conta) para se registrar. Se essas etapas de configuração falharem, tente se registrar por meio do login do Baidu Cloud, conforme descrito neste [artigo sobre login](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Página de registro do Baidu][17]{: style="max-width:80%;"}

## Etapa 2: Registre-se como desenvolvedor do Baidu

Em seguida, você deve se registrar como desenvolvedor do Baidu. Primeiro, visite o [portal do desenvolvedor do Baidu][36] e escolha **注册** (criar nova conta de desenvolvedor) para iniciar o registro.

![][37]

Na página de registro, escolha o tipo de conta (个人 para pessoal, 公司 para negócios) e o tipo de desenvolvedor (desenvolvedor é pré-selecionado e correto para a maioria dos casos). Digite seu nome, biografia e número de telefone com o código do país entre parênteses (por exemplo, (1)xxxxxxxxxxxx). Clique em **发送验证码** (enviar código de verificação) e digite o código de verificação na linha seguinte. Os próximos dois campos, site do desenvolvedor e logotipo do desenvolvedor, são opcionais. Aceite o contrato de licença e clique em **提交** (Enviar). Agora você tem uma conta de desenvolvedor do Baidu.

![][13]

## Etapa 3: Registre seu aplicativo no Baidu

Para registrar seu aplicativo no Baidu, visite o [portal de projetos do Baidu][11] e clique em **创建工程** (criar projeto).

![][10]

Na página seguinte, digite o nome do aplicativo. As duas caixas de seleção a seguir servem para ativar serviços adicionais do Baidu. Na maioria dos casos, elas devem ser deixadas em branco.

![][26]

Ao configurar o seu aplicativo, você será levado a um console que exibe informações sobre o seu app, incluindo a chave de API. Em seguida, navegue até **云推送** (cloud push) na barra lateral. Na página seguinte, clique em **推送设置** (set up push).

![][14]

![][29]

Na página seguinte, digite o nome do pacote do app (por exemplo, `com.braze.sample`) e especifique se deseja armazenar as mensagens em cache e, em caso afirmativo, por quanto tempo (em horas). Isso indica ao Baidu quanto tempo deve continuar tentando enviar mensagens para usuários off-line. Clique em **保存设置** (salvar configurações) para salvar.

![][39]

## Etapa 4: Adicione o Baidu ao seu aplicativo

Acesse o [portal do Baidu push SDK][40] e baixe o Baidu Cloud Push Android SDK mais recente.

![][41]

Dentro do SDK, você encontrará o jar do serviço push e as bibliotecas nativas específicas da plataforma. Integre-os ao seu projeto. Certifique-se de que seu app esteja direcionado para a versão mais alta do SDK atualmente suportada pelo Baidu. Esta documentação é atual para a versão do SDK do Baidu Cloud push para Android `4.6.2.38`.

Adicione as seguintes permissões necessárias do Baidu ao site `AndroidManifest.xml` do seu aplicativo.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

A biblioteca da Baidu contém receptores de transmissão que lidam com as mensagens push recebidas. Declare os receptores internos do Baidu no site `AndroidManifest.xml` do seu aplicativo dentro do elemento `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

Você também precisará criar um receptor de transmissão que ouça as mensagens e notificações por push recebidas. Declare o receptor no `AndroidManifest.xml` do seu aplicativo, dentro do elemento `<application>`. Esse receptor precisará estender o site `com.baidu.android.pushservice.PushMessageReceiver` e implementar métodos que recebam atualizações de eventos do serviço push do Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

No método `onCreate()` da atividade principal, adicione a seguinte linha, que registrará o aplicativo no Baidu e começará a ouvir as mensagens push recebidas. Certifique-se de substituir "Your-API-Key" pela chave de API do Baidu do seu projeto.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Por fim, será necessário registrar seus usuários no Braze. No método `onBind()` do receptor de transmissão do Baidu que você criou nesta etapa, envie o `channelId` para o Braze usando `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Etapa 5: Registro de aberturas push

O Baidu suporta o envio de pares de valores-chave extras com mensagens push no formato JSON. O método `public void onNotificationClicked(Context context, String title, String description, String customContentString)` do seu receptor de broadcast será chamado sempre que um usuário clicar em uma mensagem push recebida. O parâmetro `customContentString` contém os extras no formato JSON. Todas as mensagens do Braze conterão os dois pares de valores-chave a seguir:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Sempre que `onNotificationClicked` for chamado pelo seu receptor Baidu, o receptor deverá enviar uma [intenção][44] para o seu aplicativo contendo `customContentString`. Seu aplicativo registrará o clique na Braze usando o endereço `customContentString`.

O código de exemplo a seguir passa o endereço `customContentString` para a Braze e registra um clique:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Etapa 6: Extras

Além das chaves reservadas usadas pela Braze, o parâmetro `customContentString` também conterá todos os pares de chave/valor personalizados definidos pelo usuário. Para extrair seus pares de chave/valor, envolva `customContentString` em um objeto JSON e recupere seus extras:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Etapa 7: Configurar as chaves do Baidu

Você precisa inserir sua chave de API do Baidu e a chave secreta do Baidu no dashboard do Braze. Ambas as chaves estão disponíveis no console do aplicativo Baidu.

Na página **Manage Settings (Gerenciar configurações)**, selecione seu app Android China e insira sua Baidu API Key e Baidu Secret Key na seção de notificações por push.

![][19]{: style="max-width:80%;"}

## Recursos adicionais

- [Portal do Baidu][7]
- [Portal do desenvolvedor do Baidu][36]
- [Portal do projeto Baidu][11]
- [Portal do SDK de push do Baidu][40]
- [Documentos de integração do Baidu][43]

[7]: https://www.baidu.com/
[10]: {% image_buster /assets/img_archive/baidu_project.png %}
Daqui a [11]: http://developer.baidu.com/console#app/project
[13]: {% image_buster /assets/img_archive/baidu_dev_reg.png %}
[14]: {% image_buster /assets/img_archive/baidu_app_console.png %}
[17]: {% image_buster /assets/img_archive/baidu_signup.png %}
[19]: {% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"
[26]: {% image_buster /assets/img_archive/baidu_app_name.png %}
[29]: {% image_buster /assets/img_archive/baidu_continue.png %}
[33]: {% image_buster /assets/img_archive/baidu_portal.png %}
[34]: {% image_buster /assets/img_archive/baidu_email.png %}
[35]: {% image_buster /assets/img_archive/baidu_text.png %}
Daqui a [36]: http://developer.baidu.com/
[37]: {% image_buster /assets/img_archive/baidu_dev_portal.png %}
[38]: {% image_buster /assets/img_archive/baidu_login_dialog.png %}
[39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %}
Daqui a [40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[41]: {% image_buster /assets/img_archive/baidu_sdk.png %}
Daqui a [43]: http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
Daqui a [44]: http://developer.android.com/reference/android/content/Intent.html
