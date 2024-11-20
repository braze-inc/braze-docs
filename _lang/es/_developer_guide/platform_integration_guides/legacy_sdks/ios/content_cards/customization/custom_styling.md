---
nav_title: Estilo personalizado
article_title: Estilo personalizado de tarjeta de contenido para iOS
platform: iOS
page_order: 1
description: "Este artículo trata de las opciones de estilo personalizado de la tarjeta de contenido para tu aplicación iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Estilo personalizado

## Sustitución de imágenes predeterminadas

{% alert important %}
La integración de `SDWebImage` es necesaria si planeas utilizar nuestra interfaz de usuario Braze para mostrar imágenes en los mensajes dentro de la aplicación iOS o en las tarjetas de contenido.
{% endalert %}

Braze permite a los clientes sustituir las imágenes predeterminadas existentes por sus propias imágenes personalizadas. Para ello, crea un nuevo archivo `png` con la imagen personalizada y añádelo al paquete de imágenes de la aplicación. A continuación, renombra el archivo con el nombre de la imagen para anular la imagen predeterminada en nuestra biblioteca. Además, asegúrate de subir las versiones `@2x` y `@3x` de las imágenes para adaptarlas a los distintos tamaños de teléfono. Las imágenes disponibles para anular en las tarjetas de contenido incluyen:

- Imagen del marcador de posición: `appboy_cc_noimage_lrg`
- Imagen del icono anclado: `appboy_cc_icon_pinned`

Como las tarjetas de contenido tienen un tamaño máximo de 2 KB para el contenido que introduzcas en el panel (incluido el texto del mensaje, las URL de las imágenes, los enlaces y todos los pares clave-valor), comprueba el tamaño antes de enviarlas. Si se supera esta cantidad, no se podrá enviar la tarjeta.

{% alert important %}
La sustitución de imágenes predeterminadas no se admite actualmente en nuestra integración con iOS de Xamarin.
{% endalert %}

## Desactivar el modo oscuro

Para evitar que la interfaz de usuario de la tarjeta de contenido adopte un estilo de tema oscuro cuando el dispositivo del usuario tenga habilitado el modo oscuro, establece la propiedad `ABKContentCardsTableViewController.enableDarkTheme`. Puedes acceder a la propiedad `enableDarkTheme` directamente en una instancia de `ABKContentCardsTableViewController` o a través de la propiedad `ABKContentCardsViewController.contentCardsViewController` para adaptarla mejor a tu propia interfaz de usuario.

{% tabs %}
{% tab OBJETIVO-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

