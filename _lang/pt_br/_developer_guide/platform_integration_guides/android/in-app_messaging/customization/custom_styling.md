---
nav_title: Estilo personalizado
article_title: Envio de mensagens no app com estilo personalizado para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Este artigo de referência aborda o estilo personalizado de envio de mensagens no app para seu aplicativo Android ou FireOS."
channel:
  - in-app messages

---

# Estilo personalizado

> Os elementos da UI do Braze vêm com uma aparência padrão que corresponde às diretrizes da UI padrão do Android e proporciona uma experiência perfeita. Este artigo de referência aborda o estilo personalizado de envio de mensagens no app para seu aplicativo Android ou FireOS.

Você pode ver os estilos padrão no arquivo [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) do Braze SDK:

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

Se preferir, você pode substituir esses estilos para criar uma aparência que se adapte melhor ao seu app.

Para substituir um estilo, copie-o integralmente para o arquivo `styles.xml` em seu projeto e faça as modificações. Todo o estilo deve ser copiado para seu arquivo local `styles.xml` para que todas as atribuições sejam definidas corretamente. Observe que esses estilos personalizados são para alterações em elementos individuais da interface do usuário, não para alterações em massa nos layouts. As alterações no nível do layout precisam ser tratadas com exibições personalizadas.

{% alert note %}
Você pode personalizar algumas cores diretamente em sua campanha do Braze sem modificar o XML. Lembre-se de que as cores definidas no dashboard do Braze substituirão as cores que você definir em qualquer outro lugar.
{% endalert %}

## Fonte personalizada

O Braze permite a configuração de uma fonte personalizada usando a [guia de família de fontes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Para usá-lo, substitua o estilo do texto da mensagem, dos cabeçalhos e do texto do botão e use o atributo `fontFamily` para instruir o Braze a usar sua família de fontes personalizada.

Por exemplo, para atualizar a fonte do texto do botão de mensagem no app, substitua o estilo `Braze.InAppMessage.Button` e faça referência à sua família de fontes personalizada. O valor da atribuição deve apontar para uma família de fontes em seu diretório `res/font`.

Aqui está um exemplo truncado com uma família de fontes personalizadas, `my_custom_font_family`, referenciada na última linha:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Além do estilo `Braze.InAppMessage.Button` para o texto do botão, o estilo para o texto da mensagem é `Braze.InAppMessage.Message` e o estilo para os cabeçalhos da mensagem é `Braze.InAppMessage.Header`. Se quiser usar sua família de fontes personalizada em todos os textos possíveis de mensagens no app, você poderá definir sua família de fontes no estilo `Braze.InAppMessage`, que é o estilo pai de todas as mensagens no app.

{% alert important %}
Assim como ocorre com outros estilos personalizados, o estilo inteiro deve ser copiado para o arquivo local `styles.xml` para que todas as atribuições sejam definidas corretamente.
{% endalert %}

## Definição de uma orientação fixa

Para definir uma orientação fixa para uma mensagem no app, primeiro [defina um listener personalizado do gerenciador de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/). Em seguida, chame `setOrientation()` no objeto `IInAppMessage` no método delegado `beforeInAppMessageDisplayed()`:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Para dispositivos tablet, as mensagens no app aparecerão no estilo de orientação preferido do usuário, independentemente da orientação real da tela.

