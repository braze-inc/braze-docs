---
nav_title: Fuente personalizada
article_title: Personalizar la fuente predeterminada de la tarjeta de contenido
page_order: 3
description: "Este artículo trata de las opciones de personalización de la fuente de la tarjeta de contenido."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalizar la fuente predeterminada de la tarjeta de contenido

> Una fuente de tarjetas de contenido es la secuencia de tarjetas de contenido en tus aplicaciones móviles o Web. Este artículo cubre la configuración de cuándo se actualiza la fuente, el orden de las tarjetas, la gestión de múltiples fuentes y los mensajes de error de "fuente vacía". Para obtener un resumen básico de los tipos de opciones de personalización que tienes con las tarjetas de contenido, consulta [Resumen de la personalización]({{site.baseurl}}/developer_guide/customization_guides/customization_overview). 

## Actualizar la fuente

Por predeterminado, la fuente de la tarjeta de contenido se actualizará automáticamente en las siguientes instancias: 
1. Se inicia una nueva sesión
2. Cuando se abre la fuente y han transcurrido más de 60 segundos desde la última actualización

También puedes configurar el SDK para que se actualice manualmente a determinadas horas.

{% alert tip %}
Para mostrar dinámicamente tarjetas de contenido actualizadas sin actualizarlas manualmente, selecciona **En la primera impresión** durante la creación de la tarjeta. Estas tarjetas se actualizarán cuando estén disponibles.
{% endalert %}

{% tabs local %}
{% tab Android %}

Solicita una actualización manual de las tarjetas de contenido de Braze desde el SDK de Android en cualquier momento llamando a [`requestContentCardsRefresh`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-content-cards-refresh.html). 

{% subtabs local %}
{% subtab Java %}

```java
Braze.getInstance(context).requestContentCardsRefresh();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestContentCardsRefresh()
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

Solicita una actualización manual de las tarjetas de contenido de Braze desde el SDK Swift en cualquier momento llamando al método [`requestRefresh`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh(_:)) en la clase [`Braze.ContentCards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class):

{% subtabs local %}
{% subtab Swift %}

En Swift, las tarjetas de contenido pueden actualizarse con un controlador de finalización opcional o con un retorno asíncrono utilizando las API de concurrencia nativas de Swift.

### Controlador de finalización

```swift
AppDelegate.braze?.contentCards.requestRefresh { result in
  // Implement completion handler
}
```

### Async/Espera

```swift
let contentCards = await AppDelegate.braze?.contentCards.requestRefresh()
```
{% endsubtab %}
{% subtab Objective-C %}

```objc
[AppDelegate.braze.contentCards requestRefreshWithCompletion:^(NSArray<BRZContentCardRaw *> * contentCards, NSError * error) {
  // Implement completion handler
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Solicita una actualización manual de las tarjetas de contenido de Braze desde el SDK Web en cualquier momento llamando a [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

También puedes llamar a [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) para obtener todas las tarjetas actualmente disponibles desde la última actualización de las Tarjetas de Contenido. 

```javascript
import * as braze from "@braze/web-sdk";

function refresh() {
  braze.requestContentCardsRefresh();    
}
```

{% endtab %}
{% endtabs %}


{% alert important %}
Puedes hacer hasta cinco llamadas seguidas. Después, habrá una nueva llamada disponible cada 180 segundos. El sistema retendrá hasta cinco llamadas para que las utilices en cualquier momento.
{% endalert %}

## Personalizar el pedido de tarjeta mostrado

Puedes cambiar el orden en que se muestran tus tarjetas de contenido. Esto te permite ajustar la experiencia del usuario dando prioridad a determinados tipos de contenido, como las promociones sensibles al tiempo.

{% tabs %}
{% tab Sistema de visualización de Android %}

El sitio [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) se basa en un [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html) para gestionar cualquier ordenación o modificación de las tarjetas de contenido antes de que se muestren en la fuente. Se puede configurar un controlador de actualizaciones personalizado a través de [`setContentCardUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html) en tu `ContentCardsFragment`.

El siguiente es el predeterminado `IContentCardsUpdateHandler` y puede utilizarse como punto de partida para su personalización:

{% subtabs local %}
{% subtab Java %}

