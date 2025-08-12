---
nav_title: CocoaPods
article_title: Integração do CocoaPods para iOS
platform: iOS
page_order: 2
description: "Este artigo de referência mostra como integrar o SDK da Braze usando o CocoaPods para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração com o CocoaPods

## Etapa 1: Instalar o CocoaPods

A instalação do SDK do iOS por meio do [CocoaPods](http://cocoapods.org/) automatiza a maior parte do processo de instalação para você. Antes de iniciar esse processo, use a [versão 2.0.0 ou superior do Ruby](https://www.ruby-lang.org/en/installation/). Não se preocupe, não é necessário ter conhecimento da sintaxe do Ruby para instalar esse SDK.

Execute o seguinte comando para começar:

```bash
$ sudo gem install cocoapods
```

Se você tiver problemas com CocoaPods, consulte o [guia de solução de problemas](http://guides.cocoapods.org/using/troubleshooting.html) do CocoaPods.

{% alert note %}
Se solicitado a substituir o executável `rake`, consulte as direções [Introdução](http://guides.cocoapods.org/using/getting-started.html) em CocoaPods.org para mais detalhes.
{% endalert %}

## Etapa 2: Construindo o arquivo de pod

Agora que você instalou o CocoaPods Ruby Gem, precisará criar um arquivo no diretório do projeto Xcode chamado `Podfile`.

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

Sugerimos que você faça uma versão da Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Fica assim: `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com grandes alterações, você poderá usar `pod 'Appboy-iOS-SDK'` em seu Podfile.

#### Subespécies

Recomendamos que os integradores importem nosso SDK completo. No entanto, se tiver certeza de que integrará apenas um recurso específico da Braze, você poderá importar apenas a subespecificação da interface do usuário desejada em vez do SDK completo.

| Subespécie | Informações |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | A subespecificação `InAppMessage` contém a interface do usuário de mensagens no app da Braze e o Core SDK.|
| `pod 'Appboy-iOS-SDK/ContentCards'` | A subespecificação `ContentCards` contém a interface do usuário de cartões de conteúdo da Braze e o Core SDK. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | A subespécie `NewsFeed` contém o Braze Core SDK. |
| `pod 'Appboy-iOS-SDK/Core'` | A subespecificação `Core` contém suporte para análise de dados, como eventos personalizados e atributos. |
{: .ws-td-nw-1}

## Etapa 3: Instalação do SDK da Braze

Para instalar o SDK da Braze CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez de seu projeto do Xcode. 

![Uma pasta Appboy Example expandida para mostrar o novo `AppbpyExample.workspace`.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Próximos passos

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/).

## Atualizando o SDK do Braze via CocoaPods

Para atualizar um CocoaPod, basta executar o seguinte comando no diretório do projeto:

```
pod update
```

