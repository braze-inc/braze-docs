---
nav_title: Manejo personalizado de la pantalla
article_title: Personaliza el manejo de la visualización de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia trata sobre la gestión de la visualización personalizada de mensajes dentro de la aplicación para tu aplicación iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Manejo personalizado de la visualización de mensajes dentro de la aplicación

Cuando está configurado [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h), se llama al siguiente método delegado antes de que se muestren los mensajes dentro de la aplicación:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Si sólo has implementado [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)se llamará al siguiente método delegado de interfaz de usuario:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Puedes personalizar la gestión de mensajes dentro de la aplicación implementando este método delegado y devolviendo uno de los siguientes valores para `ABKInAppMessageDisplayChoice`:

| `ABKInAppMessageDisplayChoice` | Comportamiento |
| -------------------------- | -------- |
| Objective-C: `ABKDisplayInAppMessageNow`<br>Swift: `displayInAppMessageNow` | El mensaje se mostrará inmediatamente. |
| Objective-C: `ABKDisplayInAppMessageLater`<br>Swift: `displayInAppMessageLater` | El mensaje no se mostrará y volverá a colocarse en la parte superior de la pila. |
| Objective-C: `ABKDiscardInAppMessage`<br>Swift: `discardInAppMessage`| El mensaje se descartará y no se mostrará. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes utilizar el método delegado `beforeInAppMessageDisplayed:` para añadir lógica de visualización de mensajes dentro de la aplicación, personalizar los mensajes dentro de la aplicación antes de que Braze los muestre, o excluirte totalmente de la lógica de visualización de mensajes dentro de la aplicación y de la interfaz de usuario de Braze.

Consulta nuestra [aplicación de muestra](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) para ver un ejemplo de implementación.

## Anulación de mensajes dentro de la aplicación antes de la visualización

Si quieres modificar el comportamiento de visualización de los mensajes dentro de la aplicación, debes añadir la lógica de visualización necesaria a tu método delegado `beforeInAppMessageDisplayed:`. Por ejemplo, puede que quieras mostrar el mensaje dentro de la aplicación desde la parte superior de la pantalla si se está mostrando el teclado, o tomar el modelo de datos del mensaje dentro de la aplicación y mostrar tú mismo el mensaje dentro de la aplicación.

Si la campaña de mensajería dentro de la aplicación no se muestra cuando se ha iniciado la sesión, asegúrate de que has añadido la lógica de visualización necesaria a tu método delegado `beforeInAppMessageDisplayed:`. Esto permite que la campaña de mensajería dentro de la aplicación se muestre desde la parte superior de la pantalla aunque se esté mostrando el teclado.

## Desactivar el modo oscuro

Para evitar que los mensajes dentro de la aplicación adopten el estilo de modo oscuro cuando el dispositivo del usuario tiene habilitado el modo oscuro, utiliza la propiedad [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d). Desde el método `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` o `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`, establece la propiedad `enableDarkTheme` del parámetro `inAppMessage` del método en `NO`.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## Ocultar la barra de estado durante la visualización

Para los mensajes dentro de la aplicación `Full` y `HTML`, el SDK intentará colocar el mensaje sobre la barra de estado de forma predeterminada. Sin embargo, en algunos casos, la barra de estado puede seguir apareciendo encima del mensaje dentro de la aplicación. A partir de la versión [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) del SDK de iOS, puedes forzar que la barra de estado se oculte al mostrar los mensajes dentro de la aplicación `Full` y `HTML` configurando `ABKInAppMessageHideStatusBarKey` a `YES` dentro del `appboyOptions` pasado a `startWithApiKey:`.

## Registro de impresiones y clics

El registro de impresiones y clics de mensajes dentro de la aplicación no es automático cuando implementas un manejo completamente personalizado (por ejemplo, eludes la visualización de mensajes dentro de la aplicación de Braze devolviendo `ABKDiscardInAppMessage` en tu `beforeInAppMessageDisplayed:`). Si decides implementar tu propia interfaz de usuario utilizando nuestros modelos de mensajes dentro de la aplicación, debes registrar los análisis con los siguientes métodos en la clase `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

Además, deberías registrar los clics en los botones de las subclases de `ABKInAppMessageImmersive` (*i.e*., `Modal` y `Full` mensajes dentro de la aplicación):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Declaraciones de métodos

Para más información, consulta los siguientes archivos de encabezado:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Muestras de aplicación

Consulta [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) ejemplo de aplicación de mensajes dentro de la aplicación.



