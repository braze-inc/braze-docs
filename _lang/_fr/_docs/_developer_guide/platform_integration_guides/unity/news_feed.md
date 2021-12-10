---
nav_title: Flux d'actualité
article_title: Flux d'actualité pour l'unité
channel: fil d'actualité
platform:
  - Unité
  - iOS
  - Android
page_order: 5
description: "Cet article de référence couvre l'intégration des flux de nouvelles pour la plate-forme Unity."
---

# Flux d'actualité

## Réception des données du flux d'actualités dans l'unité

Vous pouvez enregistrer des objets Unity Game pour être averti des cartes de flux de nouvelles entrantes.

Sur iOS, nous vous recommandons de configurer les écouteurs d'objets du jeu à partir de l'éditeur de configuration de Braze.

Sur Android, définissez `com_appboy_feed_listener_callback_method_name` et `com_appboy_feed_listener_game_object_name` dans le `braze.xml` de votre projet Unity.

- Pour configurer votre écouteur d'objet de jeu lors de l'exécution sur l'une ou l'autre des plateformes, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.NEWS_FEED`.

## Analyse des cartes

Les messages entrants `string` reçus dans la fonction de rappel de votre objet de jeu peuvent être analysés dans notre objet [Feed][11] pré-fourni, qui a une liste d'objets [Carte][12] pour plus de commodité.

Voir l'exemple suivant pour plus de détails:

### Example callback

```csharp
void FeedReceivedCallback(message de chaîne) {
  Feed feed = new Feed(message);
  Debug. og("Flux reçu: " + feed);
  foreach (Card card in feed. ards) {
    Debug.Log("Fiche : " + carte);
  }
}
```

## Actualisation du flux d'actualités

Pour actualiser le flux d'actualités du Brésil, appelez l'une des méthodes suivantes :

```csharp
// aboutit à une requête de réseau à Braze
AppboyBinding.RequestFeedRefresh()

AppboyBinding.RequestFeedRefreshFromCache()
```

Les deux méthodes avertiront votre auditeur de flux d'actualités et transmettront le fil d'actualité à votre méthode de rappel.

## Analyses

Les clics et les impressions doivent être enregistrés manuellement pour les cartes qui ne sont pas affichées directement par Braze.

Utilisez `LogClick()` et `LogImpression()` sur [Carte][12] pour enregistrer les clics et les impressions pour des cartes spécifiques.

Pour enregistrer que l'utilisateur a vu le flux dans son ensemble, appelez `AppboyBinding.LogFeedDisplayed()`.

[11]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Feed.cs
[12]: https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/models/Cards/Card.cs
