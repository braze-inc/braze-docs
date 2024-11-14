---
nav_title: Delegado de interfaz de usuario de mensajes dentro de la aplicación
article_title: Delegado de interfaz de usuario de mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 2
description: "Este artículo de referencia cubre la configuración de un delegado de mensajería dentro de la aplicación de iOS para el SDK Swift."
channel:
  - in-app messages

---

# Delegado de interfaz de usuario de mensajes dentro de la aplicación

> Utiliza el botón opcional [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) para personalizar la presentación de los mensajes dentro de la aplicación y reaccionar a varios eventos del ciclo de vida. Este protocolo delegado puede utilizarse para recibir cargas útiles de mensajes dentro de la aplicación desencadenados para su posterior procesamiento, recibir eventos del ciclo de vida de la pantalla y controlar la temporización de la pantalla. 

## Requisitos previos

Para utilizar `BrazeInAppMessageUIDelegate`:
* Debes estar utilizando la implementación predeterminada de [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) como tu `inAppMessagePresenter`. 
* Debes incluir la biblioteca `BrazeUI` en tu proyecto.

## Configuración del delegado de mensajes dentro de la aplicación

Configura tu objeto [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) objeto delegado en la instancia de Braze siguiendo este código de ejemplo:

{% tabs %}
{% tab swift %}

Primero, implementa el protocolo `BrazeInAppMessageUIDelegate` y los métodos correspondientes que desees. En nuestro ejemplo siguiente, estamos implementando este protocolo en la clase `AppDelegate` de nuestra aplicación.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

A continuación, asigna el objeto `delegate` en la instancia `BrazeInAppMessageUI` antes de asignar esta interfaz de usuario de mensajes dentro de la aplicación como tu `inAppMessagePresenter`.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJETIVO-C %}

Primero, implementa el protocolo `BrazeInAppMessageUIDelegate` y los métodos correspondientes que desees. En nuestro ejemplo siguiente, estamos implementando este protocolo en la clase `AppDelegate` de nuestra aplicación.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

A continuación, asigna el objeto `delegate` en la instancia `BrazeInAppMessageUI` antes de asignar esta interfaz de usuario de mensajes dentro de la aplicación como tu `inAppMessagePresenter`.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

No todos los métodos de delegado están disponibles en Objective-C debido a la incompatibilidad de sus parámetros con el tiempo de ejecución del lenguaje.

{% endtab %}
{% endtabs %}

### Guía paso a paso

Para una implementación paso a paso del delegado de interfaz de usuario de mensajes dentro de la aplicación, consulta este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Personalizar la orientación de los mensajes dentro de la aplicación para iOS

### Configurar una orientación preferida

Puedes configurar todos los mensajes dentro de la aplicación para que se presenten en una orientación específica, independientemente de la orientación del dispositivo. Para establecer una orientación preferida, utiliza el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para establecer la propiedad `preferredOrientation` en `PresentationContext`. 

{% tabs %}
{% tab swift %}

Por ejemplo, para crear una orientación preferida de retrato:

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

Una vez presentado el mensaje dentro de la aplicación, cualquier cambio en la orientación del dispositivo mientras el mensaje sigue mostrándose hará que el mensaje gire con el dispositivo, siempre que sea compatible con la configuración del mensaje en `orientation`.

Ten en cuenta que la orientación del dispositivo también debe ser compatible con la propiedad `orientation` del mensaje dentro de la aplicación para que el mensaje se muestre. Además, la configuración de `preferredOrientation` sólo se respetará si está incluida en las orientaciones de interfaz admitidas de tu aplicación en la sección **Información de despliegue** de la configuración de tu objetivo en Xcode.

![Orientaciones admitidas en Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
La orientación sólo se aplica a la presentación del mensaje. Cuando el dispositivo cambia de orientación, la vista de mensajes adopta una de las orientaciones que admite. En dispositivos más pequeños (iPhones, iPod Touch), establecer una orientación horizontal para un mensaje modal o completo dentro de la aplicación puede provocar que el contenido quede truncado.
{% endalert %}

### Modificar la orientación de los mensajes

También puedes configurar la orientación por mensaje. Esta propiedad define todos los tipos de orientación disponibles para ese mensaje. Para ello, configura la propiedad `orientation` en un determinado `Braze.InAppMessage`:

{% tabs %}
{% tab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

## Desactivar el modo oscuro

Para evitar que los mensajes dentro de la aplicación adopten el estilo de modo oscuro cuando el dispositivo del usuario tiene habilitado el modo oscuro, implementa el método [delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. El `PresentationContext` pasado al método contiene una referencia al objeto `InAppMessage` que se va a presentar. Cada `InAppMessage` tiene una propiedad `themes` que contiene un tema de modo `dark` y `light`. Si estableces la propiedad `themes.dark` en `nil`, Braze presentará automáticamente el mensaje dentro de la aplicación utilizando su tema claro.

Los tipos de mensaje dentro de la aplicación con botones tienen un objeto `themes` adicional en su propiedad `buttons`. Para evitar que los botones adopten el estilo de modo oscuro, puedes utilizar [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) para crear una nueva serie de botones con un tema `light` y sin tema `dark`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Personalizar los clics de los botones

Para acceder a la información del botón de mensajes dentro de la aplicación o anular el comportamiento de clic, implementa [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi). Devuelve `true` para permitir que Braze procese la acción de clic, o devuelve `false` para anular el comportamiento.
{% tabs %}
{% tab swift %}

```swift
  func inAppMessage(
    _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
    buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
  ) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJETIVO-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Ocultar la barra de estado durante la visualización

Para los mensajes dentro de la aplicación `Full`, `FullImage` y `HTML`, el SDK ocultará la barra de estado de forma predeterminada. Para otros tipos de mensajes dentro de la aplicación, la barra de estado se deja intacta. Para configurar este comportamiento, utiliza el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para establecer la propiedad `statusBarHideBehavior` en la página `PresentationContext`. Este campo toma uno de los siguientes valores:

| Comportamiento de la barra de estado oculta            | Descripción                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | La vista de mensajes decide el estado oculto de la barra de estado.                                 |
| `.hidden`                           | Oculta siempre la barra de estado.                                                           |
| `.visible`                          | Muestra siempre la barra de estado.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Personalizar el tiempo de visualización 

Puedes controlar si un mensaje dentro de la aplicación disponible se mostrará durante ciertos momentos de tu experiencia de usuario. Si hay situaciones en las que no quieres que aparezca el mensaje dentro de la aplicación, como durante un juego a pantalla completa o en una pantalla de carga, puedes retrasar o descartar los mensajes dentro de la aplicación pendientes. Para controlar la temporización del mensaje dentro de la aplicación, utiliza el [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para establecer la propiedad `BrazeInAppMessageUI.DisplayChoice`. 

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configura `BrazeInAppMessageUI.DisplayChoice` para que devuelva uno de los siguientes valores:

| Elección de pantalla                      | Comportamiento                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | El mensaje se mostrará inmediatamente. Este es el valor predeterminado.                                                       |
| `.reenqueue`                        | El mensaje no se mostrará y volverá a colocarse en la parte superior de la pila.                                       |
| `.later`                            | El mensaje no se mostrará y volverá a colocarse en la parte superior de la pila. (Obsoleto, utiliza `.reenqueue`) |
| `.discard`                          | El mensaje se descartará y no se mostrará.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Muestras de aplicación

Consulta `InAppMessageUI` en nuestra carpeta de Ejemplos para ver un ejemplo en [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) y [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

