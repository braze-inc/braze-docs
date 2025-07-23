{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Exibição nativa de cartões de conteúdo {#unity-content-cards-native-ui}

Você pode exibir a interface do usuário padrão para os cartões de conteúdo usando a seguinte chamada:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Recebimento de dados do cartão de conteúdo no Unity

Você pode registrar objetos de jogo Unity para serem notificados sobre cartões de conteúdo. Recomendamos configurar os ouvintes de objetos de jogo no editor de configuração do Braze.

Se você precisar configurar o ouvinte do objeto do jogo em tempo de execução, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Note que, além disso, será necessário fazer uma chamada para `AppboyBinding.RequestContentCardsRefresh()` para começar a receber dados em seu ouvinte de objeto de jogo no iOS.

## Análise de cartões de conteúdo

As mensagens `string` recebidas em seu retorno de chamada de objeto de jogo de cartões de conteúdo podem ser analisadas em nosso objeto modelo [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) por conveniência.

A análise de cartões de conteúdo requer análise de JSON; consulte o exemplo a seguir para obter detalhes:

##### Exemplo de retorno de chamada dos cartões de conteúdo

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

## Atualizando os cartões de conteúdo

Para atualizar os cartões de conteúdo pela Braze, use um dos métodos a seguir:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Análise de dados

Os cliques e as impressões devem ser registrados manualmente para os cartões de conteúdo não exibidos diretamente pelo Braze.

Use `LogClick()` e `LogImpression()` no [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) para registrar cliques e impressões de cartões específicos.

