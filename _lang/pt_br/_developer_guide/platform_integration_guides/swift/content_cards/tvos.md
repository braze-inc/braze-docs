---
nav_title: tvOS
article_title: Cartões de conteúdo para tvOS
platform: tvOS
page_type: reference
description: "Saiba como personalizar seus cartões de conteúdo para a plataforma tvOS da Apple."
page_order: 1
---

# Personalização de cartões de conteúdo para tvOS

> Saiba como personalizar seus cartões de conteúdo para a plataforma tvOS da Apple.

{% alert important %}
Lembre-se de que você precisará implementar sua própria IU personalizada, pois os cartões de conteúdo são compatíveis com a IU headless usando o Swift SDK, que não inclui nenhuma IU ou exibição padrão para o tvOS.
{% endalert %}

## Configurando seu app tvOS

### Etapa 1: Crie um novo app iOS

Na Braze, selecione **Configurações** > **Configurações do app**, depois selecione **Adicionar app**. Digite um nome para o seu app tvOS, selecione **iOS**—_não tvOS_—então selecione **Adicionar App**.

![TEXTO_ALTERNATIVO.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Se você marcar a caixa de seleção **tvOS**, não poderá personalizar os cartões de conteúdo para tvOS.
{% endalert %}

### Etapa 2: Obtenha a chave de API de seu app

Nas configurações do seu app, selecione seu novo app tvOS e anote a chave de API do seu app. Você usará essa chave para configurar seu app no Xcode.

![TEXTO_ALTERNATIVO]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Etapa 3: Integrar o BrazeKit

Use a chave de API do seu app para integrar o [SDK da Braze para Swift](https://github.com/braze-inc/braze-swift-sdk) ao seu projeto tvOS no Xcode. Você só precisa integrar o BrazeKit do SDK da Braze para Swift.

### Etapa 4: Crie sua interface de usuário personalizada

Como a Braze não fornece uma interface de usuário padrão para cartões de conteúdo no tvOS, você mesmo precisará personalizá-la. Para obter um passo a passo completo, consulte nosso tutorial passo a passo: [Personalização de cartões de conteúdo para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Para obter um projeto de amostra, consulte [Amostras do SDK da Braze para Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).
