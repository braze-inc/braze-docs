{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que habilitar los mensajes dentro de la aplicación.

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Habilitación de mensajes dentro de la aplicación

### Paso 1: Crea una implementación de `BrazeInAppMessagePresenter`

Para que Braze muestre mensajes dentro de la aplicación, crea una implementación del protocolo `BrazeInAppMessagePresenter` y asígnala a la opción `inAppMessagePresenter` de tu instancia de Braze. También puedes utilizar el presentador predeterminado de la interfaz de usuario Braze instanciando un objeto `BrazeInAppMessageUI`.

Ten en cuenta que tendrás que importar la biblioteca `BrazeUI` para acceder a la clase `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### Paso 2: No desencadenar ninguna coincidencia

Implementa [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) dentro de la clase `BrazeDelegate` correspondiente. Cuando Braze no encuentre un desencadenante que coincida con un evento concreto, llamará a este método automáticamente.
