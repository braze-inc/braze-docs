> Al crear una interfaz de usuario personalizada para las Tarjetas de contenido, debes registrar manualmente los datos de análisis, como las impresiones, los clics y los descartes, ya que esto solo se gestiona automáticamente para los modelos de tarjetas predeterminados. El registro de estos eventos es una parte estándar de la integración de Tarjetas de contenido y es esencial para la elaboración de informes precisos sobre las campañas y la facturación. Para ello, rellena tu interfaz de usuario personalizada con datos de los modelos de datos de Braze y, a continuación, registra manualmente los eventos. Una vez que entiendas cómo registrar los análisis, podrás ver las formas habituales en que los clientes de Braze [crean Tarjetas de contenido personalizadas]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Registro de análisis

Al implementar tus Tarjetas de contenido personalizadas, puedes analizar los objetos de la tarjeta de contenido y extraer sus datos de carga útil, como `title`, `cardDescription` e `imageUrl`. A continuación, puedes utilizar los datos del modelo resultante para rellenar tu interfaz de usuario personalizada. 

Para obtener los modelos de datos de la tarjeta de contenido, suscríbete a las actualizaciones de la tarjeta de contenido. Hay dos propiedades a las que debes prestar especial atención:

* **`id`**: Representa la cadena ID de la tarjeta de contenido. Es el identificador único utilizado para registrar los análisis de las Tarjetas de contenido personalizadas.
* **`extras`**: Engloba todos los pares clave-valor del panel de Braze. 

Todas las propiedades fuera de `id` y `extras` son opcionales de analizar para las Tarjetas de contenido personalizadas. Para más información sobre el modelo de datos, consulta el artículo de integración de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
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
Las Tarjetas de contenido solo se actualizarán al iniciar la sesión si se llama a una solicitud de suscripción antes de `openSession()`. También puedes [actualizar manualmente la fuente]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Paso 1: Crear una variable privada de suscriptor

Para suscribirte a las actualizaciones de las tarjetas, primero declara una variable privada en tu clase personalizada para que contenga tu suscriptor:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Paso 2: Suscribirse a las actualizaciones

A continuación, añade el siguiente código para suscribirte a las actualizaciones de Tarjetas de contenido de Braze, normalmente dentro del `Activity.onCreate()` de la actividad de tus Tarjetas de contenido personalizadas:

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

### Paso 3: Cancelar suscripción

También te recomendamos cancelar la suscripción cuando tu actividad personalizada deje de estar visible. Añade el siguiente código al método del ciclo de vida `onDestroy()` de tu actividad:

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

### Paso 2: Suscribirse a las actualizaciones

A continuación, añade el siguiente código para suscribirte a las actualizaciones de Tarjetas de contenido de Braze, normalmente dentro del `Activity.onCreate()` de la actividad de tus Tarjetas de contenido personalizadas:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Paso 3: Cancelar suscripción

También te recomendamos cancelar la suscripción cuando tu actividad personalizada deje de estar visible. Añade el siguiente código al método del ciclo de vida `onDestroy()` de tu actividad:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acceder al modelo de datos de las Tarjetas de contenido, llama a [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) en tu instancia `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Además, también puedes mantener una suscripción para observar los cambios en tus Tarjetas de contenido. Puedes hacerlo de dos maneras: 
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

Además, si deseas mantener una suscripción a tus Tarjetas de contenido, puedes llamar a [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Para obtener los datos de la tarjeta de contenido, utiliza el método `getContentCards`:

```javascript
import Braze from "@braze/react-native-sdk";

