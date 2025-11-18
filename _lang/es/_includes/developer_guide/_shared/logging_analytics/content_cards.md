> Al crear una interfaz de usuario personalizada para tarjetas de contenido, debes registrar manualmente análisis como impresiones, clics y descartes, ya que esto sólo se gestiona automáticamente para los modelos de tarjeta predeterminados. El registro de estos eventos es una parte estándar de la integración de una tarjeta de contenido y es esencial para la precisión de los informes de campaña y la facturación. Para ello, rellena tu IU personalizada con datos de los modelos de datos Braze y luego registra manualmente los eventos. Una vez que entiendas cómo registrar los análisis, podrás ver las formas habituales en que los clientes de Braze [crean tarjetas de contenido personalizadas]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Escuchar las actualizaciones de las tarjetas

Al implementar tus tarjetas de contenido personalizadas, puedes analizar los objetos de la tarjeta de contenido y extraer sus datos de carga útil, como `title`, `cardDescription` y `imageUrl`. A continuación, puedes utilizar los datos del modelo resultante para rellenar tu interfaz de usuario personalizada. 

Para obtener los modelos de datos de la tarjeta de contenido, suscríbete a las actualizaciones de la tarjeta de contenido. Hay dos propiedades a las que debes prestar especial atención:

* **`id`**: Representa la cadena ID de la tarjeta de contenido. Es el identificador único utilizado para registrar los análisis de las tarjetas de contenido personalizadas.
* **`extras`**: Engloba todos los pares clave-valor del panel Braze. 

Todas las propiedades fuera de `id` y `extras` son opcionales para analizar las tarjetas de contenido personalizadas. Para más información sobre el modelo de datos, consulta el artículo de integración de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

### Paso 1: Crear una variable privada de suscriptor

Para suscribirte a las actualizaciones de las tarjetas, primero declara una variable privada en tu clase personalizada para que contenga tu suscriptor:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Paso 2: Suscribirse a las actualizaciones

A continuación, añade el siguiente código para suscribirte a las actualizaciones de tarjetas de contenido de Braze, normalmente dentro de la actividad de tus tarjetas de contenido personalizadas `Activity.onCreate()`:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### Paso 3: Cancelar suscripción

También te recomendamos cancelar suscripción cuando tu actividad personalizada pase desapercibida. Añade el siguiente código al método del ciclo de vida `onDestroy()` de tu actividad:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Paso 1: Crear una variable privada de suscriptor

Para suscribirte a las actualizaciones de las tarjetas, primero declara una variable privada en tu clase personalizada para que contenga tu suscriptor:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Paso 2: Suscribirse a las actualizaciones

A continuación, añade el siguiente código para suscribirte a las actualizaciones de tarjetas de contenido de Braze, normalmente dentro de la actividad de tus tarjetas de contenido personalizadas `Activity.onCreate()`:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Paso 3: Cancelar suscripción

También te recomendamos cancelar suscripción cuando tu actividad personalizada pase desapercibida. Añade el siguiente código al método del ciclo de vida `onDestroy()` de tu actividad:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acceder al modelo de datos de las tarjetas de contenido, llama a [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) en tu instancia `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Además, también puedes mantener una suscripción para observar los cambios en tus tarjetas de contenido. Puedes hacerlo de dos maneras: 
1. Mantener un cancelable; o 
2. Mantener un `AsyncStream`.

### Cancelable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Además, si deseas mantener una suscripción a tus tarjetas de contenido, puedes llamar a [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Registra una función de devolución de llamada para suscribirte a las actualizaciones cuando se actualicen las tarjetas.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Las tarjetas de contenido sólo se actualizarán al iniciar la sesión si se llama a una petición de suscripción antes de `openSession()`. También puedes [actualizar manualmente el canal]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Registro de eventos

Registrar métricas valiosas como impresiones, clics y descartes es rápido y sencillo. Configura un receptor de clics personalizado para gestionar manualmente estos análisis.

{% tabs %}
{% tab android %}

La página [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) puede hacer referencia a las dependencias del SDK de Braze, como la lista de matrices de objetos de la tarjeta de contenido, para obtener el código [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) para llamar a los métodos de registro Braze. Utiliza la clase base `ContentCardable` para referenciar y proporcionar datos fácilmente a `BrazeManager`. 

Para registrar una impresión o hacer clic en una tarjeta, llama a [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) o [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivamente. 

Puedes registrar manualmente o establecer una tarjeta de contenido como "descartada" en Braze para una tarjeta concreta con [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada.

Para crear un receptor de clics personalizado, crea una clase que implemente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) y regístrala con [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implementa el método [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html) que se ejecutará cuando el usuario haga clic en una tarjeta de contenido. A continuación, indica a Braze que utilice tu oyente de clic de la tarjeta de contenido. 

{% subtabs local %}
{% subtab Java %}

Por ejemplo:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Por ejemplo:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para manejar tarjetas de contenido con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.{% endalert %}

{% endtab %}
{% tab swift %}

Implementa el protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) y establece tu objeto delegado como la propiedad `delegate` de tu `BrazeContentCardUI.ViewController`. Este delegado se encargará de devolver los datos de tu objeto personalizado a Braze para que los registre. Para ver un ejemplo, consulta [el tutorial de la interfaz de usuario de las tarjetas de contenido](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para manejar tarjetas de contenido con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}
{% endtab %}

{% tab web %}

Registrar eventos de impresión cuando las tarjetas son vistas por usuarios que utilizan [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Registra los eventos de clic de tarjeta cuando los usuarios interactúan con una tarjeta utilizando [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% endtabs %}
