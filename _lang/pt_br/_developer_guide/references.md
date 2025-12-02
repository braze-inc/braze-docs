---
nav_title: Referências e aplicativos de amostra
article_title: "Referências, repositórios e aplicativos de amostra do Braze SDK"
page_order: 5.5
description: "Esta é uma lista da documentação de referência, dos repositórios do GitHub e dos apps de amostra pertencentes a cada SDK do Braze."
toc_headers: h2
---

# Referências, repositórios e aplicativos de amostra

> Esta é uma lista da documentação de referência, dos repositórios do GitHub e dos apps de amostra pertencentes a cada SDK do Braze. A documentação de referência de um SDK detalha suas classes, tipos, funções e variáveis disponíveis. Enquanto o repositório do GitHub fornece insight sobre as declarações de função e atribuição do SDK, alterações de código e controle de versão. Cada repositório também inclui aplicativos de amostra totalmente compiláveis que você pode usar para testar os recursos do Braze ou implementar junto com seus próprios aplicativos.

## Lista de recursos

{% alert note %}
Atualmente, alguns SDKs não têm documentação de referência dedicada, mas estamos trabalhando ativamente nisso.
{% endalert %}

| Plataforma          | Referência                                                                                                                                    | Repositório                                                                 | App de amostra                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [Documentação de referência](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [Repositório do GitHub](https://github.com/braze-inc/braze-android-sdk)      | [App de amostra](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| SWIFT SDK         | [Documentação de referência](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [Repositório do GitHub](https://github.com/braze-inc/braze-swift-sdk)            | [App de amostra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| SDK da Web           | [Documentação de referência](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [Repositório do GitHub](https://github.com/braze-inc/braze-web-sdk)              | [App de amostra](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [Arquivo de declaração](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [Repositório do GitHub](https://github.com/braze-inc/braze-cordova-sdk)      | [App de amostra](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| SDK para Flutter       | [Documentação de referência](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [Repositório do GitHub](https://github.com/braze-inc/braze-flutter-sdk)      | [App de amostra](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Arquivo de declaração](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [Repositório do GitHub](https://github.com/braze-inc/braze-react-native-sdk) | [App de amostra](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | N/D                                                                                                                                                         | [Repositório do GitHub](https://github.com/braze-inc/braze-roku-sdk)            | [App de amostra](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [Arquivo de declaração](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [Repositório do GitHub](https://github.com/braze-inc/braze-unity-sdk)          | [App de amostra](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| SDK do Unreal Engine | N/D                                                                                                                                                         | [Repositório do GitHub](https://github.com/braze-inc/braze-unreal-sdk)        | [App de amostra](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK       | N/D                                                                                                                                                         | [Repositório do GitHub](https://github.com/braze-inc/braze-xamarin-sdk)      | [App de amostra](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Criação de um aplicativo de amostra

{% tabs %}
{% tab Android %}
### Criação do "Droidboy"

Nosso aplicativo de teste no [repositório do Android SDK GitHub](https://github.com/braze-inc/braze-android-sdk) é chamado Droidboy. Siga estas instruções para criar uma cópia totalmente funcional dela em seu projeto.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) e note a chave de identificação da API do Braze.<br><br>
2. Copie seu ID de remetente FCM e a chave de identificação da API do Braze nos locais apropriados em `/droidboy/res/values/braze.xml` (entre as tags das strings denominadas `com_braze_push_fcm_sender_id` e `com_braze_api_key`, respectivamente).<br><br>
3. Copie a chave do servidor FCM e o ID do servidor nas configurações do espaço de trabalho em **Gerenciar configurações**.<br><br>
4. Para montar o APK do Droidboy, execute `./gradlew assemble` no diretório do SDK. Use `gradlew.bat` no Windows.<br><br>
5. Para instalar automaticamente o APK do Droidboy em um dispositivo de teste, execute `./gradlew installDebug` no diretório do SDK:

### Construindo "Hello Braze" (Olá, Braze)

O aplicativo de teste Hello Braze mostra um caso de uso mínimo do SDK da Braze e, além disso, mostra como integrar facilmente o SDK da Braze em um projeto Gradle.

1. Copie sua chave de identificador de API da página **Manage Settings** em seu arquivo `braze.xml` na pasta `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar o app de amostra em um dispositivo ou emulador, execute o seguinte comando no diretório do SDK:
```
./gradlew installDebug
```
Se você não tiver a variável `ANDROID_HOME` definida corretamente ou não tiver uma pasta `local.properties` com uma pasta `sdk.dir` válida, esse plug-in também instalará o SDK básico para você. Consulte o [repositório de plug-ins](https://github.com/JakeWharton/sdk-manager-plugin) para obter mais informações.

Para saber mais sobre o sistema de compilação do Android SDK, consulte o [LEIAME do repositório do GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Criação de apps de teste Swift

Siga estas instruções para criar e executar nossos aplicativos de teste.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) e note a chave de API do identificador do app e o ponto de extremidade.
2. Com base em seu método de integração (Swift Package Manager, CocoaPods, Manual), selecione o arquivo `xcodeproj` apropriado para abrir.
3. Coloque sua chave de API e seu endpoint no campo apropriado no arquivo `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Ao realizar o controle de qualidade na integração do SDK, use o [depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado do seu aplicativo.
{% endalert %}
