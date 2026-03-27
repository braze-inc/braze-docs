---
nav_title: Crear tarjetas
article_title: Crear tarjetas de contenido
page_order: 0
description: "Este artículo trata sobre los componentes necesarios para crear una interfaz de usuario personalizada para Tarjetas de contenido."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Crear tarjetas de contenido

> Este artículo describe el enfoque básico que utilizarás al implementar Tarjetas de contenido personalizadas, así como tres casos de uso comunes. Asume que ya has leído los demás artículos de la guía de personalización de Tarjetas de contenido para comprender qué se puede hacer de forma predeterminada y qué requiere código personalizado. Es especialmente útil comprender cómo [registrar los análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) de tus Tarjetas de contenido personalizadas. 

{% multi_lang_include banners/content_card_alert.md %}

## Crear una tarjeta

### Paso 1: Crea una interfaz de usuario personalizada 

{% tabs local %}
{% tab web %}

En primer lugar, crea tu componente HTML personalizado que se utilizará para representar las tarjetas. 

{% endtab %}
{% tab android %}

Primero, crea tu propio fragmento personalizado. El [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) predeterminado solo está diseñado para manejar nuestros tipos predeterminados de Tarjetas de contenido, pero es un buen punto de partida.

{% endtab %}
{% tab swift %}

Primero, crea tu propio componente de controlador de vista personalizado. El [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) predeterminado solo está diseñado para manejar nuestros tipos predeterminados de Tarjetas de contenido, pero es un buen punto de partida.

{% endtab %}
{% endtabs %}

### Paso 2: Suscribirse a las actualizaciones de tarjetas

Registra una función de devolución de llamada para suscribirte a las actualizaciones de datos cuando se actualicen las tarjetas. Puedes analizar los objetos de tarjeta de contenido y extraer los datos de su carga útil, como `title`, `cardDescription` e `imageUrl`, y luego usar los datos del modelo resultante para rellenar tu interfaz de usuario personalizada.

Para obtener los modelos de datos de las Tarjetas de contenido, suscríbete a las actualizaciones de Tarjetas de contenido. Presta especial atención a las siguientes propiedades:

* **`id`:** Representa la cadena de ID de la tarjeta de contenido. Es el identificador único utilizado para registrar análisis de Tarjetas de contenido personalizadas.
* **`extras`:** Engloba todos los pares clave-valor del panel de Braze. 

Todas las propiedades fuera de `id` y `extras` son opcionales de analizar para Tarjetas de contenido personalizadas. Para más información sobre el modelo de datos, consulta el artículo de integración de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).

{% tabs local %}
{% tab web %}

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
Las Tarjetas de contenido solo se actualizan al inicio de la sesión si se llama a `subscribeToContentCardsUpdates()` antes de `openSession()`. También puedes [actualizar manualmente la fuente]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) en cualquier momento.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Paso 2a: Crea una variable de suscriptor privada

Para suscribirte a las actualizaciones de tarjetas, primero declara una variable privada en tu clase personalizada para almacenar tu suscriptor:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Paso 2b: Suscríbete a las actualizaciones

Añade el siguiente código para suscribirte a las actualizaciones de Tarjetas de contenido de Braze, normalmente dentro del `Activity.onCreate()` de tu actividad personalizada de Tarjetas de contenido:

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

#### Paso 2c: Cancela la suscripción

Cancela la suscripción cuando tu actividad personalizada deje de estar visible. Añade el siguiente código al método de ciclo de vida `onDestroy()` de tu actividad:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Paso 2a: Crea una variable de suscriptor privada

Para suscribirte a las actualizaciones de tarjetas, primero declara una variable privada en tu clase personalizada para almacenar tu suscriptor:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Paso 2b: Suscríbete a las actualizaciones

Añade el siguiente código para suscribirte a las actualizaciones de Tarjetas de contenido de Braze, normalmente dentro del `Activity.onCreate()` de tu actividad personalizada de Tarjetas de contenido:

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

#### Paso 2c: Cancela la suscripción

