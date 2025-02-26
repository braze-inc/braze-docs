---
nav_title: Swift Package Manager
article_title: Integração do Swift Package Manager para iOS
platform: Swift
page_order: 1
description: "Este tutorial explica a instalação do SDK da Braze para Swift usando o Swift Package Manager para iOS."

---

# integração do Swift Package Manager

> Instalar o Swift SDK via [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatiza a maior parte do processo de instalação para você. Antes de iniciar este processo, verifique as [informações da versão](https://github.com/braze-inc/braze-swift-sdk#version-information) para garantir que seu ambiente é compatível com a Braze.

## Adicionando a dependência ao seu projeto

### Importar versão do SDK

Abra seu projeto e navegue até as configurações do seu projeto. Selecione a guia **SWIFT Packages** e clique no botão adicionar <i class="fas fa-plus"></i> abaixo da lista de pacotes.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
A partir da versão 7.4.0, o Braze Swift SDK tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Digite o URL do nosso repositório iOS SWIFT SDK `https://github.com/braze-inc/braze-swift-sdk` no campo de texto. Embaixo da seção **Regra de Dependência**, selecione a versão do SDK. Finalmente, clique em **Adicionar Pacote**.

![]({% image_buster /assets/img/importsdk_example.png %})

### Selecionar pacotes

O SDK Braze SWIFT separa os recursos em bibliotecas independentes para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos.

| Pacote | Informações |
| ------- | ------- |
| `BrazeKit` | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push. |
| `BrazeLocation` | Biblioteca de local fornecendo suporte para análise de dados de local e monitoramento de geofence. |
| `BrazeUI` | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app e Cartões de Conteúdo. |
{: .ws-td-nw-1}

#### Bibliotecas de extensão

{% alert warning %}
[Serviço de Notificação Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [História de Push Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao alvo principal do seu aplicativo. Em vez disso, siga os guias vinculados para integrá-los separadamente em suas respectivas extensões de destino.
{% endalert %}

| Pacote | Informações |
| ------- | ------- |
| `BrazeNotificationService` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `BrazePushStory` | Biblioteca de extensão de conteúdo de notificação que fornece suporte para push Stories. |
{: .ws-td-nw-1}

 Selecione o pacote que melhor atenda às suas necessidades e clique **Adicionar Pacote**. Certifique-se de selecionar `BrazeKit` no mínimo.

![]({% image_buster /assets/img/add_package.png %})

## Próximos passos

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

