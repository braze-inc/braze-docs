---
nav_title: Feed de notícias
article_title: Feed de notícias do Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "Este artigo de referência aborda a integração do feed de notícias para a plataforma Unity, como a análise de cartões, o recebimento de dados do feed de notícias e análises."

---

# Integração do Feed de notícias

> Este artigo aborda como configurar um feed de notícias para a plataforma Unity.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Recebendo dados do feed de notícias no Unity

É possível registrar objetos de jogo Unity para serem notificados sobre a entrada de cartões do Feed de notícias. 

No iOS, recomendamos definir os ouvintes de objetos de jogo no editor de configuração da Braze.

No Android, defina `com_braze_feed_listener_callback_method_name` e `com_braze_feed_listener_game_object_name` no endereço `braze.xml` de seu projeto Unity.

Para configurar seu ouvinte de objeto de jogo em tempo de execução em qualquer plataforma, use `AppboyBinding.ConfigureListener()` e especifique `BrazeUnityMessageType.NEWS_FEED`.

## Análise de cartões

As mensagens `string` recebidas em seu retorno de chamada de objeto de jogo podem ser analisadas em nosso objeto [Feed](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs) pré-fornecido, que tem uma lista de objetos [de cartão](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) por conveniência.

Veja o exemplo a seguir para obter detalhes:

### Exemplo de retorno de chamada

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## Atualizando o feed de notícias

Para atualizar o feed de notícias da Braze, use um dos métodos a seguir:

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Ambos os métodos notificarão seu ouvinte do Feed de notícias e passarão o Feed de notícias para seu método de retorno de chamada.

## Análise de dados

Os cliques e impressões devem ser registrados manualmente para cartões não exibidos diretamente pelo Braze.

Use `LogClick()` e `LogImpression()` on [Card](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) para registrar cliques e impressões para cartões específicos.

Para registrar que o usuário visualizou o feed como um todo, chame `AppboyBinding.LogFeedDisplayed()`.

