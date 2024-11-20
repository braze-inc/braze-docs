---
nav_title: Crear tarjetas de contenido personalizadas
article_title: Crear tarjetas de contenido personalizadas
page_order: 5
description: "Este artículo cubre los componentes de la creación de una interfaz de usuario de tarjeta de contenido personalizada"
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Crear tarjetas de contenido personalizadas

> Este artículo analiza el enfoque básico que utilizarás al implementar tarjetas de contenido personalizadas, así como tres casos de uso comunes: imágenes de banners, un buzón de entrada de mensajes y un carrusel de imágenes. Asume que ya has leído los demás artículos de la guía de personalización de la tarjeta de contenido para comprender qué se puede hacer de forma predeterminada y qué requiere código personalizado. Se trata especialmente de entender cómo [registrar los análisis]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) de tus tarjetas de contenido personalizadas. 

Braze proporciona diferentes [tipos de tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details): `imageOnly`, `captionedImage`, `classic`, `classicImage`, y `control`. Puedes utilizarlos como punto de partida para tus implementaciones, modificando su aspecto. 

También puedes mostrar tarjetas de contenido de forma totalmente personalizada, creando tu propia interfaz de usuario de presentación poblada con datos de los modelos Braze. Analiza los objetos de la tarjeta de contenido y extrae los datos de su carga útil. A continuación, utiliza los datos del modelo resultante para rellenar tu interfaz de usuario personalizada: la fase "de ejecución" del [enfoque "rastrea, camina, ejecuta]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)".

{% alert note %}
Cada tipo predeterminado de tarjeta de contenido es una subclase que hereda distintas propiedades de la clase genérica del modelo de tarjeta de contenido. Comprender estas propiedades heredadas será útil durante la personalización. Consulta la documentación de la clase Tarjeta para obtener todos los detalles[(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)).
{% endalert %}


## Resumen de la personalización

Dependiendo de tu caso de uso, la implementación exacta de tu tarjeta de contenido personalizada variará un poco, pero querrás seguir esta fórmula básica:

1. Construye tu propia interfaz de usuario
2. Escucha las actualizaciones de datos
3. Registra manualmente los análisis

### Paso 1: Crea una interfaz de usuario personalizada 

{% tabs %}
{% tab Android %}

Primero, crea tu propio fragmento personalizado. El [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) predeterminado solo está diseñado para manejar nuestros tipos predeterminados de tarjetas de contenido, pero es un buen punto de partida.

{% endtab %}
{% tab iOS %}

Primero, crea tu propio componente de controlador de vista personalizado. El [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) predeterminado solo está diseñado para manejar nuestros tipos predeterminados de tarjetas de contenido, pero es un buen punto de partida.

{% endtab %}
{% tab Web %}

En primer lugar, crea tu componente HTML personalizado que se utilizará para representar las tarjetas. 

{% endtab %}
{% endtabs %}

### Paso 2: Suscribirse a las actualizaciones de tarjetas

A continuación, registra una función de devolución de llamada para [suscribirte a las actualizaciones de datos]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) cuando se actualicen las tarjetas. 

### Paso 3: Implementar análisis

Las impresiones, clics y descartes de la tarjeta de contenido no se registran automáticamente en tu vista personalizada. Debes [implementar cada método respectivo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) para registrar correctamente todas las métricas de vuelta al análisis del panel de Braze.

## Colocación de tarjetas de contenido

