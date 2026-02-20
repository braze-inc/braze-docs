## Requisitos previos

Antes de poder utilizar las tarjetas de contenido, tendrás que integrar el [SDK de Braze Swift]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) en tu aplicación. Sin embargo, no es necesaria ninguna configuración adicional.

## Ver contextos del controlador

La interfaz de usuario predeterminada de las tarjetas de contenido puede integrarse desde la biblioteca `BrazeUI` del SDK de Braze. Crea el controlador de vista Tarjetas de contenido utilizando la instancia `braze`. Si deseas interceptar y reaccionar al ciclo de vida de la interfaz de usuario de la tarjeta de contenido, implementa [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) como delegado de tu `BrazeContentCardUI.ViewController`.

{% alert note %}
Para más información sobre las opciones del controlador de vista de iOS, consulta la [documentación para desarrolladores de Apple](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

La biblioteca `BrazeUI` del SDK de Swift proporciona dos contextos predeterminados de controlador de vista: [navegación](#swift_navigation) o [modal](#swift_modal). Esto significa que puedes integrar las tarjetas de contenido en estos contextos añadiendo unas pocas líneas de código a tu aplicación o sitio web. Ambas vistas ofrecen opciones de personalización y estilo, como se describe en la [guía de personalización]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). También puedes crear un controlador de vista de tarjeta de contenido personalizado, en lugar de utilizar el estándar de Braze, para tener aún más opciones de personalización: consulta el [tutorial sobre la interfaz de usuario de las tarjetas de contenido](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) para ver un ejemplo.

{% alert important %}
Para manejar tarjetas de contenido con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}

### Navegación

Un controlador de navegación es un controlador de vistas que gestiona uno o varios controladores de vistas hijos en una interfaz de navegación. He aquí un ejemplo de push de una instancia de `BrazeContentCardUI.ViewController` en un controlador de navegación:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modal

Utiliza presentaciones modales para crear interrupciones temporales en el flujo de trabajo de tu aplicación, como solicitar al usuario información importante. Esta vista modelo tiene una barra de navegación en la parte superior y un botón de **Terminar** en el lateral de la barra. He aquí un ejemplo de push de una instancia de `BrazeContentCard.ViewController` en un controlador modal:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Para ver ejemplos de uso de los controladores de vista `BrazeUI`, consulta los ejemplos de interfaz de usuario de las tarjetas de contenido correspondientes en nuestra [aplicación Ejemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Modelo de tarjeta base

El modelo de datos de las tarjetas de contenido está disponible en el módulo `BrazeKit` del SDK de Braze Swift. Este módulo contiene los siguientes tipos de tarjetas de contenido, que son una implementación del tipo `Braze.ContentCard`. Para obtener una lista completa de las propiedades de la tarjeta de contenido y su uso, consulta la [clase`ContentCard` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard). 

- Solo imagen
- Imagen subtitulada
- Clásica
- Imagen clásica
- Control

Para acceder al modelo de datos de las tarjetas de contenido, llama a `contentCards.cards` en tu instancia `braze`. Consulta [Análisis de]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) tarjetas para obtener más información sobre cómo suscribirte a los datos de las tarjetas.

{% alert note %}
Ten en cuenta que `BrazeKit` ofrece una clase [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) para que sea compatible con Objective-C.
{% endalert %}

## Métodos de tarjeta

Cada tarjeta se inicializa con un objeto `Context`, que contiene varios métodos para gestionar el estado de tu tarjeta. Llama a estos métodos cuando quieras modificar la propiedad de estado correspondiente en un objeto tarjeta concreto.

| Método                               | Descripción                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Registra el evento de impresión de la tarjeta de contenido.                                                                                                   |
| `card.context?.logClick()`           | Registra el evento de clic de la tarjeta de contenido.                                                                                                        |
| `card.context?.processClickAction()` | Procesa una entrada [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) determinada. |
| `card.context?.logDismissed()`       | Registra el evento de tarjeta de contenido descartada.                                                                                                    |
| `card.context?.logError()`           | Registra un error relacionado con la tarjeta de contenido.                                                                                                |
| `card.context?.loadImage()`          | Carga una determinada imagen de tarjeta de contenido desde una URL. Este método puede ser nulo cuando la tarjeta de contenido no tiene imagen.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más detalles, consulta la [documentación de la clase `Context` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)
