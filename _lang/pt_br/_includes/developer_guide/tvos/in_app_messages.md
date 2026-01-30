{% alert important %}
Lembre-se de que você precisará implementar sua própria interface personalizada, pois o envio de mensagens no aplicativo é suportado por meio de uma interface sem cabeça usando o SDK SWIFT—que não inclui nenhuma interface ou visualização padrão para tvOS.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Ativação de mensagens no app

### Etapa 1: Criar um novo app para iOS

Na Braze, selecione **Settings** > **App Settings** e, em seguida, selecione **Add App**. Digite um nome para o seu aplicativo para tvOS, selecione **iOS - não**_tvOS - e_selecione **Adicionar aplicativo**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Se você selecionar a caixa de seleção **tvOS**, não poderá personalizar as mensagens no app para tvOS.
{% endalert %}

### Etapa 2: Obtenha a chave de API de seu app

Nas configurações do aplicativo, selecione o novo aplicativo para tvOS e, em seguida, note a chave de API do aplicativo. Você usará essa chave para configurar seu app no Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Etapa 3: Integrar o BrazeKit

Use a chave de API de seu app para integrar o [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) em seu projeto tvOS no Xcode. Você só precisa integrar a BrazeKit a partir da Braze Swift SDK.

### Etapa 4: Crie sua interface de usuário personalizada

Como a Braze não fornece uma interface de usuário padrão para mensagens no aplicativo no tvOS, você precisará personalizá-la. Para obter um passo a passo completo, consulte nosso tutorial passo a passo: [Personalizando mensagens no app para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization). Para obter um projeto de amostra, consulte [Amostras do SDK da Braze para Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui).