```java
public class DefaultContentCardsUpdateHandler implements IContentCardsUpdateHandler {

  // Interface that must be implemented and provided as a public CREATOR
  // field that generates instances of your Parcelable class from a Parcel.
  public static final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable.Creator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    List<Card> sortedCards = event.getAllCards();
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    Collections.sort(sortedCards, new Comparator<Card>() {
      @Override
      public int compare(Card cardA, Card cardB) {
        // A displays above B
        if (cardA.getIsPinned() && !cardB.getIsPinned()) {
          return -1;
        }

        // B displays above A
        if (!cardA.getIsPinned() && cardB.getIsPinned()) {
          return 1;
        }

        // At this point, both A & B are pinned or both A & B are non-pinned
        // A displays above B since A is newer
        if (cardA.getUpdated() > cardB.getUpdated()) {
          return -1;
        }

        // B displays above A since A is newer
        if (cardA.getUpdated() < cardB.getUpdated()) {
          return 1;
        }

        // At this point, every sortable field matches so keep the natural ordering
        return 0;
      }
    });

    return sortedCards;
  }

  // Parcelable interface method
  @Override
  public int describeContents() {
    return 0;
  }

  // Parcelable interface method
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // No state is kept in this class so the parcel is left unmodified
  }
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event.allCards
    // Sort by pinned, then by the 'updated' timestamp descending
    // Pinned before non-pinned
    sortedCards.sortWith(Comparator sort@{ cardA: Card, cardB: Card ->
      // A displays above B
      if (cardA.isPinned && !cardB.isPinned) {
        return@sort -1
      }

      // B displays above A
      if (!cardA.isPinned && cardB.isPinned) {
        return@sort 1
      }

      // At this point, both A & B are pinned or both A & B are non-pinned
      // A displays above B since A is newer
      if (cardA.updated > cardB.updated) {
        return@sort -1
      }

      // B displays above A since A is newer
      if (cardA.updated < cardB.updated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // Parcelable interface method
  override fun describeContents(): Int {
    return 0
  }

  // Parcelable interface method
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // No state is kept in this class so the parcel is left unmodified
  }

  companion object {
    // Interface that must be implemented and provided as a public CREATOR
    // field that generates instances of your Parcelable class from a Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Array<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
}
```

{% endsubtab %}
{% endsubtabs %}

El código fuente de `ContentCardsFragment` está disponible en [GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.kt).

{% endtab %}
{% tab Jetpack Compose %}
Para filtrar y ordenar las tarjetas de contenido en Jetpack Compose, configura el parámetro `cardUpdateHandler`. Por ejemplo:

```kotlin
ContentCardsList(
    cardUpdateHandler = {
        it.sortedWith { cardA, cardB ->
            // A displays above B
            if (cardA.isPinned && !cardB.isPinned) {
                return@sortedWith -1
            }
            // B displays above A
            if (!cardA.isPinned && cardB.isPinned) {
                return@sortedWith 1
            }
            // At this point, both A & B are pinned or both A & B are non-pinned
            // A displays above B since A is newer
            if (cardA.updated > cardB.updated) {
                return@sortedWith -1
            }
            // B displays above A since A is newer
            if (cardA.updated < cardB.updated) {
                return@sortedWith 1
            }
            0
        }
    }
)
```
{% endtab %}
{% tab iOS %}

{% subtabs %}
{% subtab Swift %}

Personaliza el orden de la fuente de tarjetas modificando directamente la variable estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
    cards.sorted {
        if $0.pinned && !$1.pinned {
            return true
        } else if !$0.pinned && $1.pinned {
            return false
        } else {
            return $0.createdAt > $1.createdAt
        }
    }
}
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

La personalización a través de `BrazeContentCardUI.ViewController.Attributes` no está disponible en Objective-C. 

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Personaliza el orden de visualización de las tarjetas de contenido en tu fuente utilizando el parámetro [`filterFunction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) de `showContentCards():`. Por ejemplo:

```javascript
braze.showContentCards(null, (cards) => {
  return sortBrazeCards(cards); // Where sortBrazeCards is your sorting function that returns the sorted card array
});
```

{% endtab %}
{% endtabs %}

## Mensaje personalizado de "fuente vacía".

Cuando un usuario no tiene derecho a ninguna tarjeta de contenido, el SDK muestra un mensaje de error de "fuente vacía" que indica lo siguiente: "No tenemos actualizaciones. Vuelve a comprobarlo más tarde". Puedes personalizar este mensaje de error de "fuente vacía" de forma similar a la siguiente:

![Un mensaje de error de fuente vacía que dice "Este es un mensaje personalizado de estado vacío".]({% image_buster/assets/img/content_cards/content-card-customization-empty.png %})

{% tabs %}
{% tab Sistema de visualización de Android %}

Si el [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) determina que el usuario no tiene derecho a ninguna tarjeta de contenido, muestra el mensaje de error de fuente vacía.

Un adaptador especial, el [`EmptyContentCardsAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/EmptyContentCardsAdapter.kt)sustituye al [`ContentCardAdapter`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/adapters/ContentCardAdapter.kt) estándar para mostrar este mensaje de error. Para configurar el propio mensaje personalizado, anula el recurso de cadena `com_braze_feed_empty`.

