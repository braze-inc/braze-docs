{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Mostrar tarjetas de contenido de forma nativa {#unity-content-cards-native-ui}

Puedes mostrar la IU predeterminada para las tarjetas de contenido utilizando la siguiente llamada:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Recepción de datos de la tarjeta de contenido en Unity

Puedes registrar objetos del juego Unity para que se te notifique la llegada de tarjetas de contenido. Recomendamos configurar los oyentes del objeto del juego desde el editor de configuración de Braze.

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Nota, además tendrás que hacer una llamada a `AppboyBinding.RequestContentCardsRefresh()` para empezar a recibir datos en tu receptor de objetos del juego en iOS.

## Análisis sintáctico de tarjetas de contenido

Los mensajes entrantes de `string` recibidos en tu devolución de llamada al objeto del juego Tarjetas de contenido pueden analizarse en nuestro [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) para mayor comodidad.

El análisis de las tarjetas de contenido requiere el análisis JSON, consulta el siguiente ejemplo para obtener más detalles:

##### Ejemplo de devolución de llamada de tarjetas de contenido

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object 
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

## Actualizar tarjetas de contenido

Para actualizar las tarjetas de contenido desde Braze, llama a cualquiera de los siguientes métodos:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Análisis

Los clics y las impresiones deben registrarse manualmente para las tarjetas de contenido no mostradas directamente por Braze.

Utiliza `LogClick()` y `LogImpression()` en [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) para registrar los clics y las impresiones de tarjetas concretas.