Cancela la suscripción cuando tu actividad personalizada deje de estar visible. Añade el siguiente código al método de ciclo de vida `onDestroy()` de tu actividad:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acceder al modelo de datos de las Tarjetas de contenido, llama a [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) en tu instancia de `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Además, puedes mantener una suscripción para observar los cambios en tus Tarjetas de contenido. Puedes hacerlo de dos maneras: 
1. Manteniendo un cancelable; o 
2. Manteniendo un `AsyncStream`.

##### Cancelable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Además, si quieres mantener una suscripción a tus Tarjetas de contenido, puedes llamar a [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### Paso 3: Implementar análisis

Las impresiones, clics y descartes de las Tarjetas de contenido no se registran automáticamente en tu vista personalizada. Debes [implementar cada método respectivo]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para registrar correctamente todas las métricas en los análisis del panel de Braze.

### Paso 4: Prueba tu tarjeta (opcional)

Para probar tu tarjeta de contenido:

1. Establece un usuario activo en tu aplicación llamando al método [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
2. En Braze, ve a **Campañas** y [crea una nueva campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. En tu campaña, selecciona **Prueba** y, a continuación, introduce el `user-id` del usuario de prueba. Cuando estés listo, selecciona **Enviar prueba**. En breve podrás lanzar una tarjeta de contenido en tu dispositivo.

![Una campaña de tarjeta de contenido de Braze que muestra que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu tarjeta de contenido.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Colocación de Tarjetas de contenido

Las Tarjetas de contenido pueden utilizarse de muchas formas distintas. Tres implementaciones comunes son utilizarlas como centro de mensajes, anuncio dinámico con imágenes o carrusel de imágenes. Para cada una de estas colocaciones, asignarás [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (la propiedad `extras` del modelo de datos) a tus Tarjetas de contenido y, en función de los valores, ajustarás dinámicamente el comportamiento, el aspecto o la funcionalidad de la tarjeta durante el tiempo de ejecución. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Buzón de entrada de mensajes

Las Tarjetas de contenido pueden utilizarse para simular un centro de mensajes. En este formato, cada mensaje es su propia tarjeta que contiene [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que alimentan los eventos al hacer clic. Estos pares clave-valor son los identificadores clave en los que se fija la aplicación para decidir adónde ir cuando el usuario hace clic en un mensaje del buzón de entrada. Los valores de los pares clave-valor son arbitrarios. 

#### Ejemplo

Por ejemplo, es posible que quieras crear dos tarjetas de mensaje: una llamada a la acción para que los usuarios habiliten las recomendaciones de lectura y un código de cupón para tu nuevo segmento de suscriptores.

Claves como `body`, `title` y `buttonText` pueden tener simples valores de cadena que tus especialistas en marketing pueden establecer. Claves como `terms` pueden tener valores que proporcionen una pequeña colección de frases aprobadas por tu departamento jurídico. Las claves como `style` y `class_type` tienen valores de cadena que puedes configurar para determinar cómo se muestra tu tarjeta en tu aplicación o sitio web.

{% tabs local %}
{% tab Reading recommendations %}
Pares clave-valor de la tarjeta de recomendación de lectura:

| Clave         | Valor                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Añade tus intereses a tu perfil del Semanario Politer para obtener recomendaciones personales de lectura. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
Pares clave-valor para un nuevo cupón de suscriptor:

| Clave         | Valor                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Suscríbete para juegos ilimitados                                    |
| `body`       | Especial fin del verano - Disfruta de un 10 % de descuento en los juegos de Politer              |
| `buttonText` | Suscríbete ahora                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Información adicional para Android %}

En el SDK de Android y FireOS, la lógica del centro de mensajes se rige por el valor `class_type` que proporcionan los pares clave-valor de Braze. Con el método [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/) puedes filtrar e identificar estos tipos de clases.

{% tabs local %}
{% tab Kotlin %}
**Uso de `class_type` para el comportamiento al hacer clic**<br>
Cuando inflamos los datos de la tarjeta de contenido en nuestras clases personalizadas, utilizamos la propiedad `ContentCardClass` de los datos para determinar qué subclase concreta debe utilizarse para almacenar los datos.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Luego, al gestionar la interacción del usuario con la lista de mensajes, podemos utilizar el tipo de mensaje para determinar qué vista mostrar al usuario.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Uso de `class_type` para el comportamiento al hacer clic**<br>
Cuando inflamos los datos de la tarjeta de contenido en nuestras clases personalizadas, utilizamos la propiedad `ContentCardClass` de los datos para determinar qué subclase concreta debe utilizarse para almacenar los datos.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Luego, al gestionar la interacción del usuario con la lista de mensajes, podemos utilizar el tipo de mensaje para determinar qué vista mostrar al usuario.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Carrusel

Puedes configurar Tarjetas de contenido en tu fuente de carrusel totalmente personalizada, permitiendo a los usuarios deslizar y ver tarjetas destacadas adicionales. Por defecto, las Tarjetas de contenido se ordenan por fecha de creación (la más reciente primero), y tus usuarios verán todas las tarjetas para las que son elegibles.

Para implementar un carrusel de Tarjetas de contenido:

1. Crea una lógica personalizada que observe los [cambios en tus Tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) y gestione la llegada de Tarjetas de contenido.
2. Crea una lógica personalizada del lado del cliente para mostrar un número específico de tarjetas en el carrusel en cualquier momento. Por ejemplo, podrías seleccionar los cinco primeros objetos de tarjeta de contenido de la matriz o introducir pares clave-valor para construir lógica condicional en torno a ellos.

{% alert tip %}
Si estás implementando un carrusel como fuente secundaria de Tarjetas de contenido, asegúrate de [ordenar las tarjetas en la fuente correcta utilizando pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Solo imagen

Las Tarjetas de contenido no tienen por qué parecer "tarjetas". Por ejemplo, las Tarjetas de contenido pueden aparecer como una imagen dinámica que se muestra de forma permanente en tu página de inicio o en la parte superior de las páginas designadas.

Para lograrlo, tus especialistas en marketing crearán una campaña o un paso en Canvas con una tarjeta de contenido de tipo **Solo imagen**. A continuación, establece los pares clave-valor adecuados para utilizar [las Tarjetas de contenido como contenido complementario]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).