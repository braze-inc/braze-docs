---
nav_title: Cartes de contenu
article_title: Cartes de contenu pour Unity
platform: 
  - Unity
  - iOS
  - Android
channel: content cards
page_order: 4
description: "Cet article de référence couvre les directives d’implémentation des cartes de contenu pour la plateforme Unity comme l’affichage des cartes, des cartes d’analyse et les analyses."

---

# Intégration d’une carte de contenu

> Cet article de référence couvre les directives d’implémentation des cartes de contenu pour la plateforme Unity comme l’affichage des cartes, des cartes d’analyse et les analyses.

## Affichage natif des cartes de contenu {#unity-content-cards-native-ui}

Vous pouvez afficher l’interface utilisateur par défaut pour les cartes de contenu à l’aide de l’appel suivant :

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Réception des données de carte de contenu dans Unity

Vous pouvez lister des objets de jeu Unity pour être avertis des cartes de contenu entrantes. Nous recommandons de définir des auditeurs d’objets de jeu à partir de l’éditeur de configuration Braze.

Si vous devez configurer votre auditeur d’objet de jeu lors de l’exécution, utilisez `AppboyBinding.ConfigureListener()` et spécifiez `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Notez que vous devrez également appeler `AppboyBinding.RequestContentCardsRefresh()` pour commencer à recevoir des données dans votre auditeur d’objet de jeu sur iOS.

## Analyse des cartes de contenu

Les messages de type `string` entrants reçus dans votre rappel d’objet de jeu de cartes de contenu peuvent être analysés dans notre objet de modèle [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) pré-fourni pour plus de commodité.

L’analyse des cartes de contenu nécessite l’analyse Json, consultez l’exemple suivant pour plus de détails :

##### Exemple de fonction de rappel des cartes de contenu

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

## Rafraîchir les cartes de contenu

Pour actualiser les cartes de contenu de Braze, appelez l’une des méthodes suivantes :

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Support GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}

## Analyse

Les clics et les impressions doivent être enregistrés manuellement pour les cartes de contenu non affichées directement par Braze.

Utilisez `LogClick()` et `LogImpression()` sur [Contentcardable](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) pour enregistrer les clics et les impressions pour des cartes spécifiques.

