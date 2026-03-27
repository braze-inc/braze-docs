---
nav_title: Referências e apps de exemplo
article_title: "Referências, repositórios e apps de exemplo do Braze SDK"
page_order: 5.5
description: "Esta é uma lista de documentação de referência, repositórios GitHub e apps de exemplo pertencentes a cada SDK da Braze."
toc_headers: h2
---

# Referências, repositórios e apps de exemplo

> Esta é uma lista de documentação de referência, repositórios GitHub e apps de exemplo pertencentes a cada SDK da Braze. A documentação de referência de um SDK detalha suas classes, tipos, funções e variáveis disponíveis. O repositório GitHub fornece insight sobre as declarações de funções e atributos desse SDK, alterações de código e controle de versão. Cada repositório também inclui aplicativos de exemplo totalmente compiláveis que você pode usar para testar os recursos da Braze ou implementar junto com seus próprios aplicativos.

## Lista de recursos

{% alert note %}
Atualmente, alguns SDKs não possuem documentação de referência dedicada, mas estamos trabalhando ativamente nisso.
{% endalert %}

| Plataforma          | Referência                                                                                                                                    | Repositório                                                                 | App de exemplo                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [Documentação de referência](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [Repositório GitHub](https://github.com/braze-inc/braze-android-sdk)      | [App de exemplo](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [Documentação de referência](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [Repositório GitHub](https://github.com/braze-inc/braze-swift-sdk)            | [App de exemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [Documentação de referência](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [Repositório GitHub](https://github.com/braze-inc/braze-web-sdk)              | [App de exemplo](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [Arquivo de declaração](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [Repositório GitHub](https://github.com/braze-inc/braze-cordova-sdk)      | [App de exemplo](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [Documentação de referência](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [Repositório GitHub](https://github.com/braze-inc/braze-flutter-sdk)      | [App de exemplo](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Arquivo de declaração](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [Repositório GitHub](https://github.com/braze-inc/braze-react-native-sdk) | [App de exemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | N/D                                                                                                                                                         | [Repositório GitHub](https://github.com/braze-inc/braze-roku-sdk)            | [App de exemplo](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [Arquivo de declaração](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [Repositório GitHub](https://github.com/braze-inc/braze-unity-sdk)          | [App de exemplo](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| SDK .NET MAUI (anteriormente Xamarin)      | N/D                                                                                                                                                         | [Repositório GitHub](https://github.com/braze-inc/braze-xamarin-sdk)      | [App de exemplo](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Criando um app de exemplo

{% tabs %}
{% tab android %}
### Compilando o "Droidboy"

Nosso aplicativo de teste no [repositório GitHub do Android SDK](https://github.com/braze-inc/braze-android-sdk) é chamado Droidboy. Siga estas instruções para criar uma cópia totalmente funcional dele junto com seu projeto.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) e anote a chave de identificação da API da Braze.<br><br>
2. Copie seu ID de remetente FCM e a chave de identificação da API da Braze nos locais apropriados em `/droidboy/res/values/braze.xml` (entre as tags das strings denominadas `com_braze_push_fcm_sender_id` e `com_braze_api_key`, respectivamente).<br><br>
3. Copie a chave do servidor FCM e o ID do servidor nas configurações do espaço de trabalho em **Gerenciar Configurações**.<br><br>
4. Para montar o APK do Droidboy, execute `./gradlew assemble` no diretório do SDK. Use `gradlew.bat` no Windows.<br><br>
5. Para instalar automaticamente o APK do Droidboy em um dispositivo de teste, execute `./gradlew installDebug` no diretório do SDK:

### Compilando o "Hello Braze"

O aplicativo de teste Hello Braze mostra um caso de uso mínimo do SDK da Braze e também demonstra como integrar facilmente o SDK da Braze em um projeto Gradle.

1. Copie sua chave de identificador de API da página **Manage Settings** no seu arquivo `braze.xml` na pasta `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar o app de exemplo em um dispositivo ou emulador, execute o seguinte comando no diretório do SDK:
```
./gradlew installDebug
```
Se você não tiver a variável `ANDROID_HOME` definida corretamente ou não tiver uma pasta `local.properties` com uma pasta `sdk.dir` válida, esse plug-in também instalará o SDK básico para você. Consulte o [repositório do plug-in](https://github.com/JakeWharton/sdk-manager-plugin) para mais informações.

Para saber mais sobre o sistema de compilação do Android SDK, consulte o [README do repositório GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Compilando apps de teste Swift

Siga estas instruções para compilar e executar nossos aplicativos de teste.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) e anote a chave de API do identificador do app e o endpoint.
2. Com base no seu método de integração (Swift Package Manager, CocoaPods, Manual), selecione o arquivo `xcodeproj` apropriado para abrir.
3. Insira sua chave de API e seu endpoint no campo apropriado no arquivo `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Ao realizar o controle de qualidade da sua integração de SDK, use o [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado no seu app.
{% endalert %}