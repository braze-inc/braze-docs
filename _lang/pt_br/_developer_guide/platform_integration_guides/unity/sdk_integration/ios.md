---
nav_title: iOS
article_title: Integração do SDK iOS para Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "Este artigo de referência aborda a integração do iOS SDK para a plataforma Unity."
search_rank: .9
---

# integração do SDK iOS

> Este artigo de referência aborda a integração do iOS SDK para a plataforma Unity. Siga estas instruções para executar a Braze em seu app Unity. 

Se você está fazendo a transição de uma integração manual, leia as instruções em [Transição para uma integração automatizada](#transitioning-from-manual-to-automated-integration-ios).

## Etapa 1: Escolha seu pacote Braze Unity

O [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) da Braze agrupa associações nativas para as plataformas Android e iOS, juntamente com uma interface C#.

O pacote Braze Unity está disponível para download na [página de lançamentos do Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) com duas opções de integração:

1. Apenas `Appboy.unitypackage`
  - Este pacote inclui os SDKs da Braze para Android e iOS sem nenhuma outra dependência. Com este método de integração, não haverá funcionalidade adequada do envio de mensagens in-app da Braze e dos recursos de Content Cards no iOS. Se você pretende utilizar a funcionalidade completa do Braze sem código personalizado, use a opção abaixo.
  - Para usar essa opção de integração, *desmarque* a opção `Import SDWebImage dependency` na interface do Unity em "Braze Configuration" (Configuração da Braze).
2. `Appboy.unitypackage` com `SDWebImage`
  - Essa opção de integração agrupa os SDKs da Braze para Android e iOS e a dependência [SDWebImage](https://github.com/SDWebImage/SDWebImage) para o SDK iOS, que é necessária para o funcionamento adequado do envio de mensagens no app da Braze e dos recursos de cartões de conteúdo no iOS. O framework `SDWebImage` é usado para baixar e exibir imagens, inclusive GIFs. Se você pretende utilizar toda a funcionalidade da Braze, baixe e importe esse pacote.
  - Para importar automaticamente `SDWebImage`, *marque* a opção `Import SDWebImage dependency` na interface do Unity em "Braze Configuration" (Configuração da Braze).

**iOS**: Para ver se você precisa da [SDWebImage](https://github.com/SDWebImage/SDWebImage) dependência para o seu projeto iOS, visite a [documentação de mensagem no app iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: A partir do Unity 2.6.0, o artefato agrupado do Braze Android SDK requer dependências do [AndroidX](https://developer.android.com/jetpack/androidx). Se você estava usando um `jetified unitypackage`, faça a transição com segurança para o `unitypackage` correspondente.

## Etapa 2: Importar o pacote

No Unity Editor, importe o pacote em seu projeto Unity navegando até **Assets > Import Package > Custom Package** (Ativos > Importar pacote > Pacote personalizado). Em seguida, clique em **Importar**.

Como alternativa, siga as instruções de [importação de pacotes de ativos do Unity](https://docs.unity3d.com/Manual/AssetPackages.html) para obter mais detalhes sobre a importação de pacotes personalizados do Unity. 

{% alert note %}
Para importar apenas o plug-in para iOS ou Android, desmarque o subdiretório `Plugins/Android` ou `Plugins/iOS` ao importar o `.unitypackage` da Braze.
{% endalert %}

## Etapa 3: Defina sua chave de API

A Braze oferece uma solução nativa do Unity para automatizar a integração do Unity com o iOS. Essa solução modifica o projeto do Xcode usando o [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) e as subclasses `UnityAppController` do Unity que utilizam a macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. No Unity Editor, abra as configurações da Braze em **Braze > Braze Configuration** (Braze > Configuração da Braze).
2. Marque a opção **Automate Unity iOS Integration** (Automatizar a integração do Unity com iOS).
3. No campo **Braze API Key** (Chave da API da Braze), insira a chave de API do seu app que está disponível em **Gerenciar configurações**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Se o seu app já estiver usando outra subclasse `UnityAppController`, será necessário mesclar a implementação da sua subclasse com `AppboyAppDelegate.mm`.

## Integração básica de SDK completa

Agora, a Braze está coletando dados do seu app e sua integração básica está concluída. Para saber mais sobre o push de integração, consulte os artigos a seguir: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/), e [Cartões de Conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Para saber mais sobre as opções avançadas de integração de SDK, consulte [Implementação avançada]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced).

