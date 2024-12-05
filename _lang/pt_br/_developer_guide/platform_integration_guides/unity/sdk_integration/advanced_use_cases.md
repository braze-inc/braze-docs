---
nav_title: Implementação avançada
article_title: Implementação avançada do SDK
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Este artigo de referência aborda a implementação avançada do SDK para a plataforma Unity."
---

# Implementação avançada

> Este artigo de referência aborda a implementação avançada do SDK para a plataforma Unity.

## Personalização do pacote Unity

Você pode optar por personalizar e exportar o pacote Braze Unity usando os scripts fornecidos.

1. Clone o [projeto GitHub do Braze Unity SDK](https://github.com/appboy/appboy-unity-sdk):

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. No diretório `braze-unity-sdk/scripts`, execute `./generate_package.sh` para exportar os pacotes do Unity. O Unity deve estar aberto durante a execução do `generate_package.sh`.
3. Os pacotes serão exportados para `braze-unity-sdk/unity-package/`.
4. No Unity Editor, importe o pacote desejado em seu projeto Unity navegando até **Ativos** > **Importar pacote > **Pacote personalizado**.
5. (opcional) Desmarque os arquivos que não deseja importar.

Você pode personalizar o pacote Unity exportado editando o site `generate_package.sh` e o script de exportação localizado em `Assets/Editor/Build.cs`.

## Compatibilidade com o Prime 31

Para usar o plug-in Braze Unity com os plug-ins Prime31, edite o site `AndroidManifest.xml` de seu projeto para usar as classes Activity compatíveis com o Prime31. Altere todas as referências de
de `com.braze.unity.BrazeUnityPlayerActivity` a `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Amazon ADM push

A Braze oferece suporte à integração do [Amazon ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) em apps Unity. Se quiser integrar o Amazon ADM push, crie um arquivo chamado `api_key.txt` contendo sua chave de API do ADM e coloque-o na pasta `Plugins/Android/assets/`.  Para saber mais sobre a integração do Amazon ADM com a Braze, acesse nossas [instruções de integração do ADM push]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Opções avançadas de implementação do Android SDK {#android-sdk-advanced}

### Ativação do registro detalhado no Unity Editor
Para ativar o registro detalhado no Unity Editor, faça o seguinte:

1. Abra Configurações da Braze navegando até **Braze** > **Configuração da Braze**.
2. Clique no menu suspenso **Show Braze Android Settings (Mostrar configurações do Android Braze** ).
3. No campo **Nível de registro do SDK**, insira o valor "0".

### Extensão do reprodutor do Braze Unity (Android) {#extending-braze-unity-player}

O arquivo de exemplo `AndroidManifest.xml` fornecido tem uma classe Activity registrada, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Essa classe é integrada ao SDK da Braze e estende o site `UnityPlayerActivity` com manipulação de sessão, registro de mensagens no app, registro de análise de dados de notificação por push e muito mais. Para saber mais sobre como estender a classe `UnityPlayerActivity`, consulte [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html).

Se estiver criando seu próprio `UnityPlayerActivity` personalizado em uma biblioteca ou projeto de plug-in, será necessário estender nosso `BrazeUnityPlayerActivity` para integrar sua funcionalidade personalizada ao Braze. Antes de começar a trabalhar na extensão do site `BrazeUnityPlayerActivity`, siga nossas instruções para integrar a Braze em seu projeto Unity.
1. Adicione o Braze Android SDK como uma dependência de sua biblioteca ou projeto de plug-in, conforme descrito nas [instruções de integração do Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Integre nosso Unity `.aar`, que contém nossa funcionalidade específica do Unity, ao seu projeto de biblioteca Android que está sendo desenvolvido para o Unity. O site `appboy-unity.aar` está disponível em nosso [repositório público](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Depois que nossa biblioteca Unity for integrada com sucesso, modifique seu site `UnityPlayerActivity` para estender o `BrazeUnityPlayerActivity`.
3. Exporte sua biblioteca ou projeto de plug-in e solte-o em `/<your-project>/Assets/Plugins/Android` normalmente. Não inclua nenhum código-fonte da Braze em sua biblioteca ou plug-in, pois eles já estarão presentes em `/<your-project>/Assets/Plugins/Android`.
4. Edite o site `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` para especificar a subclasse `BrazeUnityPlayerActivity` como a atividade principal.

Agora, você poderá empacotar um `.apk` do Unity IDE totalmente integrado à Braze e que contenha sua funcionalidade personalizada do `UnityPlayerActivity`.

## Opções de implementação avançada do SDK do iOS {#ios-sdk-advanced}

### Ativação do registro detalhado no Unity Editor
Para ativar o registro detalhado no Unity Editor, faça o seguinte:

1. Abra Configurações da Braze navegando até **Braze** > **Configuração da Braze**.
2. Clique no menu suspenso **Mostrar configurações do Braze iOS**.
3. No campo **Nível de registro do SDK**, insira o valor "0".

### Extensão do SDK (iOS)

Para estender os comportamentos do SDK, crie um fork do [projeto Braze Unity SDK no GitHub](https://github.com/appboy/appboy-unity-sdk) e faça as alterações necessárias.

Para publicar seu código modificado como um pacote Unity, consulte nossos [casos de uso avançados]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/).

### Transição da integração manual para a automatizada (iOS)

Para aproveitar a integração automatizada do iOS oferecida no SDK do Braze Unity, siga estas etapas para fazer a transição de uma integração manual para uma automatizada.

1. Remova todo o código relacionado à Braze da subclasse `UnityAppController` de seu projeto do Xcode.
2. Remova as bibliotecas do Braze iOS de seu projeto Unity ou Xcode (como `Appboy_iOS_SDK.framework` e `SDWebImage.framework`) e [importe o pacote Braze Unity](#step-1-importing-the-braze-unity-package) para seu projeto Unity.
3. Siga as instruções de integração para [definir sua chave de API por meio do Unity](#step-2-setting-your-api-key).