Las tarjetas de contenido pueden utilizarse de muchas formas distintas. Tres implementaciones comunes son utilizarlos como centro de mensajes, banner publicitario o carrusel de imágenes. Para cada una de estas colocaciones, asignarás [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (la propiedad `extras` del modelo de datos) a tus tarjetas de contenido y, en función de los valores, ajustarás dinámicamente el comportamiento, el aspecto o la funcionalidad de la tarjeta durante el tiempo de ejecución. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Buzón de entrada de mensajes

Las tarjetas de contenido pueden utilizarse para simular un centro de mensajes. En este formato, cada mensaje es su propia tarjeta que contiene [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que alimentan los eventos al hacer clic. Estos pares clave-valor son los identificadores clave en los que se fija la aplicación para decidir adónde ir cuando el usuario hace clic en un mensaje del buzón de entrada. Los valores de los pares clave-valor son arbitrarios. 

Aquí tienes un ejemplo de configuración del panel que podrías utilizar para crear dos tarjetas de mensajes: un mensaje es una llamada a la acción para que un usuario añada sus preferencias para recibir recomendaciones de lectura específicas, y otro proporciona un código de cupón a un segmento de nuevos suscriptores. 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps.png %}){: style="max-width:20%;float:right;margin-left:15px;border:0px;"}

Ejemplos de pares clave-valor para la tarjeta de recomendación de lectura podrían ser:

- body: Añade tus intereses a tu perfil del Semanario Politer para obtener recomendaciones personales de lectura.
- style: info
- class_type: notification_center
- card_priority: 1

Ejemplos de pares clave-valor para un nuevo cupón de suscriptor podrían ser:

- title: Suscribirse para juegos ilimitados
- body: Especial fin del verano - Disfruta de un 10 % de descuento en los juegos de Politer
- buttonText: Suscríbete ahora
- estilo: promo
- class_type: notification_center
- card_priority: 2
- términos: new_subscribers_only

Tus especialistas en marketing podrían hacer que esta tarjeta de contenido sólo estuviera disponible para un segmento de nuevos usuarios. 

Manejarías cada uno de los valores. Claves como `body`, `title`, y `buttonText` pueden tener simples valores de cadena que tus especialistas en marketing pueden establecer. Claves como `terms` pueden tener valores que proporcionen una pequeña colección de frases aprobadas por tu departamento Jurídico. Tú decidirías cómo representar `style` y `class_type` en tu aplicación o sitio web. 

{% details Más explicaciones para Android %}

En el SDK de Android y FireOS, la lógica del centro de mensajería se rige por el valor `class_type` que proporcionan los pares clave-valor de Braze. Con el método [`createContentCardable`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide) puedes filtrar e identificar estos tipos de clases.

{% tabs %}
{% tab Kotlin %}
**Utilizando `class_type` para el comportamiento al hacer clic**<br>
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
**Utilizando `class_type` para el comportamiento al hacer clic**<br>
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

Las tarjetas de contenido pueden configurarse en una fuente en carrusel en la que el usuario puede deslizar horizontalmente el dedo para ver más tarjetas destacadas. 

Para crear un carrusel de tarjetas de contenido, implementa una lógica que observe los [cambios en tus tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) y gestione la llegada de tarjetas de contenido. Por defecto, las tarjetas de contenido se ordenan por fecha de creación (la más reciente primero), y un usuario ve todas las tarjetas para las que es elegible. Implementa la lógica del lado del cliente para mostrar un número específico de tarjetas en el carrusel en un momento dado.

Dicho esto, podrías ordenar y aplicar lógica de visualización adicional de varias formas. Por ejemplo, podrías seleccionar los cinco primeros objetos de la tarjeta de contenido de la matriz o introducir pares clave-valor para construir una lógica condicional en torno a ellos.

Si estás implementando un carrusel como fuente secundaria de tarjetas de contenido, consulta [Personalizar la fuente predeterminada de tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) para aprender a ordenar las tarjetas en la fuente correcta en función de los pares clave-valor.

### Banner

Las tarjetas de contenido no tienen por qué parecer "tarjetas". Por ejemplo, las tarjetas de contenido pueden aparecer como un banner dinámico que se muestra de forma persistente en tu página de inicio o en la parte superior de las páginas designadas.

Para conseguirlo, tus especialistas en marketing crearán una campaña o paso en Canvas con una tarjeta de contenido de tipo **Sólo imagen**. A continuación, establece los pares clave-valor adecuados para utilizar [las tarjetas de contenido como contenido complementario]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).


