## Acerca de las tarjetas de contenido React Native

Los SDK de Braze incluyen una fuente de tarjetas predeterminada para que empieces a utilizar las tarjetas de contenido. Para mostrar la fuente de la tarjeta, puedes utilizar el método `Braze.launchContentCards()`. La fuente predeterminada de tarjetas incluida en el SDK de Braze gestionará todos los análisis de seguimiento, descarte de tarjetas y representación de las tarjetas de contenido de un usuario.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Métodos de tarjetas

Para construir tu propia interfaz de usuario, puedes obtener una lista de las tarjetas disponibles y escuchar las actualizaciones de las tarjetas:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Si decides crear tu propia interfaz de usuario para mostrar las tarjetas, debes llamar a `logContentCardImpression` para recibir los análisis de esas tarjetas. Esto incluye las tarjetas `control`, que deben ser objeto de seguimiento aunque no se muestren al usuario.
{% endalert %}

Puedes utilizar estos métodos adicionales para crear una fuente personalizada de tarjetas de contenido dentro de tu aplicación:

| Método                                   | Descripción                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Lanza el elemento de interfaz de usuario Tarjetas de contenido.                                                                 |
| `requestContentCardsRefresh()`           | Solicita las últimas tarjetas de contenido al servidor SDK de Braze. La lista de tarjetas resultante se pasa a cada uno de los [oyentes de eventos de tarjeta de contenido](#reactnative_cards-methods) previamente registrados. |
| `getContentCards()`                      | Recupera tarjetas de contenido del SDK Braze. Devuelve una promesa que se resuelve con la última lista de tarjetas del servidor. |
| `getCachedContentCards()`                | Devuelve la matriz de tarjetas de contenido más reciente de la caché.                                            |
| `logContentCardClicked(cardId)`          | Registra un clic para el ID de tarjeta de contenido dado. Este método sólo se utiliza para análisis. Para ejecutar la acción clic, llama además a `processContentCardClickAction(cardId)`.                                                        |
| `logContentCardImpression(cardId)`       | Registra una impresión para el ID de tarjeta de contenido dado.                                                      |
| `logContentCardDismissed(cardId)`        | Registra un descarte para el ID de tarjeta de contenido dado.                                                        |
| `processContentCardClickAction(cardId)`  | Realiza la acción de una tarjeta concreta.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tipos de tarjeta y propiedades

El modelo de datos de tarjetas de contenido está disponible en el SDK de React Native y ofrece los siguientes tipos de tarjeta de tarjetas de contenido: [Sólo imagen](#image-only), [Imagen con subtítulos](#captioned-image) y [Clásico](#classic). También hay un tipo especial de tarjeta de [Control](#control), que se devuelve a los usuarios que están en el grupo de control de una tarjeta determinada. Cada tipo hereda propiedades comunes de un modelo base, además de sus propias propiedades únicas.

{% alert tip %}
Para una referencia completa del modelo de datos de la tarjeta de contenido, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).
{% endalert %}

### Modelo de tarjeta base

El modelo de tarjeta base proporciona un comportamiento básico para todas las tarjetas.

|Propiedad      | Descripción                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | El ID de la tarjeta configurado por Braze.                                                                                            |
|`created`     | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze.                                                             |
|`expiresAt`   | La fecha UNIX de caducidad de la tarjeta. Cuando el valor es inferior a 0, significa que la tarjeta no caduca nunca.      |
|`viewed`      | Si el usuario ha leído o no la tarjeta. Esto no registra análisis.                                           |
|`clicked`     | Si el usuario ha hecho clic en la tarjeta.                                                                         |
|`pinned`      | Si la tarjeta está anclada.                                                                                            |
|`dismissed`   | Si el usuario ha descartado esta tarjeta. Marcar como descartada una tarjeta que ya ha sido descartada será un no-op. |
|`dismissible` | Si la tarjeta es descartable por el usuario.                                                                           |
|`url`         | (Opcional) La cadena de URL asociada a la acción de clic en la tarjeta.                                                       |
|`openURLInWebView` | Si las URL de esta tarjeta deben abrirse en la Vista Web de Braze o no.                                            |
|`isControl`   | Si esta tarjeta es una tarjeta de control. Las tarjetas de control no deben mostrarse al usuario.                                |
|`extras`      | El mapa de extras clave-valor de esta tarjeta.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta base, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Solo imagen

Las tarjetas de sólo imagen son imágenes de tamaño completo en las que se puede hacer clic.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | El tipo de tarjeta de contenido, `IMAGE_ONLY`.                                                                              |
|`image`            | La URL de la imagen de la tarjeta.                                                                                      |
|`imageAspectRatio` | La relación de aspecto de la imagen de la tarjeta. Sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta de sólo imagen, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct).

### Imagen subtitulada

Las tarjetas de imágenes con subtítulos son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | El tipo de tarjeta de contenido, `CAPTIONED`.                                                                               |
|`image`            | La URL de la imagen de la tarjeta.                                                                                      |
|`imageAspectRatio` | La relación de aspecto de la imagen de la tarjeta. Sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
|`title`            | El texto del título de la tarjeta.                                                                                      |
|`cardDescription`  | El texto descriptivo de la tarjeta.                                                                                |
|`domain`           | (Opcional) El texto del enlace para la URL de la propiedad, por ejemplo, `"braze.com/resources/"`. Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción/dirección de hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta de imagen subtitulada, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Clásica

Las tarjetas clásicas tienen un título, una descripción y una imagen opcional a la izquierda del texto.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | El tipo de tarjeta de contenido, `CLASSIC`.                                                                                 |
|`image`            | (Opcional) La URL de la imagen de la tarjeta.                                                                           |
|`title`            | El texto del título de la tarjeta.                                                                                      |
|`cardDescription`  | El texto descriptivo de la tarjeta.                                                                                |
|`domain`           | (Opcional) El texto del enlace para la URL de la propiedad, por ejemplo, `"braze.com/resources/"`. Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción/dirección de hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta de contenido clásica (anuncio de texto), consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para la tarjeta de imagen clásica (noticias breves), consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Control

Las tarjetas de control incluyen todas las propiedades básicas, con algunas diferencias importantes. Y lo que es más importante:

- La propiedad `isControl` está garantizada en `true`.
- Se garantiza que la propiedad `extras` está vacía.

Para una referencia completa de la tarjeta de control, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct).
