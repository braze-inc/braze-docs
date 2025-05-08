---
nav_title: CocoaPods
article_title: Integração do CocoaPods para iOS
platform: Swift
page_order: 2
description: "Este artigo de referência mostra como integrar o Braze Swift SDK usando o CocoaPods para iOS."

---

# Integração com o CocoaPods

## Etapa 1: Instalar o CocoaPods

A instalação do SDK do iOS por meio do [CocoaPods](http://cocoapods.org/) automatiza a maior parte do processo de instalação para você. Para instalar o CocoaPods, consulte o [guia de introdução do  CocoaPods](https://guides.cocoapods.org/using/getting-started.html).

Execute o seguinte comando para começar:

```bash
$ sudo gem install cocoapods
```

Se você tiver problemas com o CocoaPods, consulte o [](http://guides.cocoapods.org/using/troubleshooting.html "Guia de solução de problemas do CocoaPods").

## Etapa 2: Construindo o arquivo de pod

Agora que você instalou o CocoaPods Ruby Gem, precisará criar um arquivo no diretório do projeto Xcode chamado `Podfile`.

{% alert note %}
A partir da versão 7.4.0, o Braze Swift SDK tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contém a biblioteca principal do SDK que oferece suporte a análises de dados e notificações por push.

Sugerimos que você faça uma versão da Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Fica assim: `pod 'BrazeKit' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com grandes alterações, você poderá usar `pod 'BrazeKit'` em seu Podfile.

#### Bibliotecas adicionais

O Braze Swift SDK separa os recursos em bibliotecas autônomas para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos. Além de `BrazeKit`, você pode adicionar as seguintes bibliotecas ao seu Podfile:

| Biblioteca | Informações |
| ------- | ------- |
| `pod 'BrazeLocation'` | Biblioteca de local fornecendo suporte para análise de dados de local e monitoramento de geofence. |
| `pod 'BrazeUI'` | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app e Cartões de Conteúdo. |
{: .ws-td-nw-1}

##### Bibliotecas de extensão

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao direcionamento de seu aplicativo principal. Em vez disso, será necessário criar direcionamentos de extensão separados para cada um desses módulos e importar os módulos Braze para seus direcionamentos correspondentes.

| Biblioteca | Informações |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `pod 'BrazePushStory'` | Biblioteca de extensão de conteúdo de notificação que fornece suporte para push Stories. |
{: .ws-td-nw-1}

## Etapa 3: Instalação do SDK da Braze

Para instalar o Braze SDK CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez de seu projeto do Xcode.

![Uma pasta Braze Example expandida para mostrar o novo `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

## Próximos passos

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Atualizando o SDK do Braze via CocoaPods

Para atualizar um CocoaPod, basta executar o seguinte comando no diretório do projeto:

```
pod update
```