const cards = await Braze.getContentCards();
```

Para estar al tanto de las actualizaciones, suscríbete a los eventos de actualización de la tarjeta de contenido:

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Para solicitar una actualización manual de las Tarjetas de contenido desde los servidores de Braze:

```javascript
Braze.requestContentCardsRefresh();
```

Para obtener Tarjetas de contenido almacenadas en caché sin una solicitud de red:

```javascript
const cachedCards = await Braze.getCachedContentCards();
```

{% endtab %}
{% endtabs %}

## Registro de eventos

Registrar métricas valiosas como impresiones, clics y descartes es rápido y sencillo. Configura un receptor de clics personalizado para gestionar manualmente estos análisis.

{% tabs %}
{% tab web %}

Registra eventos de impresión cuando los usuarios ven las tarjetas utilizando [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Registra los eventos de clic en tarjetas cuando los usuarios interactúan con una tarjeta utilizando [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

[`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) puede hacer referencia a las dependencias del SDK de Braze, como la lista de objetos de la tarjeta de contenido, para obtener el [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) y llamar a los métodos de registro de Braze. Utiliza la clase base `ContentCardable` para referenciar y proporcionar datos fácilmente a `BrazeManager`. 

Para registrar una impresión o un clic en una tarjeta, llama a [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) o [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivamente. 

Puedes registrar manualmente o establecer una tarjeta de contenido como "descartada" en Braze para una tarjeta concreta con [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Si una tarjeta ya está marcada como descartada, no se puede volver a marcar como descartada.

Para crear un receptor de clics personalizado, crea una clase que implemente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) y regístrala con [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implementa el método [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), que se ejecutará cuando el usuario haga clic en una tarjeta de contenido. A continuación, indica a Braze que utilice tu receptor de clics de la tarjeta de contenido. 

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
Para manejar Tarjetas de contenido con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.{% endalert %}

{% endtab %}

{% tab swift %}

Implementa el protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) y establece tu objeto delegado como la propiedad `delegate` de tu `BrazeContentCardUI.ViewController`. Este delegado se encargará de devolver los datos de tu objeto personalizado a Braze para que los registre. Para ver un ejemplo, consulta el [tutorial de la interfaz de usuario de las Tarjetas de contenido](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

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
Para manejar Tarjetas de contenido con variantes de control en tu interfaz de usuario personalizada, pasa tu objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) y llama al método `logImpression` como harías con cualquier otro tipo de tarjeta de contenido. El objeto registrará implícitamente una impresión de control para informar a nuestros análisis de cuándo un usuario habría visto la tarjeta de control.
{% endalert %}
{% endtab %}

{% tab react native %}

Registra eventos de impresión cuando los usuarios ven las tarjetas:

```javascript
Braze.logContentCardImpression(card.id);
```

Registra eventos de clic en tarjetas cuando los usuarios interactúan con una tarjeta:

```javascript
Braze.logContentCardClicked(card.id);
```

Registra los eventos de descarte cuando un usuario descarta una tarjeta:

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Gestión del comportamiento al hacer clic

{% tabs %}
{% tab web %}

Cuando un usuario hace clic en una tarjeta de contenido en una fuente personalizada, el comportamiento al hacer clic (como navegar a una URL, vinculación en profundidad o registrar un evento personalizado) no se gestiona automáticamente. Utiliza [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) para procesar la URL de la tarjeta y ejecutar la acción configurada al hacer clic, incluidas las acciones de Braze (URLs `brazeActions://`).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Parámetro | Descripción |
|---|---|
| `url` | Una URL válida, o una URL de acción de Braze válida con el esquema `brazeActions://`. |
| `openLinkInNewTab` | (Opcional) Si la URL debe abrirse en una nueva pestaña. El valor predeterminado es `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Si no llamas a `handleBrazeAction()`, los comportamientos al hacer clic configurados en el panel de Braze (como "Registrar evento personalizado" o "Navegar a URL") no se ejecutarán para las tarjetas mostradas en una fuente personalizada.
{% endalert %}

{% endtab %}
{% tab android %}

El comportamiento al hacer clic se gestiona automáticamente por la interfaz de usuario predeterminada de Tarjetas de contenido. Para implementaciones personalizadas, utiliza la interfaz [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) descrita en la sección [Registro de análisis](#logging-analytics) anterior.

{% endtab %}
{% tab swift %}

El comportamiento al hacer clic se gestiona automáticamente por la interfaz de usuario predeterminada de Tarjetas de contenido. Para implementaciones personalizadas, utiliza el protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) descrito en la sección [Registro de análisis](#logging-analytics) anterior.

{% endtab %}
{% endtabs %}