El estilo utilizado para mostrar este mensaje se puede encontrar a través de [`Braze.ContentCardsDisplay.Empty`](https://github.com/braze-inc/braze-android-sdk/blob/2e386dfa59a87bfc24ef7cb6ff5adf6b16f44d24/android-sdk-ui/src/main/res/values/styles.xml#L522-L530) y se reproduce en el siguiente fragmento de código:

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  <item name="android:lineSpacingExtra">1.5dp</item>
  <item name="android:text">@string/com_braze_feed_empty</item>
  <item name="android:textColor">@color/com_braze_content_card_empty_text_color</item>
  <item name="android:textSize">18.0sp</item>
  <item name="android:gravity">center</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent</item>
</style>
```

Para obtener más información sobre la personalización de los elementos de estilo de la tarjeta de contenido, consulta [Personalizar el estilo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles).
{% endtab %}
{% tab Jetpack Compose %}
Para personalizar el mensaje de error "fuente vacía" con Jetpack Compose, puedes pasar un `emptyString` a `ContentCardsList`. También puedes pasar `emptyTextStyle` a `ContentCardListStyling` para personalizar aún más este mensaje.

```kotlin
ContentCardsList(
    emptyString = "No messages today",
    style = ContentCardListStyling(
        emptyTextStyle = TextStyle(...)
    )
)
```

Si tienes un Composable que te gustaría mostrar en su lugar, puedes pasar `emptyComposable` a `ContentCardsList`. Si se especifica `emptyComposable`, no se utilizará `emptyString`.

```kotlin
ContentCardsList(
    emptyComposable = {
        Image(
            painter = painterResource(id = R.drawable.noMessages),
            contentDescription = "No messages"
        )
    }
)
```
{% endtab %}
{% tab iOS %}
{% subtabs local %}
{% subtab Swift %}

Personaliza el estado de vacío del controlador de vista configurando los parámetros relacionados [`Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.emptyStateMessage = "This is a custom empty state message"
attributes.emptyStateMessageFont = .preferredFont(forTextStyle: .title1)
attributes.emptyStateMessageColor = .secondaryLabel
```

{% endsubtab %}
{% subtab Objective-C %}

Cambia el idioma que aparece automáticamente en las fuentes vacías de la tarjeta de contenido redefiniendo las cadenas localizables de la tarjeta de contenido en el archivo de tu aplicación [`ContentCardsLocalizable.strings`](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization/en.lproj) de tu aplicación.

{% alert note %}
Si quieres actualizar este mensaje en diferentes idiomas de localización, busca el idioma correspondiente en la [estructura de carpetas Recursos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Sources/BrazeUI/Resources/Localization) con la cadena `ContentCardsLocalizable.strings`.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

El SDK Web no permite sustituir el lenguaje "fuente vacía" mediante programación. Puedes optar por sustituirlo cada vez que se muestre la fuente, pero no es recomendable porque la fuente puede tardar en actualizarse y el texto vacío de la fuente no se mostrará inmediatamente. 

{% endtab %}
{% endtabs %}

## Múltiples fuentes

Las tarjetas de contenido pueden filtrarse en tu aplicación para que sólo se muestren tarjetas específicas, lo que te habilita a tener varias fuentes de tarjetas de contenido para diferentes casos de uso. Por ejemplo, puedes mantener tanto una fuente de transacciones como una fuente de marketing. Para ello, crea diferentes categorías de tarjetas de contenido estableciendo pares clave-valor en el panel de Braze. Después, crea fuentes en tu aplicación o sitio que traten estos tipos de tarjetas de contenido de forma diferente, filtrando algunos tipos y mostrando otros.

### Paso 1: Establecer pares clave-valor en las tarjetas

Al crear una campaña de tarjeta de contenido, establece [datos de par clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/) en cada tarjeta. Utilizarás este par clave-valor para clasificar las tarjetas. Los pares clave-valor se almacenan en la propiedad `extras` del modelo de datos de la tarjeta.

En este ejemplo, estableceremos un par clave-valor con la clave `feed_type` que designará la fuente de la tarjeta de contenido en la que debe mostrarse la tarjeta. El valor será el que tengan tus fuentes personalizadas, como `home_screen` o `marketing`.

### Paso 2: Filtrar tarjetas de contenido

Una vez asignados los pares clave-valor, crea una fuente con una lógica que muestre las tarjetas que deseas mostrar y filtre las tarjetas de otros tipos. En este ejemplo, sólo mostraremos las tarjetas cuyo par clave-valor coincida con `feed_type: "Transactional"`.

{% tabs %}
{% tab Sistema de visualización de Android %}

Puedes filtrar las tarjetas de contenido leyendo los pares clave-valor configurados en el panel mediante [`Card.getExtras()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html) y filtrando (o realizando cualquier otra lógica que desees) mediante un controlador de actualizaciones personalizado.

