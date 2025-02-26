---
nav_title: Testes de unidade (opcional)
article_title: Testes de unidade de notificações por push para iOS
platform: iOS
page_order: 29.5
description: "Este artigo de referência descreve como implementar testes de unidade opcionais para sua implementação push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testes unitários {#unit-tests}

Este guia opcional descreve como implementar alguns testes de unidade que verificarão se o app delegate segue corretamente as etapas descritas em nossas [instruções de integração push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/). 

Se todos os testes forem aprovados, em geral, isso significa que a parte baseada em código de sua configuração push está funcionando. Se um teste falhar, isso pode significar que você seguiu incorretamente uma etapa ou pode ser resultado de uma personalização válida que não se alinha precisamente com nossas instruções padrão.

De qualquer forma, essa pode ser uma abordagem útil para verificar se você seguiu as etapas de integração e para ajudar a monitorar quaisquer regressões.

## Etapa 1: Criação de um direcionamento de testes de unidade

Pule esta etapa se o projeto do seu app no Xcode já contiver um pacote de teste de unidade.

Em seu projeto de app, acesse o menu **Arquivo > Novo > Direcionamento** e adicione um novo "Pacote de teste de unidade". Esse pacote pode usar Objective C ou Swift e ter qualquer nome. Defina o "Target to be Tested" (Alvo a ser testado) como o alvo principal de seu app.

## Etapa 2: Adicione o SDK do Braze aos seus testes unitários

Usando o mesmo método que você usou inicialmente para [instalar o SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/), confira se a mesma instalação do SDK também está disponível para o direcionamento de seus testes de unidade. Por exemplo, usando o CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Etapa 3: Adicione o OCMock aos seus testes unitários

Adicione o [OCMock](https://ocmock.org/) ao seu direcionamento de teste por meio do CocoaPods, do Carthage ou de sua biblioteca estática. Por exemplo, usando o CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Etapa 4: Concluir a instalação das bibliotecas adicionadas

Conclua a instalação do SDK da Braze e do OCMock. Por exemplo, usando o CocoaPods, navegue até o diretório do seu projeto de app do Xcode no terminal e execute o seguinte comando:

```
pod install
```

Nesse ponto, você deve conseguir abrir o espaço de trabalho do projeto Xcode criado pelo CocoaPods.

## Etapa 5: Adição de testes push

Crie um novo arquivo Objective C em seu direcionamento de testes unitários. 

Se o direcionamento dos testes de unidade estiver em Swift, o Xcode poderá perguntar: "Você gostaria de configurar um cabeçalho de ponte Objective C?" O cabeçalho de ponte é opcional, portanto, você pode clicar em **Não criar** e ainda assim executar esses testes de unidade com êxito.

Adicione o conteúdo do aplicativo de amostra HelloSwift [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) ao novo arquivo.

## Etapa 6: Executar o conjunto de testes

Execute os testes de unidade de seu app. Essa pode ser uma etapa de verificação única ou pode ser incluída indefinidamente em seu conjunto de testes para ajudar a detectar quaisquer regressões.

