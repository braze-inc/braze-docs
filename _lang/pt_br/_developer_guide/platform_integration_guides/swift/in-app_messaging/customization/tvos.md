---
nav_title: tvOS
article_title: Mensagens no app para tvOS
platform: tvOS
page_type: reference
description: "Saiba como personalizar suas mensagens no app para a plataforma tvOS da Apple."
page_order: 0
---

# Personalizando mensagens no app para tvOS

> Saiba como personalizar suas mensagens no app para a plataforma tvOS da Apple.

{% alert important %}
Lembre-se de que você precisará implementar sua própria interface personalizada, pois o envio de mensagens no aplicativo é suportado por meio de uma interface sem cabeça usando o SDK SWIFT—que não inclui nenhuma interface ou visualização padrão para tvOS.
{% endalert %}

## Configurando seu app tvOS

### Etapa 1: Crie um novo app iOS

Na Braze, selecione **Configurações** > **Configurações do app**, depois selecione **Adicionar app**. Digite um nome para o seu app tvOS, selecione **iOS**—_não tvOS_—então selecione **Adicionar App**.

![TEXTO_ALTERNATIVO.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Se você selecionar a caixa de seleção **tvOS**, não poderá personalizar as mensagens no app para tvOS.
{% endalert %}

### Etapa 2: Obtenha a chave de API de seu app

Nas configurações do seu app, selecione seu novo app tvOS e anote a chave de API do seu app. Você usará essa chave para configurar seu app no Xcode.

![TEXTO_ALTERNATIVO]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Etapa 3: Integrar o BrazeKit

Use a chave de API do seu app para integrar o [SDK da Braze para Swift](https://github.com/braze-inc/braze-swift-sdk) ao seu projeto tvOS no Xcode. Você só precisa integrar o BrazeKit do SDK da Braze para Swift.

### Etapa 4: Crie sua interface de usuário personalizada

Como a Braze não fornece uma interface de usuário padrão para mensagens no aplicativo no tvOS, você precisará personalizá-la. Para obter um passo a passo completo, consulte nosso tutorial passo a passo: [Personalizando mensagens no app para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization). Para um projeto de exemplo, veja [amostras do SDK SWIFT da Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui).
