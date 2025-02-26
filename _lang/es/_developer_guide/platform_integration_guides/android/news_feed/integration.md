---
nav_title: Integración
article_title: Integración del canal de noticias para Android y FireOS
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre los diferentes tipos de tarjetas de canal de noticias, las diferentes propiedades específicas de las tarjetas disponibles y un ejemplo de integración personalizada para tu aplicación Android o FireOS."
channel:
  - news feed
  
---

# Integración de la fuente de noticias

> Este artículo de referencia cubre los diferentes tipos de tarjetas de canal de noticias, las diferentes propiedades específicas de las tarjetas disponibles y un ejemplo de integración personalizada para tu aplicación Android o FireOS.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

En Android, la fuente de noticias se implementa como un [fragmento](http://developer.android.com/guide/components/fragments.html) disponible en el proyecto Braze Android UI. Consulta [la documentación de Google sobre fragmentos](https://developer.android.com/guide/fragments#Adding "Documentación Android: Fragmentos") para obtener información sobre cómo añadir un fragmento a una actividad.

La clase `BrazeFeedFragment` actualizará y mostrará automáticamente el contenido de la fuente de noticias y registrará los análisis de uso. Las tarjetas que pueden aparecer en la fuente de noticias de un usuario se configuran en el panel de Braze.

## Tipos de tarjeta

Braze tiene cinco tipos de tarjetas únicas: imagen de banner, imagen con pie de foto, anuncio de texto y noticias breves. Cada tipo hereda propiedades comunes de un modelo base y tiene las siguientes propiedades adicionales.

### Propiedades del modelo de tarjeta base

El modelo de [tarjeta base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) proporciona un comportamiento básico para todas las tarjetas.  

|Propiedad|Descripción|
|---|---|
| `getId()` | Devuelve el ID de la tarjeta configurado por Braze. |
| `getViewed()` | Devuelve un booleano que refleja si la tarjeta ha sido leída o no por el usuario. |
| `getExtras()` | Devuelve un mapeado de pares clave-valor extras para esta tarjeta. |
| `setViewed(boolean)` | Configura el campo visto de una tarjeta. |
| `getCreated()` | Devuelve la marca de tiempo unix de la hora de creación de la tarjeta desde el panel de Braze. |
| `getUpdated()` | Devuelve la marca de tiempo unix de la última hora de actualización de la tarjeta desde el panel de Braze. |
| `getCategories()` | Devuelve la lista de categorías asignadas a la tarjeta, a las tarjetas sin categoría se les asignará `ABKCardCategoryNoCategory`. |
| `isInCategorySet(EnumSet)` | Devuelve verdadero si la tarjeta pertenece al conjunto de categorías dado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de imagen del banner

[Las tarjetas con imágenes de banner](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic.

|Propiedad|Descripción|
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP o HTTPS o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace para la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de imagen subtitulada

[Las tarjetas de imágenes con subtítulos](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) son imágenes a tamaño completo en las que se puede hacer clic y que van acompañadas de un texto descriptivo.

|Propiedad|Descripción|
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta.  Puede ser una URL HTTP o HTTPS o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de anuncio de texto (imagen subtitulada sin imagen)

[Las tarjetas de anuncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) son tarjetas en las que se puede hacer clic y que contienen un texto descriptivo.

|Propiedad|Descripción|
|---|---|
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP o HTTPS o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Propiedades de la tarjeta de noticias breves

[Las tarjetas de noticias breves](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) son tarjetas en las que se puede hacer clic con imágenes y texto descriptivo.

|Propiedad|Descripción|
|---|---|
| `getImageUrl()` | Devuelve la URL de la imagen de la tarjeta. |
| `getTitle()` | Devuelve el texto del título de la tarjeta. |
| `getDescription()` | Devuelve el texto del cuerpo de la tarjeta. |
| `getUrl()` | Devuelve la URL que se abrirá al hacer clic en la tarjeta. Puede ser una URL HTTP o HTTPS o una URL de protocolo. |
| `getDomain()` | Devuelve el texto del enlace de la URL de la propiedad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análisis de la sesión

Los fragmentos de la interfaz de usuario de Android no realizan un seguimiento automático de los análisis de sesión. Para asegurarte de que las sesiones se [siguen correctamente]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), llama a `IBraze.openSession()` cuando se abra tu aplicación.

## Enlaces

El enlace a la fuente de noticias desde un mensaje dentro de la aplicación debe habilitarse mediante el registro de `BrazeFeedActivity` dentro de tu `AndroidManifest.xml`.

## Integración personalizada de la fuente

Si quieres mostrar la fuente de forma totalmente personalizada, es posible hacerlo utilizando tus propias vistas pobladas con datos de nuestros modelos. Para obtener modelos de fuentes de noticias, tendrás que suscribirte a las actualizaciones de fuentes de noticias y utilizar los datos del modelo resultante para rellenar tus vistas. También tendrás que registrar los análisis de los objetos del modelo a medida que los usuarios interactúen con tus vistas.

### Parte 1: Suscribirse a las actualizaciones de la fuente

En primer lugar, declara una variable privada en tu clase de fuente personalizada para guardar tu suscriptor:

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

A continuación, añade el siguiente código para suscribirte a las actualizaciones de la fuente de Braze, normalmente dentro de la actividad de tu fuente personalizada `Activity.onCreate()`:

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

También te recomendamos cancelar suscripción cuando la actividad de tu fuente personalizada pase desapercibida. Añade el siguiente código al método del ciclo de vida `onDestroy()` de tu actividad:

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### Parte 2: Análisis de registros

Cuando utilices vistas personalizadas, tendrás que registrar los análisis manualmente, ya que los análisis sólo se gestionan automáticamente cuando se utilizan vistas Braze.

Para registrar una visualización de la fuente, llama a [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html).

Para registrar una impresión o hacer clic en una tarjeta, llama a [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) y [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivamente.