Para explicarlo mejor, la fuente de tu tarjeta de contenido se muestra en un archivo [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html). El `IContentCardsUpdateHandler` predeterminado toma un [`ContentCardsUpdatedEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html) del SDK de Braze y devuelve una lista de tarjetas para mostrar, pero sólo ordena las tarjetas y no realiza ninguna eliminación ni filtrado por su cuenta.

Para que `ContentCardsFragment` pueda filtrar, crea un archivo personalizado [`IContentCardsUpdateHandler`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html). Modifica este `IContentCardsUpdateHandler` para eliminar de la lista las tarjetas que no coincidan con el valor que deseamos para el `feed_type` que establecimos anteriormente. Por ejemplo:

{% subtabs local %}
{% subtab Java %}

```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```

{% endsubtab %}
{% endsubtabs %}

Una vez que hayas creado un `IContentCardsUpdateHandler`, crea un `ContentCardsFragment` que lo utilice. Esta fuente personalizada puede utilizarse como cualquier otra `ContentCardsFragment`. En las distintas partes de tu aplicación, muestra distintas fuentes de tarjetas de contenido en función de la clave proporcionada en el panel. Cada fuente `ContentCardsFragment` tendrá un conjunto único de tarjetas mostradas gracias a la configuración personalizada `IContentCardsUpdateHandler` de cada fragmento. 

Por ejemplo:

{% subtabs local %}
{% subtab Java %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}
Para filtrar qué tarjetas de contenido se muestran en esta fuente, utiliza `cardUpdateHandler`. Por ejemplo:

```kotlin
ContentCardsList(
     cardUpdateHandler = {
         it.filter { card ->
             card.extras["feed_type"] == "Transactional"
         }
     }
 )
 ```
{% endtab %}
{% tab iOS %}

El siguiente ejemplo mostrará la fuente Tarjetas de contenido para las tarjetas de tipo `Transactional`:

{% subtabs %}
{% subtab Swift %}

```swift
// Filter cards by the `Transactional` feed type based on your key-value pair.
let transactionalCards = cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
```

Para ir un paso más allá, las tarjetas presentadas en el controlador de vista pueden filtrarse configurando la propiedad `transform` en tu estructura `Attributes` para mostrar sólo las tarjetas filtradas según tus criterios.

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.filter { $0.extras["feed_type"] as? String == "Transactional" }
}

// Pass your attributes containing the transformed cards to the Content Card UI.
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Filter cards by the `Transactional` feed type based on your key-value pair.
NSMutableArray<BRZContentCardRaw *> *transactionalCards = [[NSMutableArray alloc] init];
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if ([card.extras[@"feed_type"] isEqualToString:@"Transactional"]) {
    [transactionalCards addObject:card];
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

El siguiente ejemplo mostrará la fuente Tarjetas de contenido para las tarjetas de tipo `Transactional`:

```javascript

/**
 * @param {String} feed_type - value of the "feed_type" KVP to filter
 */
function showCardsByFeedType(feed_type) {
  braze.showContentCards(null, function(cards) {
    return cards.filter((card) => card.extras["feed_type"] === feed_type);
  });
}
```

A continuación, puedes alternar tu fuente personalizada:

```javascript
// show the "Transactional" feed when this button is clicked
document.getElementById("show-transactional-feed").onclick = function() {
  showCardsByFeedType("Transactional"); 
};
```

Para más información, consulta la [documentación del método SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards).

{% endtab %}
{% endtabs %}


