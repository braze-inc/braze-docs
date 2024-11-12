---
nav_title: Tarjetas de contenido
article_title: Tarjetas de contenido para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
channel: content cards
page_order: 3
description: "En este artículo de referencia se cubren las directrices de implementación de la tarjeta de contenido para la plataforma Xamarin."

---

# Integración de la tarjeta de contenido

> Aprende a configurar tarjetas de contenido de iOS, Android y FireOS para la plataforma Xamarin.

El SDK de Braze incluye una fuente de tarjetas predeterminada para que empieces a utilizar las tarjetas de contenido. La fuente predeterminada de tarjetas incluida en el SDK de Braze gestionará todos los análisis de seguimiento, descarte de tarjetas y representación de las tarjetas de contenido de un usuario.

Para obtener información sobre cómo integrar las tarjetas de contenido en tu aplicación Xamarin, consulta nuestra [guía de integración en Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) y nuestra [guía de integración en iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/).

## Requisitos previos

Para utilizar esta característica, tendrás que [integrar Braze SDK para la plataforma Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Métodos de la tarjeta de contenido

Puedes utilizar estos métodos adicionales para crear una fuente personalizada de tarjetas de contenido dentro de tu aplicación:

| Método                                   | Descripción                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Solicita las últimas tarjetas de contenido al servidor SDK de Braze.                                           |
| `getContentCards()`                      | Recupera tarjetas de contenido del SDK Braze. Esto devolverá la última lista de tarjetas del servidor. |
| `logContentCardClicked(cardId)`          | Registra un clic para el ID de tarjeta de contenido dado. Este método sólo se utiliza para análisis.                    |
| `logContentCardImpression(cardId)`       | Registra una impresión para el ID de tarjeta de contenido dado.                                                      |
| `logContentCardDismissed(cardId)`        | Registra un descarte para el ID de tarjeta de contenido dado.                                                        |

## Modelo de datos de la tarjeta de contenido

El SDK de Xamarin Braze tiene tres tipos únicos de tarjetas de contenido que comparten un modelo base: **banner**, **imagen subtitulada** y **clásica**. Cada tipo hereda propiedades comunes de un modelo base y tiene las siguientes propiedades adicionales.

### Propiedades del modelo de tarjeta de contenido base

|Propiedad           | Descripción                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | El ID de la tarjeta configurado por Braze.                                                                                            |
|`created`          | La marca de tiempo UNIX de la hora de creación de la tarjeta desde Braze.                                                             |
|`expiresAt`        | La fecha UNIX de caducidad de la tarjeta. Cuando el valor es inferior a 0, significa que la tarjeta no caduca nunca.      |
|`viewed`           | Si el usuario ha leído o no la tarjeta. Esto no registra análisis.                                           |
|`clicked`          | Si el usuario ha hecho clic en la tarjeta.                                                                         |
|`pinned`           | Si la tarjeta está anclada.                                                                                            |
|`dismissed`        | Si el usuario ha descartado esta tarjeta. Marcar como descartada una tarjeta que ya ha sido descartada será un no-op. |
|`dismissible`      | Si la tarjeta es descartable por el usuario.                                                                           |
|`urlString`        | (Opcional) La cadena url asociada a la acción de clic en la tarjeta.                                                       |
|`openUrlInWebView` | Si las URL de esta tarjeta deben abrirse en la WebView de Braze o no.                                                 |
|`isControlCard`    | Si esta tarjeta es una tarjeta de control. Las tarjetas de control no deben mostrarse al usuario.                                |
|`extras`           | El mapa de extras clave-valor de esta tarjeta.                                                                             |
|`isTest`           | Si esta tarjeta es una tarjeta de prueba.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta base, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Propiedades del modelo de tarjeta de contenido de banner

Las tarjetas banner son imágenes de tamaño completo en las que se puede hacer clic.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | La URL de la imagen de la tarjeta.                                                                                      |
|`imageAspectRatio` | La relación de aspecto de la imagen de la tarjeta. Sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta banner, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (ahora renombrada a sólo imagen).

### Imagen subtitulada Propiedades del modelo de tarjeta de contenido

Las tarjetas de imágenes con subtítulos son imágenes de tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | La URL de la imagen de la tarjeta.                                                                                      |
|`imageAspectRatio` | La relación de aspecto de la imagen de la tarjeta. Sirve como pista antes de que se complete la carga de la imagen. Ten en cuenta que la propiedad puede no suministrarse en determinadas circunstancias. |
|`title`            | El texto del título de la tarjeta.                                                                                      |
|`cardDescription`  | El texto descriptivo de la tarjeta.                                                                                |
|`domain`           | (Opcional) El texto del enlace para la URL de la propiedad, por ejemplo, `"braze.com/resources/"`. Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción/dirección de hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta de imagen subtitulada, consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Propiedades del modelo de tarjeta de contenido clásica

Las tarjetas clásicas tienen un título, una descripción y una imagen opcional a la izquierda del texto.

|Propiedad           | Descripción                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Opcional) La URL de la imagen de la tarjeta.                                                                           |
|`title`            | El texto del título de la tarjeta.                                                                                      |
|`cardDescription`  | El texto descriptivo de la tarjeta.                                                                                |
|`domain`           | (Opcional) El texto del enlace para la URL de la propiedad, por ejemplo, `"braze.com/resources/"`. Se puede mostrar en la interfaz de usuario de la tarjeta para indicar la acción/dirección de hacer clic en la tarjeta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para una referencia completa de la tarjeta de contenido clásica (anuncio de texto), consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para una referencia completa de la tarjeta de imagen clásica (noticias breves), consulta la documentación de [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}

