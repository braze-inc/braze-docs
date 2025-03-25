---
nav_title: Integración
article_title: Integración de la fuente de noticias para iOS
platform: iOS
page_order: 0
description: "Este artículo ofrece una visión general del modelo de datos del canal de noticias, la integración del canal de noticias en tu aplicación iOS y un ejemplo de integración de un controlador de vista personalizado."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de la fuente de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Modelo de datos del canal de noticias

### Obtener los datos

Para acceder al modelo de datos de fuentes de noticias, suscríbete a los eventos de actualización de fuentes de noticias:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Si quieres cambiar los datos de la tarjeta después de que los haya enviado Braze, te recomendamos que almacenes (copia profunda) los datos de la tarjeta localmente, los actualices y los visualices tú mismo. Las tarjetas son accesibles a través de [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "controlador de la fuente abk").

## Modelo de canal de noticias

Braze tiene cinco tipos de tarjeta únicos: imagen de banner, imagen con pie de foto, anuncio de texto y clásico. Cada tipo hereda propiedades comunes de un modelo base y tiene las siguientes propiedades adicionales.

### Propiedades del modelo de tarjeta base

|Propiedad|Descripción|
|---|---|
| `idString` | (Sólo lectura) El ID de la tarjeta configurado por Braze. |
| `viewed` | Esta propiedad refleja si el usuario ha leído o no la tarjeta. |
| `created` | (Sólo lectura) La propiedad es la marca de tiempo unix de la hora de creación de la tarjeta desde el panel de Braze. |
| `updated` | (Sólo lectura) La propiedad es la marca de tiempo unix de la última hora de actualización de la tarjeta desde el panel de Braze. |
| `categories` | La lista de categorías asignadas a la tarjeta, a las tarjetas sin categoría se les asignará `ABKCardCategoryNoCategory`.<br><br>Categorías disponibles:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | Un `NSDictionary` opcional de valores `NSString`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de imagen del banner

|Propiedad|Descripción|
|---|---|
| `image` | (Obligatorio) Esta propiedad es la URL de la imagen de la tarjeta. |
| `URL` | (Opcional) La URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(S) o una URL de protocolo. |
| `domain` | (Opcional) El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Puede mostrarse en la interfaz de usuario de la tarjeta para indicar la acción y la dirección al hacer clic en la tarjeta, pero está oculto en la fuente de noticias predeterminada de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de imagen subtitulada

|Propiedad|Descripción|
|---|---|
| `image` | (Obligatorio) Esta propiedad es la URL de la imagen de la tarjeta. |
| `title` | (Obligatorio) El texto del título de la tarjeta. |
| `description` (Obligatorio) El texto del cuerpo de la tarjeta. |
| `URL` | (Opcional) La URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(S) o una URL de protocolo. |
| `domain` | (Opcional) El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción y la dirección al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de anuncio de texto (imagen subtitulada sin imagen)

|Propiedad|Descripción|
|---|---|
| `title` | (Obligatorio) El texto del título de la tarjeta. |
| `description` | (Obligatorio) El texto del cuerpo de la tarjeta. |
| `url` | (Opcional) La URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(S) o una URL de protocolo. |
| `domain` | (Opcional) El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción y la dirección al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta clásica

|Propiedad|Descripción|
|---|---|
| `image` | (Obligatorio) Esta propiedad es la URL de la imagen de la tarjeta. |
| `title` | (Opcional) El texto del título de la tarjeta. |
| `description` | (Obligatorio) El texto del cuerpo de la tarjeta. |
| `URL` | (Opcional) La URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP(S) o una URL de protocolo. |
| `domain` | (Opcional) El texto del enlace para la URL de la propiedad, como @"blog.braze.com". Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción y la dirección al hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de tarjeta

|Método|Descripción|
|---|---|
| `logCardImpression` | Registra manualmente una impresión en Braze para una tarjeta concreta. |
| `logCardClicked` | Registra manualmente un clic en Braze para una tarjeta concreta. El SDK solo registrará un clic de tarjeta cuando la tarjeta tenga la propiedad `url` con un valor válido. Todas las subclases de `ABKCard` tienen la propiedad `url`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Visualización de la fuente de registro

Cuando muestres el canal de noticias en tu propia interfaz de usuario, puedes registrar manualmente las impresiones del canal de noticias a través de `- (void)logFeedDisplayed;`. Por ejemplo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## Integración del controlador de vista del canal de noticias

La integración del controlador de vista `ABKNewsFeedViewController` mostrará el canal de noticias de Braze.

Tienes una gran flexibilidad a la hora de elegir cómo mostrar los controladores de vista. Existen diferentes versiones de los controladores de vista para adaptarse a diferentes estructuras de navegación.

{% alert note %}
La fuente de noticias a la que se llama mediante el comportamiento predeterminado de un clic en un mensaje dentro de la aplicación no respetará ninguna delegación que hayas configurado para la fuente de noticias. Si quieres respetarlo, debes [configurar el delegado en `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) e implementar el método de delegado `ABKInAppMessageUIDelegate` [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks).
{% endalert %}

La fuente de noticias puede integrarse con dos contextos de controlador de vista: navegación o modal.

### Contexto de navegación - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab OBJETIVO-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

Para personalizar la barra de navegación `title`, establece la propiedad de título de la instancia `ABKNewsFeedTableViewController` `navigationItem`.

### Contexto modal - ABKFeedViewControllerModalContext

Este modal se utiliza para presentar el controlador de vista en una vista modal, con una barra de navegación en la parte superior y un botón **Listo** a la derecha de la barra. Para personalizar el título del modal, establece la propiedad `title` de la instancia `ABKNewsFeedTableViewController` `navigationItem` . 

Si **NO se establece** un delegado, el botón **Listo** cerrará la vista modal. Si **se establece** un delegado, el botón **Terminado** llamará al delegado, y el propio delegado se encargará de cerrar la vista.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Para ver ejemplos de controladores de vista, consulta nuestra [aplicación de ejemplo de canal de noticias](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample).


