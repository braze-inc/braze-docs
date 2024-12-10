---
nav_title: Manual
article_title: Opções de Integração Manual para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência mostra como integrar manualmente o SDK da Braze para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração manual

{% alert tip %}
Recomendamos fortemente que você implemente o SDK por meio de um gerenciador de pacotes, como [Swift Package Manager](../swift_package_manager/), [CocoaPods](../cocoapods/) ou [Carthage](../carthage_integration/). Isso vai te poupar muito tempo e automatizar grande parte do processo. No entanto, se não conseguir fazer isso, conclua a integração manualmente seguindo as instruções.
{% endalert %}

## Etapa 1: Download do SDK da Braze

### Opção 1: XCFramework Dinâmico

1. Baixe `Appboy_iOS_SDK.xcframework.zip` da [página de versão](https://github.com/appboy/appboy-ios-sdk/releases) e extraia o arquivo.
2. No Xcode, arraste e solte este `.xcframework` no seu projeto.
3. Na guia **Geral** do projeto, selecione **Incorporar e Assinar** para `Appboy_iOS_SDK.xcframework`.

### Opção 2: XCFramework estática para integração estática

1. Baixe `Appboy_iOS_SDK.zip` da [página de versão](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. No Xcode, no navegador do projeto, selecione o projeto ou grupo de destino para Braze<br><br>
3. Acesse **Arquivo > Adicionar Arquivos > Nome_Projeto**.<br><br>
4. Adicione as pastas `AppboyKit` e `AppboyUI` ao seu projeto como um grupo.
	- Certifique-se de que a opção **Copiar itens para a pasta do grupo de destino** esteja selecionada se você estiver integrando pela primeira vez. Expandir **Opções** no seletor de arquivos para selecionar **Copiar itens, se necessário** e **Criar grupos**.
	- Exclua os diretórios `AppboyKit/include` e `AppboyUI/include`.<br><br>
5. (Opcional) Se um dos seguintes se aplicar a você:
  - Você só quer os principais recursos de análise de dados do SDK e não usa nenhum recurso de interface do usuário (por exemplo, mensagens no app ou Cartões de Conteúdo).
  - Você tem uma interface de usuário personalizada para os recursos da interface de usuário do Braze e lida com o download de imagens por conta própria.<br><br>Você pode usar a versão principal do SDK removendo o arquivo `ABKSDWebImageProxy.m` e `Appboy.bundle`. Isso removerá a dependência do framework `SDWebImage` e todos os recursos relacionados à interface do usuário (por exemplo, arquivos Nib, imagens, arquivos de localização) do SDK.

{% alert warning %}
Se você tentar usar a versão principal do SDK sem os recursos de UI da Braze, as mensagens no app não serão exibidas. Tentar exibir o UI de cartões de conteúdo da Braze com a versão principal levará a um comportamento imprevisível.
{% endalert %}

## Etapa 2: Adicionando bibliotecas iOS necessárias

1. Clique no alvo para o seu projeto (usando a navegação à esquerda) e selecione a **Fases de Build** guia.<br><br>
2. Clique no botão <i class="fas fa-plus"></i> em **Link Binary With Libraries**.<br><br>
3. No menu, selecione `SystemConfiguration.framework`.<br><br>
4. Marque esta biblioteca como obrigatória usando o menu suspenso ao lado de `SystemConfiguration.framework`.<br><br>
5. Repita para adicionar cada um dos seguintes frameworks necessários ao seu projeto, marcando cada um como "obrigatório".
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Adicione os seguintes frameworks e marque-os como opcionais:
	- `CoreTelephony.framework`<br><br>
7. Selecione a guia **Configurações de Build**. Na seção **Linking**, localize a configuração **Other Linker Flags** e adicione a flag `-ObjC`.<br><br>
8. O `SDWebImage` framework é necessário para que os cartões de conteúdo e o envio de mensagens no app funcionem corretamente. `SDWebImage` é usado para download e exibição de imagens, incluindo GIFs. Se você pretende usar Cartões de Conteúdo ou mensagens no app, siga as etapas de integração do SDWebImage.

### integração SDWebImage

Para instalar `SDWebImage`, siga as [instruções](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) e depois arraste e solte o `XCFramework` resultante em seu projeto.

### Monitoramento de localização opcional

1. Adicione o `CoreLocation.framework` para ativar o monitoramento de localização.
2. Você deve autorizar local para seus usuários usando `CLLocationManager` no seu app.

## Etapa 3: Cabeçalho de ponte Objective-C

{% alert note %}
Se o seu projeto usa apenas Objective-C, pule esta etapa.
{% endalert %}

Se o seu projeto usa Swift, você precisará de um arquivo de cabeçalho de ponte.

Se você não tiver um arquivo de cabeçalho de ponte, crie um e nomeie-o `your-product-module-name-Bridging-Header.h` escolhendo **Arquivo > Novo > Arquivo > (iOS ou OS X) > Fonte > Arquivo de Cabeçalho**. Em seguida, adicione a seguinte linha de código ao topo do seu arquivo de cabeçalho de ponte:
```
#import "AppboyKit.h"
```

Nas **Configurações de Build** do seu projeto, adicione a jornada relativa do seu arquivo de cabeçalho à configuração de compilação `Objective-C Bridging Header` em `Swift Compiler - Code Generation`.

## Próximas etapas

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
