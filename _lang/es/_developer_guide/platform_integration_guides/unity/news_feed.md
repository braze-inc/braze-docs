---
nav_title: Canal de noticias
article_title: Fuente de noticias de Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "Este artículo de referencia trata de la integración del canal de noticias en la plataforma Unity, como el análisis de tarjetas, la recepción de datos del canal de noticias y la analítica."

---

# Integración de la fuente de noticias

> Este artículo explica cómo configurar una fuente de noticias para la plataforma Unity.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Recepción de datos de fuentes de noticias en Unity

Puedes registrar objetos del juego Unity para que se te notifiquen las tarjetas de canal de noticias entrantes. 

En iOS, recomendamos configurar las escuchas del objeto del juego desde el editor de configuración de Braze.

En Android, configura `com_braze_feed_listener_callback_method_name` y `com_braze_feed_listener_game_object_name` en la página `braze.xml` de tu proyecto Unity.

Para configurar la escucha de tu objeto del juego en tiempo de ejecución en cualquiera de las plataformas, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.NEWS_FEED`.

## Análisis de tarjetas

Los mensajes entrantes de `string` recibidos en la devolución de llamada de tu objeto del juego se pueden analizar en nuestro objeto [Fuente](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs), que tiene una lista de objetos [Tarjeta](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) para mayor comodidad.

Para más detalles, consulta el siguiente ejemplo:

### Ejemplo de devolución de llamada

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## Actualizar el canal de noticias

Para actualizar la fuente de noticias de Braze, utiliza uno de los siguientes métodos:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Ambos métodos notificarán a tu oyente de la fuente de noticias y pasarán la fuente de noticias a tu método de devolución de llamada.

## Análisis

Los clics y las impresiones deben registrarse manualmente para las tarjetas que Braze no muestre directamente.

Utiliza `LogClick()` y `LogImpression()` en [Tarjeta](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) para registrar los clics y las impresiones de tarjetas concretas.

Para registrar que el usuario ha visto el canal en su totalidad, llama a `AppboyBinding.LogFeedDisplayed()`.

