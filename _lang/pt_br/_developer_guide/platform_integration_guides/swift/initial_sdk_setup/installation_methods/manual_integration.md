---
nav_title: Integração Manual
article_title: Integração Manual para iOS
platform: Swift
page_order: 3
description: "Este artigo de referência mostra como integrar o SDK Braze SWIFT usando a instalação manual."
toc_headers: "h2"
---

# Integração manual

> Se você não tiver acesso a um gerenciador de pacotes, como [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) ou [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/), você pode integrar manualmente o SDK SWIFT.

## Etapa 1: Baixar o SDK da Braze

Acessar a [página de lançamento do SDK da Braze no GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), então baixar `braze-swift-sdk-prebuilt.zip`.

!["A página de lançamento do SDK da Braze no GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Etapa 2: Escolha seus frameworks

O SDK Braze SWIFT contém uma variedade de XCFrameworks independentes, o que lhe dá a liberdade de integrar os recursos que você deseja—sem precisar integrá-los todos. Consulte a tabela a seguir para escolher seus XCFrameworks:

| Pacote                    | Necessário? | Descrição                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Sim       | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push.                                                                                                                                                                                                                                             |
| `BrazeLocation`            | Não        | Biblioteca de local que fornece suporte para análise de dados de local e monitoramento de geofence.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | Não        | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app e Cartões de Conteúdo.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | Não        | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. Não adicione esta biblioteca diretamente ao seu alvo principal do aplicativo, em vez disso [adicione a biblioteca `BrazeNotificationService` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).     |
| `BrazePushStory`           | Não        | Biblioteca de extensão de conteúdo de notificação que fornece suporte para Push Stories. Não adicione esta biblioteca diretamente ao seu alvo principal do aplicativo, em vez disso [adicione a biblioteca `BrazePushStory` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                     |
| `BrazeKitCompat`           | Não        | Biblioteca de compatibilidade contendo todas as classes e métodos `Appboy` e `ABK*` que estavam disponíveis na versão `Appboy-iOS-SDK` 4.X.X. Para obter mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | Não        | Biblioteca de compatibilidade contendo todas as `ABK*` classes e métodos que estavam disponíveis na biblioteca `AppboyUI` da versão `Appboy-iOS-SDK` 4.X.X. Para obter mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Não        | Dependência usada apenas por `BrazeUICompat` no cenário de migração mínima. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Etapa 3: Prepare seus arquivos

Decida se você quer usar **Estático** ou **Dinâmico** XCFrameworks, então prepare seus arquivos:

{% tabs %}
{% tab dinâmico %}
1. Crie um diretório temporário para seus XCFrameworks.
2. No `braze-swift-sdk-prebuilt`, abra o diretório `dynamic` e mova `BrazeKit.xcframework` para o seu diretório. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Mova cada um dos seus [XCFrameworks escolhidos](#step-2-choose-your-frameworks) para o seu diretório temporário. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab static %}
### Etapa 3.1: Prepare seus frameworks

1. Crie um diretório temporário para seus XCFrameworks.
2. No `braze-swift-sdk-prebuilt`, abra o diretório `static` e mova `BrazeKit.xcframework` para o seu diretório. Seu diretório deve ser semelhante ao seguinte:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. Mova cada um dos seus [XCFrameworks escolhidos](#step-2-choose-your-frameworks) para o seu diretório temporário. Seu diretório deve ser semelhante ao seguinte:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### Etapa 3.2: Prepare seus pacotes

1. Crie um diretório temporário para seus pacotes.
2. Abra o `bundles` diretório e mova `BrazeKit.bundle` para o seu diretório. Seu diretório deve ser semelhante ao seguinte:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. Se você estiver usando os `BrazeLocation`, `BrazeUI`, `BrazeUICompat` ou `SDWebImage` XCFrameworks, mova seus pacotes correspondentes para o seu diretório temporário. Seu diretório deve ser semelhante ao seguinte:
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
Apenas mova os pacotes para os [frameworks que você preparou](#step-31-prepare-your-frameworks).
{% endalert %}
{% endtab %}
{% endtabs %}

## Etapa 4: Integre seus frameworks

Em seguida, integre as **Dinâmicas** ou **Estáticas** XCFrameworks que você [preparou anteriormente](#step-3-prepare-your-files):

{% tabs %}
{% tab dinâmico %}
No seu projeto Xcode, selecione seu alvo de build, então **Geral**. Em **Frameworks, Bibliotecas e Conteúdo Incorporado**, arraste e solte os [arquivos que você preparou anteriormente](#step-3-prepare-your-files).

!["Um exemplo de projeto Xcode com cada biblioteca Braze configurada para 'Embed & Sign.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
Para ativar o suporte a GIF, adicione `SDWebImage.xcframework`, localizado em `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}
{% endtab %}

{% tab static %}
No seu projeto Xcode, selecione seu alvo de build, então **Geral**. Em **Frameworks, Libraries, and Embedded Content**, arraste e solte os [frameworks que você preparou anteriormente](#step-31-prepare-your-frameworks). Ao lado de cada estrutura, escolha **Não Incorporar**. 

!["Um exemplo de projeto Xcode com cada biblioteca Braze configurada para 'Não Incorporar.'"]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
Para ativar o suporte a GIF, adicione `SDWebImage.xcframework`, localizado em `braze-swift-sdk-prebuilt/static`.
{% endalert %}

Enquanto estiver no seu alvo de build, selecione **Fases de Build**. Em **Copiar Recursos do Pacote** arraste e solte os [pacotes que você preparou anteriormente](#step-32-prepare-your-bundles).

!["Um exemplo de projeto Xcode com pacotes adicionados em 'Copiar Recursos do Pacote.'"]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Erros comuns para projetos Objective-C

Se o seu projeto Xcode contiver apenas arquivos Objective-C, você poderá receber erros de "símbolo ausente" ao tentar compilar seu projeto. Para corrigir esses erros, abra seu projeto e adicione um arquivo Swift vazio à sua árvore de arquivos. Isso forçará sua cadeia de ferramentas a incorporar [SWIFT Runtime](https://support.apple.com/kb/dl1998) e vincular aos frameworks apropriados durante o período em questão.

```bash
FILE_NAME.swift
```

Substitua `FILE_NAME` por qualquer string sem espaços. Seu arquivo deve ser semelhante ao seguinte:

```bash
empty_swift_file.swift
```
