---
nav_title: Integración
article_title: Integración del controlador de vista de tarjeta de contenido para iOS
platform: iOS
page_order: 1
description: "Este artículo de referencia cubre los pasos de integración, los modelos de datos y las propiedades específicas de las tarjetas que están disponibles para tu aplicación de iOS."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de la tarjeta de contenido

## Modelo de datos de las tarjetas de contenido

El modelo de datos de las tarjetas de contenido está disponible en el SDK de iOS.

### Obtener los datos

Para acceder al modelo de datos de las tarjetas de contenido, suscríbete a los eventos de actualización de las tarjetas de contenido:

{% tabs %}
{% tab OBJETIVO-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Si quieres cambiar los datos de la tarjeta después de que los haya enviado Braze, te recomendamos que almacenes localmente una copia profunda de los datos de la tarjeta, actualices los datos y los visualices tú mismo. Se puede acceder a las tarjetas a través de [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Modelo de tarjeta de contenido

Braze ofrece tres tipos de tarjetas de contenido: banner, imagen subtitulada y clásica. Cada tipo hereda propiedades comunes de una clase base `ABKContentCard` y tiene las siguientes propiedades adicionales.

### Propiedades del modelo de tarjeta de contenido base - ABKContentCard

|Propiedad|Descripción|
|---|---|
|`idString` | (Sólo lectura) El ID de la tarjeta configurado por Braze. |
| `viewed` | Esta propiedad refleja si el usuario ha visto la tarjeta o no.|
| `created` | (Sólo lectura) Esta propiedad es la marca de tiempo unix de la hora de creación de la tarjeta desde Braze. |
| `expiresAt` | (Sólo lectura) Esta propiedad es la marca de tiempo unix de la hora de caducidad de la tarjeta.|
| `dismissible` | Esta propiedad refleja si el usuario puede descartar la tarjeta.|
| `pinned` | Esta propiedad refleja si la tarjeta se configuró como "anclada" en el panel.|
| `dismissed` | Esta propiedad refleja si el usuario ha descartado la tarjeta.|
| `url` | La URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(s) o una URL de protocolo.|
| `openURLInWebView` | Esta propiedad determina si la URL se abrirá dentro de la aplicación o en un navegador web externo.|
| `extras`| Un `NSDictionary` opcional de valores `NSString`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido de banner - ABKBannerContentCard

|Propiedad|Descripción|
|---|---|
| `image` | Esta propiedad es la URL de la imagen de la tarjeta.|
| `imageAspectRatio` | Esta propiedad es la relación de aspecto de la imagen de la tarjeta y sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido de imagen subtitulada - ABKCaptionedImageCard

|Propiedad|Descripción|
|---|---|
| `image` | Esta propiedad es la URL de la imagen de la tarjeta.|
| `imageAspectRatio` | Esta propiedad es la relación de aspecto de la imagen de la tarjeta.|
| `title` | El texto del título de la tarjeta.|
| `cardDescription` | El texto del cuerpo de la tarjeta.|
| `domain` | El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción/dirección de hacer clic en la tarjeta.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de contenido clásica - ABKClassicContentCard

|Propiedad|Descripción|
|---|---|
| `image` | (Opcional) Esta propiedad es la URL de la imagen de la tarjeta.|
| `title` | El texto del título de la tarjeta. |
| `cardDescription` | El texto del cuerpo de la tarjeta. |
| `domain` | El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción y la dirección al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de tarjeta

|Método|Descripción|
|---|---|
| `logContentCardImpression` | Registra manualmente una impresión en Braze para una tarjeta concreta. |
| `logContentCardClicked` | Registra manualmente un clic en Braze para una tarjeta concreta. El SDK solo registrará un clic de tarjeta cuando la tarjeta tenga la propiedad `url` con un valor válido. |
| `logContentCardDismissed` | Registra manualmente en Braze el descarte de una tarjeta concreta. El SDK solo registrará un descarte de tarjeta si la propiedad `dismissed` de la tarjeta no está ya establecida en `true`. |
| `isControlCard` | Determina si una tarjeta es la tarjeta de control para una prueba A/B. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más detalles, consulta la [documentación de referencia de la clase](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)

## Integración del controlador de vista de las tarjetas de contenido

Las tarjetas de contenido pueden integrarse con dos contextos de controlador de vista: navegación o modal.

### Contexto de navegación

Ejemplo de push de una instancia de `ABKContentCardsTableViewController` en un controlador de navegación:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Para personalizar el título de la barra de navegación, establece la propiedad title de la instancia `ABKContentCardsTableViewController` de `navigationItem`.
{% endalert %}

### Contexto modal

Este modal se utiliza para presentar el controlador de vista en una vista modal, con una barra de navegación en la parte superior y un botón **Terminar** en el lateral de la barra.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Para ver ejemplos de controladores de vista, consulta nuestra [aplicación de ejemplo Tarjetas de contenido](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Para personalizar la cabecera, establece la propiedad title del `navigationItem` perteneciente a la instancia `ABKContentCardsTableViewController` incrustada en la instancia padre `ABKContentCardsViewController`.
{% endalert %}
