---
nav_title: Crear tarjetas
article_title: Crear tarjetas de contenido
page_order: 0
description: "Este artículo cubre los componentes de la creación de una interfaz de usuario de tarjeta de contenido personalizada."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Crear tarjetas de contenido

> Este artículo analiza el enfoque básico que utilizarás al implementar tarjetas de contenido personalizadas, así como tres casos de uso comunes. Asume que ya has leído los demás artículos de la guía de personalización de la tarjeta de contenido para comprender qué se puede hacer de forma predeterminada y qué requiere código personalizado. Es especialmente útil saber cómo [registrar los análisis]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) de tus tarjetas de contenido personalizadas. 

## Crear una tarjeta

### Paso 1: Crea una interfaz de usuario personalizada 

{% tabs local %}
{% tab android %}

Primero, crea tu propio fragmento personalizado. El [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) predeterminado solo está diseñado para manejar nuestros tipos predeterminados de tarjetas de contenido, pero es un buen punto de partida.

{% endtab %}
{% tab swift %}

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

### Paso 4: Prueba tu tarjeta (opcional)

Para probar tu tarjeta de contenido:

1. Establece un usuario activo en tu aplicación llamando al método [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) método
2. En Braze, ve a **Campañas** y [crea una nueva campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. En tu campaña, selecciona **Prueba** y, a continuación, introduce la dirección `user-id` del usuario de prueba. Cuando estés listo, selecciona **Enviar prueba**. En breve podrás iniciar una tarjeta de contenido en tu dispositivo.

![Una campaña de tarjeta de contenido Braze que muestra que puedes añadir tu propio ID de usuario como destinatario de prueba para probar tu tarjeta de contenido.]({% image_buster /assets/img/react-native/content-card-test.png %} "Prueba de campaña de tarjeta de contenido")

## Colocación de tarjetas de contenido

Las tarjetas de contenido pueden utilizarse de muchas formas distintas. Tres implementaciones comunes son utilizarlos como centro de mensajes, anuncio de imagen dinámico o carrusel de imágenes. Para cada una de estas colocaciones, asignarás [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (la propiedad `extras` del modelo de datos) a tus tarjetas de contenido y, en función de los valores, ajustarás dinámicamente el comportamiento, el aspecto o la funcionalidad de la tarjeta durante el tiempo de ejecución. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Buzón de entrada de mensajes

Las tarjetas de contenido pueden utilizarse para simular un centro de mensajes. En este formato, cada mensaje es su propia tarjeta que contiene [pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) que alimentan los eventos al hacer clic. Estos pares clave-valor son los identificadores clave en los que se fija la aplicación para decidir adónde ir cuando el usuario hace clic en un mensaje del buzón de entrada. Los valores de los pares clave-valor son arbitrarios. 

#### Ejemplo

Por ejemplo, puedes querer crear dos tarjetas de mensajes: una llamada a la acción para que los usuarios habiliten las recomendaciones de lectura y un código de cupón que se entrega a tu nuevo segmento de suscriptores.

Claves como `body`, `title`, y `buttonText` pueden tener simples valores de cadena que tus especialistas en marketing pueden establecer. Claves como `terms` pueden tener valores que proporcionen una pequeña colección de frases aprobadas por tu departamento Jurídico. Claves como `style` y `class_type` tienen valores de cadena que puedes configurar para determinar cómo se muestra tu tarjeta en tu aplicación o sitio web.

{% tabs local %}
{% tab Recomendaciones de lectura %}
Pares clave-valor de la tarjeta de recomendación de lectura:

| Clave         | Valor                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Añade tus intereses a tu perfil del Semanario Politer para obtener recomendaciones personales de lectura. |
| `style`      | información                                                                 |
| `class_type` | centro_notificaciones                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Cupón de nuevo suscriptor %}
Pares clave-valor para un nuevo cupón de suscriptor:

| Clave         | Valor                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Suscribirse para juegos ilimitados                                    |
| `body`       | Especial fin del verano - Disfruta de un 10 % de descuento en los juegos de Politer              |
| `buttonText` | Suscríbete ahora                                                    |
| `style`      | promo                                                            |
| `class_type` | centro_notificaciones                                              |
| `card_priority` | 2                                                              |
| `terms`      | solo_nuevos_abonados                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Información adicional para Android %}

En el SDK de Android y FireOS, la lógica del centro de mensajería se rige por el valor `class_type` que proporcionan los pares clave-valor de Braze. Con el método [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/) puedes filtrar e identificar estos tipos de clases.

{% tabs local %}
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

Puedes configurar tarjetas de contenido en tu fuente de carrusel totalmente personalizada, permitiendo a los usuarios deslizar y ver tarjetas destacadas adicionales. Por defecto, las tarjetas de contenido se ordenan por fecha de creación (la más reciente primero), y tus usuarios verán todas las tarjetas para las que son elegibles.

Para implementar un carrusel de tarjetas de contenido:

1. Crea una lógica personalizada que observe los [cambios en tus tarjetas de]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) contenido y gestione la llegada de tarjetas de contenido.
2. Crea una lógica personalizada del lado del cliente para mostrar un número específico de tarjetas en el carrusel en cualquier momento. Por ejemplo, podrías seleccionar los cinco primeros objetos de la tarjeta de contenido de la matriz o introducir pares clave-valor para construir una lógica condicional en torno a ellos.

{% alert tip %}
Si estás implementando un carrusel como fuente secundaria de tarjetas de contenido, asegúrate de [ordenar las tarjetas en la fuente correcta utilizando pares clave-valor]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Sólo imagen

Las tarjetas de contenido no tienen por qué parecer "tarjetas". Por ejemplo, las tarjetas de contenido pueden aparecer como una imagen dinámica que se muestra de forma persistente en tu página de inicio o en la parte superior de las páginas designadas.

Para conseguirlo, tus especialistas en marketing crearán una campaña o paso en Canvas con una tarjeta de contenido de tipo **Sólo imagen**. A continuación, establece los pares clave-valor adecuados para utilizar [las tarjetas de contenido como contenido complementario]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).
