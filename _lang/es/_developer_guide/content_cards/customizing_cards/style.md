---
nav_title: Estilo
article_title: Personalizar el estilo de las tarjetas de contenido
page_order: 1
description: "Este artículo trata de las opciones de estilo para tus tarjetas de contenido."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar el estilo de las tarjetas de contenido

> Las tarjetas de contenido Braze tienen un aspecto predeterminado. Este artículo trata de las opciones de estilo de tus tarjetas de contenido para ayudarte a que coincidan con la identidad de tu marca. Para ver la lista completa de tipos de tarjetas de contenido, consulta [Acerca de las tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/).

## Crear un estilo personalizado

La interfaz de usuario predeterminada de las tarjetas de contenido se importa de la capa de interfaz de usuario del SDK de Braze. A partir de ahí, puedes ajustar ciertas partes del estilo de la tarjeta, el orden en que se muestran las tarjetas y cómo se muestra la fuente a tus usuarios.

![Dos tarjetas de contenido, una con la fuente predeterminada y esquinas cuadradas, y otra con esquinas redondeadas y una fuente rizada]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Las propiedades de las tarjetas de contenido, como `title`, `cardDescription`, `imageUrl`, etc., se pueden editar directamente a través del [panel]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details), que es el método preferido para cambiar estos detalles.
{% endalert %}


{% tabs %}
{% tab android %}

Por defecto, las tarjetas de contenido SDK de Android y FireOS se ajustan a las directrices de la interfaz de usuario estándar de Android para ofrecer una experiencia sin fisuras. Puedes ver estos estilos predeterminados en el archivo [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) de la distribución del SDK de Braze:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

Para personalizar el estilo de tu tarjeta de contenido, anula este estilo predeterminado. Para anular un estilo, cópialo en su totalidad en el archivo `styles.xml` de tu proyecto y haz modificaciones. Debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados.

