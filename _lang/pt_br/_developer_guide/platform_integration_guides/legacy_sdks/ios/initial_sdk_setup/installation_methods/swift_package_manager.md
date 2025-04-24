---
nav_title: Swift Package Manager
article_title: Integração do Swift Package Manager para iOS
platform: iOS
page_order: 3
description: "Este tutorial cobre a instalação do Braze SDK usando o Swift Package Manager para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# integração do Swift Package Manager

Instalar o iOS SDK via [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatiza a maior parte do processo de instalação para você. Antes de começar este processo, certifique-se de usar o Xcode 12 ou superior.

{% alert note %}
tvOS não está disponível atualmente via Swift Package Manager.
{% endalert %}

## Etapa 1: Adicionando a dependência ao seu projeto

### Importar versão do SDK

Abra seu projeto e navegue até as configurações do seu projeto. Selecione a guia **SWIFT Packages** e clique no botão adicionar <i class="fas fa-plus"></i> abaixo da lista de pacotes.

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Ao importar a versão `3.33.1` do SDK ou posterior, insira a URL do nosso repositório de SDK para iOS (`https://github.com/braze-inc/braze-ios-sdk`) no campo de texto e clique em **Avançar**. 

Para versões `3.29.0` até `3.32.0`, use o URL `https://github.com/Appboy/Appboy-ios-sdk`.

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

Na próxima tela, selecione a versão do SDK e clique em **Avançar**. As versões `3.29.0` e posteriores são compatíveis com o Swift Package Manager.

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### Selecionar pacotes

Selecione o pacote que melhor atende às suas necessidades e clique em **Concluir**. Certifique-se de selecionar `AppboyKit` ou `AppboyUI`. Incluir ambos os pacotes pode levar a um comportamento indesejado:

- `AppboyUI`
  - Mais adequado se você planeja usar os componentes de UI fornecidos pela Braze.
  - Inclui `AppboyKit` automaticamente.
- `AppboyKit`
  - Mais adequado se você não precisar usar nenhum dos componentes de interface do usuário fornecidos pela Braze (por exemplo, Cartões de Conteúdo, mensagens no app, etc.).
- `AppboyPushStory`
  - Inclua este pacote se você integrou Push Stories no seu app. Isso é suportado a partir da versão `3.31.0`.
  - No menu suspenso em `Add to Target`, selecione seu alvo `ContentExtension` em vez do alvo do seu app principal. 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## Etapa 2: Configurando seu projeto

Em seguida, navegue até as **configurações de build** do seu projeto e adicione a flag `-ObjC` à configuração **Outras Flags do Linker**. Esta bandeira deve ser adicionada e quaisquer [erros](https://developer.apple.com/library/archive/qa/qa1490/_index.html) resolvidos para integrar ainda mais o SDK.

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Se você não adicionar a flag `-ObjC`, partes da API podem ficar ausentes e o comportamento será indefinido. Você pode encontrar erros inesperados, como "seletor não reconhecido enviado para a classe", falhas no aplicativo e outros problemas.
{% endalert %}

## Etapa 3: Editando o esquema do alvo
{% alert important %}
Se você estiver usando o Xcode 12.5 ou mais recente, pule esta etapa.
{% endalert %}

Se você estiver usando o Xcode 12.4 ou anterior, edite o esquema do alvo incluindo o pacote Appboy (**Produto > Esquema > Editar Esquema** item do menu):
1. Expanda o menu **Build** e selecione **Post-actions**. Pressione o botão de mais (+) e selecione **Nova Ação de Execução de Script**.
2. No menu suspenso **Provide build settings from**, selecione o alvo do seu app.
3.  Copie este script no campo aberto:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Próximos passos

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

