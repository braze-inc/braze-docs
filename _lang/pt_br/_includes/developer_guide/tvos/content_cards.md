## Pré-requisitos

Antes de usar os Cartões de Conteúdo, você precisará integrar o [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) no seu app. Em seguida, você precisará concluir as etapas para configurar seu app tvOS.

{% alert important %}
Lembre-se de que você precisará implementar sua própria IU personalizada, pois os cartões de conteúdo são compatíveis com a IU headless usando o Swift SDK, que não inclui nenhuma IU ou exibição padrão para o tvOS.
{% endalert %}

## Configurando seu app para tvOS

### Etapa 1: Criar um novo app para iOS

Na Braze, selecione **Settings** > **App Settings** e, em seguida, selecione **Add App**. Digite um nome para o seu aplicativo para tvOS, selecione **iOS - não**_tvOS - e_selecione **Adicionar aplicativo**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Se você marcar a caixa de seleção **tvOS**, não poderá personalizar os cartões de conteúdo para tvOS.
{% endalert %}

### Etapa 2: Obtenha a chave de API de seu app

Nas configurações do aplicativo, selecione o novo aplicativo para tvOS e, em seguida, note a chave de API do aplicativo. Você usará essa chave para configurar seu app no Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Etapa 3: Integrar o BrazeKit

Use a chave de API de seu app para integrar o [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) em seu projeto tvOS no Xcode. Você só precisa integrar a BrazeKit a partir da Braze Swift SDK.

### Etapa 4: Crie sua interface de usuário personalizada

Como a Braze não fornece uma interface de usuário padrão para cartões de conteúdo no tvOS, você mesmo precisará personalizá-la. Para obter um passo a passo completo, consulte nosso tutorial passo a passo: [Personalização de cartões de conteúdo para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Para obter um projeto de amostra, consulte [Amostras do SDK da Braze para Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).