{% subtabs local %}
{% subtab Correct style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

{% endsubtab %}
{% subtab Incorrect style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

Por defecto, las tarjetas de contenido SDK de Android y FireOS se ajustan a las directrices de la interfaz de usuario estándar de Android para ofrecer una experiencia sin fisuras.

Puedes aplicar el estilizado de dos formas. La primera consiste en pasar un [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) y [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) a [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)como en el ejemplo siguiente:

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

La segunda es utilizar [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) para crear un estilo global para los componentes Braze, como en el siguiente ejemplo:

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

{% endtab %}
{% tab swift %}

El controlador de vista Tarjetas de contenido te permite personalizar el aspecto y el comportamiento de todas las celdas mediante la estructura [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) estructura. Configurar las tarjetas de contenido mediante `Attributes` es una opción sencilla, que te permite lanzar tu interfaz de usuario de tarjetas de contenido con una configuración mínima. 

{% alert important %}
La personalización a través de `Attributes` sólo está disponible en Swift.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modificación de `Attributes.default`**

Personaliza el aspecto de todas las instancias del controlador de vista de interfaz de usuario de la tarjeta de contenido Braze modificando directamente la variable estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults) estática.

Por ejemplo, para cambiar el tamaño predeterminado de la imagen y el radio de las esquinas de todas las celdas:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Inicializar el controlador de vista con atributos**

Si deseas modificar sólo una instancia específica del controlador de vista de la interfaz de usuario de la tarjeta de contenido Braze, utiliza el inicializador [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) inicializador para pasar una estructura personalizada `Attributes` al controlador de vista.

Por ejemplo, puedes cambiar el tamaño de la imagen y el radio de la esquina para una instancia concreta del controlador de vista:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Celdas personalizadas mediante subclases**

También puedes crear interfaces personalizadas registrando clases personalizadas para cada tipo de tarjeta que desees. Para utilizar tu subclase en lugar de la celda predeterminada, modifica la propiedad [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) en la estructura `Attributes`. Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modificar tarjetas de contenido mediante programación**

Las tarjetas de contenido pueden modificarse mediante programación asignando el cierre [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) a tu estructura `Attributes`. El ejemplo siguiente modifica las direcciones `title` y `description` de las tarjetas compatibles:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.map { card in
    var card = card
    if let title = card.title {
      card.title = "[modified] \(title)"
    }
    if let description = card.description {
      card.description = "[modified] \(description)"
    }
    return card
  }
}

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consulta el [ejemplo de aplicación Ejemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para ver un ejemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

La personalización de las tarjetas de contenido a través de `Attributes` no es compatible con Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Los estilos predeterminados de Braze se definen en CSS dentro del SDK de Braze. Anulando los estilos seleccionados en tu aplicación, es posible personalizar nuestra fuente estándar con tus propias imágenes de fondo, familias de fuentes, estilos, tamaños, animaciones y mucho más. Por instancia, el siguiente es un ejemplo de modificación que hará que las tarjetas de contenido aparezcan con un ancho de 800 px:

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## Ejemplos de personalización

### Fuente personalizada

Personalizar el tipo de letra utilizado en tus tarjetas de contenido te permite mantener la identidad de tu marca y crear una experiencia visualmente atractiva para tus usuarios. Utiliza estas recetas para establecer la fuente de todas las tarjetas de contenido mediante programación. 

{% tabs %}
{% tab android %}

Para cambiar la fuente predeterminada mediante programación, establece un estilo para las tarjetas y utiliza el atributo `fontFamily` para indicar a Braze que utilice tu familia de fuentes personalizada.

Por ejemplo, para actualizar el tipo de letra de todos los títulos de las tarjetas con imágenes subtituladas, anula el estilo `Braze.ContentCards.CaptionedImage.Title` y haz referencia a tu familia de fuentes personalizada. El valor del atributo debe apuntar a una familia de fuentes de tu directorio `res/font`.

Aquí tienes un ejemplo truncado con una familia de fuentes personalizada, `my_custom_font_family`, a la que se hace referencia en la última línea:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Para más información sobre la personalización de fuentes en el SDK de Android, consulta la [guía de familias de fuentes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
Para cambiar el tipo de letra predeterminado mediante programación, puedes configurar el botón [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) de `ContentCardStyling`.

También puedes configurar `titleTextStyle` para un tipo de tarjeta específico configurándolo en [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) y pasándolo a la función [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) de `ContentCardStyling`.

```kotlin
val fontFamily = FontFamily(
    Font(R.font.sailec_bold)
)

ContentCardStyling(
    titleTextStyle = TextStyle(
        fontFamily = fontFamily
    )
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personaliza tus fuentes personalizando la dirección `Attributes` de la propiedad de instancia [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización de fuentes a través de `Attributes` no es compatible con Objective-C. 

Consulta la [aplicación de muestra Ejemplos](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) para ver un ejemplo de cómo crear tu propia interfaz de usuario con fuentes personalizadas.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Al igual que cualquier otro elemento Web, puedes personalizar fácilmente el aspecto de las tarjetas de contenido mediante CSS. En tu archivo CSS o en los estilos en línea, utiliza la propiedad `font-family` y especifica el nombre de la fuente deseada o la pila de fuentes.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% endtabs %}

### Iconos personalizados anclados

Al crear una tarjeta de contenido, los especialistas en marketing tienen la opción de anclarla. Una tarjeta anclada se mostrará en la parte superior de la fuente de un usuario y no podrá ser descartada por el usuario. Al personalizar los estilos de tus tarjetas, tienes la posibilidad de cambiar el aspecto del icono anclado.

![Vista previa, lado a lado, de la tarjeta de contenido en Braze para Móvil y Web con la opción "Anclar esta tarjeta a la parte superior de la fuente" seleccionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab android %}

Para establecer un icono personalizado anclado, anula el estilo de `Braze.ContentCards.PinnedIcon`. Tu activo de imagen personalizado debe declararse en el elemento `android:src`. Por ejemplo:

```xml
  <style name="Braze.ContentCards.PinnedIcon">
    <item name="android:src">@drawable/{my_custom_image_here}</item>

    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_alignParentRight">true</item>
    <item name="android:layout_alignParentTop">true</item>
    <item name="android:contentDescription">@null</item>
    <item name="android:importantForAccessibility">no</item>
  </style>
```

{% endtab %}
{% tab Jetpack Compose %}

Para cambiar el icono predeterminado anclado, puedes configurar el botón [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) de `ContentCardStyling`.  Por ejemplo:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

También puedes especificar un Composable en [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) de `ContentCardStyling`. Si se especifica `pinnedComposable`, anulará el valor de `pinnedResourceId`.

```kotlin
ContentCardStyling(
    pinnedComposable = {
        Box(Modifier.fillMaxWidth()) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .width(50.dp),
                text = "This message is not read. Please read it."
            )
        }
    }
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personaliza el ícono del pin modificando las propiedades `pinIndicatorColor` y `pinIndicatorImage` de la propiedad de instancia [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por ejemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

También puedes utilizar la subclase para crear tu propia versión personalizada de `BrazeContentCardUI.Cell`, que incluye el indicador de pin. Por ejemplo: 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización del indicador de pin mediante `Attributes` no es compatible con Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

La estructura del icono de la tarjeta anclada de contenido es:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Si quieres utilizar un icono FontAwesome diferente, sólo tienes que sustituir el nombre de clase del elemento `i` por el nombre de clase del icono deseado. 

Si quieres cambiar el icono por completo, elimina el elemento `i` y añade el icono personalizado como hijo de `ab-pinned-indicator`. Hay varias formas de hacerlo, pero un método sencillo sería `replaceChildren()` en el elemento `ab-pinned-indicator`.

Por ejemplo:

```javascript
// Get the parent element
const pinnedIndicator = document.querySelector('.ab-pinned-indicator');

// Create a new custom icon element
const customIcon = document.createElement('span');
customIcon.classList.add('customIcon');

// Replace the existing icon with the custom icon
pinnedIndicator.replaceChildren(customIcon);
```

{% endtab %}
{% endtabs %}

### Cambiar el color de los indicadores no leídos

Las tarjetas de contenido contienen una línea azul en la parte inferior de la tarjeta que indica si la tarjeta ha sido vista o no. 

![Dos tarjetas de contenido expuestas una al lado de la otra. La primera tarjeta tiene una línea azul en la parte inferior, lo que indica que no ha sido vista. La segunda tarjeta no tiene una línea azul, lo que indica que ya ha sido vista.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab android %}

Cambia el color de la barra indicadora de no leídos modificando el valor en `com_braze_content_cards_unread_bar_color` en tu archivo `colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Para cambiar el color de la barra indicadora de no leídos, modifica el valor de [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) en `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Cambia el color de la barra indicadora de no leídos asignando un valor al color de tinte de tu instancia `BrazeContentCardUI.ViewController`:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

Sin embargo, si sólo deseas modificar el indicador no visualizado, puedes acceder a la propiedad `unviewedIndicatorColor` de tu estructura `BrazeContentCardUI.ViewController.Attributes`. Si utilizas implementaciones de Braze `UITableViewCell`, debes acceder a la propiedad antes de que se dibuje la celda.

Por ejemplo, para establecer el color del indicador de no visto en rojo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Consulta el [ejemplo de aplicación Ejemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para ver un ejemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

Cambia el color de la barra indicadora de no leídos asignando un valor al color de tinte de tu `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

En Objective-C no es posible personalizar sólo el indicador no visualizado a través de `Attributes`.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Para cambiar el color del indicador no leídos de una tarjeta, añade CSS personalizado a tu página web. Por ejemplo, para establecer el color del indicador de no visto en verde:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% endtabs %}

### Desactivar indicador no leídos

{% tabs %}
{% tab android %}

Oculta la barra de indicadores no leídos configurando [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) en `ContentCardViewHolder` a `false`. 

{% endtab %}

{% tab Jetpack Compose %}
Desactivar el indicador de no leídos no es compatible con Jetpack Compose.
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Oculta la barra de indicadores no leídos estableciendo la propiedad `attributes.cellAttributes.unviewedIndicatorColor` de tu estructura `Attributes` en `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

En Objective-C no es posible personalizar sólo el indicador no visualizado a través de `Attributes`.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Oculta la barra de indicadores no leídos añadiendo el siguiente estilo a tu `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}
