---
nav_title: Exemplos de aplicativos
article_title: Exemplos de apps para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 10
description: "Este artigo de referência aborda como usar os apps de amostra do Android."

---

# Exemplos de aplicativos

> Os SDKs da Braze vêm com um aplicativo de amostra no repositório para sua conveniência. Cada um desses apps é totalmente compilável para que você possa testar os recursos da Braze e implementá-los em seus próprios aplicativos. 

Testar o comportamento em seu próprio aplicativo em comparação com o comportamento esperado e as jornadas de código nos aplicativos de amostra é uma excelente maneira de depurar quaisquer problemas que possa encontrar.

## Criação do aplicativo de teste Droidboy
Nosso aplicativo de teste no [repositório do GitHub do](https://github.com/braze-inc/braze-android-sdk "Android SDKBrazeAndroid GitHub Repository") é chamado Droidboy. Siga estas instruções para criar uma cópia totalmente funcional dela em seu projeto.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) e note a chave de identificação da API do Braze.<br><br>
2. Copie seu ID de remetente FCM e a chave de identificação da API do Braze nos locais apropriados em `/droidboy/res/values/braze.xml` (entre as tags das strings denominadas `com_braze_push_fcm_sender_id` e `com_braze_api_key`, respectivamente).<br><br>
3. Copie a chave do servidor FCM e o ID do servidor nas configurações do espaço de trabalho em **Gerenciar configurações**.<br><br>
4. Para montar o APK do Droidboy, execute `./gradlew assemble` no diretório do SDK. Use `gradlew.bat` no Windows.<br><br>
5. Para instalar automaticamente o APK do Droidboy em um dispositivo de teste, execute `./gradlew installDebug` no diretório do SDK:

## Criação do aplicativo de teste Hello Braze
O aplicativo de teste Hello Braze mostra um caso de uso mínimo do SDK da Braze e, além disso, mostra como integrar facilmente o SDK da Braze em um projeto Gradle.

1. Copie sua chave de identificador de API da página **Manage Settings** em seu arquivo `braze.xml` na pasta `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Para instalar o app de amostra em um dispositivo ou emulador, execute o seguinte comando no diretório do SDK:
```
./gradlew installDebug
```
Se você não tiver a variável `ANDROID_HOME` definida corretamente ou não tiver uma pasta `local.properties` com uma pasta `sdk.dir` válida, esse plug-in também instalará o SDK básico para você. Consulte o [repositório de plug-ins](https://github.com/JakeWharton/sdk-manager-plugin) para obter mais informações.

Para saber mais sobre o sistema de compilação do Android SDK, consulte o [LEIAME do repositório do GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).

