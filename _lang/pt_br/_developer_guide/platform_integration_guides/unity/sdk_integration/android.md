---
nav_title: Android
article_title: Integração de SDK Android para Unity
platform: 
  - Unity
  - Android
page_order: 0
description: "Este artigo de referência aborda a integração do Android SDK para a plataforma Unity."
search_rank: .9
---

# Integração do SDK com o Android

> Este artigo de referência aborda a integração do Android SDK para a plataforma Unity. Siga estas instruções para executar a Braze em seu app Unity.

## Etapa 1: Escolha seu pacote Braze Unity

O [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) da Braze agrupa associações nativas para as plataformas Android e iOS, juntamente com uma interface C#.

Há vários pacotes do Braze Unity disponíveis para baixar na [página de lançamentos do Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases):
 
- `Appboy.unitypackage`
    - Esse pacote reúne os SDKs do Braze para Android e iOS e a dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para o SDK do iOS, que é necessária para a funcionalidade adequada dos recursos de envio de mensagens no app e cartões de conteúdo do Braze no iOS. O framework SDWebImage é usado para baixar e exibir imagens, inclusive GIFs. Se você pretende utilizar toda a funcionalidade da Braze, baixe e importe esse pacote.
- `Appboy-nodeps.unitypackage`
    - Esse pacote é semelhante a `Appboy.unitypackage`, exceto pelo fato de que o framework [SDWebImage](https://github.com/SDWebImage/SDWebImage) não está presente. Esse pacote é útil se você não quiser que o framework SDWebImage esteja presente em seu app para iOS.

**iOS**: Para ver se você precisa da dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para seu projeto iOS, visite a [documentação da mensagem no app do iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).<br>
**Android**: A partir do Unity 2.6.0, o artefato agrupado do Braze Android SDK requer dependências do [AndroidX](https://developer.android.com/jetpack/androidx). Se você estava usando um `jetified unitypackage`, faça a transição com segurança para o `unitypackage` correspondente.

## Etapa 2: Importar o pacote

No Unity Editor, importe o pacote em seu projeto Unity navegando até **Assets > Import Package > Custom Package** (Ativos > Importar pacote > Pacote personalizado). Em seguida, clique em **Importar**.

Como alternativa, siga as instruções de [importação de pacotes de ativos do Unity](https://docs.unity3d.com/Manual/AssetPackages.html) para obter mais detalhes sobre a importação de pacotes personalizados do Unity. 

{% alert note %}
Para importar apenas o plug-in para iOS ou Android, desmarque o subdiretório `Plugins/Android` ou `Plugins/iOS` ao importar o `.unitypackage` da Braze.
{% endalert %}

## Etapa 3: Atualização de seu AndroidManifest.xml

Os projetos do Unity para Android precisam de um [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) para executar o app. Além disso, a Braze requer várias adições ao seu [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html) para funcionar.

### Configuração do AndroidManifest.xml

Se o seu app não tiver um `AndroidManifest.xml`, você poderá usar o seguinte modelo. Caso contrário, se você já tiver um `AndroidManifest.xml`, confira se falta alguma das seções a seguir e adicione-as ao seu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
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

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> Seu `AndroidManifest.xml` deve existir em `Assets/Plugins/Android/AndroidManifest.xml`. Para saber mais, consulte a [documentação do AndroidManifest para Unity](https://docs.unity3d.com/Manual/android-manifest.html).

> Todas as classes de atividades registradas no seu arquivo `AndroidManifest.xml` devem ser totalmente integradas ao Braze Android SDK. Se você adicionar sua própria classe de atividade, siga as [instruções de integração de atividades do Unity](#extending-braze-unity-player) para garantir que as análises de dados estejam sendo coletadas.

{% alert note %}
Seu `AndroidManifest.xml` final deve conter apenas uma única atividade com o `"android.intent.category.LAUNCHER"` presente.
{% endalert %}

### Atualize o endereço AndroidManifest.xml com o nome do seu pacote

Para encontrar o nome do pacote, clique em **File > Build Settings > Player Settings > guia Android** (Arquivo > Configurações da versão > Configurações do player > guia Android).
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

Em seu `AndroidManifest.xml`, todas as instâncias de `REPLACE_WITH_YOUR_PACKAGE_NAME` devem ser substituídas pelo `Package Name` da etapa anterior.

## Etapa 4: Adicionar dependências do gradle {#unity-android-gradle-configuration}

Para adicionar dependências do Gradle ao seu projeto Unity, primeiro ative a opção ["Custom Main Gradle Template"](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) em suas configurações de publicação. Isso criará um arquivo gradle modelo que será usado em seu projeto. Um arquivo gradle lida com as dependências de configuração e outras configurações de projeto durante o desenvolvimento. Para saber mais, consulte o aplicativo de amostra do Braze Unity [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

As seguintes dependências são necessárias:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

Você também pode definir essas dependências usando o [External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver).

## Etapa 5: Configurar o SDK {#unity-static-configuration}

A Braze oferece uma solução nativa do Unity para automatizar a integração do Unity com o Android. 

1. No Unity Editor, abra as configurações da Braze em **Braze > Braze Configuration** (Braze > Configuração da Braze).
2. Marque a caixa **Automate Unity Android Integration (Automatizar a integração do Unity com o Android** ).
3. No campo **Braze API Key (Chave de API do Braze** ), insira a chave de API de seu aplicativo encontrada em **Manage Settings (Gerenciar configurações)** no dashboard do Braze.

{% alert note %}
Essa integração automática não deve ser usada com um arquivo `braze.xml` criado manualmente, pois os valores de configuração podem entrar em conflito durante a criação do projeto. Se precisar de um `braze.xml` manual, desative a integração automática.
{% endalert %}

## Integração básica de SDK concluída

Agora, a Braze deve estar coletando dados do seu app, e sua integração básica deve estar concluída. Para saber mais sobre o push de integração, consulte os artigos a seguir: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) e [cartões de conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Para saber mais sobre as opções avançadas de integração de SDK, consulte [Implementação avançada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced).

