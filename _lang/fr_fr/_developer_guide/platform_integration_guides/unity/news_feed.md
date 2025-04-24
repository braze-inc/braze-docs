---
nav_title: Fil d’actualité
article_title: Fil d’actualité de Unity
channel: news feed
platform: 
  - Unity
  - iOS
  - Android
page_order: 5
description: "Cet article de référence couvre l’intégration du fil d’actualité pour la plateforme Unity, comme l’analyse des cartes, la réception des données du fil d’actualité et les analyses."

---

# Intégration du fil d’actualité

> Cet article explique comment configurer un fil d’actualité pour la plateforme Unity.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Réception des données du fil d’actualités dans Unity

Vous pouvez lister des objets de jeu Unity pour être avertis des cartes de fil d’actualités entrantes. 

Sur iOS, nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze.

Sur Android, définir `com_braze_feed_listener_callback_method_name` et `com_braze_feed_listener_game_object_name` dans votre projet Unity `braze.xml`.

Pour configurer votre auditeur d’objet de jeu à l’exécution sur l’une ou l’autre plateforme, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.NEWS_FEED`.

## Cartes d’analyse

Les messages de type `string` entrants reçus dans votre rappel d’objet de jeu peuvent être analysés dans notre objet [Flux](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Feed.cs) pré-défini, lequel contient une liste d’objets [Carte](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) pour plus de commodité.

Pour plus de détails, consultez l’exemple suivant :

### Exemple de fonction de rappel

```csharp
void FeedReceivedCallback(string message) {
  Feed feed = new Feed(message);
  Debug.Log("Feed received: " + feed);
  foreach (Card card in feed.Cards) {
    Debug.Log("Card: " + card);
  }
}
```

## Actualisation du fil d’actualités

Pour actualiser le fil d’actualité à partir de Braze, utilisez l’une des méthodes suivantes :

```csharp
// results in a network request to Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Les deux méthodes informeront votre auditeur de fil d’actualités et transmettront le fil d’actualités à votre méthode de rappel.

## Analyse

Les clics et les impressions doivent être enregistrés manuellement pour les cartes qui ne sont pas affichées directement par Braze.

Utilisez `LogClick()` et `LogImpression()` on [Card](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/Card.cs) pour enregistrer les clics et les impressions pour des cartes spécifiques.

Pour consigner que l’utilisateur a consulté le flux dans son ensemble, appelez `AppboyBinding.LogFeedDisplayed()`.

