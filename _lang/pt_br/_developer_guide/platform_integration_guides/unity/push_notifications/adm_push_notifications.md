---
nav_title: Envio de mensagens para dispositivos da Amazon
article_title: Notificações por push de envio de mensagens de dispositivos da Amazon para o Unity
platform: 
  - Unity
  - Android
page_order: 2
description: "Este artigo de referência cobre a integração de notificação por push do Android da Amazon para a plataforma Unity."
channel: push

---

# Envio de mensagens para dispositivos da Amazon

> Este artigo de referência cobre a integração de notificação por push do Android da Amazon para a plataforma Unity.

Uma notificação por push é um alerta fora do aplicativo que aparece na tela do usuário quando ocorre uma atualização importante. As notificações por push são uma forma valiosa de fornecer aos usuários conteúdo relevante e oportuno ou para reengajá-los com seu app.

O ADM (envio de mensagens da Amazon para dispositivos) não é compatível com dispositivos que não sejam da Amazon. Para testar o push para Kindle, você precisa ter um [dispositivo FireOS](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm). Consulte a [seção de ajuda]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) para obter práticas recomendadas adicionais.

O Braze envia notificações por push para dispositivos Amazon usando o [envio de mensagens para dispositivos Amazon (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging).

## Etapa 1: Ativar ADM

1. Crie uma conta no [Portal do desenvolvedor de apps e jogos da Amazon](https://developer.amazon.com/public), caso ainda não tenha feito isso.
2. Obtenha [as credenciais do OAuth (ID do cliente e segredo do cliente) e uma chave de API do ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Ative o **registro automático de ADM** na janela de configuração do Unity Braze. 
  - Como alternativa, é possível adicionar a seguinte linha ao arquivo `res/values/braze.xml` para ativar o registro do ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## Etapa 2: Atualizar o Unity AndroidManifest.xml

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

## Etapa 3: Armazene sua chave de API do ADM

Primeiro, [obtenha uma chave de API do ADM para seu app](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  Em seguida, salve sua chave de API do ADM em um arquivo chamado `api_key.txt` e salve-o na pasta [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) do projeto.

A Amazon não reconhecerá sua chave se `api_key.txt` contiver caracteres de espaço em branco, como uma quebra de linha à direita.

Em seu arquivo `mainTemplate.gradle`, adicione o seguinte:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## Etapa 4: Adicionar um arquivo .jar de ADM

O arquivo Jar do ADM necessário pode ser colocado em qualquer lugar do seu projeto, de acordo com a [documentação do JAR do Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

## Etapa 5: Adicionar o segredo do cliente e o ID do cliente ao dashboard da Braze

Por fim, você deve adicionar o segredo do cliente e o ID do cliente obtidos na [etapa 1](#step-1-enable-adm) à página de **Gerenciar configurações** do dashboard da Braze.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

